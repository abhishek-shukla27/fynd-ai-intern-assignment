# Fynd AI Intern – Task 1
## Review Rating Prediction using LLMs

### Overview
This task evaluates the performance of different prompt-engineering strategies
for predicting star ratings from Yelp review text using a Large Language Model (LLM).

The objective was to compare multiple prompting approaches based on accuracy and
output consistency (valid JSON format).

---

### Dataset
- Source: Yelp Reviews Dataset (Kaggle)
- Fields used:
  - `text`: review content
  - `stars`: ground truth rating
- A subset of the dataset was sampled for evaluation.

---

### Prompting Strategies
Three prompting approaches were evaluated:

1. **Simple Prompt**  
   Directly asks the model to predict a rating from the review text.

2. **Few-Shot Prompt**  
   Provides example review–rating pairs before prediction to guide the model.

3. **Structured Prompt**  
   Enforces strict output formatting using a predefined JSON schema.

---

### Evaluation Methodology
- Each review was sent to the LLM for prediction.
- The predicted rating was compared to the actual star rating.
- Metrics:
  - **Accuracy** – exact match between predicted and actual stars
  - **JSON Validity Rate** – percentage of responses returned as valid JSON

---

### Implementation
- Python, Pandas
- Google Gemini API for LLM inference
- Custom parsing and error-handling logic to validate JSON outputs

---

### Limitations
During evaluation, the Gemini API free-tier quota was exhausted,
which limited large-scale automated testing.

To demonstrate the approach, the implementation was validated on
a small subset of samples. The pipeline logic, prompting techniques,
and evaluation metrics are designed to scale seamlessly with higher
API quotas.

---

### Conclusion
Few-shot prompting showed improved alignment between the model output
and ground-truth ratings. Structured prompting improved consistency in
output formatting. The experiment demonstrates how prompt design
directly affects LLM reliability and performance.
