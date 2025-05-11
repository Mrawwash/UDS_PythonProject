from django.db import models


class Question(models.Model):
    """Model representing a question in a poll.

    Attributes:
        question_text (str): The text of the question.
        pub_date (datetime): The date and time the question was published.
        image (ImageField): An optional image associated with the question.
    Methods:
        __str__(): Returns a string representation of the question text.

    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    image = models.ImageField(upload_to="poll_images/", blank=True, null=True)

    def __str__(self):
        """Returns a string representation of the question text."""
        return str(self.question_text)


class Choice(models.Model):
    """Model representing a choice for a question in a poll.
    Attributes:
        question (ForeignKey): The question this choice is related to.
        choice_text (str): The text of the choice.
        votes (int): The number of votes for this choice.
    Methods:
        __str__(): Returns a string representation of the choice text.
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
