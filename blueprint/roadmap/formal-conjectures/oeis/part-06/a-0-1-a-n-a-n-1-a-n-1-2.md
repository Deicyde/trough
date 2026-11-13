---
declaration: theorem
origin: cited
lean: OeisA102847.conjecture
statement: formalized
---

# $a(0) = 1$, $a(n) = a(n-1)a(n-1) + 2$

> *References:*
> - [A102847](https://oeis.org/A102847)

*Quoted from [FormalConjectures/OEIS/102847.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/102847.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 8 test statements, counted here but not shown.

## `OeisA102847.conjecture`

Open: stated without proof.

> Prime for $a(1) = 3$, $a(2) = 11$, $a(4) = 15131$; semiprime for $a(3) = 123 = 3 * 41$,
> $a(5) = 228947163 = 3 * 76315721$.
> $a(6)$, added by Jonathan Vos Post, has 4 prime factors.
> $a(7) = 41 * 811^2 * 106693969 * 317171188688357726699 * 8272236925540996054440172449761$.
> When is the next prime in the sequence?

```lean
theorem conjecture : conjecture.answer = sInf {n : ℕ | 4 < n ∧ (a n).Prime}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/102847.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/102847.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/102847.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/102847.lean)
- [A102847](https://oeis.org/A102847)
