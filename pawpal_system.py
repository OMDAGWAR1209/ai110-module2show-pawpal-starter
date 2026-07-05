from dataclasses import dataclass, field
from typing import List
from enum import Enum


class Priority(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"


@dataclass
class Task:
    description: str
    duration_minutes: int
    priority: Priority = Priority.NORMAL
    completed: bool = False


@dataclass
class Pet:
    name: str
    species: str
    preferences: str = ""
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks


class Planner:
    def __init__(self, owner: Owner):
        self.owner = owner

    def build_plan(self, time_available_minutes: int):
        """Picks tasks that fit in the available time, highest priority first."""
        tasks = sorted(
            self.owner.get_all_tasks(),
            key=lambda t: {"high": 0, "normal": 1, "low": 2}[t.priority.value],
        )
        plan = []
        remaining = time_available_minutes
        for task in tasks:
            if task.duration_minutes <= remaining and not task.completed:
                plan.append(task)
                remaining -= task.duration_minutes
        return plan

    def explain_plan(self, plan: List[Task]) -> str:
        """Generates a plain-English explanation of why each task was chosen."""
        if not plan:
            return "No tasks fit in the available time."
        lines = []
        for task in plan:
            lines.append(
                f"- '{task.description}' was included because it's "
                f"{task.priority.value} priority and takes {task.duration_minutes} min."
            )
        return "\n".join(lines)