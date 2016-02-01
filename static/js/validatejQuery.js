var ERROR_FLAG = 0;

function error_display(element_id,message){
	$(element_id).parent().addClass("has-error has-feedback");
	$(element_id).next().html('<span class="glyphicon glyphicon-remove form-control-feedback"></span><p class ="text-danger"><small>'+message+'</small></p>');
}
// displaying error for check box
function error_check_display(element_id,message){
	$(element_id).parent().parent().addClass("has-error has-feedback");
	$(element_id).next().html('<p class ="text-danger small"><small>'+message+'</small></p>');

}
function error_radio_display(element_id,message){
	$("#error-text-radio").html('<label><p class ="text-danger small"><small>'+message+'</small></p></label>');
}
$(document).ready(function(){

	// removes the error message when the user starts typing
	$("input").keypress(function(){
		$(this).parent().removeClass("has-error has-feedback");
		$(this).next().html('');
		ERROR_FLAG = 0;
	});
	// removes the error from radio
	$("#male,#female").click(function(){
		$("#error-text-radio").html('');
		ERROR_FLAG = 0;
	});
	// removes the error message from checkbox
	$("#checkbox_accept").click(function(){
		$('#checkbox_accept').parent().parent().removeClass("has-error has-feedback");
		$("#checkbox_accept").next().html('');
		ERROR_FLAG = 0;
	});
	// validate the page
   $("#submit").on("click",function(){
   		var first_name = $.trim($("#first_name").val());
   		var last_name = $.trim($("#last_name").val());
		var date_of_birth = $.trim($("#date_of_birth").val());
		var contact_number = $.trim($("#contact_number").val());
		var email = $.trim($("#email").val());
		var username = $.trim($("#username").val());
		var password = $.trim($("#password").val());
		var confirm_password = $.trim($("#confirm_password").val());
		var checkbox_accept = $("#checkbox_accept");
   		// initializing error message varialbe
		var error_message = "";
		// validating the fields and displaying the appropriate error message
		var letters = /^[A-Za-z]+$/g;
		var check_email = /^([a-zA-Z0-9.])+@([a-zA-Z0-9-])+[.]([a-zA-Z0-9]{2,4})+$/g;  //email allows letters, numbers and periods
		var date = /^\d{4}-\d{1,2}-\d{1,2}$/g;

   		if (first_name == "" || first_name == "None" || !first_name.match(letters)){  //checking for alphabets too
			error_display('#first_name',"Enter first name (alphabets only)");
			ERROR_FLAG = 1;
		}
		if (last_name == "" || last_name == "None" || !last_name.match(letters)){  //checking for alphabets too
			error_display('#last_name',"Enter last name (alphabets only)");
			ERROR_FLAG = 1;
		}
		if(!$('input[name=gender]:checked').val()) {
			error_radio_display("#female","Please select gender");	
		}
		if (date_of_birth == "" || date_of_birth == "None" || !date_of_birth.match(date)){
			error_display('#date_of_birth',"Enter valid date (yyyy-mm-dd)");
			ERROR_FLAG = 1;
		}
			//checking for digits and length of 10, in the contact number field
		if (contact_number == "" || contact_number == "None" || !contact_number.match(/^[0-9]{10}$/g)){
			error_display('#contact_number',"Enter 10 digits number only");
			ERROR_FLAG = 1;
		}
		if (email == "" || email == "None" || !email.match(check_email)){
			error_display("#email","Enter valid email address (letters,numbers and periods only)");
			ERROR_FLAG = 1;
		}
		if (username == "" || username == "None" || !username.match(letters)){  //checking for alphabets too
			error_display("#username","Enter username (alphabets only)");
			ERROR_FLAG = 1;
		}
		if (password == "" || password == "None"){
			error_display("#password","Enter password");
			ERROR_FLAG = 1;
		}
		if (confirm_password == "" || confirm_password == "None"){
			error_display("#confirm_password","Enter confirm password");
			ERROR_FLAG = 1;
		}
		if (password != confirm_password){
			// error_message += "Password did not match\n";
			error_display("#password","Password did not match");
			error_display("#confirm_password","Password did not match");
			ERROR_FLAG = 1;
		}
		if(!$('input[name=checkbox_accept]:checked').val()) {
			error_check_display("#checkbox_accept","Please accept to proceed");
			ERROR_FLAG = 1;
		}
		if (ERROR_FLAG){
			return false;
		}
		else{
			return true;
		}

   });  // end of submit onclick

});
