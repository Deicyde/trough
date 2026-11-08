---
declaration: theorem
origin: cited
lean: LinearMap.isOpenMap_of_isTateRing
statement: formalized
proof: formalized
---

# The open mapping theorem over a Tate ring

A surjective linear map continuous at zero,
from a complete first-countable nonarchimedean module to a Hausdorff Baire module, is open.
The target needs only continuous constant scalar actions.

```lean
LinearMap.isOpenMap_of_isTateRing.{u_1, u_2, u_3} {A : Type u_1} {M : Type u_2} {N : Type u_3}
  [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [TauCeti.Huber.IsTateRing A]
  [AddCommGroup M] [UniformSpace M] [IsUniformAddGroup M] [CompleteSpace M]
  [(nhds 0).IsCountablyGenerated] [NonarchimedeanAddGroup M] [_root_.Module A M]
  [ContinuousSMul A M] [AddCommGroup N] [TopologicalSpace N] [IsTopologicalAddGroup N]
  [_root_.Module A N] [ContinuousConstSMul A N] [T0Space N] [BaireSpace N] (f : M →ₗ[A] N)
  (hf : Function.Surjective ⇑f) (hfc : ContinuousAt (⇑f) 0) : IsOpenMap ⇑f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Henkel's open mapping theorem](../../../topology/algebra/part-01/henkels-open-mapping-theorem.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.isOpenMap_of_isTateRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/OpenMapping.html#LinearMap.isOpenMap_of_isTateRing).

## Sources

- [Tau Ceti documentation: `LinearMap.isOpenMap_of_isTateRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/OpenMapping.html#LinearMap.isOpenMap_of_isTateRing)
- [Source of `LinearMap.isOpenMap_of_isTateRing` in TauCeti/RingTheory/Huber/OpenMapping.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Huber/OpenMapping.lean#L106)
