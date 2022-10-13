import React from "react";
import "../styles.scss";

const Classifier = () => {
  return (
    <div className="classifier">
      <div className="title">Classificador de frases</div>
      <hr />
      <div>
        <textarea
          name="oi"
          id="ola"
          cols="30"
          rows="10"
          placeholder="Digite sua frase aqui..."
        />
      </div>
    </div>
  );
};

export default Classifier;
