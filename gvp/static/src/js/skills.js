odoo.define('gvp.skills', function (require) {
'use strict';

const ajax = require('web.ajax');
const core = require('web.core');
const Dialog = require('web.Dialog');
const publicWidget = require('web.public.widget');

const QWeb = core.qweb;
const _t  = core._t;
ajax.loadXML('/gvp/static/src/xml/skills.xml', QWeb)

publicWidget.registry.GVPSkills = publicWidget.Widget.extend({
    selector: '#skills',
    events: {
        'click #edit_gvp_skills': '_onClickEdit',
    },

    start: async function() {
        var def = this._super.apply(this, arguments);

        await this.updateSkills();
        
        return def;
    },

    updateSkills: async function() {
        this.skillsData = await this._rpc({
            route: '/my/get/skills'
        });
        const $SkillContainer = $(QWeb.render('gvp.my_skills', this.skillsData));
        this.$('.skills_container').replaceWith($SkillContainer);
    },

    _onClickEdit: async function (ev) 
    {
        this.dialog = new Dialog(this, {
            $content: $(QWeb.render('gvp.skills_form', this.skillsData)),
            buttons: [{
                classes: 'btn-primary float-right',
                text: 'Submit',
                close: true,
                click: async () => {
                    const skills = this.dialog.$el.find('select').val();
                    await this._rpc({
                        route: '/my/update/skills',
                        params: {
                            skills: skills
                        }
                    });
                    this.updateSkills();
                    // location.reload();
                }
            }, {
                classes: 'btn-secondary float-right',
                close: true,
                text: _t('Close'),
            }],
            size: "medium",
            title: _t("Edit Skills"),
        }).open();
        this.dialog.opened(() => {
            this.dialog.$el.find('select').select2();
        });

    },
});
});
