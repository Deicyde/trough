---
declaration: theorem
origin: cited
lean: CFSG.classification_finite_simple_groups
statement: formalized
proof: formalized
---

# CFSG.classification_finite_simple_groups

The proof's top theorem, quoted from [CFSG/Statement.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Statement.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.classification_finite_simple_groups` (theorem, [line 4923](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Statement.lean#L4923)). Proved here.

```lean
theorem classification_finite_simple_groups
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G] :
    ∃ i : TauCeti.CFSGIndex, Nonempty (G ≃* i.Group)
```

Its proof applies [`CFSG.Assembly.classification`](reduction.md) to the catalog `CFSG.Assembly.InCatalog` and to a theorem for each of the reduction's 9 hypotheses, in its order:

- `hodd : OddOrderStatement`: [`CFSG.FeitThompson.isSolvable_of_odd_natCard`](case-hodd-oddorderstatement.md)
- `hab : AbelianStatement`: [`CFSG.Assembly.abelian_simple`](case-hab-abelianstatement.md)
- `hdisc : DisconnectedStatement`: [`CFSG.Assembly.disconnected_involution_graph`](case-hdisc-disconnectedstatement.md)
- `hlow : LowTwoRankStatement`: [`CFSG.Assembly.low_two_rank`](case-hlow-lowtworankstatement.md)
- `hdich : DichotomyStatement`: [`CFSG.Assembly.component_dichotomy`](case-hdich-dichotomystatement.md)
- `hcomp : ComponentStatement`: [`CFSG.Assembly.component_type`](case-hcomp-componentstatement.md)
- `hqt : QuasithinStatement`: [`CFSG.Assembly.quasithin`](case-hqt-quasithinstatement.md)
- `hr3 : RankThreeStatement`: [`CFSG.Assembly.rank_three_even`](case-hr3-rankthreestatement.md)
- `hle : LargeEvenStatement`: [`CFSG.Assembly.large_even`](case-hle-largeevenstatement.md)

The catalog, declared in [CFSG/Assembly/InCatalog.lean, line 10](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/InCatalog.lean#L10):

```lean
@[expose] def InCatalog : GroupProp := fun G _ => ∃ i : TauCeti.CFSGIndex, Nonempty (G ≃* i.Group)
```

## Depends on

Its statement uses no other result mapped here.

## Proof depends on

- [CFSG.Assembly.Reduction](reduction.md)
- [CFSG.FeitThompson.isSolvable_of_odd_natCard](case-hodd-oddorderstatement.md)
- [CFSG.Assembly.abelian_simple](case-hab-abelianstatement.md)
- [CFSG.Assembly.disconnected_involution_graph](case-hdisc-disconnectedstatement.md)
- [CFSG.Assembly.low_two_rank](case-hlow-lowtworankstatement.md)
- [CFSG.Assembly.component_dichotomy](case-hdich-dichotomystatement.md)
- [CFSG.Assembly.component_type](case-hcomp-componentstatement.md)
- [CFSG.Assembly.quasithin](case-hqt-quasithinstatement.md)
- [CFSG.Assembly.rank_three_even](case-hr3-rankthreestatement.md)
- [CFSG.Assembly.large_even](case-hle-largeevenstatement.md)

## Sources

- [CFSG/Statement.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Statement.lean#L4923)
