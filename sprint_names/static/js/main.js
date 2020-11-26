
function createSelectorEvent(selector, event, handler) {
  const querySelectors = document.querySelectorAll(selector);
  const onBeforeUnload = () => {
    if (querySelectors) {
      querySelectors.forEach(
        (querySelector) => querySelector.removeEventListener(event, handler)
      );
    }
  };

  if (querySelectors) {
    querySelectors.forEach(
      (querySelector) => querySelector.addEventListener(event, handler)
    );
  }

  window.onbeforeunload = onBeforeUnload;
}

function onSaveNewSprintname(event) {
  const form = document.querySelector('.new-sprintname-form');
  const elements = form.elements;
  const input = document.querySelector('nav input');
  const csrfToken = input.value;
  const payload = {};

  const valid = form.checkValidity();

  if (valid) {
    for (i = 0; i < elements.length; i++) {
      const element = elements[i];

      if ((element.nodeName === 'INPUT' || element.nodeName === 'TEXTAREA') &&
          (element.type === 'text' || element.type === 'textarea')) {
        payload[element.name] = element.value;
      }
    }

    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify(payload)
    };

    return fetch('/api/name/', options).then((response) => response.json())
      .catch((error) => {
        console.error('Error: ', error);
      });
  }

  form.reportValidity();
  form.classList.add('was-validated');

  return Promise.reject(new Error('form-invalid'));
}

function onDeleteSprintname(event) {
  const el = event.currentTarget;
  const id = el.getAttribute('data-id');
  const input = document.querySelector('nav input');
  const csrfToken = input.value;

  const options = {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken
    }
  };

  return fetch(`/api/name/${id}`, options).then((response) => response.json())
    .catch((error) => {
      console.error('Error: ', error);
    });
}
