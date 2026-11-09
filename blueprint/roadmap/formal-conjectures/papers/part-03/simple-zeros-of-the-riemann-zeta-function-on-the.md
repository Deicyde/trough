---
declaration: theorem
origin: cited
lean: riemannZeta.simple_prop_two_thirds, riemannZeta.distinct_prop_five_sixths, riemannZeta.simple_prop_montgomeryTaylor, riemannZeta.distinct_prop_montgomeryTaylor, riemannZeta.simple_prop_lt, riemannZeta.simple_prop_one_hundred, riemannZeta.distinct_prop_lt, riemannZeta.distinct_prop_one_hundred, DirichletCharacter.simple_prop_two_thirds, DirichletCharacter.distinct_prop_five_sixths, DirichletCharacter.simple_prop_montgomeryTaylor, DirichletCharacter.distinct_prop_montgomeryTaylor, DirichletCharacter.simple_prop_lt, DirichletCharacter.simple_prop_one_hundred, DirichletCharacter.distinct_prop_lt, DirichletCharacter.distinct_prop_one_hundred
statement: formalized
---

# Simple zeros of the Riemann zeta function on the critical line

> *References:*
> - [Cl26] Claude (Anthropic), *More than two thirds of the zeros of the Riemann zeta function are
>   simple and on the critical line*, August 2026.
>   [pdf](https://www-cdn.anthropic.com/95c246936988e43127bc6b2ceb7077c1dad2d68e.pdf),
>   [Lean formalisation](https://github.com/anthropics/zeta-23-lean).
> - [Wikipedia](https://en.wikipedia.org/wiki/Riemann_hypothesis#Zeros_on_the_critical_line)
>
> For a nontrivial zero `ρ = β + iγ` of `ζ` (or of a Dirichlet `L`-function) with multiplicity
> `m_ρ`, and `0 ≤ T₁ < T₂`, write
> - `N(T₁, T₂) = ∑_{T₁ < γ ≤ T₂} m_ρ` for the zeros counted with multiplicity,
> - `N_d(T₁, T₂) = #{ρ : T₁ < γ ≤ T₂}` for the distinct zeros, and
> - `Ns(T₁, T₂) = #{ρ : T₁ < γ ≤ T₂, β = 1/2, m_ρ = 1}` for the simple zeros on the critical line.
>
> [Cl26, Theorem A] proves unconditionally that `Ns(T, 2T) ≥ (2/3 - o(1)) N(T, 2T)` and
> `N_d(T, 2T) ≥ (5/6 - o(1)) N(T, 2T)`, improving to `2 - c_MT⁻¹ = 0.6725…` and
> `(3 - c_MT⁻¹) / 2 = 0.8362…` with the Montgomery–Taylor window, where
> `c_MT⁻¹ = 1/2 + cot(1/√2)/√2`; [Cl26, Theorem B] is the same for `L(s, χ)`, `χ` primitive.

*Quoted from [FormalConjectures/Paper/RiemannZetaZeros.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 16 research or textbook statements: 8 open and 8 solved.

## `riemannZeta.simple_prop_two_thirds`

Solved: stated here; a Lean proof is at [https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/FinalMult.lean#L350](https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/FinalMult.lean#L350).

> At least two thirds of the nontrivial zeros of `ζ`, counted with
> multiplicity, are simple and on the critical line [Cl26, Theorem A (i)].

```lean
theorem simple_prop_two_thirds : ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ T > 0, (2 / 3 - o T) * N riemannZeta T (2 * T) ≤ Ns riemannZeta T (2 * T)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L82).

## `riemannZeta.distinct_prop_five_sixths`

Solved: stated here; a Lean proof is at [https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/FinalMult.lean#L358](https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/FinalMult.lean#L358).

> At least five sixths of the nontrivial zeros of `ζ`, counted with
> multiplicity, are distinct [Cl26, Theorem A (ii)].

```lean
theorem distinct_prop_five_sixths : ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ T > 0, (5 / 6 - o T) * N riemannZeta T (2 * T) ≤ Nd riemannZeta T (2 * T)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L91).

## `riemannZeta.simple_prop_montgomeryTaylor`

Solved: stated here; a Lean proof is at [https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/ThmD/Mult.lean#L435](https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/ThmD/Mult.lean#L435).

> The proportion of simple zeros of `ζ` on the critical line is at least
> `2 - c_MT⁻¹ = 0.6725…`. [Cl26, Theorem A]

```lean
theorem simple_prop_montgomeryTaylor : ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ T > 0, (2 - montgomeryTaylorConst⁻¹ - o T) * N riemannZeta T (2 * T) ≤
      Ns riemannZeta T (2 * T)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L100).

## `riemannZeta.distinct_prop_montgomeryTaylor`

Solved: stated here; a Lean proof is at [https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/ThmD/Mult.lean#L449](https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/ThmD/Mult.lean#L449).

> The proportion of distinct zeros of `ζ` is at least `(3 - c_MT⁻¹) / 2 = 0.8362…`,
> [Cl26, Theorem A].

```lean
theorem distinct_prop_montgomeryTaylor : ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ T > 0, ((3 - montgomeryTaylorConst⁻¹) / 2 - o T) * N riemannZeta T (2 * T) ≤
      Nd riemannZeta T (2 * T)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L110).

## `riemannZeta.simple_prop_lt`

Open: stated without proof.

> Is the proportion of simple zeros of `ζ` on the critical line unconditionally larger than
> the Montgomery–Taylor bound `2 - c_MT⁻¹ = 0.6725…`? [Cl26, §7.2] puts the ceiling of its
> method at about `0.682`.

```lean
theorem simple_prop_lt : ∃ c > 2 - montgomeryTaylorConst⁻¹, ∃ o : ℝ → ℝ,
    o =o[atTop] (1 : ℝ → ℝ) ∧
      ∀ T > 0, (c - o T) * N riemannZeta T (2 * T) ≤ Ns riemannZeta T (2 * T)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L119).

## `riemannZeta.simple_prop_one_hundred`

Open: stated without proof.

> Almost all nontrivial zeros of `ζ` are simple and on the critical line.

```lean
theorem simple_prop_one_hundred : ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ T > 0, (1 - o T) * N riemannZeta T (2 * T) ≤ Ns riemannZeta T (2 * T)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L126).

## `riemannZeta.distinct_prop_lt`

Open: stated without proof.

> Is the proportion of distinct zeros of `ζ` unconditionally larger than the Montgomery–Taylor
> bound `(3 - c_MT⁻¹) / 2 = 0.8362…`?

```lean
theorem distinct_prop_lt : ∃ c > (3 - montgomeryTaylorConst⁻¹) / 2, ∃ o : ℝ → ℝ,
    o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ T > 0, (c - o T) * N riemannZeta T (2 * T) ≤ Nd riemannZeta T (2 * T)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L133).

## `riemannZeta.distinct_prop_one_hundred`

Open: stated without proof.

> Almost all nontrivial zeros of `ζ` are simple.

```lean
theorem distinct_prop_one_hundred : ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ T > 0, (1 - o T) * N riemannZeta T (2 * T) ≤ Nd riemannZeta T (2 * T)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 140](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L140).

## `DirichletCharacter.simple_prop_two_thirds`

Solved: stated here; a Lean proof is at [https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/ThmE/Mult.lean#L324](https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/ThmE/Mult.lean#L324).

> At least two thirds of the nontrivial zeros of `L(s, χ)`, `χ` primitive,
> counted with multiplicity, are simple and on the critical line, [Cl26, Theorem B].

```lean
theorem simple_prop_two_thirds (hχ : χ.IsPrimitive) : ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ T > 0, (2 / 3 - o T) * N (LFunction χ) T (2 * T) ≤ Ns (LFunction χ) T (2 * T)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 155](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L155).

## `DirichletCharacter.distinct_prop_five_sixths`

Solved: stated here; a Lean proof is at [https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/ThmE/Mult.lean#L333](https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/ThmE/Mult.lean#L333).

> At least five sixths of the nontrivial zeros of `L(s, χ)`, `χ` primitive,
> counted with multiplicity, are distinct, [Cl26, Theorem B].

```lean
theorem distinct_prop_five_sixths (hχ : χ.IsPrimitive) : ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ T > 0, (5 / 6 - o T) * N (LFunction χ) T (2 * T) ≤ Nd (LFunction χ) T (2 * T)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 164](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L164).

## `DirichletCharacter.simple_prop_montgomeryTaylor`

Solved: stated here; a Lean proof is at [https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/ThmDE/Mult.lean#L429](https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/ThmDE/Mult.lean#L429).

> The proportion of simple zeros of `L(s, χ)`, `χ` primitive, on the critical line is at
> least `2 - c_MT⁻¹ = 0.6725…`, [Cl26, Theorem B].

```lean
theorem simple_prop_montgomeryTaylor (hχ : χ.IsPrimitive) :
    ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ T > 0, (2 - montgomeryTaylorConst⁻¹ - o T) * N (LFunction χ) T (2 * T) ≤
      Ns (LFunction χ) T (2 * T)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 173](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L173).

## `DirichletCharacter.distinct_prop_montgomeryTaylor`

Solved: stated here; a Lean proof is at [https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/ThmDE/Mult.lean#L437](https://github.com/anthropics/zeta-23-lean/blob/v1.0/Zeta23/ThmDE/Mult.lean#L437).

> The proportion of distinct zeros of `L(s, χ)`, `χ` primitive, is at least
> `(3 - c_MT⁻¹) / 2 = 0.8362…`, [Cl26, Theorem B].

```lean
theorem distinct_prop_montgomeryTaylor (hχ : χ.IsPrimitive) :
    ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ T > 0, ((3 - montgomeryTaylorConst⁻¹) / 2 - o T) * N (LFunction χ) T (2 * T) ≤
      Nd (LFunction χ) T (2 * T)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 184](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L184).

## `DirichletCharacter.simple_prop_lt`

Open: stated without proof.

> Is the proportion of simple zeros of `L(s, χ)`, `χ` primitive, on the critical line
> unconditionally larger than the Montgomery–Taylor bound `2 - c_MT⁻¹ = 0.6725…`?

```lean
theorem simple_prop_lt (hχ : χ.IsPrimitive) : ∃ c > 2 - montgomeryTaylorConst⁻¹, ∃ o : ℝ → ℝ,
    o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ T > 0, (c - o T) * N (LFunction χ) T (2 * T) ≤ Ns (LFunction χ) T (2 * T)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 193](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L193).

## `DirichletCharacter.simple_prop_one_hundred`

Open: stated without proof.

> Almost all nontrivial zeros of `L(s, χ)`, `χ` primitive, are simple and on the critical
> line.

```lean
theorem simple_prop_one_hundred (hχ : χ.IsPrimitive) : ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ T > 0, (1 - o T) * N (LFunction χ) T (2 * T) ≤ Ns (LFunction χ) T (2 * T)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 201](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L201).

## `DirichletCharacter.distinct_prop_lt`

Open: stated without proof.

> Is the proportion of distinct zeros of `L(s, χ)`, `χ` primitive, unconditionally larger than
> the Montgomery–Taylor bound `(3 - c_MT⁻¹) / 2 = 0.8362…`?

```lean
theorem distinct_prop_lt (hχ : χ.IsPrimitive) : ∃ c > (3 - montgomeryTaylorConst⁻¹) / 2,
    ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧
      ∀ T > 0, (c - o T) * N (LFunction χ) T (2 * T) ≤ Nd (LFunction χ) T (2 * T)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 208](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L208).

## `DirichletCharacter.distinct_prop_one_hundred`

Open: stated without proof.

> Almost all nontrivial zeros of `L(s, χ)`, `χ` primitive, are simple.

```lean
theorem distinct_prop_one_hundred (hχ : χ.IsPrimitive) : ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ T > 0, (1 - o T) * N (LFunction χ) T (2 * T) ≤ Nd (LFunction χ) T (2 * T)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaZeros.lean, line 215](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean#L215).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/RiemannZetaZeros.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaZeros.lean)
- [pdf](https://www-cdn.anthropic.com/95c246936988e43127bc6b2ceb7077c1dad2d68e.pdf)
