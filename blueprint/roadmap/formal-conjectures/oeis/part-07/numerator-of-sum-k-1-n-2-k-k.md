---
declaration: theorem
origin: cited
lean: OeisA108866.conjecture
statement: formalized
---

# Numerator of $\sum_{k=1}^n 2^k/k$.

> Conjecture: for $n > 3$,
> $\textrm{numerator}(-2/n + \sum_{k=1}^{n} \frac{2^k}{k}) == 0 (\textrm{mod} n^2)$
> if and only if n is prime.
>
> *References:*
> - [A108866](https://oeis.org/A108866)

*Quoted from [FormalConjectures/OEIS/108866.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/108866.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA108866.conjecture`

Open: stated without proof.

> Conjecture: for $n > 3$,
> $\textrm{numerator}(-2/n + \sum_{k=1}^{n} \frac{2^k}{k}) == 0 (\textrm{mod} n^2)$
> if and only if n is prime.

```lean
theorem conjecture {n : ℕ} (hn : n > 3) :
    (ratExpression n).num ≡ 0 [ZMOD (n^2 : ℤ)] ↔ n.Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/108866.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/108866.lean#L76).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/108866.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/108866.lean)
- [A108866](https://oeis.org/A108866)
