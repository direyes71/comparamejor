from django.db import models

# Create your models here.


STATUS_PROCESS_CREATE = 1
STATUS_PROCESS_EXECUTE = 2
STATUS_PROCESS_FINISH = 3

STATUS_PROCESS = ((STATUS_PROCESS_CREATE, 'creado'),
                    (STATUS_PROCESS_EXECUTE, 'ejecutando'),
                    (STATUS_PROCESS_FINISH, 'finalizado'),
)


class Process(models.Model):
    name = models.CharField(max_length=140, default='process')
    time = models.PositiveSmallIntegerField(default=10)
    time_executed = models.PositiveSmallIntegerField(default=0)
    status = models.PositiveSmallIntegerField(choices=STATUS_PROCESS, default=STATUS_PROCESS_CREATE)

    def remaining_time(self):
        return self.time - self.time_executed