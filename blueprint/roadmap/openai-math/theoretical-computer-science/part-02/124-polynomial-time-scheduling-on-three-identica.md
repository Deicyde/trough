---
declaration: section
origin: cited
lean: OAI.ThreeMachine.main_theorem
statement: formalized
proof: formalized
---

# 124. Polynomial-time scheduling on three identical machines

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the three-processor unit-job scheduling problem of Garey and Johnson: a deterministic polynomial-time algorithm minimizes makespan for nonpreemptive unit-length jobs with arbitrary precedence constraints on three identical parallel machines. For an explicitly given precedence graph, it decides deadline feasibility exactly and constructs a feasible schedule.

## A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling

We give a uniform deterministic polynomial-time algorithm for scheduling unit-length jobs with arbitrary precedence constraints on three identical parallel machines. The algorithm constructs a schedule of minimum makespan and decides exactly whether all jobs can finish by a specified deadline. The proof reorganizes feasible schedules into intervals whose job sets have descriptions of bounded size. A dynamic program searches a family containing polynomially many such descriptions. Global boundary conditions and simplification of inherited information keep the descriptions bounded throughout the decomposition.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization gives a deterministic polynomial-time algorithm for scheduling nonempty collections of unit-length jobs with arbitrary acyclic precedence constraints on three identical parallel machines. It constructs a schedule of minimum makespan and decides exactly whether a valid specified deadline can be met. The algorithm is one fixed finite machine, and its running time is bounded by a polynomial in the binary input length.

## Lean: Optimal three-machine unit-job scheduling

```lean
theorem main_theorem : ReleaseTheorem
```

Stated in [ThreeMachine.lean, line 95](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ThreeMachine.lean#L95). Proved in [lean/OAI/Computability/Scheduling/Main.lean, line 59](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/Scheduling/Main.lean#L59).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/124.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/124.md)
