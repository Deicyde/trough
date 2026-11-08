---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.exists_preimage_norm_le_of_isTate, LinearMap.exists_preimage_norm_le_of_surjective
statement: formalized
proof: formalized
---

# Quantitative Open Mapping Theorem

for a surjective continuous linear map `f : M →L[R] N`
from a complete ultrametric seminormed module to a complete normed module over a Tate ring, there
exists `C > 0` such that every `y : N` lifts to `x : M` with `‖x‖ ≤ C * ‖y‖`.

```lean
ContinuousLinearMap.exists_preimage_norm_le_of_isTate.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2}
  {N : Type u_3} [SeminormedRing R] [TauCeti.NormedRing.IsTate R] [SeminormedAddCommGroup M]
  [IsUltrametricDist M] [CompleteSpace M] [_root_.Module R M] [IsBoundedSMul R M]
  [NormedAddCommGroup N] [CompleteSpace N] [_root_.Module R N] [IsBoundedSMul R N] (f : M →L[R] N)
  (hsurj : Function.Surjective ⇑f) : ∃ C > 0, ∀ (y : N), ∃ x, f x = y ∧ ‖x‖ ≤ C * ‖y‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The open mapping theorem](../../complex/part-02/the-open-mapping-theorem.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.exists_preimage_norm_le_of_isTate`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.html#ContinuousLinearMap.exists_preimage_norm_le_of_isTate).

## Other forms

**Quantitative Open Mapping Theorem for linear maps over a Tate ring.** Formalized in Tau Ceti as [`LinearMap.exists_preimage_norm_le_of_surjective`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.html#LinearMap.exists_preimage_norm_le_of_surjective).

```lean
LinearMap.exists_preimage_norm_le_of_surjective.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2}
  {N : Type u_3} [SeminormedRing R] [TauCeti.NormedRing.IsTate R] [SeminormedAddCommGroup M]
  [IsUltrametricDist M] [CompleteSpace M] [_root_.Module R M] [IsBoundedSMul R M]
  [NormedAddCommGroup N] [CompleteSpace N] [_root_.Module R N] [IsBoundedSMul R N] (f : M →ₗ[R] N)
  (hf : Continuous ⇑f) (hsurj : Function.Surjective ⇑f) :
  ∃ C > 0, ∀ (y : N), ∃ x, f x = y ∧ ‖x‖ ≤ C * ‖y‖
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.exists_preimage_norm_le_of_isTate`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.html#ContinuousLinearMap.exists_preimage_norm_le_of_isTate)
- [Source of `ContinuousLinearMap.exists_preimage_norm_le_of_isTate` in TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.lean#L291)
