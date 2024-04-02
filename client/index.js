import { ApiClient } from './apiClient.js';
import {convertDepartureTime, convertStatus, getRowClass} from "./utils.js";

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
        const row = createRow(bus)
        tbody.appendChild(row);
    });
}

function createRow(bus) {
     const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${bus.end_destination}</td>
            <td>${convertDepartureTime(bus.time_of_departure)}</td>
            <td>${bus.max_seats}</td>
            <td>${bus.seats_available}</td>
            <td>${bus.registration_plate}</td>
            <td>${bus.driver}</td>
            <td>${convertStatus(bus.status)}</td>
        `;

        const trClass = getRowClass(bus)
        if(trClass) {
            tr.classList.add(trClass)
        }

        // append reserve button
        const cell = document.createElement('td');
        const button = renderButton(bus);
        cell.appendChild(button);
        tr.appendChild(cell);

        return tr
}

export function renderButton(bus) {
    const button = document.createElement('button');
    button.textContent = 'Reserve';

    if(bus.seats_available == 0) {
        button.textContent = 'No seats available';
        button.disabled = true;
    }
    if(["leaving", "left"].includes(bus.status)){
        button.disabled = true;
    }

    return button
}