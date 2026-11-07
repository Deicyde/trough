---
declaration: def
origin: cited
lean: TauCeti.zigzagBraidK0Action
statement: formalized
---

# The action of the graph's Artin group on `K₀^gr(proj Z)`

The standard generator at `i`
acts by the deformed simple reflection at `q`, in the basis of vertex-projective classes; by
`TauCeti.zigzagBraidK0Action_gen_zigzagAlgebraGradedProjectiveClass` it sends `[P_j]` to the
Euler class of the braid complex `B_i ⊗_Z P_j`.

```lean
TauCeti.zigzagBraidK0Action.{u, w} (k : Type w) {V : Type u} [Finite V] (G : SimpleGraph V)
  [Field k] [Fintype V] [DecidableEq V] :
  TauCeti.ArtinGroup G.coxeterMatrix →*
    TauCeti.LaurentK0
        (TauCeti.gradedFiniteProjectiveModulesExactStructure
          (TauCeti.zigzagAlgebraIntegerGrade k G)) ≃ₗ[LaurentPolynomial ℤ]
      TauCeti.LaurentK0
        (TauCeti.gradedFiniteProjectiveModulesExactStructure
          (TauCeti.zigzagAlgebraIntegerGrade k G))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.zigzagBraidK0Action`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/K0.html#TauCeti.zigzagBraidK0Action).

## Sources

- [Tau Ceti documentation: `TauCeti.zigzagBraidK0Action`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/K0.html#TauCeti.zigzagBraidK0Action)
- [Source of `TauCeti.zigzagBraidK0Action` in TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/K0.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/K0.lean#L154)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
