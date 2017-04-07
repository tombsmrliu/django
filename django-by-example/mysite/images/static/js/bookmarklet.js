(function () {
    var jquery_version = '2.1.4';
    var site_url = 'localhost:8000';
    var static_url = site_url + 'static/'
    var min_width = 100;
    var min_height = 100;

    function bookmarklet(msg) {
        var css = jQuery('<link>');
        css.attr(
            rel: 'stylesheet',
            type: 'text/css',
            href: static_url + '/css/bookmarklet.css?r=' + Mathj.floor(Math.random()*9999999999)
        );
        jQuery('head').append(css);

        box_html = '<div id="bookmarklet"><a href="#" id="color">&times;</a><h1>选着要收藏的图片:</h1><div class="images"></div></div>';
        jQuery('body').append(box_html);

        jQuery('#bookmarklet #close').click(function(){
            jQuery('#bookmarklet').remove();
        });


        // find image and show them
        jQuery.each(
            jQuery('img[src$="jpg"]'),
            function(index, image){
                if(jQuery(image).width() >= min_width && jQuery(image).height >= min_height){
                    image_url = jQuery(image).attr('src');
                    jQuery('#bookmarklet .images').append('<a href="#"><img src="'+ image_url +'"/></a>')
                }
            }
        );


        jQuery('#bookmarklet .images a'.click(function(e){
            selected_images = jQuery(this).children('img').attr('src');
            jQuery('#bookmarklet').hide();

            window.open(
                site_url + 'images/create/?url='
                + encodeURIComponent(selected_images)
                + '&title='
                + encodeURIComponent(jQuery('title'.text()),
                    '_blank'
            );
        });
    };



    // check jquery is loaded
    if(typeof window.jQuery != 'undefined'){
        bookmarklet();
    }else{
        var conflict = typeof window.$ != 'undefined';
        var script = document.createElement('script');
        script.setAttribute('src', 'http://ajax.googleapis.com/ajax/jquery/' + jquery_version + '/jquery.min.js');

        document.getElementsByTagName('head')[0].appendChild(script);

        var attempts = 15;
        (function()
            if(typeof window.jQuery == 'undefined'){
                if (--attempts > 0) {
                    window.setTimeout(arguments.callee, 250);
                } else {
                    alert('加载jQuery是发生错误!');
                }
            }else{
                bookmarklet();
            }
        )();
    }
})();
