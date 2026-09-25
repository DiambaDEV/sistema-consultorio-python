from datetime import datetime

from datetime import datetime, date

def formatar_data(data):
    if isinstance(data, str):
        data = datetime.strptime(data, "%Y-%m-%d")
    return data.strftime("%d/%m/%Y")