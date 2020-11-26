
function onNew(event) {
  onSaveNewSprintname(event)
    .then((data) => {
      $('#new-sprintname-modal').modal('toggle');
      location.href = '/';
    })
    .catch((error) => {
      console.log(error.message);
    });
}

function onDelete(event) {
  onDeleteSprintname(event).then((data) => {
    location.href = '/';
  });
}

function onLoad() {
  createSelectorEvent('.save-new-sprintname', 'click', onNew);
  createSelectorEvent('.icon-trash', 'click', onDelete);
}

window.addEventListener('load', onLoad, {once: true});
