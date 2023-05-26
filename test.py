import json

json_path = "/Users/juandchaves/src/utn/I/prog_lab/Parcial/dt.json"


def json_reader(path: str) -> list:
    with open(path, "r") as file:
        dream_team_dict = json.load(file)

    return dream_team_dict


players = json_reader(json_path)
players_list = players["jugadores"]


csv_path = "/Users/juandchaves/src/utn/I/prog_lab/Parcial/stats.csv"


def csv_writer(path: str, stats: str):
    estadisticas = stats[0]["estadisticas"]
    headers_list = ["nombre"]
    values_list = ["Michael Jordan"]
    with open(path, "w+") as file:
        for key, value in estadisticas.items():
            headers_list.append(key)
            values_list.append(str(value))
        headers_str = ", ".join(headers_list)
        values_str = ", ".join(values_list)
        file.write("{0}\n".format(headers_str))
        file.write("{0},\n".format(values_str))

    print(estadisticas)
    # print(headers_str)


csv_writer(csv_path, players_list)
