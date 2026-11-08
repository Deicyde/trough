---
declaration: theorem
origin: cited
lean: TauCeti.freeProfiniteGroup.abelianizationProPEquivRelationModule_smul
statement: formalized
proof: formalized
---

# Lyndon's isomorphism is equivariant

conjugation by `f ∈ F` on `R^ab(p)`, through
`F ⧸ R`, corresponds to multiplication by `lift g f` on the relation module.

```lean
TauCeti.freeProfiniteGroup.abelianizationProPEquivRelationModule_smul.{u} (p : ℕ)
  [Fact (Nat.Prime p)] {G : Type u} [Group G] [Finite G] [TopologicalSpace G] [DiscreteTopology G]
  {ι : Type u} {g : ι → G} (hg : Subgroup.closure (Set.range g) = ⊤) [DecidableEq ι] [Fintype ι]
  (f : ↑(TauCeti.freeProfiniteGroup ι).toProfinite.toTop)
  (x :
    Additive
      (TauCeti.abelianizationProP p (↑(TauCeti.freeProfiniteGroup ι).toProfinite.toTop)
        (↑(TauCeti.freeProfiniteGroup.lift g)).ker)) :
  (TauCeti.freeProfiniteGroup.abelianizationProPEquivRelationModule p hg) (↑f • x) =
    MonoidAlgebra.single ((TauCeti.freeProfiniteGroup.lift g) f) 1 •
      (TauCeti.freeProfiniteGroup.abelianizationProPEquivRelationModule p hg) x
```

## Depends on

- [Lyndon's theorem for the relation module (NSW (5.6.6))](lyndons-theorem-for-the-relation-module-nsw-5-6.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProfiniteGroup.abelianizationProPEquivRelationModule_smul`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/RelationModule/Basic.html#TauCeti.freeProfiniteGroup.abelianizationProPEquivRelationModule_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProfiniteGroup.abelianizationProPEquivRelationModule_smul`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/RelationModule/Basic.html#TauCeti.freeProfiniteGroup.abelianizationProPEquivRelationModule_smul)
- [Source of `TauCeti.freeProfiniteGroup.abelianizationProPEquivRelationModule_smul` in TauCeti/Topology/Algebra/Group/Profinite/Free/RelationModule/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/RelationModule/Basic.lean#L599)
