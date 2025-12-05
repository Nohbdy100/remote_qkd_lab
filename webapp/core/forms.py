from django import forms

LENS_STATES = (
    ("-45", "-45"),
    ("0", "0"),
    ("45", "45"),
    ("90", "90")
)

class LensPolarity(forms.Form):
    lens_rotation = forms.ChoiceField(choices=LENS_STATES)