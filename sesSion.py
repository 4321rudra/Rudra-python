class WorkoutSession :
    def __init__(self,day,muscle_group):
        self.completed_sets=0
        self.day=day
        self.muscle_group=muscle_group
    def announce_session(self):
        print(f"This {self.muscle_group} session is scheduled for {self.day}.")
    def perform_set(self):
        self.completed_sets+=1
        print(f"Set completed! Total sets done for this session: {self.completed_sets} ")
class CardioSession(WorkoutSession):
    def __init__(self,day, muscle_group,machine_type):
        super().__init__(day,muscle_group)
        self.machine=machine_type
    def change_machine(self,new_machine):
        self.machine=new_machine
        print(f"Switched equipment to {new_machine}")
session1=WorkoutSession(day="monday",muscle_group="Chest and Triceps")
session2=WorkoutSession(day="Tuesday",muscle_group="Back and Biceps")
# WorkoutSession.announce_session(session1)
session1.perform_set()
session1.perform_set()
session1.perform_set()
cardio_run = CardioSession(day="Friday", muscle_group="Cardio", machine_type="Treadmill")
session1.announce_session()
session2.announce_session()
print(session1.completed_sets)
cardio_run.announce_session()
cardio_run.change_machine("Rowing Machine")
cardio_run.announce_session()


