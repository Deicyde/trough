---
declaration: theorem
origin: cited
lean: TauCeti.CircleSobolev.isCompactOperator_inclusion, BesselPotentialSpace.isCompact_closure_image_inclusion_of_smulLeftCLM_eq, BesselPotentialSpace.isCompactOperator_inclusion_comp_smulLeftCLM
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

- [Peetre's inequality (`TauCeti.one_add_norm_add_sq_rpow_le_mul`)](../../../../analysis/part-03/special-functions/peetres-inequality-tauceti-one-add-norm-add-sq-r.md)
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

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.isCompactOperator_inclusion`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Basic.html#TauCeti.CircleSobolev.isCompactOperator_inclusion)
- [Source of `TauCeti.CircleSobolev.isCompactOperator_inclusion` in TauCeti/Analysis/Sobolev/Circle/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/Circle/Basic.lean#L724)
