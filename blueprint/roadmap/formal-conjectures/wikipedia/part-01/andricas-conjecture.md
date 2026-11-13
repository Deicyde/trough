---
declaration: theorem
origin: cited
lean: Andrica.andrica_conjecture, Andrica.andrica_conjecture.ferreira_large_n
statement: formalized
---

# Andrica's conjecture

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Andrica%27s_conjecture)
> - [Luan Alberto Ferreira, *Real exponential sums over primes and prime gaps*](https://arxiv.org/abs/2307.08725)

*Quoted from [FormalConjectures/Wikipedia/Andrica.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Andrica.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Andrica.andrica_conjecture`

Open: stated without proof.

> **Andrica's conjecture**
> The inequality $\sqrt{p_{n+1}}-\sqrt{p_n} < 1$ holds for all $n$, where $p_n$ is the $n$-th prime number.

```lean
theorem andrica_conjecture (n : ℕ) :
    Real.sqrt ((n+1).nth Nat.Prime) - Real.sqrt (n.nth Nat.Prime) < 1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Andrica.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Andrica.lean#L38).

## `Andrica.andrica_conjecture.ferreira_large_n`

Solved: stated here without proof.

> Ferreira proved that Andrica's conjecture is true for sufficiently large n.

```lean
theorem andrica_conjecture.ferreira_large_n :
    ∀ᶠ n in atTop, Real.sqrt ((n+1).nth Nat.Prime) - Real.sqrt (n.nth Nat.Prime) < 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Andrica.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Andrica.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Andrica.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Andrica.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Andrica%27s_conjecture)
