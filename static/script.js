const RESOURCES = {
    "10th Marks": "Consider foundational aptitude and logical reasoning courses to offset low marks.",
    "12th Marks": "Focus on core subject fundamentals and showcase advanced college-level certifications.",
    "UG CGPA": "Leverage competitive programming and high-impact open source projects to overshadow your CGPA.",
    "PG CGPA": "Focus on PG-level research projects, papers, or advanced certifications.",
    "Programming Skills": "DSA practice on LeetCode/HackerRank, and fundamental Python/Java/C++ concepts.",
    "Communication Skills": "Mock interviews, HR interview tips, and verbal communication practice on YouTube.",
    "No Internships": "Start building a strong project portfolio and apply for remote or open-source internships.",
    "Few Projects": "Develop full-stack web apps, ML models, or mobile apps and upload to GitHub.",
    "Active Backlogs": "Prioritize clearing active backlogs immediately before scheduling job interviews.",
    "General": "System Design, Advanced DSA, and High-Level Architecture principles."
};

const PREP_PLANS = {
    "10th Marks": "Aptitude, Logical Reasoning, Quantitative Analysis",
    "12th Marks": "Core Fundamentals, Major Subject Foundation",
    "UG CGPA": "Advanced DSA, Competitive Programming, Open Source",
    "PG CGPA": "Research Paper Writing, Specialized Certifications",
    "Programming Skills": "DSA, OOPs, DBMS, OS, Computer Networks",
    "Communication Skills": "HR Questions, Self-Introduction, Group Discussions",
    "No Internships": "Portfolio Building, Resume Optimization, LinkedIn Networking",
    "Few Projects": "Mini Project Development, GitHub Best Practices, Documentation",
    "Active Backlogs": "Syllabus Review, Target Subject Practice Exams",
    "General": "System Design (LLD/HLD), Behavior Modeling"
};



document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('predictionForm');
    
    // Live preview updating
    const updatePreview = () => {
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        
        let weakAreas = [];
        if (parseFloat(data['10th_Marks'] || 100) < 70) weakAreas.push("10th Marks");
        if (parseFloat(data['12th_Marks'] || 100) < 70) weakAreas.push("12th Marks");
        if (data['Degree_Type'] === 'UG' && parseFloat(data['UG_CGPA'] || 10) < 7.0) {
            weakAreas.push("UG CGPA");
        } else if (data['Degree_Type'] === 'PG') {
            if (parseFloat(data['PG_CGPA'] || 10) < 7.0) weakAreas.push("PG CGPA");
            if (parseFloat(data['UG_CGPA'] || 10) < 7.0) weakAreas.push("UG CGPA");
        }
        if (parseInt(data['Programming_Skills'] || 100) < 60) weakAreas.push("Programming Skills");
        if (parseInt(data['Communication_Skills'] || 100) < 60) weakAreas.push("Communication Skills");
        if (parseInt(data['Internships'] || 1) === 0) weakAreas.push("No Internships");
        if (parseInt(data['Projects'] || 5) < 2) weakAreas.push("Few Projects");
        if (parseInt(data['Backlogs'] || 0) > 0) weakAreas.push("Active Backlogs");

        let strongAreas = [];
        if (parseFloat(data['10th_Marks'] || 0) >= 80) strongAreas.push("10th Marks");
        if (parseFloat(data['12th_Marks'] || 0) >= 80) strongAreas.push("12th Marks");
        if (parseFloat(data['UG_CGPA'] || 0) >= 8.0) strongAreas.push("UG CGPA");
        if (parseInt(data['Programming_Skills'] || 0) >= 80) strongAreas.push("Programming");
        if (parseInt(data['Communication_Skills'] || 0) >= 80) strongAreas.push("Communication");
        if (parseInt(data['Internships'] || 0) > 0) strongAreas.push("Internships");
        if (parseInt(data['Projects'] || 0) >= 2) strongAreas.push("Projects");

        const previewContainer = document.getElementById('livePreview');
        if (previewContainer) {
            if (weakAreas.length > 0) {
                previewContainer.innerHTML = `Based on your inputs, focus areas may include: <strong>${weakAreas.join(", ")}</strong>`;
            } else {
                previewContainer.innerHTML = `Based on your inputs, focus areas may include: <em>General Preparation</em>`;
            }
        }
        
        const focusPreview = document.getElementById('focusAreasPreview');
        const strongPreview = document.getElementById('strongAreasPreview');
        const readStatus = document.getElementById('readinessStatus');
        
        if (focusPreview && strongPreview && readStatus) {
            focusPreview.textContent = weakAreas.length > 0 ? weakAreas.join(", ") : "None Detected";
            strongPreview.textContent = strongAreas.length > 0 ? strongAreas.join(", ") : "Building Base";
            
            if (weakAreas.length === 0 && strongAreas.length >= 3) {
                readStatus.innerHTML = `Status: <strong style="color: #10b981;">Highly Ready 🌟</strong>`;
            } else if (weakAreas.length > 3) {
                readStatus.innerHTML = `Status: <strong style="color: #ef4444;">Needs Preparation ⚠️</strong>`;
            } else {
                readStatus.innerHTML = `Status: <strong style="color: #f59e0b;">Getting There 🚀</strong>`;
            }
        }
    };

    form.addEventListener('input', updatePreview);
    form.addEventListener('change', updatePreview);
    updatePreview(); // Trigger once on load

    const resultCard = document.getElementById('resultCard');
    const predictionResult = document.getElementById('predictionResult');
    const submitBtn = document.getElementById('submitBtn');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // UI feedback
        submitBtn.textContent = 'Analyzing Profile...';
        submitBtn.style.opacity = '0.7';
        
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        
        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            const improvementSection = document.getElementById('improvementSection');
            const weakAreasSummary = document.getElementById('weakAreasSummary');
            const improvementList = document.getElementById('improvementList');
            const predictionExplanation = document.getElementById('predictionExplanation');
            
            const assistantContainer = document.getElementById('assistantContainer');
            const resourceList = document.getElementById('resourceList');
            const prepPlanList = document.getElementById('prepPlanList');
            const quizContainer = document.getElementById('quizContainer');
            const quizResults = document.getElementById('quizResults');
            
            const defaultPanel = document.getElementById('defaultRightPanel');
            const resultPanel = document.getElementById('resultRightPanel');
            
            if (defaultPanel) defaultPanel.classList.add('hidden');
            if (resultPanel) resultPanel.classList.remove('hidden');

            resultCard.classList.remove('hidden');
            resultCard.classList.remove('result-placed');
            resultCard.classList.remove('result-not-placed');
            predictionResult.classList.remove('result-placed');
            predictionResult.classList.remove('result-not-placed');
            
            // Reset and hide improvement section initially
            improvementSection.classList.add('hidden');
            predictionExplanation.classList.add('hidden');
            improvementList.innerHTML = '';
            weakAreasSummary.textContent = '';
            
            if(assistantContainer) assistantContainer.classList.add('hidden');
            if(quizContainer) quizContainer.classList.add('hidden');
            if(resourceList) resourceList.innerHTML = '';
            if(prepPlanList) prepPlanList.innerHTML = '';
            if(quizResults) quizResults.innerHTML = '';

            if (result.success) {
                if (result.prediction === "Placed") {
                    predictionResult.textContent = "🎉 Placed!";
                    predictionResult.classList.add('result-placed');
                    
                    predictionExplanation.textContent = "This profile looks strong for placement.";
                    predictionExplanation.classList.remove('hidden');
                    
                    // Show resources for Placed as well
                    const resLi = document.createElement('li');
                    resLi.innerHTML = `<strong>General:</strong> ${RESOURCES["General"]}`;
                    if(resourceList) resourceList.appendChild(resLi);
                    
                    const planLi = document.createElement('li');
                    planLi.innerHTML = `<strong>General:</strong> ${PREP_PLANS["General"]}`;
                    if(prepPlanList) prepPlanList.appendChild(planLi);
                    
                    if(assistantContainer) assistantContainer.classList.remove('hidden');
                } else {
                    predictionResult.textContent = "⚠️ Not Placed";
                    predictionResult.classList.add('result-not-placed');
                    
                    predictionExplanation.textContent = "Based on the input data, this profile may face challenges in placement.";
                    predictionExplanation.classList.remove('hidden');
                    
                    // Generate dynamic suggestions
                    let suggestions = [];
                    let weakAreas = [];
                    
                    if (parseFloat(data['10th_Marks']) < 70) {
                        suggestions.push("Improve your 10th marks baseline or compensate heavily with advanced tech skills.");
                        weakAreas.push("10th Marks");
                    }
                    if (parseFloat(data['12th_Marks']) < 70) {
                        suggestions.push("Focus on strong current academics to offset lower 12th marks.");
                        weakAreas.push("12th Marks");
                    }
                    if (data['Degree_Type'] === 'UG' && parseFloat(data['UG_CGPA']) < 7.0) {
                        suggestions.push("Improve your UG CGPA to at least 7.0+ to meet minimum cutoffs for most companies.");
                        weakAreas.push("UG CGPA");
                    } else if (data['Degree_Type'] === 'PG') {
                        if (parseFloat(data['PG_CGPA']) < 7.0) {
                            suggestions.push("Improve your PG CGPA to at least 7.0+ to increase your competitiveness.");
                            weakAreas.push("PG CGPA");
                        }
                        if (parseFloat(data['UG_CGPA']) < 7.0) {
                            suggestions.push("Improve your past UG CGPA perception with strong PG projects/certifications.");
                            weakAreas.push("UG CGPA");
                        }
                    }
                    if (parseInt(data['Programming_Skills']) < 60) {
                        suggestions.push("Enhance your programming skills by practicing on platforms like LeetCode or HackerRank.");
                        weakAreas.push("Programming Skills");
                    }
                    if (parseInt(data['Communication_Skills']) < 60) {
                        suggestions.push("Work on your communication skills through mock interviews and group discussions.");
                        weakAreas.push("Communication Skills");
                    }
                    if (parseInt(data['Internships']) === 0) {
                        suggestions.push("Try to complete at least one internship. Practical experience is highly valued.");
                        weakAreas.push("No Internships");
                    }
                    if (parseInt(data['Projects']) < 2) {
                        suggestions.push("Build more academic or personal projects to showcase practical application of your skills.");
                        weakAreas.push("Few Projects");
                    }
                    if (parseInt(data['Backlogs']) > 0) {
                        suggestions.push("Clear your active backlogs before placement season begins.");
                        weakAreas.push("Active Backlogs");
                    }
                    
                    if (suggestions.length > 0) {
                        weakAreasSummary.textContent = "Main weak areas: " + weakAreas.join(", ");
                        suggestions.forEach(suggestion => {
                            const li = document.createElement('li');
                            li.className = 'improvement-item';
                            li.textContent = suggestion;
                            improvementList.appendChild(li);
                        });
                        improvementSection.classList.remove('hidden');
                    } else {
                        const li = document.createElement('li');
                        li.className = 'improvement-item';
                        li.textContent = "Your profile is well-rounded, but the competition is high. Consider gaining advanced certifications.";
                        improvementList.appendChild(li);
                        improvementSection.classList.remove('hidden');
                    }
                    
                    // Populate Resources and Prep plans
                    let topicsToPrepare = weakAreas.length > 0 ? weakAreas : ["General"];
                    topicsToPrepare.forEach(area => {
                        if (RESOURCES[area]) {
                            const resLi = document.createElement('li');
                            resLi.innerHTML = `<strong>${area}:</strong> ${RESOURCES[area]}`;
                            resourceList.appendChild(resLi);
                        }
                        if (PREP_PLANS[area]) {
                            const planLi = document.createElement('li');
                            planLi.innerHTML = `<strong>${area}:</strong> ${PREP_PLANS[area]}`;
                            prepPlanList.appendChild(planLi);
                        }
                    });
                    if(assistantContainer) assistantContainer.classList.remove('hidden');
                }
            } else {
                predictionResult.textContent = "Error: " + result.error;
                predictionResult.classList.add('result-not-placed');
            }
        } catch (error) {
            console.error('Error during prediction:', error);
            resultCard.classList.remove('hidden');
            predictionResult.textContent = "An error occurred during prediction.";
            predictionResult.classList.add('result-not-placed');
            
            // ensure these are hidden if there is a network error
            document.getElementById('improvementSection')?.classList.add('hidden');
            document.getElementById('predictionExplanation')?.classList.add('hidden');
            document.getElementById('assistantContainer')?.classList.add('hidden');
        } finally {
            submitBtn.textContent = 'Generate Prediction';
            submitBtn.style.opacity = '1';
        }
    });

    // Dynamic label changes for Degree Level
    const degreeSelect = document.getElementById('degree_type');
    const courseSelect = document.getElementById('course');

    degreeSelect.addEventListener('change', (e) => {
        const val = e.target.value;
        courseSelect.innerHTML = '';
        if (val === 'UG') {
            ['BTech', 'BCA', 'Others'].forEach(course => {
                const opt = document.createElement('option');
                opt.value = course;
                opt.textContent = course;
                courseSelect.appendChild(opt);
            });
        } else {
            ['MCA', 'MTech', 'MBA', 'Others'].forEach(course => {
                const opt = document.createElement('option');
                opt.value = course;
                opt.textContent = course;
                courseSelect.appendChild(opt);
            });
        }
    });

    const startPrepBtn = document.getElementById('startPrepBtn');
    
    if(startPrepBtn) {
        startPrepBtn.addEventListener('click', () => {
            window.location.href = '/topics';
        });
    }

});
