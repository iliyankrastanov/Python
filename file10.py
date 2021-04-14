# %%
connection = dict(
    timeout=300,
    host='localhost',
    is_admin=True,
    port=3306
)

connection
# %%
connection['port']
# %%
user = {
    'first_name':'Anna',
    'last_name': 'Smith',
    'age':32,
    'active': True,
    'skills': ['C++','Python']
}
# %%
user['active']
# %%
user['skills']
# %%
user.keys()
# %%
user.values()
# %%
user.items()
# %%
user['phone']

# %%
'phone' in user
# %%
user.get('phone', '000-00-00')
# %%