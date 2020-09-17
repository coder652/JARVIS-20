from pyttsx3 import speak
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak('are you ready for the trivia')
ans = input('are you ready (yes/no)')
score = 0
total_q = 6 

if ans.lower () == 'yes':
    speak('What is the best programing language')
    ans = input('1. What is the best programing language? ')
    if ans.lower() == 'python':
        score +=1
        speak('Correct answer')
        print('python')
        speak('moving to next question')
        print('moving to next question') 
    else:
        speak('Incorrect answer ,The correct answer is python')
        print('Incorrect answer ,The correct answer is python')
        speak('moving to next question')
        print('moving to next question') 

    speak('what is your favorit thing')
    ans = input('2. what is your favorit thing? ')
    if ans.lower() == 'coding':
        score +=1
        speak('Correct answer')
        print('coding')
        speak('moving to next question')
        print('moving to next question') 
    else:
        speak('Incorrect answer ,The correct answer is coding')
        print('Incorrect answer ,The correct answer is coding')
        speak('moving to next question')
        print('moving to next question')

    speak('what is your favorit pc')
    ans = input('3. what is your favorit pc ? ')       
    if ans.lower() == 'linux':
        score +=1
        speak('Correct answer')
        print('linux')
        speak('moving to next question')
        print('moving to next question') 

    else:
        speak('Incorrect answer ,The correct answer is linux')
        print('Incorrect answer ,The correct answer is linux')
        speak('moving to next question')
        print('moving to next question') 

    speak('what is your favorit subject')
    ans = input('4. what is your favrouit subject? ')
    if ans.lower() == 'science':
        score +=1
        speak('Correct answer')
        print('Correct answer')
        speak('moving to next question')
        print('moving to next question') 
    else:
        speak('Incorrect answer ,The correct answer is science')
        print('Incorrect answer ,The correct answer is science')
        speak('moving to next question')
        print('moving to next question') 

    speak('who is your personal assistant')
    ans = input('5. who is your personal assistant? ')
    if ans.lower() == 'jarvis':
        score +=1
        speak('Correct answer')
        print('jarvis')
        speak('moving to next question')
        print('moving to next question') 
    else:
        speak('Incorrect answer ,The correct answer is jarvis')
        print('Incorrect answer ,The correct answer is jarvis')
        speak('moving to next question')
        print('moving to next question') 

    speak('what pc you use ') 
    ans = input('6. what pc you use? ')
    if ans.lower() == 'hp':
        score +=1
        speak('Correct answer')
        print('hp')
        speak('Sir you have completed the trivia check ypur score Sir.')
        print('Sir you have completed the trivia check ypur score Sir.')

        speak('your marks is')

        print(" thank you for solving" ,score ,"question correct")
        mark = (score/total_q) * 100
        print('mark:' ,mark)

    else:
        speak('Incorrect answer ,The correct answer is hp')
        print('Incorrect answer ,The correct answer is hp')
        speak('Sir you have completed the trivia check ypur score Sir.')
        print('Sir you have completed the trivia check ypur score Sir.')
        print(" thank you for solving " ,score ,"question correct")
        mark = (score/total_q) * 100
        print('mark:' ,mark)

if ans.lower () == 'no':
    speak('ok good bye')
    print('ok good bye')
    print('sorry no marks recorded')
