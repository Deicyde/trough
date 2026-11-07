---
declaration: def
origin: cited
lean: TauCeti.smoothTensorInducedDiagonalClass
statement: formalized
---

# The Evens norm of a cocycle

for a homogeneous cocycle `z` of degree `n` of the total
coinduced resolution of `A`, fixed by `U`, the class in `H^{l n}(G, Ind⊗ A)` of its diagonal
tensor `z ⊗ ⋯ ⊗ z`, one factor for each of the `l` cosets of `U`. Here `A` has characteristic two,
so that the tensor-induced resolution is a complex, and the class is computed through
`TauCeti.smoothTensorInducedGradedResolutionContraction` for some order on the cosets; by
`TauCeti.smoothTensorInducedDiagonalClass_eq` it does not depend on that order.

```lean
TauCeti.smoothTensorInducedDiagonalClass.{u, v, w} {R : Type u} [CommRing R] [TopologicalSpace R]
  [DiscreteTopology R] {G : Type v} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  (U : Subgroup G) (hU : IsOpen ↑U) (s : U.LeftTransversal) [U.FiniteIndex] [CompactSpace ↥U]
  (A : TauCeti.SmoothDiscreteTopRep R ↥U) [Fintype (G ⧸ U)] (hA : ∀ (a : ↑A.obj), a + a = 0) {n : ℕ}
  (z : A.obj.gradedResolutionModule) (hz : z ∈ A.obj.gradedResolutionPiece ↑n)
  (hinv : ∀ (u : ↥U), (A.obj.gradedResolutionTopRep.ρ u) z = z)
  (hdz : A.obj.gradedResolutionDifferential z = 0) :
  ↑(continuousCohomology (Fintype.card (G ⧸ U) * n)
        ((TauCeti.toSmoothDiscrete R G).obj
            (TauCeti.DiscreteRep.tensorInduced U hU s
              ((TauCeti.ofSmoothDiscrete R ↥U).obj A))).obj).toModuleCat
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.smoothTensorInducedDiagonalClass`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Tensor/Induction/Resolution.html#TauCeti.smoothTensorInducedDiagonalClass).

## Sources

- [Tau Ceti documentation: `TauCeti.smoothTensorInducedDiagonalClass`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Tensor/Induction/Resolution.html#TauCeti.smoothTensorInducedDiagonalClass)
- [Source of `TauCeti.smoothTensorInducedDiagonalClass` in TauCeti/RepresentationTheory/Tensor/Induction/Resolution.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Tensor/Induction/Resolution.lean#L576)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
