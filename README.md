## PhrasesGenerator

![Screenshot 2023-04-17 191148](https://user-images.githubusercontent.com/105819329/232643841-ebe9ba22-be03-4e68-aaad-833d42bd65e3.png)

### Description

This Python project uses the OpenAI API to generate sentences in a selected language and saves the results in a file.

### Requirements

- Python 3.x
- OpenAI API credentials (e.g., `API_KEY`)

### Installation

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/your-repo.git
    ```

2. Install the required dependencies:

    ```
    pip install openai
    ```

### Usage

1. Set your OpenAI API credentials in your environment or configuration file:

    ```python
    import openai

    openai.api_key = "YOUR_API_KEY"
    ```

2. Update the code to specify the language and sentences you want to generate:

    ```python
    language = "en"  # specify the language code, e.g., "en" for English
    sentences = ["Hello, world!", "How are you?", "This is a sample sentence."]
    ```

3. Call the OpenAI API to generate sentences in the selected language:

    ```python
    results = openai.Completion.create(
        prompt="\n".join(sentences),
        language=language,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    ```

4. Save the results to a file:

    ```python
    with open("results.txt", "w") as f:
        f.write(results.choices[0].text)
    ```

5. Run the Python script and check the results saved in the `results.txt` file.

### Contributing

If you'd like to contribute to this project, please follow the standard GitHub workflow:


1. Fork the repository
2. Create a new branch for your changes
3. Make your changes
4. Submit a pull request
