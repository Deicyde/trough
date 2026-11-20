---
declaration: theorem
origin: cited
lean: OeisA7406.conjecture
statement: formalized
---

# Wolstenholme numbers

> Wolstenholme numbers: numerator of $\sum_{k=1}^n \frac{1}{k^2}$.
>
> *References:*
> - [A007406](https://oeis.org/A007406)

*Quoted from [FormalConjectures/OEIS/7406.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/7406.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA7406.conjecture`

Open: stated without proof.

> Conjecture: for $n > 3$, $\gcd(n, a(n-1)) = \text{A089026}(n)$.
> - Amiram Eldar and Thomas Ordowski, Jul 28 2019

```lean
theorem conjecture (n : ℕ) (hn : 3 < n) :
    Nat.gcd n (a (n - 1)) = OeisA89026.a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/7406.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/7406.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/7406.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/7406.lean)
- [A007406](https://oeis.org/A007406)
