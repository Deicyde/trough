---
declaration: section
origin: cited
lean: Cat, CategoryStruct.id, id_of_comp_left_id, id_of_comp_right_id, IsIso, IsGroupoid, Groupoid, Grpd
statement: formalized
proof: formalized
---

# 4.2 Definitions

Section 4.2 of the Stacks Project, [Tag 0013](https://stacks.math.columbia.edu/tag/0013). 15 tags here are carried by 10 declarations of the repository (4 in StacksCore and 6 in StacksFrontier) and 22 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0014, a definition

[Tag 0014](https://stacks.math.columbia.edu/tag/0014) in the Stacks Project.

Declarations registered for the tag:

- [`Cat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Cat#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L17) (StacksCore): “the type / category of all categories”.

## Tag 0016, a remark

[Tag 0016](https://stacks.math.columbia.edu/tag/0016) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryStruct.id`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryStruct.id#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L19) (StacksCore): “the identity morphism on an object”.
- [`id_of_comp_left_id`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=id_of_comp_left_id#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L20) (StacksCore): “uniqueness of left identities”.
- [`id_of_comp_right_id`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=id_of_comp_right_id#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L21) (StacksCore): “uniqueness of right identities”.

## Tag 0017, a definition

[Tag 0017](https://stacks.math.columbia.edu/tag/0017) in the Stacks Project.

Declarations registered for the tag:

- [`IsIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsIso#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L23) (StacksCore): “Prop-valued typeclass stating that a morphism is an isomorphism”.

## Tag 0018, a definition

[Tag 0018](https://stacks.math.columbia.edu/tag/0018) in the Stacks Project.

Declarations registered for the tag:

- [`IsGroupoid`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsGroupoid#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L25) (StacksCore): “Prop-valued typeclass stating that a category is a groupoid”.
- [`Groupoid`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Groupoid#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L26) (StacksCore): “typeclass for groupoids, carrying an inverse to each morphism as data”.
- [`Grpd`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Grpd#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L27) (StacksCore): “the type / category of all groupoids”.

## Tag 0019, an example

[Tag 0019](https://stacks.math.columbia.edu/tag/0019) in the Stacks Project.

**`CategoryTheory.SingleObj.isEquivalence_functor`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Basic.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L31). The attribute's comment: “with `f` the identity it follows that every one-object category is equivalent to its endomorphism monoid, which for groupoids is a group by `CategoryTheory.End.group`”.

```lean
instance CategoryTheory.SingleObj.isEquivalence_functor {C : Type*} [Category* C]
    [Subsingleton C] {X : C} {M : Type*} [Monoid M] (f : M ≃* End X) :
    (functor f.toMonoidHom).IsEquivalence
```

## Tag 001A, an example

[Tag 001A](https://stacks.math.columbia.edu/tag/001A) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.instGroupoidDiscrete`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.instGroupoidDiscrete#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L38) (StacksCore).

## Tag 001C, a definition

[Tag 001C](https://stacks.math.columbia.edu/tag/001C) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.FullyFaithful`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.FullyFaithful#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L39) (StacksCore): “structure for fully faithful functors, carrying the preimage of each morphism as data”. References: EGA 0 (8.1.5); SGA 1 V (6.9).

## Tag 001D, a definition

[Tag 001D](https://stacks.math.columbia.edu/tag/001D) in the Stacks Project.

**`CategoryTheory.Subcategory`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Subcategory.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Subcategory.lean#L63). The attribute's comment: “(a) subcategory: subsets of the objects and of the arrows, arrows having source and target among the objects, containing the identities of its objects and closed under composition; its category structure is `CategoryTheory.Subcategory.category`”.

> A subcategory of a category `C`: a set `obj` of objects of `C` and a set `hom` of arrows of
> `C` such that the source and target of every arrow in `hom` lie in `obj`, the identity of every
> object in `obj` lies in `hom`, and `hom` is closed under composition.

```lean
structure Subcategory (C : Type u) [Category.{v} C]
```

**`CategoryTheory.Subcategory.IsFull`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Subcategory.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Subcategory.lean#L135). The attribute's comment: “(b) full subcategory: every arrow of the ambient category between two objects of the subcategory is in the subcategory”.

> A subcategory is full if it contains every arrow of the ambient category between two of its
> objects, so that its morphisms between two of its objects are all those of the ambient
> category.

```lean
def IsFull : Prop
```

**`CategoryTheory.Subcategory.IsStrictlyFull`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Subcategory.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Subcategory.lean#L142). The attribute's comment: “(c) strictly full subcategory: full, and every object of the ambient category isomorphic to an object of the subcategory is in the subcategory”.

> A subcategory is strictly full if it is full and every object of the ambient category
> isomorphic to an object of the subcategory is an object of the subcategory.

```lean
def IsStrictlyFull : Prop
```

Declarations registered for the tag:

- [`ObjectProperty.IsClosedUnderIsomorphisms`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ObjectProperty.IsClosedUnderIsomorphisms#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L41) (StacksCore): “predicate for strictly full subcategories”.

## Tag 001E, a remark

[Tag 001E](https://stacks.math.columbia.edu/tag/001E) in the Stacks Project.

**`CategoryTheory.Functor.toObjRange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Representable/SmallFullSubcategory.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Representable/SmallFullSubcategory.lean#L48).

> **Stacks 001E.** A functor `F : 𝒜 ⥤ Type v` factors through the full subcategory of `Type v`
> spanned by the values of `F` on objects; `toObjRange_comp_ι` says the factorization is on the
> nose.

```lean
def toObjRange : 𝒜 ⥤ (objRange F).FullSubcategory
```

**`CategoryTheory.Functor.small_objRange_fullSubcategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Representable/SmallFullSubcategory.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Representable/SmallFullSubcategory.lean#L67).

> **Stacks 001E.** The full subcategory of `Type v` spanned by the values of `F` on objects is
> small: its objects are indexed by `Ob 𝒜`. This is the formal counterpart of the source's
> observation that `F(Ob 𝒜)` is a set even though the category of sets is big.

```lean
instance small_objRange_fullSubcategory : Small.{u₁} (objRange F).FullSubcategory
```

## Tag 001F, an example

[Tag 001F](https://stacks.math.columbia.edu/tag/001F) in the Stacks Project.

**`CategoryTheory.SingleObj.faithful_mapHom_iff`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Basic.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L46).

```lean
lemma CategoryTheory.SingleObj.faithful_mapHom_iff {M N : Type*} [Monoid M] [Monoid N]
    {f : M →* N} : f.toFunctor.Faithful ↔ Function.Injective f
```

**`CategoryTheory.SingleObj.full_mapHom_iff`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Basic.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L52).

```lean
lemma CategoryTheory.SingleObj.full_mapHom_iff {M N : Type*} [Monoid M] [Monoid N]
    {f : M →* N} : f.toFunctor.Full ↔ Function.Surjective f
```

## Tag 001G, an example

[Tag 001G](https://stacks.math.columbia.edu/tag/001G) in the Stacks Project.

Declarations registered for the tag:

- [`Over.mapForget`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Over.mapForget#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L57) (StacksCore).

## Tag 001H, an example

[Tag 001H](https://stacks.math.columbia.edu/tag/001H) in the Stacks Project.

Declarations registered for the tag:

- [`Under`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Under#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L59) (StacksCore).
- [`Under.forget`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Under.forget#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L60) (StacksCore).
- [`Under.map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Under.map#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L61) (StacksCore).
- [`Under.mapForget`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Under.mapForget#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L62) (StacksCore).

## Tag 001I, a definition

[Tag 001I](https://stacks.math.columbia.edu/tag/001I) in the Stacks Project.

Declarations registered for the tag:

- [`NatTrans`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=NatTrans#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L64) (StacksCore).
- [`NatTrans.id`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=NatTrans.id#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L65) (StacksCore).
- [`NatTrans.vcomp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=NatTrans.vcomp#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L66) (StacksCore).
- [`Functor.category`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Functor.category#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L67) (StacksCore).

## Tag 001J, a definition

[Tag 001J](https://stacks.math.columbia.edu/tag/001J) in the Stacks Project.

Declarations registered for the tag:

- [`Functor.IsEquivalence`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Functor.IsEquivalence#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L69) (StacksCore): “Prop-valued typeclass stating that a functor is an equivalence”.
- [`CategoryTheory.Equivalence.mk`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Equivalence.mk#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L71) (StacksCore): “constructor upgrading an equivalence to a half-adjoint equivalence with the the same functors”.

## Tag 05SG, a lemma

[Tag 05SG](https://stacks.math.columbia.edu/tag/05SG) in the Stacks Project.

**`CategoryTheory.Equivalence.mkOfIsos`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Basic.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L79). References: EGA 0 (8.1.5), “equivalence C₁ ≃ F(C₁)”.

> Constructs an equivalence of categories from a fully faithful functor `F`, a family of objects
> `j : D → C` and a family of isomorphisms `i : ∀ X, X ≅ F.obj (j X)`. The constructed equivalence
> has an inverse that agrees with `j` on objects and a counit with components given by `i`.
> This is similar to `F.asEquivalence`, but gives more control over the resulting equivalence.

```lean
def CategoryTheory.Equivalence.mkOfIsos {C D : Type*} [Category* C] [Category* D] (F : C ⥤ D)
    (hF : F.FullyFaithful) (j : D → C) (i : ∀ X, X ≅ F.obj (j X)) : C ≌ D
```

**`CategoryTheory.Equivalence.existsUnique_functor_of_isos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Equivalence/MkOfIsos.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Equivalence/MkOfIsos.lean#L58). The attribute's comment: “existence and uniqueness of the functor `j` extending the rule on objects for which the `i_X` form an isomorphism `id ≅ F ∘ j`, and that `j` and `F` are quasi-inverse equivalences; the equivalence itself is `CategoryTheory.Equivalence.mkOfIsos`”.

> **Stacks 05SG.** Let `F : C ⥤ D` be fully faithful and, for every object `X` of `D`, let
> `j X` be an object of `C` and `i X : X ≅ F.obj (j X)` an isomorphism. Then there is a unique
> functor `G : D ⥤ C` such that `G` extends the rule `j` on objects (`h : ∀ X, G.obj X = j X`) and
> the isomorphisms `i X` define an isomorphism of functors `α : 𝟭 D ≅ G ⋙ F` (the component of `α`
> at `X` is `i X`, transported along `h X`). Moreover, any such `G` and `F` are quasi-inverse
> equivalences of categories: there is an equivalence `e : C ≌ D` with `e.functor = F` and
> `e.inverse = G`.

```lean
theorem existsUnique_functor_of_isos (F : C ⥤ D) (hF : F.FullyFaithful) (j : D → C)
    (i : ∀ X, X ≅ F.obj (j X)) :
    (∃! G : D ⥤ C, ∃ h : ∀ X, G.obj X = j X, ∃ α : 𝟭 D ≅ G ⋙ F,
        ∀ X, α.hom.app X = (i X).hom ≫ eqToHom (congrArg F.obj (h X).symm)) ∧
      ∀ G : D ⥤ C, (∃ h : ∀ X, G.obj X = j X, ∃ α : 𝟭 D ≅ G ⋙ F,
        ∀ X, α.hom.app X = (i X).hom ≫ eqToHom (congrArg F.obj (h X).symm)) →
        ∃ e : C ≌ D, e.functor = F ∧ e.inverse = G
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.2, Tag 0013](https://stacks.math.columbia.edu/tag/0013)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
