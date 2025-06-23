\# 🌍 Global Food Price Index Dashboard (2020--2024)

This project is an interactive dashboard built using Streamlit to
analyze and visualize the trends in global food prices using FAO data.
It focuses on various food categories such as Cereals, Sugar, Oils,
Dairy, and Meat over the last two decades.

\-\--

\## 📊 Dashboard Features

\- Interactive line charts for each food category - Filter by date
range - Summary statistics: average, max, min, and volatility -
Multi-category comparison - Key event overlays: 2008 crash, COVID-19,
Ukraine war, etc. - Forecasting using ARIMA model

\-\--

\## 🔍 Key Insights from Analysis

\- \*\*Cereals and Oils are the most influential categories\*\* in the
overall Food Price Index (highest correlation). - \*\*Global events\*\*
(like COVID-19 and the 2022 Ukraine war) have \*\*immediate and dramatic
impacts\*\* on food prices. - \*\*Volatility has increased\*\* over
recent decades, especially post-2010. - The \*\*2022 Ukraine war caused
the most extreme price spikes\*\* in the entire dataset. - The data
clearly shows a \*\*strong inflationary trend post-2020\*\*. - This
analysis demonstrates how \*\*interconnected global food systems are
with geopolitical and economic events\*\*. - \*\*Policy
Recommendation\*\*: Governments and international agencies should
monitor food indices closely as \*\*food price stability is vital for
both economic and social stability\*\*.

\-\--

\## 📂 Dataset

\- \*\*Source\*\*: Food and Agriculture Organization (FAO) -
\*\*File\*\*: \`food_price_indices_data_jun25_modified.csv\` -
\*\*Columns\*\*: \`Date\`, \`Food Price Index\`, \`Cereals\`, \`Sugar\`,
\`Oils\`, \`Meat\`, \`Dairy\`

\-\--

\## 🚀 How to Run Locally

\### 1. Clone the repository

\`\`\`bash git clone
https://github.com/YOUR_USERNAME/food-price-dashboard.git cd
food-price-dashboard
#2. Install dependencies
pip install -r requirements.txt
#3. Launch the dashboard
streamlit run app.py
