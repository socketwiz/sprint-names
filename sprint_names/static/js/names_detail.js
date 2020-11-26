
function onNew(event) {
  onSaveNewSprintname(event).then((data) => {
    $('#new-sprintname-modal').modal('toggle');
    location.href = '/';
  });
}

function onDelete(event) {
  onDeleteSprintname(event).then((data) => {
    location.href = '/';
  });
}

function onLoad() {
  createSelectorEvent('.save-new-sprintname', 'click', onNew);
  createSelectorEvent('.delete-sprint-name', 'click', onDelete);
}

window.addEventListener('load', onLoad, {once: true});
