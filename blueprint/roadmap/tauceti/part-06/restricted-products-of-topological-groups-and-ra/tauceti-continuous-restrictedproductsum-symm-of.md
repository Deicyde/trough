---
declaration: theorem
origin: cited
lean: TauCeti.continuous_restrictedProductSum_symm_of_principal
statement: formalized
proof: formalized
---

# TauCeti.continuous\_restrictedProductSum\_symm\_of\_principal

For a principal filter on `ι₁ ⊕ ι₂` the inverse of the splitting is continuous for every
reference family, so that the splitting is a homeomorphism: the target is a principal stage,
whose topology is induced from the product.

```lean
TauCeti.continuous_restrictedProductSum_symm_of_principal.{u₁, u₂, v, w} {ι₁ : Type u₁}
  {ι₂ : Type u₂} {G : ι₁ ⊕ ι₂ → Type v} {S : ι₁ ⊕ ι₂ → Type w} [(k : ι₁ ⊕ ι₂) → Mul (G k)]
  [(k : ι₁ ⊕ ι₂) → SetLike (S k) (G k)] [∀ (k : ι₁ ⊕ ι₂), MulMemClass (S k) (G k)] {𝓕₁ : Filter ι₁}
  {𝓕₂ : Filter ι₂} (U : (k : ι₁ ⊕ ι₂) → S k) [(k : ι₁ ⊕ ι₂) → TopologicalSpace (G k)]
  {T : Set (ι₁ ⊕ ι₂)} (hT₁ : Filter.comap Sum.inl (Filter.principal T) = 𝓕₁)
  (hT₂ : Filter.comap Sum.inr (Filter.principal T) = 𝓕₂) :
  Continuous ⇑(TauCeti.restrictedProductSum U hT₁ hT₂).symm
```

## Depends on

- [TauCeti.restrictedProductSum](tauceti-restrictedproductsum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.continuous_restrictedProductSum_symm_of_principal`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Sum.html#TauCeti.continuous_restrictedProductSum_symm_of_principal).

## Sources

- [Tau Ceti documentation: `TauCeti.continuous_restrictedProductSum_symm_of_principal`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Sum.html#TauCeti.continuous_restrictedProductSum_symm_of_principal)
- [Source of `TauCeti.continuous_restrictedProductSum_symm_of_principal` in TauCeti/Topology/Algebra/RestrictedProduct/Sum.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/RestrictedProduct/Sum.lean#L142)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RestrictedProducts/STATUS.md)
