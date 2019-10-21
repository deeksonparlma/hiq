$(document).ready(function(){
  document.getElementById("showForm").onclick =function(){showForm()};

  $(".ham").click(function() {
   $(".options").slideToggle();
   $(".nav").css("opacity", "1");
  });
  $(".backFlip").click(function(){
    $(".content").toggle();
    $(".backContent").toggle();
  });
  $(".Front").click(function(){
    $(".content").toggle();
    $(".backContent").toggle();
  });
  $(".close").click(function(){
    $(".ff").slideUp();
    $(".form").slideUp();
    $(".content").toggle();
    $(".backContent").toggle();
  });
  function showForm() {
    $(".ff").show();
    $(".form").slideDown();
  }
  $(window).scroll(function(){
    if ($(document).scrollTop() > 50) {
            $(".nav").css("opacity", "0.6");
          } else {
            $(".nav").css("opacity", "1");
          }
})
});
