from pawpal_system import Owner, Pet, Task, Priority, Planner

owner = Owner(name="Riya")
buddy = Pet(name="Buddy", species="Dog")
owner.add_pet(buddy)

buddy.add_task(Task("Morning walk", 20, Priority.HIGH))
buddy.add_task(Task("Breakfast", 10, Priority.HIGH))
buddy.add_task(Task("Playtime", 30, Priority.LOW))
buddy.add_task(Task("Grooming", 45, Priority.NORMAL))

planner = Planner(owner)
plan = planner.build_plan(time_available_minutes=60)

print("Today's Plan:")
for task in plan:
    print(f"  - {task.description} ({task.duration_minutes} min, {task.priority.value})")

print("\nWhy this plan:")
print(planner.explain_plan(plan))