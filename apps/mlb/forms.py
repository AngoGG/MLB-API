from django import forms


class DesiredGamesDateForm(forms.Form):
    date = forms.DateTimeField(
        label="Date désirée",
        widget=forms.DateInput(
            format=("%d-%m-%Y"),
            attrs={
                "type": "date",
            },
        ),
    )
