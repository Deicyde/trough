---
declaration: theorem
origin: cited
lean: OeisA114216.conjecture
statement: formalized
---

# Largest odd divisor of $a(n-1) + \textrm{prime}(n)$

> $a(0)=0$; thereafter $a(n)$ = largest odd divisor of $a(n-1) + \textrm{prime}(n)$.
>
> *References:*
> - [A114216](https://oeis.org/A114216)

*Quoted from [FormalConjectures/OEIS/114216.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/114216.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA114216.conjecture`

Open: stated without proof.

> Is $a(33900)$ the last term equal to $1$?

```lean
theorem conjecture :
  ∀ n > 33900, a n ≠ 1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/114216.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/114216.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/114216.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/114216.lean)
- [A114216](https://oeis.org/A114216)
