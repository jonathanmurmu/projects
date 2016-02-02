ERROR_FLAG = 0;
function error_display(element_id,message){
	$(element_id).parent().addClass("has-error has-feedback");
	$(element_id).next().html('<span class="glyphicon glyphicon-remove form-control-feedback"></span><p class ="text-danger small"><small>'+message+'</small></p>');
	$(element_id).next().next().html('');
}
$(document).ready(function(){
	$("input").keypress(function(){
		$(this).parent().removeClass("has-error has-feedback");
		$(this).next().html('');
		$(this).next().next().html('<span class="glyphicon glyphicon-remove form-control-feedback"></span>');
		ERROR_FLAG = 0;		
	});

	$("#login_submit").on("click",function(e){
		e.preventDefault();
		var username = $.trim($("#username").val());
		var password = $.trim($("#password").val());
		var letters = /^[A-Za-z]+$/g;
		if (username == "" || username == "None" || !username.match(letters)){  //checking for alphabets too
			error_display("#username","Enter username (alphabets only)");
			ERROR_FLAG = 1;
		}
		if (password == "" || password == "None"){
			error_display("#password","Enter password ");
			ERROR_FLAG = 1;
		}
		if (ERROR_FLAG){
			return false;
		}
		else{
			$.ajax({
				type: "POST",
				dataType: "json",
				url: "/cgi-bin/projects/task/app/authenticate.py",
				data : $("#login_form").serialize(),
				success: function(data) {					
					if(data['success']){
						if(data['status'] == 'not active'){
							$("#error_message").html('<p class="text-danger">'+data['message']+'</p>')
							$("#username").parent().removeClass("has-error has-feedback");
							$("#username").next().html('');
							$("#username").next().next().html('<span class="glyphicon glyphicon-remove form-control-feedback"></span>');
							$("#password").parent().removeClass("has-error has-feedback");
							$("#password").next().html('');
							$("#password").next().next().html('<span class="glyphicon glyphicon-remove form-control-feedback"></span>');							
							ERROR_FLAG = 1;
							return false;
						}
						else if(data['status'] == 'error'){
							$("#error_message").html('');
							error_display("#username","Wrong username");
							error_display("#password","Wrong password");
							ERROR_FLAG = 1;
							return false;
						}
					}			
				},
				error:function(data) {
					$("#login_form").submit();
				}
			});
		}
	});  // end of login on click
});
