---
declaration: theorem
origin: cited
lean: OeisA231577.conjecture
statement: formalized
---

# Ways to write $n = x + y$ with $2^x + y(y+1)/2$ prime

> Number of ways to write $n = x + y$ ($x, y > 0$) with $2^x + y(y+1)/2$ prime.
>
> *References:*
> - [A231577](https://oeis.org/A231577)

*Quoted from [FormalConjectures/OEIS/231577.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/231577.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA231577.conjecture`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 1$.

```lean
theorem conjecture (n : ℕ) (hn : n > 1) : a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/231577.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/231577.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/231577.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/231577.lean)
- [A231577](https://oeis.org/A231577)
