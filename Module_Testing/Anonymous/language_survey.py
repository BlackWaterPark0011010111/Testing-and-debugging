from survey import AnonymousSurvey

question='What language did u first learn to speak'
my_survey=AnonymousSurvey(question)

my_survey.show_question()
print('Enter a q for quit')
while True:
    response=input('Language: ')
    if response=='q':
        break
    my_survey.store_response(response)

print('\nThank u all who participated')
my_survey.show_results()