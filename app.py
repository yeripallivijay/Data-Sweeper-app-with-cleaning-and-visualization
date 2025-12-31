import streamlit as st
import pandas as pd
import json
import sqlite3
import tempfile
import os

st.title("📊 Universal Data File Uploader for Data Scientists")

# File uploader with all common data science file types
uploaded_file = st.file_uploader(
    "Choose a file",
    type=["csv", "xlsx", "xls", "json", "parquet", "txt", "tsv", "xml", "sqlite", "db", "sql"],
    help="Supports: CSV, Excel, JSON, Parquet, TXT, TSV, XML, and SQLite databases"
)

if uploaded_file is not None:
    try:
        # Display file details
        st.info(f"**File Name:** {uploaded_file.name}")
        st.info(f"**File Size:** {uploaded_file.size / 1024:.2f} KB")
        st.info(f"**File Type:** {uploaded_file.type}")
        
        df = None
        
        # CSV files
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            st.success(" CSV file loaded successfully!")
        
        # Excel files
        elif uploaded_file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file)
            st.success(" Excel file loaded successfully!")
        
        # JSON files
        elif uploaded_file.name.endswith('.json'):
            # Try reading as JSON
            json_data = json.load(uploaded_file)
            df = pd.json_normalize(json_data) if isinstance(json_data, list) else pd.DataFrame([json_data])
            st.success(" JSON file loaded successfully!")
        
        # Parquet files
        elif uploaded_file.name.endswith('.parquet'):
            df = pd.read_parquet(uploaded_file)
            st.success(" Parquet file loaded successfully!")
        
        # TSV files (Tab-separated values)
        elif uploaded_file.name.endswith('.tsv'):
            df = pd.read_csv(uploaded_file, sep='\t')
            st.success(" TSV file loaded successfully!")
        
        # TXT files
        elif uploaded_file.name.endswith('.txt'):
            # Try different delimiters
            try:
                df = pd.read_csv(uploaded_file, sep=',')
            except:
                try:
                    df = pd.read_csv(uploaded_file, sep='\t')
                except:
                    content = uploaded_file.read().decode('utf-8')
                    st.text_area("File Content:", content, height=300)
                    st.warning(" Could not parse as tabular data. Displaying raw content.")
            if df is not None:
                st.success(" TXT file loaded successfully!")
        
        # XML files
        elif uploaded_file.name.endswith('.xml'):
            df = pd.read_xml(uploaded_file)
            st.success(" XML file loaded successfully!")
        
        # SQLite database files
        elif uploaded_file.name.endswith(('.sqlite', '.db', '.sql')):
            # Save to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.db') as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_path = tmp_file.name
            
            # Connect to database
            conn = sqlite3.connect(tmp_path)
            cursor = conn.cursor()
            
            # Get all tables
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            
            if tables:
                st.success(f" Database loaded successfully! Found {len(tables)} table(s).")
                
                # Let user select table
                table_names = [table[0] for table in tables]
                selected_table = st.selectbox("Select a table to view:", table_names)
                
                if selected_table:
                    df = pd.read_sql_query(f"SELECT * FROM {selected_table}", conn)
            else:
                st.warning(" No tables found in the database.")
            
            conn.close()
            os.unlink(tmp_path)  # Clean up temp file
        
        # Display DataFrame if available
        if df is not None:
            st.write("###  File Content Preview:")
            st.dataframe(df, use_container_width=True)
            
            # Display basic statistics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Rows", df.shape[0])
            with col2:
                st.metric("Columns", df.shape[1])
            with col3:
                st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024:.2f} KB")
            
            # Display column information
            with st.expander(" Column Information"):
                col_info = pd.DataFrame({
                    'Column Name': df.columns,
                    'Data Type': df.dtypes.values,
                    'Non-Null Count': df.count().values,
                    'Null Count': df.isnull().sum().values
                })
                st.dataframe(col_info, use_container_width=True)
            
            # Display descriptive statistics for numeric columns
            if df.select_dtypes(include=['number']).shape[1] > 0:
                with st.expander(" Descriptive Statistics"):
                    st.dataframe(df.describe(), use_container_width=True)
            
            # Download button for processed data
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇ Download as CSV",
                data=csv,
                file_name=f"processed_{uploaded_file.name.split('.')[0]}.csv",
                mime="text/csv"
            )
        
    except Exception as e:
        st.error(f" Error reading file: {e}")
        st.info(" Tip: Make sure your file is properly formatted and not corrupted.")

else:
    st.info("👆 Please upload a file to get started!")
    
    # Show supported formats
    with st.expander("⬇️ Supported File Formats"):
        st.markdown("""
        - **CSV** (.csv) - Comma-separated values
        - **Excel** (.xlsx, .xls) - Microsoft Excel files
        - **JSON** (.json) - JavaScript Object Notation
        - **Parquet** (.parquet) - Apache Parquet columnar format
        - **TSV** (.tsv) - Tab-separated values
        - **TXT** (.txt) - Plain text files
        - **XML** (.xml) - Extensible Markup Language
        - **SQLite** (.sqlite, .db, .sql) - SQLite database files
        """)
