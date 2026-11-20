---
declaration: theorem
origin: cited
lean: OeisA214560.conjecture
statement: formalized
---

# Number of $0$'s in the binary expansion of $n^2$

> For $n \ge 0$, $a(n)$ is the number of $0$'s in the base-$2$ representation of $n^2$
> (with $a(0) = 1$).
>
> *References:*
> - [A214560](https://oeis.org/A214560)

*Quoted from [FormalConjectures/OEIS/214560.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/214560.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA214560.conjecture`

Open: stated without proof.

> Conjecture: For every $x \ge 0$, there is an $i$ such that $a(n) > x$
> for all $n > i$.

```lean
theorem conjecture (x : ℕ) : ∃ i : ℕ, ∀ n > i, x < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/214560.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/214560.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/214560.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/214560.lean)
- [A214560](https://oeis.org/A214560)
