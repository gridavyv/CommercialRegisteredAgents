# with open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/agents.txt") as f, \
#      open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/filtered_agents.txt", 'w') as out_f:
#     lines = f.readlines()
#     count = 0
#     for i in range(len(lines)-2):
#         if lines[i] == "\n" and lines[i+2] == "Physical Address\n":
#             out_f.write(lines[i+1])
#             count += 1
# print(count)


# with open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/agents.txt") as f, \
#      open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/filtered_phones.txt", 'w') as out_f:
#     lines = f.readlines()
#     count = 0
#     for line in lines:
#         if "Phone:" in line:
#             out_f.write(line)
#             count += 1
# print(count)


# with open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/agents.txt") as f, \
#      open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/filtered_emails.txt", 'w') as out_f:
#     lines = f.readlines()
#     count = 0
#     for line in lines:
#         if "Email:" in line:
#             out_f.write(line)
#             count += 1
# print(count)

# with open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/filtered_phones.txt") as f, \
#      open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/filtered_phones_v1.txt", 'w') as out_f:
#     lines = f.readlines()
#     for line in lines:
#         part_1 = line.split(" ")[1].strip("\n")
#         part_2 = line.split(" ")[2].strip("\n")
#         out_f.write(part_1 + " " + part_2 + "\n")


with open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/filtered_emails.txt") as f, \
     open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/filtered_emails_v1.txt", 'w') as out_f:
    lines = f.readlines()
    var = ""
    for line in lines:
        line_list = line.split(" ")
        if len(line_list) == 1:
            var = "no_email"
        else:
            var = line_list[-1].strip("/n")
        out_f.write(var)
