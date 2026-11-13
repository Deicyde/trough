---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedNormalSpectralData, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedNormalSpectralData.ext, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedNormalSpectralData.ext_of_boundedIntegral_eq, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedUnitarySpectralData, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedUnitarySpectralData.ext, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedUnitarySpectralData.ext_of_boundedIntegral_eq, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedUnitarySpectralData.realSpectralMeasure, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedUnitarySpectralData.cayleyMap_realSpectralMeasure
statement: formalized
proof: formalized
---

# Spectral data of bounded normal and unitary operators

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Cayley.Certificate`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Certificate.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Certificate.lean): 9 declarations, 4 with a docstring.

> Spectral measures reconstructing bounded normal and unitary operators.

## i. Overview

> `BoundedNormalSpectralData` is a spectral measure on `ℂ` whose integral of the identity is a given
> bounded normal operator. `BoundedUnitarySpectralData` is the same for a unitary whose spectral
> measure is supported on the unit circle away from `1`. Pulling such a measure back along the Cayley
> transform gives a spectral measure on `ℝ`, which is determined by its Cayley pushforward.

## ii. Key results

> - `BoundedNormalSpectralData` : a spectral measure reconstructing a bounded normal operator.
> - `BoundedUnitarySpectralData` : a spectral measure reconstructing a unitary, supported away from
>   `1`.
> - `BoundedUnitarySpectralData.realSpectralMeasure` : the pulled-back spectral measure on `ℝ`.
> - `BoundedUnitarySpectralData.realSpectralMeasure_eq_of_cayleyMap_eq` : a real spectral measure is
>   determined by its Cayley pushforward.

## iv. References

> * None.

## A. Bounded normal spectral data

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedNormalSpectralData`**, a structure, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Certificate.lean#L60).

> A spectral measure on `ℂ` whose integral of the identity is the bounded normal operator `U`.

```lean
structure BoundedNormalSpectralData (U : H →L[ℂ] H) where
  /-- The spectral measure. -/
  spectralMeasure : WOTSpectralMeasure ℂ H
  reconstruction : ∀ x y : H,
    spectralMeasure.complexWeakIntegral id x y = ⟪y, U x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedNormalSpectralData.ext`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Certificate.lean#L71).

```lean
lemma ext {D E : BoundedNormalSpectralData U}
    (h : D.spectralMeasure = E.spectralMeasure) : D = E
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedNormalSpectralData.ext_of_boundedIntegral_eq`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Certificate.lean#L84).

```lean
lemma ext_of_boundedIntegral_eq {D E : BoundedNormalSpectralData U}
    (h : ∀ (f : ℂ → ℂ) (hf : Measurable f)
      (hfb : ∃ C : ℝ, ∀ z, ‖f z‖ ≤ C),
      D.spectralMeasure.boundedIntegral f hf hfb =
        E.spectralMeasure.boundedIntegral f hf hfb) :
    D = E
```

## B. Bounded unitary spectral data

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedUnitarySpectralData`**, a structure, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Certificate.lean#L99).

> A spectral measure of the unitary `u`, supported on the unit circle and giving no mass to `1`.

```lean
structure BoundedUnitarySpectralData (u : H ≃ₗᵢ[ℂ] H) where
  /-- The spectral measure. -/
  spectralMeasure : WOTSpectralMeasure ℂ H
  support_away_one : ∀ S : Set ℂ, MeasurableSet S →
    spectralMeasure S = spectralMeasure (S ∩ {z | ‖z‖ = 1 ∧ z ≠ 1})
  reconstruction : ∀ x y : H,
    spectralMeasure.complexWeakIntegral id x y = ⟪y, u x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedUnitarySpectralData.ext`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Certificate.lean#L112).

```lean
lemma ext {D E : BoundedUnitarySpectralData u}
    (h : D.spectralMeasure = E.spectralMeasure) : D = E
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedUnitarySpectralData.ext_of_boundedIntegral_eq`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Certificate.lean#L121).

```lean
lemma ext_of_boundedIntegral_eq {D E : BoundedUnitarySpectralData u}
    (h : ∀ (f : ℂ → ℂ) (hf : Measurable f)
      (hfb : ∃ C : ℝ, ∀ z, ‖f z‖ ≤ C),
      D.spectralMeasure.boundedIntegral f hf hfb =
        E.spectralMeasure.boundedIntegral f hf hfb) :
    D = E
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedUnitarySpectralData.realSpectralMeasure`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Certificate.lean#L133).

> Pull the bounded unitary measure back to the real line.

```lean
def realSpectralMeasure : WOTSpectralMeasure ℝ H
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedUnitarySpectralData.cayleyMap_realSpectralMeasure`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Certificate.lean#L136).

```lean
lemma cayleyMap_realSpectralMeasure :
    WOTSpectralMeasure.cayleyMap D.realSpectralMeasure = D.spectralMeasure
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.BoundedUnitarySpectralData.realSpectralMeasure_eq_of_cayleyMap_eq`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Certificate.lean#L163).

> The real measure recovered from bounded Cayley data is unique among real measures with the
> same Cayley pushforward.

```lean
lemma realSpectralMeasure_eq_of_cayleyMap_eq
    {μS : WOTSpectralMeasure ℝ H}
    (hμ : WOTSpectralMeasure.cayleyMap μS = D.spectralMeasure) :
    D.realSpectralMeasure = μS
```

## Depends on

- [Spectral measures and the Cayley transform](unbounded-cayley-measure.md)

## Proof depends on

- [The bounded functional calculus of a spectral measure](unbounded-boundedintegralalgebra.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Certificate.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Certificate.lean)
