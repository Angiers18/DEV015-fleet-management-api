def dict_latest_trajectories(last_trajectories):

    """
     convierte los datos de las últimas trayectorias en una lista de diccionarios

    args: 
        (list) Data de las ultimas trajectorias con 'taxiId', 'plate', 'date',
        'latitude', 'longitude'

    returns:

    lista de diccionario con la siguiente data:

        -taxiId (int): id del taxi
        -plate (str): placa del taxi
        -timestamp (datetime): fecha y hora de la última trayectoria
        -latitude (float): latitud de la última ubicación registrada
        -longitude (float): longitud de la última ubicación registrada
        })
    """

    dict_trajectories = []
    for trajectory in last_trajectories:
        dict_trajectories.append({
            'taxiId': trajectory.id,
            'plate': trajectory.plate,
            'timestamp': trajectory.date,
            'latitude': trajectory.latitude,
            'longitude': trajectory.longitude
        })
    return dict_trajectories
