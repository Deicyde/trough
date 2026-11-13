---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.existsUnique_reducedClosedSubspace, AlgebraicGeometry.Space.isEmbedding_pointsMap_of_isImmersion, AlgebraicGeometry.Space.isLocallyClosed_range_pointsMap_of_isImmersion, AlgebraicGeometry.Space.invariantLocallyClosedSubschemeEquiv_of_isAlgebraicSpace, AlgebraicGeometry.Space.closed_iff_of_isAlgebraicSpace, AlgebraicGeometry.Space.open_iff_of_isAlgebraicSpace, AlgebraicGeometry.Space.Presentation.invariantLocallyClosedSubschemeEquivOfExtendsRelation, AlgebraicGeometry.Space.Presentation.closed_iff_of_extendsRelation
statement: formalized
proof: formalized
---

# 66.12 Reduced spaces

Section 66.12 of the Stacks Project, [Tag 03IP](https://stacks.math.columbia.edu/tag/03IP). 6 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03IP, the section

[Tag 03IP](https://stacks.math.columbia.edu/tag/03IP) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_reducedClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean, line 940](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean#L940). The attribute's comment: “the SECTION tag `\section{Reduced spaces}`; its central lemma is 03IQ, the unique reduced closed subspace structure on a closed subset”.

> **Stacks 03IQ**: a closed subset of the points of an algebraic space carries a unique
> reduced closed subspace structure, with no hypothesis.
>
> Uniqueness is `AlgebraicGeometry.Space.eq_reducedClosedSubspace`, the witness is the
> datum `AlgebraicGeometry.Space.reducedClosedSubspace`, and the closed-subspace clause of
> existence is `AlgebraicGeometry.Space.isClosedSubspace_reducedClosedSubspace`, whose own
> descent hypothesis is discharged by
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isClosedImmersion`.
>
> This declaration also carries the SECTION tag 03IP, `\section{Reduced spaces}`: the section
> states no result of its own, and its central lemma is 03IQ, the reduced closed subspace
> structure on a closed subset.

```lean
theorem existsUnique_reducedClosedSubspace
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) (T : Set (points B S hS X)) (hT : IsClosed T) :
    ∃! Z : Subfunctor X,
      IsClosedSubspace B S hS Z ∧
        Set.range (pointsMap B S hS Z.toFunctor Z.ι) = T ∧
          HasEtaleLocalProperty B S hS Z.toFunctor (fun Y : Scheme.{u} => IsReduced Y)
```

## Tag 0ABJ, a lemma

[Tag 0ABJ](https://stacks.math.columbia.edu/tag/0ABJ) in the Stacks Project.

**`AlgebraicGeometry.Space.isEmbedding_pointsMap_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ImmersionPointEmbedding.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ImmersionPointEmbedding.lean#L219). The attribute's comment: “homeomorphism onto the image”.

> **Stacks 0ABJ, part one.** The map on points of an immersion of algebraic spaces over `S`
> is a topological embedding: a homeomorphism onto its image.

```lean
theorem isEmbedding_pointsMap_of_isImmersion (hX : IsAlgebraicSpace B S hS X) (i : Z ⟶ X)
    (hi : IsImmersion B S hS i) :
    Topology.IsEmbedding (pointsMap B S hS Z i)
```

**`AlgebraicGeometry.Space.isLocallyClosed_range_pointsMap_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ImmersionPointEmbedding.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ImmersionPointEmbedding.lean#L228). The attribute's comment: “locally closed image”.

> **Stacks 0ABJ, part two.** The image on points of an immersion of algebraic spaces over
> `S` is a locally closed subset of the point space of the target.

```lean
theorem isLocallyClosed_range_pointsMap_of_isImmersion (hX : IsAlgebraicSpace B S hS X)
    (i : Z ⟶ X) (hi : IsImmersion B S hS i) :
    IsLocallyClosed (Set.range (pointsMap B S hS Z i))
```

## Tag 07TW, a lemma

[Tag 07TW](https://stacks.math.columbia.edu/tag/07TW) in the Stacks Project.

**`AlgebraicGeometry.Space.invariantLocallyClosedSubschemeEquiv_of_isAlgebraicSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/ImmersionEtaleDescent.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/ImmersionEtaleDescent.lean#L351). The attribute's comment: “canonical bijection”.

> For an algebraic space `X` over `S` with a surjective étale chart `φ : U ⟶ X`, the invariant
> locally closed subschemes of `U` correspond bijectively to the locally closed subspaces of `X`,
> and the bijection is characterised by pullback along `φ`.
>
> This is `AlgebraicGeometry.Space.invariantLocallyClosedSubschemeEquiv` with its hypothesis
> `hdesc` supplied by
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isImmersion`.

```lean
noncomputable def invariantLocallyClosedSubschemeEquiv_of_isAlgebraicSpace
    (hX : IsAlgebraicSpace B S hS X) :
    {e : InvariantLocallyClosedSubscheme B S hS hs ≃
      LocallyClosedQuotientSubspace B S hS (X := X) //
      ∀ Z, ((e Z).1.preimage φ) = subschemePoints B S hS Z.1}
```

**`AlgebraicGeometry.Space.closed_iff_of_isAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/ImmersionEtaleDescent.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/ImmersionEtaleDescent.lean#L366). The attribute's comment: “closedness”.

> The subspace of `X` corresponding to an invariant subscheme of the chart is closed exactly when
> that subscheme is closed in the chart.
>
> This is `AlgebraicGeometry.Space.closed_iff` with its hypothesis `hdesc` supplied by
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isImmersion`.

```lean
theorem closed_iff_of_isAlgebraicSpace (hX : IsAlgebraicSpace B S hS X)
    (Z : InvariantLocallyClosedSubscheme B S hS hs) :
    IsClosedSubspace B S hS
        ((invariantLocallyClosedSubschemeEquiv_of_isAlgebraicSpace B S hS hs he hX).1 Z).1 ↔
      _root_.AlgebraicGeometry.IsClosedImmersion Z.1.arrow
```

**`AlgebraicGeometry.Space.open_iff_of_isAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/ImmersionEtaleDescent.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/ImmersionEtaleDescent.lean#L381). The attribute's comment: “openness”.

> The subspace of `X` corresponding to an invariant subscheme of the chart is open exactly when
> that subscheme is open in the chart.
>
> This is `AlgebraicGeometry.Space.open_iff` with its hypothesis `hdesc` supplied by
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isImmersion`.

```lean
theorem open_iff_of_isAlgebraicSpace (hX : IsAlgebraicSpace B S hS X)
    (Z : InvariantLocallyClosedSubscheme B S hS hs) :
    IsOpenSubspace B S hS
        ((invariantLocallyClosedSubschemeEquiv_of_isAlgebraicSpace B S hS hs he hX).1 Z).1 ↔
      _root_.AlgebraicGeometry.IsOpenImmersion Z.1.arrow
```

**`AlgebraicGeometry.Space.Presentation.invariantLocallyClosedSubschemeEquivOfExtendsRelation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvariantSubschemeGroupoid.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/InvariantSubschemeGroupoid.lean#L190). The attribute's comment: “the canonical bijection, with invariance taken in the groupoid sense”.

> **Stacks 07TW**, the canonical bijection, with invariance of the subschemes of the
> presenting scheme taken in the groupoid sense of Stacks 03BC part (4) against any groupoid
> scheme extending the presenting relation.
>
> Effective descent of immersions along the surjective étale morphisms of the site, which is
> Stacks 02W8 in the form Stacks 03I2 consumes, is
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isImmersion`.

```lean
noncomputable def Presentation.invariantLocallyClosedSubschemeEquivOfExtendsRelation
    (P : Presentation B S hS X hX) {G : GroupoidScheme S}
    (hG : ExtendsRelation (prod.lift ((Over.post B.inclusion).map P.target)
      ((Over.post B.inclusion).map P.source)) G)
    (hobj : G.objects.left = (BigFppfOver.toScheme B S hS).obj P.U) :
    {e : {Z : Subobject ((BigFppfOver.toScheme B S hS).obj P.U) //
            AlgebraicGeometry.IsImmersion Z.arrow ∧
              IsInvariantMonomorphism G (Z.arrow ≫ eqToHom hobj.symm)} ≃
          LocallyClosedQuotientSubspace B S hS (X := X) //
      ∀ Z, ((e Z).1.preimage P.toSpace) = subschemePoints B S hS Z.1}
```

**`AlgebraicGeometry.Space.Presentation.closed_iff_of_extendsRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvariantSubschemeGroupoid.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/InvariantSubschemeGroupoid.lean#L211). The attribute's comment: “closedness, with invariance taken in the groupoid sense”.

> **Stacks 07TW**, closedness, with invariance taken in the groupoid sense: the subspace of
> the presented algebraic space corresponding to an invariant subscheme of the presenting scheme
> is closed exactly when that subscheme is closed.

```lean
theorem Presentation.closed_iff_of_extendsRelation
    (P : Presentation B S hS X hX) {G : GroupoidScheme S}
    (hG : ExtendsRelation (prod.lift ((Over.post B.inclusion).map P.target)
      ((Over.post B.inclusion).map P.source)) G)
    (hobj : G.objects.left = (BigFppfOver.toScheme B S hS).obj P.U)
    (Z : {Z : Subobject ((BigFppfOver.toScheme B S hS).obj P.U) //
      AlgebraicGeometry.IsImmersion Z.arrow ∧
        IsInvariantMonomorphism G (Z.arrow ≫ eqToHom hobj.symm)}) :
    IsClosedSubspace B S hS
        ((P.invariantLocallyClosedSubschemeEquivOfExtendsRelation B S hS hG hobj).1 Z).1 ↔
      AlgebraicGeometry.IsClosedImmersion Z.1.arrow
```

**`AlgebraicGeometry.Space.Presentation.open_iff_of_extendsRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvariantSubschemeGroupoid.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/InvariantSubschemeGroupoid.lean#L229). The attribute's comment: “openness, with invariance taken in the groupoid sense”.

> **Stacks 07TW**, openness, with invariance taken in the groupoid sense: the subspace of
> the presented algebraic space corresponding to an invariant subscheme of the presenting scheme
> is open exactly when that subscheme is open.

```lean
theorem Presentation.open_iff_of_extendsRelation
    (P : Presentation B S hS X hX) {G : GroupoidScheme S}
    (hG : ExtendsRelation (prod.lift ((Over.post B.inclusion).map P.target)
      ((Over.post B.inclusion).map P.source)) G)
    (hobj : G.objects.left = (BigFppfOver.toScheme B S hS).obj P.U)
    (Z : {Z : Subobject ((BigFppfOver.toScheme B S hS).obj P.U) //
      AlgebraicGeometry.IsImmersion Z.arrow ∧
        IsInvariantMonomorphism G (Z.arrow ≫ eqToHom hobj.symm)}) :
    IsOpenSubspace B S hS
        ((P.invariantLocallyClosedSubschemeEquivOfExtendsRelation B S hS hG hobj).1 Z).1 ↔
      AlgebraicGeometry.IsOpenImmersion Z.1.arrow
```

## Tag 03IQ, a lemma

[Tag 03IQ](https://stacks.math.columbia.edu/tag/03IQ) in the Stacks Project.

**`AlgebraicGeometry.Space.reducedClosedSubspace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean, line 831](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean#L831). The attribute's comment: “the subspace itself, on a closed set of points”.

> **The reduced closed subspace of an algebraic space supported on a closed set of
> points**, as data rather than as a choice of a witness to an existence statement.
>
> It is `AlgebraicGeometry.Space.reducedClosedSubspaceOfChart` at a chart chosen from the
> atlas clause of the algebraic-space hypothesis. The choice is of a chart, which the
> hypothesis provides; it is not a choice of the subspace, and by
> `AlgebraicGeometry.Space.eq_reducedClosedSubspaceOfChart` the result does not depend on it.

```lean
noncomputable def reducedClosedSubspace (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X)
    (T : Set (points B S hS X)) (hT : IsClosed T) : Subfunctor X
```

**`AlgebraicGeometry.Space.range_pointsMap_ι_reducedClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean, line 839](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean#L839). The attribute's comment: “property (a): the point set of the subspace is the given closed set”.

> **The point set of the reduced closed subspace is the closed set one started with.**

```lean
theorem range_pointsMap_ι_reducedClosedSubspace (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X)
    (T : Set (points B S hS X)) (hT : IsClosed T) :
    Set.range (pointsMap B S hS (reducedClosedSubspace B S hS X hX T hT).toFunctor
      (reducedClosedSubspace B S hS X hX T hT).ι) = T
```

**`AlgebraicGeometry.Space.hasEtaleLocalProperty_isReduced_reducedClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean, line 850](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean#L850). The attribute's comment: “property (b): the subspace is reduced”.

> **The reduced closed subspace is reduced**, in the étale-local sense of Stacks 03E6.

```lean
theorem hasEtaleLocalProperty_isReduced_reducedClosedSubspace
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) (T : Set (points B S hS X)) (hT : IsClosed T) :
    HasEtaleLocalProperty B S hS (reducedClosedSubspace B S hS X hX T hT).toFunctor
      (fun Y : Scheme.{u} => IsReduced Y)
```

**`AlgebraicGeometry.Space.isClosedSubspace_reducedClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean, line 902](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean#L902). The attribute's comment: “property (c): the subspace is a closed subspace”.

> **The reduced closed subspace is a closed subspace**, unconditionally: the inclusion of
> `AlgebraicGeometry.Space.reducedClosedSubspace` into `X` is representable and a closed immersion
> after every representable base change.
>
> This is
> `AlgebraicGeometry.Space.isClosedSubspace_reducedClosedSubspace_of_closedImmersionDescent` with
> its hypothesis discharged by
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isClosedImmersion`.

```lean
theorem isClosedSubspace_reducedClosedSubspace
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) (T : Set (points B S hS X)) (hT : IsClosed T) :
    IsClosedSubspace B S hS (reducedClosedSubspace B S hS X hX T hT)
```

**`AlgebraicGeometry.Space.eq_reducedClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean, line 913](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean#L913). The attribute's comment: “uniqueness, unconditionally”.

> **Stacks 03IQ, uniqueness, unconditionally.** A closed subspace of an algebraic space
> which is étale-locally reduced and has a given set of points is
> `AlgebraicGeometry.Space.reducedClosedSubspace`.

```lean
theorem eq_reducedClosedSubspace (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X)
    (T : Set (points B S hS X)) (hT : IsClosed T) (W : Subfunctor X)
    (hWc : IsClosedSubspace B S hS W)
    (hWT : Set.range (pointsMap B S hS W.toFunctor W.ι) = T)
    (hWr : HasEtaleLocalProperty B S hS W.toFunctor (fun Y : Scheme.{u} => IsReduced Y)) :
    W = reducedClosedSubspace B S hS X hX T hT
```

**`AlgebraicGeometry.Space.existsUnique_reducedClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean, line 940](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspace.lean#L940). The attribute's comment: “existence and uniqueness”.

> **Stacks 03IQ**: a closed subset of the points of an algebraic space carries a unique
> reduced closed subspace structure, with no hypothesis.
>
> Uniqueness is `AlgebraicGeometry.Space.eq_reducedClosedSubspace`, the witness is the
> datum `AlgebraicGeometry.Space.reducedClosedSubspace`, and the closed-subspace clause of
> existence is `AlgebraicGeometry.Space.isClosedSubspace_reducedClosedSubspace`, whose own
> descent hypothesis is discharged by
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isClosedImmersion`.
>
> This declaration also carries the SECTION tag 03IP, `\section{Reduced spaces}`: the section
> states no result of its own, and its central lemma is 03IQ, the reduced closed subspace
> structure on a closed subset.

```lean
theorem existsUnique_reducedClosedSubspace
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) (T : Set (points B S hS X)) (hT : IsClosed T) :
    ∃! Z : Subfunctor X,
      IsClosedSubspace B S hS Z ∧
        Set.range (pointsMap B S hS Z.toFunctor Z.ι) = T ∧
          HasEtaleLocalProperty B S hS Z.toFunctor (fun Y : Scheme.{u} => IsReduced Y)
```

**`AlgebraicGeometry.Space.existsUnique_reducedClosedSubspace'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspaceDescent.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspaceDescent.lean#L91).

> **Stacks 03IQ.** A closed subset of the set of points of an algebraic space over `S`
> carries a unique reduced closed subspace structure: there is exactly one subfunctor of `X`
> which is a closed subspace, has that closed set as its set of points, and is étale-locally
> reduced.
>
> The witness is `AlgebraicGeometry.Space.reducedClosedSubspace`, which is constructed explicitly.

```lean
theorem existsUnique_reducedClosedSubspace' (hX : IsAlgebraicSpace B S hS X)
    (T : Set (points B S hS X)) (hT : _root_.IsClosed T) :
    ∃! Z : Subfunctor X,
      IsClosedSubspace B S hS Z ∧
        Set.range (pointsMap B S hS Z.toFunctor Z.ι) = T ∧
          HasEtaleLocalProperty B S hS Z.toFunctor (fun Y : Scheme.{u} => IsReduced Y)
```

## Tag 03JJ, a lemma

[Tag 03JJ](https://stacks.math.columbia.edu/tag/03JJ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_lift_closedSubspace_iff_pointsMap_range_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ReducedFactorThroughClosedSubspace.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ReducedFactorThroughClosedSubspace.lean#L96).

> **Stacks 03JJ.** A morphism from a reduced algebraic space factors through a closed
> subspace if and only if its image on underlying points lies in that closed subspace.

```lean
theorem exists_lift_closedSubspace_iff_pointsMap_range_subset (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (Z : Subfunctor X) (hZ : IsClosedSubspace B S hS Z)
    (hred : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsReduced T))
    (f : Y ⟶ X) :
    (∃ g : Y ⟶ Z.toFunctor, g ≫ Z.ι = f) ↔
      Set.range (pointsMap B S hS Y f) ⊆ Set.range (pointsMap B S hS Z.toFunctor Z.ι)
```

## Tag 047X, a definition

[Tag 047X](https://stacks.math.columbia.edu/tag/047X) in the Stacks Project.

**`AlgebraicGeometry.Space.IsAlgebraicSpaceStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Reduction.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Reduction.lean#L85). The attribute's comment: “algebraic space structure on a closed set of points”.

> **Stacks 047X.** An *algebraic space structure* on a closed set `Z` of points of an
> algebraic space `X` over `S` is a closed subspace of `X` whose set of points is `Z`.

```lean
def IsAlgebraicSpaceStructure {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (Z : Set (points B S hS X)) (Z' : Subfunctor X) : Prop
```

**`AlgebraicGeometry.Space.isAlgebraicSpaceStructure_reducedClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Reduction.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Reduction.lean#L109). The attribute's comment: “the reduced induced structure”.

> **Stacks 047X, the reduced induced structure.** The subspace of Stacks 03IQ on a closed set
> of points is an algebraic space structure on that set. That it is moreover reduced is
> `AlgebraicGeometry.Space.hasEtaleLocalProperty_isReduced_reducedClosedSubspace`, and that it is
> the only reduced one is
> `AlgebraicGeometry.Space.existsUnique_isAlgebraicSpaceStructure_isReduced`.

```lean
theorem isAlgebraicSpaceStructure_reducedClosedSubspace
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (Z : Set (points B S hS X)) (hZ : IsClosed Z) :
    IsAlgebraicSpaceStructure B S hS Z (reducedClosedSubspace B S hS X hX Z hZ)
```

**`AlgebraicGeometry.Space.existsUnique_isAlgebraicSpaceStructure_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Reduction.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Reduction.lean#L147). The attribute's comment: “the reduced induced structure is the unique reduced one”.

> **Stacks 047X, the reduced induced structure characterized.** A closed set of points of an
> algebraic space carries exactly one reduced algebraic space structure, namely the subspace of
> Stacks 03IQ. This is what makes *the* reduced induced structure well defined.

```lean
theorem existsUnique_isAlgebraicSpaceStructure_isReduced
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (Z : Set (points B S hS X)) (hZ : IsClosed Z) :
    ∃! Z' : Subfunctor X,
      IsAlgebraicSpaceStructure B S hS Z Z' ∧
        HasEtaleLocalProperty B S hS Z'.toFunctor (fun Y : Scheme.{u} => IsReduced Y)
```

**`AlgebraicGeometry.Space.reduction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Reduction.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Reduction.lean#L162). The attribute's comment: “the reduction”.

> **Stacks 047X, the reduction.** The *reduction* `X_red` of an algebraic space `X` over `S` is
> the reduced induced algebraic space structure on the whole of its space of points: the subspace
> of Stacks 03IQ at the closed set `Set.univ`.

```lean
noncomputable def reduction (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) : Subfunctor X
```

**`AlgebraicGeometry.Space.existsUnique_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Reduction.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Reduction.lean#L218). The attribute's comment: “the reduction is the unique reduced structure on the whole point set”.

> **Stacks 047X, the reduction characterized.** The reduction is the unique reduced algebraic
> space structure on the whole space of points.

```lean
theorem existsUnique_reduction (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) :
    ∃! Z' : Subfunctor X,
      IsAlgebraicSpaceStructure B S hS (Set.univ : Set (points B S hS X)) Z' ∧
        HasEtaleLocalProperty B S hS Z'.toFunctor (fun Y : Scheme.{u} => IsReduced Y)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.12, Tag 03IP](https://stacks.math.columbia.edu/tag/03IP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
