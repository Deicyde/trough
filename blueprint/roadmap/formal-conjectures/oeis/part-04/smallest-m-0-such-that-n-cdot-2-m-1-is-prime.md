---
declaration: theorem
origin: cited
lean: OeisA78680.conjecture
statement: formalized
---

# Smallest $m > 0$ such that $n \cdot 2^m + 1$ is prime

> The sequence $a(n)$ is the smallest positive integer $m$ such that $n \cdot 2^m + 1$ is prime,
> or $0$ if no such $m$ exists.
>
> *References:*
> - [A078680](https://oeis.org/A078680)

*Quoted from [FormalConjectures/OEIS/78680.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/78680.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA78680.conjecture`

Open: stated without proof.

> There is a conjecture that the first zero is $n = 65536 = 2^{16}$ (which is equivalent to
> the statement that $2^{2^k} + 1$ is composite for $k > 4$). - _T. D. Noe_, Feb 25 2011

```lean
theorem conjecture :
    a (2 ^ 16) = 0 ∧ ∀ n : ℕ, 1 ≤ n ∧ n < 2 ^ 16 → a n ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/78680.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/78680.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/78680.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/78680.lean)
- [A078680](https://oeis.org/A078680)
