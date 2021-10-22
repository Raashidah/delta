function login() {

    Mobile = document.getElementById("Mobile");
    password = document.getElementById("password");


    if (Mobile.value == "" || isNaN(Mobile.value) ) {
        Mobile.style.borderColor = "red";
        document.getElementById('mob').innerHTML = "Enter your mobile number";
        Mobile.focus();
        return false;

    }
    else if( Mobile.value.length!=10){
        document.getElementById('mob').innerHTML = "Length should be 10";
        Mobile.focus();
        return false;
    }
    else if(password.value==""){
      password.style.borderColor="red";
      password.focus();
      document.getElementById('pas').innerHTML = "enter your password";
      
      return false;
  }
  else if(password.value.length < 8){
      password.style.borderColor="red";
      password.focus();
      document.getElementById('pas').innerHTML = "invalid password";
     
      return false;
  }
    else {
        return true;
    }
}
