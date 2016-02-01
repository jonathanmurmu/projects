var ERROR_FLAG = 0;

function error_display(element_id,message){
	$(element_id).parent().addClass("has-error has-feedback");
	$(element_id).next().html('<p class ="text-danger small"><small>'+message+'</small></p>');
}

$(document).ready(function(){
	// removes the error message when the user starts typing
	$("input").keypress(function(){
		$(this).parent().removeClass("has-error has-feedback");
		$(this).next().html('');
		ERROR_FLAG = 0;
	});

	$("#address_submit").on("click",function(){
   		var zip_code = $.trim($("#zip").val());
   		var contact_number = $.trim($("#contact_number").val());
		//checking for digits and length of 6, in the zip code field
		if (zip_code == "" || zip_code == "None" || !zip_code.match(/^[0-9]{6}$/g)){
			error_display('#zip',"Enter 6 digits number only");
			ERROR_FLAG = 1;
		}
		//checking for digits and length of 10, in the contact number field
		if (contact_number == "" || contact_number == "None" || !contact_number.match(/^[0-9]{10}$/g)){
			error_display('#contact_number',"Enter 10 digits number only");
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
