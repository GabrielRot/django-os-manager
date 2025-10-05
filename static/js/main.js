function setActionFormDeleteModal(button, formId = 'deleteForm', url = '') {
  document.querySelector(`#${formId}`).action = url == '' ? button.getAttribute('data-url') : url;
}