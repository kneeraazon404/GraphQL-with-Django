from graphene import ObjectType, Schema
from graphene_django import DjangoListField, DjangoObjectType

from quiz.models import Answer, Category, Question, Quizzes


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = (
            "id",
            "title",
            "category",
        )


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz", "answer")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")


class Query(ObjectType):
    all_quizzes = DjangoListField(QuizzesType)


schema = Schema(query=Query)
