from django.shortcuts import render
import mysql.connector as sql
import copy



def serviceage_action(request):
    # Connect to MySQL database
    conn = sql.connect(host="localhost", user="root", passwd="@riya123", database="vaccines")
    
    cursor = conn.cursor()
   
    if request.method != "POST":

        cursor.execute("SELECT * FROM vaccines_data")
       
        rows = cursor.fetchall()
    
        cursor.close()
        conn.close()
   
        modified_rows = [list(row) for row in rows]
        

        for row in modified_rows:
            max_age = row[3]
            if max_age == 0:
                row[3] = None    
            elif max_age < 1:
                row[3] = f"{int(max_age * 30)} weeks"
            elif max_age >= 12:
                row[3] = f"{int(max_age / 12)} years"
            else:
                row[3] = f"{int(max_age)} months"
       
        for row in modified_rows:
            min_age = row[2]
            if min_age == 0:
                row[2] = None
            elif min_age < 1:
                row[2] = f"{int(min_age * 30)} weeks"
            elif min_age >= 12:
                row[2] = f"{int(min_age / 12)} years"
            else:
                row[2] = f"{int(min_age)} months"
       
        # Pass modified rows to the template
        return render(request, 'vaccines.html', {'rows': modified_rows})

    else: 
        age = request.POST.get('age')
        age_in_months = int(age) * 12  

        query = "SELECT * FROM vaccines_data WHERE min_age >= %s"
        cursor.execute(query, (age_in_months,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        modified_rows = [list(row) for row in rows]
        
        for row in modified_rows:
            max_age = row[3]
            if max_age == 0:
                row[3] = None    
            elif max_age < 1:
                row[3] = f"{int(max_age * 30)} weeks"
            elif max_age >= 12:
                row[3] = f"{int(max_age / 12)} years"
            else:
                row[3] = f"{int(max_age)} months"
       
        # Modify the rows to handle different cases for displaying the minimum age
        for row in modified_rows:
            min_age = row[2]
            if min_age == 0:
                row[2] = None
            elif min_age < 1:
                row[2] = f"{int(min_age * 30)} weeks"
            elif min_age >= 12:
                row[2] = f"{int(min_age / 12)} years"
            else:
                row[2] = f"{int(min_age)} months"
    
        return render(request, 'vaccines.html', {'rows': modified_rows})

def servicedisease_action(request):
    conn = sql.connect(host="localhost", user="root", passwd="@riya123", database="vaccines")
    
    cursor = conn.cursor()
   
    if request.method != "POST":
  
           cursor.execute("SELECT * FROM vaccines_data")
       
           rows = cursor.fetchall()
       
           # Close cursor and database connection
           cursor.close()
           conn.close()
       
          
           modified_rows = []
           for row in rows:
               max_age = row[3]
               if max_age == 0:
                   
                   modified_row = list(row)
                   modified_row[3] = None  # Set max_age to None
                   modified_rows.append(modified_row)
               elif max_age < 1:
        
                   modified_row = list(row)
                   modified_row[3] = int(max_age * 30)  # Age in weeks
                   modified_rows.append(modified_row)
               elif max_age >= 12:
                 
                   modified_row = list(row)
                   modified_row[3] = int(max_age / 12)  # Age in years
                   modified_rows.append(modified_row)
               else:
                   modified_row = list(row)
                   modified_row[3] = int(max_age)  # Age in months
                   modified_rows.append(modified_row)
       
           for row in modified_rows:
               min_age = row[2]
               if min_age == 0:
                
                   row[2] = None  # Set min_age to None
               elif min_age < 1:
                  
                   row[2] = int(min_age * 30)  # Age in weeks
               elif min_age >= 12:
                 
                   row[2] = int(min_age / 12)  # Age in years
               else:
                 
                   row[2] = int(min_age)  # Age in months
       
       
           return render(request, 'vaccines_disease.html', {'rows': modified_rows})
    
    else: 
        dis = request.POST.get('disease')
        query = "SELECT * FROM vaccines_data WHERE disease = %s"
        cursor.execute(query, (dis,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        modified_rows = [list(row) for row in rows]
       
        for row in modified_rows:
            max_age = row[3]
            if max_age == 0:
                row[3] = None    
            elif max_age < 1:
                row[3] = f"{int(max_age * 30)} weeks"
            elif max_age >= 12:
                row[3] = f"{int(max_age / 12)} years"
            else:
                row[3] = f"{int(max_age)} months"
       
       
        for row in modified_rows:
            min_age = row[2]
            if min_age == 0:
                row[2] = None
            elif min_age < 1:
                row[2] = f"{int(min_age * 30)} weeks"
            elif min_age >= 12:
                row[2] = f"{int(min_age / 12)} years"
            else:
                row[2] = f"{int(min_age)} months"
   
        return render(request, 'vaccines_disease.html', {'rows': modified_rows})

       