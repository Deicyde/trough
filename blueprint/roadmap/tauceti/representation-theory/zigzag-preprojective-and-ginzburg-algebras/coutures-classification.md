---
declaration: theorem
origin: cited
lean: TauCeti.SkewZigzagParameter.cohomologyClass_eq_iff_exists_vertexFixing_algEquiv, TauCeti.SkewZigzagParameter.cohomologyClass_map_eq_iff_exists_vertexFixing_algEquiv, TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_algEquiv_mem_span, TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_vertexPermuting_algEquiv
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

## Other forms

**Couture's classification is injective under a coefficient homomorphism that is injective on units.** Formalized in Tau Ceti as [`TauCeti.SkewZigzagParameter.cohomologyClass_map_eq_iff_exists_vertexFixing_algEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Skew/Cohomology.html#TauCeti.SkewZigzagParameter.cohomologyClass_map_eq_iff_exists_vertexFixing_algEquiv).

```lean
TauCeti.SkewZigzagParameter.cohomologyClass_map_eq_iff_exists_vertexFixing_algEquiv.{u, w, z}
  {k : Type w} {V : Type u} {G : SimpleGraph V} {l : Type z} [CommRing k] [CommMonoid l] [Finite V]
  (f : k →* l) (hf : Function.Injective ⇑(Units.map f)) {c c' : TauCeti.SkewZigzagParameter k G} :
  (TauCeti.SkewZigzagParameter.cohomologyClass l G) (TauCeti.SkewZigzagParameter.map f c) =
      (TauCeti.SkewZigzagParameter.cohomologyClass l G) (TauCeti.SkewZigzagParameter.map f c') ↔
    ∃ φ,
      ∀ (i : V),
        φ
            ((TauCeti.skewZigzagMk k G c)
              (TauCeti.PathAlgebra.vertexIdempotent k (TauCeti.DoubledQuiver.vertex G i))) =
          (TauCeti.skewZigzagMk k G c')
            (TauCeti.PathAlgebra.vertexIdempotent k (TauCeti.DoubledQuiver.vertex G i))
```

**Couture's classification up to graph automorphisms.** Formalized in Tau Ceti as [`TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_algEquiv_mem_span`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Skew/Automorphism.html#TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_algEquiv_mem_span).

```lean
TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_algEquiv_mem_span.{u, w}
  {k : Type w} [CommRing k] {V : Type u} {G : SimpleGraph V} [Finite V]
  {c c' : TauCeti.SkewZigzagParameter k G} [Nontrivial k]
  (hidempotents : ∀ (e : k), IsIdempotentElem e → e = 0 ∨ e = 1) :
  (∃ τ,
      (SimpleGraph.firstCohomologyRelabel kˣ τ)
          ((TauCeti.SkewZigzagParameter.cohomologyClass k G) c) =
        (TauCeti.SkewZigzagParameter.cohomologyClass k G) c') ↔
    ∃ φ,
      ∀ (i : V),
        φ
            ((TauCeti.skewZigzagMk k G c)
              (TauCeti.PathAlgebra.vertexIdempotent k (TauCeti.DoubledQuiver.vertex G i))) ∈
          Submodule.span k
            (Set.range fun j =>
              (TauCeti.skewZigzagMk k G c')
                (TauCeti.PathAlgebra.vertexIdempotent k (TauCeti.DoubledQuiver.vertex G j)))
```

**Couture's classification up to graph automorphisms, permuting form.** Formalized in Tau Ceti as [`TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_vertexPermuting_algEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Skew/Automorphism.html#TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_vertexPermuting_algEquiv).

```lean
TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_vertexPermuting_algEquiv.{u,
    w}
  {k : Type w} [CommRing k] {V : Type u} {G : SimpleGraph V} [Finite V]
  {c c' : TauCeti.SkewZigzagParameter k G} [Nontrivial k] :
  (∃ τ,
      (SimpleGraph.firstCohomologyRelabel kˣ τ)
          ((TauCeti.SkewZigzagParameter.cohomologyClass k G) c) =
        (TauCeti.SkewZigzagParameter.cohomologyClass k G) c') ↔
    ∃ φ σ,
      ∀ (i : V),
        φ
            ((TauCeti.skewZigzagMk k G c)
              (TauCeti.PathAlgebra.vertexIdempotent k (TauCeti.DoubledQuiver.vertex G i))) =
          (TauCeti.skewZigzagMk k G c')
            (TauCeti.PathAlgebra.vertexIdempotent k (TauCeti.DoubledQuiver.vertex G (σ i)))
```

## Sources

- [Tau Ceti documentation: `TauCeti.SkewZigzagParameter.cohomologyClass_eq_iff_exists_vertexFixing_algEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Cohomology.html#TauCeti.SkewZigzagParameter.cohomologyClass_eq_iff_exists_vertexFixing_algEquiv)
- [Source of `TauCeti.SkewZigzagParameter.cohomologyClass_eq_iff_exists_vertexFixing_algEquiv` in TauCeti/RepresentationTheory/Quiver/Zigzag/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/Zigzag/Cohomology.lean#L247)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
