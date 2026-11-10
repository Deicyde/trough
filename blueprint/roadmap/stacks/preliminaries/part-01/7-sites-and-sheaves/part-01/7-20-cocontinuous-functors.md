---
declaration: section
origin: cited
lean: CategoryTheory.Functor.IsCocontinuous, CategoryTheory.Functor.sheafAdjunctionPullbackCocontinuous, CategoryTheory.Functor.preservesFiniteColimits_sheafPullbackCocontinuous, CategoryTheory.Functor.preservesFiniteLimits_sheafPullbackCocontinuous, CategoryTheory.Functor.morphismOfTopoi_of_isCocontinuous, sheafifyRestrictionIsoSheafifyRestrictionSheafify
statement: formalized
proof: formalized
---

# 7.20 Cocontinuous functors

Section 7.20 of the Stacks Project, [Tag 00XI](https://stacks.math.columbia.edu/tag/00XI). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00XJ, a definition

[Tag 00XJ](https://stacks.math.columbia.edu/tag/00XJ) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.IsCocontinuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.IsCocontinuous#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Cocontinuous/CocontinuousDefs.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Cocontinuous/CocontinuousDefs.lean#L23) (StacksCore): “a functor between sites is cocontinuous when every covering of `u U` in `D` is refined by the image of a covering of `U` in `C`”. References: SGA 4 III (2.1); SGA 4 IV (4.7).

## Tag 00XL, a lemma

[Tag 00XL](https://stacks.math.columbia.edu/tag/00XL) in the Stacks Project.

**`CategoryTheory.Functor.sheafAdjunctionPullbackCocontinuous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoverLifting.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L83). References: SGA 4 III (5.3), “more general”; SGA 4 IV (4.6.1), “partial”; SGA 4 IV (4.7), “partial”.

> **Stacks 00XL**, the adjunction. For a cocontinuous functor `u : C ⥤ D` between
> sites, the functor `Sh(D) ⥤ Sh(C)`, `G ↦ (u^p G)^#`, is left adjoint to the pushforward
> `{}_s u = u.sheafPushforwardCocontinuous`.
>
> This is Stacks' chain of bijections: restriction along `u.op` is left adjoint to the
> right Kan extension `u.op.ran`, whose restriction to sheaves is
> `u.sheafPushforwardCocontinuous`, and sheafification is left adjoint to the inclusion of
> sheaves into presheaves.

```lean
noncomputable def sheafAdjunctionPullbackCocontinuous :
    u.sheafPullbackCocontinuous A J K ⊣ u.sheafPushforwardCocontinuous A J K
```

**`CategoryTheory.Functor.preservesFiniteColimits_sheafPullbackCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoverLifting.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L102). References: SGA 4 III (2.3), “clause 1”.

> **Stacks 00XL**, right exactness. `G ↦ (u^p G)^#` is a left adjoint, hence preserves
> all colimits; in particular it is right exact.

```lean
instance preservesFiniteColimits_sheafPullbackCocontinuous :
    PreservesFiniteColimits (u.sheafPullbackCocontinuous A J K)
```

**`CategoryTheory.Functor.preservesFiniteLimits_sheafPullbackCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoverLifting.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L112).

> **Stacks 00XL**, left exactness. `G ↦ (u^p G)^#` is the composite of three left exact
> functors: the inclusion `Sh(D) ⥤ PSh(D)` (which creates limits), restriction along `u.op`
> (limits of presheaves are computed pointwise), and sheafification, which is left exact by
> Stacks 00WJ — here the `HasSheafify J A` hypothesis, whose `isLeftExact` field is exactly
> that statement.

```lean
instance preservesFiniteLimits_sheafPullbackCocontinuous
    [HasFiniteLimits A] [HasSheafify J A] :
    PreservesFiniteLimits (u.sheafPullbackCocontinuous A J K)
```

**`CategoryTheory.Functor.morphismOfTopoi_of_isCocontinuous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSites/CocontinuousSmallModel.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSites/CocontinuousSmallModel.lean#L118). The attribute's comment: “the morphism of topoi of a cocontinuous functor, at the universe of a small model”.

> **Stacks 00XL at the universe of a small model.**  A functor between two sites essentially
> small at `u` which is both cocontinuous and continuous induces a morphism of topoi on sheaves of
> sets in `Type u`, in the same direction as the functor.
>
> Its direct image is the right Kan extension along `v.op`, and its inverse image is *restriction*
> along `v`, which Stacks 00XR (1) identifies with the sheafified pullback and which Stacks
> 00XR (3) shows to be left exact.

```lean
public noncomputable def morphismOfTopoi_of_isCocontinuous (v : C ⥤ D)
    (J : GrothendieckTopology C) (K : GrothendieckTopology D) [v.IsCocontinuous J K]
    [v.IsContinuous J K] :
    MorphismOfTopoi (Sheaf J (Type u)) (Sheaf K (Type u))
```

## Tag 00XM, a lemma

[Tag 00XM](https://stacks.math.columbia.edu/tag/00XM) in the Stacks Project.

**`sheafifyRestrictionIsoSheafifyRestrictionSheafify`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/CocontinuousTransfer.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/CocontinuousTransfer.lean#L66).

> **Stacks 00XM (canonical iso form).** In the situation of Stacks
> Lemma 00XL — i.e. assuming the 00XL transfer property `h00XL` — for
> any presheaf `G` on `D` we have a canonical isomorphism
> `(u^p G)^# ≅ (u^p G^#)^#` of sheaves on `(C, J)`, namely the
> sheafification of the whiskered unit `whiskerLeft u.op (toSheafify K G)`.

```lean
noncomputable def sheafifyRestrictionIsoSheafifyRestrictionSheafify
    {C : Type u₁} [Category.{v₁} C] {D : Type u₂} [Category.{v₂} D]
    (J : GrothendieckTopology C) (K : GrothendieckTopology D)
    (u : C ⥤ D)
    (A : Type u) [Category.{v} A]
    [HasWeakSheafify J A] [HasWeakSheafify K A]
    (h00XL : IsStacks00XLTransfer J K u A)
    (G : Dᵒᵖ ⥤ A) :
    (presheafToSheaf J A).obj (u.op ⋙ G) ≅
      (presheafToSheaf J A).obj
        (u.op ⋙ (sheafToPresheaf K A).obj ((presheafToSheaf K A).obj G))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.20, Tag 00XI](https://stacks.math.columbia.edu/tag/00XI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
