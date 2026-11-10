---
declaration: theorem
origin: cited
lean: CFSG.Milestones.brauer_suzuki, CFSG.Milestones.brauer_suzuki_central_involution
statement: formalized
proof: formalized
---

# LR_Brauer_Suzuki_central_involution

The milestone module `CFSG.Milestones.LR_Brauer_Suzuki_central_involution`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/LR_Brauer_Suzuki_central_involution.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_Brauer_Suzuki_central_involution.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.brauer_suzuki` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_Brauer_Suzuki_central_involution.lean#L12)). Proved here.

```lean
theorem _root_.CFSG.Milestones.brauer_suzuki {G : Type*} [Group G] [Finite G]
    (n : ℕ) (hn : 3 ≤ n)
    (P : Sylow 2 G)
    (hquat : Nonempty ((P : Subgroup G) ≃* QuaternionGroup (2 ^ (n - 2))))
    (t : G) (ht_mem : t ∈ (P : Subgroup G)) (ht_ord : orderOf t = 2) :
    (QuotientGroup.mk t : G ⧸ oddCore G) ∈
      Subgroup.center (G ⧸ oddCore G)
```

`CFSG.Milestones.brauer_suzuki_central_involution` (theorem, [line 26](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_Brauer_Suzuki_central_involution.lean#L26)). Proved here.

```lean
theorem _root_.CFSG.Milestones.brauer_suzuki_central_involution {G : Type*} [Group G] [Finite G]
    (n : ℕ) (hn : 3 ≤ n)
    (P : Sylow 2 G)
    (hquat : Nonempty ((P : Subgroup G) ≃* QuaternionGroup (2 ^ (n - 2))))
    (t : G) (ht_mem : t ∈ (P : Subgroup G)) (ht_ord : orderOf t = 2) :
    (QuotientGroup.mk t : G ⧸ oddCore G) ≠ 1 ∧
      (QuotientGroup.mk t : G ⧸ oddCore G) ∈ Subgroup.center (G ⧸ oddCore G)
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/LR_Brauer_Suzuki_central_involution.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_Brauer_Suzuki_central_involution.lean)
