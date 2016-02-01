function error_display(element_id,message){
	$(element_id).parent().addClass("has-error has-feedback");
	$(element_id).next().html('<span class="glyphicon glyphicon-remove form-control-feedback"></span><p class ="text-danger small"><small>'+message+')</small></p>');
	$(element_id).next().next().html('');
}
$(document).ready(function(){
	$("input").keypress(function(){
		$(this).parent().removeClass("has-error has-feedback");
		$(this).next().html('');
		$(this).next().next().html('<span class="glyphicon glyphicon-remove form-control-feedback"></span>');
		ERROR_FLAG = 0;
	});


	$("#login_submit").on("click",function(){
		var username = $.trim($("#username").val());
		var password = $.trim($("#password").val());
		if (username == "" || username == "None" || !username.match(letters)){  //checking for alphabets too
			error_display("#username","Enter username (alphabets only)");
			ERROR_FLAG = 1;
		}
		if (password == "" || password == "None" || !password.match(letters)){  //checking for alphabets too
			error_display("#password","Enter password");
			ERROR_FLAG = 1;
		}
		if (ERROR_FLAG){
			return false;
		}
		else{
			return true;
		}
	});  // end of login on click

});
