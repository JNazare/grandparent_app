$(document).ready(function() {

	$(".choose-photo-button").click(function() {
		$(".choose-photo-container").hide();
		$(".add-message-container").show();
	});

	$(".add-message-button").click(function() {
		$(".add-message-container").hide();
		$(".add-recipient-container").show();
	});
});