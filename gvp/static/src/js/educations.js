odoo.define('gvp.education', function (require) {
'use strict';

const ajax = require('web.ajax');
const core = require('web.core');
const Dialog = require('web.Dialog');
const publicWidget = require('web.public.widget');

const QWeb = core.qweb;
const _t  = core._t;
ajax.loadXML('/gvp/static/src/xml/education.xml', QWeb)

publicWidget.registry.GVPEducation = publicWidget.Widget.extend({
    selector: '#education',
    events: {
        'click #edit_gvp_education': '_onClickEdit',
    },

    start: async function() {
        var def = this._super.apply(this, arguments);

        await this.updateEducations();
        
        return def;
    },

    updateEducations: async function() {
        this.educationData = await this._rpc({
            route: '/my/get/educations'
        });
        const $EducationContainer = $(QWeb.render('gvp.my_educations', this.educationData));
        this.$('.educations_container').replaceWith($EducationContainer);
    },

    _onClickEdit: async function (ev) 
    {
        this.dialog = new Dialog(this, {
            $content: $(QWeb.render('gvp.education_form', this.educationData)),
            buttons: [{
                classes: 'btn-primary float-right',
                text: 'Submit',
                close: true,
                click: async () => {
                    const educations = this.dialog.$el.find('select').val();
                    await this._rpc({
                        route: '/my/update/educations',
                        params: {
                            educations: educations
                        }
                    });
                    this.updateEducations();
                    location.reload();
                }
            }, {
                classes: 'btn-secondary float-right',
                close: true,
                text: _t('Close'),
            }],
            size: "medium",
            title: _t("Edit Education"),
        }).open();
        this.dialog.opened(() => {
            this.dialog.$el.find('select').select2();
        });

    },
});
});
