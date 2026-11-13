---
declaration: theorem
origin: cited
lean: OeisA17666.conjecture
statement: formalized
---

# Denominator of sum of reciprocals of divisors

> Denominator of sum of reciprocals of divisors of $n$:
>
> $$\sum_{d \mid n} \frac{1}{d} = \frac{\sigma(n)}{n}$$
>
> in lowest terms.
>
> *References:*
> - [A017666](https://oeis.org/A017666)

*Quoted from [FormalConjectures/OEIS/17666.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/17666.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA17666.conjecture`

Open: stated without proof.

> If $a(n)$ is in A005153, then $n$ is in A005153.
> - Jaycob Coleman, Sep 27 2014
>
> We require $0 < n$ because $a(0) = 1$ is in A005153 (practical numbers), but $0$ is not.

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) : OeisA5153.A (a n) → OeisA5153.A n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/17666.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/17666.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/17666.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/17666.lean)
- [A017666](https://oeis.org/A017666)
