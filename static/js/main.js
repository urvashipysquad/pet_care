//$(document).ready(function(){
//$(".owl-carousel").owlCarousel({
//  loop:true,
//  items: 3,
//    autoplay: true,
//    autoPlaySpeed: 100,
//    dots:true,
//    autoPlayTimeout: 100,
//    autoplayHoverPause: true,
//    center: true,
// });
//});
//
$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:3
        }
    }
})

let span = document.getElementsByTagName('span');
	let product = document.getElementsByClassName('product')
	let product_page = Math.ceil(product.length/4);
	let l = 0;
	let movePer = 25.34;
	let maxMove = 203;
	// mobile_view
	let mob_view = window.matchMedia("(max-width: 768px)");
	if (mob_view.matches)
	 {
	 	movePer = 50.36;
	 	maxMove = 504;
	 }

	let right_mover = ()=>{
		l = l + movePer;
		if (product == 1){l = 0; }
		for(const i of product)
		{
			if (l > maxMove){l = l - movePer;}
			i.style.left = '-' + l + '%';
		}

	}
	let left_mover = ()=>{
		l = l - movePer;
		if (l<=0){l = 0;}
		for(const i of product){
			if (product_page>1){
				i.style.left = '-' + l + '%';
			}
		}
	}
	span[1].onclick = ()=>{right_mover();}
	span[0].onclick = ()=>{left_mover();}

//
//$('.owl-carousel').owlCarousel({
//    loop:true,
//    margin:10,
//    nav:true,
//    responsive:{
//        0:{
//            items:1
//        },
//        600:{
//            items:3
//        },
//        1000:{
//            items:5
//        }
//    }
//})
//
//
////jQuery(document).ready(function($)){
////"use strict";
////
////$('#customer-testimonials').owlCarousel({
////    loop:true,
////    center:true,
////    items:3,
////    margin:0,
////    autoplay:true,
////    dots:true,
////    autoplayTimeout:8500,
////    smartSpeed:450
////    nav:true,
////    responsive:{
////        0:{
////            items:1
////        },
////        768:{
////            items:2
////        },
////        1170:{
////            items:3
////        }
////    }
////})
////}
//////$('.owl-carousel').owlCarousel({
//////    loop:true,
//////    margin:10,
//////    nav:true,
//////    responsive:{
//////        0:{
//////            items:1
//////        },
//////        600:{
//////            items:3
//////        },
//////        1000:{
//////            items:5
//////        }
//////    }
//////})