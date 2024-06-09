(function($) {
  Drupal.behaviors.categorySelector = {
    attach: function(context) {
	    var $category_item = $('.view-content-category .views-field-name');
		var $category_input = $('#edit-field-featured-categories-und');
		$category_item.click(function() {
			var text = $(this).text().trim();
			$category_input.val(text);
	    });
    }
  }
  Drupal.behaviors.FacetMobile = {
    attach: function(context) {
      width = window.innerWidth;
      if(width < 500){
        $('.block-facetapi ul.facetapi-facetapi-links').hide();
        var $m_head = $('.page-policy-all .region-sidebar-first #filter-wrapper');
        $m_head.click(function() {
          $('.page-policy-all .region-sidebar-first .block-facetapi').slideToggle();
          $('.page-policy-all .region-sidebar-first .block-views').slideToggle();
          });
          if($('.block-facetapi ul.facetapi-facetapi-checkbox-links li .facetapi-active').length > 0) {
            $('.page-policy-all .region-sidebar-first .block-facetapi').show();
            $('.page-policy-all .region-sidebar-first .block-views').show();
          }
      }
    }
  } 
Drupal.behaviors.ODSDocumentLink = {
    attach: function(context, settings) {
    var cType = Drupal.settings.contType;
        if ($('body.page-node-add-unite-document').length > 0 || cType == 'unite_document'){
        //console.log(cType);
        $(".form-radio[value=_none]").parent().parent().hide();
            var symbol_value    = document.getElementById('edit-field-document-symbol-und-0-value');
            var ods_Link_url    = document.getElementById('edit-field-ods-link-und-0-url');
            var check_ODS       = document.getElementById('edit-field-select-file-type-und-ods');
            var doc_language    = document.getElementById('edit-language');
            $("input#edit-field-ods-link-und-0-url").attr("readonly", true);
          }
        else if ($('body.page-node-add-unite-event').length > 0 || $('body.page-node-edit.node-type-unite-event').length > 0){
          var symbol_value    = document.getElementById('edit-field-unite-document-und-form-field-document-symbol-und-0-value');
          var ods_Link_url    = document.getElementById('edit-field-unite-document-und-form-field-ods-link-und-0-url');
          var check_ODS       = document.getElementById('edit-field-unite-document-und-form-field-select-file-type-und-ods');
          var doc_language    = document.getElementById('edit-language');
          $("input#edit-field-unite-document-und-form-field-ods-link-und-0-url").attr("readonly", true);
        }
            if(typeof(check_ODS) != "undefined" && check_ODS != null) {
            check_ODS.addEventListener('change', function() {
                if ($(this).val() == 'ods') {
                    if (doc_language.value == 'und' || doc_language.value == 'en') {
                        ods_Link_url.value = 'https://www.undocs.org/' + symbol_value.value;
                    } else if (doc_language.value == 'ar') {
                        ods_Link_url.value = 'https://www.undocs.org/ar/' + symbol_value.value;
                    } else if (doc_language.value == 'es') {
                        ods_Link_url.value = 'https://www.undocs.org/es/' + symbol_value.value;
                    } else if (doc_language.value == 'fr') {
                        ods_Link_url.value = 'https://www.undocs.org/fr/' + symbol_value.value;
                    } else if (doc_language.value == 'ru') {
                        ods_Link_url.value = 'https://www.undocs.org/ru/' + symbol_value.value;
                    } else if (doc_language.value == 'zh-hans') {
                        ods_Link_url.value = 'https://www.undocs.org/zh/' + symbol_value.value;
                    }
                    if(symbol_value.value == ''){
                        ods_Link_url.value = "https://www.undocs.org/<Enter Document Symbol/Reference Above>";
                    }
                } else {
                    ods_Link_title.value = '';
                    ods_Link_url.value = '';
                }
            }, true);
            doc_language.addEventListener('change', function() {
                if (symbol_value.value != '') {
                    if (doc_language.value == 'und' || doc_language.value == 'en') {
                        ods_Link_url.value = 'https://www.undocs.org/' + symbol_value.value;
                    } else if (doc_language.value == 'ar') {
                        ods_Link_url.value = 'https://www.undocs.org/ar/' + symbol_value.value;
                    } else if (doc_language.value == 'es') {
                        ods_Link_url.value = 'https://www.undocs.org/es/' + symbol_value.value;
                    } else if (doc_language.value == 'fr') {
                        ods_Link_url.value = 'https://www.undocs.org/fr/' + symbol_value.value;
                    } else if (doc_language.value == 'ru') {
                        ods_Link_url.value = 'https://www.undocs.org/ru/' + symbol_value.value;
                    } else if (doc_language.value == 'zh-hans') {
                        ods_Link_url.value = 'https://www.undocs.org/zh/' + symbol_value.value;
                    }
                }
            }, true);
            symbol_value.addEventListener('change', function() {
                if (symbol_value.value != '') {
                    if (doc_language.value == 'und' || doc_language.value == 'en') {
                        ods_Link_url.value = 'https://www.undocs.org/' + symbol_value.value;
                    } else if (doc_language.value == 'ar') {
                        ods_Link_url.value = 'https://www.undocs.org/ar/' + symbol_value.value;
                    } else if (doc_language.value == 'es') {
                        ods_Link_url.value = 'https://www.undocs.org/es/' + symbol_value.value;
                    } else if (doc_language.value == 'fr') {
                        ods_Link_url.value = 'https://www.undocs.org/fr/' + symbol_value.value;
                    } else if (doc_language.value == 'ru') {
                        ods_Link_url.value = 'https://www.undocs.org/ru/' + symbol_value.value;
                    } else if (doc_language.value == 'zh-hans') {
                        ods_Link_url.value = 'https://www.undocs.org/zh/' + symbol_value.value;
                    }
                } else {
                    ods_Link_url.value = "https://www.undocs.org/<Enter Document Symbol/Reference Above>";
                }
            }, true);
          }

    }
};
Drupal.behaviors.UWMemberState = {
  attach: function(context) {
    var mcType = Drupal.settings.contType;
    if ($('body.page-node-add-unite-web-member-state').length > 0 || mcType == 'unite_web_member_state'){
      //console.log(mcType);
      var hide_title    = $('#edit-field-hide-title-und');
      var mem_title    = document.getElementById('edit-title');
      var mem_state    = document.getElementById('edit-field-member-state-und');
      $('.pane-node-form-title input#edit-title').hide();
      $('.pane-node-form-path').hide();
      hide_title.click(function() {
        if ($('#edit-field-hide-title-und').attr('checked')) {
          $('.pane-node-form-title input#edit-title').hide();
          $('.pane-node-form-path').hide();
        } else{
          $('.pane-node-form-title input#edit-title').show();
          $('.pane-node-form-path').show();
        }
      });
      mem_state.addEventListener('change', function() {
        mem_title.value = $("#edit-field-member-state-und option:selected").text();
      });
    }
  }
}

Drupal.behaviors.PubEndDate = {
  attach: function(context, settings) {
    var cType = Drupal.settings.contType;

    if ($('body.page-node-add-unite-document').length > 0 || cType == 'unite_document') {
      $('.end-date-wrapper').hide();
      $('.form-item-field-publication-date-und-0-show-todate').hide();
      var doc_ser    = $('#edit-field-document-series-und');
      doc_ser.click(function() {
        if ($('input[type=checkbox]').attr('checked')) {
          $('.end-date-wrapper').show();
        } else {
          $('.end-date-wrapper').hide();
          $('#edit-field-publication-date-und-0-value2-datepicker-popup-0').val($('#edit-field-publication-date-und-0-value-datepicker-popup-0').val());
        }
      });
    }
    if ($('body.page-node-add-unite-event').length > 0 || $('body.page-node-edit.node-type-unite-event').length > 0) {
      $('.field-name-field-publication-date .end-date-wrapper').hide();
      var doc_ser    = $('#edit-field-unite-document-und-form-field-document-series-und');
      doc_ser.click(function() {
        if ($('#edit-field-unite-document-und-form-field-document-series-und').attr('checked')) {
          $('.field-name-field-publication-date .end-date-wrapper').show();
        } else {
          $('.field-name-field-publication-date .end-date-wrapper').hide();
        }
      });
    }
  }
}

Drupal.behaviors.UNNewsAccordion = {
    attach: function(context) {
        $('.view-un-news-articles .view-content').hide();
        var $accordion_item = $('.view-un-news-articles .un-news-article-accordion');
        var $news_listing   = $('.view-un-news-articles .view-content');
        $accordion_item.click(function() {
          $news_listing.slideToggle(1000);
        });
    }
}

/* Implementation of confirmation option on revert to default panel page */
Drupal.behaviors.PanelizerIPE = {
  attach: function (context) {
    // Redirect to confirmation page.
    $('#panelizer-ipe-revert', context).once('revert-alert', function() {
      $(this).bind('mouseup', function (e) {
        window.location.href = Drupal.settings.panelizer.revert_default_url;
        this.ipeCancelThis = true;
        return false;
      });
    });
  }
};

  $(document).ready(function() {
    $(".unite-web-document-widget .view-content div").first().addClass("first");
    /*$(".navigation ul.menu li a").each(function(index) {
      var menu = $(this).text()
      if (menu.toLowerCase() == 'how to report') {
          $(this).addClass('redbutton');
      }
    });*/
    if($( ".breadcrumb li" ).length > 0) {
      $( ".breadcrumb li" ).last().addClass('last active');
    }
  $('.pagination  li a').click(UWEventPreNexButton);
  jQuery(document).ajaxComplete(function() {
    jQuery(".icon-only").click(UWEventPreNexButton);
  });
  function UWEventPreNexButton() {
    $('.pagination  li a').removeClass('progress-disabled');
    $('.pagination  li a .icon').removeClass('glyphicon');
    $('.pagination  li a .icon').removeClass('glyphicon-menu-left');
    $('.pagination  li a .icon').removeClass('glyphicon-refresh');
    $('.ajax-progress i').removeClass('glyphicon-spin');
    $('.ajax-progress i').removeClass('glyphicon-refresh');
    $('.ajax-progress i').removeClass('glyphicon-spin');
    $('.ajax-progress-throbber').css({'vertical-align': 'unset', 'width': '14px', 'padding': '1px'});
  }
  $(window).on("resize", function (e) {
	UWcheckScreenSize();
  });
  UWcheckScreenSize();
  function UWcheckScreenSize(){
	var newWindowWidth = $(window).width();
	if (newWindowWidth < 760) {
		if ($('body').find('.uw_tax_hier_show').is(":hidden")){
			/*$('.pane-uw-f-unite-web-policy-taxonomy-hierarchy-menu-block .pane-content').prepend('<div class="uw_tax_hier_block"><span class="uw_tax_hier_show">Category Menu</span></div>');*/
			$('.pane-content #tax-hierarchy-menu').css("display", "none");
			$('.uw_tax_hier_show').css("color", "#FFF");
			$('.uw_tax_hier_block').css({'display' : 'inline-block'});
		}
	}
	else {
		$('.uw_tax_hier_block').css({'display' : 'none'});
		$('.pane-content #tax-hierarchy-menu').css("display", "block");
	}
  }
  setTimeout(
    function()
    {
	  jQuery(".uw_tax_hier_show").click(function(){
	    jQuery('#tax-hierarchy-menu').toggle();
	  });
    }, 2000);
  });
})(jQuery);

if(navigator.userAgent.toLowerCase().indexOf('firefox') <= -1){
  (function($) {
      Drupal.behaviors.drupaldeveloper = {
          attach: function (context) {
              /*$('a.dropdown-toggle').focusout(function() {
                  $(this).parent('li').removeClass('open');
              })*/
              $('.nav > li, li.mega').focusin(function(event) {
                  $(this).addClass('open');
              })
              $('.nav > li, li.mega').focusout(function(event) {
                  $(this).removeClass('open');
              })
              $('.nav > li, li.mega').keydown(function(event) {
                  $(this).addClass('open');
              })

              $(".nav > li a").focus(function(){
                $(this).parent().parent().find('ul').hide();
                $(this).parent().find('ul').show();
              });
          }
      }
  })(jQuery);
}

