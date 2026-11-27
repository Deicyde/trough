---
declaration: theorem
origin: cited
lean: EllipticDivisibilitySequence.einsiedler_everest_ward_finite_primes, EllipticDivisibilitySequence.silverman_eds_primitive_prime_divisors
statement: formalized
---

# Prime values and primitive divisors in elliptic divisibility sequences

> Morgan Ward (1948) studied integer divisibility sequences $(W_n)_{n \in \mathbb{Z}}$ satisfying
> the elliptic recurrence $W_{m+n} W_{m-n} W_1^2 = W_{m+1} W_{m-1} W_n^2 - W_{n+1} W_{n-1} W_m^2$.
> A normalized sequence ($W_1 = 1$) is *nonsingular* when its discriminant is nonzero—equivalently,
> by Ward's representation theorem, when $(W_n)$ evaluates the division polynomials $\psi_n(x, y)$
> at a rational point on an elliptic curve $E / \mathbb{Q}$ ($\Delta_E \ne 0$). In Ward's and
> Einsiedler–Everest–Ward's (§2) terminology, an elliptic divisibility sequence is *proper* when
> $W_0 = 0$, $W_1 = 1$, and $W_2 W_3 \ne 0$; for a normalized nonsingular sequence, non-periodicity
> ($W_n \ne 0$ for all $n \ne 0$, corresponding to a non-torsion rational point) automatically
> ensures properness and positive quadratic logarithmic growth. Joseph H. Silverman (1988) proved
> that all sufficiently large terms of a non-periodic nonsingular sequence admit primitive prime
> divisors, while Manfred Einsiedler, Graham Everest, and Thomas Ward (2001) conjectured that
> $|W_n|$ is prime for only finitely many indices $n \ge 1$.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Elliptic_divisibility_sequence)
> - M. Ward, *Memoir on elliptic divisibility sequences*, Amer. J. Math. **70** (1948), 31–74.
> - J. H. Silverman, *Wieferich's criterion and the $abc$-conjecture*, J. Number Theory **30**
>   (1988), no. 2, 226–237.
> - M. Einsiedler, G. Everest, and T. Ward, *Primes in elliptic divisibility sequences*, LMS J.
>   Comput. Math. **4** (2001), 1–13.

*Quoted from [FormalConjectures/Wikipedia/EllipticDivisibilitySequence.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/EllipticDivisibilitySequence.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 3 test statements, counted here but not shown.

## `EllipticDivisibilitySequence.einsiedler_everest_ward_finite_primes`

Open: stated without proof.

> Einsiedler–Everest–Ward Conjecture (2001): every non-periodic (`∀ n ≠ 0, W n ≠ 0`) normalized
> nonsingular elliptic divisibility sequence takes prime values $|W_n|$ at finitely many indices
> $n \ge 1$. (Einsiedler–Everest–Ward, eq. (10), p. 5 also study sequences obtained by dividing out
> bad-reduction factors, which need not satisfy the elliptic divisibility recurrence.)

```lean
theorem einsiedler_everest_ward_finite_primes :
    ∀ W : ℤ → ℤ,
      IsNonsingularEDS W →
      (∀ n : ℤ, n ≠ 0 → W n ≠ 0) →
      {n : ℕ | 1 ≤ n ∧ (W n).natAbs.Prime}.Finite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticDivisibilitySequence.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/EllipticDivisibilitySequence.lean#L113).

## `EllipticDivisibilitySequence.silverman_eds_primitive_prime_divisors`

Solved: stated here without proof.

> Silverman's Primitive Divisor Theorem (1988): every non-periodic (`∀ n ≠ 0, W n ≠ 0`)
> normalized nonsingular elliptic divisibility sequence has a primitive prime divisor for all
> sufficiently large $n$.

```lean
theorem silverman_eds_primitive_prime_divisors :
    ∀ W : ℤ → ℤ,
      IsNonsingularEDS W →
      (∀ n : ℤ, n ≠ 0 → W n ≠ 0) →
      ∀ᶠ n in Filter.atTop, HasPrimitivePrimeDivisor W n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticDivisibilitySequence.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/EllipticDivisibilitySequence.lean#L124).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/EllipticDivisibilitySequence.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/EllipticDivisibilitySequence.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Elliptic_divisibility_sequence)
