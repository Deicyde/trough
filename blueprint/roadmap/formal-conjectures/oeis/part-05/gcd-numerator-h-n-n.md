---
declaration: theorem
origin: cited
lean: OeisA93818.conjecture
statement: formalized
---

# $\gcd(\mathrm{numerator}(H_n), n!)$

> $a(n) = \gcd(\mathrm{A001008}(n), n!)$, where $\mathrm{A001008}(n)$ is the numerator of
> the $n$-th harmonic number $H_n = \sum_{i=1}^n \frac{1}{i}$.
>
> *References:*
> - [A093818](https://oeis.org/A093818)

*Quoted from [FormalConjectures/OEIS/93818.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/93818.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA93818.conjecture`

Open: stated without proof.

> Conjecture: Every odd prime occurs as a term in the sequence.

```lean
theorem conjecture (p : ℕ) (hp : p.Prime) (hp_odd : p ≠ 2) : ∃ n > 0, a n = p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/93818.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/93818.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/93818.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/93818.lean)
- [A093818](https://oeis.org/A093818)
