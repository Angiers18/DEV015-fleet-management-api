from flask import request

def get_params_trajectories():

    """
    obtiene los params:
        taxi_id: (int, required): numero de identificación de cada taxi
        date: (datetime, required): fecha de la trayectoria
    
    returns:
        params: taxi_id, date 
    """

    taxi_id = request.args.get('taxiId')
    date = request.args.get('date')

    return taxi_id, date
