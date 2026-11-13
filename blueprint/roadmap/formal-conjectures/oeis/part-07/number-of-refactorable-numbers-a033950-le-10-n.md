---
declaration: theorem
origin: cited
lean: OeisA111291.conjecture, OeisA111291.colton_conjecture
statement: formalized
---

# Number of refactorable numbers (A033950) $\le 10^n$

> A number $k$ is refactorable if its number of divisors, $\tau(k)$, divides $k$.
>
> *References:*
> - [A111291](https://oeis.org/A111291)
> - [Co99] Colton, S., *Refactorable numbers - a machine invention*. J. Integer Seq. 2 (1999),
>   Article 99.1.2.
> - [Ze02] Zelinsky, J., *Tau numbers: a partial proof of a conjecture and other results*.
>   J. Integer Seq. 5 (2002), Article 02.2.8.
> - [Sp85] Spiro, C., *How often is the number of divisors of n a divisor of n?*
>   J. Number Theory 21 (1985), 81--100.

*Quoted from [FormalConjectures/OEIS/111291.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/111291.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 6 test statements, counted here but not shown.

## `OeisA111291.conjecture`

Solved: stated here without proof.

> Simon Colton conjectures that the number of refactorable numbers less than $x$ is at least
> $\frac{x}{2\log x}$. This is an asymptotic claim, so we state it for sufficiently large $x$.
>
> In this form it is a theorem: Zelinsky [Ze02, Theorem 7] proved that for every $k$ the number of
> refactorable numbers $\le n$ exceeds $k \pi(n)$ for all sufficiently large $n$, and
> $\pi(n) \sim n / \log n$. It also follows from Spiro's asymptotic [Sp85], by which the count is
> $\frac{x}{\sqrt{\log x}} (\log \log x)^{-1 + o(1)}$. See `colton_conjecture` for the
> pointwise conjecture that remains open.

```lean
theorem conjecture : ∀ᶠ x in Filter.atTop,
    (countRefactorable x : ℝ) ≥ x / (2 * Real.log x)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/111291.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/111291.lean#L88).

## `OeisA111291.colton_conjecture`

Open: stated without proof.

> Colton's conjecture [Co99] as stated by Zelinsky [Ze02]: for every $n$, the number of
> refactorable numbers $\le n$ is at least half the number of primes $\le n$, i.e.
> $\pi(n) \le 2\,T(n)$.
>
> Zelinsky [Ze02] proved this for all sufficiently large $n$ (see `conjecture`), with an explicit
> bound of $7.42 \cdot 10^{13}$ beyond which it holds; the remaining range is open.

```lean
theorem colton_conjecture : ∀ n : ℕ, Nat.primeCounting n ≤ 2 * countRefactorableNat n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/111291.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/111291.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/111291.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/111291.lean)
- [A111291](https://oeis.org/A111291)
