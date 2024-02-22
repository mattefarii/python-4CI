import requests
import time
import threading
from threading  import Thread
import multiprocessing
from queue import Queue
siti_web = [
    'https://envato.com',
    'http://amazon.com',
    'http://facebook.com',
    'http://google.com',
    'http://google.fr',
    'http://google.es',
    'http://internet.org',
    'http://gmail.com',
    'http://stackoverflow.com',
    'http://github.com',
    'http://heroku.com',
    'http://really-cool-available-domain.com',
    'http://djangoproject.com',
    'http://rubyonrails.org',
    'http://basecamp.com',
    'http://trello.com',
    'http://yiiframework.com',
    'http://shopify.com',
    'http://another-really-interesting-domain.co',
    'http://airbnb.com',
    'http://instagram.com',
    'http://snapchat.com',
    'http://youtube.com',
    'http://baidu.com',
    'http://yahoo.com',
    'http://live.com',
    'http://linkedin.com',
    'http://yandex.ru',
    'http://netflix.com',
    'http://wordpress.com',
    'http://bing.com',
]

NUM_WORKERS=4

def effettua_request(url):
    try:
        response = requests.get(url)  # Effettua la richiesta GET all'URL specificato
        response.raise_for_status()  # Solleva un'eccezione in caso di errore nella risposta
        #print("Risposta:", response.text)  # Stampa il contenuto della risposta
        print("OK ",url)
    except requests.exceptions.RequestException as e:
        print("Errore durante la richiesta:", e)

def worker(queue):
    while not queue.empty():
        a=queue.get()
        effettua_request(a)
        queue.task_done()

if __name__=="__main__":
    start_time=time.time()
    for url in  siti_web:
        effettua_request(url)
    end_time=time.time()
    print("Tempo seriale:",end_time-start_time)    
    
    queue=Queue()
    start_time=time.time()
    for url in (siti_web):
        queue.put(url)
    process=[Thread(target=worker,args=(queue,)) for _ in range(4)]
    [processes.start() for processes in process]

    #[processes.join() for processes in process]
    queue.join()
    end_time=time.time()
    print("Tempo utilizzando i thread:",end_time-start_time)


