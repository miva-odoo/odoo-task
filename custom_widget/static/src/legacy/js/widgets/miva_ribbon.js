odoo.define('custom_widget.miva_ribbon', function (require) {
    'use strict';

    var widgetRegistry = require('web.widget_registry');
    var Widget = require('web.Widget');

    var RibbonWidget = Widget.extend({
        template: 'custom_widget.miva_ribbon',
        xmlDependencies: ['/custom_widget/static/src/legacy/xml/miva_ribbon.xml'],

        init: function (parent, data, options) {
            this._super.apply(this, arguments);
            this.text = options.attrs.title || options.attrs.text;
            this.tooltip = options.attrs.tooltip;
            this.className = options.attrs.bg_color ? options.attrs.bg_color : 'bg-secondary';
            if (this.text.length > 15) {
                this.className += ' o_small';
            } else if (this.text.length > 10) {
                this.className += ' o_medium';
            }
        },
    });

    widgetRegistry.add('miva_ribbon', RibbonWidget);
    return RibbonWidget;
});
