---
declaration: theorem
origin: cited
lean: OeisA130911.conjecture
statement: formalized
---

# Odious primes minus evil primes among first $n$ primes

> $a(n)$ is the number of primes with odd binary weight (odious primes) among the first $n$ primes
> minus the number with even binary weight (evil primes).
>
> *References:*
> - [A130911](https://oeis.org/A130911)

*Quoted from [FormalConjectures/OEIS/130911.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/130911.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA130911.conjecture`

Open: stated without proof.

> Shevelev conjectures that $a(n) \ge 0$ for $n > 3$.

```lean
theorem conjecture (n : ℕ) (hn : 3 < n) : a n ≥ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/130911.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/130911.lean#L98).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/130911.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/130911.lean)
- [A130911](https://oeis.org/A130911)
