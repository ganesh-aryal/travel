/*custom javascript*/

$(document).ready(function(){
	let width = $(window).width();
	$(document).scroll(function(){
		let s = $(document).scrollTop();
		if(s > 50){
			$('nav').removeClass('trans');
			$('nav').css({"z-index":"16", 
				"-webkit-box-shadow": "0 8px 17px 2px rgba(0,0,0,0.14), 0 3px 14px 2px rgba(0,0,0,0.12), 0 5px 5px -3px rgba(0,0,0,0.2)",
    			"box-shadow": "0 8px 17px 2px rgba(0,0,0,0.14), 0 3px 14px 2px rgba(0,0,0,0.12), 0 5px 5px -3px rgba(0,0,0,0.2)" });
			$('#myUl').css("margin-top","0px");
			$('nav a img').css({
				"width":"50px",
				"height":"50px"
			});
			$('nav ul a').css("font-size","18px")
			$('nav a.navbar-brand').css("left","48%");
		}
		else{
			$('nav').addClass('trans');	
			$('nav').css({"z-index":"5",
				"box-shadow":"none"});
			$('#myUl').css("margin-top","52px");
			if(width > 600 )
				$('nav a img').css({
				"width":"150px",
				"height":"150px"
				});	
			else
				$('nav a img').css({
				"width":"80px",
				"height":"80px"
				});						
			$('nav ul a').css("font-size","20px")
			$('nav a.navbar-brand').css("left","45%");
		}
	});

});
