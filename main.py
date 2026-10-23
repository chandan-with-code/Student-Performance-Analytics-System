import pandas as pd
import numpy as np

def load_student_data(filename):
    """Step 2: Read the CSV file using Pandas"""
    df = pd.read_csv(filename)
    print("--- Initial Student Dataset ---")
    print(df.head(), "\n")
    return df

def process_performance(df):
    """Step 3: Process data to calculate totals, averages, grades, and pass/fail status"""
    subject_cols = ['Maths', 'Science', 'English']
    
    # Calculate Total and Average Marks using Pandas/NumPy
    df['Total_Marks'] = df[subject_cols].sum(axis=1)
    df['Average_Marks'] = df[subject_cols].mean(axis=1)
    
    # Reusable function for grading rules
    def get_grade(avg):
        if avg >= 85:
            return 'A'
        elif avg >= 70:
            return 'B'
        elif avg >= 50:
            return 'C'
        else:
            return 'D'
            
    df['Grade'] = df['Average_Marks'].apply(get_grade)
    
    # Identify Pass/Fail using NumPy condition (Passing average >= 50)
    df['Status'] = np.where(df['Average_Marks'] >= 50, 'Pass', 'Fail')
    
    return df

def analyze_performance(df):
    """Step 4: Perform practical analysis questions"""
    subject_cols = ['Maths', 'Science', 'English']
    
    print("========================================")
    print("      STUDENT PERFORMANCE ANALYSIS      ")
    print("========================================")
    
    # Overall class statistics
    print(f"Total Students: {len(df)}")
    print(f"Overall Class Average Marks: {df['Average_Marks'].mean():.2f}")
    print(f"Total Students Passed: {(df['Status'] == 'Pass').sum()}")
    print(f"Total Students Failed: {(df['Status'] == 'Fail').sum()}")
    
    # Top Performing Student
    top_student = df.loc[df['Average_Marks'].idxmax()]
    print(f"\nTop Performer: {top_student['Name']} (Dept: {top_student['Department']}) with Average: {top_student['Average_Marks']:.2f}")
    
    # Subject-wise performance
    print("\n--- Subject-wise Average Marks ---")
    print(df[subject_cols].mean().round(2))
    
    print("\n--- Highest Marks in Each Subject ---")
    print(df[subject_cols].max())
    
    print("\n--- Lowest Marks in Each Subject ---")
    print(df[subject_cols].min())

if __name__ == "__main__":
    # 1. Load Data
    data_file = 'students.csv'
    student_df = load_student_data(data_file)
    
    # 2. Process Data
    processed_df = process_performance(student_df)
    print("--- Processed Data Summary ---")
    print(processed_df[['StudentID', 'Name', 'Total_Marks', 'Average_Marks', 'Grade', 'Status']], "\n")
    
    # 3. Analyze Data
    analyze_performance(processed_df)
    
    # 4. Save Final Output (Optional)
    processed_df.to_csv('processed_students.csv', index=False)
    print("\n[INFO] Processed results successfully saved to 'processed_students.csv'")