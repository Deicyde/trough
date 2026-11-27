---
declaration: theorem
origin: cited
lean: SternPrime.stern_primes_finite, SternPrime.isSternPrime_iff
statement: formalized
---

# Stern Primes

> As recounted by Laurent Hodges (1993), Christian Goldbach proposed in a 1752 letter to Euler that
> every odd integer greater than $1$ equals $p + 2 b^2$ with $b \ge 0$ (counting $1$ as prime); for
> modern primes, its nontrivial content is the *Goldbach–Stern conjecture* that every odd composite
> equals $p + 2 b^2$ with $p$ prime and $b \ge 1$. Moritz Abraham Stern (1856) refuted this via the
> counterexamples $5777$ and $5993$ (`OEIS A060003`).
>
> A prime $q$ admitting no decomposition $q = p + 2 b^2$ with $p$ prime and $b \ge 1$ is called a
> *Stern prime* (`OEIS A042978`). Only eight examples are known ($2, 3, 17, 137, 227, 977, 1187$, and
> $1493$); Euler noted heuristically that larger primes acquire more decompositions $p + 2 b^2$,
> suggesting that Stern primes form a finite set and that $1493$ may be the largest.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Stern_prime)
> - [OEIS A042978](https://oeis.org/A042978)
> - M. A. Stern, *Sur une assertion de Goldbach relative aux nombres impairs*, Nouv. Ann. Math.
>   **15** (1856), 23–24.
> - L. Hodges, *A lesser-known Goldbach conjecture*, Math. Mag. **66** (1993), no. 1, 45–47.

*Quoted from [FormalConjectures/Wikipedia/SternPrime.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SternPrime.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 2 test statements, counted here but not shown.

## `SternPrime.stern_primes_finite`

Open: stated without proof.

> Is the set of Stern primes finite? Euler's representation heuristic suggests that only finitely
> many primes avoid the form $p + 2 b^2$.

```lean
theorem stern_primes_finite : {q : ℕ | IsSternPrime q}.Finite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SternPrime.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SternPrime.lean#L90).

## `SternPrime.isSternPrime_iff`

Open: stated without proof.

> Does $\{2, 3, 17, 137, 227, 977, 1187, 1493\}$ exhaust all Stern primes? No ninth example appears
> among the first $100{,}000$ primes (McCranie) or below $2 \times 10^{13}$ (Chaffin, `OEIS A042978`).

```lean
theorem isSternPrime_iff :
    ∀ q : ℕ, IsSternPrime q ↔ q ∈ ({2, 3, 17, 137, 227, 977, 1187, 1493} : Set ℕ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SternPrime.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SternPrime.lean#L98).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SternPrime.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SternPrime.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Stern_prime)
