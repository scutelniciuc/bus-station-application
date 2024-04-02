import { renderButton } from "../index.js";
import { JSDOM } from "jsdom";
import { expect } from "chai";

describe("renderButton", () => {
  before(() => {
    const dom = new JSDOM("<!DOCTYPE html><html><body></body></html>");
    global.document = dom.window.document;
  });

  it('create a button with text "Reserve" when seats are available', () => {
    const bus = { seats_available: 8, status: "available" };
    const button = renderButton(bus);
    expect(button.textContent).to.equal("Reserve");
    expect(button.disabled).to.be.false;
  });

  it('create a button with text "No seats available"', () => {
    const bus = { seats_available: 0, status: "available" };
    const button = renderButton(bus);
    expect(button.textContent).to.equal("No seats available");
    expect(button.disabled).to.be.true;
  });

  it('disable the button when bus status is "leaving" or "left"', () => {
    const leavingBus = { seats_available: 2, status: "leaving" };
    const leftBus = { seats_available: 2, status: "left" };
    const leavingButton = renderButton(leavingBus);
    const leftButton = renderButton(leftBus);
    expect(leavingButton.disabled).to.be.true;
    expect(leftButton.disabled).to.be.true;
  });
});
