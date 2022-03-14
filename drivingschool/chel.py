from drivingschool import models as m

d = dict([(name, cls) for name, cls in m.__dict__.items() if isinstance(cls, type)])
for k, v in d.items():
    if k == 'AbstractUser' or k == 'userr':
        continue
    try:
        v._meta.get_fields()
    except:
        continue
    print(f'''
    <table>
        <tr>
            <th colspan="5">{k}</th>
        </tr>
        <tr>
            <th>Key</th>
            <th>Column Name</th>
            <th>Data Type</th>
            <th>Allow Nulls</th>
            <th>Notes</th>
        </tr>
    ''')
    for field in v._meta.get_fields():
        print('<tr>')
        try:
            if field.primary_key:
                print(f'<td>PK</td>')
            else:
                print('<td></td>')
        except:
            print('<td>FK</td>')
        print(f'<td>{field.name}</td>')
        print(f'<td>{field.get_internal_type()}')
        print(f'<td>{field.null}</td>')
        print(f'<td></td>')
        print('</tr>')
    print('</table>')