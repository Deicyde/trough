---
declaration: theorem
origin: cited
lean: OeisA214497.conjecture
statement: formalized
---

# Twin primes of the form $(3^n - k) 2^n \pm 1$

> For $n > 0$, $a(n)$ is the smallest nonnegative integer $k$ such that $(3^n - k) 2^n - 1$ and
> $(3^n - k) 2^n + 1$ form a twin prime pair.
>
> *References:*
> - [A214497](https://oeis.org/A214497)

*Quoted from [FormalConjectures/OEIS/214497.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/214497.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA214497.conjecture`

Open: stated without proof.

> Conjecture: There is always one such $k$ for each $n > 0$ such that
> $(3^n - k) 2^n - 1$ and $(3^n - k) 2^n + 1$ are a twin prime pair.

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) : (a n).isSome
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/214497.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/214497.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/214497.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/214497.lean)
- [A214497](https://oeis.org/A214497)
