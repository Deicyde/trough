---
declaration: section
origin: cited
lean: Stacks.Topology.CategoryStalk.stalk_exists, Stacks.Topology.CategoryStalk.stalkUnderlyingSetIso, Stacks.Topology.CategoryStalk.stalkFunctor
statement: formalized
proof: formalized
---

# 6.13 Stalks of presheaves of algebraic structures

Section 6.13 of the Stacks Project, [Tag 007G](https://stacks.math.columbia.edu/tag/007G). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 007H, a lemma

[Tag 007H](https://stacks.math.columbia.edu/tag/007H) in the Stacks Project.

**`Stacks.Topology.CategoryStalk.stalk_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/ValuedInCategory.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Stalk/ValuedInCategory.lean#L96).

> **Existence of the stalk.** Assuming filtered colimits of the appropriate size
> exist in `C`, the directed colimit
>   `ℱ_x = colim_{x ∈ U} ℱ(U)`
> exists in `C`.

```lean
theorem stalk_exists
    {C : Type u} [Category.{v} C]
    [HasFilteredColimitsOfSize.{v, v} C]
    {X : TopCat.{v}} (x : X) (ℱ : TopCat.Presheaf C X) :
    HasColimit (stalkDiagram x ℱ)
```

**`Stacks.Topology.CategoryStalk.stalkUnderlyingSetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/ValuedInCategory.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Stalk/ValuedInCategory.lean#L121).

> **Underlying set of the stalk.** Applying `F` to the stalk `ℱ_x` yields the stalk
> of the underlying presheaf of sets: the canonical comparison morphism furnishes an
> isomorphism in `Type v`
>   `F(ℱ_x) ≅ colim_{x ∈ U} F(ℱ(U)) = (F ∘ ℱ)_x`.
>
> The isomorphism is `preservesColimitIso F (stalkDiagram x ℱ)` composed with the
> identification of the two diagrams from `stalkDiagram_comp_eq`.

```lean
noncomputable def stalkUnderlyingSetIso
    {C : Type u} [Category.{v} C]
    (F : C ⥤ Type v) [F.Faithful]
    [HasFilteredColimitsOfSize.{v, v} C] [PreservesFilteredColimits.{v} F]
    {X : TopCat.{v}} (x : X) (ℱ : TopCat.Presheaf C X) :
    haveI : HasColimit (stalkDiagram x ℱ) := stalk_exists x ℱ
    haveI : HasColimit (stalkDiagram x (underlyingPresheafOfSets F ℱ)) :=
      stalk_exists (C := Type v) x (underlyingPresheafOfSets F ℱ)
    F.obj (colimit (stalkDiagram x ℱ)) ≅
      colimit (stalkDiagram x (underlyingPresheafOfSets F ℱ))
```

**`Stacks.Topology.CategoryStalk.stalkFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/ValuedInCategory.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Stalk/ValuedInCategory.lean#L145). References: EGA 0 (3.1.6).

> **Functoriality.** The stalk construction `ℱ ↦ ℱ_x` extends to a functor
>   `(·)_x : TopCat.Presheaf C X ⥤ C`.
> Concretely, every morphism of presheaves `φ : ℱ ⟶ 𝒢` induces (by the universal
> property of the colimit) a morphism `φ_x : ℱ_x ⟶ 𝒢_x` in `C`, and this assignment
> respects identities and composition: the functor is the whiskering by
> `(OpenNhds.inclusion x).op` followed by taking the colimit.

```lean
noncomputable def stalkFunctor
    (C : Type u) [Category.{v} C]
    [HasFilteredColimitsOfSize.{v, v} C]
    {X : TopCat.{v}} (x : X) :
    TopCat.Presheaf C X ⥤ C
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.13, Tag 007G](https://stacks.math.columbia.edu/tag/007G)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
