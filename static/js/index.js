const form = document.querySelector("form")
const button = document.querySelector('button[type="submit"]')
const dialog = document.querySelector("dialog")
const result = document.querySelector("p.result")
const closeModal = document.querySelector("button.closeModal")

async function handleSubmit(event) {
  event.preventDefault()

  const formData = new FormData(form, button)
  const data = Object.fromEntries(formData)

  const request = new Request("/", {
    method: "post",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
    },
  })

  const response = await fetch(request)
  const responseData = await response.json()

  result.textContent =
    responseData === 0 ? "This person does not have heart disease" : "This person has heart disease"

  dialog.showModal()
}

closeModal.onclick = () => dialog.close()

form.onsubmit = handleSubmit
