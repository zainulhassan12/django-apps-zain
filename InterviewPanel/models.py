import os
import re

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify

ANSWER_ORDER_OPTIONS = (
    ('content', 'Content'),
    ('none', 'None'),
    # ('random', 'Random')
)


class CategoryManager(models.Manager):

    def new_category(self, category):
        new_category = self.create(category=re.sub('\s+', '-', category)
                                   .lower())

        new_category.save()
        return new_category


class Category(models.Model):
    category = models.CharField(
        verbose_name="Category",
        max_length=250, blank=True,
        unique=True, null=True)

    objects = CategoryManager()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class Quiz(models.Model):
    title = models.CharField(
        verbose_name="Title",
        max_length=60, blank=False,
        help_text=" Descriptive Title For Quiz"
    )
    description = models.TextField(verbose_name="Description", null=True,
                                   help_text="Add some meaningful information about this Quiz.")

    url = models.SlugField(
        max_length=60, blank=True, unique=True,
        help_text="a user friendly url",
        verbose_name="user friendly url")

    # Count = models.IntegerField()
    Instructions = models.TextField(verbose_name="Instructions", null=True,
                                    help_text="Add some meaningful information about rules to follow during Quiz")
    category = models.ForeignKey(
        Category, null=True, blank=True,
        verbose_name="Category", on_delete=models.CASCADE, help_text="To Manage The Quizzes Assign a Categeory")

    answers_at_end = models.BooleanField(
        blank=False, default=False,
        help_text=("Correct answer is NOT shown after question."
                   " Answers displayed at the end."),
        verbose_name="Answers at end")

    single_attempt = models.BooleanField(
        blank=False, default=False,
        help_text=("If yes, only one attempt by"
                   " a user will be permitted."
                   " Non users cannot sit this exam."),
        verbose_name="Single Attempt")
    success_text = models.TextField(
        blank=True, help_text="Displayed if user passes.",
        verbose_name="Success Text")

    fail_text = models.TextField(
        verbose_name="Fail Text",
        blank=True, help_text="Displayed if user fails.")

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp', ]
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)

        if self.single_attempt is True:
            self.exam_paper = True

        super(Quiz, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_questions(self):
        return self.questions_set.all().select_subclasses()

    @property
    def get_max_score(self):
        return self.get_questions().count()


class Questions(models.Model):
    quiz = models.ManyToManyField(Quiz, verbose_name='Quiz',
                                  help_text="Select a Quiz to which this Question Belong")
    question = models.CharField(max_length=1000, blank=False,
                                help_text="Write Your Question in Given Box.Max Length is 500")
    explanation = models.TextField(max_length=2000,
                                   blank=True,
                                   help_text="Explanation to be shown after the question has been answered.",
                                   verbose_name='Explanation')

    def __str__(self):
        return self.question


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True)
    answer = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

    def check_correct(self, ans, num):
        for x in Answers.objects.filter(question_id=num).values() & Answers.objects.filter(answer=ans).values():
            if x['is_correct']:
                return True
            else:
                return False

    def get_correct_answer(self, qid):
        for q in Answers.objects.filter(question_id=qid).values():
            if q['is_correct']:
                return q['answer']


class InterviewQuestions(models.Model):
    Question = models.CharField(max_length=1000, verbose_name="Interview Question",
                                help_text="Question To Ask in Interview")
    Explanation = models.CharField(max_length=1000, verbose_name="Explanation",
                                   help_text="Explanation For Question")

    class Meta:
        verbose_name = "Question For Interview"
        verbose_name_plural = "Questions For Interview"

    def __str__(self):
        return self.Question


def csv_file_validator(value):
    filename, ext = os.path.splitext(value.name)
    if str(ext) != '.csv':
        raise ValidationError("Must be a csv file")


class CSVUpload(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title', blank=False,help_text="Title for your Files.")
    file = models.FileField(upload_to="Csv Of ApplicantGrades/", blank=True,
                            help_text="Paste the PDF file of your DMC/Result card for best practices",
                           )
    Uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, help_text="Time of Uploading")


class InterviewModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)
    Personality = models.PositiveIntegerField(help_text="Personality Marks__Range(1,10)",
                                              verbose_name="Personality Marks",
                                              )
    Dressing_Sense = models.PositiveIntegerField(help_text="Dressing Marks__Range(1,10)",
                                                 verbose_name="Dressing Sense",

                                                 )
    Communication_Skills = models.PositiveIntegerField(help_text="Communication Skills Marks__Range(1,10)",
                                                       verbose_name="Communication Skills",

                                                       )
    InterView_Questions = models.PositiveIntegerField(help_text="Interview Question Marks__Range(1,10)",
                                                      verbose_name="InterView Questions",

                                                      )
    total_marks_for_interview = models.FloatField(help_text="Total marks for interview",

                                                  verbose_name="Total Marks",
                                                  error_messages={'message': 'Its a negative integer field'})

    class Meta:
        verbose_name = "InterView Result"
        verbose_name_plural = "Interview Results"

    def __str__(self):
        return str(self.user)

# class QuizQuestion(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=False)
#     question = models.ManyToManyField(Questions, blank=False)
#
#     def __str__(self):
#         return "{0} {1}".format(self.quiz, self.question)

# class join(models.Model):


#     quiz = models.ForeignKey()
#     question = models.ForeignKey(Quiz, on_delete=models.CASCADE


# class correct(models.Model):
#     question = models.ForeignKey(Questions, on_delete=models.CASCADE)
#     is_correct = models.BooleanField(default=False)


# class QuizTaker(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     score = models.IntegerField(default=0)
#     completed = models.BooleanField(default=False)
#     date_finished = models.DateTimeField(null=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.user.email
#
