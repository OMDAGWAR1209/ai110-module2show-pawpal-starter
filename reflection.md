# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
I designed 4 classes: Task, Pet, Owner, and Planner. Task stores description, time, priority, duration, and completion status. Pet stores a name, species, and list of tasks. Owner stores a name and list of pets. Planner builds a daily plan by looking at time available and task priorities, and explains why it picked that plan.
**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
Yes — I added a duration field to Task that wasn't in my first draft, since the Planner needs to know how long each task takes to fit it into the owner's available time.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
The scheduler considers time available, task priority (high/normal/low), and owner preferences. Priority mattered most — high-priority tasks (like meds) get placed first, then lower-priority ones fill remaining time.
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used AI to brainstorm the UML class diagram, generate Python class skeletons from that diagram, and help debug the scheduling logic. The most helpful prompts were ones where I described the exact classes and asked it to suggest methods, and ones where I pasted an error message directly.
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**
I used AI to brainstorm the UML class diagram, generate Python class skeletons from that diagram, and help debug the scheduling logic. The most helpful prompts were ones where I described the exact classes and asked it to suggest methods, and ones where I pasted an error message directly.
- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**
I tested that tasks sort correctly by time, that marking a recurring task complete creates the next occurrence, and that the scheduler flags two tasks scheduled at the same time. These were important because they're the core "smart" behaviors of the app.
- What behaviors did you test?
- Why were these tests important?

**b. Confidence**
I'm fairly confident (4/5) the scheduler works correctly for the core cases. If I had more time I'd test edge cases like a pet with zero tasks, and tasks that span midnight.
- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**
I'm most satisfied with how cleanly the Planner class separates scheduling logic from the Task/Pet/Owner data classes — it made testing and debugging much easier.
- What part of this project are you most satisfied with?

**b. What you would improve**
With another iteration, I'd add support for custom recurrence (e.g. specific weekdays) and a smarter conflict check that looks at overlapping durations, not just exact time matches.
- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**
I learned that AI is great for generating boilerplate and catching edge cases, but I still have to make the actual architecture decisions myself — like where logic should live and which tradeoffs make sense for this app.
- What is one important thing you learned about designing systems or working with AI on this project?
