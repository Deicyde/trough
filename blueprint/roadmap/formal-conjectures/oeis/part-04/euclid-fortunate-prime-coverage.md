---
declaration: theorem
origin: cited
lean: OeisA67836.conjecture
statement: formalized
---

# Euclid–Fortunate prime coverage

> OEIS A067836 starts with $2$. Each later term is the gap from the product of all previous terms to
> the least prime strictly greater than that product plus one.
>
> *References:*
> - [OEIS A067836](https://oeis.org/A067836)

*Quoted from [FormalConjectures/OEIS/67836.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/67836.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements and 5 API statements, counted here but not shown.

## `OeisA67836.conjecture`

Open: stated without proof.

> [OEIS A067836](https://oeis.org/A067836) asks: "Do all primes occur in the sequence?"

```lean
theorem conjecture :
    ∀ p, p.Prime → ∃ n ≥ 1, a n = p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/67836.lean, line 138](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/67836.lean#L138).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/67836.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/67836.lean)
- [OEIS A067836](https://oeis.org/A067836)
