ROADMAP_DATA = {
    'Data Scientist': [
        {
            'skill': 'Python', 'level': 'Beginner', 
            'explanation': 'Start here! Python is the industry standard for Data Science. Mastering basic syntax and data structures is essential for everything that follows.',
            'resources': {
                'beginner': {'name': 'Python for Beginners (Mosh)', 'url': 'https://www.youtube.com/watch?v=_uQrJ0TkZlc'},
                'intermediate': {'name': 'Python Data Science Course', 'url': 'https://www.youtube.com/watch?v=rfscVS0vtbw'},
                'practice': {'name': 'HackerRank Python', 'url': 'https://www.hackerrank.com/domains/python'},
                'docs': {'name': 'Official Python Docs', 'url': 'https://docs.python.org/3/'},
                'project': {'name': 'Build a Simple Calculator/Scraper', 'url': 'https://github.com/karan/Projects'}
            }
        },
        {
            'skill': 'NumPy', 'level': 'Beginner',
            'explanation': 'NumPy introduces efficient array processing, which is the backbone of all mathematical computations in Data Science.',
            'resources': {
                'beginner': {'name': 'NumPy Tutorial for Beginners', 'url': 'https://www.youtube.com/watch?v=QUT1VHiLmmI'},
                'intermediate': {'name': 'NumPy User Guide', 'url': 'https://numpy.org/doc/stable/user/absolute_beginners.html'},
                'practice': {'name': '100 NumPy Exercises', 'url': 'https://github.com/rougier/numpy-100'},
                'docs': {'name': 'Official NumPy Docs', 'url': 'https://numpy.org/doc/'},
                'project': {'name': 'Numerical Data Analysis Project', 'url': 'https://github.com/topics/numpy-projects'}
            }
        },
        {
            'skill': 'Pandas', 'level': 'Intermediate',
            'explanation': 'Pandas is the core library for data manipulation. It allows you to clean and analyze structured data using DataFrames.',
            'resources': {
                'beginner': {'name': 'Pandas Tutorial (Keith Galli)', 'url': 'https://www.youtube.com/watch?v=vmEHCJofslg'},
                'intermediate': {'name': 'Pandas Mastery (Corey Schafer)', 'url': 'https://www.youtube.com/watch?v=ZyhVh-qRZPA'},
                'practice': {'name': 'Pandas Exercises (GitHub)', 'url': 'https://github.com/guipsamora/pandas_exercises'},
                'docs': {'name': 'Pandas Documentation', 'url': 'https://pandas.pydata.org/docs/'},
                'project': {'name': 'Titanic Dataset Analysis', 'url': 'https://www.kaggle.com/c/titanic'}
            }
        },
        {
            'skill': 'SQL', 'level': 'Intermediate',
            'explanation': 'Most data lives in databases. SQL is critical for extracting and joining data before you can analyze it in Python.',
            'resources': {
                'beginner': {'name': 'SQL for Beginners (Mosh)', 'url': 'https://www.youtube.com/watch?v=7S_tz1z_5bA'},
                'intermediate': {'name': 'SQL Full Course (FreeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=HXV3zePRqGY'},
                'practice': {'name': 'SQLZoo Interactive Exercises', 'url': 'https://sqlzoo.net/'},
                'docs': {'name': 'Postgres Documentation', 'url': 'https://www.postgresql.org/docs/'},
                'project': {'name': 'Sales Data DB Queries', 'url': 'https://github.com/topics/sql-projects'}
            }
        },
        {
            'skill': 'Statistics', 'level': 'Intermediate',
            'explanation': 'Statistics provides the mathematical framework for understanding data distributions, probability, and hypothesis testing.',
            'resources': {
                'beginner': {'name': 'Statistics for Data Science', 'url': 'https://www.youtube.com/watch?v=VPZD_aij8H0'},
                'intermediate': {'name': 'Statistics & Probability Course', 'url': 'https://www.khanacademy.org/math/statistics-probability'},
                'practice': {'name': 'StatQuest Video Quizzes', 'url': 'https://statquest.org/'},
                'docs': {'name': 'SciPy Stats Module Docs', 'url': 'https://docs.scipy.org/doc/scipy/reference/stats.html'},
                'project': {'name': 'Hypothesis Testing Study', 'url': 'https://github.com/topics/statistics-projects'}
            }
        },
        {
            'skill': 'Data Visualization', 'level': 'Advanced',
            'explanation': 'Communicating insights is as important as finding them. Learn to create professional charts using Matplotlib and Seaborn.',
            'resources': {
                'beginner': {'name': 'Matplotlib & Seaborn Tutorial', 'url': 'https://www.youtube.com/watch?v=qErMGa-L6mI'},
                'intermediate': {'name': 'Data Viz Mastery (Sentdex)', 'url': 'https://www.youtube.com/watch?v=wB9C0Mz9gSo'},
                'practice': {'name': 'Tableau Public Challenges', 'url': 'https://public.tableau.com/'},
                'docs': {'name': 'Matplotlib Documentation', 'url': 'https://matplotlib.org/stable/contents.html'},
                'project': {'name': 'Interactive Dashboard Project', 'url': 'https://github.com/topics/data-visualization'}
            }
        },
        {
            'skill': 'Machine Learning', 'level': 'Advanced',
            'explanation': 'This is where prediction happens. You\'ll learn to build models that learn from historical data to forecast future outcomes.',
            'resources': {
                'beginner': {'name': 'ML for Beginners (FreeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=i_LwzRVP7bg'},
                'intermediate': {'name': 'ML Course (Sentdex)', 'url': 'https://www.youtube.com/watch?v=T5pRlIbr6Ww'},
                'practice': {'name': 'Kaggle ML Competitions', 'url': 'https://www.kaggle.com/competitions'},
                'docs': {'name': 'Scikit-Learn Documentation', 'url': 'https://scikit-learn.org/'},
                'project': {'name': 'House Price Prediction Model', 'url': 'https://github.com/topics/machine-learning'}
            }
        },
        {
            'skill': 'Deep Learning', 'level': 'Expert',
            'explanation': 'Deep Learning uses neural networks to handle complex data like images and text. It\'s the state-of-the-art for modern AI.',
            'resources': {
                'beginner': {'name': 'Deep Learning Crash Course', 'url': 'https://www.youtube.com/watch?v=VyWavY205hs'},
                'intermediate': {'name': 'Deep Learning with PyTorch', 'url': 'https://www.youtube.com/watch?v=V_xro1bcAuA'},
                'practice': {'name': 'MNIST Digit Classification', 'url': 'https://github.com/topics/deep-learning'},
                'docs': {'name': 'PyTorch Documentation', 'url': 'https://pytorch.org/docs/'},
                'project': {'name': 'Image Recognition System', 'url': 'https://github.com/topics/cnn'}
            }
        }
    ],
    'AI Engineer': [
        {
            'skill': 'Python', 'level': 'Beginner', 
            'explanation': 'AI Engineers use Python to implement complex algorithms and interface with deep learning frameworks.',
            'resources': {
                'beginner': {'name': 'Python AI Roadmap', 'url': 'https://www.youtube.com/watch?v=mkv5mxnvW7c'},
                'intermediate': {'name': 'Python for Beginners (Mosh)', 'url': 'https://www.youtube.com/watch?v=_uQrJ0TkZlc'},
                'practice': {'name': 'CodingBat Python', 'url': 'https://codingbat.com/python'},
                'docs': {'name': 'Python Docs', 'url': 'https://docs.python.org/'},
                'project': {'name': 'AI Scripting Projects', 'url': 'https://github.com/topics/python-ai'}
            }
        },
        {
            'skill': 'Neural Networks', 'level': 'Beginner',
            'explanation': 'Understanding the biological inspiration and mathematical foundations of AI is essential before using advanced libraries.',
            'resources': {
                'beginner': {'name': 'Neural Networks (3Blue1Brown)', 'url': 'https://www.youtube.com/watch?v=aircAruvnKk'},
                'intermediate': {'name': 'Neural Networks Zero to Hero', 'url': 'https://karpathy.ai/zero-to-hero.html'},
                'practice': {'name': 'TensorFlow Playground', 'url': 'https://playground.tensorflow.org/'},
                'docs': {'name': 'Deep Learning Theory', 'url': 'https://www.deeplearningbook.org/'},
                'project': {'name': 'Manual Backprop Implementation', 'url': 'https://github.com/topics/neural-network'}
            }
        },
        {
            'skill': 'Deep Learning', 'level': 'Intermediate',
            'explanation': 'Build on Neural Networks to understand complex multi-layer architectures and optimization techniques.',
            'resources': {
                'beginner': {'name': 'Deep Learning (FreeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=6M5VXAPfJ20'},
                'intermediate': {'name': 'DeepLearning.ai Specialization', 'url': 'https://www.deeplearning.ai/'},
                'practice': {'name': 'Kaggle DL Exercises', 'url': 'https://www.kaggle.com/learn/deep-learning'},
                'docs': {'name': 'Keras Docs', 'url': 'https://keras.io/'},
                'project': {'name': 'Neural Network From Scratch', 'url': 'https://github.com/topics/deep-learning-projects'}
            }
        },
        {
            'skill': 'TensorFlow', 'level': 'Intermediate',
            'explanation': 'TensorFlow is Google\'s primary AI framework, widely used for production-grade deep learning applications.',
            'resources': {
                'beginner': {'name': 'TensorFlow Full Course', 'url': 'https://www.youtube.com/watch?v=tPYj3fFJGjk'},
                'intermediate': {'name': 'TF Certification Path', 'url': 'https://www.tensorflow.org/certificate'},
                'practice': {'name': 'Official TF Hub', 'url': 'https://tfhub.dev/'},
                'docs': {'name': 'TensorFlow API Docs', 'url': 'https://www.tensorflow.org/api_docs'},
                'project': {'name': 'Production AI Model', 'url': 'https://github.com/tensorflow/models'}
            }
        },
        {
            'skill': 'PyTorch', 'level': 'Intermediate',
            'explanation': 'PyTorch is favored by researchers for its dynamic graph capability and is currently the most popular framework in AI.',
            'resources': {
                'beginner': {'name': 'PyTorch for Beginners', 'url': 'https://www.youtube.com/watch?v=V_xro1bcAuA'},
                'intermediate': {'name': 'PyTorch Examples (GitHub)', 'url': 'https://github.com/pytorch/examples'},
                'practice': {'name': 'PyTorch Tutorials', 'url': 'https://pytorch.org/tutorials/'},
                'docs': {'name': 'Official PyTorch Docs', 'url': 'https://pytorch.org/docs/'},
                'project': {'name': 'Research Paper Re-implementation', 'url': 'https://github.com/topics/pytorch-projects'}
            }
        },
        {
            'skill': 'NLP', 'level': 'Advanced',
            'explanation': 'Teach machines to understand human language. Essential for building chatbots, translators, and search engines.',
            'resources': {
                'beginner': {'name': 'NLP with SpaCy/NLTK', 'url': 'https://www.youtube.com/watch?v=xvqsFTUsOmc'},
                'intermediate': {'name': 'Stanford CS224N (NLP)', 'url': 'https://web.stanford.edu/class/cs224n/'},
                'practice': {'name': 'Sentiment Analysis Project', 'url': 'https://github.com/topics/nlp'},
                'docs': {'name': 'Hugging Face Docs', 'url': 'https://huggingface.co/docs'},
                'project': {'name': 'Build a Translation AI', 'url': 'https://github.com/topics/translation'}
            }
        },
        {
            'skill': 'Computer Vision', 'level': 'Advanced',
            'explanation': 'Enable AI to "see" and interpret visual data from the world, like objects in images or real-time video.',
            'resources': {
                'beginner': {'name': 'Computer Vision with OpenCV', 'url': 'https://www.youtube.com/watch?v=WQeoO7MI0Bs'},
                'intermediate': {'name': 'CV with OpenCV (Sentdex)', 'url': 'https://www.youtube.com/watch?v=Z78zbnLlPUA'},
                'practice': {'name': 'Object Detection (YOLO)', 'url': 'https://github.com/topics/computer-vision'},
                'docs': {'name': 'OpenCV Documentation', 'url': 'https://docs.opencv.org/'},
                'project': {'name': 'Face Recognition System', 'url': 'https://github.com/topics/face-recognition'}
            }
        },
        {
            'skill': 'LLMs', 'level': 'Expert',
            'explanation': 'Master the cutting edge. Learn to work with Large Language Models like GPT, Llama, and fine-tuning techniques.',
            'resources': {
                'beginner': {'name': 'LLM Roadmap (YouTube)', 'url': 'https://www.youtube.com/watch?v=p6m7uT0sP10'},
                'intermediate': {'name': 'Hugging Face Course', 'url': 'https://huggingface.co/learn/nlp-course/'},
                'practice': {'name': 'LangChain Documentation', 'url': 'https://python.langchain.com/'},
                'docs': {'name': 'OpenAI API Reference', 'url': 'https://platform.openai.com/docs/'},
                'project': {'name': 'Personal AI Assistant with LLM', 'url': 'https://github.com/topics/llm-projects'}
            }
        }
    ],
    'Cloud Engineer': [
        {
            'skill': 'Linux', 'level': 'Beginner', 
            'explanation': 'The foundation of the cloud. Most servers and containers run on Linux. Mastering the terminal is mandatory.',
            'resources': {
                'beginner': {'name': 'Linux for Beginners (NetworkChuck)', 'url': 'https://www.youtube.com/watch?v=V1y-mbWM3B8'},
                'intermediate': {'name': 'Linux Full Course (FreeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=wBp0Rb-ZJak'},
                'intermediate_2': {'name': 'Linux Journey', 'url': 'https://linuxjourney.com/'},
                'practice': {'name': 'OverTheWire Wargames', 'url': 'https://overthewire.org/wargames/'},
                'docs': {'name': 'Ubuntu Community Help', 'url': 'https://help.ubuntu.com/'},
                'project': {'name': 'Setup a Home Server', 'url': 'https://github.com/topics/linux-projects'}
            }
        },
        {
            'skill': 'Networking', 'level': 'Beginner',
            'explanation': 'You can\'t build in the cloud without understanding how data moves through IPs, Subnets, and Firewalls.',
            'resources': {
                'beginner': {'name': 'Networking for Cloud', 'url': 'https://www.youtube.com/watch?v=qiQR5rTSshw'},
                'intermediate': {'name': 'Networking Basics (Professor Messer)', 'url': 'https://www.youtube.com/watch?v=0_u6_6XF4nE'},
                'practice': {'name': 'Cisco Packet Tracer', 'url': 'https://www.netacad.com/courses/packet-tracer'},
                'docs': {'name': 'AWS VPC Documentation', 'url': 'https://docs.aws.amazon.com/vpc/'},
                'project': {'name': 'Network Architecture Design', 'url': 'https://github.com/topics/networking'}
            }
        },
        {
            'skill': 'AWS', 'level': 'Intermediate',
            'explanation': 'The market-leading cloud platform. Learn core services like EC2, S3, and IAM to deploy global infrastructure.',
            'resources': {
                'beginner': {'name': 'AWS Cloud Practitioner (FreeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=SOTamWNgDKc'},
                'intermediate': {'name': 'AWS Training and Certification', 'url': 'https://www.aws.training/'},
                'practice': {'name': 'AWS Hands-On Labs', 'url': 'https://aws.amazon.com/getting-started/hands-on/'},
                'docs': {'name': 'AWS Official Documentation', 'url': 'https://docs.aws.amazon.com/'},
                'project': {'name': 'Deploy a Static Site on AWS', 'url': 'https://github.com/topics/aws-projects'}
            }
        },
        {
            'skill': 'Docker', 'level': 'Intermediate',
            'explanation': 'Containerization allows applications to run reliably across different environments. It is the modern standard for deployment.',
            'resources': {
                'beginner': {'name': 'Docker Crash Course (Nana)', 'url': 'https://www.youtube.com/watch?v=3c-iBn73dDE'},
                'intermediate': {'name': 'Docker Full Course (FreeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=fqMOX6JJhGo'},
                'practice': {'name': 'Play with Docker', 'url': 'https://labs.play-with-docker.com/'},
                'docs': {'name': 'Docker Documentation', 'url': 'https://docs.docker.com/'},
                'project': {'name': 'Containerize a Full-Stack App', 'url': 'https://github.com/topics/docker-projects'}
            }
        },
        {
            'skill': 'Kubernetes', 'level': 'Advanced',
            'explanation': 'Orchestrate hundreds of containers. K8s is essential for managing large-scale, resilient cloud applications.',
            'resources': {
                'beginner': {'name': 'Kubernetes for Beginners (Nana)', 'url': 'https://www.youtube.com/watch?v=X48VuDVv0do'},
                'intermediate': {'name': 'Kubernetes Full Course', 'url': 'https://www.youtube.com/watch?v=d6WC5n9G_sM'},
                'practice': {'name': 'Killercoda Interactive K8s', 'url': 'https://killercoda.com/playgrounds/scenario/kubernetes'},
                'docs': {'name': 'Kubernetes Official Docs', 'url': 'https://kubernetes.io/docs/'},
                'project': {'name': 'K8s Cluster Management', 'url': 'https://github.com/topics/kubernetes-projects'}
            }
        },
        {
            'skill': 'Terraform', 'level': 'Advanced',
            'explanation': 'Manage infrastructure with code. Terraform allows you to automate the creation of entire cloud environments.',
            'resources': {
                'beginner': {'name': 'Terraform Crash Course', 'url': 'https://www.youtube.com/watch?v=SLB_c_ayRMo'},
                'intermediate': {'name': 'HashiCorp Learn', 'url': 'https://developer.hashicorp.com/terraform/tutorials'},
                'practice': {'name': 'Terraform Cloud Lab', 'url': 'https://app.terraform.io/'},
                'docs': {'name': 'Terraform Registry', 'url': 'https://registry.terraform.io/'},
                'project': {'name': 'Automated Multi-region AWS Setup', 'url': 'https://github.com/topics/terraform-projects'}
            }
        },
        {
            'skill': 'CI/CD', 'level': 'Advanced',
            'explanation': 'Automate the software release process. CI/CD ensures that code changes are tested and deployed automatically.',
            'resources': {
                'beginner': {'name': 'CI/CD Explained (Nana)', 'url': 'https://www.youtube.com/watch?v=scEDHsr3APg'},
                'intermediate': {'name': 'GitHub Actions Mastery', 'url': 'https://www.youtube.com/watch?v=R8_veQiYBjI'},
                'practice': {'name': 'Build a Jenkins Pipeline', 'url': 'https://www.jenkins.io/doc/tutorials/'},
                'docs': {'name': 'GitLab CI Documentation', 'url': 'https://docs.gitlab.com/ee/ci/'},
                'project': {'name': 'Automated Deployment Pipeline', 'url': 'https://github.com/topics/cicd'}
            }
        },
        {
            'skill': 'DevOps', 'level': 'Expert',
            'explanation': 'The final synthesis. DevOps combines development and operations into a single lifecycle for high-speed reliability.',
            'resources': {
                'beginner': {'name': 'DevOps Roadmap (Nana)', 'url': 'https://www.youtube.com/watch?v=hQcFE0RD0cQ'},
                'intermediate': {'name': 'DevOps Full Course', 'url': 'https://www.youtube.com/watch?v=0_u6_6XF4nE'},
                'practice': {'name': 'DevOps Challenges', 'url': 'https://github.com/topics/devops'},
                'docs': {'name': 'Microsoft DevOps Guide', 'url': 'https://learn.microsoft.com/en-us/devops/'},
                'project': {'name': 'SRE Infrastructure Project', 'url': 'https://github.com/topics/sre'}
            }
        }
    ],
    'Web Developer': [
        {
            'skill': 'HTML', 'level': 'Beginner', 
            'explanation': 'Every website starts with HTML. It defines the structure and content of your web pages.',
            'resources': {
                'beginner': {'name': 'HTML Full Course (FreeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=kUMe1FH4CHE'},
                'intermediate': {'name': 'HTML Tutorial for Beginners', 'url': 'https://www.youtube.com/watch?v=ok-plXXHlWw'},
                'practice': {'name': 'W3Schools Exercises', 'url': 'https://www.w3schools.com/html/html_exercises.asp'},
                'docs': {'name': 'HTML Specification', 'url': 'https://html.spec.whatwg.org/'},
                'project': {'name': 'Build a Portfolio Skeleton', 'url': 'https://github.com/topics/html-projects'}
            }
        },
        {
            'skill': 'CSS', 'level': 'Beginner',
            'explanation': 'CSS makes websites look beautiful. Master layouts, colors, and responsive design with Flexbox and Grid.',
            'resources': {
                'beginner': {'name': 'CSS Tutorial (Kevin Powell)', 'url': 'https://www.youtube.com/watch?v=1PnVor36_40'},
                'intermediate': {'name': 'CSS Full Course (FreeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=OXGznpKZ_sA'},
                'practice': {'name': 'Flexbox Froggy', 'url': 'https://flexboxfroggy.com/'},
                'docs': {'name': 'CSS MDN Docs', 'url': 'https://developer.mozilla.org/en-US/docs/Web/CSS'},
                'project': {'name': 'Responsive Landing Page', 'url': 'https://github.com/topics/css-projects'}
            }
        },
        {
            'skill': 'JavaScript', 'level': 'Beginner',
            'explanation': 'JavaScript adds interactivity. It is the only language that runs in the browser and is essential for modern web apps.',
            'resources': {
                'beginner': {'name': 'JavaScript for Beginners', 'url': 'https://www.youtube.com/watch?v=EerdGm-ehVw'},
                'intermediate': {'name': 'JS Full Course (FreeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=jS4aFq5-91M'},
                'practice': {'name': 'Codewars Challenges', 'url': 'https://www.codewars.com/'},
                'docs': {'name': 'JavaScript Reference', 'url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript'},
                'project': {'name': 'Interactive To-Do List', 'url': 'https://github.com/topics/javascript-projects'}
            }
        },
        {
            'skill': 'Git', 'level': 'Beginner',
            'explanation': 'Version control is mandatory. Learn to track changes and collaborate with others using Git and GitHub.',
            'resources': {
                'beginner': {'name': 'Git & GitHub (Mosh)', 'url': 'https://www.youtube.com/watch?v=RGOj5yH7evk'},
                'intermediate': {'name': 'Git Full Course', 'url': 'https://www.youtube.com/watch?v=apGV9Kg7ics'},
                'practice': {'name': 'Learn Git Branching', 'url': 'https://learngitbranching.js.org/'},
                'docs': {'name': 'Git Documentation', 'url': 'https://git-scm.com/doc'},
                'project': {'name': 'Open Source Contribution', 'url': 'https://github.com/firstcontributions/first-contributions'}
            }
        },
        {
            'skill': 'APIs', 'level': 'Intermediate',
            'explanation': 'Connect your app to the world. Learn how to fetch data from REST and GraphQL APIs.',
            'resources': {
                'beginner': {'name': 'APIs for Beginners', 'url': 'https://www.youtube.com/watch?v=GZvSYJDk-us'},
                'intermediate': {'name': 'What is an API? (Fireship)', 'url': 'https://www.youtube.com/watch?v=-MTSQjw5DrM'},
                'practice': {'name': 'Postman Challenges', 'url': 'https://www.postman.com/api-network/'},
                'docs': {'name': 'JSON Placeholder (Fake API)', 'url': 'https://jsonplaceholder.typicode.com/'},
                'project': {'name': 'Weather Fetcher App', 'url': 'https://github.com/topics/api-projects'}
            }
        },
        {
            'skill': 'React', 'level': 'Intermediate',
            'explanation': 'The most popular frontend library. Build complex UIs efficiently using components and hooks.',
            'resources': {
                'beginner': {'name': 'React Course (FreeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=bMknfKXIFA8'},
                'intermediate': {'name': 'React Tutorial for Beginners', 'url': 'https://www.youtube.com/watch?v=SqcY0GlETPk'},
                'practice': {'name': 'Frontend Mentor Challenges', 'url': 'https://www.frontendmentor.io/'},
                'docs': {'name': 'Official React Docs', 'url': 'https://react.dev/'},
                'project': {'name': 'Build a Social Media Dashboard', 'url': 'https://github.com/topics/react-projects'}
            }
        },
        {
            'skill': 'Node.js', 'level': 'Advanced',
            'explanation': 'Take JavaScript to the server. Build fast and scalable backend systems using Node and Express.',
            'resources': {
                'beginner': {'name': 'Node.js Full Course', 'url': 'https://www.youtube.com/watch?v=Oe421EPjeBE'},
                'intermediate': {'name': 'Express.js Crash Course', 'url': 'https://www.youtube.com/watch?v=L72fhGm1tfE'},
                'practice': {'name': 'FreeCodeCamp Back End Cert', 'url': 'https://www.freecodecamp.org/learn/back-end-development-and-apis/'},
                'docs': {'name': 'Node.js Documentation', 'url': 'https://nodejs.org/en/docs/'},
                'project': {'name': 'Real-time Chat App', 'url': 'https://github.com/topics/nodejs-projects'}
            }
        },
        {
            'skill': 'MongoDB', 'level': 'Advanced',
            'explanation': 'A modern NoSQL database that works perfectly with JavaScript. Store and manage data for your web apps.',
            'resources': {
                'beginner': {'name': 'MongoDB Crash Course (Mosh)', 'url': 'https://www.youtube.com/watch?v=pWbMrx5rVBE'},
                'intermediate': {'name': 'MongoDB Full Course', 'url': 'https://www.youtube.com/watch?v=ExcRbA7xyS8'},
                'practice': {'name': 'Mongoose ODM Tutorial', 'url': 'https://mongoosejs.com/docs/guide.html'},
                'docs': {'name': 'MongoDB Docs', 'url': 'https://www.mongodb.com/docs/'},
                'project': {'name': 'E-commerce Database Design', 'url': 'https://github.com/topics/mongodb-projects'}
            }
        }
    ],
    'Cyber Security': [
        {
            'skill': 'Networking', 'level': 'Beginner', 
            'explanation': 'You can\'t secure a network you don\'t understand. Master TCP/IP, OSI, and routing fundamentals.',
            'resources': {
                'beginner': {'name': 'Networking for Cyber Security', 'url': 'https://www.youtube.com/watch?v=qiQR5rTSshw'},
                'intermediate': {'name': 'Networking Basics (Professor Messer)', 'url': 'https://www.youtube.com/watch?v=0_u6_6XF4nE'},
                'practice': {'name': 'TryHackMe Pre-Security Path', 'url': 'https://tryhackme.com/path/outline/presecurity'},
                'docs': {'name': 'Internet Standards Docs', 'url': 'https://www.ietf.org/standards/rfcs/'},
                'project': {'name': 'Packet Capture Analysis', 'url': 'https://github.com/topics/networking'}
            }
        },
        {
            'skill': 'Linux', 'level': 'Beginner',
            'explanation': 'Security tools and servers run on Linux. Mastering the command line is your primary weapon.',
            'resources': {
                'beginner': {'name': 'Linux for Cyber Security', 'url': 'https://www.youtube.com/watch?v=3p_jB8B6XvM'},
                'intermediate': {'name': 'Linux Full Course (FreeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=wBp0Rb-ZJak'},
                'practice': {'name': 'OverTheWire Bandit', 'url': 'https://overthewire.org/wargames/bandit/'},
                'docs': {'name': 'Kali Linux Docs', 'url': 'https://www.kali.org/docs/'},
                'project': {'name': 'Automated Scripting for Security', 'url': 'https://github.com/topics/linux-projects'}
            }
        },
        {
            'skill': 'Kali Linux', 'level': 'Intermediate',
            'explanation': 'The OS of hackers. Learn to use its suite of offensive and defensive tools.',
            'resources': {
                'beginner': {'name': 'Kali Linux Full Course', 'url': 'https://www.youtube.com/watch?v=mY9Yv-NmsF4'},
                'intermediate': {'name': 'Kali Linux Tutorial', 'url': 'https://www.youtube.com/watch?v=f9nOnU-N6_w'},
                'practice': {'name': 'Nmap Hands-On Lab', 'url': 'https://nmap.org/book/man.html'},
                'docs': {'name': 'Metasploit Guide', 'url': 'https://docs.metasploit.com/'},
                'project': {'name': 'Penetration Testing Simulation', 'url': 'https://github.com/topics/kali-linux'}
            }
        },
        {
            'skill': 'Cryptography', 'level': 'Intermediate',
            'explanation': 'The math behind security. Learn how encryption, hashing, and digital signatures protect data.',
            'resources': {
                'beginner': {'name': 'Cryptography for Beginners', 'url': 'https://www.youtube.com/watch?v=NuyzuNBFWxc'},
                'intermediate': {'name': 'Intro to Cryptography', 'url': 'https://www.youtube.com/watch?v=EDC6U2S_5L4'},
                'practice': {'name': 'CryptoHack Challenges', 'url': 'https://cryptohack.org/'},
                'docs': {'name': 'OpenSSL Documentation', 'url': 'https://www.openssl.org/docs/'},
                'project': {'name': 'Build a Secure Messaging Tool', 'url': 'https://github.com/topics/encryption'}
            }
        },
        {
            'skill': 'Ethical Hacking', 'level': 'Advanced',
            'explanation': 'Think like a hacker to stop one. Master the methodology of penetration testing.',
            'resources': {
                'beginner': {'name': 'Ethical Hacking Course (TCM)', 'url': 'https://www.youtube.com/watch?v=3Kq1MIfTWCE'},
                'intermediate': {'name': 'Ethical Hacking Full Course', 'url': 'https://www.youtube.com/watch?v=dz7Ntp7zv8w'},
                'practice': {'name': 'Hack The Box Labs', 'url': 'https://www.hackthebox.com/'},
                'docs': {'name': 'OWASP Top 10', 'url': 'https://owasp.org/www-project-top-ten/'},
                'project': {'name': 'Vulnerability Assessment Project', 'url': 'https://github.com/topics/ethical-hacking'}
            }
        },
        {
            'skill': 'Threat Analysis', 'level': 'Advanced',
            'explanation': 'Identify and neutralize threats before they cause damage. Learn to analyze malware and attacks.',
            'resources': {
                'beginner': {'name': 'Threat Intelligence Basics', 'url': 'https://www.youtube.com/watch?v=6m82Xz8L3C8'},
                'intermediate': {'name': 'Cyber Threat Intelligence', 'url': 'https://www.youtube.com/watch?v=tY8D_T7m3eA'},
                'practice': {'name': 'Blue Team Labs Online', 'url': 'https://blueteamlabs.online/'},
                'docs': {'name': 'MITRE ATT&CK Framework', 'url': 'https://attack.mitre.org/'},
                'project': {'name': 'Incident Response Simulation', 'url': 'https://github.com/topics/threat-analysis'}
            }
        },
        {
            'skill': 'SIEM', 'level': 'Expert',
            'explanation': 'The eye of the SOC. Learn to monitor enterprise-wide security events and respond to incidents.',
            'resources': {
                'beginner': {'name': 'SIEM Explained', 'url': 'https://www.youtube.com/watch?v=ZfH2OPrvH3A'},
                'intermediate': {'name': 'Splunk Fundamentals (Free)', 'url': 'https://www.splunk.com/en_us/training/free-courses/splunk-fundamentals-1.html'},
                'practice': {'name': 'SIEM Home Lab Setup', 'url': 'https://github.com/topics/siem'},
                'docs': {'name': 'Microsoft Sentinel Docs', 'url': 'https://learn.microsoft.com/en-us/azure/sentinel/'},
                'project': {'name': 'SOC Analyst Dashboard Project', 'url': 'https://github.com/topics/soc'}
            }
        }
    ],
    'Software Developer': [
        {
            'skill': 'Java', 'level': 'Beginner', 
            'explanation': 'A robust, typed language. Java is the foundation for large-scale enterprise software and Android development.',
            'resources': {
                'beginner': {'name': 'Java Full Course (Mosh)', 'url': 'https://www.youtube.com/watch?v=eIrMbLywjVk'},
                'intermediate': {'name': 'Java Tutorial for Beginners', 'url': 'https://www.youtube.com/watch?v=grEKMHGYyz4'},
                'practice': {'name': 'CodingBat Java', 'url': 'https://codingbat.com/java'},
                'docs': {'name': 'Official Java Tutorials', 'url': 'https://docs.oracle.com/javase/tutorial/'},
                'project': {'name': 'Inventory Management System', 'url': 'https://github.com/topics/java-projects'}
            }
        },
        {
            'skill': 'Python', 'level': 'Beginner',
            'explanation': 'The most versatile language. Used for scripting, web backend, and automation.',
            'resources': {
                'beginner': {'name': 'Python Crash Course (Mosh)', 'url': 'https://www.youtube.com/watch?v=_uQrJ0TkZlc'},
                'intermediate': {'name': 'Python Full Course (FreeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=rfscVS0vtbw'},
                'practice': {'name': 'Edabit Python Challenges', 'url': 'https://edabit.com/challenges/python'},
                'docs': {'name': 'Python Developer Guide', 'url': 'https://devguide.python.org/'},
                'project': {'name': 'Automated Finance Tracker', 'url': 'https://github.com/topics/python-projects'}
            }
        },
        {
            'skill': 'OOP', 'level': 'Intermediate',
            'explanation': 'The paradigm of professional coding. Learn to build modular, reusable systems using objects and classes.',
            'resources': {
                'beginner': {'name': 'OOP in 7 Minutes (Mosh)', 'url': 'https://www.youtube.com/watch?v=pTB0EiLXUC8'},
                'intermediate': {'name': 'SOLID Principles Explained', 'url': 'https://www.youtube.com/watch?v=v-274SleCYM'},
                'practice': {'name': 'Refactoring Guru', 'url': 'https://refactoring.guru/'},
                'docs': {'name': 'Microsoft OOP Guide', 'url': 'https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/tutorials/oop'},
                'project': {'name': 'Library Management System', 'url': 'https://github.com/topics/oop-projects'}
            }
        },
        {
            'skill': 'DBMS', 'level': 'Intermediate',
            'explanation': 'Every real app needs a database. Learn to design schemas and manage data efficiently.',
            'resources': {
                'beginner': {'name': 'DBMS Full Course', 'url': 'https://www.youtube.com/watch?v=kB6YNYBaE8M'},
                'intermediate': {'name': 'Database Design Tutorial', 'url': 'https://www.youtube.com/watch?v=ztHopE5Wnpc'},
                'practice': {'name': 'SQL Exercises', 'url': 'https://sqlbolt.com/'},
                'docs': {'name': 'MySQL Reference Manual', 'url': 'https://dev.mysql.com/doc/'},
                'project': {'name': 'Student Management System DB', 'url': 'https://github.com/topics/dbms-projects'}
            }
        },
        {
            'skill': 'Git', 'level': 'Intermediate',
            'explanation': 'Collaboration is key. Git is the standard for version control and teamwork in software development.',
            'resources': {
                'beginner': {'name': 'Git Mastery (Mosh)', 'url': 'https://www.youtube.com/watch?v=RGOj5yH7evk'},
                'intermediate': {'name': 'Git & GitHub Full Course', 'url': 'https://www.youtube.com/watch?v=apGV9Kg7ics'},
                'practice': {'name': 'Learn Git Branching', 'url': 'https://learngitbranching.js.org/'},
                'docs': {'name': 'GitHub Docs', 'url': 'https://docs.github.com/en'},
                'project': {'name': 'Open Source Collaboration', 'url': 'https://github.com/topics/hacktoberfest'}
            }
        },
        {
            'skill': 'DSA', 'level': 'Advanced',
            'explanation': 'The heart of software. Master data structures and algorithms to write efficient, high-performance code.',
            'resources': {
                'beginner': {'name': 'DSA for Beginners (Mosh)', 'url': 'https://www.youtube.com/watch?v=8hly31xKli0'},
                'intermediate': {'name': 'Algorithms Full Course (FCC)', 'url': 'https://www.youtube.com/watch?v=RBSGKlAvoiM'},
                'practice': {'name': 'LeetCode 75', 'url': 'https://leetcode.com/studyplan/leetcode-75/'},
                'docs': {'name': 'GeeksforGeeks DSA', 'url': 'https://www.geeksforgeeks.org/data-structures/'},
                'project': {'name': 'Pathfinding Visualizer', 'url': 'https://github.com/topics/dsa-projects'}
            }
        },
        {
            'skill': 'Problem Solving', 'level': 'Advanced',
            'explanation': 'Translate logic into code. This skill is critical for technical interviews and day-to-day engineering.',
            'resources': {
                'beginner': {'name': 'Problem Solving Strategies', 'url': 'https://www.youtube.com/watch?v=Yn89qS3A86c'},
                'intermediate': {'name': 'Technical Interview Guide', 'url': 'https://www.youtube.com/watch?v=uQit2S1PT_8'},
                'practice': {'name': 'Codewars Katas', 'url': 'https://www.codewars.com/'},
                'docs': {'name': 'Competitive Programming Handbook', 'url': 'https://cses.fi/book/book.pdf'},
                'project': {'name': 'Complex Algorithm Implementation', 'url': 'https://github.com/topics/coding-challenges'}
            }
        },
        {
            'skill': 'System Design', 'level': 'Expert',
            'explanation': 'Design global systems. Learn how to architect apps that scale to millions of users.',
            'resources': {
                'beginner': {'name': 'System Design for Beginners', 'url': 'https://www.youtube.com/watch?v=m8ICP_MCcE0'},
                'intermediate': {'name': 'System Design Primer', 'url': 'https://github.com/donnemartin/system-design-primer'},
                'practice': {'name': 'Grokking System Design', 'url': 'https://www.educative.io/courses/grokking-the-system-design-interview'},
                'docs': {'name': 'High Scalability Blog', 'url': 'http://highscalability.com/'},
                'project': {'name': 'Scalable E-commerce Architecture', 'url': 'https://github.com/topics/system-design'}
            }
        }
    ]
}
