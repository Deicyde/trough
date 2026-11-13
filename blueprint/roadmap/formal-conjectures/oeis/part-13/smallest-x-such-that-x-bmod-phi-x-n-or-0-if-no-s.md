---
declaration: theorem
origin: cited
lean: OeisA234642.conjecture
statement: formalized
---

# Smallest $x$ such that $x \bmod \phi(x) = n$, or $0$ if no such $x$ exists

> For $n \ge 0$, $a(n)$ is the smallest positive integer $x$ such that $x \bmod \phi(x) = n$, or $0$
> if no such $x$ exists, where $\phi$ is Euler's totient function.
>
> *References:*
> - [A234642](https://oeis.org/A234642)

*Quoted from [FormalConjectures/OEIS/234642.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/234642.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA234642.conjecture`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n$.

```lean
theorem conjecture (n : ℕ) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234642.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/234642.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/234642.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/234642.lean)
- [A234642](https://oeis.org/A234642)
