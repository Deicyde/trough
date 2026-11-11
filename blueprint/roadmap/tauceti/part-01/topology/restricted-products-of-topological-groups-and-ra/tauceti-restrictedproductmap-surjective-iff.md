---
declaration: theorem
origin: cited
lean: TauCeti.restrictedProductMap_surjective_iff
statement: formalized
proof: formalized
---

# TauCeti.restrictedProductMap_surjective_iff

A componentwise restricted-product homomorphism is surjective exactly when every coordinate
map is surjective and, at all but finitely many indices, the coordinate map carries the source
reference subgroup onto the target one. Surjectivity of each coordinate map alone is not enough:
an element of the target may lie in the target reference subgroups at infinitely many indices
where no preimage lies in the source reference subgroup.

```lean
TauCeti.restrictedProductMap_surjective_iff.{u, v, w} {ι : Type u} {G : ι → Type v}
  [(i : ι) → Group (G i)] {H : ι → Type w} [(i : ι) → Group (H i)] (U : (i : ι) → Subgroup (G i))
  (U' : (i : ι) → Subgroup (H i)) (φ : (i : ι) → G i →* H i)
  (hφ : ∀ᶠ (i : ι) in Filter.cofinite, Set.MapsTo ⇑(φ i) ↑(U i) ↑(U' i)) :
  Function.Surjective ⇑(TauCeti.restrictedProductMap U U' φ hφ) ↔
    (∀ (i : ι), Function.Surjective ⇑(φ i)) ∧
      ∀ᶠ (i : ι) in Filter.cofinite, Set.SurjOn ⇑(φ i) ↑(U i) ↑(U' i)
```

## Depends on

- [TauCeti.restrictedProductMap](tauceti-restrictedproductmap.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.restrictedProductMap_surjective_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Map.html#TauCeti.restrictedProductMap_surjective_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.restrictedProductMap_surjective_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Map.html#TauCeti.restrictedProductMap_surjective_iff)
- [Source of `TauCeti.restrictedProductMap_surjective_iff` in TauCeti/Topology/Algebra/RestrictedProduct/Map.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/RestrictedProduct/Map.lean#L137)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RestrictedProducts/STATUS.md)
