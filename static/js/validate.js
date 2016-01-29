function validateForm(){
	// initializing the variables
	var first_name = document.getElementById("first_name").value.trim();
	var last_name = document.getElementById("last_name").value.trim();
	var gender = document.getElementsByName("gender")
	var date_of_birth = document.getElementById("date_of_birth").value.trim();
	var contact_number = document.getElementById("contact_number").value.trim();
	var email = document.getElementById("email").value.trim();
	var username = document.getElementById("username").value.trim();
	var password = document.getElementById("password").value;
	var confirm_password = document.getElementById("confirm_password").value;
	var checkbox_accept = document.getElementById("checkbox_accept");
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
	if (gender[0].checked == false && gender[1].checked == false){
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
	if (checkbox_accept.checked == false){
		error_message += "Please accept before proceeding\n";
	}
	if (error_message!=""){
		alert (error_message);
		return false;
	}

}
// validating the personal information before updating into database
function personal_validate(){
	var first_name = document.getElementById("first_name").value.trim();
	var last_name = document.getElementById("last_name").value.trim();
	var gender = document.getElementsByName("gender")
	var date_of_birth = document.getElementById("date_of_birth").value.trim();
	// initializing error message varialbe
	var error_message = "";
	// validating the fields and displaying the appropriate error message
	var letters = /^[A-Za-z]+$/g;
	var date = /^\d{4}-\d{1,2}-\d{1,2}$/g;
	if (first_name == "" || first_name == "None" || !first_name.match(letters)){  //checking for alphabets too
		error_message += "Enter first name (alphabets only)\n";
	}
	if (last_name == "" || last_name == "None" || !last_name.match(letters)){  //checking for alphabets too
		error_message += "Enter last name (alphabets only)\n";
	}
	if (gender[0].checked == false && gender[1].checked == false){
		error_message += "Please select gender\n";
	}
	if (date_of_birth == "" || date_of_birth == "None" || !date_of_birth.match(date)){
		error_message += "Enter valid date of birth (yyyy-mm-dd)\n";
	}
	if (error_message!==""){
		alert (error_message)
		return false;
	}
}

// validating the address fields before updating into database
function address_validate(){
	var zip_code = document.getElementById("zip").value;
	var contact_number = document.getElementById("contact_number").value;
	var error_message = "";
	if ( zip_code == "" || zip_code == "None" || !zip_code.match(/^[0-9]{6}$/g)){
		error_message += "Enter 6 digit zip code\n"
	}
	if ( contact_number == "" || contact_number == "None" || !contact_number.match(/^[0-9]{10}$/g)){
		error_message += "Enter 10 digit contact number\n"
	}
	if (error_message!==""){
		alert (error_message)
		return false;
	}
}
function pic_validate(){
	var profile_pic = document.getElementById("profile_pic").value;
	var ext = profile_pic.substring(profile_pic.lastIndexOf('.') + 1);
	if(ext == "JPEG" || ext == "jpeg" || ext == "jpg" || ext == "JPG" || ext == "png" || ext == "PNG"){
		
	}
	else{
		alert ("Please upload 'jpeg' or 'png' files only");
		return false;
	}

}
function forgot_email_validate(){
	var email = document.getElementById("email").value;
	// email allows letters, numbers and periods
	var check_email = /^([a-zA-Z0-9.])+@([a-zA-Z0-9-])+[.]([a-zA-Z0-9]{2,4})+$/g;
	if (email == "" || email == "None" || !email.match(check_email)){
		alert("Enter valid email address (letters,numbers and periods)");
		return false;
	}
}