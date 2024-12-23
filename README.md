# CSV Analysis Web Application

This is a Django-based web application that allows users to upload CSV files, perform basic data analysis using pandas and numpy, and visualize the results using matplotlib and seaborn. The analysis results and visualizations are displayed on a web interface.

---

## **Features**

- Upload CSV files through a user-friendly web interface.
- Perform data analysis:
  - Display the first few rows of the dataset.
  - Calculate summary statistics (mean, median, standard deviation, etc.) for numerical columns.
  - Identify and handle missing values.
- Generate visualizations:
  - Histograms for numerical columns.
  - Display plots directly on the webpage.

---

## **Technologies Used**

- **Backend**: Django, Python
- **Data Analysis**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Frontend**: HTML, Bootstrap

---

## **Installation and Setup**

### **Prerequisites**

Ensure you have the following installed on your system:

- Python 3.8 or higher
- pip (Python package manager)

### **Steps to Set Up the Application**

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate   # For Windows
   ```

3. **Install Required Dependencies**

   ```bash
   pip install django pandas matplotlib seaborn
   ```

4. **Set Up the Django Project**

   - Navigate to the project folder where `manage.py` is located.
   - Apply database migrations:
     ```bash
     python manage.py migrate
     ```

5. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   - Open your browser and visit: `http://127.0.0.1:8000`

6. **Upload and Analyze CSV Files**

   - Use the upload form on the homepage to upload your CSV file.
   - View analysis results and visualizations directly on the webpage.

---

## **Directory Structure**

```
project-root/
|-- manage.py
|-- project/
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- app/
|   |-- views.py
|   |-- urls.py
|   |-- templates/
|       |-- upload.html
|-- uploaded_files/ (temporary storage for uploaded files)
```

---

## **Usage Instructions**

### **Uploading a CSV File**

1. Click the "Choose File" button on the homepage.
2. Select a CSV file from your computer.
3. Click the "Upload" button to process the file.

### **Viewing Analysis Results**

- **Dataset Preview**: Displays the first few rows of the dataset.
- **Summary Statistics**: Numerical statistics such as mean, median, and standard deviation.
- **Missing Values**: Table showing the count of missing values for each column.

### **Viewing Visualizations**

- View histograms for numerical columns, showing their distribution.

---

## **Troubleshooting**

### **Common Errors**

1. **Django Not Installed**
   - Run: `pip install django`
2. **pandas or matplotlib Not Installed**
   - Run: `pip install pandas matplotlib seaborn`
3. **File Not Uploading**
   - Ensure the file is a valid CSV format.
   - Check the file size limits in Django settings (default: 2.5 MB).

### **Logs and Debugging**

- Check logs in the terminal where the server is running.
- Use Django's built-in `DEBUG` mode in `settings.py` for detailed error messages:
  ```python
  DEBUG = True
  ```

---

## **Deliverables**

1. **GitHub Repository**
   - Include the full project code.
2. **README File**
   - Detailed setup instructions and usage guide.
3. **Sample CSV File**
   - Include a sample CSV file (`sample.csv`) for testing purposes.

---

## **Contributing**

- Fork the repository.
- Create a feature branch (`git checkout -b feature-name`).
- Commit changes (`git commit -m 'Add feature'`).
- Push to the branch (`git push origin feature-name`).
- Open a pull request.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---



