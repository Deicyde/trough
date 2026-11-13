---
declaration: theorem
origin: cited
lean: Green77.green_77
statement: formalized
---

# Ben Green's Open Problem 77

> *Reference:*
> - [Ben Green's Open Problem 77](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.77)

*Quoted from [FormalConjectures/GreensOpenProblems/77.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/77.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Green77.green_77`

Open: stated without proof.

> Given $n$ points in the unit disc, must there be a triangle of area at most $n^{-2+o(1)}$
> determined by them?

```lean
theorem green_77 :
    ∃ (o : ℕ → ℝ), Tendsto o atTop (𝓝 0) ∧
      α ≪ fun n ↦ n ^ (-2 + o n)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/77.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/77.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/77.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/77.lean)
- [Ben Green's Open Problem 77](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.77)
