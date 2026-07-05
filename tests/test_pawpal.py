import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pawpal_system import Owner, Pet, Task, Priority, Planner


def test_task_completion_changes_status():
    task = Task("Walk", 20, Priority.NORMAL)
    assert task.completed is False
    task.completed = True
    assert task.completed is True


def test_adding_task_increases_pet_task_count():
    pet = Pet(name="Rex", species="Dog")
    assert len(pet.tasks) == 0
    pet.add_task(Task("Feed", 10, Priority.NORMAL))
    assert len(pet.tasks) == 1


def test_plan_prioritizes_high_priority_tasks_first():
    owner = Owner(name="Test Owner")
    pet = Pet(name="Rex", species="Dog")
    owner.add_pet(pet)
    pet.add_task(Task("Low task", 10, Priority.LOW))
    pet.add_task(Task("High task", 10, Priority.HIGH))
    planner = Planner(owner)
    plan = planner.build_plan(time_available_minutes=100)
    assert plan[0].description == "High task"


def test_plan_skips_tasks_that_dont_fit_in_time():
    owner = Owner(name="Test Owner")
    pet = Pet(name="Rex", species="Dog")
    owner.add_pet(pet)
    pet.add_task(Task("Big task", 90, Priority.HIGH))
    pet.add_task(Task("Small task", 10, Priority.LOW))
    planner = Planner(owner)
    plan = planner.build_plan(time_available_minutes=50)
    descriptions = [t.description for t in plan]
    assert "Big task" not in descriptions
    assert "Small task" in descriptions


def test_explain_plan_returns_message_for_empty_plan():
    owner = Owner(name="Test Owner")
    planner = Planner(owner)
    result = planner.explain_plan([])
    assert "No tasks" in result