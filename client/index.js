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

        tr.id = bus.registration_plate
        return tr
}

function renderButton(bus) {
    const button = document.createElement('button');
    button.textContent = 'Reserve';
    button.id = 'reserve'

    if(bus.seats_available == 0) {
        button.textContent = 'No seats available';
        button.disabled = true;
    }
    if(["leaving", "left"].includes(bus.status)){
        button.disabled = true;
    }

    button.addEventListener('click', async () => {
        if(button.id == 'reserve') {
            apiClient.postReserveSeat(bus.registration_plate)
        .then(data => {
            button.textContent = 'Unreserve';
            button.id = 'unreserve';
            updateRow(bus, data, button)
        })
        .catch(error => {
            console.error('Error:', error.message);
        });
        }
        if(button.id == 'unreserve') {
            button.textContent = 'Reserve';
            button.id = 'reserve';
            apiClient.postUnreserveSeat(bus.registration_plate)
        .then(data => {
            console.log(data);
            updateRow(bus, data, button)
        })
        .catch(error => {
            console.error('Error:', error.message);
        });
        }
    });

    return button
}

function updateRow(bus, newData, button) {
    const existingRow = document.getElementById(bus.registration_plate);

    existingRow.innerHTML = `
        <td>${newData.end_destination}</td>
        <td>${convertDepartureTime(newData.time_of_departure)}</td>
        <td>${newData.max_seats}</td>
        <td>${newData.seats_available}</td>
        <td>${newData.registration_plate}</td>
        <td>${newData.driver}</td>
        <td>${convertStatus(newData.status)}</td>
    `;

    const trClass = getRowClass(newData);
    if (trClass) {
        existingRow.className = '';
        existingRow.classList.add(trClass);
    }

    const cell = document.createElement('td');
    // const button = renderButton(bus);
    cell.appendChild(button);
    existingRow.appendChild(cell);

}