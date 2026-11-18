---
declaration: theorem
origin: cited
lean: CategoryTheory.Sheaf.bijective_postcomp_mk₀_supportedSectionsι
statement: formalized
proof: formalized
---

# Degenerate edge comparison for `n = 0`

If the local cohomology sheaves `𝓗_S^q(F)`
vanish for all `q > 0`, then for every closed `Z ≤ S` the inclusion `Γ_S(F) ⟶ F` induces
bijections `H_Z^j(W, Γ_S(F)) ⟶ H_Z^j(W, F)` in every degree `j`.

```lean
CategoryTheory.Sheaf.bijective_postcomp_mk₀_supportedSectionsι.{u} {X : TopCat}
  (F : CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) AddCommGrpCat)
  {S Z : TopologicalSpace.Closeds ↑X}
  (h : ∀ (q : ℕ), CategoryTheory.Limits.IsZero (F.supportedHSheaf S (q + 1))) (hZS : Z ≤ S)
  (W : TopologicalSpace.Opens ↑X) (j : ℕ) :
  Function.Bijective
    ⇑((CategoryTheory.Abelian.Ext.mk₀ (F.supportedSectionsι S)).postcomp
        (TauCeti.CategoryTheory.relativeFreeYonedaSheaf (Opens.grothendieckTopology ↑X)
          (Z.complInclusion W))
        ⋯)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.bijective_postcomp_mk₀_supportedSectionsι`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/LocalCohomology/Basic.html#CategoryTheory.Sheaf.bijective_postcomp_mk%E2%82%80_supportedSections%CE%B9).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.bijective_postcomp_mk₀_supportedSectionsι`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/LocalCohomology/Basic.html#CategoryTheory.Sheaf.bijective_postcomp_mk%E2%82%80_supportedSections%CE%B9)
- [Source of `CategoryTheory.Sheaf.bijective_postcomp_mk₀_supportedSectionsι` in TauCeti/Topology/Sheaves/LocalCohomology/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Sheaves/LocalCohomology/Basic.lean#L849)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Hyperfunctions/STATUS.md)
