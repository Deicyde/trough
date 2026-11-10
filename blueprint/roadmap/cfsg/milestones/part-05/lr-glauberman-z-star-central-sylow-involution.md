---
declaration: theorem
origin: cited
lean: CFSG.Milestones.glauberman_zStar, CFSG.Milestones.glauberman_zStar_central_sylow_involution
statement: formalized
proof: formalized
---

# LR_Glauberman_Z_star_central_Sylow_involution

The milestone module `CFSG.Milestones.LR_Glauberman_Z_star_central_Sylow_involution`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/LR_Glauberman_Z_star_central_Sylow_involution.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_Glauberman_Z_star_central_Sylow_involution.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.glauberman_zStar` (theorem, [line 11](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_Glauberman_Z_star_central_Sylow_involution.lean#L11)). Proved here.

```lean
theorem _root_.CFSG.Milestones.glauberman_zStar (G : Type) [Group G] [Fintype G]
    (t : G) (ht1 : t ≠ 1) (ht2 : t * t = 1)
    (hisolated : ∀ g : G, (g * t * g⁻¹) * t = t * (g * t * g⁻¹) →
      g * t * g⁻¹ = t) :
    ∃ N : Subgroup G, N.Normal ∧ Odd (Nat.card N) ∧
      ∀ g : G, g * t * g⁻¹ * t⁻¹ ∈ N
```

`CFSG.Milestones.glauberman_zStar_central_sylow_involution` (theorem, [line 24](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_Glauberman_Z_star_central_Sylow_involution.lean#L24)). Proved here.

```lean
theorem _root_.CFSG.Milestones.glauberman_zStar_central_sylow_involution {G : Type} [Group G] [Finite G] (S : Sylow 2 G)
    (z : (S : Subgroup G)) (hzZ : z ∈ Subgroup.center (S : Subgroup G)) (hz : orderOf z = 2)
    (hwc : ∀ g : G, g⁻¹ * (z : G) * g ∈ (S : Subgroup G) → g⁻¹ * (z : G) * g = z) :
    (∀ g : G, ∃ c ∈ Subgroup.centralizer ({(z : G)} : Set G), ∃ k ∈ oddCore G, g = c * k) ∧
      (QuotientGroup.mk (z : G) : G ⧸ oddCore G) ∈ Subgroup.center (G ⧸ oddCore G)
```

The files of 5 case theorems import it, directly or through other files: [`CFSG.Assembly.low_two_rank`](../../case-division/case-hlow-lowtworankstatement.md), [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/LR_Glauberman_Z_star_central_Sylow_involution.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_Glauberman_Z_star_central_Sylow_involution.lean)
