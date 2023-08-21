import openai
import random


openai.api_key = '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'

def inicio():
    answer = ['serpiente','cocodrilo','hipopotamo','hiena','elefante','leon','tigre','mono','jirafa']
    random_answer = random.choice(answer)
    promt = 'Adivina el animal que estoy pensando, es un animal de la selva'
    
    return promt, random_answer

def comparision(user_option, random_option):
    if user_option == random_option:
        return True
    return False

def give_property(animal):
  response = openai.Completion.create(
                                      engine = 'text-davinci-003',
                                      prompt = f'Dame una caracteristica del tipo animal'+ animal + ',pero jamas digas el nombre del animal' + animal,
                                      max_tokens = 100,
                                      top_p = 1,
                                      frequency_penalty = 0.5,
                                      presence_penalty = 0
  )
  return response.choices[0].text

def run():
    prom,answer = inicio()
    print(prom)
    vidas = 5
    while True:
        
        user_option = input('Que animal crees que estoy pensando => ')
        if comparision(user_option,answer):
            print(f'GANASTE!!, La respuesta era {answer}')
            break

        elif not comparision(user_option,answer):
            print('Incorrecto, intenta de nuevo')
            print(give_property(answer))
            vidas -= 1

        if vidas == 0:
            print('PERDISTE, HASTA LA PROXIMA')
            print(f'El animal correcto era {answer}')
            break


run()