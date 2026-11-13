---
declaration: theorem
origin: cited
lean: BetrothedNumbers.same_parity_betrothed, BetrothedNumbers.infinitely_many_betrothed
statement: formalized
---

# Betrothed numbers

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Betrothed_numbers)
> - [OEIS A005276](https://oeis.org/A005276)

*Quoted from [FormalConjectures/Wikipedia/BetrothedNumbers.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BetrothedNumbers.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 2 test statements, counted here but not shown.

## `BetrothedNumbers.same_parity_betrothed`

Open: stated without proof.

> **Same parity betrothed numbers conjecture.**
> Do there exist betrothed numbers $(m, n)$ where both have the same parity
> (both even or both odd)?
>
> All known betrothed pairs consist of one even and one odd number.
>
> The requirement $m \neq n$ is part of the question: $\mathrm{IsBetrothed}\ n\ n$ says
> $\sigma(n) = 2n + 1$, i.e. that $n$ is quasiperfect, which is the separate open problem
> `QuasiperfectNumbers.exists_quasiperfect`.

```lean
theorem same_parity_betrothed :
    ∃ m n : ℕ, m ≠ n ∧ IsBetrothed m n ∧ (Even m ↔ Even n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/BetrothedNumbers.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BetrothedNumbers.lean#L67).

## `BetrothedNumbers.infinitely_many_betrothed`

Open: stated without proof.

> **Infinitude of betrothed numbers conjecture.**
> Are there infinitely many betrothed number pairs?

```lean
theorem infinitely_many_betrothed :
    {p : ℕ × ℕ | p.1 < p.2 ∧ IsBetrothed p.1 p.2}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/BetrothedNumbers.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BetrothedNumbers.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/BetrothedNumbers.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BetrothedNumbers.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Betrothed_numbers)
