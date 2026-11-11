---
declaration: def
origin: cited
lean: TauCeti.addRestrictedProductSum
statement: formalized
---

# TauCeti.addRestrictedProductSum

An additive restricted product over `ι₁ ⊕ ι₂` with
respect to a filter `𝓕` is the product of the restricted products over the two summands with
respect to the comaps of `𝓕` along `Sum.inl` and `Sum.inr`, coordinatewise the identity in both
directions.

```lean
TauCeti.addRestrictedProductSum.{u₁, u₂, v, w} {ι₁ : Type u₁} {ι₂ : Type u₂} {G : ι₁ ⊕ ι₂ → Type v}
  {S : ι₁ ⊕ ι₂ → Type w} [(k : ι₁ ⊕ ι₂) → Add (G k)] [(k : ι₁ ⊕ ι₂) → SetLike (S k) (G k)]
  [∀ (k : ι₁ ⊕ ι₂), AddMemClass (S k) (G k)] {𝓕 : Filter (ι₁ ⊕ ι₂)} {𝓕₁ : Filter ι₁}
  {𝓕₂ : Filter ι₂} (U : (k : ι₁ ⊕ ι₂) → S k) (h₁ : Filter.comap Sum.inl 𝓕 = 𝓕₁)
  (h₂ : Filter.comap Sum.inr 𝓕 = 𝓕₂) :
  RestrictedProduct (fun k => G k) (fun k => ↑(U k)) 𝓕 ≃+
    RestrictedProduct (fun i => G (Sum.inl i)) (fun i => ↑(U (Sum.inl i))) 𝓕₁ ×
      RestrictedProduct (fun j => G (Sum.inr j)) (fun j => ↑(U (Sum.inr j))) 𝓕₂
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.addRestrictedProductSum`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Sum.html#TauCeti.addRestrictedProductSum).

## Sources

- [Tau Ceti documentation: `TauCeti.addRestrictedProductSum`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Sum.html#TauCeti.addRestrictedProductSum)
- [Source of `TauCeti.addRestrictedProductSum` in TauCeti/Topology/Algebra/RestrictedProduct/Sum.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/RestrictedProduct/Sum.lean#L67)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RestrictedProducts/STATUS.md)
