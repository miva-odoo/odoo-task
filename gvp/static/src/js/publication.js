odoo.define('gvp.publication', function (require) {
'use strict';

const ajax = require('web.ajax');
const core = require('web.core');
const Dialog = require('web.Dialog');
const publicWidget = require('web.public.widget');

const QWeb = core.qweb;
const _t  = core._t;
ajax.loadXML('/gvp/static/src/xml/publication.xml', QWeb)

publicWidget.registry.GVPPub = publicWidget.Widget.extend({
    selector: '#pub',
    events: {
        'click #edit_gvp_education': '_onClickEdit',
    },

    start: async function() {
        var def = this._super.apply(this, arguments);

        await this.updatePublication();

        return def;
    },

    updatePublication: async function() {
        this.publicationData = await this._rpc({
            route: '/my/get/publication'
        });
        const $PublicationContainer = $(QWeb.render('gvp.my_publication', this.publicationData));
        this.$('.publication_container').replaceWith($PublicationContainer);
    },

    _onClickEdit: async function (ev)
    {
        this.dialog = new Dialog(this, {
            $content: $(QWeb.render('gvp.publication_form', this.publicationData)),
            buttons: [{
                classes: 'btn-primary float-right',
                text: 'Submit',
                close: true,
                click: async () => {
                    const publication = this.dialog.$el.find('select').val();
                    await this._rpc({
                        route: '/my/update/publication',
                        params: {
                            publication: publication
                        }
                    });
                    this.updatePublication();
                    location.reload();
                }
            }, {
                classes: 'btn-secondary float-right',
                close: true,
                text: _t('Close'),
            }],
            size: "medium",
            title: _t("Edit Publication"),
        }).open();
        this.dialog.opened(() => {
            this.dialog.$el.find('select').select2();
        });

    },
});
});
