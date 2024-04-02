import { expect } from "chai";
import { getRowClass } from "../utils.js"; // Adjust the path accordingly

describe("test getRowClass function", () => {
  it('should return "bus-leaving" when bus status is "leaving"', () => {
    const bus = { status: "leaving" };
    const result = getRowClass(bus);
    expect(result).to.equal("bus-leaving");
  });

  it('should return "bus-full" when bus is full', () => {
    const bus = { seats_available: 0 };
    const result = getRowClass(bus);
    expect(result).to.equal("bus-full");
  });

  it('should return "low-seats" when seats available are less than 10', () => {
    const bus = { status: "on_platform", seats_available: 5 };
    const result = getRowClass(bus);
    expect(result).to.equal("low-seats");
  });

  it('should return "bus-arriving" when status is "arriving"', () => {
    const bus = { status: "arriving" };
    const result = getRowClass(bus);
    expect(result).to.equal("bus-arriving");
  });
});
