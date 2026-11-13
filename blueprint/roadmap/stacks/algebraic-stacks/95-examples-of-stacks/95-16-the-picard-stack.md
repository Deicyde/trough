---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.PicardObject, AlgebraicGeometry.Space.PicardHom, AlgebraicGeometry.Space.PicardHom.comp, AlgebraicGeometry.Space.picardStackCategory, AlgebraicGeometry.Space.picardStackBasedCategory, AlgebraicGeometry.Space.picardStackBasedCategory_fiber_isGroupoid, AlgebraicGeometry.Space.picardBasedCategory_isStackInGroupoids
statement: formalized
proof: formalized
---

# 95.16 The Picard stack

Section 95.16 of the Stacks Project, [Tag 0372](https://stacks.math.columbia.edu/tag/0372). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0372, the section

[Tag 0372](https://stacks.math.columbia.edu/tag/0372) in the Stacks Project.

**`AlgebraicGeometry.Space.PicardObject`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStack.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardStack.lean#L249). The attribute's comment: “the objects of the Picard stack”.

> **Section 0372, the objects of `Picardstack_{X/B}`.**  A triple `(U, b, L)`: a scheme `U` of
> the site with a morphism `b : U ⟶ B` to the base, and an invertible module `L` on the base
> change `X_U`.

```lean
structure PicardObject (s : PicardSituation B S hS)
```

**`AlgebraicGeometry.Space.PicardHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStack.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardStack.lean#L261). The attribute's comment: “the morphisms of the Picard stack”.

> **Section 0372, the morphisms of `Picardstack_{X/B}`.**  A pair `(f, g)`: a morphism
> `f : U ⟶ U'` of schemes over the base, and an isomorphism `g : f^*L' ⟶ L` of modules on
> `X_U`.

```lean
structure PicardHom {s : PicardSituation B S hS} (A C : PicardObject s)
```

**`AlgebraicGeometry.Space.PicardHom.comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStack.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardStack.lean#L298). The attribute's comment: “the composition”.

> **Section 0372, the composition `(f, g)` with `(f', g')` is `(f' ∘ f, g ∘ f^*(g'))`.**  The
> composite of the base maps, with the inverse image of the second comparison followed by the
> first, read through the comparison of Stacks 03LU for the composite.

```lean
def comp (m : PicardHom A C) (n : PicardHom C D) : PicardHom A D
```

**`AlgebraicGeometry.Space.picardStackCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategoryCanonical.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategoryCanonical.lean#L87). The attribute's comment: “the category Picardstack\_\{X/B}: objects (U, b, L), morphisms (f, g) with g : f^*L' ≅ L, composition (f' ∘ f, g ∘ f^*(g')), and its identities”.

> **Section 0372, the category `Picardstack_{X/B}`.**  The objects are the triples `(U, b, L)`
> of `AlgebraicGeometry.Space.PicardObject`, the morphisms `(U, b, L) ⟶ (U', b', L')` are the
> pairs `(f, g)` of `AlgebraicGeometry.Space.PicardHom` of a morphism of schemes `f : U ⟶ U'`
> over the base and an isomorphism `g : f^*L' ⟶ L`, the composite of `(f, g)` with `(f', g')` is
> `(f' ∘ f, g ∘ f^*(g'))` (`AlgebraicGeometry.Space.PicardHom.comp`), and the identity of
> `(U, b, L)` is the identity of `U` with the unit law `(𝟙)^*L ≅ L` of the inverse images of
> Stacks 03LU.
>
> The comparisons of inverse images are the ones of the pseudofunctoriality
> `AlgebraicGeometry.Space.modulePushforwardCoherence` of the direct images, which is constructed
> with no hypothesis, so the category takes no input beyond the morphism `π : X ⟶ B` of algebraic
> spaces of `s`.

```lean
def picardStackCategory : Category.{u + 1} (PicardObject s)
```

**`AlgebraicGeometry.Space.picardStackBasedCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategoryCanonical.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategoryCanonical.lean#L116). The attribute's comment: “the functor p : Picardstack\_\{X/B} ⟶ (Sch/S)\_fppf, (U, b, L) ↦ U”.

> **Section 0372, the functor `p : Picardstack_{X/B} ⟶ (Sch/S)_fppf`**, sending `(U, b, L)` to
> `U` and `(f, g)` to `f`, as a category over the big fppf site of `S`.

```lean
def picardStackBasedCategory : BasedCategory.{u + 1, u + 1} (BigFppfOver B S hS)
```

**`AlgebraicGeometry.Space.picardStackBasedCategory_fiber_isGroupoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategoryCanonical.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategoryCanonical.lean#L146). The attribute's comment: “the fibre categories of Picardstack\_\{X/B} over (Sch/S)\_fppf are groupoids”.

> **Section 0372, the fibre categories of `Picardstack_{X/B}` are groupoids.**  Every morphism
> of the fibre of `p : Picardstack_{X/B} ⟶ (Sch/S)_fppf` over a scheme `U` is an isomorphism.

```lean
theorem picardStackBasedCategory_fiber_isGroupoid (U : BigFppfOver B S hS) :
    IsGroupoid ((picardStackBasedCategory s).p.Fiber U)
```

## Tag 04WN, a lemma

[Tag 04WN](https://stacks.math.columbia.edu/tag/04WN) in the Stacks Project.

**`AlgebraicGeometry.Space.picardBasedCategory_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackIsStack.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardStackIsStack.lean#L82). The attribute's comment: “the functor Picardstack\_\{X/B} ⟶ (Sch/S)\_fppf of Section 0372, for the category built from the coherence data of 03LU, is a stack in groupoids: all three conditions of Stacks 02ZI, for p itself (stronger than the cutdown of 03ZZ, which follows)”.

> **Stacks 04WN.**  In Situation 0D25, the functor `p : Picardstack_{X/B} ⟶ (Sch/S)_fppf` of
> Section 0372, sending `(U, b, L)` to `U`, is a stack in groupoids over the big fppf site of `S`:
> it is fibred in groupoids, its `Isom` presheaves are sheaves, and every descent datum relative to
> an fppf covering is effective.
>
> The statement is made for `p` itself rather than for the cutdown of Stacks 03ZZ, the objects of
> `Picardstack_{X/B}` forming a type.
>
> This is the sole 04WN registration.  The former conditional sibling
> `AlgebraicGeometry.Space.picardProjection_isFiberedInGroupoids`, condition (1) only, is an
> unregistered step of this proof, entering through
> `AlgebraicGeometry.Space.picardBasedCategory_isFiberedInGroupoids`.

```lean
theorem picardBasedCategory_isStackInGroupoids (s : PicardSituation B S hS) :
    Functor.IsStackInGroupoids.{w} (picardBasedCategory (modulePushforwardCoherence B S hS) s).p
      (BigFppfOver.topology B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 95.16, Tag 0372](https://stacks.math.columbia.edu/tag/0372)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
