odoo.define('geminate_ecommerce_theme.counter', function (require) {
"use strict";
const options = require('web_editor.snippets.options');
require('website.form_editor');
options.registry.WebsiteFormEditor.include({
  xmlDependencies: options.registry.WebsiteFormEditor.prototype.xmlDependencies.concat(
        ['/geminate_ecommerce_theme/static/src/xml/website_form_editior.xml']
    ),
});
});

$ (document).ready(function(){
  if($(".counter").length)
  $(".counter").counterUp({
    delay:10,
    time:2000,
});
});

