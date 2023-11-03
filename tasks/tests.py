from django.contrib.auth import get_user_model
from django.utils import timezone
from django.test import TestCase

from .models import Task


class TaskTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='test_password')
        self.user.save()
        due_datetime = (timezone.now() + timezone.timedelta(days=10)).replace(hour=0, minute=0, second=0, microsecond=0)
        self.task = Task.objects.create(author=self.user,
                                        title='Task-1',
                                        status='TO_DO',
                                        description='description',
                                        due_date=due_datetime)
        self.task.save()

    def tearDown(self):
        self.user.delete()

    def test_read_task(self):
        self.assertEqual(self.task.author, self.user)
        self.assertEqual(self.task.title, 'Task-1')
        self.assertEqual(self.task.status, 'TO_DO')
        self.assertEqual(self.task.description, 'description')
        due_datetime = (timezone.now() + timezone.timedelta(days=10)).replace(hour=0, minute=0, second=0, microsecond=0)
        self.assertEqual(self.task.due_date, due_datetime)

    def test_task_created_date(self):
        self.assertIsNotNone(self.task.created_date)

    def test_task_updated_date(self):
        self.assertIsNotNone(self.task.updated_date)

    def test_update_task_title(self):
        self.task.title = 'Updated Task'
        self.task.save()
        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.title, 'Updated Task')

    def test_update_task_status(self):
        self.task.status = 'DONE'
        self.task.save()
        self.assertEqual(self.task.status, 'DONE')

    def test_update_task_description(self):
        self.task.description = 'new description'
        self.task.save()
        self.assertEqual(self.task.description, 'new description')

    def test_update_task_due_date(self):
        due_datetime = (timezone.now() + timezone.timedelta(days=10)).replace(hour=0, minute=0, second=0, microsecond=0)
        self.task.due_date = due_datetime
        self.task.save()
        self.assertEqual(self.task.due_date, due_datetime)

    def test_delete_task(self):
        task_id = self.task.id
        self.task.delete()
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task_id)

    def test_read_task(self):
        self.assertEqual(self.task.author, self.user)
        self.assertEqual(self.task.title, 'Task-1')
        self.assertEqual(self.task.status, 'TO_DO')
        self.assertEqual(self.task.description, 'description')
        due_datetime = (timezone.now() + timezone.timedelta(days=10)).replace(hour=0, minute=0, second=0, microsecond=0)
        self.assertEqual(self.task.due_date, due_datetime)


class TaskCreationLimitTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='test_password')
        self.user.save()
        self.client.post('/login/', {'username': 'test', 'password': 'test_password'})

    def tearDown(self):
        self.user.delete()

    def test_task_creation_limit(self):
        # Creating 5 tasks on the same day
        today_date = timezone.now().date()
        due_datetime = (timezone.now() + timezone.timedelta(days=10)).replace(hour=0, minute=0, second=0, microsecond=0)
        for _ in range(5):
            self.task = Task.objects.create(author=self.user, title='Test Task', status='TO_DO',
                                            description='Test description', due_date=due_datetime)
            self.task.save()

        # Attempt to create another task
        response = self.client.post('/tasks/add/', {'author_id': self.user.id, 'title': 'New Task', 'status': 'TODO',
                                                    'description': 'New description', 'due_date': timezone.now()})
        # # Check if the response redirects to the home page
        self.assertRedirects(response, '/home/')

        # Check if the task count is still 5
        task_count = Task.objects.filter(created_date__date=today_date).count()
        self.assertEqual(task_count, 5)
