import json
import re

json_path = "/Users/juandchaves/src/utn/I/prog_lab/Parcial/dt.json"


def json_reader(path: str) -> list:
    with open(path, "r") as file:
        dream_team_dict = json.load(file)

    return dream_team_dict


players = json_reader(json_path)
players_list = players["jugadores"]

"""
average()
verify_input(input_value: str)
greater_than_average(value: str)
best_by_key()
print_result()??
"""

# 1


def player_by_position(players_list: list) -> None:
    """
    Receives the list of dicts of players.
    Prints each player and its position.
    """
    aux_players_list = players_list.copy()
    for player in aux_players_list:
        message = "{0} - {1}".format(player["nombre"], player["posicion"])
        print(message)


def find_player_name() -> any:
    """
    Ask the user for a name to find in the list of players
    Returns a list of matches or a error message string
    """
    aux_players_list = players_list.copy()
    users_input = input("Ingresa el nombre de un jugador: ").capitalize()
    result = "** ERROR ** No se encontraron resultados"
    filtered_players = []

    # INTENTAR HACER UNA VARIACION CON REGEX

    for player in aux_players_list:
        if re.search(users_input, player["nombre"]) != None:
            filtered_players.append(player["nombre"])
            result = filtered_players

    return result


def find_player_id(players_list: list) -> any:
    """
    Receives the list of players
    Ask the user for an id to find in the list of players
    Returns a list of matches or a error message string
    """
    users_input = input("Ingresa el id de un jugador: ")
    total_players = len(players_list)
    pattern = "^\d+$"

    result = "** ERROR ** No se encontraron resultados"

    if re.match(pattern, users_input) != None:
        users_input_int = int(users_input)
        if users_input_int >= 0 and users_input_int < total_players:
            result = users_input_int

    return result


# 2
def player_stats() -> tuple:
    """
    Creates and prints a string with the values of each of the fields in "estadisticas"
    Returns a tuple with the player id and the string with the values.
    """
    aux_players_list = players_list.copy()
    player = find_player_id(aux_players_list)
    player_dict = aux_players_list[player]
    message = "Jugador: {0}.\nTemporadas jugadas: {1}.\nPuntos totales: {2}.\nPromedio de puntos por partido: {3}.\nRebotes totales: {4}.\nPromedio de rebotes por partido: {5}\nAsistencias totales: {6}.\nPromedio de asistencias por partido: {7}.\nRobos totales: {8}.\nBloqueos totales: {9}.\nPorcentaje de tiros de campo: {10}%.\nPorcentaje de tiros libres: {11}%.\nPorcentaje de tiros triples: {12}%.".format(
        player_dict["nombre"],
        player_dict["estadisticas"]["temporadas"],
        player_dict["estadisticas"]["puntos_totales"],
        player_dict["estadisticas"]["promedio_puntos_por_partido"],
        player_dict["estadisticas"]["rebotes_totales"],
        player_dict["estadisticas"]["promedio_rebotes_por_partido"],
        player_dict["estadisticas"]["asistencias_totales"],
        player_dict["estadisticas"]["promedio_asistencias_por_partido"],
        player_dict["estadisticas"]["robos_totales"],
        player_dict["estadisticas"]["bloqueos_totales"],
        player_dict["estadisticas"]["porcentaje_tiros_de_campo"],
        player_dict["estadisticas"]["porcentaje_tiros_libres"],
        player_dict["estadisticas"]["porcentaje_tiros_triples"],
    )

    print(message)

    result = (player, message)
    return result  # This tuple could be used as a format variation to be used by csv_writer

    # *Print*
    # key: value
    # key: value
    # key: value

    # *Save csv*
    # key   key   key
    # value value value


def csv_writer(path: str, stats_list: list) -> None:
    """
    Recieves the path to save the csv file and a list of lists that contain 1 row of keys and at least 1 row or values
    """
    if len(stats_list) > 1:
        with open(path, "w+") as file:
            is_key = True
            for index in range(len(stats_list)):
                if is_key == True:
                    key_row = ", ".join(stats_list[index])
                    file.write("{0}\n".format(key_row))
                    is_key = False
                    print("index: ", index)
                else:
                    print("index: ", index)
                    print("values: ", stats_list[index])
                    value_row = ", ".join(stats_list[index])
                    file.write("{0}\n".format(value_row))
                index += 1
    else:
        print("*ERROR*")


def create_stats_list(player_dict: dict, player_id: str) -> list:
    """
    Receives a player dict and a string with the current player's id
    Returns a list of lists where list[0] == keys and list[1+] == values
    """
    stats_list = []
    key_list = ["id", "nombre"]
    value_list = [str(player_id), player_dict["nombre"]]

    stats_list.append(key_list)
    stats_list.append(value_list)
    for key, value in player_dict["estadisticas"].items():
        key_list.append(key)
        value_list.append(str(value))
    return stats_list


# 3
def player_stats_csv():
    aux_players_list = players_list.copy()
    player_id = find_player_id(aux_players_list)
    player_dict = aux_players_list[player_id]
    stats_list = create_stats_list(player_dict, player_id)
    csv_path = "/Users/juandchaves/src/utn/I/prog_lab/Parcial/stats_{0}.csv".format(
        aux_players_list[player_id]["nombre"]
    )
    csv_writer(csv_path, stats_list)


# 4
def show_player_achievements() -> None:
    """
    Calls find_player_name. For every match finds the players achievements
    Prints a str with a message
    """
    aux_players_list = players_list.copy()
    player_names = find_player_name()
    if len(player_names) > 0:
        for player in aux_players_list:
            if player["nombre"] in player_names:
                achievements_str = ", ".join(player["logros"])
                message = "{0} fue: {1}".format(player["nombre"], achievements_str)
                print(message)
    else:
        print("*ERROR*")
    if len(player_names) > 0:
        for player in aux_players_list:
            if player["nombre"] in player_names:
                achievements_str = ", ".join(player["logros"])
                message = "{0} fue: {1}".format(player["nombre"], achievements_str)
                print(message)
    else:
        print("*ERROR*")


# 5


# 6
def hof_member_check() -> None:
    """
    Calls find_player_name. For every match finds if the player has "Miembro del Salon de la Fama del Baloncesto" in its "logros" list
    Prints a str with a message for every match
    """
    aux_players_list = players_list.copy()
    player_names_input = find_player_name()
    player_names = []

    match_value = "Miembro del Salon de la Fama del Baloncesto"
    if len(player_names_input) > 0:
        for player in aux_players_list:
            player_names.append(player["nombre"])
            if (
                player["nombre"] in player_names_input
                and match_value in player["logros"]
            ):
                message = "{0} fue {1}.".format(player["nombre"], match_value)
                print(message)
            elif (
                player["nombre"] in player_names_input
                and match_value not in player["logros"]
            ):
                message = "{0} no fue {1}.".format(player["nombre"], match_value)
                print(message)
    else:
        print("*ERROR*")


#  ESTE CREO QUE NO TOCA HACERLO
def value_average(players_list: list, stat: str) -> float:
    value_sum = 0.0
    for player in players_list:
        value_sum += player["estadisticas"][stat]

    average = value_sum / len(players_list)
    print("average: ", average)

    return average


# ********************************************


def float_input() -> float:
    """
    Receives the list of players
    Ask the user for a number to later check against the players_list values
    """
    users_input = input("Ingresa un número: ")
    pattern = "^\d+$"

    if re.match(pattern, users_input) != None:
        users_input_float = float(users_input)
    else:
        print("*ERROR*")

    return users_input_float


# 10, 11, 12, 15, 18
def player_above_input_by_value(stat: str):
    """
    Receives the stat to be evaluated in a string
    Prints a string with the players that are above the input number by stat
    """
    aux_players_list = players_list.copy()
    input_float = float_input()
    aux_players_above = []
    for player in aux_players_list:
        if input_float < player["estadisticas"][stat]:
            aux_players_above.append(player["nombre"])

    if aux_players_above == []:
        message = "*ERROR* No se encontraron resultados"
    else:
        players_above = ", ".join(aux_players_above)
        message = "Los jugadores con {0} por encima de {1} son: {2}".format(
            stat, str(input_float), players_above
        )

    print(message)


# 7, 8, 9, 13, 14, 17, 19
def calculate_player_with_highest_value(stat: str) -> str:
    aux_players_list = players_list.copy()

    if stat == "logros":
        highest_value_achievements = len(aux_players_list[0][stat])
    else:
        highest_value = aux_players_list[0]["estadisticas"][stat]

    player_id = 0
    highest_value_player_id = 0
    for player in aux_players_list:
        if stat != "logros":
            if highest_value < player["estadisticas"][stat]:
                highest_value = player["estadisticas"][stat]
                highest_value_player_id = player_id
        elif stat == "logros" and highest_value_achievements < len(player[stat]):
            highest_value_achievements = len(player[stat])
            highest_value_player_id = player_id
        player_id += 1
    message = "El jugador con más {0} es: {1}".format(
        stat, aux_players_list[highest_value_player_id]["nombre"]
    )

    print(message)


# 5, 16

# def player_above_average_by_value(stat: str):
# 20 -> player_above_average_by_value() "posicion" "porcentaje_tiros_de_campo"

# 23

while True:
    numeral_str = input(
        "DREAM TEAM | Parcial\nSelecciona alguna de las opciones: \n1.Lista de Jugadores y su posicion  \n2. Estadisticas por jugador  \n3. Guardar en CSV estadisticas de la opcion 2  \n4. Logros por jugador  \n5. Ranking promedio de puntos por partido  \n6. ¿Miembro del salón de la Fama del Baloncesto?  \n7. Jugador con la mayor cantidad de rebotes totales  \n8. Jugador con el mayor porcentaje de tiros de campo. \n9. Jugador con la mayor cantidad de asistencias totales. \n10. Jugadores que han promediado más puntos por partido superior a: \n11. Jugadores que han promediado más rebotes por partido superior a: \n12. Jugadores que han promediado más asistencias por partido superior a: \n13. Jugador con la mayor cantidad de robos totales. \n14. Jugador con la mayor cantidad de bloqueos totales. \n15. Jugadores que hayan tenido un porcentaje de tiros libres superior a: \n16. Promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad. \n17. Jugador con la mayor cantidad de logros obtenidos \n18. Jugadores que hayan tenido un porcentaje de tiros triples superior a: \n19. Jugador con la mayor cantidad de temporadas jugadas \n20. Jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a:  \n23. Tabla del Ranking \n0. Salir. \n"
    )

    numeral_int = int(numeral_str)

    match numeral_int:
        case 1:
            player_by_position(players_list)
        case 2:
            player_stats()
        case 3:
            player_stats_csv()
        case 4:
            show_player_achievements()
        case 5:
            # Calcular y mostrar
            pass
        case 6:
            hof_member_check()
        case 7:
            calculate_player_with_highest_value("rebotes_totales")
        case 8:
            calculate_player_with_highest_value("porcentaje_tiros_de_campo")
        case 9:
            calculate_player_with_highest_value("asistencias_totales")
        case 10:
            player_above_input_by_value("promedio_puntos_por_partido")
        case 11:
            player_above_input_by_value("promedio_rebotes_por_partido")
        case 12:
            player_above_input_by_value("promedio_asistencias_por_partido")
        case 13:
            calculate_player_with_highest_value("robos_totales")
        case 14:
            calculate_player_with_highest_value("bloqueos_totales")
        case 15:
            player_above_input_by_value("porcentaje_tiros_libres")
        case 16:
            # Calcular y mostrar
            pass
        case 17:
            calculate_player_with_highest_value("logros")
        case 18:
            player_above_input_by_value("porcentaje_tiros_triples")
        case 19:
            calculate_player_with_highest_value("temporadas")
        case 20:
            # Permitir
            pass
        case 23:
            pass
        case 0:
            print("Gracias, nos vemos!")
            break
