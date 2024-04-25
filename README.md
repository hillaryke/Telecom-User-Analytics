# Telecom User Analytics

## Overview
This project is about analyzing news data to find out the correlation between news and various global media agencies. The project is implemented using Python programming language and the libraries used are pandas, matplotlib and spacy for NER (Name Entity Recognition).

## Data
The data used in this project is a news dataset from Kaggle. The dataset contains news articles from various global media agencies.

## Installation
### Creating a Virtual Environment
#### Using Conda

If Conda is your preferred package manager:

1. Open your terminal or command prompt.


2. Navigate to the project directory.
    ```bash
    cd path/to/telecom-user-analytics
   ```

3. Run the following commands to create a new virtual environment.

    ```bash
    conda create --name env_name python=3.12
    ```
    Replace ```env_name``` with the desired name of the virtual environment and ```3.12``` with your preferred Python version.


4. Activate the virtual environment.

    ```bash
    conda activate env_name
   ```

#### Using Virtualenv

```bash
virtualenv telecom_user_analytics
source telecom_user_analytics/bin/activate
```

### Installing Required Libraries

```bash
pip install -r requirements.txt
```

## Usage

### Data Loading


## Testing
The package provides a test module (inside the tests folder) to run unit tests on the implemented functions.

To run the tests, execute the following command:
```bash
make test
```
The command above uses the Makefile to run the tests. If you don't have Make installed, you can run the tests using the following command:
```bash
python -m unittest discover -s tests
```

## Documentation
The package provides a documentation module (```docs.py```) to generate documentation for the implemented functions.

To generate the documentation, execute the following command:
```bash
make docs
```

## License
This project is licensed under the MIT License.




