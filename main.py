calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return(len(string), string.upper(), string.lower())
print(string_info('Capybara'))
print(string_info('Armageddon'))

def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string.lower():
            return True
    return False

print(is_contains('Urban',['BaNaN', 'urBAN',]))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
count_calls()