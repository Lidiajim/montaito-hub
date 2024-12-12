from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, AnyOf


class FakenodoForm(FlaskForm):
    """
    Formulario para crear o editar un Fakenodo.
    """
    name = StringField(
        "Name",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(max=128, message="El nombre no puede superar los 128 caracteres.")
        ],
        render_kw={"placeholder": "Ingrese el nombre del nodo"}
    )

    status = SelectField(
        "Status",
        choices=[("active", "Active"), ("inactive", "Inactive")],
        validators=[
            DataRequired(message="El estado es obligatorio."),
            AnyOf(["active", "inactive"], message="El estado debe ser 'active' o 'inactive'.")
        ]
    )

    submit = SubmitField("Save Fakenodo")
