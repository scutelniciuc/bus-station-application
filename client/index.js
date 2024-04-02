import { ApiClient } from './apiClient.js';

const API_URL="http://127.0.0.1:8000"
const apiClient = new ApiClient(API_URL);

apiClient.getBusesList()
    .then(buses => {
        populateTable(buses)
    })
    .catch(error => {
        console.error(error)
    })

function populateTable(buses) {
    const table = document.querySelector('#bus-schedule');
    const tbody = table.querySelector('tbody');

    tbody.innerHTML = '';

    buses.forEach(bus => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${bus.end_destination}</td>
            <td>${bus.time_of_departure}</td>
            <td>${bus.max_seats}</td>
            <td>${bus.seats_available}</td>
            <td>${bus.registration_plate}</td>
            <td>${bus.driver}</td>
            <td>${bus.status}</td>
            <td><button>Reserve</button></td>
        `;
        tbody.appendChild(tr);
    });
}