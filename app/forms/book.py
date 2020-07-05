from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, Required, NumberRange


class SearchForm(Form):
    q = StringField(validators=[Required(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
