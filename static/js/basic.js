$(()=> {
    // code copied from https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_modal
    // Get the modal
    var login_modal = document.getElementById("login-modal");
    // Get the button that opens the modal
    var btnlogin = document.getElementById("login");
    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close-login")[0];
    // When the user clicks the button, open the modal 
    btnlogin.onclick = function () {
        login_modal.style.display = "block";
    }
    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        login_modal.style.display = "none";
    }
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == login_modal) {
            login_modal.style.display = "none";
        }
    }
    // Get the modal
    var signup_modal = document.getElementById("signup-modal");
    // Get the button that opens the modal
    var btnsignup = document.getElementById("signup");
    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close-signup")[0];
    // When the user clicks the button, open the modal 
    btnsignup.onclick = function () {
        signup_modal.style.display = "block";
    }
    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        signup_modal.style.display = "none";
    }
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == signup_modal) {
            signup_modal.style.display = "none";
        }
    }
});