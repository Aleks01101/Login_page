const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
// const form_fields = document.getElementsByTagName('input');

// form_fields[1].placeholder = 'Username..';
// form_fields[2].placeholder = 'Email..';
// form_fields[3].placeholder = 'Enter password..';
// form_fields[4].placeholder = 'Re-enter password..';

// for (const field in form_fields){
// 	form_fields[field].className += 'form-control'
// }


signUpButton.addEventListener('click', () => 
	container.classList.add('right-panel-active')
);

signInButton.addEventListener('click', () => 
	container.classList.remove('right-panel-active')
);