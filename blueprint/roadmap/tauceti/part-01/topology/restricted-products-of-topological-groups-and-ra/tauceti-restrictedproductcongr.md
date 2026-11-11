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
- [Source of `TauCeti.restrictedProductCongr` in TauCeti/Topology/Algebra/RestrictedProduct/Congr/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/RestrictedProduct/Congr/Basic.lean#L52)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RestrictedProducts/STATUS.md)
