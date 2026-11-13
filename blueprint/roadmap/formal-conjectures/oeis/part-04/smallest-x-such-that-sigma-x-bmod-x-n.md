---
declaration: theorem
origin: cited
lean: OeisA76495.conjecture
statement: formalized
---

# Smallest $x$ such that $\sigma(x) \bmod x = n$

> The sequence $a(n)$ is the smallest positive integer $x$ such that $\sigma_1(x) \bmod x = n$,
> or $0$ if no such $x$ exists.
>
> *References:*
> - [A076495](https://oeis.org/A076495)

*Quoted from [FormalConjectures/OEIS/76495.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/76495.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA76495.conjecture`

Open: stated without proof.

> At present, the 0 entry for $n = 5$ is only a conjecture.
> That is, it is conjectured that there is no positive integer $x$ such that
> $\sigma_1(x) \bmod x = 5$.

```lean
theorem conjecture : a 5 = 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/76495.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/76495.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/76495.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/76495.lean)
- [A076495](https://oeis.org/A076495)
