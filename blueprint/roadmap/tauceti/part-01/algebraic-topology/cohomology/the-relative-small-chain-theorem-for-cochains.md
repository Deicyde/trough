---
declaration: theorem
origin: cited
lean: TopPair.quasiIso_cochainComplexMap_restrictι_smallSingularSubcomplex
statement: formalized
proof: formalized
---

# The relative small-chain theorem for cochains

Restricting relative singular cochains of
a topological pair to the simplices subordinate to an open cover of the ambient space is a
quasi-isomorphism.

```lean
TopPair.quasiIso_cochainComplexMap_restrictι_smallSingularSubcomplex.{w, v, u, u_1, u_2}
  {C : Type u} [CategoryTheory.Category.{v, u} C] [CategoryTheory.Limits.HasCoproducts C]
  [CategoryTheory.Abelian C] {R : C} {k : Type u_1} [Ring k] [CategoryTheory.Linear k C] {M : C}
  {ι : Type u_2} (P : TopPair) (U : ι → Set ↑TopPair.fst) (hU : ∀ (i : ι), IsOpen (U i))
  (hcov : ⋃ i, U i = Set.univ) :
  QuasiIso
    (SSetPair.cochainComplexMap
      ((TopPair.toSSetPair.obj P).restrictι (P.smallSingularSubcomplex U)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TopPair.quasiIso_cochainComplexMap_restrictι_smallSingularSubcomplex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/Excision.html#TopPair.quasiIso_cochainComplexMap_restrict%CE%B9_smallSingularSubcomplex).

## Sources

- [Tau Ceti documentation: `TopPair.quasiIso_cochainComplexMap_restrictι_smallSingularSubcomplex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/Excision.html#TopPair.quasiIso_cochainComplexMap_restrict%CE%B9_smallSingularSubcomplex)
- [Source of `TopPair.quasiIso_cochainComplexMap_restrictι_smallSingularSubcomplex` in TauCeti/AlgebraicTopology/Cohomology/Excision.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Cohomology/Excision.lean#L76)
