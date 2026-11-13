---
declaration: theorem
origin: cited
lean: Green58.green_58
statement: formalized
---

# Ben Green's Open Problem 58

> *Reference:* [Ben Green's Open Problem 58](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.8 Problem 58)

*Quoted from [FormalConjectures/GreensOpenProblems/58.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/58.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Green58.green_58`

Open: stated without proof.

> Suppose $A, B ⊆ \{1, \dots, N\}$ both have size at least $N^{0.49}$. Must the sumset $A + B$
> contain a composite number?

```lean
theorem green_58 :
    ∀ᶠ (N : ℕ) in Filter.atTop, ∀ᵉ (A ⊆ Finset.Icc 1 N) (B ⊆ Finset.Icc 1 N),
      (N : ℝ) ^ (0.49 : ℝ) ≤ (A.card : ℝ) →
      (N : ℝ) ^ (0.49 : ℝ) ≤ (B.card : ℝ) →
      ∃ m ∈ (A + B), m.Composite
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/58.lean, line 36](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/58.lean#L36).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/58.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/58.lean)
- [https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.8](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.8)
