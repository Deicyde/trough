---
declaration: theorem
origin: cited
lean: TauCeti.SkewZigzagParameter.cohomologyClass_eq_iff_exists_vertexFixing_algEquiv
statement: formalized
proof: formalized
---

# Couture's classification

over a commutative ring, two skew-zigzag parameters of a finite
graph have the same cohomology class in `H¹(G, kˣ)` exactly when their relation quotients are
isomorphic by an algebra isomorphism fixing every vertex idempotent.

```lean
TauCeti.SkewZigzagParameter.cohomologyClass_eq_iff_exists_vertexFixing_algEquiv.{u, w} {V : Type u}
  {G : SimpleGraph V} {k : Type w} [CommRing k] [Finite V]
  {c c' : TauCeti.SkewZigzagParameter k G} :
  (TauCeti.SkewZigzagParameter.cohomologyClass k G) c =
      (TauCeti.SkewZigzagParameter.cohomologyClass k G) c' ↔
    ∃ φ,
      ∀ (i : V),
        φ
            ((TauCeti.skewZigzagMk k G c)
              (TauCeti.PathAlgebra.vertexIdempotent k (TauCeti.DoubledQuiver.vertex G i))) =
          (TauCeti.skewZigzagMk k G c')
            (TauCeti.PathAlgebra.vertexIdempotent k (TauCeti.DoubledQuiver.vertex G i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SkewZigzagParameter.cohomologyClass_eq_iff_exists_vertexFixing_algEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Cohomology.html#TauCeti.SkewZigzagParameter.cohomologyClass_eq_iff_exists_vertexFixing_algEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.SkewZigzagParameter.cohomologyClass_eq_iff_exists_vertexFixing_algEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Cohomology.html#TauCeti.SkewZigzagParameter.cohomologyClass_eq_iff_exists_vertexFixing_algEquiv)
- [Source of `TauCeti.SkewZigzagParameter.cohomologyClass_eq_iff_exists_vertexFixing_algEquiv` in TauCeti/RepresentationTheory/Quiver/Zigzag/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/Zigzag/Cohomology.lean#L247)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
