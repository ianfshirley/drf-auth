from rest_framework import generics
from .serializers import JobSerializer
from .models import Job
from .permissions import IsApplicantOrReadOnly


class JobList(generics.ListCreateAPIView):
    # A QuerySet represents a collection of objects from your database. It can have zero, one or many filters. Filters narrow down the query results based on the given parameters. In SQL terms, a QuerySet equates to a SELECT statement, and a filter is a limiting clause such as WHERE or LIMIT.
    # The queryset that should be used for returning objects from this view.
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsApplicantOrReadOnly,)
    queryset = Job.objects.all()
    serializer_class = JobSerializer