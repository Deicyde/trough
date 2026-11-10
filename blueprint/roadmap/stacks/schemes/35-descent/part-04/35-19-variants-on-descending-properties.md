---
declaration: section
origin: cited
lean: AlgebraicGeometry.isReduced_of_flat_of_surjective, AlgebraicGeometry.Space.hasEtaleLocalProperty_isRegular_of_isSurjective_of_isFlat_of_isLocallyOfFinitePresentation
statement: formalized
proof: formalized
---

# 35.19 Variants on descending properties

Section 35.19 of the Stacks Project, [Tag 06QL](https://stacks.math.columbia.edu/tag/06QL). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06QM, a lemma

[Tag 06QM](https://stacks.math.columbia.edu/tag/06QM) in the Stacks Project.

**`AlgebraicGeometry.isReduced_of_flat_of_surjective`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SchemeProperty/Reduced.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SchemeProperty/Reduced.lean#L45). References: SGA 3 VIB (2.1.2), “partial”.

> The target of a flat surjective morphism of schemes with reduced source is reduced.

```lean
lemma isReduced_of_flat_of_surjective {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Flat f] [Surjective f] [IsReduced X] : IsReduced Y
```

## Tag 06QN, a lemma

[Tag 06QN](https://stacks.math.columbia.edu/tag/06QN) in the Stacks Project.

**`AlgebraicGeometry.Space.hasEtaleLocalProperty_isRegular_of_isSurjective_of_isFlat_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Regular.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Regular.lean#L109). The attribute's comment: “the same statement in the descent chapter”. References: SGA 1 I (9.2), “converse (X reg ⇒ Y reg)”.

> **Stacks 06MK.** Regularity passes from the source of a surjective, flat morphism of
> algebraic spaces over `S` locally of finite presentation to its target.
>
> A regular scheme is locally Noetherian, so a regular étale chart of the source witnesses local
> Noetherianity of the source; Stacks 06MJ carries that to the target, and
> `hasEtaleLocalProperty_isRegular_of_isSurjective_of_isFlat` then applies.

```lean
theorem hasEtaleLocalProperty_isRegular_of_isSurjective_of_isFlat_of_isLocallyOfFinitePresentation
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hfp : IsLocallyOfFinitePresentation B S hS f)
    (hflat : IsFlat B S hS f)
    (hsurj : IsSurjective B S hS f)
    (hreg : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsRegular T)) :
    HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsRegular T)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.19, Tag 06QL](https://stacks.math.columbia.edu/tag/06QL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
