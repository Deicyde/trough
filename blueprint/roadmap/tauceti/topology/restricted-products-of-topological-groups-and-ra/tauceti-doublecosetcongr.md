---
declaration: def
origin: cited
lean: TauCeti.doubleCosetCongr
statement: formalized
---

# TauCeti.doubleCosetCongr

Transport of a double-coset space along a change of reference family. The subgroups on the
right are the images of those on the left under `restrictedProductCongr`, not the integral
subgroups of the new family; see `exists_map_integralSubgroup_ne`.

```lean
TauCeti.doubleCosetCongr.{u, v} {ι : Type u} {G : ι → Type v} [(i : ι) → Group (G i)]
  (U U' : (i : ι) → Subgroup (G i)) (h : ∀ᶠ (i : ι) in Filter.cofinite, U i = U' i)
  (Γ K : Subgroup (RestrictedProduct (fun i => G i) (fun i => ↑(U i)) Filter.cofinite)) :
  DoubleCoset.Quotient ↑Γ ↑K ≃
    DoubleCoset.Quotient ↑(Subgroup.map (↑(TauCeti.restrictedProductCongr U U' h)) Γ)
      ↑(Subgroup.map (↑(TauCeti.restrictedProductCongr U U' h)) K)
```

## Depends on

- [TauCeti.restrictedProductCongr](tauceti-restrictedproductcongr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.doubleCosetCongr`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Congr/DoubleCoset.html#TauCeti.doubleCosetCongr).

## Sources

- [Tau Ceti documentation: `TauCeti.doubleCosetCongr`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Congr/DoubleCoset.html#TauCeti.doubleCosetCongr)
- [Source of `TauCeti.doubleCosetCongr` in TauCeti/Topology/Algebra/RestrictedProduct/Congr/DoubleCoset.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/RestrictedProduct/Congr/DoubleCoset.lean#L38)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RestrictedProducts/STATUS.md)
