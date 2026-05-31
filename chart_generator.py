from role_skills import ROLE_SKILLS

def get_dashboard_chart_data(target_role, analysis):
    """
    Generates consistent Chart.js initialization data for the dashboard.
    If no analysis exists, it defaults to 0% user skills for the selected target_role.
    """
    relevant_skills = ROLE_SKILLS.get(target_role, ROLE_SKILLS['Data Scientist'])
    
    if analysis and 'user_skills_data' in analysis:
        user_skills = [analysis['user_skills_data'].get(s, 0) for s in relevant_skills]
        match_score = analysis.get('match_score', 0)
    else:
        # Default empty state for the selected role
        user_skills = [10 for _ in relevant_skills]  # Give a slight visual bump so chart isn't completely flat
        match_score = 0
        
    required_skills = [85 for _ in relevant_skills] # Industry standard target
    
    return {
        'skill_labels': relevant_skills,
        'user_skills': user_skills,
        'required_skills': required_skills,
        'match_score': match_score
    }
