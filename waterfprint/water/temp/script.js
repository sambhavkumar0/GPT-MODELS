document.addEventListener("DOMContentLoaded", function () {
    const calculateBtn = document.getElementById("shower");
    const stateInput = document.getElementById("flush");
    const waterConsumptionInput = document.getElementById("dishwasher");
    const showerTimeInput = document.getElementById("laundry");
    const dietDropdown = document.getElementById("diet");
    const extraTasksInput = document.getElementById("local");
    const resultDiv = document.getElementById("result");

    calculateBtn.addEventListener("click", function () {
        const state = stateInput.value;
        const waterConsumption = parseFloat(waterConsumptionInput.value) || 0;
        const showerTime = parseFloat(showerTimeInput.value) || 0;
        const diet = dietDropdown.value;
        const extraTasks = extraTasksInput.value;

        // Calculate the total water consumption
        const totalWaterConsumption = waterConsumption + (showerTime * 12); // Assuming 12 liters per minute for showering

        // Create a result message
        const resultMessage = `
            State: ${state}<br>
            Total Water Consumption: ${totalWaterConsumption} liters per day<br>
            Diet: ${diet}<br>
            Extra Water-Using Tasks: ${extraTasks}
        `;

        // Display the result
        resultDiv.innerHTML = resultMessage;
    });
});



// Event listener for the Calculate button
const calculateBtn = document.getElementById('calculate-btn');
calculateBtn.addEventListener('click', updateResult);


document.addEventListener("DOMContentLoaded", function () {
    const displayBtn = document.getElementById("display-btn");
    const stateDropdown = document.getElementById("state-dropdown");
    const selectedStateDiv = document.getElementById("selected-state");

    displayBtn.addEventListener("click", function () {
        const selectedValue = stateDropdown.value;
        const selectedText = stateDropdown.options[stateDropdown.selectedIndex].text;

        if (selectedValue !== "") {
            selectedStateDiv.textContent = `Selected State: ${selectedText}, Counter Value: ${selectedValue}`;
        } else {
            selectedStateDiv.textContent = "Please select a state first.";
        }
    });
});







