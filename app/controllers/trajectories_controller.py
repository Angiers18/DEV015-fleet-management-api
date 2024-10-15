from flask import request

def get_params_trajectories():

    """
    Obtiene los params:
        taxi_id: (int, required): Número de identificación de cada taxi
        date: (datetime, required): Fecha de la trayectoria
    
    returns:
        params: taxi_id, date 
    """

    taxi_id = request.args.get('taxiId')
    date = request.args.get('date')

    return taxi_id, date
