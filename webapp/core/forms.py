from django import forms

CAMERA_STATES = (
    ("-45", "-45"),
    ("0", "0"),
    ("45", "45"),
    ("90", "90")
)

class CameraRotate(forms.Form):
    camera_rotation = forms.ChoiceField(choices=CAMERA_STATES)