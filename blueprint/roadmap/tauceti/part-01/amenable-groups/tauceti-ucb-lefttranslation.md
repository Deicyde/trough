---
declaration: def
origin: cited
lean: TauCeti.UCB.leftTranslation
statement: formalized
---

# TauCeti.UCB.leftTranslation

Left translation `g ↦ L_g`, where `(L_g f)(x) = f (g⁻¹ * x)`, as a group homomorphism from `G`
to the linear isometry equivalences of `UCB G`; the case `𝕜 = ℝ` of
`ucbSubalgebra.leftTranslation`.

```lean
TauCeti.UCB.leftTranslation.{u_2} {G : Type u_2} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] : G →* TauCeti.UCB G ≃ₗᵢ[ℝ] TauCeti.UCB G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UCB.leftTranslation`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/UCB/Translation.html#TauCeti.UCB.leftTranslation).

## Sources

- [Tau Ceti documentation: `TauCeti.UCB.leftTranslation`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/UCB/Translation.html#TauCeti.UCB.leftTranslation)
- [Source of `TauCeti.UCB.leftTranslation` in TauCeti/Topology/Algebra/Group/UCB/Translation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/UCB/Translation.lean#L132)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AmenableGroups/STATUS.md)
