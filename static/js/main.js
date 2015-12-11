$(document).on('scroll', function (e) {
	color = 'rgba(22,22,22,' + ($(document).scrollTop() / 500) / 1.5 + ')'
    $('.transparent').css('background-color', color);
});