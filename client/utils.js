export function convertDepartureTime(timestamp) {
    const date = new Date(timestamp);
    return date.toLocaleString()
}

export const BUS_STATUS = {
    'on_platform': 'On platform',
    'arriving': 'Arriving',
    'leaving': 'Leaving',
    'left': 'Left'
};

export function convertStatus(status) {
    return BUS_STATUS[status]
}

export function getRowClass(bus) {
    if(bus.status == "leaving" || bus.status == "left") {
        return "bus-leaving"
    }
    if(bus.seats_available == 0) {
        return "bus-full"
    }
    if(bus.status == "on_platform" || bus.status == "arriving") {
        return bus.seats_available < 10 ? "low-seats" : "bus-arriving"
    }
}