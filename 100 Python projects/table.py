
from prettytable import PrettyTable


table = PrettyTable()

table.add_column("Student names", ["Abdulkadir", "Duran", "Adan"])
table.add_column("Student Id", [5035190144, 5035190148, 5035190144])

print(table.align)