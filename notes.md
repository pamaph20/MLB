# Baseball Player Performance Dashboard

## Everything You Need for the Baseball Player Performance Dashboard

---

### 1. Data Sources
- **MLB Stats API (Official)**:
  - URL: [MLB Stats API](https://statsapi.mlb.com/)
  - What You Get: Player stats, game logs, team info, standings, and more.
  - Documentation: [Unofficial MLB Stats API Docs](https://appac.github.io/mlb-data-api-docs/)
  - Best For: Real-time and historical player performance data.

- **Baseball Savant (Statcast Data)**:
  - URL: [Baseball Savant](https://baseballsavant.mlb.com/)
  - What You Get: Advanced metrics like exit velocity, launch angle, and pitch data.
  - API Documentation: Check out [Baseball Savant API](https://github.com/jldbc/pybaseball) (via the PyBaseball library).
  - Best For: Deeper insights into player performance and trends.

- **Fangraphs API (Advanced Metrics)**:
  - URL: [FanGraphs](https://www.fangraphs.com/)
  - What You Get: Advanced metrics like WAR, wOBA, and splits.
  - API Access: No public API, but you can scrape data using Python libraries like BeautifulSoup.
  - Best For: Advanced analytics and comparisons.

---

### 2. Tech Stack
- **Frontend (Angular)**:
  - Library: [Chart.js](https://www.chartjs.org/) - Easy-to-use charting library.
  - Alternative: [D3.js](https://d3js.org/) - More customizable but more complex.
  - UI Framework: [Angular Material](https://material.angular.io/) for a clean, modern look.

- **Backend**:
  - Framework: [Express.js](https://expressjs.com/) for a fast, lightweight backend.
  - Alternative: [Flask](https://flask.palletsprojects.com/) if you’re more comfortable with Python.
  - Data Handling: Use [Axios](https://axios-http.com/) or [Node-Fetch](https://www.npmjs.com/package/node-fetch) to fetch data.

- **Database**:
  - **MongoDB** (NoSQL): Great for storing player and game logs.
  - **PostgreSQL** (SQL): Better for structured stats and historical data.
  - Library: [Mongoose](https://mongoosejs.com/) (if using MongoDB).

---

### 3. Machine Learning (Stretch Goal)
- Library: [scikit-learn](https://scikit-learn.org/) for regression models and data processing.
- Model Ideas:
  - Linear Regression: Predict future performance based on past stats.
  - Time Series Forecasting: Use ARIMA or LSTM models for game-to-game predictions.
  - Clustering: Group similar player profiles for deeper analysis.

---

### 4. Deployment and Hosting
- **Frontend Hosting**:
  - [Netlify](https://www.netlify.com/) or [Vercel](https://vercel.com/) for Angular apps.

- **Backend Hosting**:
  - [Heroku](https://www.heroku.com/) for a simple setup.
  - [AWS EC2](https://aws.amazon.com/ec2/) for more flexibility.

- **Database Hosting**:
  - [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for MongoDB.
  - [ElephantSQL](https://www.elephantsql.com/) for PostgreSQL.

---

### 5. Tools for Development and Testing
- **Version Control**: [GitHub](https://github.com/) for collaboration and versioning.
- **API Testing**: [Postman](https://www.postman.com/) to test your backend endpoints.
- **Data Scraping (if needed)**:
  - [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing.
  - [Selenium](https://www.selenium.dev/) for web scraping automation.

---

### 6. Design and UI Inspiration
- **UI Kits**:
  - [Tailwind UI](https://tailwindui.com/) for pre-designed components.
  - [Shadcn UI](https://ui.shadcn.dev/) for minimalistic components.

- **Inspiration**:
  - [Baseball Savant Visuals](https://baseballsavant.mlb.com/)
  - [FanGraphs Leaderboards](https://www.fangraphs.com/leaders.aspx)

---

### 7. Learning Resources
- **APIs and Data Handling**:
  - [API Design in Node.js](https://www.digitalocean.com/community/tutorial_series/api-design-in-node-js)
  - [Working with REST APIs in Angular](https://angular.io/guide/http)

- **Data Visualization**:
  - [Chart.js Guide](https://www.chartjs.org/docs/)
  - [D3.js Tutorials](https://observablehq.com/@d3/learn-d3)

- **ML and Prediction Models**:
  - [Machine Learning with scikit-learn](https://scikit-learn.org/stable/tutorial/index.html)
  - [Time Series Analysis with Python](https://www.analyticsvidhya.com/blog/2021/07/a-comprehensive-guide-to-time-series-analysis/)

Let me know if you need more details or guidance on any section!
