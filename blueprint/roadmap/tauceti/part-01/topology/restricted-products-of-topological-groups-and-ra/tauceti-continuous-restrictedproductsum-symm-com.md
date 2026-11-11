---
declaration: theorem
origin: cited
lean: TauCeti.continuous_restrictedProductSum_symm_comp_prodMap_inclusion
statement: formalized
proof: formalized
---

# TauCeti.continuous_restrictedProductSum_symm_comp_prodMap_inclusion

On principal stages the inverse of the splitting over a sum is continuous for every filter
and every reference family: for the cofinite filter, openness of the reference subsets is needed
only to pass from the stages to the restricted products themselves.

```lean
TauCeti.continuous_restrictedProductSum_symm_comp_prodMap_inclusion.{u₁, u₂, v, w} {ι₁ : Type u₁}
  {ι₂ : Type u₂} {G : ι₁ ⊕ ι₂ → Type v} {S : ι₁ ⊕ ι₂ → Type w} [(k : ι₁ ⊕ ι₂) → Mul (G k)]
  [(k : ι₁ ⊕ ι₂) → SetLike (S k) (G k)] [∀ (k : ι₁ ⊕ ι₂), MulMemClass (S k) (G k)]
  {𝓕 : Filter (ι₁ ⊕ ι₂)} {𝓕₁ : Filter ι₁} {𝓕₂ : Filter ι₂} (U : (k : ι₁ ⊕ ι₂) → S k)
  (h₁ : Filter.comap Sum.inl 𝓕 = 𝓕₁) (h₂ : Filter.comap Sum.inr 𝓕 = 𝓕₂)
  [(k : ι₁ ⊕ ι₂) → TopologicalSpace (G k)] {S₁ : Set ι₁} {S₂ : Set ι₂}
  (hS₁ : 𝓕₁ ≤ Filter.principal S₁) (hS₂ : 𝓕₂ ≤ Filter.principal S₂) :
  Continuous
    (⇑(TauCeti.restrictedProductSum U h₁ h₂).symm ∘
      Prod.map
        (RestrictedProduct.inclusion (fun i => G (Sum.inl i)) (fun i => ↑(U (Sum.inl i))) hS₁)
        (RestrictedProduct.inclusion (fun j => G (Sum.inr j)) (fun j => ↑(U (Sum.inr j))) hS₂))
```

## Depends on

- [TauCeti.restrictedProductSum](tauceti-restrictedproductsum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.continuous_restrictedProductSum_symm_comp_prodMap_inclusion`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Sum.html#TauCeti.continuous_restrictedProductSum_symm_comp_prodMap_inclusion).

## Sources

- [Tau Ceti documentation: `TauCeti.continuous_restrictedProductSum_symm_comp_prodMap_inclusion`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Sum.html#TauCeti.continuous_restrictedProductSum_symm_comp_prodMap_inclusion)
- [Source of `TauCeti.continuous_restrictedProductSum_symm_comp_prodMap_inclusion` in TauCeti/Topology/Algebra/RestrictedProduct/Sum.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/RestrictedProduct/Sum.lean#L159)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RestrictedProducts/STATUS.md)
