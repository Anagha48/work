$(document).ready(function(){
    $("#signup-form").validate({
        rules:{
            fname:{
                required:true,
                minlength:4,
                maxlength:6
                

            },
            $sname:{
                required:true,
                minlength:4
            },
            $num:{
                required:true,
                email:true
            },
            $pswd:{
                minlength:6
                
            },
            day:{
                required:true
            },
            gender:{
                required:true

            },
            messages:{
                fname:{
                required:"enter first name",
                minlength:"enter atleast 4 character"
            }
        }
        }      
    });  
});