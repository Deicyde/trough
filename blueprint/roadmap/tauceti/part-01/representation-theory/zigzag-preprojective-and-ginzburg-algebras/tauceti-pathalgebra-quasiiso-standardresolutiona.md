---
declaration: theorem
origin: cited
lean: TauCeti.PathAlgebra.quasiIso_standardResolutionAugmentation
statement: formalized
proof: formalized
---

# TauCeti.PathAlgebra.quasiIso_standardResolutionAugmentation

The small resolution resolves the DG path algebra: its augmentation induces an
isomorphism in every cohomological degree. No restriction on the arrow weights or on the
number of arrows is needed.

```lean
TauCeti.PathAlgebra.quasiIso_standardResolutionAugmentation.{u, v, w} (k : Type w) [CommRing k]
  (Q : Type u) [Quiver Q] [Fintype Q] [DecidableEq Q] [(i j : Q) → DecidableEq (i ⟶ j)]
  (wt : {i j : Q} → (i ⟶ j) → ℤ) (d : TauCeti.pathAlgebra k Q →ₗ[k] TauCeti.pathAlgebra k Q)
  (hd : TauCeti.IsDGAlgebra (TauCeti.PathAlgebra.gradeBy k fun {a b} => wt) d)
  (hdε : ∀ (i : Q), d (TauCeti.PathAlgebra.vertexIdempotent k i) = 0) :
  QuasiIso (TauCeti.PathAlgebra.standardResolutionAugmentation k Q (fun {i j} => wt) d hd hdε)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PathAlgebra.quasiIso_standardResolutionAugmentation`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/PathAlgebra/SemifreeResolution/Cone.html#TauCeti.PathAlgebra.quasiIso_standardResolutionAugmentation).

## Sources

- [Tau Ceti documentation: `TauCeti.PathAlgebra.quasiIso_standardResolutionAugmentation`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/PathAlgebra/SemifreeResolution/Cone.html#TauCeti.PathAlgebra.quasiIso_standardResolutionAugmentation)
- [Source of `TauCeti.PathAlgebra.quasiIso_standardResolutionAugmentation` in TauCeti/RepresentationTheory/Quiver/PathAlgebra/SemifreeResolution/Cone.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/Quiver/PathAlgebra/SemifreeResolution/Cone.lean#L80)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
