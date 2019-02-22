//клик по вкладкам
function tabClick(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
  }
  
  function ulDblClick(div){
    let label = $(div).find('label');
    $('<input/>', {
        value: label.text()
    })
    .select()
    .on('keyup', function (e) {
      if (e.keyCode == 13) {
        this.blur();
      }
    })
    .on('blur', function (e) {
      inputDone(this, label);
    })
    .insertBefore(label)
    .select();
    label.hide();
  }
  
  function inputDone(input, label){
    label.empty();
    label.append(input.value);
    label.show();
    input.remove();
  }
  
  function addGroupOfParams(elem,txt){
    if (typeof(elem.groupCount) === 'undefined'){
      elem.groupCount = 0;
    }
    elem.groupCount++;
    let li = $('<li/>')
    .appendTo($('#groupsList'));
    let ul = $('<ul/>', {
      class: 'group-of-params'
    });
    let labelDiv = $('<div/>', {
      ondblclick: 'ulDblClick(this);'
    })
    .on('click', function(){
      $('#groupsList div').removeClass('selected');
      this.classList.add('selected');
    });
    let label = $('<label/>')
    .append(txt + elem.groupCount)
    .appendTo(labelDiv);
    labelDiv.appendTo(ul);
    ul.appendTo(li);
  }
  
  
  // if (typeof(label.input) !== 'undefined'){
  //   $(label.input).remove();
  // }
  // label.input = $('<input/>', {
  //   type: 'hidden',
  //   value:
  // }).appendTo(label.parent());
  
  
  function deleteGroupOfParams(){
    let lis = $('#groupsList div.selected').siblings();
    for (let i = 0; i < lis.length; i++){
      $('#'+lis[i].id.substr(3)).toggleClass('d-none');
    }
    $('#groupsList div.selected').parent().parent().remove();
  }
  
  function addParamToGroup(td, value){
    let ul = $('#groupsList div.selected').parent();
    if (ul.length == 0)
      return;
    $(td).toggleClass('d-none');
    let li_param = $('<li/>', {
      class: 'param-in-group',
      id: 'li_' + td.id
    })
    .append(td.innerText)
    .appendTo(ul);
    let ul_value = $('<ul/>')
    .appendTo(li_param);
    let li_value = $('<li/>')
    .appendTo(ul_value);
    $('<input/>', {
      type: 'number',
      name: td.id + '[]',
      class: 'param-list-new',
      placeholder: value
    })
    .appendTo(li_value)
    .on('input', function() {
      let $this = $(this);
      let $clone = $this.parent().clone();
      let inp = $clone.find('input');
      inp.on("blur", function() {
        let value = $(this).val();
        if (value === "" && !$(this).hasClass('param-list-new')) {
          $(this).parent().hide();
        }
      });
      let name = $clone.attr('name');
      inp.val('');
      $this.removeClass('param-list-new');
      $clone.appendTo($this.parent().parent());
      inp[0].placeholder = '';
      $this.off('input', arguments.callee);
      inp.on('input', arguments.callee);
    });
  }
  /*
    $('.param-list-new').on('input', function() {
      let $this = $(this);
      let $clone = $this.clone();
      let name = $clone.attr('name');
      let n = parseInt(name.split('_')[1]) + 1;
      name = 'param_' + n;
      $clone.val('');
      $clone.attr('name', name);
      $clone.appendTo($this.parent());
      $this.removeClass('param-list-new');
      $this.off('input', arguments.callee);
      $clone.on('input', arguments.callee);
    $("form input[name^='param_']:not(.param-list-new)")
      .on("blur", function() {
        var value = $(this).val();
        if (value === "") {
          $(this).hide();
        }
      })
  })*/
  