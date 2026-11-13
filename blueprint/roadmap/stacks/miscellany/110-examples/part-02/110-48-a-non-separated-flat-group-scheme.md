---
declaration: section
origin: cited
lean: Stacks.Examples.exists_flat_finiteType_groupScheme_not_isSeparated, AlgebraicGeometry.exists_flat_finiteType_groupScheme_not_quasiSeparated
statement: formalized
proof: formalized
---

# 110.48 A non-separated flat group scheme

Section 110.48 of the Stacks Project, [Tag 06E7](https://stacks.math.columbia.edu/tag/06E7). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06E8, a lemma

[Tag 06E8](https://stacks.math.columbia.edu/tag/06E8) in the Stacks Project.

**`Stacks.Examples.exists_flat_finiteType_groupScheme_not_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/GroupSchemes/NonSeparated.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/GroupSchemes/NonSeparated.lean#L83). References: SGA 3 VIB (5.6.4), “base = affine line”.

> **Stacks Project, Tag 06E8.** There is a flat group scheme of finite type over the affine
> line that is not separated.

```lean
public theorem exists_flat_finiteType_groupScheme_not_isSeparated (k : Type u) [Field k] :
    ∃ G : CategoryTheory.Over (Spec (.of (Polynomial k))),
      Nonempty (GrpObj G) ∧ Flat G.hom ∧ LocallyOfFiniteType G.hom ∧
        QuasiCompact G.hom ∧ ¬ IsSeparated G.hom
```

## Tag 08IX, a lemma

[Tag 08IX](https://stacks.math.columbia.edu/tag/08IX) in the Stacks Project.

**`AlgebraicGeometry.exists_flat_finiteType_groupScheme_not_quasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ObstructionIX/NonQuasiSeparatedGroupScheme.lean, line 609](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/ObstructionIX/NonQuasiSeparatedGroupScheme.lean#L609).

> **Stacks Project, Tag 08IX.** A flat finite-type group scheme over
> infinite-dimensional affine space need not be quasi-separated.

```lean
public theorem exists_flat_finiteType_groupScheme_not_quasiSeparated
    (k : Type u) [Field k] :
    ∃ G : Grp (Over (Spec (.of (MvPolynomial ℕ k)))),
      Flat G.X.hom ∧ LocallyOfFiniteType G.X.hom ∧
        QuasiCompact G.X.hom ∧ ¬ QuasiSeparated G.X.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.48, Tag 06E7](https://stacks.math.columbia.edu/tag/06E7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
