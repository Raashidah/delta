$(function(){
    $("form[name='login']").validate({
        rules:{
            mobile:{
                required:true,
                maxlength:10,
            },
                pwd:{
                    required:true,
                    minlength: 8,
                    maxlength:12,
                }
        },
         messages:{
             mobile:{
                    required:"please enter your mobile number",
                    maxlength:"enter 10 digits"
            },
            pwd:{
                required:"please enter your password",
                minlength:"length of password should be minimum 8", 
                maxlength:"maximum length of password is 12",
            }
        },
        submitHandler:function(form){
        form.submit();
    }
})
})