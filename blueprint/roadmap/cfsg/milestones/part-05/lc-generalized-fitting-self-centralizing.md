---
declaration: theorem
origin: cited
lean: CFSG.Milestones.lc_generalized_fitting_self_centralizing, CFSG.Milestones.lc_generalized_fitting_self_centralizing_stated
statement: formalized
proof: formalized
---

# LC_generalized_fitting_self_centralizing

The milestone module `CFSG.Milestones.LC_generalized_fitting_self_centralizing`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/LC_generalized_fitting_self_centralizing.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_generalized_fitting_self_centralizing.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.lc_generalized_fitting_self_centralizing` (theorem, [line 11](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_generalized_fitting_self_centralizing.lean#L11)). Proved here.

```lean
theorem lc_generalized_fitting_self_centralizing (G : Type u) [Group G] [Finite G] :
    Subgroup.centralizer
      (CFSG.GorensteinWalter.generalizedFittingSubgroupOf (⊤ : Subgroup G) : Set G) ≤
      CFSG.GorensteinWalter.generalizedFittingSubgroupOf (⊤ : Subgroup G)
```

`CFSG.Milestones.lc_generalized_fitting_self_centralizing_stated` (theorem, [line 22](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_generalized_fitting_self_centralizing.lean#L22)). Proved here.

```lean
theorem _root_.CFSG.Milestones.lc_generalized_fitting_self_centralizing_stated
    (G : Type) [Group G] [Finite G] :
    Subgroup.centralizer (genFittingFStar G : Set G) ≤ genFittingFStar G
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/LC_generalized_fitting_self_centralizing.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_generalized_fitting_self_centralizing.lean)
