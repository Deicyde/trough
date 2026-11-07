---
declaration: def
origin: cited
lean: TauCeti.restrictedProductMap
statement: formalized
---

# TauCeti.restrictedProductMap

The componentwise homomorphism of restricted products induced by a family that eventually
maps each reference subgroup into the corresponding target subgroup.

```lean
TauCeti.restrictedProductMap.{u, v, w} {ι : Type u} {G : ι → Type v} [(i : ι) → Group (G i)]
  {H : ι → Type w} [(i : ι) → Group (H i)] (U : (i : ι) → Subgroup (G i))
  (U' : (i : ι) → Subgroup (H i)) (φ : (i : ι) → G i →* H i)
  (hφ : ∀ᶠ (i : ι) in Filter.cofinite, Set.MapsTo ⇑(φ i) ↑(U i) ↑(U' i)) :
  RestrictedProduct (fun i => G i) (fun i => ↑(U i)) Filter.cofinite →*
    RestrictedProduct (fun i => H i) (fun i => ↑(U' i)) Filter.cofinite
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.restrictedProductMap`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Map.html#TauCeti.restrictedProductMap).

## Sources

- [Tau Ceti documentation: `TauCeti.restrictedProductMap`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Map.html#TauCeti.restrictedProductMap)
- [Source of `TauCeti.restrictedProductMap` in TauCeti/Topology/Algebra/RestrictedProduct/Map.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/RestrictedProduct/Map.lean#L44)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RestrictedProducts/STATUS.md)
