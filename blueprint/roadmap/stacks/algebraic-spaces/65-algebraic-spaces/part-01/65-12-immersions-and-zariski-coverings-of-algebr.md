---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsOpenImmersion, AlgebraicGeometry.Space.IsOpenSubspace, AlgebraicGeometry.Space.IsClosedImmersion, AlgebraicGeometry.Space.IsClosedSubspace, AlgebraicGeometry.Space.IsImmersion, AlgebraicGeometry.Space.IsLocallyClosedSubspace, AlgebraicGeometry.Space.isOpenImmersion_comp, AlgebraicGeometry.Space.isClosedImmersion_comp
statement: formalized
proof: formalized
---

# 65.12 Immersions and Zariski coverings of algebraic spaces

Section 65.12 of the Stacks Project, [Tag 02YT](https://stacks.math.columbia.edu/tag/02YT). 6 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02YU, a definition

[Tag 02YU](https://stacks.math.columbia.edu/tag/02YU) in the Stacks Project.

**`AlgebraicGeometry.Space.IsOpenImmersion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L104). The attribute's comment: “part (1): open immersions”.

> **Stacks 02YU, part (1).** A morphism of algebraic spaces over `S` is an *open
> immersion* when it is representable and every represented base change of it is an open
> immersion of schemes.

```lean
abbrev IsOpenImmersion {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G) : Prop
```

**`AlgebraicGeometry.Space.IsOpenSubspace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L125). The attribute's comment: “part (2): open subspaces”.

> **Stacks 02YU, part (2).** A subfunctor of a presheaf on the big fppf site of `S` is
> an *open subspace* when it is an algebraic space over `S` and its inclusion is an open
> immersion.

```lean
abbrev IsOpenSubspace {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (G : Subfunctor F) : Prop
```

**`AlgebraicGeometry.Space.IsClosedImmersion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L132). The attribute's comment: “part (3): closed immersions”.

> **Stacks 02YU, part (3).** A morphism of algebraic spaces over `S` is a *closed
> immersion* when it is representable and every represented base change of it is a closed
> immersion of schemes.

```lean
abbrev IsClosedImmersion {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G) : Prop
```

**`AlgebraicGeometry.Space.IsClosedSubspace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L150). The attribute's comment: “part (4): closed subspaces”.

> **Stacks 02YU, part (4).** A subfunctor of a presheaf on the big fppf site of `S` is
> a *closed subspace* when it is an algebraic space over `S` and its inclusion is a closed
> immersion.

```lean
abbrev IsClosedSubspace {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (G : Subfunctor F) : Prop
```

**`AlgebraicGeometry.Space.IsImmersion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L157). The attribute's comment: “part (5): immersions”.

> **Stacks 02YU, part (5).** A morphism of algebraic spaces over `S` is an *immersion*
> when it is representable and every represented base change of it is an immersion of
> schemes.

```lean
abbrev IsImmersion {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G) : Prop
```

**`AlgebraicGeometry.Space.IsLocallyClosedSubspace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L175). The attribute's comment: “part (6): locally closed subspaces”.

> **Stacks 02YU, part (6).** A subfunctor of a presheaf on the big fppf site of `S` is
> a *locally closed subspace* when it is an algebraic space over `S` and its inclusion is
> an immersion.

```lean
abbrev IsLocallyClosedSubspace {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (G : Subfunctor F) : Prop
```

## Tag 02YV, a lemma

[Tag 02YV](https://stacks.math.columbia.edu/tag/02YV) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpenImmersion_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ImmersionBaseChange.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ImmersionBaseChange.lean#L167). The attribute's comment: “part (1): open immersions”. References: EGA I (4.2.5), “open immersions”.

> **Stacks 02YV**, part (1): a composite of open immersions of algebraic spaces over `S` is
> an open immersion.

```lean
theorem isOpenImmersion_comp {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : F ⟶ G) (g : G ⟶ H)
    (hf : IsOpenImmersion B S hS f) (hg : IsOpenImmersion B S hS g) :
    IsOpenImmersion B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.isClosedImmersion_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ImmersionBaseChange.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ImmersionBaseChange.lean#L178). The attribute's comment: “part (2): closed immersions”. References: EGA I (4.2.5), “closed immersions”; EGA I (4.1.6), “closed subprescheme”.

> **Stacks 02YV**, part (2): a composite of closed immersions of algebraic spaces over `S` is
> a closed immersion.

```lean
theorem isClosedImmersion_comp {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : F ⟶ G) (g : G ⟶ H)
    (hf : IsClosedImmersion B S hS f) (hg : IsClosedImmersion B S hS g) :
    IsClosedImmersion B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.isImmersion_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ImmersionBaseChange.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ImmersionBaseChange.lean#L187). The attribute's comment: “part (3): immersions”. References: EGA I (4.2.5), “immersions”; EGA I (4.1.6), “subprescheme case”.

> **Stacks 02YV**, part (3): a composite of immersions of algebraic spaces over `S` is an
> immersion.

```lean
theorem isImmersion_comp {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : F ⟶ G) (g : G ⟶ H)
    (hf : IsImmersion B S hS f) (hg : IsImmersion B S hS g) :
    IsImmersion B S hS (f ≫ g)
```

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.relative_isStableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.relative_isStableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Immersions.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Immersions.lean#L233) (StacksFrontier): “parts (1)-(3), in the generality of a relatively representable morphism property: the relative property of a property stable under composition is again stable under composition”.
- [`CategoryTheory.MorphismProperty.comp_mem`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.comp_mem#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Immersions.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Immersions.lean#L236) (StacksFrontier): “parts (1)-(3), the conclusion read off from that stability: a composite of two morphisms with a property stable under composition again has it”.

## Tag 02YW, a lemma

[Tag 02YW](https://stacks.math.columbia.edu/tag/02YW) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosedImmersion_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ImmersionBaseChange.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ImmersionBaseChange.lean#L113). The attribute's comment: “closed immersions”. References: EGA I (4.3.2), “closed immersion”.

> **Stacks 02YW** for closed immersions: a base change of a closed immersion of algebraic
> spaces over `S` is a closed immersion.

```lean
theorem isClosedImmersion_of_isPullback {F G H P : AlgebraicSpaces B S hS}
    {f : F ⟶ H} {g : G ⟶ H} {fst : P ⟶ F} {snd : P ⟶ G} (sq : IsPullback fst snd f g)
    (hf : IsClosedImmersion B S hS f.hom) :
    IsClosedImmersion B S hS snd.hom
```

**`AlgebraicGeometry.Space.isOpenImmersion_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ImmersionBaseChange.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ImmersionBaseChange.lean#L122). The attribute's comment: “open immersions”. References: EGA I (4.3.2), “open immersion”.

> **Stacks 02YW** for open immersions: a base change of an open immersion of algebraic
> spaces over `S` is an open immersion.

```lean
theorem isOpenImmersion_of_isPullback {F G H P : AlgebraicSpaces B S hS}
    {f : F ⟶ H} {g : G ⟶ H} {fst : P ⟶ F} {snd : P ⟶ G} (sq : IsPullback fst snd f g)
    (hf : IsOpenImmersion B S hS f.hom) :
    IsOpenImmersion B S hS snd.hom
```

**`AlgebraicGeometry.Space.isImmersion_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ImmersionBaseChange.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ImmersionBaseChange.lean#L131). The attribute's comment: “immersions”. References: EGA I (4.3.2), “immersion”.

> **Stacks 02YW** for immersions: a base change of an immersion of algebraic spaces over
> `S` is an immersion.

```lean
theorem isImmersion_of_isPullback {F G H P : AlgebraicSpaces B S hS}
    {f : F ⟶ H} {g : G ⟶ H} {fst : P ⟶ F} {snd : P ⟶ G} (sq : IsPullback fst snd f g)
    (hf : IsImmersion B S hS f.hom) :
    IsImmersion B S hS snd.hom
```

## Tag 02YX, a lemma

[Tag 02YX](https://stacks.math.columbia.edu/tag/02YX) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpenSubspace_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OpenImmersionCriteria.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/OpenImmersionCriteria.lean#L107). The attribute's comment: “open subspaces”.

> An open subspace of an algebraic space over `S` which
> is contained in a second subfunctor is an open subspace of that subfunctor.

```lean
theorem isOpenSubspace_of_le (F₁ F₂ : Subfunctor F) (hF₁ : IsOpenSubspace B S hS F₁)
    (h : F₁ ≤ F₂) :
    IsOpenSubspace B S hS (Subfunctor.range (Subfunctor.homOfLe h))
```

**`AlgebraicGeometry.Space.isClosedSubspace_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OpenImmersionCriteria.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/OpenImmersionCriteria.lean#L117). The attribute's comment: “closed subspaces”.

> A closed subspace of an algebraic space over `S` which is contained in a second subfunctor
> is a closed subspace of that subfunctor.

```lean
theorem isClosedSubspace_of_le (F₁ F₂ : Subfunctor F) (hF₁ : IsClosedSubspace B S hS F₁)
    (h : F₁ ≤ F₂) :
    IsClosedSubspace B S hS (Subfunctor.range (Subfunctor.homOfLe h))
```

**`AlgebraicGeometry.Space.isLocallyClosedSubspace_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OpenImmersionCriteria.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/OpenImmersionCriteria.lean#L127). The attribute's comment: “locally closed subspaces”.

> A locally closed subspace of an algebraic space over `S` which is contained in a second
> subfunctor is a locally closed subspace of that subfunctor.

```lean
theorem isLocallyClosedSubspace_of_le (F₁ F₂ : Subfunctor F)
    (hF₁ : IsLocallyClosedSubspace B S hS F₁) (h : F₁ ≤ F₂) :
    IsLocallyClosedSubspace B S hS (Subfunctor.range (Subfunctor.homOfLe h))
```

## Tag 02YY, a definition

[Tag 02YY](https://stacks.math.columbia.edu/tag/02YY) in the Stacks Project.

**`AlgebraicGeometry.Space.IsZariskiCover`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCover.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCover.lean#L35).

> A family `U` of subfunctors of a presheaf `F` on the big fppf site of `S` is a *Zariski
> covering* of `F` when every member is an open subspace and the map from the coproduct of the
> members to `F` is locally surjective for the fppf topology.

```lean
abbrev IsZariskiCover (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (I : Type u) (U : I → Subfunctor F) : Prop
```

## Tag 02YZ, a definition

[Tag 02YZ](https://stacks.math.columbia.edu/tag/02YZ) in the Stacks Project.

**`AlgebraicGeometry.Space.OpenSubspaces`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallZariskiSite.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallZariskiSite.lean#L223). The attribute's comment: “underlying category”.

> The category of open subspaces of an algebraic space, with inclusions as morphisms.

```lean
public abbrev OpenSubspaces
```

**`AlgebraicGeometry.Space.OpenSubspaces.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallZariskiSite.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallZariskiSite.lean#L231). The attribute's comment: “covering families”.

> A family of open subspaces covers an open subspace if it is a Zariski cover
> of that subspace in the sense of Stacks 02YY.

```lean
public abbrev IsCovering
    (E : Covering.{u + 1, u + 1, u} (OpenSubspaces B S hS F)) : Prop
```

**`AlgebraicGeometry.Space.OpenSubspaces.isSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallZariskiSite.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallZariskiSite.lean#L294). The attribute's comment: “site axioms”.

> Zariski covering families satisfy the axioms of a site.

```lean
public theorem isSite : IsSite (IsCovering B S hS F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 65.12, Tag 02YT](https://stacks.math.columbia.edu/tag/02YT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
