window.Home = (function Home(window, $) {
    $('.day-container').click(function() {
        $('.day-container').removeClass('js-selected');
        $(this).addClass('js-selected');
    });
})(window, jQuery);