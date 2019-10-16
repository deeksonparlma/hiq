$(document).ready(function(){
  document.getElementById("showForm").onclick =function(){showForm()};

  $(".ham").click(function() {
   $(".options").slideToggle();
   $(".nav").css("opacity", "1");
  });

  $(".close").click(function(){
    $(".ff").slideUp();
    $(".form").slideUp();
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
