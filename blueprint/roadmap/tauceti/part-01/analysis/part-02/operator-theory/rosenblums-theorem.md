---
declaration: theorem
origin: cited
lean: LinearPMap.Intertwines.eq_zero_of_disjoint_spectrum, ContinuousLinearMap.eq_zero_of_comp_eq_comp_of_disjoint_spectrum
statement: formalized
proof: formalized
---

# Rosenblum's theorem

A bounded operator intertwining two self-adjoint partial linear maps
with disjoint spectra is zero.

```lean
LinearPMap.Intertwines.eq_zero_of_disjoint_spectrum.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E] [NormedAddCommGroup F]
  [InnerProductSpace ℂ F] [CompleteSpace F] {A : E →ₗ.[ℂ] E} {B : F →ₗ.[ℂ] F} {X : E →L[ℂ] F}
  (h : A.Intertwines B X) (hA : IsSelfAdjoint A) (hB : IsSelfAdjoint B)
  (hAB : Disjoint A.spectrum B.spectrum) : X = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearPMap.Intertwines.eq_zero_of_disjoint_spectrum`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/Rosenblum.html#LinearPMap.Intertwines.eq_zero_of_disjoint_spectrum).

## Other forms

**Rosenblum's theorem for bounded operators.** Formalized in Tau Ceti as [`ContinuousLinearMap.eq_zero_of_comp_eq_comp_of_disjoint_spectrum`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/Rosenblum.html#ContinuousLinearMap.eq_zero_of_comp_eq_comp_of_disjoint_spectrum).

```lean
ContinuousLinearMap.eq_zero_of_comp_eq_comp_of_disjoint_spectrum.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
  [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F] {S : E →L[ℂ] E} {T : F →L[ℂ] F}
  {X : E →L[ℂ] F} (h : X ∘SL S = T ∘SL X) (hS : IsSelfAdjoint S) (hT : IsSelfAdjoint T)
  (hST : Disjoint (spectrum ℂ S) (spectrum ℂ T)) : X = 0
```

## Sources

- [Tau Ceti documentation: `LinearPMap.Intertwines.eq_zero_of_disjoint_spectrum`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/Rosenblum.html#LinearPMap.Intertwines.eq_zero_of_disjoint_spectrum)
- [Source of `LinearPMap.Intertwines.eq_zero_of_disjoint_spectrum` in TauCeti/Analysis/InnerProductSpace/LinearPMap/Rosenblum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/LinearPMap/Rosenblum.lean#L61)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/OperatorTheory/STATUS.md)
