import datetime

import pandas as pd


def init_excel(buttons: dict):
    # Создание DataFrame из словаря кнопок
    df_list = []
    days = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница'}
    times = {1: '9:30 - 11:05', 2: '11:20 - 12:55', 3: '13:10 - 14:45', 4: '15:25 - 17:00', 5: '17:15 - 18:50'}

    for i in range(1, 26):
        day = days[(i - 1) // 5 + 1]
        time = times[(i - 1) % 5 + 1]
        df_list.append(
            pd.DataFrame({'День': [day], 'Время': [time], 'Верхняя неделя': [buttons[f'pushButton_{i}']],
                          'Нижняя неделя': [buttons[f'pushButton_{i + 25}']]}))

    df = pd.concat(df_list, ignore_index=True)

    update_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    df = pd.concat(
        [df, pd.DataFrame([['', '', '', '']], columns=['День', 'Время', 'Верхняя неделя', 'Нижняя неделя']),
         pd.DataFrame([['Последнее обновление', update_time, '', '']],
                      columns=['День', 'Время', 'Верхняя неделя', 'Нижняя неделя']),
         pd.DataFrame([['', f'{buttons["corner_button"]}', '', '']],
                      columns=['День', 'Время', 'Верхняя неделя', 'Нижняя неделя'])],
        ignore_index=True)

    # Сохранение DataFrame в файл Excel
    with pd.ExcelWriter('Расписание.xlsx') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

        # Объединение ячеек с одинаковыми днями
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})

        start_row = 1
        for i in range(2, len(df) + 1):
            if df.iloc[i - 1, 0] != df.iloc[i - 2, 0]:
                worksheet.merge_range(start_row, 0, i - 1, 0, df.iloc[i - 2, 0], format)
                start_row = i
        worksheet.merge_range(start_row, 0, len(df), 0, df.iloc[len(df) - 1, 0], format)


def read_excel_buttons(file_path='Расписание.xlsx'):
    try:
        df = pd.read_excel(file_path, dtype=str)
    except FileNotFoundError:
        return None

    buttons_dict = {}
    df.fillna('', inplace=True)
    print(df)
    for index, row in df.iterrows():
        upper_week_button = row['Верхняя неделя']
        lower_week_button = row['Нижняя неделя']
        time_button = row['Время']

        buttons_dict[f'pushButton_{index + 1}'] = upper_week_button
        buttons_dict[f'pushButton_{index + 26}'] = lower_week_button
        buttons_dict[f'pushButton_{index + 51}'] = time_button

        if int(index) >= 24:
            break

    last_update = df.iloc[26, 1]
    last_update = datetime.datetime.strptime(last_update, '%d.%m.%Y %H:%M:%S')
    week = int(''.join(filter(str.isdigit, df.iloc[27, 1])))
    now = datetime.datetime.now()

    # Получаем номер недели для last_update и текущей даты
    week_number_last_update = last_update.isocalendar()[1]
    week_number_now = now.isocalendar()[1]

    # Если last_update был на прошлой неделе, прибавляем 1 к числу
    if week_number_last_update < week_number_now:
        week += 1

    buttons_dict['corner_button'] = f'Неделя {week}'
    return buttons_dict
