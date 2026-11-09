---
declaration: theorem
origin: cited
lean: TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_graded_algEquiv
statement: formalized
proof: formalized
---

# Couture's graded classification by `Aut(G)`-orbits on `H¹(G, kˣ)`

Over a nontrivial
commutative ring with only trivial idempotents, the cohomology classes of two parameters lie
in the same graph-automorphism orbit exactly when their skew-zigzag relation quotients are
graded isomorphic. Together with `cohomologyClass_surjective`, this describes all graded
isomorphism classes of the relation quotients arising from skew-zigzag parameters.

```lean
TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_graded_algEquiv.{u, w}
  {k : Type w} [CommRing k] [Nontrivial k] {V : Type u} [Finite V] {G : SimpleGraph V}
  {c c' : TauCeti.SkewZigzagParameter k G}
  (hidempotents : ∀ (e : k), IsIdempotentElem e → e = 0 ∨ e = 1) :
  (∃ τ,
      (SimpleGraph.firstCohomologyRelabel kˣ τ)
          ((TauCeti.SkewZigzagParameter.cohomologyClass k G) c) =
        (TauCeti.SkewZigzagParameter.cohomologyClass k G) c') ↔
    ∃ φ,
      ∀ (n : ℕ) (x : TauCeti.skewZigzagQuotient k G c),
        φ x ∈ TauCeti.skewZigzagGrade k G c' n ↔ x ∈ TauCeti.skewZigzagGrade k G c n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_graded_algEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Skew/Classification.html#TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_graded_algEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_graded_algEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Skew/Classification.html#TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_graded_algEquiv)
- [Source of `TauCeti.SkewZigzagParameter.exists_firstCohomologyRelabel_eq_iff_exists_graded_algEquiv` in TauCeti/RepresentationTheory/Quiver/Zigzag/Skew/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/Zigzag/Skew/Classification.lean#L78)
