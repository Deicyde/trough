---
declaration: section
origin: cited
lean: Deformation.GroupoidInFunctors.IsProrepresentable, Deformation.GroupoidInFunctors.completion, Deformation.GroupoidInFunctors.completionRestrictIso, Deformation.GroupoidInFunctors.completionRestrictionIso, Deformation.GroupoidInFunctors.isProrepresentable_iff_isRepresentable_completion, Deformation.GroupoidInFunctors.isProrepresentable_iff_objects_arrows
statement: formalized
proof: formalized
---

# 90.22 Groupoids in functors on the base category

Section 90.22 of the Stacks Project, [Tag 06KC](https://stacks.math.columbia.edu/tag/06KC). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06KD, a definition

[Tag 06KD](https://stacks.math.columbia.edu/tag/06KD) in the Stacks Project.

**`Deformation.GroupoidInFunctors.IsProrepresentable`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/BaseCategory.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/BaseCategory.lean#L102). References: SGA 7 VI (2.13), “prorepresentable”.

> A groupoid in functors on Artinian local `Λ`-algebras is prorepresentable
> if it is isomorphic to the restriction of a representable groupoid in functors
> on Noetherian complete local `Λ`-algebras.

```lean
public abbrev GroupoidInFunctors.IsProrepresentable {Λ : Type u} {k : Type w} [CommRing Λ]
    [Field k] [Algebra Λ k]
    (G : GroupoidInFunctors.{_, v, max v z}
      (ArtinianLocalAlgCat.{u, v, w} Λ k)) : Prop
```

## Tag 06KE, a definition

[Tag 06KE](https://stacks.math.columbia.edu/tag/06KE) in the Stacks Project.

**`Deformation.GroupoidInFunctors.completion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/Groupoid/Completion.lean, line 887](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Formal/Groupoid/Completion.lean#L887).

> Completion of a groupoid in functors on Artinian local algebras.

```lean
public noncomputable def completion {Λ : Type u} {k : Type w} [CommRing Λ]
    [Field k] [Algebra Λ k]
    (G : GroupoidInFunctors.{_, v, max v z}
      (ArtinianLocalAlgCat.{u, v, w} Λ k)) :
    GroupoidInFunctors.{_, v, max v z}
      (CompleteLocalAlgCat.{u, v, w} Λ k)
```

## Tag 06KF, a remark

[Tag 06KF](https://stacks.math.columbia.edu/tag/06KF) in the Stacks Project.

**`Deformation.GroupoidInFunctors.completionRestrictIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/Groupoid/CompletionRestrict.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Formal/Groupoid/CompletionRestrict.lean#L43). The attribute's comment: “completion\_restrict”.

> The canonical isomorphism from a completed groupoid, restricted back to
> Artinian local algebras, to the original groupoid. Its two components are the
> completion--restriction counits.

```lean
public noncomputable def completionRestrictIso
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (G : GroupoidInFunctors.{_, v, max v z}
      (ArtinianLocalAlgCat.{u, v, w} Λ k)) :
    { e : GroupoidInFunctors.restrict
          (GroupoidInFunctors.completion G)
          (artinianToComplete (Λ := Λ) (k := k)) ≅ G //
      e.hom.mapObjects =
        (cofiberedCompletionAdjunction
          (Λ := Λ) (k := k)).counit.app G.objects ∧
      e.hom.mapArrows =
        (cofiberedCompletionAdjunction
          (Λ := Λ) (k := k)).counit.app G.arrows }
```

**`Deformation.GroupoidInFunctors.completionRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/Groupoid/RestrictCompletion.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Formal/Groupoid/RestrictCompletion.lean#L158). The attribute's comment: “restrict\_completion”.

> The canonical groupoid isomorphism from the completion of a restricted
> limit-preserving groupoid to the original groupoid.

```lean
public noncomputable def completionRestrictionIso
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (G : GroupoidInFunctors.{_, v, max v z}
      (CompleteLocalAlgCat.{u, v, w} Λ k))
    [PreservesLimits G.objects] [PreservesLimits G.arrows] :
    { i : GroupoidInFunctors.completion
        (GroupoidInFunctors.restrict G
          (artinianToComplete (Λ := Λ) (k := k))) ≅ G //
      i.inv.mapObjects =
        (cofiberedCompletionAdjunction (Λ := Λ) (k := k)).unit.app
          G.objects ∧
      i.inv.mapArrows =
        (cofiberedCompletionAdjunction (Λ := Λ) (k := k)).unit.app
          G.arrows }
```

## Tag 06KG, a lemma

[Tag 06KG](https://stacks.math.columbia.edu/tag/06KG) in the Stacks Project.

**`Deformation.GroupoidInFunctors.isProrepresentable_iff_isRepresentable_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/Groupoid/Prorepresentable.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Formal/Groupoid/Prorepresentable.lean#L461). The attribute's comment: “part (1)”.

> A groupoid in functors on Artinian local algebras is prorepresentable if
> and only if its completion is representable on complete local algebras.

```lean
public theorem isProrepresentable_iff_isRepresentable_completion
    (G : GroupoidInFunctors.{_, v, max v z}
      (ArtinianLocalAlgCat.{u, v, w} Λ k)) :
    GroupoidInFunctors.IsProrepresentable G ↔
      IsRepresentable (GroupoidInFunctors.completion G)
```

**`Deformation.GroupoidInFunctors.isProrepresentable_iff_objects_arrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/Groupoid/Prorepresentable.lean, line 500](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Formal/Groupoid/Prorepresentable.lean#L500). The attribute's comment: “part (2)”.

> A groupoid in functors is prorepresentable if and only if both its object
> and arrow functors are prorepresentable.

```lean
public theorem isProrepresentable_iff_objects_arrows
    (G : GroupoidInFunctors.{_, v, v}
      (ArtinianLocalAlgCat.{u, v, w} Λ k)) :
    GroupoidInFunctors.IsProrepresentable G ↔
      (_root_.Deformation.IsProrepresentable G.objects ∧
        _root_.Deformation.IsProrepresentable G.arrows)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.22, Tag 06KC](https://stacks.math.columbia.edu/tag/06KC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
