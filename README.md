# ShieldRx - Vaccine Recommendation System

ShieldRx is a web-based application that provides personalized vaccine recommendations based on age and disease conditions. The system aims to help users make informed decisions about vaccinations by providing accurate, up-to-date information.

## Features

- **User Authentication**
  - Register/Login functionality

- **Vaccine Recommendations**
  - Age-based vaccine suggestions
  - Disease-specific vaccine recommendations
  - Comprehensive vaccine database

- **Information Hub**
  - Current medical news
  - Healthcare department updates
  - FAQs about vaccinations
  - Image gallery

- **Contact System**
  - User inquiry form
  - Direct contact information
  - Location details

## Technical Stack

- **Backend**
  - Django 5.1.2
  - MySQL Database
  - Python 3.12.4

- **Frontend**
  - HTML5/CSS3
  - Bootstrap
  - JavaScript
  - jQuery

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/shieldrx.git
cd shieldrx
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the MySQL database:
```sql
CREATE DATABASE website;
CREATE DATABASE vaccines;
```

5. Configure database settings in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'website',
        'USER': 'root',
        'PASSWORD': '@riya123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

6. Run migrations:
```bash
python manage.py migrate
```

7. Start the development server:
```bash
python manage.py runserver
```

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255),
    password VARCHAR(255),
    phone_no VARCHAR(15),
    dob DATE,
    gender VARCHAR(10)
);
```

### Vaccines Table
```sql
CREATE TABLE vaccines_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    vaccine_name VARCHAR(255),
    min_age INT,
    max_age INT,
    disease VARCHAR(255)
);
```

## Usage

1. Register a new account or login with existing credentials
2. Navigate to Services section
3. Choose recommendation type:
   - By Age
   - By Disease
4. View personalized vaccine recommendations
5. Access additional information through the news section
6. Contact support for any queries

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Contact

- Email: ShieldRx@gmail.com
- Phone: +1 0000 1111 2222
- Location: D.Y.Patil College of Engineering, Akurdi, Pune, Maharashtra, India

## Acknowledgments

- Django Documentation
- Bootstrap Templates
- Medical Information Sources
- Contributors and Team Members
