function clearThenAppendRows(contains) {
    var count = contains[0].map(x => x + 2)
    var max_count = count[0] > count[1] ? count[0] : count[1];
    var d = document;
    var table = d.getElementById("cat_types_train_table");
    table = table.lastElementChild;
    table.innerHTML = "";
    var trs = Array();
    for (tr_index in [...Array(max_count).keys()]){
        trs.push(d.createElement("tr"));
    }
    for ( i = 0; i < 2; i++){
        for ( j = 1; j < count[i]; j++) {
            var td = d.createElement("td");
            td.innerText = contains[j][i];
            trs[j].appendChild(td);
            i == 1 ? table.appendChild(trs[j]) : null;
        }
    }
}