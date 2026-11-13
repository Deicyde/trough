---
declaration: theorem
origin: cited
lean: OeisA113609.conjecture
statement: formalized
---

# Number of prime powers $q<=n$ such that also $q+2$ is a prime power

> *References:*
> - [A113609](https://oeis.org/A113609)

*Quoted from [FormalConjectures/OEIS/113609.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113609.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA113609.conjecture`

Open: stated without proof.

> (25,27) is the smallest pair of prime powers (q,q+2) such that both q and q+2 are not primes,
> conjecture: there are more (but not < 10^6).

```lean
theorem conjecture :
  ∃ q ≥ 1000000,
    IsOeisPrimePower q ∧ IsOeisPrimePower (q + 2) ∧
    ¬ q.Prime ∧ ¬ (q + 2).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/113609.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113609.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/113609.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113609.lean)
- [A113609](https://oeis.org/A113609)
