$('.skill-bar-percent').ready(() =>{
	for (var i = $('.skill-bar-percent').length - 1; i >= 0; i--) {
		$($('.skill-bar-percent')[i]).prev().css('width',$($('.skill-bar-percent')[i]).html())
	}
})