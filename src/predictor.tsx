import React, { useState, FormEvent } from "react";
import axios from "axios";
import "./predictor.css"; // Make sure to import your CSS

interface InputData {
  screen_time_and_sleep_quality: number | null;
  education_level: number | null;
  average_daily_screen_time: number | null;
  sleep_issues_from_screen_time: number | null;
}

const Predictor: React.FC = () => {
  const [inputData, setInputData] = useState<InputData>({
    screen_time_and_sleep_quality: null,
    education_level: null,
    average_daily_screen_time: null,
    sleep_issues_from_screen_time: null,
  });

  const [prediction, setPrediction] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();

    // Validate that all fields are selected
    if (
      inputData.screen_time_and_sleep_quality === null ||
      inputData.education_level === null ||
      inputData.average_daily_screen_time === null ||
      inputData.sleep_issues_from_screen_time === null
    ) {
      setError("Please make sure all fields are selected.");
      return;
    }

    try {
      const response = await axios.post("http://localhost:8000/get_prediction", inputData);
      const modelResponse = response.data[0]?.model_response[0]; // Adjust to extract the response
      setPrediction(modelResponse);
      setError(null); // Clear any previous errors
    } catch (error) {
      console.error("Error making prediction: ", error);
      setError("There was an error processing your request. Please try again later.");
    }
  };

  return (
    <div className="predictor-container">
      {/* Purpose Statement */}
      <div className="purpose-statement">
        <h1>Screen Time Impact Predictor</h1>
        <p>
          This tool is designed to help you understand the potential impact of your screen time habits on your overall quality of life.
          By providing insights into how factors like screen time and sleep quality interact, you can make informed decisions to improve your well-being.
        </p>
      </div>

      {/* Form */}
      <form onSubmit={handleSubmit} className="input-form">
        {/* Screen Time & Sleep Quality Dropdown */}
        <div className="form-group">
          <label htmlFor="screen_time_and_sleep_quality">Impact of Screen Time in Sleep Quality:</label>
          <select
            id="screen_time_and_sleep_quality"
            value={inputData.screen_time_and_sleep_quality ?? ""}
            onChange={(e) => setInputData({ ...inputData, screen_time_and_sleep_quality: parseInt(e.target.value) })}
          >
            <option value="">Select</option>
            <option value={0}>Strongly Agree</option>
            <option value={1}>Agree</option>
            <option value={2}>Neutral</option>
          </select>
        </div>

        {/* Education Level Dropdown */}
        <div className="form-group">
          <label htmlFor="education_level">Education Level:</label>
          <select
            id="education_level"
            value={inputData.education_level ?? ""}
            onChange={(e) => setInputData({ ...inputData, education_level: parseInt(e.target.value) })}
          >
            <option value="">Select</option>
            <option value={0}>Bachelor's degree</option>
            <option value={1}>Master's degree</option>
            <option value={2}>Primary education</option>
            <option value={3}>Higher secondary education</option>
          </select>
        </div>

        {/* Average Daily Screen Time Dropdown */}
        <div className="form-group">
          <label htmlFor="average_daily_screen_time">Average Daily Screen Time (hour):</label>
          <select
            id="average_daily_screen_time"
            value={inputData.average_daily_screen_time ?? ""}
            onChange={(e) => setInputData({ ...inputData, average_daily_screen_time: parseInt(e.target.value) })}
          >
            <option value="">Select</option>
            <option value={0}>Less than 1</option>
            <option value={1}>0</option>
            <option value={2}>1 approximately</option>
            <option value={3}>2 approximately</option>
            <option value={4}>More than 6</option>
          </select>
        </div>

        {/* Sleep Issues from Screen Time Dropdown */}
        <div className="form-group">
          <label htmlFor="sleep_issues_from_screen_time">Sleep Issues from Screen Time:</label>
          <select
            id="sleep_issues_from_screen_time"
            value={inputData.sleep_issues_from_screen_time ?? ""}
            onChange={(e) => setInputData({ ...inputData, sleep_issues_from_screen_time: parseInt(e.target.value) })}
          >
            <option value="">Select</option>
            <option value={0}>Often</option>
            <option value={1}>Rarely</option>
            <option value={2}>Sometimes</option>
            <option value={3}>Always</option>
            <option value={4}>Never</option>
          </select>
        </div>

        {/* Error Message */}
        {error && <p className="error-message">{error}</p>}

        <button type="submit" className="submit-button">Get Prediction</button>
      </form>

      {/* Prediction Result */}
      {prediction !== null && (
        <div className="prediction-result">
          <h2>Prediction Result:</h2>
          <p>
            {prediction === 0
              ? "Strongly Negative"
              : prediction === 1
              ? "Negative"
              : prediction === 2
              ? "Neutral"
              : prediction === 3
              ? "Positive"
              : "Strongly Positive"}
          </p>

          {/* Suggestion Section */}
          <div className="suggestions">
            <h3>Suggestions for Improving Quality of Life:</h3>
            <ul>
              <li>Consider reducing your screen time, especially before bed, to improve sleep quality.</li>
              <li>Incorporate more physical activities into your daily routine to balance screen usage.</li>
              <li>Engage in social activities with family and friends to enhance your overall well-being.</li>
              <li>Explore relaxation techniques, such as meditation, to manage stress related to screen use.</li>
            </ul>
          </div>
        </div>
      )}
    </div>
  );
};

export default Predictor;
