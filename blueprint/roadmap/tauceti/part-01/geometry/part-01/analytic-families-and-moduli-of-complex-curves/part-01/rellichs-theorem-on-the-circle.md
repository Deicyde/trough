---
declaration: theorem
origin: cited
lean: TauCeti.CircleSobolev.isCompactOperator_inclusion, BesselPotentialSpace.isCompact_closure_image_inclusion_of_smulLeftCLM_eq, BesselPotentialSpace.isCompactOperator_inclusion_comp_smulLeftCLM, TauCeti.CylinderSobolev.isCompactOperator_restrictValue_comp_subtypeL
statement: formalized
proof: formalized
---

# Rellich's theorem on the circle

the inclusion `H^s → H^t` is a compact operator for
`t < s` when `E` is finite-dimensional.

```lean
TauCeti.CircleSobolev.isCompactOperator_inclusion.{u_1} {s t : ℝ} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] (h : t < s) :
  IsCompactOperator ⇑(TauCeti.CircleSobolev.inclusion ⋯)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Fréchet--Kolmogorov criterion for a family vanishing almost everywhere off a fixed bounded set](../../../../measure-theory/function/part-01/the-frechet-kolmogorov-criterion-for-a-family-va.md)
- [Hölder's inequality for disjoint pieces](../../../../measure-theory/function/part-01/holders-inequality-for-disjoint-pieces.md)
- [Peetre's inequality (`TauCeti.one_add_norm_add_sq_rpow_le_mul`)](../../../../analysis/part-04/special-functions/peetres-inequality-tauceti-one-add-norm-add-sq-r.md)
- [Plancherel's theorem for the inverse Fourier transform of Schwartz functions](../../../../analysis/part-03/distribution/plancherels-theorem-for-the-inverse-fourier-tran.md)
- [The weighted Plancherel bound](../../../../analysis/part-03/distribution/the-weighted-plancherel-bound.md)
- [Young's convolution inequality](../../../../analysis/part-03/convolution/youngs-convolution-inequality.md)
- [Young's inequality for integral kernels](../../../../measure-theory/integral/part-02/youngs-inequality-for-integral-kernels.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CircleSobolev.isCompactOperator_inclusion`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Basic.html#TauCeti.CircleSobolev.isCompactOperator_inclusion).

## Other forms

**Rellich's theorem for a common compact support.** Formalized in Tau Ceti as [`BesselPotentialSpace.isCompact_closure_image_inclusion_of_smulLeftCLM_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/BesselPotential/Rellich.html#BesselPotentialSpace.isCompact_closure_image_inclusion_of_smulLeftCLM_eq).

```lean
BesselPotentialSpace.isCompact_closure_image_inclusion_of_smulLeftCLM_eq.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [InnerProductSpace ℂ F]
  [CompleteSpace F] {r s : ℝ} [FiniteDimensional ℂ F] {φ : SchwartzMap E ℂ} (h : r < s)
  {S : Set (BesselPotentialSpace E F s 2)} (hS : Bornology.IsBounded S)
  (hφ : ∀ u ∈ S, (BesselPotentialSpace.smulLeftCLM s φ) u = u) :
  IsCompact (closure (⇑(BesselPotentialSpace.inclusion ⋯) '' S))
```

**Rellich's theorem for Bessel-potential spaces.** Formalized in Tau Ceti as [`BesselPotentialSpace.isCompactOperator_inclusion_comp_smulLeftCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/BesselPotential/Rellich.html#BesselPotentialSpace.isCompactOperator_inclusion_comp_smulLeftCLM).

```lean
BesselPotentialSpace.isCompactOperator_inclusion_comp_smulLeftCLM.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [InnerProductSpace ℂ F]
  [CompleteSpace F] {r s : ℝ} [FiniteDimensional ℂ F] (φ : SchwartzMap E ℂ) (h : r < s) :
  IsCompactOperator ⇑(BesselPotentialSpace.inclusion ⋯ ∘SL BesselPotentialSpace.smulLeftCLM s φ)
```

**Rellich's theorem on the cylinder.** Formalized in Tau Ceti as [`TauCeti.CylinderSobolev.isCompactOperator_restrictValue_comp_subtypeL`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Cylinder.html#TauCeti.CylinderSobolev.isCompactOperator_restrictValue_comp_subtypeL).

```lean
TauCeti.CylinderSobolev.isCompactOperator_restrictValue_comp_subtypeL.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] (T : ℝ) :
  IsCompactOperator
    ⇑(TauCeti.CylinderSobolev.restrictValue T ∘SL (TauCeti.CylinderSobolev.H1 V).subtypeL)
```

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.isCompactOperator_inclusion`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Basic.html#TauCeti.CircleSobolev.isCompactOperator_inclusion)
- [Source of `TauCeti.CircleSobolev.isCompactOperator_inclusion` in TauCeti/Analysis/Sobolev/Circle/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Sobolev/Circle/Basic.lean#L733)
