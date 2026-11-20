---
declaration: theorem
origin: cited
lean: OeisA245211.conjecture
statement: formalized
---

# Sum of $d \cdot \tau(d)$ over proper divisors $d$ of $n$

> The sequence $a(n)$ is the sum of $d \cdot \tau(d)$ over all proper divisors $d < n$ of $n$,
> where $\tau(d)$ is the number of divisors of $d$:
>
> $$a(n) = \sum_{d \mid n, d < n} d \cdot \tau(d)$$
>
> *References:*
> - [A245211](https://oeis.org/A245211)

*Quoted from [FormalConjectures/OEIS/245211.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/245211.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA245211.conjecture`

Open: stated without proof.

> Conjecture: $21$ is the only positive integer $n$ such that $a(n) = n$.

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) : a n = n ↔ n = 21
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/245211.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/245211.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/245211.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/245211.lean)
- [A245211](https://oeis.org/A245211)
