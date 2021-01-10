import pandas as pd


def format_data(csv_name: str, csv_output_name: str):
    df = pd.read_csv(csv_name)
    df['price'] = ["".join(price.split(" ")) for price in df['price']]
    df['price'] = [price[:-2] for price in df['price']]
    df['area'] = [area[:-3] for area in df['area']]

    for i in range(len(df['level'])):
        if df['level'][i] == "parter":
            df['level'][i] = 0
        df['area'][i] = df['area'][i].replace(",", ".")
    df['area'] = pd.to_numeric(df['area'])
    locations = {
        'Bieńczyce': 0,
        'Bieżanów-Prokocim': 1,
        'Bronowice': 2,
        'Dębniki': 3,
        'Grzegórzki': 4,
        'Krowodrza': 5,
        'Łagiewniki-Borek Fałęcki': 6,
        'Mistrzejowice': 7,
        'Nowa Huta': 8,
        'Podgórze': 9,
        'Podgórze Duchackie': 10,
        'Prądnik Biały': 11,
        'Prądnik Czerwony': 12,
        'Śródmieście': 13,
        'Stare Miasto': 14,
        'Swoszowice': 15,
        'Wzgórza Krzesławickie': 16,
        'Zwierzyniec': 17,
    }

    states = {
        'do remontu': 0,
        'do wykończenia': 1,
        'do zamieszkania': 2,
    }

    for i in range(len(df['location'])):
        df['location'][i] = match_feature(locations, df['location'][i])
    for i in range(len(df['state'])):
        df['state'][i] = match_feature(states, df['state'][i])

    df.to_csv(f"{csv_output_name}", index=False)


def match_feature(match_dict: dict, feature_val):
    for key, val in match_dict.items():
        if key in feature_val:
            return val
    return -1
