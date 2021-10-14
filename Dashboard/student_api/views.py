from .serializers import CampusSerializer, InstituteSerializer, UnderGraduatesSerializer, PostGraduatesSerializer
from .models import Campus, Institute, UnderGraduates, PostGraduates
from rest_framework import viewsets

class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all().order_by('id')
    serializer_class = CampusSerializer

class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all().order_by('id')
    serializer_class = InstituteSerializer

class UnderGraduatesViewSet(viewsets.ModelViewSet):
    queryset = UnderGraduates.objects.all().order_by('id')
    serializer_class = UnderGraduatesSerializer

class PostGraduatesViewSet(viewsets.ModelViewSet):
    queryset = PostGraduates.objects.all().order_by('id')
    serializer_class = PostGraduatesSerializer

# helper
import json

def campus_util(q):
    qs = Institute.objects.get(institute_name=q.institute_name).undergraduates_set.all()
    print(qs)

def institute_util(name=""):
    qs = Campus.objects.get(campus_name=name).institute_set.all()
    dt = {}
    for q in qs:
        if 'ins' not in dt:
            dt['ins'] = [q.institute_name]
        else:
            dt['ins'].append(q.institute_name)
        campus_util(q)
    return dt

    # from student_api.views import *
    # Institute.objects.get(institute_name='git').undergraduates_set.all()
    # a = Institute.objects.get(institute_name='git').postgraduates_set.all()
    # a[0].graduates_ptr_id
    # a[0].total_students