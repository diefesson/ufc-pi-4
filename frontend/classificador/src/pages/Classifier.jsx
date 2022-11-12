import React, { useState, useEffect } from "react";
import { getTextRating } from "../classifier";
import ButtonGeneral from "../components/Button/ButtonGeneral";
import ModalFeedback from "../components/ModalFeedback/ModalFeedback";
import "../styles.scss";

const Classifier = ({ onClick }) => {
  const [text, setText] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [verified, setVerified] = useState();
  const [rating, setRating] = useState();

  const handleVerifyText = async () => {
    setIsLoading(true);
    setVerified(
      await fetch(process.env.REACT_APP_URL_API, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ body: text }),
      }).then((response) => {
        setIsLoading(false);
        return response.json();
      })
    );
  };

  console.log(process.env.REACT_APP_URL_API);

  useEffect(() => {
    if (isLoading === false) {
      setRating(getTextRating(verified));
    }
  }, [isLoading, verified]);

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
          <ButtonGeneral
            onClick={handleVerifyText}
            text="Analisar"
            isLoading={isLoading}
          />
        </div>
      </div>
      <div className="positionFeedback">
        {rating !== null && <ModalFeedback isApproved={rating} />}
      </div>
    </div>
  );
};

export default Classifier;
