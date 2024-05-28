
// Calculation part starts here


function getTextElementValueById(elementId){
    const phoneTotalElement = document.getElementById(elementId);
    const currentPhoneTotalString = phoneTotalElement.innerText;
    const currentPhoneTotal = parseInt(currentPhoneTotalString);
    return currentPhoneTotal;
}

function setTextElementValueById(elementId, value){
    const subTotalElement = document.getElementById(elementId);
    subTotalElement.innerText = value;
}

function calculateSubTotal(){
    // calculate total
    const currentPhoneTotal = getTextElementValueById('one');
    console.log(currentPhoneTotal);
    const currentCaseTotal = getTextElementValueById('two');
    console.log(currentCaseTotal);
    
    const currentSubTotal = currentPhoneTotal + currentCaseTotal;
    setTextElementValueById('sub-total', currentSubTotal);

    // calculate tax
    const taxAmountString = (currentSubTotal * 0.1).toFixed(2);
    const taxAmount = parseFloat(taxAmountString);
    setTextElementValueById('tax-amount', taxAmount);

    const finalAmount = currentSubTotal + taxAmount;
    setTextElementValueById('final-total', finalAmount);
}

/*
    JavaScript code for Phone
*/ 

function updatePhone(isIncrease){
    const phoneField = document.getElementById('phone');
    const phoneString = phoneField.value;
    const previousPhone = parseInt(phoneString);

    let newPhone;

    if(isIncrease){
        newPhone = previousPhone + 1;
    } else{
        newPhone = previousPhone - 1;
    }

    phoneField.value = newPhone;

    return newPhone;
}

function updatePhonePrice(newPhone){
    const totalPrice = newPhone*1219;
    const totalPriceElement = document.getElementById('one');
    totalPriceElement.innerText = `${totalPrice}`;
}

document.getElementById('increasePhone').addEventListener('click', function(){
    const newPhone = updatePhone(true);
    updatePhonePrice(newPhone);

    calculateSubTotal();
})

document.getElementById('decreasePhone').addEventListener('click', function(){
    const newPhone = updatePhone(false);
    updatePhonePrice(newPhone);

    calculateSubTotal();
})


/*Javascript code for Case*/

function updateCase(isIncrease){
    const caseField = document.getElementById('case');
    const caseString = caseField.value;
    const previousCase = parseInt(caseString);

    let newCase;

    if(isIncrease){
        newCase = previousCase + 1;
    }else{
        newCase = previousCase - 1;
    }

    caseField.value = newCase;

    return newCase;
}

function updateCasePrice(newCase){
    const totalCasePrice = newCase * 59;
    const totalCasePriceElement = document.getElementById('two');
    totalCasePriceElement.innerText = `${totalCasePrice}`;
}

document.getElementById('increaseCase').addEventListener('click', function(){
    const newCase = updateCase(true);
    updateCasePrice(newCase);

    calculateSubTotal();
})

document.getElementById('decreaseCase').addEventListener('click', function(){
    const newCase = updateCase(false);
    updateCasePrice(newCase);

    calculateSubTotal();
})

