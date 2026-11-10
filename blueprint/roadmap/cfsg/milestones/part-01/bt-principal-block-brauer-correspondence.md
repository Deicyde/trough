---
declaration: theorem
origin: cited
lean: CFSG.Milestones.brauer_third_main_theorem
statement: formalized
proof: formalized
---

# BT_principal_block_Brauer_correspondence

The milestone module `CFSG.Milestones.BT_principal_block_Brauer_correspondence`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/BT_principal_block_Brauer_correspondence.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/BT_principal_block_Brauer_correspondence.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.brauer_third_main_theorem` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/BT_principal_block_Brauer_correspondence.lean#L12)). Proved here.

```lean
theorem _root_.CFSG.Milestones.brauer_third_main_theorem (p : ℕ) (hp : p.Prime) (m : Ideal BlocksAlgInt) (hm : m.IsMaximal)
    (hpm : (p : BlocksAlgInt) ∈ m)
    (G : Type) [Group G] [Finite G] (P H : Subgroup G) (hP : IsPGroup p P)
    (hPH : P ≤ H) (hCH : Subgroup.centralizer (P : Set G) ≤ H)
    (hHN : H ≤ Subgroup.normalizer (P : Set G))
    (β : Set (H → ℂ)) (hβ : BlocksIsBlock m H β) :
    BlocksBrauerCorr m P H β (BlocksPrincipalBlock m G) ↔ β = BlocksPrincipalBlock m H
```

No case theorem's file imports it, directly or through other files.

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/BT_principal_block_Brauer_correspondence.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/BT_principal_block_Brauer_correspondence.lean)
