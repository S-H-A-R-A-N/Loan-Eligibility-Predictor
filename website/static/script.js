document.getElementById("loanForm").addEventListener("submit", function(e){
    e.preventDefault();

    let age = parseInt(document.getElementById("age").value);
    let income = parseInt(document.getElementById("income").value);
    let education = parseInt(document.getElementById("education").value);
    let credit_score = parseInt(document.getElementById("credit_score").value);
    let employment_status = parseInt(document.getElementById("employment_status").value);
    let loan_amount = parseInt(document.getElementById("loan_amount").value);

    // Simple rule-based prediction (placeholder)
    let result = "Not Approved";
    if(credit_score > 680 && income > 40000 && loan_amount < income*0.5){
        result = "Approved";
    }

    document.getElementById("result").innerText = `Loan Status: ${result}`;
});
