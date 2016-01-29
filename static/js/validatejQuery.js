
$(document).ready(function(){
   $("#submit").on("click",function(){

   		var first_name = $.trim($("#first_name").val());
   		var last_name = $.trim($("#last_name").val());
		// var gender = $("#gender")
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
			error_message += "Enter first name (alphabets only)\n";
		}
		if (last_name == "" || last_name == "None" || !last_name.match(letters)){  //checking for alphabets too
			error_message += "Enter last name (alphabets only)\n";
		}
		if(!$('input[name=gender]:checked').val()) {
			error_message += "Please select gender\n";
		}
		if (date_of_birth == "" || date_of_birth == "None" || !date_of_birth.match(date)){
			error_message += "Enter valid date of birth (yyyy-mm-dd)\n";
		}
			//checking for digits and length of 10, in the contact number field
		if (contact_number == "" || contact_number == "None" || !contact_number.match(/^[0-9]{10}$/g)){
			error_message += "Enter contact number (10 digits only)\n";
		}
		if (email == "" || email == "None" || !email.match(check_email)){
			error_message += "Enter valid email address (letters,numbers and periods)\n";
		}
		if (username == "" || username == "None" || !username.match(letters)){  //checking for alphabets too
			error_message += "Enter username (alphabets only)\n";
		}
		if (password == "" || password == "None"){
			error_message += "Enter password\n";
		}
		if (confirm_password == "" || confirm_password == "None"){
			error_message += "Enter confirm password\n";
		}
		if (password != confirm_password){
			error_message += "Password did not match\n";
		}
		if(!$('input[name=checkbox_accept]:checked').val()) {
			error_message += "Please select accept before proceeding\n";
		}
		if (error_message!=""){
			alert (error_message);
			return false;
		}

   });  // end of submit onclick

});
