---
declaration: theorem
origin: cited
lean: DeterminantalConjecture.determinantal_conjecture
statement: formalized
---

# Determinantal conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Determinantal_conjecture)

*Quoted from [FormalConjectures/Wikipedia/DeterminantalConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/DeterminantalConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `DeterminantalConjecture.determinantal_conjecture`

Open: stated without proof.

> Does the determinant of the sum $A + B$ of two $n \times n$ normal
> complex matrices $A$ and $B$ always lie in the convex hull
> of the $n!$ points $\prod\_i (\lambda(A)\_i + \lambda(B)\_{\sigma(i)})$?
> Here the numbers $\lambda(A)\_i$ and $\lambda(B)\_i$ are
> the eigenvalues of $A$ and $B$, and $\sigma$ is an element of the symmetric
> group $S\_n$.

```lean
theorem determinantal_conjecture
    (n : Type) [Fintype n] [DecidableEq n]
    (d1 d2 : n → ℂ) (U1 U2 : unitary (Matrix n n ℂ)) :
    (U1 * Matrix.diagonal d1 * star U1 + U2 * Matrix.diagonal d2 * star U2).det
      ∈ convexHull ℝ { ∏ i, (d1 i + d2 (σ i)) | σ : Equiv.Perm n }
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Wikipedia/DeterminantalConjecture.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/DeterminantalConjecture.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/DeterminantalConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/DeterminantalConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Determinantal_conjecture)
