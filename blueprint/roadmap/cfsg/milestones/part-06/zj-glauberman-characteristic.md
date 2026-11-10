---
declaration: theorem
origin: cited
lean: CFSG.Milestones.zj_glauberman_characteristic_1, CFSG.Milestones.zj_glauberman_characteristic_2
statement: formalized
proof: formalized
---

# ZJ_glauberman_characteristic

The milestone module `CFSG.Milestones.ZJ_glauberman_characteristic`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/ZJ_glauberman_characteristic.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/ZJ_glauberman_characteristic.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.zj_glauberman_characteristic_1` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/ZJ_glauberman_characteristic.lean#L12)). Proved here.

```lean
theorem _root_.CFSG.Milestones.zj_glauberman_characteristic_1
    (G : Type) [Group G] [Finite G]
    (p : ℕ) (hp : p.Prime) (hodd : Odd p)
    (hcharp : Subgroup.centralizer (pCore p G : Set G) ≤ pCore p G)
    (S : Sylow p G)
    (hstable : ∀ (P : Subgroup G) [P.Normal], IsPGroup p P → StatedConjPStable p P) :
    ((Subgroup.center (thompsonSubgroup (S : Subgroup G))).map
        (thompsonSubgroup (S : Subgroup G)).subtype).Characteristic
```

`CFSG.Milestones.zj_glauberman_characteristic_2` (theorem, [line 28](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/ZJ_glauberman_characteristic.lean#L28)). Proved here.

```lean
theorem _root_.CFSG.Milestones.zj_glauberman_characteristic_2
    (G : Type) [Group G] [Finite G]
    (p : ℕ) (hp : p.Prime) (hodd : Odd p)
    (hstable : CFSG.Open.IsPStable p G)
    (hconstrained : Subgroup.centralizer (CFSG.Open.pCore p G : Set G) ≤ CFSG.Open.pCore p G)
    (S : Sylow p G) :
    ((Subgroup.center (CFSG.Open.thompsonSubgroup (S : Subgroup G))).map
        (CFSG.Open.thompsonSubgroup (S : Subgroup G)).subtype).Normal
```

The files of 3 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/ZJ_glauberman_characteristic.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/ZJ_glauberman_characteristic.lean)
