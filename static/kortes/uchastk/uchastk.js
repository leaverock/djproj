//клик на левой таблице на странице ctgs_types_train.html
function showMassesSost(contains) {
  var count = contains[0].map(x => x + 2)
  var max_count = count[0] > count[1] ? count[0] : count[1];
  var d = document;
  var table = d.getElementById("cat_types_train_table");
  table = table.lastElementChild;
  table.innerHTML = "";
  var trs = Array();
  for (tr_index in [...Array(max_count).keys()]) {
    trs.push(d.createElement("tr"));
  }
  for (i = 0; i < 2; i++) {
    for (j = 1; j < count[i]; j++) {
      var td = d.createElement("td");
      td.innerText = contains[j][i];
      trs[j].appendChild(td);
      i == 1 ? table.appendChild(trs[j]) : null;
    }
  }
}

function ulDblClick(div) {
  let label = $(div).find('label');
  $(div).find('input')
    .show()
    .on('keyup', function (e) {
      if (e.keyCode == 13) {
        this.blur();
      }
    })
    .on('blur', function (e) {
      inputDone($(this), label);
    })
    .select();
  label.hide();
}

function inputDone(input, label) {
  label.empty();
  label.append(input.val());
  label.show();
  input.hide();
}

function addGroupOfParams(elem) {
  if (typeof (elem.groupCount) === 'undefined') {
    elem.groupCount = 0;
  }
  elem.groupCount++;
  let params = {
    ondblclick: 'ulDblClick(this);',
    class: 'col-3 text-center'
  };
  let li = $('<li/>')
    .appendTo($('#groupsList'));
  let ul = $('<ul/>', {
    class: 'group-of-params'
  }).appendTo(li);
  let rowDiv = $('<div/>', { class: 'row' })
    .on('click', function () {
      $('#groupsList div').removeClass('selected');
      this.classList.add('selected');
    }).appendTo(ul);
  let labelDiv = $('<div/>', params).appendTo(rowDiv);//наименование станции
  let putRazvDiv = $('<div/>', { class: 'col-3 text-center' }).appendTo(rowDiv);//наличие путевого развития
  let koordPlanDiv = $('<div/>', params).appendTo(rowDiv);//координата на плане
  let koordFactDiv = $('<div/>', params).appendTo(rowDiv);//фактическая координата
  //наименование станции
$('<input/>', {
    name: 'stansName[]',
    class: 'w-100'
  }).on('blur', function () {
    try {
      let label = $('#uchNameLabel');
      let uchastki = document.getElementsByName('stansName[]');
      label.empty();
      label.append(uchastki[0].value + ' - ' + uchastki[uchastki.length - 1].value);
      label.parent().find('input').val(label[0].innerText);
    }
    catch{

    }
  })
    .hide()
    .val('Участок ' + elem.groupCount)
    .appendTo(labelDiv).blur();
  $('<label/>')
    .append('Участок ' + elem.groupCount)
    .appendTo(labelDiv);

  //наличие путевого развития
  let putRazvInput = $('<input/>', {
    name: 'putRazv[]',
    class: 'w-100 d-none',
    value: '1',
  }).appendTo(putRazvDiv);
  let putRazvLabel = $('<label/>')
    .append("ДА")
    .appendTo(putRazvDiv);
  putRazvDiv.on('dblclick', {
    label: putRazvLabel,
    input: putRazvInput
  }, function (e) {
    let label = $(e.data['label']);
    let input = e.data['input'];
    label.empty();
    if (input.val() == "1") {
      label.append("НЕТ");
      input.val(0);
    }
    else {
      label.append("ДА");
      input.val(1);
    }
    if (window.getSelection) {
      window.getSelection().removeAllRanges();
    } else { // старый IE
      document.selection.empty();
    }
  });

  //координата на плане
  $('<input/>', {
    name: 'koordPlan[]',
    class: 'w-100 text-center pl-3',
    type: 'number',
    maxlength: "7"
  }).hide()
    .val(0.)
    .appendTo(koordPlanDiv);
  $('<label/>')
    .append(0.)
    .appendTo(koordPlanDiv);

  //фактическая координата
  $('<input/>', {
    name: 'koordFact[]',
    class: 'w-100 text-center pl-3',
    type: 'number',
    maxlength: "7"
  }).hide()
    .val(0.)
    .appendTo(koordFactDiv);
  $('<label/>')
    .append(0.)
    .appendTo(koordFactDiv);
}

function deleteGroupOfParams() {
  let lis = $('#groupsList div.selected').siblings();
  for (let i = 0; i < lis.length; i++) {
    $('#' + lis[i].id.substr(3)).toggleClass('d-none');
  }
  $('#groupsList div.selected').parent().parent().remove();
}

function addParamToGroup(td, value) {
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
    .on('input', function () {
      let $this = $(this);
      let $clone = $this.parent().clone();
      let inp = $clone.find('input');
      inp.on("blur", function () {
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