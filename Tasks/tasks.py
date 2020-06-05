## IMPORT REQUIRED MODULES
import os, time  
from app import app
from celery.utils.log import get_task_logger

## DEFINE CELERY LOGGING
logger = get_task_logger(__name__)

## DEFINE DUMMY DEMO CELERY TASKS
@app.task(bind=True, name='tasks.parent')
def parent(self):
    ## DEBUG LOGGING
    logger.info("Parent Task Called ...")

    ## CALL SUBTASKS (THIS PASSES THE RESULT FROM THE PREVIOUS TASK TO THE NEXT TASK)
    #taskchain = task1.s() | task2.s() | task3.s()
    #taskchain()

    ## CALL SUBTASKS (ONE AFTER THE OTHER)
    taskchain = task1.si() | task2.si() | task3.si()
    taskchain()
    
    ## DEBUG LOGGING
    logger.info("Parent Task Completed !!")

@app.task(bind=True, name='tasks.task1')
def task1(self):
    ## DEBUG
    print("Starting Task #1 ...", flush=True)
    logger.info("Starting Task #1 ...")

    ## Pretend to Do Work
    Counter = 0

    while (Counter <= 60):
        ## Update Status
        self.update_state(state='PROGRESS', 
        meta={
            'done': Counter, 
            'total': 60
        })

        ## Update Counter
        Counter += 1

        ## Wait 1 Second (Pretend Work)
        time.sleep(1)

    ## DEBUG
    print("Task #1 Complete!")

@app.task(bind=True, name='tasks.task2')
def task2(self):
    ## DEBUG
    print("Starting Task #2 ...", flush=True)
    
    ## Pretend to Do Work
    Counter = 0

    while (Counter <= 60):
        ## Update Status
        self.update_state(state='PROGRESS', 
        meta={
            'done': Counter, 
            'total': 60
        })

        ## Update Counter
        Counter += 1

        ## Wait 1 Second (Pretend Work)
        time.sleep(1)

    ## DEBUG
    print("Task #2 Complete!")

@app.task(bind=True, name='tasks.task3')
def task3(self):
    ## DEBUG
    print("Starting Task #3 ...", flush=True)
    
    ## Pretend to Do Work
    Counter = 0

    while (Counter <= 60):
        ## Update Status
        self.update_state(state='PROGRESS', 
        meta={
            'done': Counter, 
            'total': 60
        })

        ## Update Counter
        Counter += 1

        ## Wait 1 Second (Pretend Work)
        time.sleep(1)

    ## DEBUG
    print("Task #3 Complete!")