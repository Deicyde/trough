---
declaration: section
origin: cited
lean: AlgebraicGeometry.nodalCurvesOpenSubstack, AlgebraicGeometry.classifying_factors_nodalCurvesOpenSubstack_iff, AlgebraicGeometry.lifts_nodalCurves_curveFamilyOfProperOverField_iff, AlgebraicGeometry.lifts_nodalCurvesInclusion_curveFamilyOfProperOverField_iff, AlgebraicGeometry.isNodalCurveFamily_of_hom, AlgebraicGeometry.isClosedUnderIsomorphisms_isNodalCurveFamily, AlgebraicGeometry.nodalCurvesOpenSubstackUnconditional, AlgebraicGeometry.classifying_factors_nodalCurvesOpenSubstack_iff_unconditional
statement: formalized
proof: formalized
---

# 109.18 Nodal curves

Section 109.18 of the Stacks Project, [Tag 0DSX](https://stacks.math.columbia.edu/tag/0DSX). 2 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DSY, a lemma

[Tag 0DSY](https://stacks.math.columbia.edu/tag/0DSY) in the Stacks Project.

**`AlgebraicGeometry.nodalCurvesOpenSubstack`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodal.lean, line 1133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodal.lean#L1133). The attribute's comment: “the open substack and part (1): the characterisation on every family of curves, given a presentation of the algebraic stack of curves. Part (2), the characterisation for a proper scheme over a field, is NOT asserted here”.

> **Stacks 0DSY, part (1).** The open substack `Curves^{nodal}` of families of curves which are
> at-worst-nodal of relative dimension one, together with the characterisation of its objects: an
> object of the stack belongs to it exactly when the family of curves it classifies is
> at-worst-nodal of relative dimension one.
>
> The algebraic stack of curves is a hypothesis: `𝒳` is any algebraic stack over the big fppf site
> of the integers whose objects are identified with families of curves by an equivalence `E` over
> that site.
>
> Part (2) of the source, the characterisation for a proper scheme over a field, is not asserted
> here.
>
> The definition carries `@[no_expose]`: its body names the private helpers that build the
> substack, so it may not be exposed. Nothing downstream needs to unfold it — the
> characterisation of its objects is the second component of the subtype.

```lean
def nodalCurvesOpenSubstack
    (𝒳 : Stack.AlgebraicStacks.{u, w} B integerBase hZ)
    (E : CurveFamily B hZ ≌ 𝒳.val.val.obj)
    (hE : E.functor ⋙ 𝒳.val.val.p = curvesProjectionOver B hZ) :
    {U : Stack.OpenSubstack 𝒳 //
      ∀ F : CurveFamily B hZ,
        U.property (E.functor.obj F) ↔
          Space.IsAtWorstNodalOfRelativeDimensionOne B integerBase hZ F.toBase.hom}
```

**`AlgebraicGeometry.classifying_factors_nodalCurvesOpenSubstack_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodal.lean, line 1202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodal.lean#L1202). The attribute's comment: “part (1): the classifying morphism of a family factors through the nodal open substack iff the family is at-worst-nodal of relative dimension one, given a presentation of the algebraic stack of curves. Part (2), the characterisation for a proper scheme over a field, is NOT asserted here”.

> **Stacks 0DSY, part (1).** The classifying object of a family of curves lifts through the
> inclusion of the nodal open substack exactly when the family is at-worst-nodal of relative
> dimension one.
>
> As for `AlgebraicGeometry.nodalCurvesOpenSubstack`, the algebraic stack of curves and its
> identification with families of curves are hypotheses.

```lean
theorem classifying_factors_nodalCurvesOpenSubstack_iff
    (𝒳 : Stack.AlgebraicStacks.{u, w} B integerBase hZ)
    (E : CurveFamily B hZ ≌ 𝒳.val.val.obj)
    (hE : E.functor ⋙ 𝒳.val.val.p = curvesProjectionOver B hZ)
    (F : CurveFamily B hZ) :
    (∃ Y : (nodalCurvesOpenSubstack B hZ 𝒳 E hE).1.property.FullSubcategory,
      Y.obj = E.functor.obj F) ↔
      Space.IsAtWorstNodalOfRelativeDimensionOne B integerBase hZ F.toBase.hom
```

**`AlgebraicGeometry.lifts_nodalCurves_curveFamilyOfProperOverField_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalOverField.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalOverField.lean#L190). The attribute's comment: “part (2): for a scheme X proper over a field k with dim(X) ≤ 1, the classifying morphism Spec(k) → Curves factors through Curves^{nodal} if and only if the singularities of X are at-worst-nodal and X is equidimensional of dimension 1. Factoring through the substack is lifting the classifying object through the inclusion of the strictly full subcategory of at-worst-nodal families, as in AlgebraicGeometry.lifts_nodalCurves_iff; no part of Tag 04S6 is assumed, and this declaration carries no hypothesis beyond the source's”.

> **Stacks 0DSY, part (2).** Let `k` be a field and let `X ⟶ Spec(k)` be a morphism of the big
> fppf site of the integers which is proper and whose source has dimension at most one. The
> classifying morphism `Spec(k) → Curves` of the attached family of curves factors through
> `Curves^{nodal}` — that is, that family lifts through the inclusion of the strictly full
> subcategory of families which are at-worst-nodal of relative dimension one — if and only if the
> singularities of `X` are at worst nodal and `X` is equidimensional of dimension one.
>
> The hypotheses are those of the source: `X` is proper over the field and of dimension at most
> one. Nothing else is assumed; in particular this does not use the hypothesis
> `AlgebraicGeometry.Stack.Bootstrap04S6Spaces` on which
> `AlgebraicGeometry.nodalCurvesOpenSubstackUnconditional` — the open substack itself, part of the
> same tag — is conditional, because factoring through the substack is tested by lifting the
> classifying object through the inclusion, and that inclusion is constructed unconditionally.
>
> "Equidimensional of dimension one" is read as the source's definition reads it: `X` is
> equidimensional and every irreducible component of `X` has dimension one.

```lean
theorem lifts_nodalCurves_curveFamilyOfProperOverField_iff
    {T W : BigFppfOver B integerBase hZ} (g : T ⟶ W) (k : Type u) [Field k]
    (hW : (BigFppfOver.toScheme B integerBase hZ).obj W = Spec (.of k))
    (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1) :
    letI : ((BigFppfOver.toScheme B integerBase hZ).obj T).Over (Spec (.of k)) :=
      ⟨(BigFppfOver.toScheme B integerBase hZ).map g ≫ eqToHom hW⟩
    ((∃ Y : (isNodalCurveFamily B hZ).FullSubcategory,
        Y.obj = curveFamilyOfProperOverFieldEqSpec B hZ g k hW hproper hdim) ↔
      (Stacks.Curves.HasAtWorstNodalSingularities k
          ((BigFppfOver.toScheme B integerBase hZ).obj T) ∧
        Equidimensional ((BigFppfOver.toScheme B integerBase hZ).obj T) ∧
        ∀ Z ∈ irreducibleComponents ((BigFppfOver.toScheme B integerBase hZ).obj T),
          topologicalKrullDim Z = (1 : WithBot ℕ∞)))
```

**`AlgebraicGeometry.lifts_nodalCurvesInclusion_curveFamilyOfProperOverField_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalOverField.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalOverField.lean#L236). The attribute's comment: “part (2), stated through the inclusion 1-morphism AlgebraicGeometry.nodalCurvesInclusion of the open substack: for a scheme X proper over a field k with dim(X) ≤ 1, the classifying morphism Spec(k) → Curves factors through Curves^nodal if and only if the singularities of X are at-worst-nodal and X is equidimensional of dimension 1. Unconditional: no presentation of Curves as an algebraic stack (Tag 0D5A) and no part of Tag 04S6 is assumed, and this declaration carries no hypothesis beyond the source's”.

> **Stacks 0DSY, part (2).** Let `k` be a field and let `X ⟶ Spec(k)` be a morphism of the big
> fppf site of the integers which is proper and whose source has dimension at most one. The
> classifying morphism `Spec(k) → Curves` of the attached family of curves factors through the
> open substack `Curves^{nodal}` if and only if the singularities of `X` are at worst nodal and
> `X` is equidimensional of dimension one.
>
> This is `AlgebraicGeometry.lifts_nodalCurves_curveFamilyOfProperOverField_iff` with factoring
> through `Curves^{nodal}` read as being in the image on objects of the 1-morphism
> `AlgebraicGeometry.nodalCurvesInclusion`, so that the statement is about the same object as the
> other registrations of the tag: the strictly full subcategory
> `AlgebraicGeometry.nodalCurvesFiberedCategory` of the fibred category of families of curves,
> whose inclusion is proved representable by algebraic spaces and an open immersion in
> `AlgebraicGeometry.isRepresentableByAlgebraicSpaces_nodalCurvesInclusion` and
> `AlgebraicGeometry.isOpenImmersion_nodalCurvesInclusion`.
>
> The hypotheses are those of the source: `X` is proper over the field and of dimension at most
> one. Nothing else is assumed; in particular there is no algebraic stack `𝒳`, no equivalence
> identifying it with the category of families of curves, and no part of Stacks 04S6.
>
> "Equidimensional of dimension one" is read as the source's definition reads it: `X` is
> equidimensional and every irreducible component of `X` has dimension one.

```lean
theorem lifts_nodalCurvesInclusion_curveFamilyOfProperOverField_iff
    {T W : BigFppfOver B integerBase hZ} (g : T ⟶ W) (k : Type u) [Field k]
    (hW : (BigFppfOver.toScheme B integerBase hZ).obj W = Spec (.of k))
    (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1) :
    letI : ((BigFppfOver.toScheme B integerBase hZ).obj T).Over (Spec (.of k)) :=
      ⟨(BigFppfOver.toScheme B integerBase hZ).map g ≫ eqToHom hW⟩
    ((∃ Y : (nodalCurvesFiberedCategory B hZ).based.obj,
        (CatFiberedInGroupoids.homFunctor (nodalCurvesInclusion B hZ)).obj Y =
          curveFamilyOfProperOverFieldEqSpec B hZ g k hW hproper hdim) ↔
      (Stacks.Curves.HasAtWorstNodalSingularities k
          ((BigFppfOver.toScheme B integerBase hZ).obj T) ∧
        Equidimensional ((BigFppfOver.toScheme B integerBase hZ).obj T) ∧
        ∀ Z ∈ irreducibleComponents ((BigFppfOver.toScheme B integerBase hZ).obj T),
          topologicalKrullDim Z = (1 : WithBot ℕ∞)))
```

**`AlgebraicGeometry.isNodalCurveFamily_of_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean#L70). The attribute's comment: “the open substack Curves^nodal, base-change clause: the at-worst-nodal condition is inherited along every morphism of families of curves, and a morphism of families is a cartesian square, so the subcategory is closed under base change. Unconditional: no presentation of Curves as an algebraic stack (Tag 0D5A) and no part of Tag 04S6 is assumed”.

> A family of curves mapping to an at-worst-nodal family of relative dimension one is itself
> at-worst-nodal of relative dimension one.

```lean
theorem isNodalCurveFamily_of_hom {F G : CurveFamily B hZ} (a : F ⟶ G)
    (hG : isNodalCurveFamily B hZ G) : isNodalCurveFamily B hZ F
```

**`AlgebraicGeometry.isClosedUnderIsomorphisms_isNodalCurveFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean#L80). The attribute's comment: “the open substack Curves^nodal, strict-fullness clause: the at-worst-nodal condition is invariant under isomorphism of families of curves, so it cuts a strictly full subcategory out of Curves. Unconditional: no presentation of Curves as an algebraic stack (Tag 0D5A) and no part of Tag 04S6 is assumed”.

> **Stacks 0DSY.** The nodal condition cuts a *strictly* full subcategory out of the category
> of families of curves: it is invariant under isomorphism.

```lean
theorem isClosedUnderIsomorphisms_isNodalCurveFamily :
    (isNodalCurveFamily B hZ).IsClosedUnderIsomorphisms
```

**`AlgebraicGeometry.nodalCurvesOpenSubstackUnconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean#L111). The attribute's comment: “the open substack and part (1): the characterisation on every family of curves, given a presentation of the algebraic stack of curves. Part (2), the characterisation for a proper scheme over a field, is registered separately on `AlgebraicGeometry.lifts_nodalCurves_curveFamilyOfProperOverField_iff`”.

> **Stacks 0DSY, part (1).** The open substack `Curves^{nodal}` of families of curves which are
> at-worst-nodal of relative dimension one, together with the characterisation of its objects: an
> object of the stack belongs to it exactly when the family of curves it classifies is
> at-worst-nodal of relative dimension one.
>
> This is `AlgebraicGeometry.curvesOpenSubstackOfBaseLocus`, the method of Section 109.6, at the
> locus `AlgebraicGeometry.exists_nodal_baseOpen`.
>
> The algebraic stack of curves is a hypothesis: `𝒳` is any algebraic stack over the big fppf site
> of the integers whose objects are identified with families of curves by an equivalence `E` over
> that site. Nothing else is assumed; in particular no part of Stacks 04S6 is, the algebraic-stack
> field of the substack coming from the unconditional Stacks 05UM.
>
> Part (2) of the source, the characterisation for a proper scheme over a field, is not asserted
> here.
>
> The definition carries `@[no_expose]`: its body names the private helpers that build the
> substack, so it may not be exposed. Nothing downstream needs to unfold it — the
> characterisation of its objects is the second component of the subtype.

```lean
def nodalCurvesOpenSubstackUnconditional
    (𝒳 : Stack.AlgebraicStacks.{u, w} B integerBase hZ)
    (E : CurveFamily B hZ ≌ 𝒳.val.val.obj)
    (hE : E.functor ⋙ 𝒳.val.val.p = curvesProjectionOver B hZ) :
    {U : Stack.OpenSubstack 𝒳 //
      ∀ F : CurveFamily B hZ,
        U.property (E.functor.obj F) ↔
          Space.IsAtWorstNodalOfRelativeDimensionOne B integerBase hZ F.toBase.hom}
```

**`AlgebraicGeometry.classifying_factors_nodalCurvesOpenSubstack_iff_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean#L133). The attribute's comment: “part (1): the classifying morphism of a family factors through the nodal open substack iff the family is at-worst-nodal of relative dimension one, given a presentation of the algebraic stack of curves. Part (2), the characterisation for a proper scheme over a field, is registered separately on `AlgebraicGeometry.lifts_nodalCurves_curveFamilyOfProperOverField_iff`”.

> **Stacks 0DSY, part (1).** The classifying object of a family of curves lifts through the
> inclusion of the nodal open substack exactly when the family is at-worst-nodal of relative
> dimension one.
>
> As for `AlgebraicGeometry.nodalCurvesOpenSubstackUnconditional`, the algebraic stack of curves
> and its identification with families of curves are hypotheses, and nothing else is assumed.

```lean
theorem classifying_factors_nodalCurvesOpenSubstack_iff_unconditional
    (𝒳 : Stack.AlgebraicStacks.{u, w} B integerBase hZ)
    (E : CurveFamily B hZ ≌ 𝒳.val.val.obj)
    (hE : E.functor ⋙ 𝒳.val.val.p = curvesProjectionOver B hZ)
    (F : CurveFamily B hZ) :
    (∃ Y : (nodalCurvesOpenSubstackUnconditional B hZ 𝒳 E hE).1.property.FullSubcategory,
      Y.obj = E.functor.obj F) ↔
      Space.IsAtWorstNodalOfRelativeDimensionOne B integerBase hZ F.toBase.hom
```

**`AlgebraicGeometry.nodalCurvesFiberedCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean#L158). The attribute's comment: “the open substack Curves^nodal itself, as the strictly full subcategory of Curves spanned by the families which are at-worst-nodal of relative dimension one, read as an object of the 2-category of categories fibred in groupoids over the big fppf site of Spec(Z). Unconditional: no presentation of Curves as an algebraic stack (Tag 0D5A) and no part of Tag 04S6 is assumed”.

> **Stacks 0DSY.** The category `Curves^{nodal}` of families of curves which are at-worst-nodal
> of relative dimension one, as an object of the 2-category of categories fibred in groupoids over
> the big fppf site of `Spec(ℤ)`.

```lean
def nodalCurvesFiberedCategory :
    CatFiberedInGroupoids.{u, u + 1, u + 1, u + 1} (BigFppfOver B integerBase hZ)
```

**`AlgebraicGeometry.nodalCurvesInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean#L168). The attribute's comment: “the inclusion Curves^nodal ⊂ Curves of the open substack, as a 1-morphism of categories fibred in groupoids over the big fppf site of Spec(Z). Unconditional: no presentation of Curves as an algebraic stack (Tag 0D5A) and no part of Tag 04S6 is assumed”.

> **Stacks 0DSY.** The inclusion `Curves^{nodal} ⊂ Curves`, as a 1-morphism of categories
> fibred in groupoids over the big fppf site of `Spec(ℤ)`.

```lean
def nodalCurvesInclusion :
    nodalCurvesFiberedCategory B hZ ⟶ curvesFiberedCategory B hZ
```

**`AlgebraicGeometry.isRepresentableByAlgebraicSpaces_nodalCurvesInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean#L178). The attribute's comment: “the open substack Curves^nodal, representability clause: the inclusion Curves^nodal ⊂ Curves is representable by algebraic spaces. Unconditional: no presentation of Curves as an algebraic stack (Tag 0D5A) and no part of Tag 04S6 is assumed”.

> **Stacks 0DSY.** The inclusion `Curves^{nodal} ⊂ Curves` is representable by algebraic
> spaces.

```lean
theorem isRepresentableByAlgebraicSpaces_nodalCurvesInclusion :
    Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ (nodalCurvesInclusion B hZ).hom
```

**`AlgebraicGeometry.isOpenImmersion_nodalCurvesInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean#L189). The attribute's comment: “the open substack Curves^nodal, open-immersion clause: the inclusion Curves^nodal ⊂ Curves is an open immersion in the sense of Tag 04XB. Unconditional: no presentation of Curves as an algebraic stack (Tag 0D5A) and no part of Tag 04S6 is assumed”.

> **Stacks 0DSY.** The inclusion `Curves^{nodal} ⊂ Curves` is an open immersion: every
> algebraic space representing one of its base changes along a scheme-valued point of `Curves` has
> open immersion structural morphism.

```lean
theorem isOpenImmersion_nodalCurvesInclusion :
    Stack.IsOpenImmersion B integerBase hZ (nodalCurvesInclusion B hZ)
```

**`AlgebraicGeometry.lifts_nodalCurves_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean#L201). The attribute's comment: “part (1): the classifying morphism of a family of curves factors through Curves^nodal -- that is, the family lifts through the inclusion of the strictly full subcategory -- if and only if the family is at-worst-nodal of relative dimension one. Unconditional: no presentation of Curves as an algebraic stack (Tag 0D5A) and no part of Tag 04S6 is assumed”.

> **Stacks 0DSY, part (1).** A family of curves lifts through the inclusion
> `Curves^{nodal} ⊂ Curves` exactly when it is at-worst-nodal of relative dimension one.

```lean
theorem lifts_nodalCurves_iff (F : CurveFamily B hZ) :
    (∃ Y : (isNodalCurveFamily B hZ).FullSubcategory, Y.obj = F) ↔
      Space.IsAtWorstNodalOfRelativeDimensionOne B integerBase hZ F.toBase.hom
```

**`AlgebraicGeometry.lifts_nodalCurvesInclusion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalUnconditional.lean#L225). The attribute's comment: “part (1), stated through the inclusion 1-morphism AlgebraicGeometry.nodalCurvesInclusion of the open substack: a family of curves is in the image on objects of Curves^nodal ⟶ Curves if and only if it is at-worst-nodal of relative dimension one. Unconditional: no presentation of Curves as an algebraic stack (Tag 0D5A) and no part of Tag 04S6 is assumed”.

> **Stacks 0DSY, part (1).** The classifying morphism of a family of curves factors through
> `Curves^{nodal}` exactly when the family is at-worst-nodal of relative dimension one, where
> factoring through `Curves^{nodal}` is being in the image on objects of the 1-morphism
> `AlgebraicGeometry.nodalCurvesInclusion` itself.
>
> This is `AlgebraicGeometry.lifts_nodalCurves_iff` read through that 1-morphism, so that part (1)
> is asserted about the very object whose inclusion is proved representable by algebraic spaces
> and an open immersion in
> `AlgebraicGeometry.isRepresentableByAlgebraicSpaces_nodalCurvesInclusion` and
> `AlgebraicGeometry.isOpenImmersion_nodalCurvesInclusion`.
>
> The declaration carries no hypothesis beyond the site and its containing `Spec(ℤ)`: there is no
> algebraic stack `𝒳` and no equivalence identifying it with the category of families of
> curves.

```lean
theorem lifts_nodalCurvesInclusion_iff (F : CurveFamily B hZ) :
    (∃ Y : (nodalCurvesFiberedCategory B hZ).based.obj,
        (CatFiberedInGroupoids.homFunctor (nodalCurvesInclusion B hZ)).obj Y = F) ↔
      Space.IsAtWorstNodalOfRelativeDimensionOne B integerBase hZ F.toBase.hom
```

## Tag 0E00, a lemma

[Tag 0E00](https://stacks.math.columbia.edu/tag/0E00) in the Stacks Project.

**`AlgebraicGeometry.isSmoothOverIntegers_curvesNodal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalSmooth.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesNodalSmooth.lean#L52).

> The morphism `Curves^{nodal} → Spec(ℤ)` is smooth. Here `Curves^{nodal}` is the open substack
> of the algebraic stack of curves (Stacks 0D5A) of the families of curves which are at-worst-nodal
> of relative dimension one (Stacks 0DSY).

```lean
theorem isSmoothOverIntegers_curvesNodal :
    IsSmoothOverIntegers B hZ (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)
      (isOpenCurvesLocus_isAtWorstNodal B hZ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.18, Tag 0DSX](https://stacks.math.columbia.edu/tag/0DSX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
