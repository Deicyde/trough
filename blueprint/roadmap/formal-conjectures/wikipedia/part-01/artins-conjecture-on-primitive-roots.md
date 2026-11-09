---
declaration: theorem
origin: cited
lean: ArtinPrimitiveRootsConjecture.artin_primitive_roots.parts.i, ArtinPrimitiveRootsConjecture.conditional_artin_primitive_roots.parts.i, ArtinPrimitiveRootsConjecture.artin_primitive_roots.parts.ii, ArtinPrimitiveRootsConjecture.conditional_artin_primitive_roots.parts.ii, ArtinPrimitiveRootsConjecture.artin_primitive_roots.variants.part_ii_square_or_minus_one, ArtinPrimitiveRootsConjecture.artin_primitive_roots.variants.part_ii_power_squarefreePart_not_modeq_one, ArtinPrimitiveRootsConjecture.conditional_artin_primitive_roots.variants.part_ii_power_squarefreePart_not_modeq_one, ArtinPrimitiveRootsConjecture.artin_primitive_roots.variants.part_ii_power_squarefreePart_modeq_one, ArtinPrimitiveRootsConjecture.conditional_artin_primitive_roots.variants.part_ii_power_squarefreePart_modeq_one
statement: formalized
---

# Artin's conjecture on primitive roots

> Artin's conjecture predicts, given an integer $a$, densities of primes $p$ for which
> $a$ is a primitive root modulo $p$. Under certain conditions (when $a$ is not a
> power and its squarefree part is not $1\pmod{4}$) the density is given by Artin's constant
>
> $$\prod_{p\ \text{prime}} \left(1 - \frac{1}{p(p - 1)}\right).$$
>
> For more general values of $a$, this constant must be corrected by certain factors.
> - When $a = b^m$, $m$ is a maximal odd power, the squarefree part of $b$ satisfies
>   $b_0 \not\equiv 1\pmod{4}$. Then Artin's constant should be multiplied by
>
> $$\prod_{p \mid m} \frac{p(p - 2)}{p^2 - p - 1}.$$
>
> - When $a = b^m$, $m$ is a maximal power, the squarefree part of $b$ satisfies
>   $b_0\equiv 1\pmod{4}$. Then Artin's constant should be multiplied by the factor in
>   the above bullet, as well as an additional entanglement factor from the primes dividing
>   $\gcd(b_0, m)$ and primes dividing $b_0$:
>
> $$1 - \prod_{p \mid \gcd(b_0, m)} \frac{1}{2 - p}
>   \prod_{p \mid b_0, p\nmid m} \frac{1}{1 + p - p^2}.$$
>
> - When $a = -1$ or $a$ is a square, then the density is $0$.
>
> Note that Artin's conjecture has been proved by Hooley [Ho67] subject to the Riemann hypothesis
> for the Dedekind zeta functions of the Kummer fields $\mathbb{Q}(\zeta_k, a^{1/k})$, $k$
> squarefree. These fields are in general non-abelian over $\mathbb{Q}$, so this hypothesis is not
> covered by the Generalized Riemann Hypothesis for Dirichlet $L$-functions.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Artin%27s_conjecture_on_primitive_roots)
> - [A85397](https://oeis.org/A85397)
> - [LMS14](https://arxiv.org/pdf/1112.4816) Lenstra, H.W. et al. "Character sums for primitive root densities" _arXiv:1112.4816_ [math.NT] (2014).
> - [Ho67] Hooley, C. "On Artin's conjecture." _Journal für die reine und angewandte Mathematik_ 225 (1967): 209-220.

*Quoted from [FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 9 research or textbook statements: 4 open and 5 solved. It also has 1 API statement, counted here but not shown.

## `ArtinPrimitiveRootsConjecture.artin_primitive_roots.parts.i`

Open: stated without proof.

> **Artin's Conjecture on Primitive Roots**, first half.
> Let $a$ be an integer that is not a square number and not $−1$. Then the set $S(a)$
> of primes $p$ such that $a$ is a primitive root modulo $p$ has a positive asymptotic
> density inside the set of primes. In particular, $S(a)$ is infinite.

```lean
theorem artin_primitive_roots.parts.i (a : ℤ) (ha : ¬IsSquare a) (ha' : a ≠ -1) :
    ∃ x > 0, (S a).HasDensity x {p | p.Prime}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean#L120).

## `ArtinPrimitiveRootsConjecture.conditional_artin_primitive_roots.parts.i`

Solved: stated here without proof.

> **Artin's Conjecture on Primitive Roots**, first half, conditional on the Riemann hypothesis
> for the Dedekind zeta functions of the fields $\mathbb{Q}(\zeta_k, a^{1/k})$, $k$ squarefree
> [Ho67].

```lean
theorem conditional_artin_primitive_roots.parts.i (a : ℤ) (ha : ¬IsSquare a) (ha' : a ≠ -1)
    (h : HooleyHypothesis a) :
    ∃ x > 0, (S a).HasDensity x {p | p.Prime}
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean#L130).

## `ArtinPrimitiveRootsConjecture.artin_primitive_roots.parts.ii`

Open: stated without proof.

> **Artin's Conjecture on Primitive Roots**, second half.
> Write $a = a_0 b^2$ where $a_0$ is squarefree. Under the conditions that $a$ is not a perfect
> power and $a_0\not\equiv 1\pmod{4}$ (sequence A85397 in the OEIS), the density of the set
> $S(a)$ of primes $p$ such that $a$ is a primitive root modulo $p$ is independent of $a$ and
> equals Artin's constant.

```lean
theorem artin_primitive_roots.parts.ii
    (a a_0 b : ℤ) (ha : a = a_0 * b ^ 2)
    (ha' : ∀ n m, m ≠ 1 → a ≠ n ^ m) (ha_0 : Squarefree a_0)
    (ha_0' : ¬a_0 ≡ 1 [ZMOD 4]) :
    (S a).HasDensity ArtinConstant {p | p.Prime}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean#L143).

## `ArtinPrimitiveRootsConjecture.conditional_artin_primitive_roots.parts.ii`

Solved: stated here without proof.

> **Artin's Conjecture on Primitive Roots**, second half, conditional on the Riemann hypothesis
> for the Dedekind zeta functions of the fields $\mathbb{Q}(\zeta_k, a^{1/k})$, $k$ squarefree
> [Ho67].

```lean
theorem conditional_artin_primitive_roots.parts.ii
    (a a_0 b : ℤ) (ha : a = a_0 * b ^ 2)
    (ha' : ∀ n m, m ≠ 1 → a ≠ n ^ m) (ha_0 : Squarefree a_0)
    (ha_0' : ¬a_0 ≡ 1 [ZMOD 4])
    (h : HooleyHypothesis a) :
    (S a).HasDensity ArtinConstant {p | p.Prime}
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean, line 157](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean#L157).

## `ArtinPrimitiveRootsConjecture.artin_primitive_roots.variants.part_ii_square_or_minus_one`

Proved here.

> **Artin's Conjecture on Primitive Roots**, second half, different residue version
> If $a$ is a square number or $a = −1$, then the density of the set $S(a)$ of primes
> $p$ such that $a$ is a primitive root modulo $p$ is $0$.

```lean
theorem artin_primitive_roots.variants.part_ii_square_or_minus_one
    (a : ℤ) (ha : IsSquare a ∨ a = -1) :
    (S a).HasDensity 0 {p | p.Prime}
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean, line 198](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean#L198).

## `ArtinPrimitiveRootsConjecture.artin_primitive_roots.variants.part_ii_power_squarefreePart_not_modeq_one`

Open: stated without proof.

> **Artin's Conjecture on Primitive Roots**, second half, power version
> If $a = b^m$ is a perfect odd power of a number $b$ whose squarefree part
> $b_0\not\equiv 1 \pmod{4}$, then the density of the set $S(a)$ of primes $p$ such that
> $a$ is a primitive root modulo $p$ is given by
>
> $$C\prod_{p \mid m} \frac{p(p - 2)}{p^2 - p - 1}$$
>
> ,
> where $C$ is Artin's constant.

```lean
theorem artin_primitive_roots.variants.part_ii_power_squarefreePart_not_modeq_one
    (a m b : ℕ) (ha : a = b ^ m) (hb : ∀ u v, 1 < u → b ≠ v^u) (hm₁ : 1 < m)
    (hm₂ : Odd m) (hb' : ¬ b.squarefreePart ≡ 1 [MOD 4]) :
    (S a).HasDensity (ArtinConstant * powCorrectionFactor m) {p | p.Prime}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean, line 214](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean#L214).

## `ArtinPrimitiveRootsConjecture.conditional_artin_primitive_roots.variants.part_ii_power_squarefreePart_not_modeq_one`

Solved: stated here without proof.

> **Artin's Conjecture on Primitive Roots**, second half, power version, conditional on the
> Riemann hypothesis for the Dedekind zeta functions of the fields $\mathbb{Q}(\zeta_k, a^{1/k})$,
> $k$ squarefree [Ho67].

```lean
theorem conditional_artin_primitive_roots.variants.part_ii_power_squarefreePart_not_modeq_one
    (a m b : ℕ) (ha : a = b ^ m) (hb : ∀ u v, 1 < u → b ≠ v ^ u) (hm₁ : 1 < m)
    (hm₂ : Odd m) (hb' : ¬ b.squarefreePart ≡ 1 [MOD 4])
    (h : HooleyHypothesis a) :
    (S a).HasDensity (ArtinConstant * powCorrectionFactor m) {p | p.Prime}
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean, line 226](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean#L226).

## `ArtinPrimitiveRootsConjecture.artin_primitive_roots.variants.part_ii_power_squarefreePart_modeq_one`

Open: stated without proof.

> **Artin's Conjecture on Primitive Roots**, second half, power version
> If $a = b^m$ is a perfect power of a number $b$ whose squarefree part $b_0\equiv 1 \pmod{4}$,
> then the density of the set $S(a)$ of primes $p$ such that $a$ is a primitive root modulo $p$
> is given by
>
> $$C \left(\prod_{p \mid m} \frac{p(p-2)}{(p ^ 2 - p - 1)}\right)
> \left(1 - \prod_{p \mid \gcd(b_0, m)} \frac{1}{2 - p}
> \prod_{p \mid b_0, p\nmid m} \frac{1}{(1 + p - p ^ 2)}\right),$$
>
> where $C$ is Artin's constant.

```lean
theorem artin_primitive_roots.variants.part_ii_power_squarefreePart_modeq_one
    (a m b : ℕ) (ha : a = b ^ m) (hb : ∀ u v, 1 < u → b ≠ v ^ u) (hm₁ : 1 < m)
    (hm₂ : Odd m) (hb' : b.squarefreePart ≡ 1 [MOD 4]) :
    (S a).HasDensity
      (ArtinConstant * powCorrectionFactor m * entanglementFactor b m)
      {p | p.Prime}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean, line 244](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean#L244).

## `ArtinPrimitiveRootsConjecture.conditional_artin_primitive_roots.variants.part_ii_power_squarefreePart_modeq_one`

Solved: stated here without proof.

> **Artin's Conjecture on Primitive Roots**, second half, power version, conditional on the
> Riemann hypothesis for the Dedekind zeta functions of the fields $\mathbb{Q}(\zeta_k, a^{1/k})$,
> $k$ squarefree [Ho67].

```lean
theorem conditional_artin_primitive_roots.variants.part_ii_power_squarefreePart_modeq_one
    (a m b : ℕ) (ha : a = b ^ m) (hb : ∀ u v, 1 < u → b ≠ v ^ u) (hm₁ : 1 < m)
    (hm₂ : Odd m) (hb' : b.squarefreePart ≡ 1 [MOD 4])
    (h : HooleyHypothesis a) :
    (S a).HasDensity
      (ArtinConstant * powCorrectionFactor m * entanglementFactor b m)
      {p | p.Prime}
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean, line 258](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean#L258).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ArtinPrimitiveRootsConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Artin%27s_conjecture_on_primitive_roots)
