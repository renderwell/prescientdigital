
$(document).on('ready', function() {
    $('.menu.vertical > li').hover(function() {
        var el = $(this);
        var dropdown_height = el.find('.submenu').height();
        if (dropdown_height > $(window).height()) {
            el.addClass('max');
        }
    });
});
