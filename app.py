from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import ml_model
import uuid
import json
import os
from datetime import datetime, timedelta

from role_skills import ROLE_SKILLS, SKILL_KEYWORDS, SKILL_LEARNING_WEEKS, SKILL_IMPACT_WEIGHTS
from quiz_bank import QUIZ_QUESTIONS, QUIZ_TOPICS
from roadmap_data import ROADMAP_DATA

import analysis_engine
import recommendation_engine
import chart_generator

app = Flask(__name__)
app.secret_key = 'adaptive-ai-secret-key-2026'

# Persistent storage file
DATA_FILE = 'user_data.json'
USER_STORE = {}

def load_user_data():
    global USER_STORE
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                USER_STORE = json.load(f)
        except Exception as e:
            print(f"Error loading user data: {e}")
            USER_STORE = {}

def save_user_data():
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(USER_STORE, f, indent=4)
    except Exception as e:
        print(f"Error saving user data: {e}")

load_user_data()

def add_notification(storage_key, text, n_type='info'):
    """Adds a notification to the user store with duplicate prevention."""
    if storage_key not in USER_STORE:
        return
    
    # Duplicate prevention: Check if same text was added recently (last 5 mins)
    now = datetime.now()
    five_mins_ago = (now - timedelta(minutes=5)).timestamp()
    
    for n in USER_STORE[storage_key].get('notifications', []):
        try:
            n_time = datetime.strptime(n['timestamp'], '%Y-%m-%d %H:%M:%S').timestamp()
            if n['text'] == text and n_time > five_mins_ago:
                return # Skip duplicate
        except:
            continue

    notification = {
        'id': str(uuid.uuid4()),
        'text': text,
        'type': n_type,
        'read': False,
        'timestamp': now.strftime('%H:%M, %b %d')
    }
    
    if 'notifications' not in USER_STORE[storage_key]:
        USER_STORE[storage_key]['notifications'] = []
        
    USER_STORE[storage_key]['notifications'].insert(0, notification)
    # Keep only last 20
    USER_STORE[storage_key]['notifications'] = USER_STORE[storage_key]['notifications'][:20]
    save_user_data()

def generate_readiness_prediction(current_score, missing_skills, target_role):
    """Predicts non-linear future career readiness growth based on skill importance."""
    timeline = []
    
    # Starting point
    timeline.append({
        'date': 'Present',
        'score': current_score,
        'reason': 'Current technical baseline.'
    })
    
    if not missing_skills:
        # If already ready, show maintenance or advanced growth
        timeline.append({'date': 'Month 1', 'score': 99, 'reason': 'Advanced specialization.'})
        return timeline
        
    # Get weights for the specific role
    role_weights = SKILL_IMPACT_WEIGHTS.get(target_role, {})
        
    # Sort missing skills by impact weight for a logical learning progression
    missing_skills_sorted = sorted(missing_skills, key=lambda x: role_weights.get(x, 5), reverse=True)
    
    cumulative_weeks = 0
    current_proj_score = current_score
    target_max = 98
    score_gap = target_max - current_score
    
    total_weight = sum(role_weights.get(s, 5) for s in missing_skills)
    if total_weight == 0: total_weight = 1
    
    for skill in missing_skills_sorted:
        weeks = SKILL_LEARNING_WEEKS.get(skill, 2)
        cumulative_weeks += weeks
        
        # Growth depends on the weight of the skill
        weight = role_weights.get(skill, 5)
        # Add non-linear jump based on weight
        gain = (weight / total_weight) * score_gap
        current_proj_score += gain
        
        # Label logic
        if cumulative_weeks <= 6:
            label = f"Week {cumulative_weeks}"
        else:
            months = cumulative_weeks // 4
            rem_weeks = cumulative_weeks % 4
            label = f"Month {months}" if rem_weeks == 0 else f"Month {months}, Wk {rem_weeks}"
            
        # Context-aware reasoning
        reason = f"Learning {skill} creates a significant readiness spike."
        if weight >= 9:
            reason = f"Mastering {skill} is a high-impact milestone for {target_role} roles."
        elif weight <= 5:
            reason = f"Acquiring {skill} rounds out your supporting technical toolkit."
            
        timeline.append({
            'date': label,
            'score': min(98, int(current_proj_score)),
            'reason': reason
        })
    
    return timeline

def generate_career_tips(target_role, missing_skills):
    """Generates intelligent, role-specific AI Career Tips."""
    role_tips = {
        'AI Engineer': [
            "Mastering Deep Learning and LLMs will create the biggest jump in your AI readiness.",
            "Your AI career growth accelerates after mastering PyTorch or TensorFlow."
        ],
        'Cloud Engineer': [
            "Kubernetes and Terraform are the highest-impact skills for cloud deployment readiness.",
            "Automating infrastructure creates a competitive edge in DevOps roles."
        ],
        'Web Developer': [
            "Full-stack proficiency requires bridging the gap between React UIs and Node.js backends.",
            "Mastering APIs and MongoDB is essential for building data-driven applications."
        ],
        'Cyber Security': [
            "Advanced Networking and Ethical Hacking are your primary defense vectors.",
            "SIEM and Threat Analysis skills are mandatory for enterprise SOC roles."
        ],
        'Data Scientist': [
            "Focus on Machine Learning and Statistics to unlock predictive analysis capabilities.",
            "Pandas and SQL are the foundation for any professional data engineering pipeline."
        ],
        'Software Developer': [
            "DSA and Problem Solving are the most critical features for passing technical interviews.",
            "System Design and OOP mastery differentiate senior engineers from juniors."
        ]
    }
    
    base_tips = role_tips.get(target_role, ["Focus on mastering core fundamentals to build a solid foundation."])
    
    # Dynamic prioritization based on missing skills
    critical_missing = [s for s in missing_skills if SKILL_IMPACT_WEIGHTS.get(s, 0) >= 9]
    
    final_tips = []
    if critical_missing:
        final_tips.append(f"Prioritize {critical_missing[0]}; it is the most critical gap in your current profile.")
        
    final_tips.extend(base_tips)
    return final_tips[:3]

@app.before_request
def ensure_session():
    if 'uid' not in session:
        session['uid'] = str(uuid.uuid4())
    
    # Use email as key if logged in for persistence across devices/sessions
    user_email = session.get('user', {}).get('email')
    storage_key = user_email if user_email else session['uid']
    
    if storage_key not in USER_STORE:
        USER_STORE[storage_key] = {
            'target_role': 'Not Selected',
            'entered_skills': '',
            'last_analysis': None,
            'past_analyses': [], # Store historical snapshots
            'quiz_history': [],
            'analysis_history': [], # Prediction curve
            'career_tips': [],
            'completed_skills': {}, # Role -> list of manually completed skills
            'notifications': [], # List of notification objects
            'stats': {
                'streak': 1,
                'last_activity': datetime.now().strftime('%Y-%m-%d'),
                'roadmap_completion': 0,
                'quiz_accuracy': 0
            }
        }
        add_notification(storage_key, "Welcome to Adaptive AI! Start by selecting a role and analyzing your skills.", "ai_recommendation")
    else:
        # Migration: Add missing keys for existing users
        if 'notifications' not in USER_STORE[storage_key]:
            USER_STORE[storage_key]['notifications'] = []
            add_notification(storage_key, "AI Notification System activated. We'll keep you updated on your career progress!", "ai_recommendation")
        if 'stats' not in USER_STORE[storage_key]:
            USER_STORE[storage_key]['stats'] = {
                'streak': 1,
                'last_activity': datetime.now().strftime('%Y-%m-%d'),
                'roadmap_completion': 0,
                'quiz_accuracy': 0
            }
    
    # Update session UID if we switched to email to ensure current requests use the right data
    session['storage_key'] = storage_key

@app.before_request
def before_request():
    """Initializes session and user data before every request."""
    # Skip for static files
    if request.path.startswith('/static'):
        return
    ensure_session()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth')
def auth():
    return render_template('auth.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email', '')
    name = request.form.get('name', '')
    if not name:
        name = email.split('@')[0] if email else 'User'
    
    # Migrate guest data to email key if they just logged in
    old_key = session.get('storage_key')
    if old_key and old_key in USER_STORE and email and old_key != email:
        # If email already exists, we might want to merge, but for now we just switch
        if email not in USER_STORE:
            USER_STORE[email] = USER_STORE.pop(old_key)
        else:
            # Transfer history if new email key was empty
            if not USER_STORE[email]['quiz_history']:
                USER_STORE[email] = USER_STORE.pop(old_key)
            else:
                USER_STORE.pop(old_key) # Just drop guest data if email already has data
    
    save_user_data()
    session['user'] = {'name': name, 'email': email, 'logged_in': True}
    return redirect(url_for('dashboard'))

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name', 'User')
    email = request.form.get('email')
    
    # Migrate guest data to email key
    old_key = session.get('storage_key')
    if old_key and old_key in USER_STORE and email and old_key != email:
        if email not in USER_STORE:
            USER_STORE[email] = USER_STORE.pop(old_key)
        else:
            # Transfer history if new email key was empty
            if not USER_STORE[email].get('quiz_history'):
                USER_STORE[email] = USER_STORE.pop(old_key)
            else:
                USER_STORE.pop(old_key) # Just drop guest data if email already has data
    
    save_user_data()
    session['user'] = {'name': name, 'email': email, 'logged_in': True}
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    user = session.get('user', {'name': 'Guest', 'email': '', 'logged_in': False})
    user_data = USER_STORE[session['storage_key']]
    target_role = user_data['target_role']
    analysis = user_data['last_analysis']
    
    # Calculate counts for dashboard summary
    matched_count = len(analysis.get('detected_skills', [])) if analysis else 0
    missing_count = len(analysis.get('missing_skills', [])) if analysis else 0
    total_skills = len(analysis.get('skill_names', [])) if analysis else 0
    
    # Tracking Stats
    completed_list = user_data['completed_skills'].get(target_role, [])
    tracking_stats = {
        'completed': matched_count,
        'in_progress': 1 if missing_count > 0 else 0,
        'remaining': missing_count,
        'velocity': 'High' if len(completed_list) > 1 else 'Normal',
        'next_skill': analysis['missing_skills'][0] if analysis and analysis['missing_skills'] else 'None'
    }
    
    chart_data = chart_generator.get_dashboard_chart_data(target_role, analysis)
    
    return render_template('dashboard.html', 
                           user=user, 
                           analysis=analysis, 
                           target_role=target_role,
                           tracking_stats=tracking_stats,
                           chart_data=chart_data,
                           analysis_history=user_data.get('analysis_history', []),
                           quiz_history=user_data.get('quiz_history', []),
                           total_skills=total_skills,
                           career_tips=user_data.get('career_tips', []))

@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    user = session.get('user', {'name': 'Guest'})
    user_data = USER_STORE[session['storage_key']]
    
    if request.method == 'POST':
        target_role = request.form.get('target_role', 'Data Scientist')
        user_data['target_role'] = target_role
        skills_text = request.form.get('current_skills', '').lower()
        user_data['entered_skills'] = skills_text
        
        # 1. Analyze Skills using Engine
        user_skills_scores, relevant_skills, detected_skills, missing_skills = analysis_engine.analyze_skills(target_role, skills_text)
        
        # Merge with manually completed skills
        completed_for_role = user_data['completed_skills'].get(target_role, [])
        for skill in completed_for_role:
            if skill not in detected_skills:
                detected_skills.append(skill)
                user_skills_scores[skill] = 95 # Assume 95% mastery if completed
            if skill in missing_skills:
                missing_skills.remove(skill)
        
        # 2. Get AI Recommendation
        result = recommendation_engine.train_and_predict(target_role, user_skills_scores, relevant_skills, detected_skills, missing_skills)
        
        # 3. Assemble Result
        result['target_role'] = target_role
        result['user_skills_data'] = user_skills_scores
        result['skill_names'] = relevant_skills
        result['detected_skills'] = detected_skills
        result['missing_skills'] = missing_skills
        
        result['match_score'] = result.get('match_score', 0)
        result['gap_score'] = 100 - result['match_score']
        
        # Store in session via USER_STORE
        user_data['last_analysis'] = result
        
        # Add to past analyses for history (keep at least 10)
        history_entry = {
            'date': datetime.now().strftime('%b %d, %Y - %H:%M'),
            'role': target_role,
            'score': result['match_score'],
            'skills': result['detected_skills']
        }
        user_data['past_analyses'].insert(0, history_entry)
        user_data['past_analyses'] = user_data['past_analyses'][:10]
        
        # Generate FUTURE prediction timeline
        user_data['analysis_history'] = generate_readiness_prediction(
            result['match_score'], 
            missing_skills, 
            target_role
        )

        # Generate AI Career Tips
        user_data['career_tips'] = generate_career_tips(target_role, missing_skills)
        
        # TRIGGER NOTIFICATIONS
        if missing_skills:
            high_impact = [s for s in missing_skills if SKILL_IMPACT_WEIGHTS.get(s, 0) >= 9]
            if high_impact:
                add_notification(session['storage_key'], f"High Impact Alert: Learning {high_impact[0]} can boost your readiness by ~15%!", "ai_recommendation")
        
        add_notification(session['storage_key'], f"Skill Analysis Complete. Your {target_role} match score is {result['match_score']}%.", "readiness_update")
        
        save_user_data()
    else:
        # GET request: Retrieve previous state if it exists
        result = user_data['last_analysis']
        
    selected_role = user_data['target_role']
    entered_skills = user_data['entered_skills']

    return render_template('analysis.html',
                           result=result,
                           user=user,
                           role_skills=ROLE_SKILLS,
                           skill_keywords=SKILL_KEYWORDS,
                           selected_role=selected_role,
                           entered_skills=entered_skills)

@app.route('/mark_skill_completed', methods=['POST'])
def mark_skill_completed():
    data = request.get_json()
    skill = data.get('skill')
    user_data = USER_STORE[session['storage_key']]
    target_role = user_data['target_role']
    
    if target_role not in user_data['completed_skills']:
        user_data['completed_skills'][target_role] = []
    
    if skill not in user_data['completed_skills'][target_role]:
        user_data['completed_skills'][target_role].append(skill)
    
    # Re-trigger analysis logic to update scores and graph
    analysis_data = user_data['last_analysis']
    if analysis_data:
        # Update current result locally
        if skill in analysis_data['missing_skills']:
            analysis_data['missing_skills'].remove(skill)
        if skill not in analysis_data['detected_skills']:
            analysis_data['detected_skills'].append(skill)
            analysis_data['user_skills_data'][skill] = 95
            
        # Re-run recommendation engine for updated match_score
        updated_result = recommendation_engine.train_and_predict(
            target_role, 
            analysis_data['user_skills_data'], 
            analysis_data['skill_names'], 
            analysis_data['detected_skills'], 
            analysis_data['missing_skills']
        )
        analysis_data['match_score'] = updated_result['match_score']
        analysis_data['gap_score'] = 100 - analysis_data['match_score']
        
        # Update timeline prediction
        user_data['analysis_history'] = generate_readiness_prediction(
            analysis_data['match_score'], 
            analysis_data['missing_skills'], 
            target_role
        )
        
        # Update tips
        user_data['career_tips'] = generate_career_tips(target_role, analysis_data['missing_skills'])
        
        # TRIGGER NOTIFICATIONS
        add_notification(session['storage_key'], f"Milestone: {skill} marked as completed!", "skill_update")
        add_notification(session['storage_key'], f"Readiness improved to {analysis_data['match_score']}%!", "readiness_update")
        
        save_user_data()
        
    return jsonify({'status': 'success', 'match_score': analysis_data['match_score'] if analysis_data else 0})

@app.route('/quiz')
def quiz():
    user = session.get('user', {'name': 'Guest'})
    user_data = USER_STORE[session['storage_key']]
    target_role = user_data['target_role']
    if target_role == 'Not Selected':
        # Default to Data Scientist if no role selected
        target_role = 'Data Scientist'
    
    questions = QUIZ_QUESTIONS.get(target_role, QUIZ_QUESTIONS['Data Scientist'])
    topics = QUIZ_TOPICS.get(target_role, QUIZ_TOPICS['Data Scientist'])
    
    return render_template('quiz.html', 
                           questions=questions, 
                           user=user, 
                           target_role=target_role,
                           topics=topics)

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    data = request.get_json()
    answers = data.get('answers', {})
    storage_key = session['storage_key']
    user_data = USER_STORE[storage_key]
    target_role = user_data['target_role']
    if target_role == 'Not Selected':
        target_role = 'Data Scientist'
    questions = QUIZ_QUESTIONS.get(target_role, QUIZ_QUESTIONS['Data Scientist'])
    
    correct = 0
    total = len(questions)
    topic_scores = {}
    details = []
    
    for q in questions:
        qid = str(q['id'])
        user_answer = int(answers.get(qid, -1)) if qid in answers else -1
        is_correct = (user_answer == q['correct'])
        if is_correct:
            correct += 1
        
        topic = q['topic']
        if topic not in topic_scores:
            topic_scores[topic] = {'correct': 0, 'total': 0}
        topic_scores[topic]['total'] += 1
        if is_correct:
            topic_scores[topic]['correct'] += 1
        
        details.append({
            'question': q['question'],
            'your_answer': q['options'][user_answer] if 0 <= user_answer < len(q['options']) else 'Not answered',
            'correct_answer': q['options'][q['correct']],
            'is_correct': is_correct,
            'topic': topic
        })
    
    score_pct = int((correct / total) * 100) if total > 0 else 0
    status = "Mastered" if score_pct >= 80 else "Improved" if score_pct >= 50 else "Needs Work"
    
    # Calculate weak topics
    weak_topics = []
    for topic, score_info in topic_scores.items():
        if score_info['total'] > 0 and (score_info['correct'] / score_info['total']) < 0.70:
            weak_topics.append(topic)
            
    # Store in persistent history
    history_entry = {
        'date': datetime.now().strftime('%b %d, %Y'),
        'quiz': f"{target_role} Skill Test",
        'score': score_pct,
        'status': status,
        'topics': topic_scores
    }
    
    if 'quiz_history' not in USER_STORE[storage_key]:
        USER_STORE[storage_key]['quiz_history'] = []
    USER_STORE[storage_key]['quiz_history'].append(history_entry)
    
    # Notification for achievement
    if score_pct >= 80:
        add_notification(storage_key, f"Achievement: Scored {score_pct}% in {target_role} Skill Test!", "quiz_alert")
    
    save_user_data()
    
    return jsonify({
        'correct': correct,
        'score': correct,
        'total': total,
        'percentage': score_pct,
        'topic_scores': topic_scores,
        'weak_topics': weak_topics,
        'details': details,
        'status': status
    })

@app.route('/roadmap')
def roadmap():
    from role_skills import SKILL_LEARNING_WEEKS
    user = session.get('user', {'name': 'Guest'})
    user_data = USER_STORE[session['storage_key']]
    analysis = user_data['last_analysis']
    target_role = user_data['target_role']
    roadmap_data = ROADMAP_DATA.get(target_role, ROADMAP_DATA['Data Scientist'])
    return render_template('roadmap.html', 
                           user=user, 
                           analysis=analysis, 
                           roadmap_data=roadmap_data,
                           learning_weeks=SKILL_LEARNING_WEEKS)

@app.route('/history')
def history():
    user = session.get('user', {'name': 'Guest'})
    storage_key = session.get('storage_key')
    
    if not storage_key or storage_key not in USER_STORE:
        return redirect(url_for('auth'))
        
    user_data = USER_STORE[storage_key]
    return render_template('history.html', 
                           user=user, 
                           quiz_history=user_data.get('quiz_history', []), 
                           past_analyses=user_data.get('past_analyses', []),
                           analysis=user_data.get('last_analysis'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/notifications/read_all', methods=['POST'])
def read_all_notifications():
    storage_key = session.get('storage_key')
    if storage_key in USER_STORE:
        for n in USER_STORE[storage_key]['notifications']:
            n['read'] = True
        save_user_data()
    return jsonify({'status': 'success'})

@app.route('/api/notifications/clear', methods=['POST'])
def clear_notifications():
    storage_key = session.get('storage_key')
    if storage_key in USER_STORE:
        USER_STORE[storage_key]['notifications'] = []
        save_user_data()
    return jsonify({'status': 'success'})

@app.route('/api/user/reset', methods=['POST'])
def reset_user_progress():
    storage_key = session.get('storage_key')
    if storage_key in USER_STORE:
        USER_STORE[storage_key] = {
            'target_role': 'Not Selected',
            'entered_skills': '',
            'last_analysis': None,
            'past_analyses': [],
            'quiz_history': [],
            'analysis_history': [],
            'career_tips': [],
            'completed_skills': {},
            'notifications': [],
            'stats': {
                'streak': 1,
                'last_activity': datetime.now().strftime('%Y-%m-%d'),
                'roadmap_completion': 0,
                'quiz_accuracy': 0
            }
        }
        add_notification(storage_key, "Progress has been reset. Start your journey again!", "ai_recommendation")
        save_user_data()
    return jsonify({'status': 'success'})

def get_ai_career_summary(user_data):
    role = user_data['target_role']
    analysis = user_data['last_analysis']
    if not analysis: return "Start your analysis to generate an AI Career Summary."
    
    score = analysis['match_score']
    if score > 80: level = "Advanced"
    elif score > 50: level = "Intermediate"
    else: level = "Starter"
    
    summary = f"You are currently on a {level} {role} learning track. "
    if analysis['detected_skills']:
        summary += f"Your strongest skills are {', '.join(analysis['detected_skills'][:2])}. "
    if analysis['missing_skills']:
        summary += f"Your biggest career gap is {analysis['missing_skills'][0]} understanding."
    
    return summary

def get_ai_career_identity(user_data):
    role = user_data['target_role']
    identities = {
        'AI Engineer': 'AI Builder',
        'Cloud Engineer': 'Cloud Infrastructure Specialist',
        'Web Developer': 'Full Stack Creator',
        'Cyber Security': 'Security Defender',
        'Data Scientist': 'Data Intelligence Analyst'
    }
    return identities.get(role, 'Tech Visionary')

@app.context_processor
def inject_global_data():
    """Injects notifications and profile data into all templates."""
    storage_key = session.get('storage_key')
    if storage_key and storage_key in USER_STORE:
        user_data = USER_STORE[storage_key]
        unread_count = len([n for n in user_data['notifications'] if not n['read']])
        
        # Calculate roadmap completion
        roadmap_completion = 0
        if user_data['last_analysis']:
            total = len(user_data['last_analysis']['skill_names'])
            completed = len(user_data['last_analysis']['detected_skills'])
            roadmap_completion = int((completed / total) * 100) if total > 0 else 0
            
        # Quiz Accuracy
        quiz_accuracy = 0
        if user_data['quiz_history']:
            quiz_accuracy = sum(q['score'] for q in user_data['quiz_history']) // len(user_data['quiz_history'])

        # Global Stats Calculations
        target_role = user_data['target_role']
        last_analysis = user_data['last_analysis']
        role_weights = SKILL_IMPACT_WEIGHTS.get(target_role, {})

        missing_critical_count = 0
        if last_analysis:
            missing_critical_count = len([s for s in last_analysis['missing_skills'] if role_weights.get(s, 0) >= 9])

        return {
            'global_notifications': user_data['notifications'],
            'unread_notifications_count': unread_count,
            'ai_career_summary': get_ai_career_summary(user_data),
            'ai_career_identity': get_ai_career_identity(user_data),
            'global_stats': {
                'roadmap_completion': roadmap_completion,
                'quiz_accuracy': quiz_accuracy,
                'skills_completed': len(last_analysis['detected_skills']) if last_analysis else 0,
                'skills_in_progress': 1 if last_analysis and last_analysis['missing_skills'] else 0,
                'missing_critical': missing_critical_count,
                'current_focus': last_analysis['missing_skills'][0] if last_analysis and last_analysis['missing_skills'] else 'None',
                'next_high_impact': [s for s in last_analysis['missing_skills'] if role_weights.get(s, 0) >= 9][0] if last_analysis and any(role_weights.get(s, 0) >= 9 for s in last_analysis['missing_skills']) else 'None'
            }
        }
    return {
        'global_notifications': [],
        'unread_notifications_count': 0,
        'ai_career_summary': "Complete analysis to see your summary.",
        'ai_career_identity': "Explorer",
        'global_stats': {
            'roadmap_completion': 0,
            'quiz_accuracy': 0,
            'skills_completed': 0,
            'skills_in_progress': 0,
            'missing_critical': 0,
            'current_focus': 'None',
            'next_high_impact': 'None'
        }
    }

if __name__ == '__main__':
    app.run(debug=True)
