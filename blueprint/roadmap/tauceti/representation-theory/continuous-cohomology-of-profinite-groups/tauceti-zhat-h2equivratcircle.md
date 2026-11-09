---
declaration: def
origin: cited
lean: TauCeti.zHat.h2EquivRatCircle
statement: formalized
---

# TauCeti.zHat.h2EquivRatCircle

Second integral continuous cohomology of the profinite integers is the rational circle.
The inverse sends a rational-circle value to the connecting class of the unique continuous
character taking that value at the canonical generator.

```lean
TauCeti.zHat.h2EquivRatCircle.{u}
  [DistribMulAction (↑TauCeti.zHat.toProfinite.toTop) (ULift.{u, 0} ℤ)]
  [DistribMulAction (↑TauCeti.zHat.toProfinite.toTop) (ULift.{u, 0} ℚ)]
  [TopologicalSpace (ULift.{u, 0} ℚ)] [DiscreteTopology (ULift.{u, 0} ℚ)] (C : Type u)
  [AddCommGroup C] [TopologicalSpace C] [DiscreteTopology C]
  [DistribMulAction (↑TauCeti.zHat.toProfinite.toTop) C] (e : C ≃+ AddCircle 1)
  (hℤ : ∀ (g : ↑TauCeti.zHat.toProfinite.toTop) (x : ULift.{u, 0} ℤ), g • x = x)
  (hℚ : ∀ (g : ↑TauCeti.zHat.toProfinite.toTop) (x : ULift.{u, 0} ℚ), g • x = x)
  (hC : ∀ (g : ↑TauCeti.zHat.toProfinite.toTop) (x : C), g • x = x) :
  ↑(continuousCohomology 2
          (TauCeti.ofDiscreteModule ℤ (↑TauCeti.zHat.toProfinite.toTop)
            (ULift.{u, 0} ℤ))).toModuleCat ≃+
    AddCircle 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.zHat.h2EquivRatCircle`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/IntegralCohomology.html#TauCeti.zHat.h2EquivRatCircle).

## Sources

- [Tau Ceti documentation: `TauCeti.zHat.h2EquivRatCircle`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/IntegralCohomology.html#TauCeti.zHat.h2EquivRatCircle)
- [Source of `TauCeti.zHat.h2EquivRatCircle` in TauCeti/Topology/Algebra/Group/Profinite/ZHat/IntegralCohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ZHat/IntegralCohomology.lean#L52)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
