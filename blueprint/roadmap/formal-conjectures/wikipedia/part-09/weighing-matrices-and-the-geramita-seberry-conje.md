---
declaration: theorem
origin: cited
lean: WeighingMatrix.weighing_matrix_conjecture, WeighingMatrix.weighing_matrix_conjecture.variants.asymptotic
statement: formalized
---

# Weighing matrices and the Geramita–Seberry conjecture

> A *weighing matrix* $W(n, w)$ of order $n$ and weight $w$ is an $n \times n$ matrix with entries in
> $\{-1, 0, 1\}$ satisfying $W W^{\mathsf{T}} = w I_n$. At $w = n$, this recovers Hadamard matrices.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Weighing_matrix)
> - [GS79] Geramita, A. V. and Seberry, J. (1979). *Orthogonal Designs: Quadratic Forms and Hadamard
>   Matrices*, Lecture Notes in Pure and Applied Mathematics 45, Marcel Dekker, New York.

*Quoted from [FormalConjectures/Wikipedia/WeighingMatrix.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WeighingMatrix.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 2 test statements and 3 API statements, counted here but not shown.

## `WeighingMatrix.weighing_matrix_conjecture`

Open: stated without proof.

> **Weighing matrix conjecture** (Wallis 1972; Geramita–Seberry [GS79]): for every positive integer
> $m \ge 1$ and every weight $0 \le w \le 4m$, there exists a weighing matrix $W(4m, w)$ of order
> $4m$ and weight $w$.
>
> At $w = 4m$, this specializes to Hadamard's conjecture.

```lean
theorem weighing_matrix_conjecture (m w : ℕ) (hm : 1 ≤ m) (hw : w ≤ 4 * m) :
    ∃ W, IsWeighingMatrix (4 * m) w W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Wikipedia/WeighingMatrix.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WeighingMatrix.lean#L92).

## `WeighingMatrix.weighing_matrix_conjecture.variants.asymptotic`

Solved: stated here without proof.

> **Asymptotic existence of weighing matrices** (Geramita–Seberry [GS79]): for every fixed weight
> $w$, a weighing matrix $W(4m, w)$ exists for all sufficiently large multiples $4m$.

```lean
theorem weighing_matrix_conjecture.variants.asymptotic (w : ℕ) :
    ∀ᶠ m in Filter.atTop, ∃ W, IsWeighingMatrix (4 * m) w W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Wikipedia/WeighingMatrix.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WeighingMatrix.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/WeighingMatrix.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WeighingMatrix.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Weighing_matrix)
