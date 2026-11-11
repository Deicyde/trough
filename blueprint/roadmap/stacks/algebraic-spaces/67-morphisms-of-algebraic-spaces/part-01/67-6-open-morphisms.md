---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.presheaf_universallyOpen_iff, AlgebraicGeometry.Space.IsOpenMorphism, AlgebraicGeometry.Space.UniversallyOpen, AlgebraicGeometry.Space.universallyOpen_pullback, AlgebraicGeometry.Space.IsOpenMorphism.comp, AlgebraicGeometry.Space.universallyOpen_comp, AlgebraicGeometry.Space.universallyOpen_tfae, AlgebraicGeometry.Space.universallyOpen_to_field
statement: formalized
proof: formalized
---

# 67.6 Open morphisms

Section 67.6 of the Stacks Project, [Tag 03Z0](https://stacks.math.columbia.edu/tag/03Z0). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03Z1, a lemma

[Tag 03Z1](https://stacks.math.columbia.edu/tag/03Z1) in the Stacks Project.

**`AlgebraicGeometry.Space.presheaf_universallyOpen_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean, line 669](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean#L669).

> A representable morphism of algebraic spaces over `S` is universally open, that is, every
> base change of it by an algebraic space over `S` is open on points, exactly when each of its
> represented base changes is a universally open morphism of schemes.

```lean
theorem presheaf_universallyOpen_iff {f : X ⟶ Y}
    (hf : yoneda.relativelyRepresentable f) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.UniversallyOpen.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f ↔ UniversallyOpen B S hS f
```

## Tag 03Z2, a definition

[Tag 03Z2](https://stacks.math.columbia.edu/tag/03Z2) in the Stacks Project.

**`AlgebraicGeometry.Space.IsOpenMorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean#L117). The attribute's comment: “part (1): open”.

> A morphism of algebraic spaces over `S` is *open* when the map it induces on points is an
> open map for the topology detected by scheme-valued points.

```lean
abbrev IsOpenMorphism (f : F ⟶ G) : Prop
```

**`AlgebraicGeometry.Space.UniversallyOpen`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean#L125). The attribute's comment: “part (2): universally open”.

> A morphism of algebraic spaces over `S` is *universally open* when its base change along
> every morphism to its target from an algebraic space over `S` is open.

```lean
abbrev UniversallyOpen (f : F ⟶ G) : Prop
```

## Tag 03Z3, a lemma

[Tag 03Z3](https://stacks.math.columbia.edu/tag/03Z3) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyOpen_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean#L211).

> A base change of a universally open morphism of algebraic spaces over `S` is universally
> open.

```lean
theorem universallyOpen_pullback {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (_hX : IsAlgebraicSpace B S hS X) (_hY : IsAlgebraicSpace B S hS Y)
    (_hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Z ⟶ Y)
    (hf : UniversallyOpen B S hS f) :
    UniversallyOpen B S hS (pullback.fst g f)
```

## Tag 03Z4, a lemma

[Tag 03Z4](https://stacks.math.columbia.edu/tag/03Z4) in the Stacks Project.

**`AlgebraicGeometry.Space.IsOpenMorphism.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean#L201). The attribute's comment: “open”.

> A composition of open morphisms of algebraic spaces over `S` is open.

```lean
theorem IsOpenMorphism.comp {f : F ⟶ G} {g : G ⟶ H} (hg : IsOpenMorphism B S hS g)
    (hf : IsOpenMorphism B S hS f) :
    IsOpenMorphism B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.universallyOpen_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean#L221). The attribute's comment: “universally open”.

> A composition of universally open morphisms of algebraic spaces over `S` is universally
> open.

```lean
theorem universallyOpen_comp {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (_hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : UniversallyOpen B S hS f) (hg : UniversallyOpen B S hS g) :
    UniversallyOpen B S hS (f ≫ g)
```

## Tag 03Z5, a lemma

[Tag 03Z5](https://stacks.math.columbia.edu/tag/03Z5) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyOpen_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean#L422).

> For a morphism `f : X ⟶ Y` of algebraic spaces over `S` the following are equivalent:
>
> 1. `f` is universally open;
> 2. for every scheme `Z` in the site and every `Z ⟶ Y` the projection `|Z ×_Y X| → |Z|` is
>    open;
> 3. the same for every affine scheme `Z` in the site;
> 4. there is a scheme `V` in the site and a surjective étale `V ⟶ Y` with `V ×_Y X ⟶ V`
>    universally open;
> 5. there is a Zariski covering of `Y` by open subspaces `Y_i` with each
>    `f⁻¹(Y_i) ⟶ Y_i` universally open.

```lean
theorem universallyOpen_tfae (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE
      [UniversallyOpen B S hS f,
        ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
          IsOpenMorphism B S hS (pullback.fst g f),
        ∀ (Z : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          ∀ g : yoneda.obj Z ⟶ Y, IsOpenMorphism B S hS (pullback.fst g f),
        ∃ (V : BigFppfOver B S hS) (v : yoneda.obj V ⟶ Y),
          IsSurjective B S hS v ∧ IsEtale B S hS v ∧
            UniversallyOpen B S hS (pullback.fst v f),
        ∃ (I : Type u) (U : I → Subfunctor Y), IsZariskiCover B S hS I U ∧
          ∀ i, UniversallyOpen B S hS (pullback.fst (U i).ι f)]
```

## Tag 06DN, a lemma

[Tag 06DN](https://stacks.math.columbia.edu/tag/06DN) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyOpen_to_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Open.lean#L523). References: EGA IV (2.4.10); EGA IV (2.4.9), “Y = Spec k”; SGA 4 VIII (9.4.4), “more general”.

> A morphism from an algebraic space over `S` to a representable presheaf whose representing
> scheme is the spectrum of a field is universally open.

```lean
theorem universallyOpen_to_field (hX : IsAlgebraicSpace B S hS X)
    {K : BigFppfOver B S hS} {k : Type u} [Field k]
    (e : (BigFppfOver.toScheme B S hS).obj K ≅ Spec (CommRingCat.of k))
    (p : X ⟶ yoneda.obj K) :
    UniversallyOpen B S hS p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.6, Tag 03Z0](https://stacks.math.columbia.edu/tag/03Z0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
