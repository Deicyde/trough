---
declaration: theorem
origin: cited
lean: PreAbstractSimplicialComplex.IsCombinatorialManifold.exists_chartedSpace_hasGroupoid_PLGroupoid
statement: formalized
proof: formalized
---

# PreAbstractSimplicialComplex.IsCombinatorialManifold.exists\_chartedSpace\_hasGroupoid\_PLGroupoid

The weak realization of a positive-dimensional combinatorial manifold is a PL manifold,
possibly with boundary: it has an atlas modelled on the half-space in `(Fin n → ℝ) × ℝ` whose
chart transitions lie in the PL groupoid. No finiteness or countability of the complex is
assumed.

```lean
PreAbstractSimplicialComplex.IsCombinatorialManifold.exists_chartedSpace_hasGroupoid_PLGroupoid.{u_1}
  {ι : Type u_1} [DecidableEq ι] {K : AbstractSimplicialComplex ι} {n : ℕ}
  (h : K.IsCombinatorialManifold (n + 1)) :
  ∃ C,
    have this := C;
    HasGroupoid K.Realization (TauCeti.PLGroupoid (TauCeti.modelWithCornersHalfSpace (Fin n → ℝ)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PreAbstractSimplicialComplex.IsCombinatorialManifold.exists_chartedSpace_hasGroupoid_PLGroupoid`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialComplex/CombinatorialManifold/PL.html#PreAbstractSimplicialComplex.IsCombinatorialManifold.exists_chartedSpace_hasGroupoid_PLGroupoid).

## Sources

- [Tau Ceti documentation: `PreAbstractSimplicialComplex.IsCombinatorialManifold.exists_chartedSpace_hasGroupoid_PLGroupoid`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialComplex/CombinatorialManifold/PL.html#PreAbstractSimplicialComplex.IsCombinatorialManifold.exists_chartedSpace_hasGroupoid_PLGroupoid)
- [Source of `PreAbstractSimplicialComplex.IsCombinatorialManifold.exists_chartedSpace_hasGroupoid_PLGroupoid` in TauCeti/AlgebraicTopology/SimplicialComplex/CombinatorialManifold/PL.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/SimplicialComplex/CombinatorialManifold/PL.lean#L66)
- [Tau Ceti roadmap status: Geometric topology and the solved Kirby-list problems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricTopology/STATUS.md)
