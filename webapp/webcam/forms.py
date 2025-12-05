from django import forms

CAMERA_STATES = (
    ("-45", "-45"),
    ("0", "0"),
    ("45", "45"),
    ("90", "90")
)

#Not really needed since I have the dual setup now
CAMERAS = (
    ("1", "1"),
    ("2", "2")
)

class CameraRotate(forms.Form):
    camera_rotation = forms.ChoiceField(choices=CAMERA_STATES)
    #camera_feed = forms.ChoiceField(choices = CAMERAS)