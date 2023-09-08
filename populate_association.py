
# import os
# import sys

# # Get the absolute path to the root folder
# root_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


# # Add root foldet to python path
# sys.path.append(root_folder_path)


# from database.config import session
# from models.tag import association_table

# # Get the absolute path to the root folder
# root_folder_path = os.path.abspath("NOTE_APP")

# # Get the Note and Tag to associate
# note_id = 4
# tag_id = 3

# # check if the association already exists
# existing_association = session.query(association_table).filter_by(note_id=note_id, tag_id=tag_id).first()
# if existing_association:
#     print("Association already exists.")
# else:
#     # create a new association
#     new_association = association_table.insert().values(note_id=note_id, tag_id=tag_id)

#     # use context manager to handle the session
#     with session.begin():
#         session.execute(new_association)


