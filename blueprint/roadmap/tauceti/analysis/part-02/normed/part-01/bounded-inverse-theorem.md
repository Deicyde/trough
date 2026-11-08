---
declaration: def
origin: cited
lean: ContinuousLinearEquiv.ofBijectiveOfIsTate, LinearEquiv.continuous_symm_of_isTate
statement: formalized
---

# Bounded Inverse Theorem

a bijective continuous linear map from a complete ultrametric
seminormed module to a complete normed module over a Tate ring is a continuous linear
equivalence.

```lean
ContinuousLinearEquiv.ofBijectiveOfIsTate.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2}
  {N : Type u_3} [SeminormedRing R] [TauCeti.NormedRing.IsTate R] [SeminormedAddCommGroup M]
  [IsUltrametricDist M] [CompleteSpace M] [_root_.Module R M] [IsBoundedSMul R M]
  [NormedAddCommGroup N] [CompleteSpace N] [_root_.Module R N] [IsBoundedSMul R N] (f : M →L[R] N)
  (hf : Function.Bijective ⇑f) : M ≃L[R] N
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Open Mapping Theorem for normed modules over a Tate ring](../part-02/open-mapping-theorem-for-normed-modules-over-a-t.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearEquiv.ofBijectiveOfIsTate`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.html#ContinuousLinearEquiv.ofBijectiveOfIsTate).

## Other forms

**Bounded Inverse Theorem for linear equivalences over a Tate ring.** Formalized in Tau Ceti as [`LinearEquiv.continuous_symm_of_isTate`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.html#LinearEquiv.continuous_symm_of_isTate).

```lean
LinearEquiv.continuous_symm_of_isTate.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2} {N : Type u_3}
  [SeminormedRing R] [TauCeti.NormedRing.IsTate R] [SeminormedAddCommGroup M] [IsUltrametricDist M]
  [CompleteSpace M] [_root_.Module R M] [IsBoundedSMul R M] [NormedAddCommGroup N] [CompleteSpace N]
  [_root_.Module R N] [IsBoundedSMul R N] (e : M ≃ₗ[R] N) (he : Continuous ⇑e) : Continuous ⇑e.symm
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearEquiv.ofBijectiveOfIsTate`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.html#ContinuousLinearEquiv.ofBijectiveOfIsTate)
- [Source of `ContinuousLinearEquiv.ofBijectiveOfIsTate` in TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.lean#L237)
