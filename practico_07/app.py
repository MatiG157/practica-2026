from flask import Flask, flash, redirect, render_template, request, url_for

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import (
    DniRepetido,
    LongitudInvalida,
    MaximoAlcanzado,
    NegocioSocio,
)


app = Flask(__name__)
app.config["SECRET_KEY"] = "tp7-secret-key"

negocio = NegocioSocio()


def _parse_dni(raw_dni):
    try:
        return int(raw_dni)
    except (TypeError, ValueError):
        return None


@app.route("/")
def index():
    socios = negocio.todos()
    return render_template("index.html", socios=socios)


@app.route("/alta", methods=["GET", "POST"])
def alta():
    if request.method == "POST":
        dni = _parse_dni(request.form.get("dni"))
        nombre = (request.form.get("nombre") or "").strip()
        apellido = (request.form.get("apellido") or "").strip()

        if dni is None:
            flash("El DNI debe ser numerico.", "error")
            return render_template(
                "form.html",
                titulo="Alta de Socio",
                accion="Guardar",
                socio=None,
                valores={"dni": request.form.get("dni", ""), "nombre": nombre, "apellido": apellido},
            )

        socio = Socio(dni=dni, nombre=nombre, apellido=apellido)
        try:
            negocio.alta(socio)
            flash("Socio dado de alta correctamente.", "ok")
            return redirect(url_for("index"))
        except (DniRepetido, LongitudInvalida, MaximoAlcanzado) as error:
            flash(str(error), "error")

        return render_template(
            "form.html",
            titulo="Alta de Socio",
            accion="Guardar",
            socio=None,
            valores={"dni": request.form.get("dni", ""), "nombre": nombre, "apellido": apellido},
        )

    return render_template(
        "form.html",
        titulo="Alta de Socio",
        accion="Guardar",
        socio=None,
        valores={"dni": "", "nombre": "", "apellido": ""},
    )


@app.route("/baja/<int:id_socio>", methods=["POST"])
def baja(id_socio):
    exito = negocio.baja(id_socio)
    if exito:
        flash("Socio eliminado correctamente.", "ok")
    else:
        flash("No se encontro el socio a eliminar.", "error")
    return redirect(url_for("index"))


@app.route("/modificar/<int:id_socio>", methods=["GET", "POST"])
def modificar(id_socio):
    socio = negocio.buscar(id_socio)
    if socio is None:
        flash("No se encontro el socio solicitado.", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        dni = _parse_dni(request.form.get("dni"))
        nombre = (request.form.get("nombre") or "").strip()
        apellido = (request.form.get("apellido") or "").strip()

        if dni is None:
            flash("El DNI debe ser numerico.", "error")
            return render_template(
                "form.html",
                titulo="Modificar Socio",
                accion="Aceptar",
                socio=socio,
                valores={"dni": request.form.get("dni", ""), "nombre": nombre, "apellido": apellido},
            )

        otro = negocio.buscar_dni(dni)
        if otro is not None and otro.id != socio.id:
            flash("El DNI ya esta registrado.", "error")
            return render_template(
                "form.html",
                titulo="Modificar Socio",
                accion="Aceptar",
                socio=socio,
                valores={"dni": request.form.get("dni", ""), "nombre": nombre, "apellido": apellido},
            )

        socio.dni = dni
        socio.nombre = nombre
        socio.apellido = apellido

        try:
            negocio.modificacion(socio)
            flash("Socio modificado correctamente.", "ok")
            return redirect(url_for("index"))
        except LongitudInvalida as error:
            flash(str(error), "error")

        return render_template(
            "form.html",
            titulo="Modificar Socio",
            accion="Aceptar",
            socio=socio,
            valores={"dni": request.form.get("dni", ""), "nombre": nombre, "apellido": apellido},
        )

    return render_template(
        "form.html",
        titulo="Modificar Socio",
        accion="Aceptar",
        socio=socio,
        valores={"dni": socio.dni, "nombre": socio.nombre, "apellido": socio.apellido},
    )


if __name__ == "__main__":
    app.run(debug=True)
