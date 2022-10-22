import React, { useState } from "react";
import ButtonGeneral from "../components/Button/ButtonGeneral";
import ModalFeedback from "../components/ModalFeedback/ModalFeedback";
import "../styles.scss";

const Classifier = ({ onClick }) => {
  const [text, setText] = useState("");
  const [verified, setVerified] = useState();

  const handleVerifyText = () => {
    fetch("api", {
      comment: text,
    })
      .then((data) => setVerified(data))
      .catch((err) => console.log(err));
  };

  console.log(verified);

  return (
    <div className="classifier">
      <div className="title">Classificador de frases</div>
      <span onClick={() => onClick(false)}>
        Entenda melhor como funciona {`->`}
      </span>
      <hr />
      <div className="inputs">
        <div className="inputs__text">
          <textarea
            cols="30"
            rows="10"
            onChange={(e) => setText(e.target.value)}
            placeholder="Digite sua frase aqui..."
          />
        </div>
        <div className="inputs__button">
          <ButtonGeneral onClick={handleVerifyText} text="Analisar" isLoading />
        </div>
      </div>
      <div className="positionFeedback">
        <ModalFeedback isApproved />
      </div>
    </div>
  );
};

export default Classifier;
