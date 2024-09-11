from datetime import datetime
from sqlalchemy import func
from flask import Blueprint, request, jsonify
from app.database.db import db
from app.models import Trajectory


bp_route_trajectories = Blueprint('bp_route_trajectories', __name__, url_prefix='/trajectories' )

@bp_route_trajectories.route("/", methods=['GET'])
def get_trajectories() :

    """
    Obtiene una lista de trayectorias de un taxi desde la base de datos.

    La ruta responde a una solicitud GET y requiere los parámetros obligatorios 
    `taxiId` y `date` para filtrar las trayectorias del taxi en una fecha específica.

    Query Params:
    taxiId (int, requerido): El ID del taxi para obtener sus trayectorias.
    date (str, requerido): La fecha específica para en formato DD-MM-YYYY.

    Returns:
    list[dict]: Una lista de diccionarios que representan las trayectorias del taxi en la fecha proporcionada.
    Si no encuentra trayectorias o faltan parámetros, devuelve un mensaje de error en formato JSON.
    
    Status Codes:
    400: Faltan parámetros requeridos o el formato de la fecha es incorrecto.
    404: No se encontraron trayectorias para el taxi y la fecha proporcionados.
    """

    taxi_id = request.args.get('taxiId', '')
    if not taxi_id:
        return jsonify({"error": "El ID del taxi es obligatorio"}), 400

    date = request.args.get('date')

    if not date:
        return jsonify({"error": "La fecha es obligatoria"}), 400
    try:
        date = datetime.strptime(date, '%d-%m-%Y')

    except ValueError:
        return jsonify({"error": "Fecha invalida, por favor usa el formato DD-MM-YYYY"}), 400

    query = db.session.query(Trajectory)

    trajectories = query.filter(
    Trajectory.taxi_id == taxi_id,
    func.date(Trajectory.date) == date.date()  # Comparar solo la fecha sin la hora
    ).all()

    if not trajectories:
        return jsonify({"error": "No se encontraron trayectorias para el taxi y fecha proporcionados"}), 404
    
    return jsonify([trajectory.to_dict() for trajectory in trajectories])
