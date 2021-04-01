
function onDelete(event) {
  onDeleteSprintname(event).then((data) => {
    location.href = '/';
  });
}

function onLoad() {
  createSelectorEvent('.icon-trash', 'click', onDelete);
}

window.addEventListener('load', onLoad, {once: true});
