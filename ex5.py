# Problem statement: Implement a group_by_owners function that:
    # 1)Accepts a dictionary containing the file owner name for each file name.
    # 2) Returns a dictionary containing a list of file names for each owner name, in any order.


class FileOwners:

    @staticmethod

    def group_by_owners(files):
        owners=set()
        ownerDict={}

        for i, d in files.items():
            #fill set names of owners
            owners.add(d)
        for m in owners:
            ownerDict[m]=[]
            for i, d in files.items():
                #fill out new dictionary list of file names
                if d==m:
                    ownerDict[m].append(i)
        return ownerDict;



files = {'Input.txt': 'Randy','Code.py': 'Stan','Output.txt': 'Randy'}

print(FileOwners.group_by_owners(files))