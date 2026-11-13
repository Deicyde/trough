---
declaration: module
origin: cited
lean: ProbabilisticTheory.spectralFunctional, ProbabilisticTheory.spectralFunctionalCc, ProbabilisticTheory.spectralMeasure, ProbabilisticTheory.spectralMeasure_isFiniteMeasure, ProbabilisticTheory.spectralFunctional_one, ProbabilisticTheory.spectralMeasure_isProbabilityMeasure, ProbabilisticTheory.spectralMeasure_integral, ProbabilisticTheory.realSpectralMeasure
statement: formalized
proof: formalized
---

# The distribution of an observable

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.SpectralMeasure`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean): 22 declarations, 17 with a docstring.

> The outcome distribution of an observable in a state, and the measurement of an isolated eigenvalue.

## i. Overview

> A state `ω` and an observable `a` determine a probability measure `μ_{ω,a}` on `ℝ`, the distribution
> of the outcomes of measuring `a` in `ω`. It is the unique probability measure on the spectrum of `a`
> with `ω(f(a)) = ∫ f dμ_{ω,a}` for continuous `f`, given by the Riesz–Markov–Kakutani theorem. At an
> isolated point `x` of the spectrum the spectral projection gives a two-outcome measurement "does `a`
> take the value `x`?", whose probability of `true` is `μ_{ω,a}({x})`.

## ii. Key results

> - `realSpectralMeasure` : the distribution `μ_{ω,a}`.
> - `realSpectralMeasure_integral` : `ω(f(a)) = ∫ f dμ_{ω,a}`.
> - `realSpectralMeasure_unique` : the distribution is unique.
> - `eigenMeasurement` : the measurement of an isolated eigenvalue.
> - `eigenMeasurement_true` : its outcome probability is `μ_{ω,a}({x})`.

## iv. References

> * None.

**`ProbabilisticTheory.spectralFunctional`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L54).

> The positive functional `f ↦ ω(f(a))` on continuous functions on the spectrum of `a`.

```lean
noncomputable def spectralFunctional (ω : 𝓢[ℂ, A]) (a : Observable A) :
    C(spectrum ℝ (a : A), ℝ) →ₚ[ℝ] ℝ
```

**`ProbabilisticTheory.spectralFunctionalCc`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L76).

> `spectralFunctional` on compactly supported functions.

```lean
noncomputable def spectralFunctionalCc (ω : 𝓢[ℂ, A]) (a : Observable A) :
    C_c(spectrum ℝ (a : A), ℝ) →ₚ[ℝ] ℝ
```

**`ProbabilisticTheory.spectralMeasure`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L90).

> `spectralMeasure` on the spectrum itself; `realSpectralMeasure` below places it inside `ℝ`.

```lean
noncomputable def spectralMeasure (ω : 𝓢[ℂ, A]) (a : Observable A) :
    Measure (spectrum ℝ (a : A))
```

**`ProbabilisticTheory.spectralMeasure_isFiniteMeasure`**, an instance, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L94).

```lean
instance spectralMeasure_isFiniteMeasure (ω : 𝓢[ℂ, A]) (a : Observable A) :
    IsFiniteMeasure (spectralMeasure ω a)
```

**`ProbabilisticTheory.spectralFunctional_one`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L98).

```lean
lemma spectralFunctional_one (ω : 𝓢[ℂ, A]) (a : Observable A) :
    spectralFunctional ω a 1 = 1
```

**`ProbabilisticTheory.spectralMeasure_isProbabilityMeasure`**, an instance, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L108).

> Total mass one, matching `ω(1) = 1`.

```lean
instance spectralMeasure_isProbabilityMeasure (ω : 𝓢[ℂ, A]) (a : Observable A) :
    IsProbabilityMeasure (spectralMeasure ω a)
```

**`ProbabilisticTheory.spectralMeasure_integral`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L116).

> `∫ f dμ = ω(f(a))` on the spectrum.

```lean
lemma spectralMeasure_integral (ω : 𝓢[ℂ, A]) (a : Observable A)
    (f : C(spectrum ℝ (a : A), ℝ)) :
    ω.onObservables ⟨cfcHom a.property f, cfcHom_predicate a.property f⟩ =
      ∫ x, f x ∂(spectralMeasure ω a)
```

**`ProbabilisticTheory.realSpectralMeasure`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L127).

> **The distribution of `a` in `ω`**, the probability measure `μ_{ω,a}` on `ℝ` with `ω(f(a)) = ∫ f
> dμ\_\{ω,a}`.

```lean
noncomputable def realSpectralMeasure (ω : 𝓢[ℂ, A]) (a : Observable A) : Measure ℝ
```

**`ProbabilisticTheory.realSpectralMeasure_isProbabilityMeasure`**, an instance, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L130).

```lean
instance realSpectralMeasure_isProbabilityMeasure (ω : 𝓢[ℂ, A]) (a : Observable A) :
    IsProbabilityMeasure (realSpectralMeasure ω a)
```

**`ProbabilisticTheory.realSpectralMeasure_compl_spectrum`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L135).

> `μ_{ω,a}` is concentrated on `a`'s spectrum.

```lean
lemma realSpectralMeasure_compl_spectrum (ω : 𝓢[ℂ, A]) (a : Observable A) :
    realSpectralMeasure ω a (spectrum ℝ (a : A))ᶜ = 0
```

**`ProbabilisticTheory.realSpectralMeasure_integral`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L146).

> `∫ f dμ_{ω,a} = ω(f(a))`, for any `f` continuous on the spectrum of `a`.

```lean
lemma realSpectralMeasure_integral (ω : 𝓢[ℂ, A]) (a : Observable A) (f : ℝ → ℝ)
    (hf : ContinuousOn f (spectrum ℝ (a : A))) :
    ω.onObservables ⟨cfc f (a : A), cfc_predicate f (a : A)⟩ =
      ∫ y, f y ∂(realSpectralMeasure ω a)
```

**`ProbabilisticTheory.exists_continuousOn_extend`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L166).

> Every continuous function on the spectrum extends to one on `ℝ`, continuous on the spectrum.

```lean
lemma exists_continuousOn_extend (a : Observable A) (g : C(spectrum ℝ (a : A), ℝ)) :
    ∃ f : ℝ → ℝ, ContinuousOn f (spectrum ℝ (a : A)) ∧
      ∀ x : spectrum ℝ (a : A), f (x : ℝ) = g x
```

**`ProbabilisticTheory.comap_integral_eq`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L179).

> If a measure `μ` on `ℝ` reproduces `ω(f(a))` for every continuous `f`, then pulling `μ` back
> to the spectrum integrates every continuous test
> function there exactly as `spectralMeasure ω a` does.

```lean
lemma comap_integral_eq (ω : 𝓢[ℂ, A]) (a : Observable A) (μ : Measure ℝ)
    (hrep : ∀ f : ℝ → ℝ, ContinuousOn f (spectrum ℝ (a : A)) →
      ω.onObservables ⟨cfc f (a : A), cfc_predicate f (a : A)⟩ = ((∫ y, f y ∂μ : ℝ)))
    (hcomap_map :
      Measure.map Subtype.val (μ.comap (Subtype.val : spectrum ℝ (a : A) → ℝ)) = μ)
    (g : C(spectrum ℝ (a : A), ℝ)) :
    (∫ x, g x ∂(μ.comap (Subtype.val : spectrum ℝ (a : A) → ℝ))) =
      ∫ x, g x ∂(spectralMeasure ω a)
```

**`ProbabilisticTheory.realSpectralMeasure_unique`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L216).

> `μ_{ω,a}` is the only probability measure on `ℝ`, concentrated on `a`'s spectrum, with
> `∫ f dμ = ω(f(a))`: any other measure with these two properties already is `μ_{ω,a}`.

```lean
lemma realSpectralMeasure_unique (ω : 𝓢[ℂ, A]) (a : Observable A) (μ : Measure ℝ)
    [IsProbabilityMeasure μ] (hsupp : μ (spectrum ℝ (a : A))ᶜ = 0)
    (hrep : ∀ f : ℝ → ℝ, ContinuousOn f (spectrum ℝ (a : A)) →
      ω.onObservables ⟨cfc f (a : A), cfc_predicate f (a : A)⟩ = ((∫ y, f y ∂μ : ℝ))) :
    μ = realSpectralMeasure ω a
```

## A. Measuring an isolated eigenvalue

> At an isolated point `x` of the spectrum of `a`, an eigenvalue separated from the rest of the
> spectrum, the indicator of `{x}` is continuous on the spectrum, so the continuous functional
> calculus gives the spectral projection `eigenEffect`. Its two-outcome measurement asks whether `a`
> takes the value `x`, and the probability of `true` in `ω` is `μ_{ω,a}({x})`. Spectral projections of
> arbitrary Borel sets need the Borel functional calculus.

**`ProbabilisticTheory.eigenIndicator`**, a def, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L254).

> The indicator function of an isolated point `x` of `a`'s spectrum, as a continuous function on
> the spectrum: continuous because `{x}` is clopen (`IsClopen.continuous_indicator`).

```lean
noncomputable def eigenIndicator (a : Observable A) {x : spectrum ℝ (a : A)}
    (hx : IsClopen ({x} : Set (spectrum ℝ (a : A)))) : C(spectrum ℝ (a : A), ℝ)
```

**`ProbabilisticTheory.eigenIndicator_apply`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L260).

```lean
lemma eigenIndicator_apply (a : Observable A) {x : spectrum ℝ (a : A)}
    (hx : IsClopen ({x} : Set (spectrum ℝ (a : A)))) (y : spectrum ℝ (a : A)) :
    eigenIndicator a hx y = Set.indicator {x} 1 y
```

**`ProbabilisticTheory.eigenEffect`**, a def, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L265).

> The spectral projection of `a` at an isolated point `x` of its spectrum.

```lean
noncomputable def eigenEffect (a : Observable A) {x : spectrum ℝ (a : A)}
    (hx : IsClopen ({x} : Set (spectrum ℝ (a : A)))) : Effect (Observable A)
```

**`ProbabilisticTheory.eigenIndicator_mul_self`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L288).

```lean
lemma eigenIndicator_mul_self (a : Observable A) {x : spectrum ℝ (a : A)}
    (hx : IsClopen ({x} : Set (spectrum ℝ (a : A)))) :
    eigenIndicator a hx * eigenIndicator a hx = eigenIndicator a hx
```

**`ProbabilisticTheory.isIdempotentElem_eigenEffect`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L297).

> `eigenEffect` is idempotent: `cfcHom` is an algebra homomorphism, and the indicator function
> `eigenIndicator a hx` is already idempotent under pointwise multiplication.

```lean
lemma isIdempotentElem_eigenEffect (a : Observable A) {x : spectrum ℝ (a : A)}
    (hx : IsClopen ({x} : Set (spectrum ℝ (a : A)))) :
    IsIdempotentElem (((eigenEffect a hx : Effect (Observable A)) : Observable A) : A)
```

**`ProbabilisticTheory.isSharp_eigenEffect`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L305).

> The spectral projection at an isolated point is sharp.

```lean
lemma isSharp_eigenEffect (a : Observable A) {x : spectrum ℝ (a : A)}
    (hx : IsClopen ({x} : Set (spectrum ℝ (a : A)))) :
    Effect.IsSharp (eigenEffect a hx)
```

**`ProbabilisticTheory.eigenMeasurement`**, a def, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L311).

> The two-outcome measurement "does `a` read out the isolated spectral point `x`, or not?"

```lean
noncomputable def eigenMeasurement (a : Observable A) {x : spectrum ℝ (a : A)}
    (hx : IsClopen ({x} : Set (spectrum ℝ (a : A)))) : Measurement Bool (Observable A)
```

**`ProbabilisticTheory.eigenMeasurement_true`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean#L318).

> The probability that `eigenMeasurement` reads out `x` in `ω` is `μ_{ω,a}({x})`: the Born rule
> of the two-outcome measurement "does `a` read out `x`?" agrees with the probability measure built
> from `a`'s continuous functional calculus.

```lean
lemma eigenMeasurement_true (ω : 𝓢[ℂ, A]) (a : Observable A)
    {x : spectrum ℝ (a : A)} (hx : IsClopen ({x} : Set (spectrum ℝ (a : A))))
    (h : MeasurableSet {true}) :
    ω.onObservables (eigenMeasurement a hx {true} h : Observable A) =
      (realSpectralMeasure ω a).real ({(x : ℝ)} : Set ℝ)
```

## Depends on

- [The observables of a C⋆-algebra](../../../physlib/probabilistictheory/cstaralgebra/orderunit.md)
- [Sharp effects](../../../physlib/probabilistictheory/effect/sharp.md)
- [Binary measurements](../measurement/binary.md)
- [Observables](../staralgebra/observable.md)

## Proof depends on

- [Projections are sharp](sharpeffect.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SpectralMeasure.lean)
