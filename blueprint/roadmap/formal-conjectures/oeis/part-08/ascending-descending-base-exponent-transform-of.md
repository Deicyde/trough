---
declaration: theorem
origin: cited
lean: OeisA113257.conjecture1, OeisA113257.conjecture2
statement: formalized
---

# Ascending descending base exponent transform of squares

> a n is $\sum_{i=1}^n (i^2)^((n-i+1)^2)$.
>
> *References:*
> - [A113257](https://oeis.org/A113257)

*Quoted from [FormalConjectures/OEIS/113257.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113257.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA113257.conjecture1`

Open: stated without proof.

> The smallest prime in this sequence is $a(2) = 5$. What is the next prime?

```lean
theorem conjecture1 :
    conjecture1.answer = a (sInf {n : ℕ | 2 < n ∧ (a n).Prime})
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/113257.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113257.lean#L58).

## `OeisA113257.conjecture2`

Open: stated without proof.

> What is the first square value after 1?

```lean
theorem conjecture2 :
    conjecture2.answer = a (sInf {n : ℕ | 1 < n ∧ IsSquare (a n)})
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/113257.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113257.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/113257.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113257.lean)
- [A113257](https://oeis.org/A113257)
