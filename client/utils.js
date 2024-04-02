/**
 * Convert a timestamp to a string to be presented as departure time.
 * @param {string} timestamp - The timestamp representing the departure time.
 * @returns {string} A string representing the departure time in a locale format.
 * */
export function convertDepartureTime(timestamp) {
  const date = new Date(timestamp);
  return date.toLocaleString();
}

export const BUS_STATUS = {
  on_platform: "On platform",
  arriving: "Arriving",
  leaving: "Leaving",
  left: "Left",
};

/**
 * Convert a status key to its value from BUS_STATUS.
 * @param {string} status - The status key to convert.
 * @returns {string} The corresponding status value from BUS_STATUS.
 * */
export function convertStatus(status) {
  return BUS_STATUS[status];
}

/**
 * Get the CSS class for styling a row based on restriction
 * @param {Object} bus - The bus object
 * @returns {string} The CSS class name for styling the row
 * */
export function getRowClass(bus) {
  if (bus.status == "leaving" || bus.status == "left") {
    return "bus-leaving";
  }
  if (bus.seats_available == 0) {
    return "bus-full";
  }
  if (bus.status == "on_platform" || bus.status == "arriving") {
    return bus.seats_available < 10 ? "low-seats" : "bus-arriving";
  }
}
