import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import ModalFeedback from "./ModalFeedback";

describe("Modal with feedback to user", () => {
  test("deve conter a classe approved", () => {
    render(<ModalFeedback isApproved={true} />);
    const modalStyle = screen.getByText("apropriada");

    expect(modalStyle).toBeInTheDocument();
  });
  test("deve conter a classe notApproved", () => {
    render(<ModalFeedback isApproved={false} />);
    const modalStyle = screen.getByText("inapropriada");

    expect(modalStyle).toBeInTheDocument();
  });
});
