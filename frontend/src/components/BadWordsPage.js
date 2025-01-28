const BadWordsPage = () => {
    return (
        <div style={{ textAlign: "center" }}>
            <h1>Bad Words Chatbot</h1>
            <iframe
                src={`http://127.0.0.1:7860`} // Gradio URL
                style={{
                    width: "100%",
                    height: "800px",
                    border: "none",
                    overflow: "hidden",
                }}
                title="Gradio Chatbot"
            ></iframe>
        </div>
    );
};

export default BadWordsPage;