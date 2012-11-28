var Ordering = {

    /**
     * Get list of elements that can be reordered
     *
     * At this point, only already existent records can be reordered (ie. where pk != '')
     *
     * @return Array
     * @todo Check if given record changed, and if so, make it reorderable
     * @todo Primary key might not be 'id' - better selector needed
     *
     */
    getOrderables: function () {
        var allInlineRows = Ordering.jQuery('.inline-related'),
            i = 0,
            ids = [];
        
        for (i = 0; i < allInlineRows.length; i = i + 1) {
            if (Ordering.jQuery('.ordering input, .field-ordering input', allInlineRows[i]).val()) {
                ids.push('#' + allInlineRows[i].id);
            }
        }
        
        // this redundant way is required, so that proper order is maintained, 
        // otherwise orderables were returned in more or less random order
        return Ordering.jQuery(ids.join(', ')); 
    },
    
    /**
     * Inits the jQuery UI D&D
     *
     */
    init: function (jQuery) {
        Ordering.jQuery = jQuery;
        Ordering.jQuery("div.inline-group").sortable({
            axis: 'y',
            placeholder: 'ui-state-highlight',
            forcePlaceholderSize: 'true',
            items: Ordering.getOrderables(),
            update: Ordering.update
        });
        //jQuery("div.inline-group").disableSelection();
        
        Ordering.jQuery('div.ordering').hide();
        Ordering.jQuery('td.ordering input').hide();
        
        Ordering.jQuery('.add-row a').click(Ordering.update);
        
        Ordering.getOrderables().css('cursor', 'move');

        Ordering.update();
    },
    
    jQuery: null,
    
    /**
     * Updates the position field
     *
     */
    update: function () {
        Ordering.getOrderables().each(function (i) {
            Ordering.jQuery('input[id$=ordering]', this).val(i + 1);
            Ordering.jQuery(this).find('h3 > span.position').remove();
            Ordering.jQuery(this).find('h3').append('<span class="position">#' + (i + 1).toFixed() + '</span>');
        });
    }
    
};

django.jQuery(function () {
    Ordering.init(django.jQuery);
});