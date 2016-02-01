var ERROR_FLAG = 0;
function error_display(element_id,message){
	$(element_id).parent().addClass("has-error has-feedback");
	$(element_id).next().html('<p class ="text-danger small"><small>'+message+'</small></p>');
}
function error_radio_display(message){
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

	$("#personal_submit").on("click",function(){
		var first_name = $.trim($("#first_name").val());
   		var last_name = $.trim($("#last_name").val());
   		var date_of_birth = $.trim($("#date_of_birth").val());
   		var letters = /^[A-Za-z]+$/g;
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
			error_radio_display("Please select gender");	
		}
		if (date_of_birth == "" || date_of_birth == "None" || !date_of_birth.match(date)){
			error_display('#date_of_birth',"Enter valid date");
			ERROR_FLAG = 1;
		}
		if (ERROR_FLAG){
			return false;
		}
		else{
			return true;
		}

	});
});
