---
declaration: theorem
origin: cited
lean: OeisA105720.conjecture
statement: formalized
---

# Triangular matchstick numbers in the class of prime numbers

> $a(n) = \sum_{k = n}^{2n} p_k$, where $p_k$ is the $k$-th prime.
>
> *References:*
> - [A105720](https://oeis.org/A105720)

*Quoted from [FormalConjectures/OEIS/105720.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/105720.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements and 3 API statements, counted here but not shown.

## `OeisA105720.conjecture`

Open: stated without proof.

> Terms are squares at only(?) three values of $n = 3, 6, 4072$:
> corresponding terms are 6^2, 13^2, and 15735^2.

```lean
theorem conjecture :
    ∀ n : ℕ, 0 < n → (IsSquare (a n) ↔ (n = 3 ∨ n = 6 ∨ n = 4072))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/105720.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/105720.lean#L108).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/105720.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/105720.lean)
- [A105720](https://oeis.org/A105720)
