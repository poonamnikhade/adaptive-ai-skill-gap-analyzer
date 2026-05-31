from role_skills import ROLE_SKILLS, SKILL_KEYWORDS

def analyze_skills(target_role, skills_text):
    skills_text = skills_text.lower()
    required_skills = ROLE_SKILLS.get(target_role, ROLE_SKILLS.get('Data Scientist'))
    
    user_skills_scores = {}
    detected_skills = []
    missing_skills = []
    
    for skill in required_skills:
        keywords = SKILL_KEYWORDS.get(skill, [skill.lower()])
        # Check if any keyword matches the input text
        found = False
        match_count = 0
        for kw in keywords:
            if kw.lower() in skills_text:
                found = True
                match_count += 1
        
        if found:
            # Dynamic scoring based on keyword density/relevance
            score = min(60 + (match_count * 10), 98)
            user_skills_scores[skill] = score
            detected_skills.append(skill)
        else:
            # Low score for missing skills
            user_skills_scores[skill] = 20
            missing_skills.append(skill)
            
    return user_skills_scores, required_skills, detected_skills, missing_skills
