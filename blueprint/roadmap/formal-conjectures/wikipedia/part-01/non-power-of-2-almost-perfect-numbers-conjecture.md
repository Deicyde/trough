---
declaration: theorem
origin: cited
lean: AlmostPerfectNumbers.exists_almost_perfect_not_power_of_two
statement: formalized
---

# Non-Power-of-2 Almost Perfect Numbers Conjecture

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Almost_perfect_number)
> - [mathworld](https://mathworld.wolfram.com/AlmostPerfectNumber.html)
> -

*Quoted from [FormalConjectures/Wikipedia/AlmostPerfectNumbers.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AlmostPerfectNumbers.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `AlmostPerfectNumbers.exists_almost_perfect_not_power_of_two`

Open: stated without proof.

> **Non-Power-of-2 Almost Perfect Numbers Conjecture.**
> Does there exist an almost perfect number that is not a power of 2?

```lean
theorem exists_almost_perfect_not_power_of_two :
    ∃ n : ℕ, AlmostPerfect n ∧ ¬ ∃ k : ℕ, n = 2^k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AlmostPerfectNumbers.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AlmostPerfectNumbers.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/AlmostPerfectNumbers.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AlmostPerfectNumbers.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Almost_perfect_number)
