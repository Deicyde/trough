---
declaration: section
origin: cited
lean: Stacks.Injectives.eventuallyConst_subobject_of_monotone, Stacks.Injectives.eventuallyConst_subobject_of_antitone, Stacks.Injectives.mk_subobject_le_two_pow_mk_hom, Stacks.Injectives.cardinality_le_hom_of_strictMono_subobject, Stacks.Injectives.cardinality_le_hom_of_strictAnti_subobject, Stacks.Injectives.Size.size, Stacks.Injectives.Size.size_X₁_le_size_X₂, Stacks.Injectives.Size.size_X₃_le_size_X₂
statement: formalized
proof: formalized
---

# 19.11 Injectives in Grothendieck categories

Section 19.11 of the Stacks Project, [Tag 05AB](https://stacks.math.columbia.edu/tag/05AB). 7 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E8N, a lemma

[Tag 0E8N](https://stacks.math.columbia.edu/tag/0E8N) in the Stacks Project.

**`Stacks.Injectives.eventuallyConst_subobject_of_monotone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Size/EventuallyConstantChains.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Size/EventuallyConstantChains.lean#L79). The attribute's comment: “eventually constant”.

> **Stacks 0E8N.** An increasing well-ordered chain of subobjects is eventually constant if
> the cofinality of the index order exceeds the number of morphisms from a separator to the
> ambient object.

```lean
theorem eventuallyConst_subobject_of_monotone {U X : C} (hU : IsSeparator U)
    {α : Type w} [LinearOrder α] [WellFoundedLT α]
    (hcof : Cardinal.lift.{w} (Cardinal.mk (U ⟶ X)) <
      Cardinal.lift.{v} (Order.cof α)) (f : α → Subobject X) (hf : Monotone f) :
    atTop.EventuallyConst f
```

**`Stacks.Injectives.eventuallyConst_subobject_of_antitone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Size/EventuallyConstantChains.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Size/EventuallyConstantChains.lean#L96). The attribute's comment: “eventually constant”.

> **Stacks 0E8N.** A decreasing well-ordered chain of subobjects is eventually constant if
> the cofinality of the index order exceeds the number of morphisms from a separator to the
> ambient object.

```lean
theorem eventuallyConst_subobject_of_antitone {U X : C} (hU : IsSeparator U)
    {α : Type w} [LinearOrder α] [WellFoundedLT α]
    (hcof : Cardinal.lift.{w} (Cardinal.mk (U ⟶ X)) <
      Cardinal.lift.{v} (Order.cof α)) (f : α → Subobject X) (hf : Antitone f) :
    atTop.EventuallyConst f
```

**`Stacks.Injectives.mk_subobject_le_two_pow_mk_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Size/SubobjectCardinality.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Size/SubobjectCardinality.lean#L64). The attribute's comment: “subobject cardinality”.

> The collection of subobjects of an object has cardinality at most the cardinality of the
> power set of the morphisms to it from a separator.

```lean
theorem mk_subobject_le_two_pow_mk_hom {U X : C} (hU : IsSeparator U) :
    Cardinal.mk (Subobject X) ≤
      (2 : Cardinal.{max u v}) ^ Cardinal.lift.{u} (Cardinal.mk (U ⟶ X))
```

**`Stacks.Injectives.cardinality_le_hom_of_strictMono_subobject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Size/SubobjectCardinality.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Size/SubobjectCardinality.lean#L191). The attribute's comment: “chain bound”.

> A strictly increasing chain of subobjects has cardinality at most the cardinality of the
> set of morphisms from a separator to the ambient object.

```lean
theorem cardinality_le_hom_of_strictMono_subobject {U X : C} (hU : IsSeparator U)
    {ι : Type w} [LinearOrder ι] [WellFoundedLT ι]
    (f : ι → Subobject X) (hf : StrictMono f) :
    Cardinal.lift.{v} (Cardinal.mk ι) ≤ Cardinal.lift.{w} (Cardinal.mk (U ⟶ X))
```

**`Stacks.Injectives.cardinality_le_hom_of_strictAnti_subobject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Size/SubobjectCardinality.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Size/SubobjectCardinality.lean#L206). The attribute's comment: “chain bound”.

> A strictly decreasing chain of subobjects has cardinality at most the cardinality of the
> set of morphisms from a separator to the ambient object.

```lean
theorem cardinality_le_hom_of_strictAnti_subobject {U X : C} (hU : IsSeparator U)
    {ι : Type w} [LinearOrder ι] [WellFoundedLT ι]
    (f : ι → Subobject X) (hf : StrictAnti f) :
    Cardinal.lift.{v} (Cardinal.mk ι) ≤ Cardinal.lift.{w} (Cardinal.mk (U ⟶ X))
```

## Tag 079C, a definition

[Tag 079C](https://stacks.math.columbia.edu/tag/079C) in the Stacks Project.

**`Stacks.Injectives.Size.size`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Size/Defs.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Size/Defs.lean#L41).

> The *size* of an object `M` of an abelian category: the cardinality of the set of
> subobjects of `M`.

```lean
noncomputable def size {C : Type*} [Category C] [Abelian C] (M : C) : Cardinal
```

## Tag 079D, a lemma

[Tag 079D](https://stacks.math.columbia.edu/tag/079D) in the Stacks Project.

**`Stacks.Injectives.Size.size_X₁_le_size_X₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Size/Defs.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Size/Defs.lean#L48).

> For a short exact sequence `0 → M' → M → M'' → 0` in a Grothendieck abelian
> category, the size of `M'` is at most the size of `M`: there is an injection from the
> subobjects of `M'` into the subobjects of `M`, hence `|M'| ≤ |M|`.

```lean
theorem size_X₁_le_size_X₂ {C : Type*} [Category C] [Abelian C] [IsGrothendieckAbelian C]
    (S : ShortComplex C) (hS : S.ShortExact) :
    size S.X₁ ≤ size S.X₂
```

**`Stacks.Injectives.Size.size_X₃_le_size_X₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Size/Defs.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Size/Defs.lean#L86).

> For a short exact sequence `0 → M' → M → M'' → 0`, the size of `M''` is at most the
> size of `M`: there is an injection from the subobjects of `M''` into the subobjects of
> `M`, hence `|M''| ≤ |M|`.

```lean
theorem size_X₃_le_size_X₂ {C : Type*} [Category C] [Abelian C] [IsGrothendieckAbelian C]
    (S : ShortComplex C) (hS : S.ShortExact) :
    size S.X₃ ≤ size S.X₂
```

## Tag 079E, a lemma

[Tag 079E](https://stacks.math.columbia.edu/tag/079E) in the Stacks Project.

**`Stacks.Injectives.exists_epi_coproduct_of_subobject_cardinality_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Size/BoundedSizeObjects.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Size/BoundedSizeObjects.lean#L102). The attribute's comment: “part (1)”.

> If the cardinality of the set of subobjects of `M` is at most `κ`, then `M` is a
> quotient of a coproduct, indexed by a type of cardinality at most `κ`, of copies of the
> generator `U`.

```lean
theorem exists_epi_coproduct_of_subobject_cardinality_le (U M : C) (hU : IsSeparator U)
    (κ : Cardinal.{w})
    (hM : Cardinal.lift.{w} (Cardinal.mk (Subobject M)) ≤
      Cardinal.lift.{max u v} κ) :
    ∃ (ι : Type w), Cardinal.mk ι ≤ κ ∧
      ∃ (f : (∐ fun (_ : ι) => U) ⟶ M), Epi f
```

**`Stacks.Injectives.essentiallySmall_subobject_cardinality_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Size/BoundedSizeObjects.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Size/BoundedSizeObjects.lean#L113). The attribute's comment: “part (2)”.

> For every cardinal `κ`, the objects whose sets of subobjects have cardinality at most
> `κ` have only a set of isomorphism classes.

```lean
theorem essentiallySmall_subobject_cardinality_le (κ : Cardinal.{w}) :
    ObjectProperty.EssentiallySmall.{w}
      (fun M : C => Cardinal.lift.{w} (Cardinal.mk (Subobject M)) ≤
        Cardinal.lift.{max u v} κ)
```

## Tag 079F, a proposition

[Tag 079F](https://stacks.math.columbia.edu/tag/079F) in the Stacks Project.

**`Stacks.Injectives.isSmallWithRespectTo_monomorphisms_of_hasCardinalLT_subobject_cof`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Size/SmallWithRespectToInjections.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Size/SmallWithRespectToInjections.lean#L76).

> **Stacks 079F.** Let `A` be a Grothendieck abelian category, let `M` be an object of `A`
> and let `κ = |M|` be the cardinality of the set of subobjects of `M`. If `α` is an ordinal
> whose cofinality is bigger than `κ`, then `M` is `α`-small with respect to injections: for
> every system `(B_β)_{β ∈ α}` in `A` with monomorphic transition maps the canonical map
> `colim_β Hom(M, B_β) ⟶ Hom(M, colim_β B_β)` is bijective.

```lean
theorem isSmallWithRespectTo_monomorphisms_of_hasCardinalLT_subobject_cof
    {C : Type u} [Category.{v} C] [Abelian C] [IsGrothendieckAbelian.{w} C]
    (M : C) (α : Ordinal.{w}) (hM : HasCardinalLT (Subobject M) α.cof) :
    IsSmallWithRespectTo M (MorphismProperty.monomorphisms C) α
```

## Tag 079G, a lemma

[Tag 079G](https://stacks.math.columbia.edu/tag/079G) in the Stacks Project.

**`CategoryTheory.injective_iff_exists_extension_of_subobject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/DetectingMonomorphisms.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Injective/DetectingMonomorphisms.lean#L76).

> **Stacks Tag 079G.** An object `I` of a Grothendieck abelian category is injective if and
> only if, for every subobject `M` of a separator `G`, every morphism `M ⟶ I` extends along
> `M.arrow` to a morphism `G ⟶ I`.
>
> The forward implication is injectivity applied to the monomorphism `M.arrow`; the converse is
> the statement that the inclusions of the subobjects of a separator have the same right lifting
> property as all monomorphisms.

```lean
theorem injective_iff_exists_extension_of_subobject [Abelian C] [IsGrothendieckAbelian.{w} C]
    {G : C} (hG : IsSeparator G) (I : C) :
    Injective I ↔
      ∀ (M : Subobject G) (f : (M : C) ⟶ I), ∃ g : G ⟶ I, M.arrow ≫ g = f
```

**`CategoryTheory.exists_monomorphisms_injective_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/DetectingMonomorphisms.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Injective/DetectingMonomorphisms.lean#L98). The attribute's comment: “set-indexed form”.

> **Tag 079G in set-indexed form.** A Grothendieck abelian category has a set `T` and, for
> each `t : T`, a monomorphism `N t ⟶ N' t` such that an object `I` is injective precisely when
> every morphism `N t ⟶ I` extends to `N' t`.
>
> The family is the one of `injective_iff_exists_extension_of_subobject`: the inclusions of the
> subobjects of `CategoryTheory.separator C`, whose collection is `w`-small because a
> Grothendieck abelian category is well-powered. This is the shape in which Tags 0FSN and 0FSS
> consume Tag 079G.

```lean
theorem exists_monomorphisms_injective_iff (C : Type u) [Category.{v} C] [Abelian C]
    [IsGrothendieckAbelian.{w} C] :
    ∃ (T : Type w) (N N' : T → C) (i : ∀ t, N t ⟶ N' t),
      (∀ t, Mono (i t)) ∧
        ∀ I : C, Injective I ↔ ∀ (t : T) (f : N t ⟶ I), ∃ g : N' t ⟶ I, i t ≫ g = f
```

## Tag 079H, a theorem

[Tag 079H](https://stacks.math.columbia.edu/tag/079H) in the Stacks Project.

**`Stacks.Injectives.FunctorialEmbedding.hasFunctorialInjectiveEmbeddings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/GrothendieckFunctorial.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Injective/GrothendieckFunctorial.lean#L107). The attribute's comment: “functorial form; Mathlib's enoughInjectives has the non-functorial half”. References: SGA 4 V (0.1.1), “enough injectives”.

> **Stacks Project, Tag 079H.** A Grothendieck abelian category has functorial injective
> embeddings in the sense of [Stacks, Tag 0139].

```lean
theorem hasFunctorialInjectiveEmbeddings : HasFunctorialInjectiveEmbeddings C
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 19.11, Tag 05AB](https://stacks.math.columbia.edu/tag/05AB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
