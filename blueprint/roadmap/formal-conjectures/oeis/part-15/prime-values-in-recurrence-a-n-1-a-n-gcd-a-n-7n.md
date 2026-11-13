---
declaration: theorem
origin: cited
lean: OeisA261307.conjecture
statement: formalized
---

# Prime values in recurrence $a(n+1) = |a(n) - \gcd(a(n), 7n+6)|$

> The sequence is defined by $a(1) = 1$ and $a(n+1) = |a(n) - \gcd(a(n), 7n+6)|$ for $n \ge 1$.
>
> *References:*
> - [A261307](https://oeis.org/A261307)

*Quoted from [FormalConjectures/OEIS/261307.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261307.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA261307.conjecture`

Open: stated without proof.

> It is conjectured that for all $n > 2$, $a(n) = 0$ implies that $7n+6 = a(n+1)$ is prime,
> cf. A186259.

```lean
theorem conjecture (n : ℕ) (hn : 2 < n) (ha : a n = 0) : Nat.Prime (7 * n + 6)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/261307.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261307.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/261307.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261307.lean)
- [A261307](https://oeis.org/A261307)
