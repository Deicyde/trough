---
declaration: theorem
origin: cited
lean: OeisA49473.conjecture
statement: formalized
---

# Nearest integer to $n/\sqrt{2}$

> Nearest integer to $n/\sqrt{2}$, defined by $\lfloor n/\sqrt{2} + 1/2 \rfloor$.
>
> *References:*
> - [A049473](https://oeis.org/A049473)

*Quoted from [FormalConjectures/OEIS/49473.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/49473.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 6 test statements, counted here but not shown.

## `OeisA49473.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a049473-zeta3-beatty/blob/b3a74bf/lean/OeisA49473FC.lean#L667-L673](https://github.com/KitaKen1/oeis-a049473-zeta3-beatty/blob/b3a74bf/lean/OeisA49473FC.lean#L667-L673).

> Let $s(n) = \zeta(3) - \sum_{k=1}^n \frac{1}{k^3}$.
> Conjecture: for $n \ge 1$, $s(a(n)) < \frac{1}{n^2} < s(a(n)-1)$, and the difference sequence of
> A049473 consists solely of $0$'s and $1$'s, in positions given by the nonhomogeneous Beatty
> sequences A001954 and A001953, respectively.
> - Clark Kimberling, Oct 05 2014

```lean
theorem conjecture :
    (∀ n : ℕ, 1 ≤ n → s (a n) < 1 / (n : ℝ) ^ 2 ∧ 1 / (n : ℝ) ^ 2 < s (a n - 1)) ∧
    (∀ n : ℕ, 1 ≤ n →
      let diff : ℕ := a n - a (n - 1)
      (diff = 0 ↔ n - 1 ∈ A001954) ∧ (diff = 1 ↔ n - 1 ∈ A001953))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/49473.lean, line 195](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/49473.lean#L195).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/49473.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/49473.lean)
- [A049473](https://oeis.org/A049473)
