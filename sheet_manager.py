from datetime import datetime
import gspread as gs
import pandas as pd


def load_data(key: str):
    gservaccount = gs.service_account(filename='service_account.json')
    sheet_file = gservaccount.open_by_key(key)
    worksheet = sheet_file.get_worksheet_by_id(0)

    return pd.DataFrame(
        worksheet.get_all_records(),
        columns= worksheet.get_all_values()[0]
    )


def push_data(key: str, data: pd.DataFrame):

    old_data = load_data(key)
    gservaccount = gs.service_account(filename='service_account.json')
    sheet_file = gservaccount.open_by_key(key)
    worksheet = sheet_file.get_worksheet_by_id(0)

    concat_data = pd.concat([old_data, data], ignore_index=True).fillna('')
    worksheet.update(
        [concat_data.columns.values.tolist()] + concat_data.values.tolist()
    )


if __name__ == '__main__':
    ex_key = ''

    # Test Pull
    sample = load_data(ex_key)
    sample.head()

    # Test Push
    new_data = pd.DataFrame({
        'date_created':[datetime.strftime(datetime.now(), '%Y-%M-%dT%H:%M:%S.%f')],
        'email':['example_email@gmail.com'],
        'osu_username':['osuer'],
        'discord_username':['discorder'],
        'days_attending':['Day 1, Day 3'],
        'has_consented':True
    })
    push_data(ex_key, new_data)

