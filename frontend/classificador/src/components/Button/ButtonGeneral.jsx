import React from "react";
import Loading from "../Loading/Loading";
import "./styles.scss";

const ButtonGeneral = ({ text, onClick, isLoading }) => {
  return (
    <button onClick={onClick} className="buttonStyle">
      {!isLoading ? <Loading /> : <>{text}</>}
    </button>
  );
};

export default ButtonGeneral;
