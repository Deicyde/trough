---
declaration: def
origin: cited
lean: TauCeti.subcomplexSmallChainHomotopyEquiv
statement: formalized
---

# The small-chain theorem on an affinely stable subcomplex

For an open cover `U` of `X`
and an affinely stable subcomplex `S` of the singular simplicial set of `X`, the inclusion of the
chains of the simplices of `S` subordinate to `U` into the chains of `S` is a chain homotopy
equivalence, whose homotopy inverse is even a strict retraction.

```lean
TauCeti.subcomplexSmallChainHomotopyEquiv.{w, v, u, u_1} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasCoproducts C] (R : C) {X : TopCat}
  (S : (TopCat.toSSet.obj X).Subcomplex) [S.IsAffineStable] {ι : Type u_1} (U : ι → Set ↑X)
  (hU : ∀ (i : ι), IsOpen (U i)) (hcov : ⋃ i, U i = Set.univ) :
  HomotopyEquiv ((S ⊓ X.smallSingularSubcomplex U).toSSet.chainComplex R) (S.toSSet.chainComplex R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.subcomplexSmallChainHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Subdivision/Small/Subcomplex.html#TauCeti.subcomplexSmallChainHomotopyEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.subcomplexSmallChainHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Subdivision/Small/Subcomplex.html#TauCeti.subcomplexSmallChainHomotopyEquiv)
- [Source of `TauCeti.subcomplexSmallChainHomotopyEquiv` in TauCeti/AlgebraicTopology/Singular/Subdivision/Small/Subcomplex.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/Subdivision/Small/Subcomplex.lean#L151)
