from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    """View for displaying the latest questions in the poll.

    Attributes:
        model (Question): The model representing the question.
        template_name (str): The name of the template to render.
        context_object_name (str): The name of the context variable to use in the template.
    """

    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    """View for displaying the details of a specific question.

    Attributes:
        model (Question): The model representing the question.
        template_name (str): The name of the template to render.
    """

    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    """View for displaying the results of a specific question.
    Attributes:
        model (Question): The model representing the question.
        template_name (str): The name of the template to render.
    """

    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    """Handle the voting process for a specific question.
    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the question being voted on.
    Returns:
        HttpResponseRedirect: Redirects to the results page of the question.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
