"""
1. AbstaractBaseClasses
부모는 테이블이 없고 자식은 테이블이 있음
2. Multitable ingeritance
부모와 자식 모두 테이블이 있음
3. Pronxy model
부모는 테이블이 있고 자식은 테이블이 없음
"""
from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    class Mata:
        abstract = True


class Student(CommonInfo):
    school = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} (학교: {self.school})'


class Instructor(CommonInfo):
    academy = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} (학원: {self.academy})'
