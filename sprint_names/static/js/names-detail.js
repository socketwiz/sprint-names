
function onDelete(event) {
  onDeleteSprintname(event).then((data) => {
    location.href = '/';
  });
}

function onUse(event) {
  onUseSprintname(event).then((data) => {
    history.go(0);
  });
}

function onLoad() {
  createSelectorEvent('.delete-sprint-name', 'click', onDelete);
  createSelectorEvent('.use-sprint-name', 'click', onUse);
}

window.addEventListener('load', onLoad, {once: true});
