const QUIZ_BANK = {
    dbms: [
        { q: "What does ACID stand for in DBMS?", opts: ["Atomicity, Consistency, Isolation, Durability", "Auto, Consistent, Internal, Database", "Atomicity, Concurrency, Isolation, Duplicate"], ans: 0, fb: "ACID properties guarantee database transactions are processed reliably." },
        { q: "Which command is used to remove all records from a table without logging individual row deletions?", opts: ["DELETE", "DROP", "TRUNCATE", "REMOVE"], ans: 2, fb: "TRUNCATE is a DDL command which is faster than DELETE as it doesn't scan every row." },
        { q: "What is the highest normal form usually achieved in standard database design designed to eliminate transitive dependency?", opts: ["1NF", "2NF", "3NF", "BCNF"], ans: 2, fb: "3NF focuses on removing transitive dependencies." },
        { q: "A primary key cannot contain...", opts: ["Duplicate values", "Null values", "Both A and B", "Foreign keys"], ans: 2, fb: "A primary key must be totally unique and cannot be null." },
        { q: "What type of join returns all rows from the left table and matched rows from the right?", opts: ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"], ans: 1, fb: "Left join prioritizes the left table." },
        { q: "Which of the following is completely not a NoSQL database?", opts: ["MongoDB", "Cassandra", "PostgreSQL", "Redis"], ans: 2, fb: "PostgreSQL is a classic relational sequence-based SQL DB." }
    ],
    oops: [
        { q: "Which of the following is NOT a pillar of OOP?", opts: ["Encapsulation", "Polymorphism", "Compilation", "Abstraction"], ans: 2, fb: "Compilation is a step in program execution, not an OOP concept." },
        { q: "What concept enables a subclass to provide a specific implementation of a method already provided by its parent class?", opts: ["Overloading", "Overriding", "Encapsulation", "Interfaces"], ans: 1, fb: "Method overriding handles dynamic polymorphism at runtime." },
        { q: "Wrapping data and code acting on the data together into a single unit is called?", opts: ["Abstraction", "Inheritance", "Polymorphism", "Encapsulation"], ans: 3, fb: "Encapsulation creates a protective shield that prevents data access from outside the class." },
        { q: "Which OOP concept is used as a blueprint for creating objects?", opts: ["Method", "Attribute", "Class", "Package"], ans: 2, fb: "A class defines the properties and behaviors that objects will hold." },
        { q: "Can a class implement multiple interfaces in languages like Java?", opts: ["Yes", "No", "Only if abstract", "Only 2 maximum"], ans: 0, fb: "Multiple inheritance is achieved via interfaces to avoid the Diamond Problem." }
    ],
    python: [
        { q: "Which of these data structures in Python is immutable?", opts: ["List", "Dictionary", "Set", "Tuple"], ans: 3, fb: "Tuples cannot be changed after creation." },
        { q: "How do you create a function in Python?", opts: ["function myFunc()", "def myFunc():", "void myFunc()", "create myFunc()"], ans: 1, fb: "The 'def' keyword is used to define functions." },
        { q: "What does the 'self' parameter refer to?", opts: ["The class itself", "A global variable", "The current instance of the class", "A reserved keyword in Python"], ans: 2, fb: "'self' points to the object bounding the method." },
        { q: "Which keyword is used to handle exceptions?", opts: ["try...catch", "try...except", "do...catch", "attempt...except"], ans: 1, fb: "Python utilizes try and except blocks." },
        { q: "What does the map() function do?", opts: ["Plots a graph", "Applies a given function to all items in an iterable", "Maps keys to values", "Finds memory addresses"], ans: 1, fb: "Map takes a function and an iterable and applies the function." },
        { q: "What logic is built into Python decorators?", opts: ["Adds additional functionality to a function dynamically", "Used to decorate text output", "Defines class inheritance", "Creates UI elements"], ans: 0, fb: "Decorators wrap functions to extend behavior without modifying original code." }
    ],
    hr: [
        { q: "If an interviewer asks 'What is your biggest weakness?', what is the best strategy?", opts: ["Say you work too hard", "List a genuine flaw and explain how you are actively overcoming it", "Say you don't have any", "Refuse to answer"], ans: 1, fb: "Honesty paired with actionable self-improvement looks exceptional." },
        { q: "When answering behavioral questions, which formatting method should you use?", opts: ["STAR (Situation, Task, Action, Result)", "SMART (Specific, Measurable, Actionable, Result, Time)", "KISS (Keep It Simple)", "SWOT (Strengths, Weaknesses)"], ans: 0, fb: "The STAR method gives structure and depth to story-based answers." },
        { q: "What should you do at the end of an interview?", opts: ["Ask about salary immediately", "Ask thoughtful questions about the role or company", "Pack your bags silently", "Ask if you got the job"], ans: 1, fb: "Asking questions shows engagement and cultural fit." },
        { q: "Why do companies ask 'Tell me about yourself'?", opts: ["To hear your entire life story", "To check if your resume is real", "To assess your communication skills and career trajectory summary", "To fill time"], ans: 2, fb: "It's an ice-breaker designed to see how you pitch your professional self." }
    ],
    aptitude: [
        { q: "A train running at 54 kmph crosses a pole in 20 seconds. What is the length of the train?", opts: ["150m", "200m", "300m", "350m"], ans: 2, fb: "54 km/hr = 15 m/s. 15 * 20 = 300 meters." },
        { q: "If A can do a piece of work in 10 days and B in 15 days, how long do they take together?", opts: ["5 days", "6 days", "8 days", "12 days"], ans: 1, fb: "(10 * 15) / (10 + 15) = 150 / 25 = 6 days." },
        { q: "What is the next number in the series: 2, 6, 12, 20, 30, ...?", opts: ["40", "42", "44", "48"], ans: 1, fb: "Differences are 4, 6, 8, 10, 12. So 30 + 12 = 42." },
        { q: "The cost price of 20 articles is the same as the selling price of x articles. If the profit is 25%, then the value of x is:", opts: ["15", "16", "18", "25"], ans: 1, fb: "20 * CP = x * SP. SP/CP = 20/x. Profit = (SP-CP)/CP = 25%. Thus x = 16." }
    ],
    os: [
        { q: "What causes a deadlock?", opts: ["Mutual Exclusion, Hold and Wait, No preemption, Circular Wait", "Too much RAM", "Using a GUI", "CPU overheating"], ans: 0, fb: "These are the 4 Coffman conditions for logical deadlock." },
        { q: "What is a context switch?", opts: ["Changing the keyboard layout", "Saving the state of a process to load another", "Switching power sources", "Changing file permissions"], ans: 1, fb: "Context switches allow multi-tasking by freezing and unfreezing process states." },
        { q: "What is virtual memory?", opts: ["Cloud storage space", "A technique giving the illusion of a larger main memory using disk space", "Memory inside the GPU", "Cache memory"], ans: 1, fb: "It pages data out to the hard disk to free up active RAM." },
        { q: "Which scheduling algorithm is non-preemptive?", opts: ["Round Robin", "First Come First Serve (FCFS)", "Shortest Remaining Time First", "Multilevel Queue"], ans: 1, fb: "Once a process starts in FCFS, it cannot be interrupted." }
    ],
    cn: [
        { q: "Which layer in the OSI model is responsible for routing?", opts: ["Data Link Layer", "Network Layer", "Transport Layer", "Session Layer"], ans: 1, fb: "The Network layer (Layer 3) handles IP routing." },
        { q: "What is the primary difference between TCP and UDP?", opts: ["TCP is connection-oriented and reliable, UDP is connectionless and fast", "TCP is for local networks, UDP is for internet", "TCP is hardware, UDP is software", "No difference"], ans: 0, fb: "TCP enforces handshakes and packet delivery checks. UDP just blasts data." },
        { q: "What port does HTTPS operate on?", opts: ["80", "21", "443", "22"], ans: 2, fb: "HTTPS utilizes port 443 for encrypted communication." },
        { q: "What translates a domain name (like google.com) into an IP address?", opts: ["DHCP", "DNS", "NAT", "ARP"], ans: 1, fb: "DNS (Domain Name System) is the phonebook of the internet." }
    ]
};

// Utilities
function shuffle(array) {
    let currentIndex = array.length,  randomIndex;
    while (currentIndex != 0) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;
        [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
    }
    return array;
}

function getUnusedQuestions(topicId, rawQuestions, count) {
    const storageKey = `quiz_history_${topicId}`;
    let usedIndexes = JSON.parse(localStorage.getItem(storageKey) || "[]");
    
    // If not enough unseen questions exist, reset the loop
    if (rawQuestions.length - usedIndexes.length < count) {
        usedIndexes = []; // Reset history
    }
    
    let pool = [];
    rawQuestions.forEach((qObj, index) => {
        if (!usedIndexes.includes(index)) {
            pool.push({ ...qObj, originalIndex: index });
        }
    });
    
    shuffle(pool);
    const selected = pool.slice(0, count);
    
    // Save new used indexes
    selected.forEach(q => usedIndexes.push(q.originalIndex));
    localStorage.setItem(storageKey, JSON.stringify(usedIndexes));
    
    return selected;
}

// App State
let currentQuestions = [];
let currentTopic = "";

document.addEventListener('DOMContentLoaded', () => {
    const topicBtns = document.querySelectorAll('.topic-btn');
    const selectionState = document.getElementById('selectionState');
    const activeQuizState = document.getElementById('activeQuizState');
    const analysisState = document.getElementById('analysisState');
    const questionsContainer = document.getElementById('questionsContainer');
    const quizTitle = document.getElementById('quizTitle');
    const submitBtn = document.getElementById('submitQuizBtn');
    
    // Topic Selection
    const handleTopicSelection = (topicId, topicName) => {
        currentTopic = topicId;
        const rawQuestions = QUIZ_BANK[currentTopic];
        
        if(!rawQuestions) {
            alert("Topic not found.");
            return;
        }
        
        // Grab 5 non-repeating questions
        currentQuestions = getUnusedQuestions(currentTopic, rawQuestions, 5);
        
        renderQuiz();
        selectionState.classList.add('hidden');
        activeQuizState.classList.remove('hidden');
        quizTitle.textContent = (topicName || topicId.toUpperCase()) + " Quiz";
    };

    topicBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            handleTopicSelection(e.target.getAttribute('data-topic'), e.target.textContent);
            // Re-write URL gently so it feels stateful
            window.history.replaceState({}, '', `/quiz?topic=${currentTopic}`);
        });
    });

    // Handle initial load param
    const urlParams = new URLSearchParams(window.location.search);
    const initialTopic = urlParams.get('topic');
    if (initialTopic && QUIZ_BANK[initialTopic]) {
        // Attempt to find element text for title
        let matchingBtn = Array.from(topicBtns).find(b => b.getAttribute('data-topic') === initialTopic);
        handleTopicSelection(initialTopic, matchingBtn ? matchingBtn.textContent : initialTopic);
        
        // Dynamically fix the back button to navigate to the specific learning page
        const backBtn = document.getElementById('backBtn');
        if(backBtn) backBtn.href = `/topic/${initialTopic}`;
    }

    function renderQuiz() {
        questionsContainer.innerHTML = '';
        
        currentQuestions.forEach((qObj, index) => {
            // Shuffle options and track new answer index
            let optionsObj = qObj.opts.map((text, i) => ({ text, isCorrect: i === qObj.ans }));
            shuffle(optionsObj);
            
            const card = document.createElement('div');
            card.className = 'question-card';
            card.innerHTML = `<h3>Q${index + 1}: ${qObj.q}</h3>`;
            
            const optionsGroup = document.createElement('div');
            optionsObj.forEach((opt, optIndex) => {
                const label = document.createElement('label');
                label.className = 'option-label';
                
                const radio = document.createElement('input');
                radio.type = 'radio';
                radio.name = `q${index}`;
                radio.value = opt.isCorrect ? 'true' : 'false';
                
                // Add click listener for border highlight visually
                radio.addEventListener('change', () => {
                    const siblings = optionsGroup.querySelectorAll('.option-label');
                    siblings.forEach(sib => sib.classList.remove('selected'));
                    label.classList.add('selected');
                });

                label.appendChild(radio);
                label.appendChild(document.createTextNode(opt.text));
                optionsGroup.appendChild(label);
            });
            
            const feedback = document.createElement('div');
            feedback.className = 'feedback-text';
            feedback.textContent = qObj.fb;
            
            card.appendChild(optionsGroup);
            card.appendChild(feedback);
            questionsContainer.appendChild(card);
        });
    }

    submitBtn.addEventListener('click', () => {
        const cards = questionsContainer.querySelectorAll('.question-card');
        let score = 0;
        let total = currentQuestions.length;

        cards.forEach((card, index) => {
            const options = card.querySelectorAll('.option-label');
            const feedback = card.querySelector('.feedback-text');
            
            let answered = false;
            options.forEach(opt => {
                const radio = opt.querySelector('input');
                if(radio.checked) {
                    answered = true;
                    if(radio.value === 'true') {
                        opt.classList.add('correct');
                        score++;
                    } else {
                        opt.classList.add('wrong');
                    }
                } else if(radio.value === 'true') {
                    // Show what the correct answer was!
                    opt.classList.add('correct');
                }
                radio.disabled = true; // Lock the choice
            });
            
            feedback.style.display = 'block';
        });

        // Show analysis
        document.getElementById('finalScoreText').textContent = `${score} / ${total}`;
        const feedbackText = document.getElementById('scoreFeedback');
        
        if(score === total) {
            feedbackText.textContent = "Flawless! You are extremely well prepared.";
        } else if (score >= total * 0.6) {
            feedbackText.textContent = "Good job! Review the indicated concepts for perfection.";
        } else {
            feedbackText.textContent = "You need more practice in this domain.";
        }

        submitBtn.style.display = 'none';
        analysisState.classList.remove('hidden');
        analysisState.scrollIntoView({ behavior: 'smooth' });
    });

    document.getElementById('retryBtn').addEventListener('click', () => {
        // Restart via same core logic seamlessly
        const matchingBtn = Array.from(topicBtns).find(b => b.getAttribute('data-topic') === currentTopic);
        handleTopicSelection(currentTopic, matchingBtn ? matchingBtn.textContent : currentTopic);
        
        analysisState.classList.add('hidden');
        submitBtn.style.display = 'block';
        window.scrollTo(0, 0);
    });

    document.getElementById('anotherBtn').addEventListener('click', () => {
        window.location.href = '/topics';
    });
});
