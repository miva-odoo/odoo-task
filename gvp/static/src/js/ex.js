odoo.define('gvp.ex', function (require) {
'use strict';

const ajax = require('web.ajax');
const core = require('web.core');
const Dialog = require('web.Dialog');
const publicWidget = require('web.public.widget');

const QWeb = core.qweb;
const _t  = core._t;
ajax.loadXML('/gvp/static/src/xml/education.xml', QWeb)

publicWidget.registry.GVPExp = publicWidget.Widget.extend({
    selector: '#exp',
    events: {
        'click #edit_gvp_ex': '_onClickEdit',
    },

    start: async function() {
        var def = this._super.apply(this, arguments);

        await this.updateEexperiences();
        
        return def;
    },

    updateEexperiences: async function() {
        this.experiencesData = await this._rpc({
            route: '/my/get/experiences'
        });
        const $ExperiencesContainer = $(QWeb.render('gvp.my_experiences', this.experiencesData));
        this.$('.experiences_container').replaceWith($ExperiencesContainer);
    },

    _onClickEdit: async function (ev) 
    {
        this.dialog = new Dialog(this, {
            $content: $(QWeb.render('gvp.experience_form', this.experiencesData)),
            buttons: [{
                classes: 'btn-primary float-right',
                text: 'Submit',
                close: true,
                click: async () => {
                    const experiences = this.dialog.$el.find('select').val();
                    await this._rpc({
                        route: '/my/update/experiences',
                        params: {
                            experiences: experiences
                        }
                    });
                    this.updateEexperiences();
                    location.reload();
                }
            }, {
                classes: 'btn-secondary float-right',
                close: true,
                text: _t('Close'),
            }],
            size: "medium",
            title: _t("Edit Experiences"),
        }).open();
        this.dialog.opened(() => {
            this.dialog.$el.find('select').select2();
        });

    },
});
});
