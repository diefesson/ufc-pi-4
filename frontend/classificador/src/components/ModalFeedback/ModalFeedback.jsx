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
        <spam className="textFeedback">
          Esta frase foi categorizada como{" "}
          {isApproved ? (
            <spam className="approved">apropriada</spam>
          ) : (
            <spam className="notApproved">inapropriada</spam>
          )}
        </spam>
      </div>
    </div>
  );
};

export default ModalFeedback;
