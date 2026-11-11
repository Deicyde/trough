---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.exists_smoothSurjectivePresentation_lift, AlgebraicGeometry.Stack.faithful_homFunctor_of_isRepresentableByAlgebraicSpaces, AlgebraicGeometry.Stack.AlgebraicStacks.faithful_homFunctor_of_isRepresentableByAlgebraicSpaces, AlgebraicGeometry.Stack.AlgebraicStacks.faithful_homFunctor_tfae, CategoryTheory.Functor.IsFiberedInGroupoids.faithful_iff_forall_fiber, AlgebraicGeometry.Stack.isAlgebraicStack_of_smoothPresentation, AlgebraicGeometry.Stack.isAlgebraicStack_source_of_isRepresentableByAlgebraicSpaces, AlgebraicGeometry.Stack.isStack_and_isAlgebraicStack_of_isRepresentableByAlgebraicSpaces
statement: formalized
proof: formalized
---

# 94.15 Algebraic stacks, overhauled

Section 94.15 of the Stacks Project, [Tag 04T0](https://stacks.math.columbia.edu/tag/04T0). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04T1, a lemma

[Tag 04T1](https://stacks.math.columbia.edu/tag/04T1) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_smoothSurjectivePresentation_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PresentationLift.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PresentationLift.lean#L190).

> **Stacks 04T1.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` and let
> `y : (Sch/V)_fppf ⟶ 𝒴` be surjective and smooth. Then there are a scheme `U` over `S`, a
> 1-morphism `x : (Sch/U)_fppf ⟶ 𝒳` which is surjective and smooth, and a 1-morphism
> `a : (Sch/U)_fppf ⟶ (Sch/V)_fppf` making the square `x ≫ f ≅ a ≫ y` 2-commute.
>
> Surjectivity and smoothness are the relative properties of Stacks 03YK for
> `AlgebraicGeometry.Space.surjectiveMorphismProperty` and
> `AlgebraicGeometry.Space.smoothMorphismProperty`.

```lean
theorem exists_smoothSurjectivePresentation_lift
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (_h𝒴 : IsAlgebraicStack.{u, w} B S hS 𝒴.val)
    (f : 𝒳 ⟶ 𝒴) (V : BigFppfOver B S hS) (y : schemeFibredCategory B S hS V ⟶ 𝒴)
    (hy : IsRepresentableByAlgebraicSpaces B S hS y.hom)
    (hysurj : HasRelativeProperty B S hS (Space.surjectiveMorphismProperty B S hS) y hy)
    (hysmooth : HasRelativeProperty B S hS (Space.smoothMorphismProperty B S hS) y hy) :
    ∃ (U : BigFppfOver B S hS) (x : schemeFibredCategory B S hS U ⟶ 𝒳)
      (a : schemeFibredCategory B S hS U ⟶ schemeFibredCategory B S hS V)
      (hx : IsRepresentableByAlgebraicSpaces B S hS x.hom),
      Nonempty (x ≫ f ≅ a ≫ y) ∧
        HasRelativeProperty B S hS (Space.surjectiveMorphismProperty B S hS) x hx ∧
          HasRelativeProperty B S hS (Space.smoothMorphismProperty B S hS) x hx
```

## Tag 04Y5, a lemma

[Tag 04Y5](https://stacks.math.columbia.edu/tag/04Y5) in the Stacks Project.

**`AlgebraicGeometry.Stack.faithful_homFunctor_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FaithfulRepresentable.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FaithfulRepresentable.lean#L63). The attribute's comment: “the implication (3) ⟹ (2)”.

> A 1-morphism of categories fibred in groupoids over the big fppf site of `S` which is
> representable by algebraic spaces has faithful underlying functor.

```lean
theorem faithful_homFunctor_of_isRepresentableByAlgebraicSpaces
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom) :
    (CatFiberedInGroupoids.homFunctor f).Faithful
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.faithful_homFunctor_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FaithfulRepresentable.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FaithfulRepresentable.lean#L79). The attribute's comment: “the implication (3) ⟹ (2) for algebraic stacks”.

> A 1-morphism of algebraic stacks over `S` which is representable by algebraic spaces has
> faithful underlying functor.

```lean
theorem faithful_homFunctor_of_isRepresentableByAlgebraicSpaces
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    (CatFiberedInGroupoids.homFunctor f.hom).Faithful
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.faithful_homFunctor_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FaithfulRepresentableUnconditional.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FaithfulRepresentableUnconditional.lean#L119).

> **Stacks 04Y5.** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` the following are
> equivalent:
>
> 1. for every object `U` of the big fppf site of `S` the functor `f_U : 𝒳_U ⥤ 𝒴_U` on fibres is
>    faithful;
> 2. the functor `f` is faithful;
> 3. `f` is representable by algebraic spaces.
>
> The equivalence (1) ⟺ (2) is Stacks 003Z (1),
> `CategoryTheory.Functor.IsFiberedInGroupoids.faithful_iff_forall_fiber`; the implication
> (3) ⟹ (2) is
> `AlgebraicGeometry.Stack.AlgebraicStacks.faithful_homFunctor_of_isRepresentableByAlgebraicSpaces`
> and the implication (2) ⟹ (3) is
> `AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_of_faithful`.

```lean
theorem faithful_homFunctor_tfae {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    List.TFAE
      [∀ U : BigFppfOver B S hS, (Functor.Fiber.mapOfComp 𝒳.val.val.p 𝒴.val.val.p
          (CatFiberedInGroupoids.homFunctor f.hom)
          (CatFiberedInGroupoids.homFunctor_comp_p f.hom) U).Faithful,
        (CatFiberedInGroupoids.homFunctor f.hom).Faithful,
        IsRepresentableByAlgebraicSpaces B S hS f.hom.hom]
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.IsFiberedInGroupoids.faithful_iff_forall_fiber`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Fibrewise.lean#L207), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/FaithfulRepresentable.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FaithfulRepresentable.lean#L55) (StacksFrontier): “the equivalence of parts (1) and (2)”.

## Tag 05UL, a lemma

[Tag 05UL](https://stacks.math.columbia.edu/tag/05UL) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_of_smoothPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationAlgebraicStack.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationAlgebraicStack.lean#L82).

> **Stacks 05UL.** A stack in groupoids over the big fppf site of `S` which receives a
> 1-morphism from a category representable by an algebraic space that is representable by
> algebraic spaces, surjective and smooth is an algebraic stack.

```lean
theorem isAlgebraicStack_of_smoothPresentation (v : 𝒰 ⟶ 𝒳)
    (h𝒳 : 𝒳.val.p.IsStack (BigFppfOver.topology B S hS))
    (h𝒰 : IsRepresentableByAlgebraicSpace B S hS 𝒰)
    (hv : IsRepresentableByAlgebraicSpaces B S hS v.hom)
    (hsurj : HasRelativeProperty.{u, u, u + 1, u + 1} B S hS
      (Space.surjectiveMorphismProperty B S hS) v hv)
    (hsmooth : HasRelativeProperty.{u, u, u + 1, u + 1} B S hS
      (Space.smoothMorphismProperty B S hS) v hv) :
    IsAlgebraicStack.{u, w} B S hS 𝒳.val
```

## Tag 05UM, a lemma

[Tag 05UM](https://stacks.math.columbia.edu/tag/05UM) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_source_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableMorphismAlgebraicStack.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableMorphismAlgebraicStack.lean#L145).

> **Stacks 05UM.** If a 1-morphism `j : 𝒳 ⟶ 𝒴` of categories fibred in groupoids over the big
> fppf site of `S` is representable by algebraic spaces and `𝒴` is an algebraic stack over `S`,
> then `𝒳` is an algebraic stack over `S`.
>
> The scheme atlas of `𝒴` base changes along `j` to a 1-morphism `W ⟶ 𝒳` which is again
> representable by algebraic spaces (Stacks 0302), surjective and smooth (Stacks 045C), with `W`
> representable by an algebraic space (Stacks 0300); the diagonal of `𝒳` is inherited from that of
> `𝒴`, so the form of Stacks 05UL that takes the diagonal as a hypothesis applies.
>
> The same statement is the algebraic-stack clause of **Stacks 05UN**, whose stack-in-groupoids
> clause is `AlgebraicGeometry.Stack.isStack_of_isRepresentableByAlgebraicSpaces`; the two
> clauses together are
> `AlgebraicGeometry.Stack.isStack_and_isAlgebraicStack_of_isRepresentableByAlgebraicSpaces`.

```lean
theorem isAlgebraicStack_source_of_isRepresentableByAlgebraicSpaces (j : 𝒳 ⟶ 𝒴)
    (hj : IsRepresentableByAlgebraicSpaces B S hS j.hom)
    (h𝒴 : IsAlgebraicStack.{u, w} B S hS 𝒴.val) :
    IsAlgebraicStack.{u, w} B S hS 𝒳.val
```

## Tag 05UN, a lemma

[Tag 05UN](https://stacks.math.columbia.edu/tag/05UN) in the Stacks Project.

**`AlgebraicGeometry.Stack.isStack_and_isAlgebraicStack_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableMorphismAlgebraicStack.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableMorphismAlgebraicStack.lean#L188).

> **Stacks 05UN.** Let `j : 𝒳 ⟶ 𝒴` be a 1-morphism of categories fibred in groupoids over the
> big fppf site of `S` which is representable by algebraic spaces. If `𝒴` is a stack in groupoids
> then so is `𝒳`, and if `𝒴` is an algebraic stack then so is `𝒳`.
>
> The first clause is `AlgebraicGeometry.Stack.isStack_of_isRepresentableByAlgebraicSpaces`, the
> second `AlgebraicGeometry.Stack.isAlgebraicStack_source_of_isRepresentableByAlgebraicSpaces`.

```lean
theorem isStack_and_isAlgebraicStack_of_isRepresentableByAlgebraicSpaces (j : 𝒳 ⟶ 𝒴)
    (hj : IsRepresentableByAlgebraicSpaces B S hS j.hom) :
    (𝒴.val.p.IsStack (BigFppfOver.topology B S hS) →
        𝒳.val.p.IsStack (BigFppfOver.topology B S hS)) ∧
      (IsAlgebraicStack.{u, w} B S hS 𝒴.val → IsAlgebraicStack.{u, w} B S hS 𝒳.val)
```

**`AlgebraicGeometry.Stack.isStack_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableMorphismStack.lean, line 808](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableMorphismStack.lean#L808). The attribute's comment: “the stack-in-groupoids clause”.

> **Stacks 05UN, the stack-in-groupoids clause.** A category fibred in groupoids over the big
> fppf site of `S` admitting a 1-morphism representable by algebraic spaces into a stack in
> groupoids is itself a stack in groupoids.
>
> This is the source's own proof of that clause: the criterion of Stacks 02ZY turns
> representability by algebraic spaces into the faithfulness and sheaf hypotheses of
> Stacks 0CKJ.

```lean
theorem isStack_of_isRepresentableByAlgebraicSpaces
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w}
      (AlgebraicGeometry.BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴)
    (hf : AlgebraicGeometry.Stack.IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (h𝒴 : 𝒴.val.p.IsStack (AlgebraicGeometry.BigFppfOver.topology B S hS)) :
    𝒳.val.p.IsStack (AlgebraicGeometry.BigFppfOver.topology B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 94.15, Tag 04T0](https://stacks.math.columbia.edu/tag/04T0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
