import docx
from drivingschool.models import Group, Weekday
from django.conf import settings

def gen_report():
    doc = docx.Document()
    doc.add_heading('Отчет о расписании теоретических занятий', 0)

    for group in Group.objects.all():
        doc.add_paragraph(group.name)
        table = doc.add_table(rows=8, cols=3)
        table.style = 'Table Grid'

        table.cell(0, 0).text = 'День недели'
        table.cell(0, 1).text = 'Время'
        table.cell(0, 2).text = 'Преподаватели'

        for i, weekday in enumerate(Weekday.choices, start=1):
            table.cell(i, 0).text = str(weekday[1])
            table.cell(i, 1).text = '---'
            table.cell(i, 2).text = '---'

        for schedule in group.scheduletheory_set.all():
            row = schedule.weekday + 1
            table.cell(row, 0).text = schedule.get_weekday_display()
            table.cell(row, 1).text = schedule.get_position_display()
            table.cell(row, 2).text = schedule.substitute_tutor.user.get_short_name() if schedule.substitute_tutor else group.tutor.user.get_short_name()

    doc.save(settings.BASE_DIR / 'table.docx')