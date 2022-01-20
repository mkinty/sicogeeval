$( ".open-modal" ).click(function(e){
    e.preventDefault();
    const popup_url = $(this).data("popup-url");
    $(".modal-content").load(popup_url, function () {
       console.log(popup_url)
      $(document).ready(function(){
        $('.modal').modal();
  });
    });
});
