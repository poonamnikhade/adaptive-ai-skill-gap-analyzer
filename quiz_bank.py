QUIZ_QUESTIONS = {
    'Data Scientist': [
        {'id': 1, 'topic': 'Python', 'question': 'Which library is primarily used for high-level data manipulation in Python?', 'options': ['NumPy', 'Pandas', 'Matplotlib', 'Scipy'], 'correct': 1},
        {'id': 2, 'topic': 'Statistics', 'question': 'What does a p-value of 0.03 typically indicate in hypothesis testing?', 'options': ['Null hypothesis is true', 'Result is statistically significant', 'Insufficient data', 'High variance'], 'correct': 1},
        {'id': 3, 'topic': 'Machine Learning', 'question': 'Which of these is an example of an unsupervised learning task?', 'options': ['Linear Regression', 'Spam detection', 'Clustering', 'Digit classification'], 'correct': 2},
        {'id': 4, 'topic': 'Deep Learning', 'question': 'What is the standard activation function used in the hidden layers of modern neural networks?', 'options': ['Sigmoid', 'Tanh', 'ReLU', 'Softmax'], 'correct': 2},
        {'id': 5, 'topic': 'SQL', 'question': 'Which SQL clause is used to filter records after an aggregation?', 'options': ['WHERE', 'FILTER', 'HAVING', 'GROUP BY'], 'correct': 2}
    ],
    'AI Engineer': [
        {'id': 1, 'topic': 'Deep Learning', 'question': 'In a CNN, what is the primary purpose of a pooling layer?', 'options': ['Increase weights', 'Reduce spatial dimensions', 'Apply activation', 'Normalize data'], 'correct': 1},
        {'id': 2, 'topic': 'NLP', 'question': 'Which architecture introduced the "Attention" mechanism for sequential data?', 'options': ['RNN', 'LSTM', 'Transformer', 'GRU'], 'correct': 2},
        {'id': 3, 'topic': 'PyTorch', 'question': 'What is the primary data structure used in PyTorch for computations?', 'options': ['Array', 'Tensor', 'List', 'Matrix'], 'correct': 1},
        {'id': 4, 'topic': 'LLMs', 'question': 'What does the "G" in GPT stand for?', 'options': ['Global', 'General', 'Generative', 'Graph'], 'correct': 2},
        {'id': 5, 'topic': 'Computer Vision', 'question': 'Which algorithm is widely used for real-time object detection?', 'options': ['ResNet', 'YOLO', 'VGG16', 'BERT'], 'correct': 1}
    ],
    'Cloud Engineer': [
        {'id': 1, 'topic': 'AWS', 'question': 'Which AWS service provides resizable compute capacity in the cloud?', 'options': ['S3', 'Lambda', 'EC2', 'RDS'], 'correct': 2},
        {'id': 2, 'topic': 'Docker', 'question': 'What is the purpose of a Dockerfile?', 'options': ['Run a container', 'Define the image build process', 'Manage volumes', 'Network setup'], 'correct': 1},
        {'id': 3, 'topic': 'Kubernetes', 'question': 'What is the smallest deployable unit in Kubernetes?', 'options': ['Container', 'Node', 'Pod', 'Service'], 'correct': 2},
        {'id': 4, 'topic': 'Terraform', 'question': 'What type of language is HCL (used by Terraform)?', 'options': ['Imperative', 'Declarative', 'Procedural', 'Functional'], 'correct': 1},
        {'id': 5, 'topic': 'CI/CD', 'question': 'Which process ensures that code changes are automatically tested and prepared for release?', 'options': ['Continuous Deployment', 'Continuous Delivery', 'Unit Testing', 'Code Review'], 'correct': 1}
    ],
    'Web Developer': [
        {'id': 1, 'topic': 'JavaScript', 'question': 'Which keyword is used to declare a block-scoped variable in modern JS?', 'options': ['var', 'let', 'global', 'define'], 'correct': 1},
        {'id': 2, 'topic': 'React', 'question': 'What is the primary purpose of "Hooks" in React?', 'options': ['Connect to DB', 'Use state in functional components', 'Apply CSS', 'Manage routing'], 'correct': 1},
        {'id': 3, 'topic': 'Node.js', 'question': 'Which core module is used to handle file system operations?', 'options': ['http', 'path', 'fs', 'os'], 'correct': 2},
        {'id': 4, 'topic': 'APIs', 'question': 'What does REST stand for?', 'options': ['Representational State Transfer', 'Responsive Site Technology', 'Real-time State Tracking', 'Remote Storage'], 'correct': 0},
        {'id': 5, 'topic': 'MongoDB', 'question': 'What type of database is MongoDB?', 'options': ['Relational', 'Graph', 'Document-oriented', 'Key-value'], 'correct': 2}
    ],
    'Cyber Security': [
        {'id': 1, 'topic': 'Networking', 'question': 'On which layer of the OSI model does a Router operate?', 'options': ['Layer 2', 'Layer 3', 'Layer 4', 'Layer 7'], 'correct': 1},
        {'id': 2, 'topic': 'Ethical Hacking', 'question': 'What is "nmap" primarily used for?', 'options': ['Password cracking', 'Network scanning', 'SQL injection', 'Traffic analysis'], 'correct': 1},
        {'id': 3, 'topic': 'Cryptography', 'question': 'Which of these is a symmetric encryption algorithm?', 'options': ['RSA', 'AES', 'Diffie-Hellman', 'ECC'], 'correct': 1},
        {'id': 4, 'topic': 'SIEM', 'question': 'What is the main goal of a SIEM system?', 'options': ['Encrypt files', 'Centralized log monitoring and analysis', 'Block firewall ports', 'Scan for viruses'], 'correct': 1},
        {'id': 5, 'topic': 'Threat Analysis', 'question': 'What is a "Zero-day" vulnerability?', 'options': ['Old bug', 'Newly discovered, unpatched bug', 'Low-risk bug', 'Virus with no payload'], 'correct': 1}
    ],
    'Software Developer': [
        {'id': 1, 'topic': 'DSA', 'question': 'What is the average time complexity of a Quicksort algorithm?', 'options': ['O(n)', 'O(n log n)', 'O(n^2)', 'O(log n)'], 'correct': 1},
        {'id': 2, 'topic': 'OOP', 'question': 'Which principle refers to the ability of different classes to be treated as instances of the same interface?', 'options': ['Encapsulation', 'Inheritance', 'Polymorphism', 'Abstraction'], 'correct': 2},
        {'id': 3, 'topic': 'Java', 'question': 'What is the role of the JVM?', 'options': ['Compile code', 'Execute Java bytecode', 'Manage DB', 'Design UI'], 'correct': 1},
        {'id': 4, 'topic': 'System Design', 'question': 'What is the primary benefit of using a Load Balancer?', 'options': ['Encrypt traffic', 'Distribute incoming requests', 'Store session data', 'Compile assets'], 'correct': 1},
        {'id': 5, 'topic': 'Git', 'question': 'Which command is used to combine changes from one branch into another?', 'options': ['git push', 'git merge', 'git add', 'git commit'], 'correct': 1}
    ]
}

QUIZ_TOPICS = {
    'Data Scientist': 'Python, Statistics, ML, SQL',
    'AI Engineer': 'Deep Learning, NLP, PyTorch, LLMs',
    'Cloud Engineer': 'AWS, Docker, K8s, CI/CD',
    'Web Developer': 'JS, React, Node, MongoDB',
    'Cyber Security': 'Networking, Hacking, Crypto, SIEM',
    'Software Developer': 'DSA, OOP, Java, System Design'
}
