from django.shortcuts import render, redirect
from django.contrib import messages
import mysql.connector as sql
from datetime import datetime

def register_action(request):
    if request.method == "POST":
        try:
            # Get form data
            username = request.POST.get("Username")
            password = request.POST.get("Password")
            phone_no = request.POST.get("Phone_No")
            dob = request.POST.get("DOB")
            gender = request.POST.get("Gender")

            # Validate required fields
            if not all([username, password]):
                messages.error(request, "Username and password are required")
                return render(request, 'registration_form.html')

            # Convert DOB if provided
            if dob:
                try:
                    dob = datetime.strptime(dob, '%d/%m/%Y').strftime('%Y-%m-%d')
                except ValueError:
                    messages.error(request, "Invalid date format. Use DD/MM/YYYY")
                    return render(request, 'registration_form.html')

            # Database connection with context manager
            with sql.connect(
                host="localhost",
                user="root",
                passwd="@riya123",
                database="website"
            ) as conn:
                with conn.cursor() as cursor:
                    # Use parameterized query to prevent SQL injection
                    query = """
                        INSERT INTO users (username, password, phone_no, dob, gender) 
                        VALUES (%s, %s, %s, %s, %s)
                    """
                    cursor.execute(query, (username, password, phone_no, dob, gender))
                    conn.commit()

            messages.success(request, "Registration successful!")
            return redirect('index')  # Redirect to index page

        except sql.Error as e:
            messages.error(request, f"Database error: {str(e)}")
            return render(request, 'registration_form.html')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'registration_form.html')

    # GET request - show empty form
    return render(request, 'registration_form.html')