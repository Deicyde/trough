---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.PicardObject, AlgebraicGeometry.Space.PicardHom, AlgebraicGeometry.Space.PicardHom.id, AlgebraicGeometry.Space.PicardHom.comp, AlgebraicGeometry.Space.PicardHom.id_comp, AlgebraicGeometry.Space.PicardHom.comp_id, AlgebraicGeometry.Space.PicardHom.comp_assoc, AlgebraicGeometry.Space.picardCategory
statement: formalized
proof: formalized
---

# 95.16 The Picard stack

Section 95.16 of the Stacks Project, [Tag 0372](https://stacks.math.columbia.edu/tag/0372). 2 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0372, the section

[Tag 0372](https://stacks.math.columbia.edu/tag/0372) in the Stacks Project.

**`AlgebraicGeometry.Space.PicardObject`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStack.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStack.lean#L252). The attribute's comment: “the objects of the Picard stack”.

> **Section 0372, the objects of `Picardstack_{X/B}`.**  A triple `(U, b, L)`: a scheme `U` of
> the site with a morphism `b : U ⟶ B` to the base, and an invertible module `L` on the base
> change `X_U`.

```lean
structure PicardObject (s : PicardSituation B S hS)
```

**`AlgebraicGeometry.Space.PicardHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStack.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStack.lean#L264). The attribute's comment: “the morphisms of the Picard stack”.

> **Section 0372, the morphisms of `Picardstack_{X/B}`.**  A pair `(f, g)`: a morphism
> `f : U ⟶ U'` of schemes over the base, and an isomorphism `g : f^*L' ⟶ L` of modules on
> `X_U`.

```lean
structure PicardHom {s : PicardSituation B S hS} (A C : PicardObject s)
```

**`AlgebraicGeometry.Space.PicardHom.id`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStack.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStack.lean#L294). The attribute's comment: “the identity, conditional on the pseudofunctoriality of the direct images of Stacks 03LU”.

> **Section 0372, the identity of an object.**  The identity of its pair `(U, b)`, with the
> unit law `(X_{𝟙 U})^* ≅ 𝟭` of Stacks 03LU as its comparison of modules.

```lean
def id (hc : ModulePushforwardCoherence B S hS) (A : PicardObject s) : PicardHom A A
```

**`AlgebraicGeometry.Space.PicardHom.comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStack.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStack.lean#L303). The attribute's comment: “the composition”.

> **Section 0372, the composition `(f, g)` with `(f', g')` is `(f' ∘ f, g ∘ f^*(g'))`.**  The
> composite of the base maps, with the inverse image of the second comparison followed by the
> first, read through the comparison of Stacks 03LU for the composite.

```lean
def comp (m : PicardHom A C) (n : PicardHom C D) : PicardHom A D
```

**`AlgebraicGeometry.Space.PicardHom.id_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean#L243). The attribute's comment: “the identity law at the source for the composition of the Picard stack”.

> **Section 0372, the identity law at the source.**  Composing a morphism of
> `Picardstack_{X/B}` with the identity of its source returns it.

```lean
theorem id_comp (hc : ModulePushforwardCoherence B S hS) {A C : PicardObject s}
    (m : PicardHom A C) : PicardHom.comp (PicardHom.id hc A) m = m
```

**`AlgebraicGeometry.Space.PicardHom.comp_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean#L253). The attribute's comment: “the identity law at the target for the composition of the Picard stack”.

> **Section 0372, the identity law at the target.**  Composing a morphism of
> `Picardstack_{X/B}` with the identity of its target returns it.

```lean
theorem comp_id (hc : ModulePushforwardCoherence B S hS) {A C : PicardObject s}
    (m : PicardHom A C) : PicardHom.comp m (PicardHom.id hc C) = m
```

**`AlgebraicGeometry.Space.PicardHom.comp_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean#L262). The attribute's comment: “associativity of the composition of the Picard stack”.

> **Section 0372, associativity.**  The composition of `Picardstack_{X/B}` is associative.

```lean
theorem comp_assoc (hc : ModulePushforwardCoherence B S hS) {A C D E : PicardObject s}
    (m : PicardHom A C) (n : PicardHom C D) (p : PicardHom D E) :
    PicardHom.comp (PicardHom.comp m n) p = PicardHom.comp m (PicardHom.comp n p)
```

**`AlgebraicGeometry.Space.picardCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean#L286). The attribute's comment: “the category Picardstack_{X/B}, conditional on the pseudofunctoriality of the direct images of Stacks 03LU that its identity already needs”.

> **Section 0372, the category `Picardstack_{X/B}`.**  The objects are the triples `(U, b, L)`,
> the morphisms are the pairs `(f, g)` of a morphism of test schemes over the base and an
> isomorphism `f^*L' ≅ L`, and the identities and the composition are the ones of Section 0372.

```lean
def picardCategory (hc : ModulePushforwardCoherence B S hS) (s : PicardSituation B S hS) :
    Category.{u + 1} (PicardObject s)
```

**`AlgebraicGeometry.Space.picardProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean#L298). The attribute's comment: “the projection of the Picard stack to the test schemes over the base”.

> **Section 0372, the functor `p`.**  The projection of `Picardstack_{X/B}` to the test schemes
> over the base, forgetting the invertible module.

```lean
def picardProjection (hc : ModulePushforwardCoherence B S hS) (s : PicardSituation B S hS) :
    letI : Category.{u + 1} (PicardObject s) := picardCategory hc s
    PicardObject s ⥤ s.SchemesOver
```

**`AlgebraicGeometry.Space.picardCategoryData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean#L312). The attribute's comment: “a value of the specification of the category Picardstack_{X/B} with its projection, conditional on the pseudofunctoriality of the direct images of Stacks 03LU”.

> **Section 0372.**  The category `Picardstack_{X/B}` together with its projection satisfies
> the specification `AlgebraicGeometry.Space.PicardCategoryData`: its hom-sets, identities,
> composition and projection are the ones of Section 0372.

```lean
def picardCategoryData (hc : ModulePushforwardCoherence B S hS)
    (s : PicardSituation B S hS) : PicardCategoryData hc s
```

## Tag 04WN, a lemma

[Tag 04WN](https://stacks.math.columbia.edu/tag/04WN) in the Stacks Project.

**`AlgebraicGeometry.Space.picardProjection_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackFibered.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackFibered.lean#L385). The attribute's comment: “condition (1) of Stacks 02ZI only — the functor Picardstack_{X/B} ⟶ (Sch/S)_fppf is fibred in groupoids — and conditional on the category of Section 0372; conditions (2) and (3) need Stacks 04W8, which this development does not carry”.

> **Condition (1) of Stacks 02ZI for the functor of Stacks 04WN.**  In Situation 0D25 the
> projection `p : Picardstack_{X/B} ⟶ (Sch/S)_fppf` of Section 0372, which sends an object
> `(U, b, L)` to its test scheme `U`, is fibred in groupoids.
>
> The projection of `Picardstack_{X/B}` to the test schemes over the base is fibred in groupoids
> by `AlgebraicGeometry.Space.picardProjection_isFiberedInGroupoids_schemesOver`, the projection
> of the test schemes over the base to the schemes of the site is fibred in groupoids by
> `CategoryTheory.Functor.IsFiberedInGroupoids.costructuredArrow_proj`, and Stacks 09WW composes
> the two.
>
> **This carrier asserts the first of the three conditions of Stacks 02ZI, and asserts it
> conditionally.**  Stacks 04WN is the conjunction of all three for this functor, and conditions
> (2) and (3) — the `Isom` presheaves being sheaves, and effectivity of descent data — are not
> proved here: the source proves them by citing Descent on Spaces, Proposition 74.4.1
> (Stacks 04W8), fpqc descent of quasi-coherent modules on algebraic spaces, which this
> development does not carry.  Of the hypotheses, `cd` is the category of Section 0372, which the
> source introduces by designation, and `hc` is the pseudofunctoriality of Stacks 03LU that its
> identities and composition already need.
> The attribute is qualified accordingly, and no unqualified 04WN claim is made here.  The
> source's "up to a replacement as in Remark 03ZZ" clause needs nothing: see the implementation
> notes of the file.

```lean
theorem picardProjection_isFiberedInGroupoids (hc : ModulePushforwardCoherence B S hS)
    {s : PicardSituation B S hS} (cd : PicardCategoryData hc s) :
    letI : Category.{u + 1} (PicardObject s) := cd.category
    Functor.IsFiberedInGroupoids
      (cd.projection ⋙ CostructuredArrow.proj (schemeSpaceFunctor B S hS) s.base)
```

**`AlgebraicGeometry.Space.picardBasedCategory_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackIsStack.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackIsStack.lean#L71). The attribute's comment: “the functor Picardstack_{X/B} ⟶ (Sch/S)_fppf is a stack in groupoids: all three conditions of Stacks 02ZI”.

> **Stacks 04WN.**  In Situation 0D25, the functor `p : Picardstack_{X/B} ⟶ (Sch/S)_fppf` of
> Section 0372, sending `(U, b, L)` to `U`, is a stack in groupoids over the big fppf site of `S`:
> it is fibred in groupoids, its `Isom` presheaves are sheaves, and every descent datum relative to
> an fppf covering is effective.
>
> The statement is made for `p` itself rather than for the cutdown of Stacks 03ZZ, the objects of
> `Picardstack_{X/B}` forming a type.

```lean
theorem picardBasedCategory_isStackInGroupoids (s : PicardSituation B S hS) :
    Functor.IsStackInGroupoids.{w} (picardBasedCategory (modulePushforwardCoherence B S hS) s).p
      (BigFppfOver.topology B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 95.16, Tag 0372](https://stacks.math.columbia.edu/tag/0372)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
