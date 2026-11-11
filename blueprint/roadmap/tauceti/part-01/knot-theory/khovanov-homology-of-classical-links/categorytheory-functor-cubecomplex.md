---
declaration: def
origin: cited
lean: CategoryTheory.Functor.cubeComplex
statement: formalized
---

# CategoryTheory.Functor.cubeComplex

The signed totalization of the commutative cube `F`: in degree `r` it is the biproduct of
the vertices `F(S)` of height `#S = r`, with differential the sum of the edge maps
`F(S) ⟶ F(S ∪ {a})`, signed by `(-1)` to the number of elements of `S` below `a`. It is
characterised by the summand inclusions `Functor.cubeComplexι` and projections
`Functor.cubeComplexπ`, and by `Functor.ι_cubeComplex_d`.

```lean
CategoryTheory.Functor.cubeComplex.{w, v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] [CategoryTheory.Limits.HasFiniteBiproducts C] {ι : Type w}
  [Fintype ι] [LinearOrder ι] (F : CategoryTheory.Functor (Finset ι) C) : CochainComplex C ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.cubeComplex`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Cube/Basic.html#CategoryTheory.Functor.cubeComplex).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.cubeComplex`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Cube/Basic.html#CategoryTheory.Functor.cubeComplex)
- [Source of `CategoryTheory.Functor.cubeComplex` in TauCeti/Algebra/Homology/Cube/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/Cube/Basic.lean#L152)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/KhovanovHomology/STATUS.md)
