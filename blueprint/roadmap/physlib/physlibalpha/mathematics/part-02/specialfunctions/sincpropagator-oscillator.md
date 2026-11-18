---
declaration: module
origin: cited
lean: SincPropagator.generator, SincPropagator.generator_sq, SincPropagator.generator_pow_even, SincPropagator.generator_pow_odd, SincPropagator.hasSum_sincPropagator, SincPropagator.hasSum_exp_generator, SincPropagator.evolutionMatrix, SincPropagator.evolutionMatrix_eq
statement: formalized
proof: formalized
---

# The harmonic oscillator

The module `PhyslibAlpha.Mathematics.SpecialFunctions.SincPropagator.Oscillator`, [PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean): 27 declarations, 13 with a docstring.

## i. Overview

> The matrix exponential of the generator and the Duhamel formula for the oscillator with a source.

## ii. Key results

> - `generator` : The generator `[[0, 1], [-ω², 0]]` of the free evolution of Cauchy data at frequency
>   `ω`.
> - `evolutionMatrix` : The evolution matrix of the Cauchy data at frequency `ω` over the time `t`.
> - `duhamelOsc` : The retarded solution of `u'' + ω² u = G` with zero data at the time `a`.
> - `duhamelOscCos` : The derivative of `duhamelOsc`: the same integral with the cosine kernel.

## iv. References

> None.

## A. The exponential of the Klein–Gordon generator

> - `generator` : The generator `[[0, 1], [-ω², 0]]` of the free evolution of Cauchy data at frequency
>   `ω`.
> - `evolutionMatrix` : The evolution matrix of the Cauchy data at frequency `ω` over the time `t`.
>
> Lemmas: `generator_sq`, `generator_pow_even`, `generator_pow_odd`, `hasSum_sincPropagator`,
> `hasSum_exp_generator`, `evolutionMatrix_eq`, `exp_generator`, `evolutionMatrix_add`,
> `sincPropagator_add`, `cos_mul_add`.

## B. Duhamel's formula for the harmonic oscillator

> - `duhamelOsc` : The retarded solution of `u'' + ω² u = G` with zero data at the time `a`.
> - `duhamelOscCos` : The derivative of `duhamelOsc`: the same integral with the cosine kernel.
>
> Lemmas: `sincPropagator_sub_split`, `cos_sub_split`, `cos_sq_add_sq_mul`,
> `continuous_sincPropagator_smul`, `continuous_cos_smul`, `duhamelOsc_eq`, `duhamelOscCos_eq`,
> `hasDerivAt_cosIntegral`, `hasDerivAt_sinIntegral`, `hasDerivAt_duhamelOsc` and more.

**`SincPropagator.generator`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L70).

> The generator `[[0, 1], [-ω², 0]]` of the free evolution of Cauchy data at frequency `ω`.

```lean
def generator (ω : ℝ) : Matrix (Fin 2) (Fin 2) ℂ
```

**`SincPropagator.generator_sq`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L72).

```lean
lemma generator_sq (ω : ℝ) : generator ω ^ 2 = (-((ω ^ 2 : ℝ) : ℂ)) • (1 : Matrix (Fin 2) (Fin 2)
    ℂ)
```

**`SincPropagator.generator_pow_even`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L77).

```lean
lemma generator_pow_even (ω : ℝ) (n : ℕ) :
    generator ω ^ (2 * n) = (-((ω ^ 2 : ℝ) : ℂ)) ^ n • (1 : Matrix (Fin 2) (Fin 2) ℂ)
```

**`SincPropagator.generator_pow_odd`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L81).

```lean
lemma generator_pow_odd (ω : ℝ) (n : ℕ) :
    generator ω ^ (2 * n + 1) = (-((ω ^ 2 : ℝ) : ℂ)) ^ n • generator ω
```

**`SincPropagator.hasSum_sincPropagator`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L86).

> The series of `sincPropagator`, as a convergent sum.

```lean
lemma hasSum_sincPropagator (t ω : ℝ) :
    HasSum (fun n : ℕ => (-1) ^ n * t ^ (2 * n + 1) * ω ^ (2 * n) / (2 * n + 1)!)
      (sincPropagator t ω)
```

**`SincPropagator.hasSum_exp_generator`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L103).

```lean
lemma hasSum_exp_generator (t ω : ℝ) :
    HasSum (fun n : ℕ => ((n ! : ℂ)⁻¹) • ((t : ℂ) • generator ω) ^ n)
      (((cos (ω * t) : ℝ) : ℂ) • (1 : Matrix (Fin 2) (Fin 2) ℂ) +
        ((sincPropagator t ω : ℝ) : ℂ) • generator ω)
```

**`SincPropagator.evolutionMatrix`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L126).

> The evolution matrix of the Cauchy data at frequency `ω` over the time `t`.

```lean
def evolutionMatrix (t ω : ℝ) : Matrix (Fin 2) (Fin 2) ℂ
```

**`SincPropagator.evolutionMatrix_eq`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L130).

```lean
lemma evolutionMatrix_eq (t ω : ℝ) :
    evolutionMatrix t ω = ((cos (ω * t) : ℝ) : ℂ) • (1 : Matrix (Fin 2) (Fin 2) ℂ) +
      ((sincPropagator t ω : ℝ) : ℂ) • generator ω
```

**`SincPropagator.exp_generator`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L138).

> The exponential of the generator is the evolution matrix.

```lean
lemma exp_generator (t ω : ℝ) :
    exp ((t : ℂ) • generator ω) = evolutionMatrix t ω
```

**`SincPropagator.evolutionMatrix_add`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L148).

> The group law of the evolution matrix, from `exp (A + B) = exp A * exp B` for commuting
> `A` and `B`.

```lean
lemma evolutionMatrix_add (s t ω : ℝ) :
    evolutionMatrix (s + t) ω = evolutionMatrix s ω * evolutionMatrix t ω
```

**`Real.sincPropagator_add`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L160).

> The addition law of `sincPropagator`, read off from the entry `(0, 1)` of the group law.

```lean
lemma sincPropagator_add (s t ω : ℝ) :
    sincPropagator (s + t) ω =
      cos (ω * s) * sincPropagator t ω + sincPropagator s ω * cos (ω * t)
```

**`Real.cos_mul_add`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L168).

> The addition law of the cosine, read off from the entry `(0, 0)` of the group law.

```lean
lemma cos_mul_add (s t ω : ℝ) :
    cos (ω * (s + t)) =
      cos (ω * s) * cos (ω * t) - ω ^ 2 * sincPropagator s ω * sincPropagator t ω
```

**`Real.duhamelOsc`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L183).

> The retarded solution of `u'' + ω² u = G` with zero data at the time `a`.

```lean
def duhamelOsc (ω a : ℝ) (G : ℝ → V) (t : ℝ) : V
```

**`Real.duhamelOscCos`**, a def, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L187).

> The derivative of `duhamelOsc`: the same integral with the cosine kernel.

```lean
def duhamelOscCos (ω a : ℝ) (G : ℝ → V) (t : ℝ) : V
```

**`Real.sincPropagator_sub_split`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L190).

```lean
lemma sincPropagator_sub_split (ω t s : ℝ) :
    sincPropagator (t - s) ω =
      sincPropagator t ω * cos (ω * s) - cos (ω * t) * sincPropagator s ω
```

**`Real.cos_sub_split`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L198).

```lean
lemma cos_sub_split (ω t s : ℝ) :
    cos (ω * (t - s)) =
      cos (ω * t) * cos (ω * s) + ω ^ 2 * sincPropagator t ω * sincPropagator s ω
```

**`Real.cos_sq_add_sq_mul`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L206).

```lean
lemma cos_sq_add_sq_mul (ω t : ℝ) :
    cos (ω * t) ^ 2 + ω ^ 2 * sincPropagator t ω ^ 2 = 1
```

**`Real.continuous_sincPropagator_smul`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L220).

```lean
lemma continuous_sincPropagator_smul : Continuous fun s => sincPropagator s ω • G s
```

**`Real.continuous_cos_smul`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L224).

```lean
lemma continuous_cos_smul : Continuous fun s => cos (ω * s) • G s
```

**`Real.duhamelOsc_eq`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L227).

```lean
lemma duhamelOsc_eq (t : ℝ) :
    duhamelOsc ω a G t =
      sincPropagator t ω • (∫ s in a..t, cos (ω * s) • G s) -
        cos (ω * t) • (∫ s in a..t, sincPropagator s ω • G s)
```

**`Real.duhamelOscCos_eq`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L245).

```lean
lemma duhamelOscCos_eq (t : ℝ) :
    duhamelOscCos ω a G t =
      cos (ω * t) • (∫ s in a..t, cos (ω * s) • G s) +
        (ω ^ 2 * sincPropagator t ω) • (∫ s in a..t, sincPropagator s ω • G s)
```

**`Real.hasDerivAt_cosIntegral`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L263).

```lean
lemma hasDerivAt_cosIntegral (t : ℝ) :
    HasDerivAt (fun u => ∫ s in a..u, cos (ω * s) • G s) (cos (ω * t) • G t) t
```

**`Real.hasDerivAt_sinIntegral`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L267).

```lean
lemma hasDerivAt_sinIntegral (t : ℝ) :
    HasDerivAt (fun u => ∫ s in a..u, sincPropagator s ω • G s) (sincPropagator t ω • G t) t
```

**`Real.hasDerivAt_duhamelOsc`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L272).

> The derivative of the retarded oscillator solution is the cosine Duhamel integral.

```lean
lemma hasDerivAt_duhamelOsc (t : ℝ) :
    HasDerivAt (duhamelOsc ω a G) (duhamelOscCos ω a G t) t
```

**`Real.hasDerivAt_duhamelOscCos`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L288).

> The second derivative: the force minus `ω²` times the solution.

```lean
lemma hasDerivAt_duhamelOscCos (t : ℝ) :
    HasDerivAt (duhamelOscCos ω a G) (G t - ω ^ 2 • duhamelOsc ω a G t) t
```

**`Real.duhamelOsc_operator`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L309).

> The oscillator Green kernel recovers a twice differentiable field up to its initial data.

```lean
lemma duhamelOsc_operator {g g' g'' : ℝ → V}
    (hg : ∀ s, HasDerivAt g (g' s) s) (hg' : ∀ s, HasDerivAt g' (g'' s) s)
    (hg'' : Continuous g'') (ω a t : ℝ) :
    duhamelOsc ω a (fun s => g'' s + ω ^ 2 • g s) t =
      g t - (cos (ω * (t - a)) • g a + sincPropagator (t - a) ω • g' a)
```

**`Real.duhamelOsc_operator_of_initial_zero`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean#L338).

> The retarded oscillator Green operator is a left inverse on fields with zero initial data.

```lean
lemma duhamelOsc_operator_of_initial_zero {g g' g'' : ℝ → V}
    (hg : ∀ s, HasDerivAt g (g' s) s) (hg' : ∀ s, HasDerivAt g' (g'' s) s)
    (hg'' : Continuous g'') (ω a t : ℝ) (hga : g a = 0) (hg'a : g' a = 0) :
    duhamelOsc ω a (fun s => g'' s + ω ^ 2 • g s) t = g t
```

## Depends on

- [The sine propagation function `t ↦ sin (ω t) / ω`](sincpropagator-basic.md)

## Sources

- [PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Oscillator.lean)
