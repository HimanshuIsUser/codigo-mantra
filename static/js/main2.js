
function register(){
    let email = document.getElementById('email').value;
    let name= document.getElementById('username').value;
    let password = document.getElementById('password').value;
    var csrf = document.getElementById('csrf').value;
    alert(email,name,password,csrf)

    if (email == ''){
        alert('Email is required')
    }
    else if(password==''){
        alert('Password is required')
    }
    var data = {
        'email' : email,
        'password':password,
        'name':name
    }
    fetch('/login/register/',{
        method : 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrf,
        },
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => { 
        console.log('response:', response.data.email);
        if (response.status === 200){
            localStorage.setItem('access_token',response.accessToken)
            localStorage.setItem('id',response.user)
            window.location.href = '/';
        }
        else{
            console.log(response);
            alert(response.message);
        }
    })
    .catch(error => {
        console.error(error);
        alert('An error occurred during registration. Please try again later.');
    });
}

function login(){
    var username = document.getElementById('loginusername').value;
    var password = document.getElementById('loginpassword').value;
    var csrf = document.getElementById('csrf').value;

    if (username=='' && password==''){
        alert('You have to enter both')
        return;
    }

    var data = {
        'email':username,
        'password':password
    }

    fetch('/login/login/',{
        method : 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrf,
        },
        
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        console.log('response:', response);
        if (response.status === 200){
            console.log(response.access_token);
            localStorage.setItem('access_token',response.access_token)
            localStorage.setItem('id',response.user)
            console.log(localStorage.getItem('access_token'))
            window.location.href = '/';
        }
        else{
            console.log('No user Found');
            alert('No User Found');
        }
    })
    .catch(error => {
        console.error(error);
        alert('An error occurred during login. Please try again later.');
    });

}

function contact(){
    alert("thank you")
    var first_name = document.getElementById('first_name').value;
    var last_name = document.getElementById('last_name').value;
    var email = document.getElementById('email').value;
    var subject = document.getElementById('subject').value;
    var text = document.getElementById('text').value;
    var csrf = document.getElementById('csrf').value;
    if (first_name=='' && last_name=='' && email=="" && subject=="" && text==""){
        alert('You have to fill all details')
    }

    var data = {
        'email':email,
        'first_name':first_name,
        'last_name':last_name,
        'subject':subject,
        'text':text
    }

    fetch('/contactus/',{
        method : 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrf,
        },
        
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => { 
        console.log('response:', response);
        if (response.status === 200){
            alert("Thank you for contacting us")
        }
        else{
            alert("Try again")
        }
    })
    .catch(error => {
        console.error(error);
        alert('An error occurred during login. Please try again later.');
    });

}

const accessToken = localStorage.getItem('access_token');
const loginButton = document.getElementById('login-button');
const logoutButton = document.getElementById('logout-button');
const commentsection = document.getElementById('comment_section');

if (accessToken) {
    console.log(accessToken)
    // If an access token is present, show the logout button and hide the login button
    logoutButton.style.display = 'inline-block';
    loginButton.style.display = 'none';
    commentsection.style.display = 'inline-block';


  } else {
    // If no access token is present, show the login button and hide the logout button
    loginButton.style.display = 'inline-block';
    logoutButton.style.display = 'none';
    commentsection.style.display = 'none';
  }


function logout() {
    // Remove the access token from localStorage and hide the logout button
    localStorage.removeItem('access_token');
    localStorage.removeItem('id');
    logoutButton.style.display = 'none';
    loginButton.style.display = 'inline-block';

}