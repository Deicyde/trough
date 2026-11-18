---
declaration: module
origin: cited
lean: KleinGordon.sineEvolution, KleinGordon.sineEvolutionTempered, KleinGordon.sineEvolutionTempered_coe, KleinGordon.cosEvolution, KleinGordon.frequencySqOperator, KleinGordon.sineEvolution_apply_eq, KleinGordon.sineEvolution_zero, KleinGordon.cosEvolution_zero
statement: formalized
proof: formalized
---

# The free evolution

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.FreeEvolution`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean): 24 declarations, 12 with a docstring.

## i. Overview

> The sine and cosine evolution of Schwartz data and its time and space derivatives.

## ii. Key results

> - `sineEvolution` : The propagation over the time `t` on Schwartz functions.
> - `sineEvolutionTempered` : The propagation over the time `t` on tempered distributions.
> - `cosEvolution` : The cosine evolution on Schwartz functions.
> - `frequencySqOperator` : The Fourier multiplier `ω²`, i.e.
> - `evolveU` : The field `u τ = C τ a + S τ b` evolved from the Cauchy data `(a, b)`.
> - `evolveV` : The velocity `v τ = C τ b - ω² S τ a` of the evolved field.

## iv. References

> None.

## A. The Klein–Gordon propagation multiplier

> - `sineEvolution` : The propagation over the time `t` on Schwartz functions.
> - `sineEvolutionTempered` : The propagation over the time `t` on tempered distributions.
>
> Lemmas: `sineEvolutionTempered_coe`.

## B. The free Klein–Gordon evolution and its group law

> - `cosEvolution` : The cosine evolution on Schwartz functions.
> - `frequencySqOperator` : The Fourier multiplier `ω²`, i.e.

## C. The free evolution

> Lemmas: `sineEvolution_apply_eq`.

## D. The free Klein–Gordon evolution as a one-parameter group

> Lemmas: `sineEvolution_zero`, `cosEvolution_zero`.

## E. The homogeneous Klein–Gordon evolution of Schwartz data

> - `evolveU` : The field `u τ = C τ a + S τ b` evolved from the Cauchy data `(a, b)`.
> - `evolveV` : The velocity `v τ = C τ b - ω² S τ a` of the evolved field.
>
> Lemmas: `hasDerivAt_sineEvolution_apply`, `hasDerivAt_cosEvolution_apply`, `hasDerivAt_evolveU`,
> `frequencySqOperator_sineEvolution`, `frequencySqOperator_cosEvolution`, `hasDerivAt_evolveV`,
> `lineDeriv_evolveU`, `lineDeriv_evolveV`, `frequencySqOperator_eq`,
> `continuous_sineEvolution_apply'` and more.

**`KleinGordon.sineEvolution`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L85).

> The propagation over the time `t` on Schwartz functions.

```lean
def sineEvolution (t μ : ℝ) : 𝓢(E, F) →L[ℂ] 𝓢(E, F)
```

**`KleinGordon.sineEvolutionTempered`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L89).

> The propagation over the time `t` on tempered distributions.

```lean
def sineEvolutionTempered (t μ : ℝ) : 𝓢'(E, F) →L[ℂ] 𝓢'(E, F)
```

**`KleinGordon.sineEvolutionTempered_coe`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L93).

> The two propagations agree on Schwartz functions.

```lean
lemma sineEvolutionTempered_coe [CompleteSpace F] (t : ℝ) {μ : ℝ} (hμ : 0 ≤ μ) (f : 𝓢(E, F)) :
    sineEvolutionTempered F t μ (f : 𝓢'(E, F)) = (sineEvolution F t μ f : 𝓢'(E, F))
```

**`KleinGordon.cosEvolution`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L105).

> The cosine evolution on Schwartz functions.

```lean
def cosEvolution (t μ : ℝ) : 𝓢(E, F) →L[ℂ] 𝓢(E, F)
```

**`KleinGordon.frequencySqOperator`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L109).

> The Fourier multiplier `ω²`, i.e. `-Δ + μ`, on Schwartz functions.

```lean
def frequencySqOperator (μ : ℝ) : 𝓢(E, F) →L[ℂ] 𝓢(E, F)
```

**`KleinGordon.sineEvolution_apply_eq`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L114).

> The pointwise Fourier integral of the sine evolution.

```lean
lemma sineEvolution_apply_eq (r : ℝ) {μ : ℝ} (hμ : 0 ≤ μ) (g : 𝓢(E, F)) (x : E) :
    sineEvolution F r μ g x = ∫ ξ : E, 𝐞 (inner ℝ ξ x) • (multiplier r μ ξ • 𝓕 g ξ)
```

**`KleinGordon.sineEvolution_zero`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L120).

```lean
lemma sineEvolution_zero (μ : ℝ) : sineEvolution (E := E) F 0 μ = 0
```

**`KleinGordon.cosEvolution_zero`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L126).

```lean
lemma cosEvolution_zero (μ : ℝ) : cosEvolution (E := E) F 0 μ = ContinuousLinearMap.id ℂ _
```

**`KleinGordon.hasDerivAt_sineEvolution_apply`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L140).

> The time derivative of the sine evolution of Schwartz data is the cosine evolution.

```lean
lemma hasDerivAt_sineEvolution_apply {μ : ℝ} (hμ : 0 ≤ μ) (b : 𝓢(E, F)) (x : E) (τ : ℝ) :
    HasDerivAt (fun r => sineEvolution F r μ b x) (cosEvolution F τ μ b x) τ
```

**`KleinGordon.hasDerivAt_cosEvolution_apply`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L155).

> The time derivative of the cosine evolution of Schwartz data.

```lean
lemma hasDerivAt_cosEvolution_apply {μ : ℝ} (hμ : 0 ≤ μ) (a : 𝓢(E, F)) (x : E) (τ : ℝ) :
    HasDerivAt (fun r => cosEvolution F r μ a x)
      (-(frequencySqOperator F μ (sineEvolution F τ μ a) x)) τ
```

**`KleinGordon.evolveU`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L204).

> The field `u τ = C τ a + S τ b` evolved from the Cauchy data `(a, b)`.

```lean
def evolveU (μ τ : ℝ) (a b : 𝓢(E, F)) : 𝓢(E, F)
```

**`KleinGordon.evolveV`**, a def, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L208).

> The velocity `v τ = C τ b - ω² S τ a` of the evolved field.

```lean
def evolveV (μ τ : ℝ) (a b : 𝓢(E, F)) : 𝓢(E, F)
```

**`KleinGordon.hasDerivAt_evolveU`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L211).

```lean
lemma hasDerivAt_evolveU {μ : ℝ} (hμ : 0 ≤ μ) (a b : 𝓢(E, F)) (x : E) (τ : ℝ) :
    HasDerivAt (fun r => evolveU μ r a b x) (evolveV μ τ a b x) τ
```

**`KleinGordon.frequencySqOperator_sineEvolution`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L219).

```lean
lemma frequencySqOperator_sineEvolution {μ : ℝ} (hμ : 0 ≤ μ) (r : ℝ) (a : 𝓢(E, F)) :
    frequencySqOperator F μ (sineEvolution F r μ a) =
      sineEvolution F r μ (frequencySqOperator F μ a)
```

**`KleinGordon.frequencySqOperator_cosEvolution`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L224).

```lean
lemma frequencySqOperator_cosEvolution {μ : ℝ} (hμ : 0 ≤ μ) (r : ℝ) (a : 𝓢(E, F)) :
    frequencySqOperator F μ (cosEvolution F r μ a) =
      cosEvolution F r μ (frequencySqOperator F μ a)
```

**`KleinGordon.hasDerivAt_evolveV`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L230).

> The velocity has the time derivative `-ω² u`.

```lean
lemma hasDerivAt_evolveV {μ : ℝ} (hμ : 0 ≤ μ) (a b : 𝓢(E, F)) (x : E) (τ : ℝ) :
    HasDerivAt (fun r => evolveV μ r a b x)
      (-(frequencySqOperator F μ (evolveU μ τ a b) x)) τ
```

**`KleinGordon.lineDeriv_evolveU`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L245).

```lean
lemma lineDeriv_evolveU {μ : ℝ} (hμ : 0 ≤ μ) (m : E) (τ : ℝ) (a b : 𝓢(E, F)) :
    ∂_{m} (evolveU μ τ a b) = evolveU μ τ (∂_{m} a) (∂_{m} b)
```

**`KleinGordon.lineDeriv_evolveV`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L254).

```lean
lemma lineDeriv_evolveV {μ : ℝ} (hμ : 0 ≤ μ) (m : E) (τ : ℝ) (a b : 𝓢(E, F)) :
    ∂_{m} (evolveV μ τ a b) = evolveV μ τ (∂_{m} a) (∂_{m} b)
```

**`KleinGordon.frequencySqOperator_eq`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L266).

> The operator `ω²` is `-Δ + μ` on Schwartz functions.

```lean
lemma frequencySqOperator_eq (μ : ℝ) (f : 𝓢(E, F)) :
    frequencySqOperator F μ f = -(Δ f) + μ • f
```

**`KleinGordon.continuous_sineEvolution_apply'`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L287).

```lean
lemma continuous_sineEvolution_apply' {μ : ℝ} (hμ : 0 ≤ μ) (a : 𝓢(E, F)) :
    Continuous fun p : ℝ × E => sineEvolution F p.1 μ a p.2
```

**`KleinGordon.continuous_cosEvolution_apply`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L297).

```lean
lemma continuous_cosEvolution_apply {μ : ℝ} (hμ : 0 ≤ μ) (a : 𝓢(E, F)) :
    Continuous fun p : ℝ × E => cosEvolution F p.1 μ a p.2
```

**`KleinGordon.continuous_frequencySqSine_apply`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L309).

```lean
lemma continuous_frequencySqSine_apply {μ : ℝ} (hμ : 0 ≤ μ) (a : 𝓢(E, F)) :
    Continuous fun p : ℝ × E => frequencySqOperator F μ (sineEvolution F p.1 μ a) p.2
```

**`KleinGordon.continuous_evolveU_apply`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L335).

```lean
lemma continuous_evolveU_apply {μ : ℝ} (hμ : 0 ≤ μ) (a b : 𝓢(E, F)) :
    Continuous fun p : ℝ × E => evolveU μ p.1 a b p.2
```

**`KleinGordon.continuous_evolveV_apply`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean#L339).

```lean
lemma continuous_evolveV_apply {μ : ℝ} (hμ : 0 ≤ μ) (a b : 𝓢(E, F)) :
    Continuous fun p : ℝ × E => evolveV μ p.1 a b p.2
```

## Depends on

- [The propagation multiplier](multiplier.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FreeEvolution.lean)
