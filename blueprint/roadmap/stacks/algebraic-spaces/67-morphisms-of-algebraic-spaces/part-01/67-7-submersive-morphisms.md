---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.presheaf_universallySubmersive_iff_universallySubmersive, AlgebraicGeometry.Space.IsSubmersive, AlgebraicGeometry.Space.UniversallySubmersive, AlgebraicGeometry.Space.universallySubmersive_pullback, AlgebraicGeometry.Space.IsSubmersive.comp, AlgebraicGeometry.Space.universallySubmersive_comp
statement: formalized
proof: formalized
---

# 67.7 Submersive morphisms

Section 67.7 of the Stacks Project, [Tag 0411](https://stacks.math.columbia.edu/tag/0411). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CFQ, a lemma

[Tag 0CFQ](https://stacks.math.columbia.edu/tag/0CFQ) in the Stacks Project.

**`AlgebraicGeometry.Space.presheaf_universallySubmersive_iff_universallySubmersive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean, line 1123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean#L1123).

> **Stacks 0CFQ.** A representable morphism `f : X ⟶ Y` of algebraic spaces over `S` is
> universally submersive in the sense of Stacks 03HA — each of its represented base changes is a
> universally submersive morphism of schemes — if and only if every base change of it by an
> algebraic space over `S` is submersive on points, which is universal submersiveness in the
> sense of Stacks 0412, part (2).
>
> The implication from left to right chooses a scheme atlas `a : U ⟶ Z` of the base `Z`: the
> chosen represented base change of `f` along `a ≫ g` is a quotient map of schemes, hence on
> points, and it factors through the base change along `g` by a continuous map, so
> `Topology.IsQuotientMap.of_comp` gives the conclusion.
>
> The converse must upgrade quotient-map-ness of the base changes available inside the size
> cutoff of the site to the unbounded `CategoryTheory.MorphismProperty.universally`. That is what
> the affine-space test `AlgebraicGeometry.Space.quotientMap_of_affineSpace_tests` is for: the
> base changes of a represented base change to the affine spaces over its target are inside the
> cutoff once the index type is small, by
> `AlgebraicGeometry.Space.quotientMap_of_small_baseChange`, and
> `AlgebraicGeometry.Space.quotientMap_affineSpace_map_of_small` removes the smallness
> restriction. No algebraicity hypothesis on `X` or `Y` is needed, only representability of
> `f`.

```lean
theorem presheaf_universallySubmersive_iff_universallySubmersive (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f) :
    (MorphismProperty.inverseImage
        ((topologically @Topology.IsQuotientMap : MorphismProperty Scheme.{u}).universally)
        (BigFppfOver.toScheme B S hS)).presheaf f ↔
      UniversallySubmersive B S hS f
```

## Tag 0412, a definition

[Tag 0412](https://stacks.math.columbia.edu/tag/0412) in the Stacks Project.

**`AlgebraicGeometry.Space.IsSubmersive`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean#L142). The attribute's comment: “part (1): submersive”. References: EGA IV (15.7.8), “more general”; SGA 1 IX (2.1), “submersive”.

> **Stacks 0412, part (1).** A morphism of algebraic spaces over `S` is *submersive* when the
> map it induces on points is a quotient map for the topology detected by scheme-valued points.
>
> This is unrelated to the notion of a submersion of differential manifolds.

```lean
abbrev IsSubmersive (f : F ⟶ G) : Prop
```

**`AlgebraicGeometry.Space.UniversallySubmersive`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean#L151). The attribute's comment: “part (2): universally submersive”. References: SGA 1 IX (2.1), “univ. submersive”.

> **Stacks 0412, part (2).** A morphism of algebraic spaces over `S` is *universally
> submersive* when its base change along every morphism to its target from an algebraic space
> over `S` is submersive.

```lean
abbrev UniversallySubmersive (f : F ⟶ G) : Prop
```

## Tag 0CFR, a lemma

[Tag 0CFR](https://stacks.math.columbia.edu/tag/0CFR) in the Stacks Project.

**`AlgebraicGeometry.Space.universallySubmersive_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean#L263).

> **Stacks 0CFR.** A base change of a universally submersive morphism of algebraic spaces
> over `S` is universally submersive.
>
> Nothing is needed beyond unwinding the definition: a base change of `Z ×_Y X ⟶ Z` along
> `k : W ⟶ Z` is a base change of `X ⟶ Y` along `k ≫ g`.

```lean
theorem universallySubmersive_pullback {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (_hX : IsAlgebraicSpace B S hS X) (_hY : IsAlgebraicSpace B S hS Y)
    (_hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Z ⟶ Y)
    (hf : UniversallySubmersive B S hS f) :
    UniversallySubmersive B S hS (pullback.fst g f)
```

## Tag 0CFS, a lemma

[Tag 0CFS](https://stacks.math.columbia.edu/tag/0CFS) in the Stacks Project.

**`AlgebraicGeometry.Space.IsSubmersive.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean#L250). The attribute's comment: “submersive”.

> **Stacks 0CFS, submersive morphisms.** A composition of submersive morphisms of algebraic
> spaces over `S` is submersive: the map on points of a composition is the composition of the
> maps on points.

```lean
theorem IsSubmersive.comp {f : F ⟶ G} {g : G ⟶ H} (hg : IsSubmersive B S hS g)
    (hf : IsSubmersive B S hS f) :
    IsSubmersive B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.universallySubmersive_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean#L277). The attribute's comment: “universally submersive”.

> **Stacks 0CFS, universally submersive morphisms.** A composition of universally submersive
> morphisms of algebraic spaces over `S` is universally submersive.
>
> The base change `W ×_Z X ⟶ W` of the composite along `k : W ⟶ Z` is identified by the pasting
> isomorphism `W ×_Z X ≅ (W ×_Z Y) ×_Y X` with the composition of a base change of `X ⟶ Y` and a
> base change of `Y ⟶ Z`.

```lean
theorem universallySubmersive_comp {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (_hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : UniversallySubmersive B S hS f) (hg : UniversallySubmersive B S hS g) :
    UniversallySubmersive B S hS (f ≫ g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.7, Tag 0411](https://stacks.math.columbia.edu/tag/0411)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
