# SOLAR-CHALLENGE-WEEK1

A solar radiation monitoring and analysis system for three solar radiation sites, leveraging data understanding, data analysis and visualization to choose the right solar radiation site  exposure . The project processes environmental and temporal radiation data to provide actionable insights for solar precision farming.

## Development Environment Setup

### Project Structure
``` bash
solar-challenge-week1
├── app
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── data
│   ├── benin_clean.csv
│   ├── sierraleone_clean.csv
│   └── togo_clean.csv
├── datasets
│   └── combined.csv
├── figures
├── LICENSE
├── notebooks
│   ├── bennin_eda.ipynb
│   ├── compare_countries.ipynb
│   ├── __init__ py
│   ├── sierraleone.ipynb
│   └── togo_eda.ipynb
├── README.md
├── requirements.txt
├── scripts
│   └── __init__.py
├── src
│   └── __init__.py
└── tests
    └── __init__.py
```

### Prerequisites
- Python 3.8+
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/abrehamashebir/solar-challenge-week1.git
cd solar-challenge-week1
```
### 2. Set Up Virtual Environment
 For Linux/macOS
```bash
python -m venv venv
source venv/bin/activate
```

 For Windows
 ```bash
python -m venv venv
.\venv\Scripts\activate
```
### 3. Install Python Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
### 1. To run streamlit app
```bash
cd solar-challenge-week1/app
streamlit run main.py
```
