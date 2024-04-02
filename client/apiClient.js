export class ApiClient {
    constructor(url) {
        this.apiUrl = url;
    }

    async getBusesList() {
        const response = await fetch(this.apiUrl + "/api/bus-list/");
        const data = await response.json();
        return data
    }
}