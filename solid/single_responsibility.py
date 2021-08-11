'''
Here we have a journal class, where we can:
    1. Add a journal entry.
    2. Remove a journal entry.
    3. Print all the journal entries.

So far we haven't broken the Single Responsiblity Principle.

Now we are going to break the single reponsibility principle.
We will give it a method to save itself, which will save itself in a file.

How does save break the single responsibility principle?
Well, it now has two responsibilities:
1. Editing journal
2. Persistence - Saving, Loading Journals

If we consider other types such as emails, notes, etc.
All of them might need their own save, load, etc, methods.

If we ever need to change any of these methods then we need to
go to every single class and make the changes.

So persistence has to be a separate class.

Anti-pattern
============
God Object: Having too many functionalities within a single class resulting
            in a massive class.

Single Responsibility Principle prevents us from creating God Objects.
'''


class Journal:
    
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
    
    def remove_entry(self, pos):
        del self.entries[pos-1]
    
    def __str__(self):
        return '\n'.join(self.entries)

    # the method that breaks single responsibility
    # def save(self, filename):
    #     with open(filename, 'w') as fw:
    #         fw.write(str(journal))


class PersistenceManager:

    @staticmethod
    def save(journal, filename):
        with open(filename, 'w') as fw:
            fw.write(str(journal))


if __name__ == "__main__":
    journal = Journal()
    journal.add_entry("Journal 1")
    journal.add_entry("Journal 2")
    journal.add_entry("Journal 3")
    journal.add_entry("Journal 4")
    print(journal)
    # journal.save('./journal') # Bad practice
    PersistenceManager.save(journal, './journal')
    journal.remove_entry(3)
    print('Journal after removal')
    print(journal)
    # journal.save('./journal') # Bad practice
    PersistenceManager.save(journal, './journal')
