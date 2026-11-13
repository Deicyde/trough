---
declaration: theorem
origin: cited
lean: Green1.green_1
statement: formalized
---

# Ben Green's Open Problem 1

> *References:*
> - [Ben Green's Open Problem 1](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.1 Problem 1)
> - [Be25] Bedert, Benjamin, Large sum-free subsets of sets of integers via $L^1$-estimates for
>   trigonometric series. [arXiv:2502.08624](https://arxiv.org/abs/2502.08624) (2025).

*Quoted from [FormalConjectures/GreensOpenProblems/1.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/1.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Green1.green_1`

Solved: stated here without proof.

> Let $A$ be a set of $n$ positive integers. Does $A$ contain a sum-free set
> of size at least $\frac n 3 + Ω(n)$, where $Ω(n) → ∞$ as $n → ∞$?
>
> Bedert [Be25] proved that every set of $n$ integers contains a sum-free subset of size at least
> $\frac n 3 + c \log\log n$ for some absolute constant $c > 0$, so the answer is yes.

```lean
theorem green_1 : ∃ Ω : ℕ → ℝ, atTop.Tendsto Ω atTop ∧
     ∀ n, ∀ (A : Finset ℕ), (∀ a ∈ A, 0 < a) → A.card = n →
     ∃ (S : Finset ℕ), S ⊆ A ∧ IsSumFree (S : Set ℕ) ∧ ((n : ℝ) / 3) + Ω n ≤ S.card
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/1.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/1.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/1.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/1.lean)
- [https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.1](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.1)
