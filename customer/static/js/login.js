
// function login(){
//    var mobile=Number(document.getElementById("Mobile").value);
//    var password=document.getElementById("password").value;

//     if(mobile==9037738575 && password=="admin"){
//         alert("login successfully");
        
//     }
//     else
//     {
//         alert("login failed");
//     }
// }


$(function(){
    $("form[name='log']").validate({
        rules:{
            mobile:{
                required:true,
                maxlength:8,
            }
                // password:{
                //     required:true,
                //     minlength: 8,
                //     maxlength:12,
                // }
        },
            messages:{
                mobile:{
                    required:"please enter your mobile number",
                    maxlength:"enter 10 digits"
            }
        },
        submitHandler:function(form){
        form.submit();
    }
})
})