import React from "react";
import ButtonGeneral from "../components/Button/ButtonGeneral";
import "../styles.scss";

const Classifier = () => {
  return (
    <div className="classifier">
      <div className="title">Classificador de frases</div>
      <hr />
      <div className="inputs">
        <div className="inputs__text">
          <textarea
            name="oi"
            id="ola"
            cols="30"
            rows="10"
            placeholder="Digite sua frase aqui..."
          />
        </div>
        <div className="inputs__button">
          <ButtonGeneral text="Analisar" />
        </div>
      </div>
    </div>
  );
};

export default Classifier;
