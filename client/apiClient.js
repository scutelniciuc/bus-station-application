/*
 * Class representing an API client to interact with the django backend
 */
export class ApiClient {
  /*
   * Create API client
   * @param {string} baseUrl - Backend's base url
   * */
  constructor(baseUrl) {
    this.apiUrl = baseUrl;
  }

  /*
   * Get the list of all buses
   * @returns {Array<Object>} Array of buses
   * */
  async getBusesList() {
    const response = await fetch(this.apiUrl + "/api/bus-list/");
    const data = await response.json();
    return data;
  }

  /*
   * Reserves a seat in a bus
   * @param {string} registration_plate
   * @returns {<Object>} Updated bus with reserved seat
   * */
  async postReserveSeat(registrationPlate) {
    try {
      const response = await fetch(
        `${this.apiUrl}/api/bus/${registrationPlate}/reserve-seat/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        },
      );

      if (!response.ok) {
        throw new Error("Error reserving seat");
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.error("Error", error.message);
    }
  }

  /*
   * Unreserves a seat in a bus
   * @param {string} registration_plate
   * @returns {<Object>} Updated bus with unreserved seat
   * */
  async postUnreserveSeat(registrationPlate) {
    try {
      const response = await fetch(
        `${this.apiUrl}/api/bus/${registrationPlate}/unreserve-seat/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        },
      );

      if (!response.ok) {
        throw new Error("Error reserving seat");
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.error("Error", error.message);
    }
  }
}
