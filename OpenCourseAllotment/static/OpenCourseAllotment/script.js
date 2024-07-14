document.addEventListener('DOMContentLoaded', ()=> {
    toggleRegister();
});

// ! Register User Toggler
function toggleRegister() {
    let buttons = document.querySelectorAll('.reg-buttons button');
    let trReg = document.querySelector('.tr-reg');
    let studReg = document.querySelector('.stud-reg');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            // Use the 'data' attribute to find which button has been clicked
            if (this.dataset.role == "teacher") {
                trReg.style.display = 'block';
                studReg.style.display = 'none';
                console.log('a');
            } else {
                trReg.style.display = 'none';
                studReg.style.display = 'block';
                console.log('b');
            }
        });
    });
}

// ! Add Choice for Application
function addChoice() {
    let addOptionDiv = document.querySelector('.add-option');
    let choice = document.querySelectorAll('.choice');
    let choiceChildren = document.querySelectorAll('.choice > *');
    choiceChildren.forEach(child => {
        console.log(child.id);
    });
    
}

