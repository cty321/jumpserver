# ~*~ coding: utf-8 ~*~
from __future__ import unicode_literals

from django.urls import path
from rest_framework.routers import DefaultRouter
from .. import api


app_name = "ops"

router = DefaultRouter()
router.register(r'tasks', api.TaskViewSet, 'task')
router.register(r'adhoc', api.AdHocViewSet, 'adhoc')
router.register(r'history', api.AdHocRunHistorySet, 'history')

urlpatterns = [
    path('tasks/<uuid:pk>/run/', api.TaskRun.as_view(), name='task-run'),
    path('celery/task/<uuid:pk>/log/', api.CeleryTaskLogApi.as_view(), name='celery-task-log'),
]

urlpatterns += router.urls
