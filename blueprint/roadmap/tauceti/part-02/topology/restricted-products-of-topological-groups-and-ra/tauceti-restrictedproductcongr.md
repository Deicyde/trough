---
declaration: def
origin: cited
lean: TauCeti.restrictedProductCongr
statement: formalized
---

# TauCeti.restrictedProductCongr

The multiplicative equivalence between the restricted products with respect to two reference
families that agree at all but finitely many indices. It is the identity in every coordinate.

```lean
TauCeti.restrictedProductCongr.{u, v} {ι : Type u} {G : ι → Type v} [(i : ι) → Group (G i)]
  (U U' : (i : ι) → Subgroup (G i)) (h : ∀ᶠ (i : ι) in Filter.cofinite, U i = U' i) :
  RestrictedProduct (fun i => G i) (fun i => ↑(U i)) Filter.cofinite ≃*
    RestrictedProduct (fun i => G i) (fun i => ↑(U' i)) Filter.cofinite
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.restrictedProductCongr`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Congr/Basic.html#TauCeti.restrictedProductCongr).

## Sources

- [Tau Ceti documentation: `TauCeti.restrictedProductCongr`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Congr/Basic.html#TauCeti.restrictedProductCongr)
- [Source of `TauCeti.restrictedProductCongr` in TauCeti/Topology/Algebra/RestrictedProduct/Congr/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/RestrictedProduct/Congr/Basic.lean#L52)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/RestrictedProducts/STATUS.md)
