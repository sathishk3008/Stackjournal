const API_URL = "http://127.0.0.1:5000/contacts";

const contactForm = document.getElementById("contactForm");
const contactList = document.getElementById("contactList");
const submitBtn = document.getElementById("submitBtn");

let editMode = false;
let currentEditId = null;

async function loadContacts() {

    const response = await fetch(API_URL);
    const contacts = await response.json();

    contactList.innerHTML = "";

    contacts.forEach(contact => {

        contactList.innerHTML += `
        <tr>
            <td>${contact.id}</td>
            <td>${contact.name}</td>
            <td>${contact.email}</td>
            <td>${contact["phone no"]}</td>
            <td>
                <button onclick="editContact(${contact.id})">
                    Update
                </button>

                <button onclick="deleteContact(${contact.id})">
                    Delete
                </button>
            </td>
        </tr>
        `;
    });
}

contactForm.addEventListener("submit", async function(event){

    event.preventDefault();

    const contact = {
        id: Number(document.getElementById("id").value),
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        "phone no": document.getElementById("phone").value
    };

    if(editMode){

        await fetch(`${API_URL}/${currentEditId}`,{
            method:"PUT",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(contact)
        });

        editMode = false;
        currentEditId = null;
        submitBtn.textContent = "Add Contact";

    }else{

        await fetch(API_URL,{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(contact)
        });
    }

    contactForm.reset();
    loadContacts();
});

async function deleteContact(id){

    await fetch(`${API_URL}/${id}`,{
        method:"DELETE"
    });

    loadContacts();
}

async function editContact(id){

    const response = await fetch(API_URL);
    const contacts = await response.json();

    const contact = contacts.find(c => c.id === id);

    document.getElementById("id").value = contact.id;
    document.getElementById("name").value = contact.name;
    document.getElementById("email").value = contact.email;
    document.getElementById("phone").value = contact["phone no"];

    editMode = true;
    currentEditId = id;

    submitBtn.textContent = "Update Contact";
}

loadContacts();