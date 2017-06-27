/**
 * XBlockStringFieldEditor is a view that allows the user to inline edit an XBlock string field.
 * Clicking on the field value will hide the text and replace it with an input to allow the user
 * to change the value. Once the user leaves the field, a request will be sent to update the
 * XBlock field's value if it has been changed. If the user presses Escape, then any changes will
 * be removed and the input hidden again.
 */
define(['js/views/baseview'],
    function(BaseView) {
        var XBlockAccessEditor = BaseView.extend({
            events: {
            },

            // takes XBlockInfo as a model

            initialize: function() {
                BaseView.prototype.initialize.call(this);
                this.template = this.loadTemplate('xblock-access-editor');
            },

            render: function() {
                this.$el.append(this.template({}));
                return this;
            }
        });

        return XBlockAccessEditor;
    }); // end define();
