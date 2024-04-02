export class ApiClient {
    constructor(url) {
        this.apiUrl = url;
    }

    async getBusesList() {
        const response = await fetch(this.apiUrl + "/api/bus-list/");
        const data = await response.json();
        return data
    }

    async postReserveSeat(registrationPlate) {
    try {
        const response = await fetch(`${this.apiUrl}/api/bus/${registrationPlate}/reserve-seat/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
        });

        if (!response.ok) {
            throw new Error('Error reserving seat');
        }

        const data = await response.json();
        return data
    } catch (error) {
        console.error('Error', error.message);
    }


}

async postUnreserveSeat(registrationPlate) {
    try {
        const response = await fetch(`${this.apiUrl}/api/bus/${registrationPlate}/unreserve-seat/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
        });

        if (!response.ok) {
            throw new Error('Error reserving seat');
        }

        const data = await response.json();
        return data
    } catch (error) {
        console.error('Error', error.message);
    }
}
}