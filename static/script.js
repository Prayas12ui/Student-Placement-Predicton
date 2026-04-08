document.addEventListener('DOMContentLoaded', () => {
    // Load metrics on startup
    fetch('/metrics')
        .then(response => response.json())
        .then(data => {
            if (!data.error) {
                document.getElementById('modelName').textContent = data.best_model;
                document.getElementById('modelAccuracy').textContent = data.accuracy;
                document.getElementById('modelPrecision').textContent = data.precision;
                document.getElementById('modelRecall').textContent = data.recall;
            }
        })
        .catch(error => console.error("Error loading metrics:", error));

    const form = document.getElementById('predictionForm');
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

            if (result.success) {
                if (result.prediction === "Placed") {
                    predictionResult.textContent = "🎉 Placed!";
                    predictionResult.classList.add('result-placed');
                    
                    predictionExplanation.textContent = "This profile looks strong for placement.";
                    predictionExplanation.classList.remove('hidden');
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
});
