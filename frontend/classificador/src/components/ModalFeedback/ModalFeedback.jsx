import React from "react";
import approved from "../../approved.png";
import notApproved from "../../notApproved.png";
import "./styles.scss";

const ModalFeedback = ({ isApproved }) => {
  return (
    <div className="contentModal">
      <div>
        <img src={isApproved ? approved : notApproved} alt="classfier" />
      </div>
      <div>
        <div className="textFeedback">
          Esta frase foi categorizada como{" "}
          {isApproved ? (
            <div className="approved">apropriada</div>
          ) : (
            <div className="notApproved">inapropriada</div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ModalFeedback;
