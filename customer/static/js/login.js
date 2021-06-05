
function login(){
   var mobile=Number(document.getElementById("Mobile").value);
   var password=document.getElementById("password").value;

    if(mobile==9037738575 && password=="admin"){
        alert("login successfully");
        
    }
    else
    {
        alert("login failed");
    }
}
