TOPICS_DATA = {
    "dsa": {
        "id": "dsa",
        "title": "Data Structures and Algorithms (DSA)",
        "intro": "DSA focuses on the foundational logic of programming—how to efficiently store (structures) and process (algorithms) data. It forms the core of almost all technical interview rounds.",
        "importance": "Top tech companies prioritize candidates with strong problem-solving capabilities. A solid grasp of DSA acts as proof that you can optimize code for performance and massive scale.",
        "subtopics": [
            "Arrays, Strings & Pointers",
            "Linked Lists, Stacks & Queues",
            "Trees & Graphs",
            "Sorting & Searching Algorithms",
            "Dynamic Programming"
        ],
        "strategy": "Begin by mastering basic data structures before moving to complex algorithms. Dedicate time daily to solve problems on platforms like LeetCode or GeeksforGeeks. Always analyze the precise Time and Space Complexities (Big-O) of your code.",
        "resources": [
            "LeetCode Curriculum",
            "Cracking the Coding Interview (Book)",
            "NeetCode YouTube Channel"
        ],
        "samples": [
            "How do you invert a Binary Tree?",
            "Explain the difference between QuickSort and MergeSort.",
            "Write a function to detect a cycle in a Linked List."
        ]
    },
    "dbms": {
        "id": "dbms",
        "title": "Database Management Systems (DBMS)",
        "intro": "DBMS deals with the design, development, and administration of databases. Knowing how to store, retrieve, and manage data robustly is critical for any backend developer.",
        "importance": "Enterprise applications constantly interact with databases. Poor database design cripples performance, so interviewers rigorously test your understanding of normalization, indexing, and transactional integrity.",
        "subtopics": [
            "ACID Properties",
            "SQL Queries, Joins & Subqueries",
            "Normalization (1NF, 2NF, 3NF, BCNF)",
            "Indexing & Hashing",
            "Transactions & Concurrency Control"
        ],
        "strategy": "Write actual SQL queries rather than just memorizing syntax. Understand the internal mechanisms: how B-Trees make indexing fast, and precisely how Deadlocks occur during concurrent architecture.",
        "resources": [
            "W3Schools SQL Tutorial",
            "Database System Concepts (Silberschatz)",
            "SQLZoo Interactive Practice"
        ],
        "samples": [
            "What is the difference between TRUNCATE and DELETE?",
            "Write a query to find the second highest salary.",
            "Explain exactly how a Clustered Index works."
        ]
    },
    "oops": {
        "id": "oops",
        "title": "Object-Oriented Programming (OOPs)",
        "intro": "OOP is a programming paradigm built entirely around the concept of 'objects' containing data fields and structural methods. It models real-world entities logically into code.",
        "importance": "Nearly all major production codebases (Java, C++, Python setups) are built using OOP. It allows massive teams of engineers to maintain code iteratively, reuse components, and scale easily.",
        "subtopics": [
            "Classes vs Objects",
            "Encapsulation & Data Hiding",
            "Inheritance (Single, Multiple, Hierarchical)",
            "Polymorphism (Overloading vs Overriding)",
            "Abstraction & Interfaces"
        ],
        "strategy": "Don't just memorize definitions—practice building real structures. Design a rough architecture for a 'Parking Lot' or a 'Library Management System' using OOP principles to prove your structural understanding.",
        "resources": [
            "Java T Point OOP Tutorials",
            "Head First Object-Oriented Analysis and Design",
            "GeeksForGeeks System Design Basics"
        ],
        "samples": [
            "What is the Diamond Problem in multiple inheritance?",
            "Design the classes for a Chess Game.",
            "Differentiate between Abstract Classes and Interfaces."
        ]
    },
    "python": {
        "id": "python",
        "title": "Python Programming",
        "intro": "Python is a high-level interpreted language known for its ultra-readable syntax, massive libraries, and dominating presence in AI, Data Science, and backend scripting.",
        "importance": "As scripting and AI become universal, Python fluency is highly demanded. Interviewers test your knowledge of its internal mechanics (memory management) rather than just syntax.",
        "subtopics": [
            "Lists, Tuples, Sets, & Dictionaries",
            "List Comprehension & Generators",
            "Decorators & Context Managers",
            "Memory Management & Garbage Collection",
            "Multithreading vs Multiprocessing (GIL)"
        ],
        "strategy": "Focus intensely on 'Pythonic' code. Learn how memory handles mutable vs immutable types, how the 'yeild' keyword operates, and the limitations brought by the Global Interpreter Lock (GIL).",
        "resources": [
            "Real Python Library",
            "Fluent Python (Book)",
            "Corey Schafer YouTube Series"
        ],
        "samples": [
            "Why is a dictionary faster than a list?",
            "Explain *args and **kwargs natively.",
            "Write a decorator that calculates a function's execution time."
        ]
    },
    "aptitude": {
        "id": "aptitude",
        "title": "Quantitative Aptitude",
        "intro": "Aptitude evaluates your basic mathematical prowess, lateral thinking, and logical deduction speed—often serving as the absolute first elimination criteria in hiring pools.",
        "importance": "No matter how technically gifted you are, failure to pass the initial 30-minute aptitude test will immediately disqualify you from massive corporate placements.",
        "subtopics": [
            "Time, Speed, & Distance",
            "Profit & Loss",
            "Permutations & Combinations",
            "Probability & Statistics",
            "Logical Reasoning (Puzzles, Blood Relations)"
        ],
        "strategy": "Speed is everything. Memorize core fractions, squares, and cubes. Take 20-minute timed mock tests daily to train your brain to recognize patterns and mathematical loops intuitively under pressure.",
        "resources": [
            "IndiaBIX Platform",
            "Quantitative Aptitude by R.S. Aggarwal",
            "PrepInsta Mock Tests"
        ],
        "samples": [
            "A train running at 90 km/hr crosses a pole in 10s. Length of the train?",
            "In how many ways can the letters of the word 'LEADER' be arranged?",
            "Calculate probability of drawing two Kings consecutively."
        ]
    },
    "hr": {
        "id": "hr",
        "title": "HR & Behavioral Interviews",
        "intro": "The HR round is the final gatekeeper aiming to assess your cultural fit, professionalism, communication skills, and response to immense corporate pressure.",
        "importance": "Failing the HR round after passing all technical assessments is tragically common. Companies reject brilliant coders if they demonstrate arrogance, poor teamwork, or massive instability.",
        "subtopics": [
            "The perfect 'Self Introduction'",
            "Strength and Weakness handling",
            "The STAR Method (Situation, Task, Action, Result)",
            "Handling Conflict and Pressure",
            "Negotiation and Future Trajectory"
        ],
        "strategy": "Prepare a 60-second professional elevator pitch. Structure your life stories using the STAR method so your answers don't ramble. Project immense confidence accompanied by respectful humility.",
        "resources": [
            "STAR Method Preparation Guides",
            "Mock Interviews with Peers",
            "CareerVidz YouTube Channel"
        ],
        "samples": [
            "Tell me about a time you failed.",
            "Where do you see yourself technically in 5 years?",
            "Why should we absolutely hire you over others?"
        ]
    },
    "os": {
        "id": "os",
        "title": "Operating Systems (OS)",
        "intro": "OS concepts detail exactly how software directly interacts with the hardware components—managing pure system resources like the CPU, memory blocks, and I/O files.",
        "importance": "Essential for understanding deep performance bottlenecks. Interviewers expect you to know how multi-application environments handle isolated parallel processing securely via the kernel.",
        "subtopics": [
            "Process Management & Multithreading",
            "CPU Scheduling Algorithms",
            "Deadlocks (Coffman Conditions)",
            "Memory Management (Paging, Virtual Memory)",
            "File Systems"
        ],
        "strategy": "Understand exactly how a process transitions through various execution states. Grasp the theoretical math of paging and how Context Switches physically operate in standard computers.",
        "resources": [
            "Operating System Concepts (Galvin)",
            "Neso Academy OS Playlist",
            "GeeksForGeeks OS Notes"
        ],
        "samples": [
            "Explain exactly what a Semaphore mathematically is.",
            "How does Virtual Memory map to pure physical RAM?",
            "Detail the precise conditions causing a Deadlock."
        ]
    },
    "cn": {
        "id": "cn",
        "title": "Computer Networks (CN)",
        "intro": "Computer Networks cover the literal communication protocols and hardware architectures that securely bind the global internet together.",
        "importance": "Crucial for Backend, API, and Fullstack roles. Understanding how packets travel and how latency degrades performance makes you infinitely more valuable.",
        "subtopics": [
            "OSI & TCP/IP Models",
            "TCP vs UDP Mechanics",
            "HTTP, HTTPS, and DNS resolution",
            "Routing Algorithms",
            "Subnetting & Network Security protocols"
        ],
        "strategy": "Don't just memorize the 7 OSI layers; understand precisely what data headers are injected into packets at every level as they traverse downwards.",
        "resources": [
            "Computer Networking: A Top-Down Approach",
            "Kurose & Ross Textbooks",
            "Cisco CCNA Fundamentals"
        ],
        "samples": [
            "What exactly happens under the hood when you type Google.com?",
            "Describe the intense three-way handshake of TCP.",
            "Why would an architecture choose UDP over TCP?"
        ]
    }
}
