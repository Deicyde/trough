---
declaration: theorem
origin: cited
lean: TauCeti.quasiIso_cubicalChainComplexProdToSingular
statement: formalized
proof: formalized
---

# The small-chain theorem for a product of open pairs

for open `A ⊆ X` and `B ⊆ Y`, the
comparison `N(P × Q) ⟶ C(X × Y, A × Y ∪ X × B)` of the relative cubical chains of the product of
the pairs `P = (X, A)` and `Q = (Y, B)` with relative singular chains is a quasi-isomorphism.

```lean
TauCeti.quasiIso_cubicalChainComplexProdToSingular.{u} (k : Type u) [Ring k] {X Y : TopCat}
  {A : Set ↑X} {B : Set ↑Y} (hA : IsOpen A) (hB : IsOpen B) :
  QuasiIso (TauCeti.cubicalChainComplexProdToSingular k A B)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The relative small-chain theorem](the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.quasiIso_cubicalChainComplexProdToSingular`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Excisive.html#TauCeti.quasiIso_cubicalChainComplexProdToSingular).

## Sources

- [Tau Ceti documentation: `TauCeti.quasiIso_cubicalChainComplexProdToSingular`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Excisive.html#TauCeti.quasiIso_cubicalChainComplexProdToSingular)
- [Source of `TauCeti.quasiIso_cubicalChainComplexProdToSingular` in TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Excisive.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Excisive.lean#L235)
