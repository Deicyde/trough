---
declaration: theorem
origin: cited
lean: Green26.green_26, Green26.green_26.variants.yu25, Green26.green_26.variants.alm91, Green26.green_26.variants.open
statement: formalized
---

# Green's Open Problem 26

> References:
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.26)
> - [JLP92] Jaeger, François, et al. "Group connectivity of graphs—a nonhomogeneous analogue of
>   nowhere-zero flow properties." Journal of Combinatorial Theory, Series B 56.2 (1992): 165-182.
> - [ALM91] Alon, Noga, Nathan Linial, and Roy Meshulam. "Additive bases of vector spaces over prime
>   fields." Journal of Combinatorial Theory, Series A 57.2 (1991): 203-210.
> - [Yu25] Yu, Yang. "Note on the Additive Basis Conjecture." arXiv preprint arXiv:2510.01300 (2025).

*Quoted from [FormalConjectures/GreensOpenProblems/26.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/26.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Green26.green_26`

Solved: stated here without proof.

> Let $A_1, \dots, A_{100}$ be "cubes" in $\mathbb{F}^n_3$.
> Is it true that $A_1 + \dots + A_{100} = \mathbb{F}^n_3$?

```lean
theorem green_26 :
    ∀ n : ℕ,
      ∀ A : Fin 100 → Set (𝔽₃ n), (∀ i, IsCube (A i)) →
      ∑ i, A i = univ
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/26.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/26.lean#L53).

## `Green26.green_26.variants.yu25`

Solved: stated here without proof.

> [Yu25] has solved the original problem (with 100 replaced by 4)

```lean
theorem green_26.variants.yu25 :
    ∀ n : ℕ,
    ∀ A : Fin 4 → Set (𝔽₃ n), (∀ i, IsCube (A i)) →
      ∑ i, A i = univ
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/26.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/26.lean#L61).

## `Green26.green_26.variants.alm91`

Solved: stated here without proof.

> [ALM91] showed that if 100 is replaced by $\leq c(p) \log n$ then the result is true for
> $\mathbb{F}^n_p$.

```lean
theorem green_26.variants.alm91 :
    ∀ (p : ℕ) [Fact p.Prime],
      ∃ (k : ℕ → ℕ),
        ((fun n ↦ (k n : ℝ)) =O[atTop] fun n ↦ Real.log n) ∧
        ∀ᶠ n in atTop,
          ∀ A : Fin (k n) → Set (𝔽 p n), (∀ i, IsCube (A i)) →
          ∑ i, A i = univ
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/26.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/26.lean#L74).

## `Green26.green_26.variants.open`

Open: stated without proof.

> The analogous problem in $\mathbb{F}^n_p$ remains open. [Gr24]

```lean
theorem green_26.variants.open :
    ∀ (p : ℕ) [Fact p.Prime],
      (∃ C, ∀ n, ∀ A : Fin C → Set (𝔽 p n), (∀ i, IsCube (A i)) →
      ∑ i, A i = univ)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/26.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/26.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/26.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/26.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.26)
