---
marp: false
---

# Chain of responsiblity
Sequence of handlers processing an event one after another

## Motivation
- Unethical behaviour by an employee; who takes the blame?
    - Employee, L1
    - Manager, L2
    - CEO, L3

- You click a graphical element on a form 
    - Button handles it, stops further processing
    - Underlying group box
    - Underlying window

- CCG computer game
    - Creature has attack and defense values
    - Those can be boosted by other cards

## Defination
A chain of components who all get a chance to process a command or query, optionally having default processing implementation and ability to terminate the processing chain.