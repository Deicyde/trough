---
declaration: theorem
origin: cited
lean: TauCeti.continuous_rationalDiagonal
statement: formalized
proof: formalized
---

# TauCeti.continuous\_rationalDiagonal

The diagonal is continuous when the coordinate maps are continuous and there is one cofinite
set of indices at which every `γ` is integral. Pointwise eventual integrality alone builds the
map but is not enough for continuity, because the restricted-product topology is finer than the
topology induced from the full product.

```lean
TauCeti.continuous_rationalDiagonal.{u, v, w} {ι : Type u} {G : ι → Type v} [(i : ι) → Group (G i)]
  {Γ : Type w} [MulOneClass Γ] [TopologicalSpace Γ] [(i : ι) → TopologicalSpace (G i)]
  (φ : (i : ι) → Γ →* G i) (U : (i : ι) → Subgroup (G i))
  (h : ∀ (γ : Γ), ∀ᶠ (i : ι) in Filter.cofinite, (φ i) γ ∈ U i)
  (hcont : ∀ (i : ι), Continuous ⇑(φ i)) (S : Set ι) (hS : S ∈ Filter.cofinite)
  (huniform : ∀ (γ : Γ), ∀ i ∈ S, (φ i) γ ∈ U i) : Continuous ⇑(TauCeti.rationalDiagonal φ U h)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.continuous_rationalDiagonal`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Diagonal.html#TauCeti.continuous_rationalDiagonal).

## Sources

- [Tau Ceti documentation: `TauCeti.continuous_rationalDiagonal`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Diagonal.html#TauCeti.continuous_rationalDiagonal)
- [Source of `TauCeti.continuous_rationalDiagonal` in TauCeti/Topology/Algebra/RestrictedProduct/Diagonal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/RestrictedProduct/Diagonal.lean#L158)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RestrictedProducts/STATUS.md)
