

document.addEventListener('DOMContentLoaded', registerAnchorCallbacks, false);
document.addEventListener('DOMContentLoaded', hideTables, false);

function registerAnchorCallbacks() {
  const anchors = document.getElementsByClassName('host-expand');
  Array.prototype.forEach.call(anchors, function (anchor) {
    anchor.onclick = expandTable;
  });
}

function hideTables() {
  const tables = document.getElementsByClassName('host-packages');
  Array.prototype.forEach.call(tables, function (table) {
    table.style = 'visibility: collapse;';
  });
}

function expandTable(e) {
  const table = this.nextSibling.nextSibling
  if (table) {
    console.log('toggle', table);
    if (table.visible) {
      table.style = 'visibility: collapse;';
    } else {
      table.style = 'visibility: visible;';
    }
    table.visible = !table.visible
  }
}
