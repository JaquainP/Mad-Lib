mad_libs = [
('DONTINPUT', 'It was a '),
('INPUT', 'adjective'),
('DONTINPUT', ', cold November day. I woke up to the '),
('INPUT', 'adjective'),
('DONTINPUT', ' smell of '),
('INPUT', 'type of bird'),
('DONTINPUT', ' roasting in the '),
('INPUT', 'room in a house'),
('DONTINPUT', ' downstairs'),
]

# Retrieve user input to mad_lib
def fill_in_story(part_of_speech: str):
    print("Fill in next word, must be a {}".format(part_of_speech))
    return input()

# Build story based on user input
# Run through each mad line of madlib
# determine if user input needed or not
def write_madlib(mad_lib: list):
    story = ""
    for lib in mad_lib:
        if lib[0] is 'INPUT':
            story += fill_in_story(lib[1])
        else:
            story += lib[1]
            print(lib[1])
    return story

print("""Your Story is:
{}""".format(write_madlib(mad_libs)))
