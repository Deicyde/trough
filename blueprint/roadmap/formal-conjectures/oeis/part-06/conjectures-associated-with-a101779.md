---
declaration: theorem
origin: cited
lean: OeisA101779.conjecture
statement: formalized
---

# Conjectures associated with A101779

> $a(n)$ is the least $k$ such that all of $k, 2k+1, 3k+2, ..., nk+n-1$ are primes,
> or $0$ if no such $k$ is found.
> It is conjectured $k$ always exists.
>
> *References:*
> - [A101779](https://oeis.org/A101779)

*Quoted from [FormalConjectures/OEIS/101779.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/101779.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA101779.conjecture`

Open: stated without proof.

> It is conjectured k always exists.

```lean
theorem conjecture : ∀ (n : ℕ), 1 ≤ n → ∃ k : ℕ, Ak n k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/101779.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/101779.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/101779.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/101779.lean)
- [A101779](https://oeis.org/A101779)
