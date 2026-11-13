---
declaration: theorem
origin: cited
lean: OeisA60841.conjecture1, OeisA60841.conjecture2
statement: formalized
---

# Numerator of $1/\det(M)$ for $M[i,j] = 1/\operatorname{lcm}(i,j)$

> Numerator of $1/\det(M)$ where $M$ is the $n \times n$ matrix with
> $M[i,j] = 1/\operatorname{lcm}(i,j)$.
>
> *References:*
> - [A060841](https://oeis.org/A060841)
> - T. Adamczewski, "OEIS Open: How many conjectures can language models turn into theorems?",
>   [arXiv:2608.11941](https://arxiv.org/abs/2608.11941) [cs.AI], 2026.

*Quoted from [FormalConjectures/OEIS/60841.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/60841.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA60841.conjecture1`

Open: stated without proof.

> "Conjecture: $1/\det(M)$ is an integer only for n: 1 to 34, 36 and 38." - _Robert G. Wilson v_,
> Aug 02 2015

```lean
theorem conjecture1 :
    ∀ n : ℕ, 1 ≤ n → (((lcmMatrix n).det)⁻¹.den = 1 ↔ n ∈ integerDetN)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/OEIS/60841.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/60841.lean#L76).

## `OeisA60841.conjecture2`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_OeisA60841_conjecture2.lean#L377](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_OeisA60841_conjecture2.lean#L377).

> "All denominators are powers of two (A000079)." - _Robert G. Wilson v_, Aug 02 2015
>
> This is false: for $n = 1807$ the denominator of $1/\det(M)$ is divisible by $3$.
> See T. Adamczewski, OEIS Open: How many conjectures can language models turn into theorems?,
> [arXiv:2608.11941](https://arxiv.org/abs/2608.11941). The Lean disproof there uses the closed
> form $1/\det(M) = \prod_{k=1}^n k^2/\varphi(k)$ from the OEIS entry:
> https://github.com/epoch-research/LeanOpenProblems-results/blob/fd09021e79869476ef83cda231312f1a2a89c8d7/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_60841_conjecture_0/Submission/Spec.lean#L272

```lean
theorem conjecture2 :
    ¬ ∀ n : ℕ, 1 ≤ n → ∃ k : ℕ, ((lcmMatrix n).det)⁻¹.den = 2 ^ k
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/OEIS/60841.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/60841.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/60841.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/60841.lean)
- [A060841](https://oeis.org/A060841)
