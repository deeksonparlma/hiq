$(document).ready(function(){
  $(".ham").click(function() {
   $(".options").slideToggle();
   $(".nav").css("opacity", "1");
  });
  $(window).scroll(function(){
    if ($(document).scrollTop() > 50) {
            $(".nav").css("opacity", "0.6");
          } else {
            $(".nav").css("opacity", "1");
          }
})
});
