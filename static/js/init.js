(function($){
  $(function(){

      $('.button-collapse').sideNav();
      $('.parallax').parallax();

      //initialize single selects
      $('select:not([multiple])').material_select();

  }); // end of document ready
})(jQuery); // end of jQuery name space