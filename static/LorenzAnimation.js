document.addEventListener("DOMContentLoaded", function () {
    const selectBtn = document.querySelector(".select-btn");
    const saveBtn = document.querySelector(".save-btn");
    const resetBtn = document.querySelector(".reset-btn");
    const itemInputs = document.querySelectorAll(".item-input");

    let validSigma = false;
    let validRho = false;
    let validTime = false;
    let validIterations = false;
    let validX = false;
    let validY = false;
    let validZ = false;

    let validButton = false

    let LorenzValues = []

    selectBtn.addEventListener("click", () => {
        selectBtn.classList.toggle("open");

        itemInputs.forEach((input) => {
            const errorMessage = input.parentElement.querySelector(".error-message");
            const exclamationIcon = input.parentElement.querySelector(".fa-exclamation-circle");
            
            errorMessage.style.display = "none";
            exclamationIcon.style.display = "none"; // Hide exclamation point
        });

        // Toggle the display of the Save button
        if (selectBtn.classList.contains("open")) {
            saveBtn.style.display = "block";
            resetBtn.style.display = "block";

            if(LorenzValues.length === 7){
                // Loop through LorenzValues array and set values back into text fields
                LorenzValues.forEach((value, index) => {
                    itemInputs[index].value = value;
                });
        
                validSigma = true;
                validRho = true;
                validTime = true;
                validIterations = true;
                validX = true;
                validY = true;
                validZ = true;

                saveBtn.style.backgroundColor = "#3E96F4";
                validButton = true
                }

        } else {
            saveBtn.style.display = "none";
            resetBtn.style.display = "none";
            // Clear the values in the text fields when the dropdown is closed
            itemInputs.forEach((input) => {
                input.value = "";
            });

            validSigma = false;
            validRho = false;
            validTime = false;
            validIterations = false;
            validX = false;
            validY = false;
            validZ = false;

            saveBtn.style.backgroundColor = "grey";
            validButton = false
        }
    });

    // Add event listener to each input field
    itemInputs.forEach((input) => {
        input.addEventListener("keypress", (event) => {
            // Check if text is selected
            const isTextSelected = document.getSelection().toString() !== '';

            // Check if the pressed key is Enter
            if (event.key === "Enter") {
                // Blur the input field to exit focus
                input.blur();
            }

            if (isTextSelected) {
                // Allow the entered character to replace the selected text
                return;
            }

            if (input.value.length > 8) {
                // Prevent further input
                event.preventDefault();
                return;
            }

            // Allow only digits for Time Span and Iterations
            if (input.classList.contains("time-input") || input.classList.contains("iterations-input")) {
                if (!/^\d$/.test(event.key)) {
                    event.preventDefault();
                }
            } else {
                // Allow only digits and at most one decimal point for other fields
                if (!/^\d$/.test(event.key) && !(event.key === "." && !input.value.includes("."))) {
                    event.preventDefault();
                }
                if (input.value.split(".")[1]?.length >= 3) {
                    event.preventDefault();
                }
            }
        });

        // Add blur event listener to handle clicking off the text field
        input.addEventListener("blur", () => {
            // Remove the last decimal point if it exists
            if (input.value.endsWith(".")) {
                input.value = input.value.slice(0, -1);
            }

            // Remove the first zero if not followed by a decimal point and if the input value is greater than 1 character
            if (/^0(?!\.)/.test(input.value) && input.value.length > 1) {
                input.value = input.value.substring(1);
            }

            // Hide error message and exclamation point for the current input
            checkErrorElements(input);
            checkValidInputs();
        });

        // Trigger initial hiding on page load
        hideErrorElements(input);
        checkValidInputs();
    });

    function checkErrorElements(input){
        const errorMessage = input.parentElement.querySelector(".error-message");
        const exclamationIcon = input.parentElement.querySelector(".fa-exclamation-circle");
        const choiceName = input.parentElement.querySelector(".item-text").textContent.trim();

        // Parse the input value as a float
        const value = parseFloat(input.value);

        // Define ranges for each choice option
        const ranges = {
            "Sigma": {min: 5.0, max: 10.0},
            "Rho": {min: 20.0, max: 40.0},
            "Time": {min: 20, max: 100},
            "Iterations": {min: 20, max: 100},
            "X": {min: 0.001, max: 0.999},
            "Y": {min: 0.001, max: 0.999},
            "Z": {min: 0.001, max: 0.999},
            // Add other choices and their ranges as needed
        };

        // Check if the value is outside the specified range for the current choice
        if (isNaN(value) || value < ranges[choiceName].min || value > ranges[choiceName].max) {
            errorMessage.style.display = "block";
            exclamationIcon.style.display = "inline"; // Show exclamation point

            if(choiceName == "Sigma"){
                validSigma = false
            }
            else if(choiceName == "Rho"){
                validRho = false
            }
            else if(choiceName == "Time"){
                validTime = false
            }
            else if(choiceName == "Iterations"){
                validIterations = false
            }
            else if(choiceName == "X"){
                validX = false
            }
            else if(choiceName == "Y"){
                validY = false
            }
            else if(choiceName == "Z"){
                validZ = false
            }

        } else {
            errorMessage.style.display = "none";
            exclamationIcon.style.display = "none"; // Hide exclamation point

            if(choiceName == "Sigma"){
                validSigma = true
            }
            else if(choiceName == "Rho"){
                validRho = true
            }
            else if(choiceName == "Time"){
                validTime = true
            }
            else if(choiceName == "Iterations"){
                validIterations = true
            }
            else if(choiceName == "X"){
                validX = true
            }
            else if(choiceName == "Y"){
                validY = true
            }
            else if(choiceName == "Z"){
                validZ = true
            }
        }
    }

    // Function to hide error message and exclamation point
    function hideErrorElements(input) {
        const errorMessage = input.parentElement.querySelector(".error-message");
        const exclamationIcon = input.parentElement.querySelector(".fa-exclamation-circle");

        errorMessage.style.display = "none";
        exclamationIcon.style.display = "none";
    }

    function checkValidInputs(){
        if(validSigma && validRho && validTime && validIterations && validX && validY && validZ){
            saveBtn.style.backgroundColor = "#3E96F4";
            validButton = true
        }
        else{
            saveBtn.style.backgroundColor = "grey";
            validButton = false
        }
    }

    // Add event listener for the Save button click
    saveBtn.addEventListener("click", () => {
        if(validButton){
        // Clear the array before adding new values
        LorenzValues = [];

        // Loop through all text fields and store their values in LorenzValues array
        itemInputs.forEach((input) => {
            LorenzValues.push(input.value);
        });

        // Print the values in the console
        console.log("LorenzValues:", LorenzValues);

         // Add a class to trigger the button press animation
         saveBtn.classList.add("pressed");
        
         // Remove the class after a short delay to reset the button appearance
         setTimeout(() => {
             saveBtn.classList.remove("pressed");
         }, 150);
        }
    });

    // Add event listener for the Save button click
    resetBtn.addEventListener("click", () => {
        // Add a class to trigger the button press animation
        resetBtn.classList.add("pressed");
        
        // Remove the class after a short delay to reset the button appearance
        setTimeout(() => {
            resetBtn.classList.remove("pressed");
        }, 150);

        LorenzValues = [];

        itemInputs.forEach((input) => {
            const errorMessage = input.parentElement.querySelector(".error-message");
            const exclamationIcon = input.parentElement.querySelector(".fa-exclamation-circle");
            
            errorMessage.style.display = "none";
            exclamationIcon.style.display = "none"; // Hide exclamation point
        });

        itemInputs.forEach((input) => {
            input.value = "";
        });

        validSigma = false;
        validRho = false;
        validTime = false;
        validIterations = false;
        validX = false;
        validY = false;
        validZ = false;

        saveBtn.style.backgroundColor = "grey";
        validButton = false
    });
    
});