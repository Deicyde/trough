---
declaration: theorem
origin: cited
lean: TopPair.isIso_homologyMap_restrictι_smallSingularSubcomplex
statement: formalized
proof: formalized
---

# The relative small-chain theorem

Restricting the singular pair of a topological pair to
the simplices subordinate to an open cover of the ambient space does not change relative
homology.

```lean
TopPair.isIso_homologyMap_restrictι_smallSingularSubcomplex.{w, v, u, u_1} {A : Type u}
  [CategoryTheory.Category.{v, u} A] [CategoryTheory.Limits.HasCoproducts A]
  [CategoryTheory.Abelian A] (R : A) (P : TopPair) {ι : Type u_1} (U : ι → Set ↑TopPair.fst)
  (hU : ∀ (i : ι), IsOpen (U i)) (hcov : ⋃ i, U i = Set.univ) (n : ℕ) :
  CategoryTheory.IsIso
    (SSetPair.homologyMap ((TopPair.toSSetPair.obj P).restrictι (P.smallSingularSubcomplex U)) R n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TopPair.isIso_homologyMap_restrictι_smallSingularSubcomplex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Subdivision/Small/Relative.html#TopPair.isIso_homologyMap_restrict%CE%B9_smallSingularSubcomplex).

## Sources

- [Tau Ceti documentation: `TopPair.isIso_homologyMap_restrictι_smallSingularSubcomplex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Subdivision/Small/Relative.html#TopPair.isIso_homologyMap_restrict%CE%B9_smallSingularSubcomplex)
- [Source of `TopPair.isIso_homologyMap_restrictι_smallSingularSubcomplex` in TauCeti/AlgebraicTopology/Singular/Subdivision/Small/Relative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Singular/Subdivision/Small/Relative.lean#L77)
