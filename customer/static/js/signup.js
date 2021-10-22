$(document).ready(function () {
    $("form[name='sign']").validate({
        rules: {
            firstname: {
                required: true,
                
            },
            mn: {
                required: true,
                maxlength: 10,
            },
            email: {
                required: true,
                email: true,
            },
            address:{
                required: true,

            },
            pwd: {
                required: true,
                minlength: 8,
                maxlength: 12,
            },
            pwd2: {
                required: true,
                equalTo: '#pas1',
            }
            },
            messages: {
                firstname:{
                    required:"please enter your name"
                },
                mn: {
                    required: "please enter your mobile number",
                    maxlength: "enter 10 digits"
                },
                email: {
                    email: "please enter a valid email address"
                },
                address:{
                    required: "please enter your address"
    
                },
                pwd: {
                    required: "please enter your password",
                    minlength: "length of password should be minimum 8",
                    maxlength: "maximum length of password is 12",
                },
                
            },
            submitHandler:function(form){
                form.submit();
            }
     })

})

function myFunction1() {
        var x = document.getElementById("pas1");
        if (x.type === "password") {
            x.type = "text";
        } else {
            x.type = "password";
        }
        var x = document.getElementById("pas2");
        if (x.type === "password") {
            x.type = "text";
        } else {
            x.type = "password";
        }
        }