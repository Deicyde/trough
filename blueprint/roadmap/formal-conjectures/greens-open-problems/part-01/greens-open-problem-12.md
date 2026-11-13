---
declaration: theorem
origin: cited
lean: Green12.green_12
statement: formalized
---

# Green's Open Problem 12

> References:
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.12)

*Quoted from [FormalConjectures/GreensOpenProblems/12.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/12.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Green12.green_12`

Open: stated without proof.

> Let $G$ be an abelian group of size $N$, and suppose that $A \subset G$ has density $\alpha$.
> Are there at least $\alpha^{15} N^{10}$ tuples $(x_1, \dots, x_5, y_1, \dots, y_5) \in G^{10}$
> such that $x_i + y_j \in A$ whenever $j \in \{i, i+1, i+2\}$?
>
> Note: We interpret indices modulo 5.

```lean
theorem green_12 :
    ∀ {G : Type*} [AddCommGroup G] [Fintype G] [DecidableEq G],
    ∀ (A : Finset G),
    let N := Fintype.card G
    let α := (A.card : ℝ) / N
    let valid_tuples : Finset ((Fin 5 → G) × (Fin 5 → G)) := Finset.univ.filter (fun t =>
      ∀ i : Fin 5, ∀ j ∈ ({i, i + 1, i + 2} : Finset (Fin 5)), t.1 i + t.2 j ∈ A)
    (valid_tuples.card : ℝ) ≥ α ^ 15 * (N : ℝ) ^ 10
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/12.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/12.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/12.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/12.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.12)
