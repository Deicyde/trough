---
declaration: theorem
origin: cited
lean: LinearMap.isOpenMap_of_isTate
statement: formalized
proof: formalized
---

# Open Mapping Theorem for normed modules over a Tate ring

A surjective continuous linear map from a complete ultrametric seminormed module to a complete
normed module over a Tate ring is an open map.

```lean
LinearMap.isOpenMap_of_isTate.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2} {N : Type u_3}
  [SeminormedRing R] [TauCeti.NormedRing.IsTate R] [SeminormedAddCommGroup M] [IsUltrametricDist M]
  [CompleteSpace M] [_root_.Module R M] [IsBoundedSMul R M] [NormedAddCommGroup N] [CompleteSpace N]
  [_root_.Module R N] [IsBoundedSMul R N] (f : M →ₗ[R] N) (hf : Continuous ⇑f)
  (hsurj : Function.Surjective ⇑f) : IsOpenMap ⇑f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Henkel's open mapping theorem](../../../../topology/algebra/part-01/henkels-open-mapping-theorem.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.isOpenMap_of_isTate`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.html#LinearMap.isOpenMap_of_isTate).

## Sources

- [Tau Ceti documentation: `LinearMap.isOpenMap_of_isTate`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.html#LinearMap.isOpenMap_of_isTate)
- [Source of `LinearMap.isOpenMap_of_isTate` in TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.lean#L156)
