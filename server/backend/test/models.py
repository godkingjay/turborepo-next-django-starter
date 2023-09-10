from django.db import models


class Test(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    age = models.IntegerField()

    verbose_name = "Test"
    verbose_name_plural = "Tests"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TestReference(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(
        upload_to="storage/images", blank=True, null=True, default=None
    )
    author = models.ForeignKey(Test, on_delete=models.CASCADE)

    verbose_name = "Test Reference"
    verbose_name_plural = "Test References"

    def __str__(self):
        return self.title
