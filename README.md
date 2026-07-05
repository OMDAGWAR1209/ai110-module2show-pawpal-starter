# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Features

- **Task representation**: each task has a description, duration, priority (low/medium/high), and completion status.
- **Pet & Owner modeling**: an Owner can manage multiple Pets, each with their own task list and preferences.
- **Smart daily planning**: `Planner.build_plan()` selects tasks that fit within a given time budget, prioritizing high-priority tasks first.
- **Explainable scheduling**: `Planner.explain_plan()` generates a plain-English explanation of why each task was included in the plan.
- **Interactive UI**: a Streamlit app lets you add pets, add tasks, and generate/view the explained daily plan in the browser.
- **Automated tests**: 5 pytest tests cover task completion, task counting, priority-based ordering, time-budget filtering, and empty-plan messaging.## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. Enter an owner name, pet name, and species in the sidebar form.
2. Add a few care tasks (title, duration in minutes, and priority: low/medium/high) using the "Add task" button — they'll appear in the "Current tasks" table.
3. Scroll to "Build Schedule" and set how much time is available today.
4. Click "Generate schedule" to see the selected tasks, sorted by priority, that fit within your time budget.
5. Read the "Why this plan" explanation to see the reasoning behind each included task.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
## Sample Output

```Today's Plan:
  - Morning walk (20 min, high)
  - Breakfast (10 min, high)
  - Playtime (30 min, low)

Why this plan:
- 'Morning walk' was included because it's high priority and takes 20 min.
- 'Breakfast' was included because it's high priority and takes 10 min.
- 'Playtime' was included because it's low priority and takes 30 min.```
```## Testing PawPal+

Run the test suite with:

​```
python -m pytest -v
​```

​```
tests/test_pawpal.py::test_task_completion_changes_status PASSED [20%]
tests/test_pawpal.py::test_adding_task_increases_pet_task_count PASSED [40%]
tests/test_pawpal.py::test_plan_prioritizes_high_priority_tasks_first PASSED [60%]
tests/test_pawpal.py::test_plan_skips_tasks_that_dont_fit_in_time PASSED [80%]
tests/test_pawpal.py::test_explain_plan_returns_message_for_empty_plan PASSED [100%]
5 passed in 0.04s
​```

**Confidence Level:** 4/5 stars — core scheduling, prioritization, and edge cases are covered.```