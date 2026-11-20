---
declaration: theorem
origin: cited
lean: OeisA100800.conjecture
statement: formalized
---

# Conjectures associated with A100800

> Let $f(n) = n + \text{sum of the digits of } n$. If $f(n)$ is multiple of $n$ then $a(n)= f(n)$
> else $a(n) = f(f(f(n)))\dots$ until one gets a multiple of $n$; $a(n) = 0$ if no such number
> exists.
>
> *References:*
> - [A100800](https://oeis.org/A100800)

*Quoted from [FormalConjectures/OEIS/100800.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/100800.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements and 1 API statement, counted here but not shown.

## `OeisA100800.conjecture`

Open: stated without proof.

> A100800 Conjecture: No term is zero.

```lean
theorem conjecture : ∀ (n : ℕ), n ≠ 0 → a n ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/100800.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/100800.lean#L87).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/100800.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/100800.lean)
- [A100800](https://oeis.org/A100800)
