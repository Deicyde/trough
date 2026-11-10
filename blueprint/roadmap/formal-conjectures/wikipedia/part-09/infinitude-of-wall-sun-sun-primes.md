---
declaration: lemma
origin: cited
lean: QuadraticAlgebra.discr_rat_of_modEq_one, QuadraticAlgebra.discr_rat_of_not_modEq_one, Algebra.exists_quadraticAlgebra_of_isQuadraticExtension, Algebra.isQuadraticExtension_iff_exists_quadraticAlgebra, NumberField.exists_quadraticAlgebra_of_isQuadraticExtension, NumberField.isQuadraticExtension_iff_exists_quadraticAlgebra, NumberField.isFundamentalDiscr_iff_exists_discr_quadraticAlgebra, NumberField.isFundamentalDiscr_iff_exists_discr_numberField, WallSunSun.exists_isWallSunSunPrime, WallSunSun.infinite_isWallSunSunPrime, WallSunSun.infinite_isWallSunSunPrime_of_disc_eq
statement: formalized
---

# Infinitude of Wall–Sun–Sun primes

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Wall%E2%80%93Sun%E2%80%93Sun_prime)
> - [EJ10] A.-S. Elsenhans and J. Jahnel, *The Fibonacci sequence modulo $p^2$ – An investigation by
>   computer for $p < 10^{14}$*, [arXiv:1006.0824](https://arxiv.org/abs/1006.0824)

*Quoted from [FormalConjectures/Wikipedia/WallSunSun.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WallSunSun.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 11 research or textbook statements: 3 open and 8 textbook results. It also has 1 test statement, counted here but not shown.

## `QuadraticAlgebra.discr_rat_of_modEq_one`

Textbook result, stated without proof.

> The discriminant of `ℚ[√d]` for `d ≥ 2` squarefree congruent to 1 mod 4 is `d`.

```lean
lemma discr_rat_of_modEq_one (hd₄ : d ≡ 1 [ZMOD 4]) : discr (QuadraticAlgebra ℚ d 0) = d
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WallSunSun.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WallSunSun.lean#L39).

## `QuadraticAlgebra.discr_rat_of_not_modEq_one`

Textbook result, stated without proof.

> The discriminant of `ℚ[√d]` for `d ≥ 2` squarefree not congruent to 1 mod 4 is `4 * d`.

```lean
lemma discr_rat_of_not_modEq_one (hd₄ : ¬ d ≡ 1 [ZMOD 4]) :
    discr (QuadraticAlgebra ℚ d 0) = 4 * d
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WallSunSun.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WallSunSun.lean#L44).

## `Algebra.exists_quadraticAlgebra_of_isQuadraticExtension`

Textbook result, stated without proof.

> A quadratic algebra `L` over a field `K` is isomorphic to the explicit quadratic algebra
> `QuadraticAlgebra K a b` for some `a b : K`.

```lean
lemma exists_quadraticAlgebra_of_isQuadraticExtension [IsQuadraticExtension K L] :
    ∃ a b, Nonempty (L ≃ₐ[K] QuadraticAlgebra K a b)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WallSunSun.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WallSunSun.lean#L57).

## `Algebra.isQuadraticExtension_iff_exists_quadraticAlgebra`

Textbook result, stated without proof.

> An algebra `L` is quadratic over a field `K` iff it is isomorphic to the explicit quadratic
> algebra `QuadraticAlgebra K a b` for some `a b : K`.

```lean
lemma isQuadraticExtension_iff_exists_quadraticAlgebra :
    IsQuadraticExtension K L ↔ ∃ a b, Nonempty (L ≃ₐ[K] QuadraticAlgebra K a b)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WallSunSun.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WallSunSun.lean#L64).

## `NumberField.exists_quadraticAlgebra_of_isQuadraticExtension`

Textbook result, stated without proof.

> A quadratic number field `K` is isomorphic to the explicit quadratic field
> `QuadraticAlgebra ℚ d 0` for some squarefree `d : ℤ` not equal to 1.

```lean
lemma exists_quadraticAlgebra_of_isQuadraticExtension [IsQuadraticExtension ℚ K] :
    ∃ d ≠ (1 : ℤ), Squarefree d ∧ Nonempty (K ≃+* QuadraticAlgebra ℚ d 0)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WallSunSun.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WallSunSun.lean#L78).

## `NumberField.isQuadraticExtension_iff_exists_quadraticAlgebra`

Textbook result, stated without proof.

> A number field `K` is quadratic iff it is isomorphic to the explicit quadratic field
> `QuadraticAlgebra ℚ d 0` for some squarefree `d : ℤ` not equal to 1.

```lean
lemma isQuadraticExtension_iff_exists_quadraticAlgebra :
    IsQuadraticExtension ℚ K ↔
      ∃ d ≠ (1 : ℤ), Squarefree d ∧ Nonempty (K ≃+* QuadraticAlgebra ℚ d 0)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WallSunSun.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WallSunSun.lean#L85).

## `NumberField.isFundamentalDiscr_iff_exists_discr_quadraticAlgebra`

Textbook result, proved here.

> An integer `D` is a fundamental discriminant iff it is the discriminant of the explicit
> quadratic field `QuadraticAlgebra ℚ d 0` for some squarefree `d : ℤ` not equal to 1.

```lean
lemma isFundamentalDiscr_iff_exists_discr_quadraticAlgebra {D : ℤ} :
    IsFundamentalDiscr D ↔ ∃ (d : ℤ) (_ : Fact <| d ≠ 1) (_ : Fact <| Squarefree d),
      discr (QuadraticAlgebra ℚ d 0) = D
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WallSunSun.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WallSunSun.lean#L94).

## `NumberField.isFundamentalDiscr_iff_exists_discr_numberField`

Textbook result, proved here.

> An integer `D` is a fundamental discriminant iff it is the discriminant of some number field.

```lean
lemma isFundamentalDiscr_iff_exists_discr_numberField {D : ℤ} :
    IsFundamentalDiscr D ↔
      ∃ (K : Type) (_ : Field K) (_ : NumberField K), IsQuadraticExtension ℚ K ∧ discr K = D
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WallSunSun.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WallSunSun.lean#L111).

## `WallSunSun.exists_isWallSunSunPrime`

Open: stated without proof.

> A prime $p$ is a Wall–Sun–Sun prime if and only if $L_p \equiv 1 \pmod{p^2}$, where $L_p$ is the
> $p$-th Lucas number. It is conjectured that there is at least one Wall–Sun–Sun prime.

```lean
theorem exists_isWallSunSunPrime : ∃ p, IsWallSunSunPrime p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WallSunSun.lean, line 135](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WallSunSun.lean#L135).

## `WallSunSun.infinite_isWallSunSunPrime`

Open: stated without proof.

> A prime $p$ is a Wall–Sun–Sun prime if and only if $L_p \equiv 1 \pmod{p^2}$, where $L_p$ is the
> $p$-th Lucas number. It is conjectured that there are infinitely many Wall-Sun-Sun primes.

```lean
theorem infinite_isWallSunSunPrime : {p : ℕ | IsWallSunSunPrime p}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WallSunSun.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WallSunSun.lean#L143).

## `WallSunSun.infinite_isWallSunSunPrime_of_disc_eq`

Open: stated without proof.

> Let $K$ be a real quadratic field of discriminant $D$ and let $\varepsilon$ be a fundamental unit
> of $K$. Following [EJ10, Remark 2.2.8], an odd prime $p \nmid D$ is a Wall–Sun–Sun prime for $K$
> if, in $\mathcal{O}_K$, $\varepsilon^{p-1} \equiv 1 \pmod{p^2}$ when
> $\left(\tfrac{D}{p}\right) = 1$, and $\varepsilon^{2p+2} \equiv 1 \pmod{p^2}$ when
> $\left(\tfrac{D}{p}\right) = -1$. Both exponents are even, so the condition does not depend on the
> choice of $\varepsilon$, and it is equivalent to asking the same congruence for every unit of $K$.
> For $K = \mathbb{Q}(\sqrt{5})$ and $\varepsilon = \frac{1 + \sqrt{5}}{2}$ these are the classical
> Wall–Sun–Sun primes other than $2$ and $5$ [EJ10, Proposition 2.2.6].
>
> It is conjectured that for every fundamental discriminant $D \neq 1$ there are infinitely many
> Wall–Sun–Sun primes with discriminant $D$ (Wikipedia; [EJ10, §4.1] gives the heuristic for
> $\mathbb{Q}(\sqrt{5})$). It is stated here for $D > 0$ only. Wikipedia's sentence also covers
> $D < 0$, but [EJ10] gives the definition above only for real quadratic fields, and its literal
> extension to imaginary quadratic fields is degenerate: there every unit is a root of unity of
> order dividing $4$ or $6$, and that order divides the relevant exponent $p - 1$ or $2p + 2$ for
> every odd prime $p \nmid D$.

```lean
theorem infinite_isWallSunSunPrime_of_disc_eq {K : Type*} [Field K] [NumberField K]
    [IsQuadraticExtension ℚ K] [IsTotallyReal K] {D : ℤ} (hD : discr K = D) :
    {p : ℕ | p.Prime ∧ Odd p ∧ ¬ (p : ℤ) ∣ D ∧ ∀ ε : (𝓞 K)ˣ,
      (p : 𝓞 K) ^ 2 ∣ (ε : 𝓞 K) ^ (if J(D | p) = 1 then p - 1 else 2 * p + 2) - 1}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WallSunSun.lean, line 214](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WallSunSun.lean#L214).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/WallSunSun.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WallSunSun.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Wall%E2%80%93Sun%E2%80%93Sun_prime)
