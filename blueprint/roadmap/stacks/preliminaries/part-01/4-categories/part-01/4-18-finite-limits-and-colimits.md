---
declaration: section
origin: cited
lean: CategoryTheory.exists_finCategory_functor_of_finitelyGeneratedShape, CategoryTheory.Limits.hasLimitsOfShape_isConnected_iff_hasEqualizers_and_hasPullbacks, nonempty_finite_limits_tfae, CategoryTheory.Limits.hasFiniteLimits_tfae, CategoryTheory.Limits.hasColimitsOfShape_isConnected_iff_hasCoequalizers_and_hasPushouts, CategoryTheory.Limits.HasNonemptyFiniteColimits, CategoryTheory.Limits.hasNonemptyFiniteColimits_tfae, CategoryTheory.Limits.hasFiniteColimits_tfae
statement: formalized
proof: formalized
---

# 4.18 Finite limits and colimits

Section 4.18 of the Stacks Project, [Tag 04AS](https://stacks.math.columbia.edu/tag/04AS). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05XU, a lemma

[Tag 05XU](https://stacks.math.columbia.edu/tag/05XU) in the Stacks Project.

**`CategoryTheory.exists_finCategory_functor_of_finitelyGeneratedShape`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Finite/FiniteIndexReduction.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Finite/FiniteIndexReduction.lean#L403).

> **Stacks Tag 05XU.**  Let `I` be a small category whose objects form a finite type
> and whose morphisms are generated, by composition, from a finite list of arrows.
> Then there exist a finite category `J` and a functor `F : J ⥤ I` such that:
>
> * (a) `J` is a finite category (witnessed by the `FinCategory J` instance);
> * (b) for every category `C` and every diagram `M : I ⥤ C`:
>     - `HasLimit M ↔ HasLimit (F ⋙ M)` and `HasColimit M ↔ HasColimit (F ⋙ M)`
>       (existence equivalences), and
>     - whenever both limits exist, the *canonical comparison morphism*
>       `limit.pre M F : limit M ⟶ limit (F ⋙ M)` is an isomorphism; dually, whenever
>       both colimits exist, `colimit.pre M F : colimit (F ⋙ M) ⟶ colimit M` is an
>       isomorphism.  Since these comparison morphisms are, by construction,
>       compatible with the projections / injections through `F`
>       (`limit.pre_π`, `colimit.ι_pre`), this is precisely the statement that `M` and
>       `F ⋙ M` have canonically isomorphic (co)limits via the comparison induced by
>       `F`;
> * (c) `J` is connected iff `I` is connected; and
> * (d) `J` is nonempty iff `I` is nonempty.

```lean
theorem exists_finCategory_functor_of_finitelyGeneratedShape {I : Type u} [SmallCategory I]
    (hI : FinitelyGeneratedShape I) :
    ∃ (J : Type u) (_ : SmallCategory J) (_ : FinCategory J) (F : J ⥤ I),
      -- (b) existence equivalences for limits and colimits, for every diagram
      (∀ {C : Type u'} [Category.{v'} C] (M : I ⥤ C),
        (HasLimit M ↔ HasLimit (F ⋙ M)) ∧
        (HasColimit M ↔ HasColimit (F ⋙ M))) ∧
      -- (b) the canonical comparison morphism on limits is an isomorphism
      (∀ {C : Type u'} [Category.{v'} C] (M : I ⥤ C) [HasLimit M] [HasLimit (F ⋙ M)],
        IsIso (limit.pre M F)) ∧
      -- (b) the canonical comparison morphism on colimits is an isomorphism
      (∀ {C : Type u'} [Category.{v'} C] (M : I ⥤ C) [HasColimit M] [HasColimit (F ⋙ M)],
        IsIso (colimit.pre M F)) ∧
      -- (c) connectedness is preserved
      (IsConnected J ↔ IsConnected I) ∧
      -- (d) nonemptiness is preserved
      (Nonempty J ↔ Nonempty I)
```

## Tag 04AT, a lemma

[Tag 04AT](https://stacks.math.columbia.edu/tag/04AT) in the Stacks Project.

**`CategoryTheory.Limits.hasLimitsOfShape_isConnected_iff_hasEqualizers_and_hasPullbacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Finite/Connected.lean, line 643](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Finite/Connected.lean#L643).

> **Stacks 04AT.** A category `C` admits limits over every finite connected shape
> if and only if it has equalizers and pullbacks.

```lean
theorem hasLimitsOfShape_isConnected_iff_hasEqualizers_and_hasPullbacks
    (C : Type u) [Category.{v} C] :
    (∀ (J : Type) [SmallCategory J] [FinCategory J] [IsConnected J], HasLimitsOfShape J C) ↔
      (HasEqualizers C ∧ HasPullbacks C)
```

## Tag 04AU, a lemma

[Tag 04AU](https://stacks.math.columbia.edu/tag/04AU) in the Stacks Project.

**`nonempty_finite_limits_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Finite/Nonempty.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Finite/Nonempty.lean#L242).

> **Stacks 04AU**. For a category `C`, having every limit indexed by a finite nonempty shape is
> equivalent to having binary products together with equalizers, and equivalent to having binary
> products together with pullbacks.

```lean
theorem nonempty_finite_limits_tfae :
    List.TFAE
      [ HasNonemptyFiniteLimits C,
        HasBinaryProducts C ∧ HasEqualizers C,
        HasBinaryProducts C ∧ HasPullbacks C ]
```

## Tag 002O, a lemma

[Tag 002O](https://stacks.math.columbia.edu/tag/002O) in the Stacks Project.

**`CategoryTheory.Limits.hasFiniteLimits_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Finite/Defs.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Finite/Defs.lean#L40). References: SGA 4 I (2.3.1).

> **Stacks 002O.** For a category `C` the following are equivalent:
> 1. finite limits exist in `C`;
> 2. finite products and equalizers exist in `C`;
> 3. a terminal object and fibre products exist in `C`.

```lean
theorem hasFiniteLimits_tfae (C : Type*) [Category C] :
    List.TFAE
      [HasFiniteLimits C,
       HasFiniteProducts C ∧ HasEqualizers C,
       HasTerminal C ∧ HasPullbacks C]
```

## Tag 04AV, a lemma

[Tag 04AV](https://stacks.math.columbia.edu/tag/04AV) in the Stacks Project.

**`CategoryTheory.Limits.hasColimitsOfShape_isConnected_iff_hasCoequalizers_and_hasPushouts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Finite/ConnectedColimits.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Finite/ConnectedColimits.lean#L51).

> **Stacks 04AV.** A category `C` admits colimits over every finite connected shape
> if and only if it has coequalizers and pushouts.

```lean
theorem hasColimitsOfShape_isConnected_iff_hasCoequalizers_and_hasPushouts
    (C : Type u) [Category.{v} C] :
    (∀ (J : Type) [SmallCategory J] [FinCategory J] [IsConnected J], HasColimitsOfShape J C) ↔
      (HasCoequalizers C ∧ HasPushouts C)
```

## Tag 04AW, a lemma

[Tag 04AW](https://stacks.math.columbia.edu/tag/04AW) in the Stacks Project.

**`CategoryTheory.Limits.HasNonemptyFiniteColimits`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Finite/NonemptyColimits.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Finite/NonemptyColimits.lean#L52).

> `HasNonemptyFiniteColimits C` says that `C` has all colimits of shape `J` for `J` a
> small, finite, *nonempty* category; equivalently, every nonempty finite diagram in `C`
> has a colimit. Unlike Mathlib's `HasFiniteColimits` this deliberately omits the empty
> shape, so it does not require an initial object.

```lean
class HasNonemptyFiniteColimits : Prop
```

**`CategoryTheory.Limits.hasNonemptyFiniteColimits_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Finite/NonemptyColimits.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Finite/NonemptyColimits.lean#L134).

> **Stacks 04AW.** For a category `C` the following are equivalent:
> 1. nonempty finite colimits exist in `C`;
> 2. coproducts of pairs and coequalizers exist in `C`;
> 3. coproducts of pairs and pushouts exist in `C`.

```lean
theorem hasNonemptyFiniteColimits_tfae :
    List.TFAE
      [ HasNonemptyFiniteColimits C
      , HasBinaryCoproducts C ∧ HasCoequalizers C
      , HasBinaryCoproducts C ∧ HasPushouts C ]
```

## Tag 002Q, a lemma

[Tag 002Q](https://stacks.math.columbia.edu/tag/002Q) in the Stacks Project.

**`CategoryTheory.Limits.hasFiniteColimits_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Finite/Colimits.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Finite/Colimits.lean#L41). References: SGA 4 I (2.3.1).

> **Stacks 002Q.** For a category `C` the following are equivalent:
> 1. finite colimits exist in `C`;
> 2. finite coproducts and coequalizers exist in `C`;
> 3. an initial object and pushouts exist in `C`.

```lean
theorem hasFiniteColimits_tfae (C : Type*) [Category C] :
    List.TFAE
      [HasFiniteColimits C,
       HasFiniteCoproducts C ∧ HasCoequalizers C,
       HasInitial C ∧ HasPushouts C]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.18, Tag 04AS](https://stacks.math.columbia.edu/tag/04AS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
