import React, { useState, useEffect } from "react";

const BadWordsPage = () => {
    const [badWord, setBadWord] = useState("");
  
    // Fetch the random phrase from the backend
    useEffect(() => {
      fetch("http://127.0.0.1:8000/api/badWords/random-phrase")
        .then((response) => response.json())
        .then((data) => {
          setBadWord(data.phrase);
        })
        .catch((error) => console.error("Error fetching bad word:", error));
    }, []);

    return (
        <div style={{ textAlign: "center" }}>
            <h1>Bad Words Chatbot</h1>
            <h1 style={{ color: "red", fontWeight: "bold" }}> {badWord} </h1>
            <iframe
                src="http://127.0.0.1:7860" // Gradio URL
                style={{
                    width: "100%",
                    height: "500px",
                    border: "none",
                    overflow: "hidden",
                }}
                title="Gradio Chatbot"
            ></iframe>
        </div>
    );
};

export default BadWordsPage;