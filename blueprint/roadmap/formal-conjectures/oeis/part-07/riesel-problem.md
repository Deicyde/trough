---
declaration: theorem
origin: cited
lean: OeisA108129.conjecture
statement: formalized
---

# Riesel Problem

> Riesel problem: let $k=2n-1$; then $a(n)$ is the smallest $m \ge 1$ such that
> $k \cdot 2^m-1$ is prime, or $-1$ if no such prime exists.
>
> *References:*
> - [A108129](https://oeis.org/A108129)

*Quoted from [FormalConjectures/OEIS/108129.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/108129.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements and 1 API statement, counted here but not shown.

## `OeisA108129.conjecture`

Open: stated without proof.

> It is conjectured that the integer $k = 509203$ is the smallest Riesel number,
> that is, the first $n$ such that $a(n) = -1$ is $254602$.

```lean
theorem conjecture :
    a 254602 = -1 ∧ (∀ n : ℕ, 1 ≤ n ∧ n < 254602 → a n ≠ -1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/108129.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/108129.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/108129.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/108129.lean)
- [A108129](https://oeis.org/A108129)
