ROLE_SKILLS = {
    'Data Scientist': ['Python', 'Pandas', 'NumPy', 'Machine Learning', 'SQL', 'Data Visualization', 'Statistics', 'Deep Learning'],
    'AI Engineer': ['Python', 'TensorFlow', 'PyTorch', 'Deep Learning', 'NLP', 'Neural Networks', 'LLMs', 'Computer Vision'],
    'Cloud Engineer': ['AWS', 'Docker', 'Kubernetes', 'Linux', 'Terraform', 'CI/CD', 'Networking', 'DevOps'],
    'Web Developer': ['HTML', 'CSS', 'JavaScript', 'React', 'Node.js', 'APIs', 'MongoDB', 'Git'],
    'Cyber Security': ['Networking', 'Linux', 'Ethical Hacking', 'Cryptography', 'SIEM', 'Kali Linux', 'Threat Analysis'],
    'Software Developer': ['Java', 'Python', 'DSA', 'OOP', 'DBMS', 'Git', 'Problem Solving', 'System Design']
}

SKILL_KEYWORDS = {
    # Data Scientist / AI Engineer / Software Developer
    'Python': ['python', 'py', 'python3', 'django', 'flask', 'scripting'],
    'Pandas': ['pandas', 'dataframe', 'data manipulation', 'data cleaning'],
    'NumPy': ['numpy', 'ndarrays', 'numerical python', 'linear algebra'],
    'Machine Learning': ['machine learning', 'ml', 'scikit-learn', 'supervised', 'unsupervised', 'regression', 'classification'],
    'SQL': ['sql', 'mysql', 'postgres', 'postgresql', 'queries', 'rdbms'],
    'Data Visualization': ['visualization', 'matplotlib', 'seaborn', 'plotly', 'tableau', 'bi'],
    'Statistics': ['statistics', 'stats', 'probability', 'hypothesis', 'distribution'],
    'Deep Learning': ['deep learning', 'dl', 'neural networks', 'ann', 'cnn', 'rnn'],
    
    # AI Engineer
    'TensorFlow': ['tensorflow', 'tf', 'keras'],
    'PyTorch': ['pytorch', 'torch'],
    'NLP': ['nlp', 'natural language', 'spacy', 'nltk', 'text mining'],
    'Neural Networks': ['neural networks', 'ann', 'cnn', 'rnn', 'lstm'],
    'LLMs': ['llm', 'large language models', 'gpt', 'transformers', 'bert', 'langchain'],
    'Computer Vision': ['computer vision', 'cv', 'opencv', 'image processing', 'yolo'],
    
    # Cloud Engineer
    'AWS': ['aws', 'amazon web services', 'ec2', 's3', 'lambda', 'cloud'],
    'Docker': ['docker', 'containerization', 'containers'],
    'Kubernetes': ['kubernetes', 'k8s', 'helm', 'orchestration'],
    'Linux': ['linux', 'unix', 'bash', 'shell', 'ubuntu', 'centos', 'redhat'],
    'Terraform': ['terraform', 'iac', 'infrastructure as code'],
    'CI/CD': ['ci/cd', 'jenkins', 'github actions', 'gitlab ci', 'pipelines'],
    'Networking': ['networking', 'tcp/ip', 'dns', 'http', 'routing', 'vpc', 'subnet'],
    'DevOps': ['devops', 'automation', 'sre'],
    
    # Web Developer
    'HTML': ['html', 'html5', 'markup'],
    'CSS': ['css', 'css3', 'sass', 'scss', 'tailwind', 'bootstrap'],
    'JavaScript': ['javascript', 'js', 'es6', 'typescript', 'ts'],
    'React': ['react', 'reactjs', 'nextjs', 'redux'],
    'Node.js': ['node.js', 'node', 'express', 'backend js'],
    'APIs': ['api', 'rest', 'graphql', 'endpoints', 'json'],
    'MongoDB': ['mongodb', 'mongo', 'nosql', 'mongoose'],
    'Git': ['git', 'github', 'gitlab', 'version control'],
    
    # Cyber Security
    'Ethical Hacking': ['ethical hacking', 'penetration testing', 'pentesting', 'metasploit', 'vulnerability'],
    'Cryptography': ['cryptography', 'crypto', 'encryption', 'tls', 'ssl', 'hashing'],
    'SIEM': ['siem', 'splunk', 'qradar', 'log analysis', 'incident response'],
    'Kali Linux': ['kali', 'kali linux', 'nmap', 'wireshark'],
    'Threat Analysis': ['threat analysis', 'threat intelligence', 'malware analysis'],
    
    # Software Developer
    'Java': ['java', 'spring', 'springboot', 'jvm'],
    'DSA': ['dsa', 'data structures', 'algorithms', 'sorting', 'searching'],
    'OOP': ['oop', 'object oriented', 'classes', 'inheritance', 'polymorphism', 'encapsulation'],
    'DBMS': ['dbms', 'database', 'sql', 'nosql', 'rdbms'],
    'Problem Solving': ['problem solving', 'coding challenges', 'leetcode', 'logic'],
    'System Design': ['system design', 'scalability', 'architecture', 'load balancing']
}

SKILL_LEARNING_WEEKS = {
    # Data Scientist
    'Python': 2, 'Pandas': 1, 'NumPy': 1, 'SQL': 2, 'Machine Learning': 4, 'Statistics': 3, 'Data Visualization': 2, 'Deep Learning': 5,
    # AI Engineer
    'TensorFlow': 3, 'PyTorch': 3, 'NLP': 4, 'Neural Networks': 4, 'LLMs': 5, 'Computer Vision': 4,
    # Cloud Engineer
    'AWS': 3, 'Docker': 2, 'Kubernetes': 4, 'Linux': 3, 'Terraform': 2, 'CI/CD': 2, 'Networking': 3, 'DevOps': 4,
    # Web Developer
    'HTML': 1, 'CSS': 1, 'JavaScript': 3, 'React': 4, 'Node.js': 3, 'APIs': 2, 'MongoDB': 2, 'Git': 1,
    # Cyber Security
    'Ethical Hacking': 5, 'Cryptography': 4, 'SIEM': 3, 'Kali Linux': 2, 'Threat Analysis': 4,
    # Software Developer
    'Java': 3, 'DSA': 5, 'OOP': 3, 'DBMS': 3, 'Problem Solving': 5, 'System Design': 6
}

SKILL_IMPACT_WEIGHTS = {
    # Data Scientist
    'Machine Learning': 10, 'Statistics': 9, 'Deep Learning': 9, 'SQL': 7, 'Python': 6, 'Pandas': 5, 'NumPy': 5, 'Data Visualization': 6,
    # AI Engineer
    'Deep Learning': 10, 'LLMs': 10, 'Neural Networks': 9, 'NLP': 8, 'Computer Vision': 8, 'TensorFlow': 7, 'PyTorch': 7, 'Python': 6,
    # Cloud Engineer
    'Kubernetes': 10, 'DevOps': 10, 'Terraform': 9, 'AWS': 8, 'Docker': 7, 'Linux': 6, 'CI/CD': 7, 'Networking': 6,
    # Web Developer
    'React': 10, 'Node.js': 9, 'APIs': 8, 'JavaScript': 7, 'MongoDB': 6, 'HTML': 4, 'CSS': 4, 'Git': 5,
    # Cyber Security
    'Ethical Hacking': 10, 'Threat Analysis': 9, 'Networking': 8, 'Linux': 7, 'SIEM': 7, 'Cryptography': 8, 'Kali Linux': 6,
    # Software Developer
    'DSA': 10, 'Problem Solving': 10, 'System Design': 9, 'OOP': 8, 'Java': 7, 'DBMS': 7, 'Git': 5, 'Python': 6
}
