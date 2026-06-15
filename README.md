# Netflix Movies & TV Shows — Exploratory Data Analysis

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-lightblue?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12-teal)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> An end-to-end exploratory data analysis of Netflix's content library using Python, uncovering trends in content type, geography, genres, ratings, and movie durations.

---

## Project Overview

This project analyses the Netflix Movies and TV Shows dataset sourced from Kaggle (6,234 titles). The goal is to extract meaningful insights about Netflix's content strategy through data cleaning, transformation, and visualisation.

This is an entry-level data analytics portfolio project built using Python in a Jupyter Notebook environment.

---

## Key Insights

- Netflix's library is approximately **69% Movies** and **31% TV Shows**
- The **United States** dominates content production by a large margin, followed by India and the UK
- Content additions **peaked in 2019**, with a noticeable drop after 2020 (likely COVID-related production slowdowns)
- **International Movies** is the single most popular genre on the platform
- **TV-MA** (mature audiences) is the most common content rating — Netflix skews adult
- The average movie duration is approximately **99 minutes**

---

## Charts Generated

| # | Chart | Description |
|---|-------|-------------|
| 1 | Content Type Distribution | Donut chart — Movies vs TV Shows |
| 2 | Top 10 Countries by Content | Horizontal bar chart |
| 3 | Content Added Per Year | Line chart with trend from 2010–2021 |
| 4 | Top 10 Genres | Vertical bar chart |
| 5 | Ratings Distribution | Grouped by Kids / Teen / Adult audience |
| 6 | Movie Duration Distribution | Histogram with mean and median markers |

---

## Project Structure

```
netflix-eda/
│
├── data/
│   └── netflix_titles.csv        # Raw dataset from Kaggle
│
├── charts/
│   ├── chart1_content_type.png
│   ├── chart2_top_countries.png
│   ├── chart3_yearly_trend.png
│   ├── chart4_top_genres.png
│   ├── chart5_ratings.png
│   └── chart6_movie_duration.png
│
├── notebook/
│   ├── Netflix_EDA.ipynb         # Main Jupyter Notebook
│   └── netflix_eda.py            # Python script version
│
└── README.md
```

---

## Technologies Used

- **Python 3.8+**
- **Pandas** — data loading, cleaning, and transformation
- **Matplotlib** — custom chart styling and rendering
- **Seaborn** — statistical visualisation
- **Jupyter Notebook** — interactive analysis environment

---

## How to Run This Project

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/netflix-eda.git
cd netflix-eda
```

### 2. Install dependencies
```bash
pip install pandas matplotlib seaborn jupyter notebook
```

### 3. Download the dataset
- Go to [Kaggle — Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- Download `netflix_titles.csv`
- Place it inside the `data/` folder

### 4. Run the notebook
```bash
jupyter notebook notebook/Netflix_EDA.ipynb
```
Or open it directly in VS Code with the Jupyter extension.

---

## Dataset

- **Source:** [Kaggle — Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Records:** 6,234 titles
- **Columns:** 12 (show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description)
- **Missing values handled:** director (31%), cast (9%), country (7%)

---

## Skills Demonstrated

- Data loading and exploration with Pandas
- Handling missing values and data type conversion
- String manipulation and feature extraction
- Time-series trend analysis
- Custom data visualisation with Matplotlib
- Insight communication through charts and annotations

---

## Author

**Aditya Subhash**
Master of Information Technology | Data Analyst

- Email: adityasubhash35@gmail.com
- LinkedIn: [linkedin.com/in/adityasubhash](https://linkedin.com/in/adityasubhash)
- GitHub: [github.com/YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

## License

This project is open source and available under the [MIT License](LICENSE).
