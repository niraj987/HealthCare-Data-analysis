// Tab Navigation
function showTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.style.display = 'none';
    });
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.classList.remove('active');
    });
    
    document.getElementById(tabId).style.display = 'block';
    event.target.classList.add('active');
}

// Chart.js Default styling
Chart.defaults.color = '#9CA3AF';
Chart.defaults.font.family = 'Inter';

// Fetch EDA Data and Render Charts
async function loadEDA() {
    try {
        const response = await fetch('/api/eda_data');
        const data = await response.json();

        // 1. Billing by Admission Chart
        const ctxBilling = document.getElementById('billingChart').getContext('2d');
        new Chart(ctxBilling, {
            type: 'bar',
            data: {
                labels: Object.keys(data.billing_admission),
                datasets: [{
                    label: 'Total Billing Amount ($)',
                    data: Object.values(data.billing_admission),
                    backgroundColor: ['rgba(79, 70, 229, 0.6)', 'rgba(6, 182, 212, 0.6)', 'rgba(236, 72, 153, 0.6)'],
                    borderWidth: 1,
                    borderColor: 'rgba(255, 255, 255, 0.2)'
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false } }
            }
        });

        // 2. Blood Type Chart
        const ctxBlood = document.getElementById('bloodTypeChart').getContext('2d');
        new Chart(ctxBlood, {
            type: 'doughnut',
            data: {
                labels: Object.keys(data.blood_type),
                datasets: [{
                    data: Object.values(data.blood_type),
                    backgroundColor: [
                        '#4F46E5', '#06B6D4', '#EC4899', '#8B5CF6', 
                        '#10B981', '#F59E0B', '#EF4444', '#3B82F6'
                    ],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                cutout: '70%',
                plugins: {
                    legend: { position: 'right' }
                }
            }
        });

        // 3. Condition by Gender Chart (Grouped Bar)
        const conditions = Object.keys(data.condition_gender['Female'] || {});
        const femaleData = conditions.map(c => data.condition_gender['Female'][c] || 0);
        const maleData = conditions.map(c => data.condition_gender['Male'][c] || 0);

        const ctxCondition = document.getElementById('conditionGenderChart').getContext('2d');
        new Chart(ctxCondition, {
            type: 'bar',
            data: {
                labels: conditions,
                datasets: [
                    {
                        label: 'Female',
                        data: femaleData,
                        backgroundColor: 'rgba(236, 72, 153, 0.7)'
                    },
                    {
                        label: 'Male',
                        data: maleData,
                        backgroundColor: 'rgba(59, 130, 246, 0.7)'
                    }
                ]
            },
            options: {
                responsive: true,
                scales: {
                    x: { stacked: false },
                    y: { stacked: false }
                }
            }
        });

    } catch (e) {
        console.error("Error loading EDA data", e);
    }
}

// Prediction APIs
async function predictCondition(e) {
    e.preventDefault();
    const btn = e.target.querySelector('button');
    btn.innerText = "Predicting...";
    
    const payload = {
        Age: parseInt(document.getElementById('c-age').value),
        Gender: document.getElementById('c-gender').value,
        Blood_Type: document.getElementById('c-blood').value,
        Admission_Type: document.getElementById('c-admission').value,
        Test_Results: document.getElementById('c-test').value
    };

    const res = await fetch('/predict/condition', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    const data = await res.json();
    
    const resDiv = document.getElementById('res-condition');
    resDiv.innerText = `Predicted Condition: ${data.prediction}`;
    resDiv.classList.add('show');
    btn.innerText = "Predict Condition";
}

async function predictBilling(e) {
    e.preventDefault();
    const btn = e.target.querySelector('button');
    btn.innerText = "Estimating...";

    const payload = {
        Age: parseInt(document.getElementById('b-age').value),
        Gender: document.getElementById('b-gender').value,
        Medical_Condition: document.getElementById('b-condition').value,
        Admission_Type: document.getElementById('b-admission').value,
        Medication: document.getElementById('b-medication').value
    };

    const res = await fetch('/predict/billing', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    const data = await res.json();

    const resDiv = document.getElementById('res-billing');
    resDiv.innerText = `Estimated Billing: $${data.prediction}`;
    resDiv.classList.add('show');
    btn.innerText = "Estimate Bill";
}

async function predictTest(e) {
    e.preventDefault();
    const btn = e.target.querySelector('button');
    btn.innerText = "Predicting...";

    const payload = {
        Age: parseInt(document.getElementById('t-age').value),
        Gender: document.getElementById('t-gender').value,
        Medical_Condition: document.getElementById('t-condition').value,
        Blood_Type: document.getElementById('t-blood').value,
        Admission_Type: document.getElementById('t-admission').value
    };

    const res = await fetch('/predict/test_results', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    const data = await res.json();

    const resDiv = document.getElementById('res-test');
    resDiv.innerText = `Predicted Test Results: ${data.prediction}`;
    resDiv.classList.add('show');
    btn.innerText = "Predict Test Results";
}

// Load EDA on start
window.onload = loadEDA;
