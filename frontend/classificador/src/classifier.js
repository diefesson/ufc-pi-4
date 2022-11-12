export const getTextRating = (data) => {
  if (!data) {
    return null;
  }

  console.log(data);
  return data.result.classification !== "OFFENSIVE";
};
