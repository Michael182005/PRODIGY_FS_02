from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Employee
from datetime import date

class EmployeeTests(TestCase):
    def setUp(self):
        # Create a test staff user
        self.user = User.objects.create_user(username='teststaff', password='TestPassword123', is_staff=True)
        self.client = Client()
        self.client.login(username='teststaff', password='TestPassword123')

        # Create a sample employee
        self.employee = Employee.objects.create(
            name='John Doe',
            email='john@example.com',
            phone='+1234567890',
            salary=50000,
            hire_date=date.today()
        )

    def test_employee_list_view(self):
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')

    def test_employee_create_view(self):
        response = self.client.post(reverse('employee_create'), {
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'phone': '+1987654321',
            'salary': 60000,
            'hire_date': '2023-01-01'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Employee.objects.filter(email='jane@example.com').exists())

    def test_employee_update_view(self):
        response = self.client.post(reverse('employee_update', args=[self.employee.pk]), {
            'name': 'John Updated',
            'email': 'john@example.com',
            'phone': '+1234567890',
            'salary': 55000,
            'hire_date': '2023-01-01'
        })
        self.assertEqual(response.status_code, 302)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.name, 'John Updated')
        self.assertEqual(self.employee.salary, 55000)

    def test_employee_delete_view(self):
        response = self.client.post(reverse('employee_delete', args=[self.employee.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Employee.objects.filter(pk=self.employee.pk).exists())

    def test_unique_email_validation(self):
        response = self.client.post(reverse('employee_create'), {
            'name': 'Duplicate Email',
            'email': 'john@example.com',  # Existing email
            'phone': '+1111111111',
            'salary': 40000,
            'hire_date': '2023-01-01'
        })
        self.assertEqual(response.status_code, 200)  # Form re-rendered with errors
        self.assertFormError(response, 'form', 'email', 'Employee with this Email already exists.')

    def test_salary_positive_validation(self):
        response = self.client.post(reverse('employee_create'), {
            'name': 'Negative Salary',
            'email': 'negative@example.com',
            'phone': '+1111111111',
            'salary': -1000,
            'hire_date': '2023-01-01'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'salary', 'Ensure this value is greater than or equal to 0.')

    def test_phone_regex_validation(self):
        response = self.client.post(reverse('employee_create'), {
            'name': 'Invalid Phone',
            'email': 'phone@example.com',
            'phone': 'invalidphone',
            'salary': 30000,
            'hire_date': '2023-01-01'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'phone', 'Enter a valid phone number.')

    def test_access_control(self):
        # Logout current user
        self.client.logout()
        # Try to access employee list without login
        response = self.client.get(reverse('employee_list'))
        self.assertRedirects(response, '/login/?next=/employees/')
