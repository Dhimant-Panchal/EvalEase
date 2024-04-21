from django.db import models


class Keyword(models.Model):
    text = models.CharField(max_length=40)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                models.functions.Lower(
                    models.functions.Replace(
                        "text", models.Value(" "), models.Value("")
                    )
                ),
                name="text_unique",
            ),
        ]
