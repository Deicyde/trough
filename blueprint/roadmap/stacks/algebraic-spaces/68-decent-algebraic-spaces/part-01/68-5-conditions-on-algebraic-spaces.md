---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isRepresentable_of_isQuasiSeparatedScheme, AlgebraicGeometry.Space.isAbsolutelyZariskiLocallyQuasiSeparated_of_isAbsolutelyQuasiSeparated, AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_of_isQuasiSeparatedScheme, AlgebraicGeometry.Space.hasFiniteChartFibersAtEveryPoint_of_hasFiniteChartAndRelationFibers, AlgebraicGeometry.Space.hasFiniteRelationFibersAtEveryPoint_of_hasFiniteChartAndRelationFibers, AlgebraicGeometry.Space.hasFiniteChartAndRelationFibersAtEveryPoint_of_alpha_and_beta, AlgebraicGeometry.Space.hasFiniteChartAndRelationFibersAtEveryPoint_iff_alpha_and_beta, AlgebraicGeometry.Space.isAbsolutelyZariskiLocallyQuasiSeparated_of_isRepresentable
statement: formalized
proof: formalized
---

# 68.5 Conditions on algebraic spaces

Section 68.5 of the Stacks Project, [Tag 03JW](https://stacks.math.columbia.edu/tag/03JW). 3 tags here are carried by 24 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03JX, a lemma

[Tag 03JX](https://stacks.math.columbia.edu/tag/03JX) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_of_isQuasiSeparatedScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean#L91). The attribute's comment: “(iota) implies (theta)”.

> Condition `(ι)` implies condition `(θ)`: an algebraic space which is a quasi-separated
> scheme is representable.

```lean
theorem isRepresentable_of_isQuasiSeparatedScheme
    (h : IsQuasiSeparatedScheme B S hS X) : X.IsRepresentable
```

**`AlgebraicGeometry.Space.isAbsolutelyZariskiLocallyQuasiSeparated_of_isAbsolutelyQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean#L101). The attribute's comment: “(eta) implies (zeta)”.

> Condition `(η)` implies condition `(ζ)`: a quasi-separated algebraic space is Zariski
> locally quasi-separated.

```lean
theorem isAbsolutelyZariskiLocallyQuasiSeparated_of_isAbsolutelyQuasiSeparated
    (hX : IsAlgebraicSpace B S hS X) (h : IsAbsolutelyQuasiSeparated B S hS hZ X) :
    IsAbsolutelyZariskiLocallyQuasiSeparated B S hS hZ X
```

**`AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_of_isQuasiSeparatedScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean#L130). The attribute's comment: “(iota) implies (eta)”.

> Condition `(ι)` implies condition `(η)`: an algebraic space which is a quasi-separated
> scheme is a quasi-separated algebraic space.

```lean
theorem isAbsolutelyQuasiSeparated_of_isQuasiSeparatedScheme
    (h : IsQuasiSeparatedScheme B S hS X) : IsAbsolutelyQuasiSeparated B S hS hZ X
```

**`AlgebraicGeometry.Space.hasFiniteChartFibersAtEveryPoint_of_hasFiniteChartAndRelationFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean#L156). The attribute's comment: “(gamma) implies (alpha)”.

> Condition `(γ)` implies condition `(α)`: if every affine étale chart has finite fibres
> together with its self-intersection, then every affine étale chart has finite fibres.

```lean
theorem hasFiniteChartFibersAtEveryPoint_of_hasFiniteChartAndRelationFibers
    (h : HasFiniteChartAndRelationFibersAtEveryPoint B S hS X) :
    HasFiniteChartFibersAtEveryPoint B S hS X
```

**`AlgebraicGeometry.Space.hasFiniteRelationFibersAtEveryPoint_of_hasFiniteChartAndRelationFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean#L189). The attribute's comment: “(gamma) implies (beta)”.

> Condition `(γ)` implies condition `(β)`, in the form of condition (1) of Stacks 03JU:
> for an algebraic space satisfying `(γ)`, every point has an étale chart and a pair of points
> above it whose relation fibre is finite.

```lean
theorem hasFiniteRelationFibersAtEveryPoint_of_hasFiniteChartAndRelationFibers
    (hX : IsAlgebraicSpace B S hS X)
    (h : HasFiniteChartAndRelationFibersAtEveryPoint B S hS X) :
    HasFiniteRelationFibersAtEveryPoint B S hS X
```

**`AlgebraicGeometry.Space.hasFiniteChartAndRelationFibersAtEveryPoint_of_alpha_and_beta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean#L208). The attribute's comment: “(alpha) and (beta) imply (gamma)”.

> Conditions `(α)` and `(β)` imply condition `(γ)`: an algebraic space all of whose affine
> étale charts have finite fibres and all of whose points have a finite relation fibre satisfies
> condition `(γ)`.

```lean
theorem hasFiniteChartAndRelationFibersAtEveryPoint_of_alpha_and_beta
    (hX : IsAlgebraicSpace B S hS X)
    (hα : HasFiniteChartFibersAtEveryPoint B S hS X)
    (hβ : HasFiniteRelationFibersAtEveryPoint B S hS X) :
    HasFiniteChartAndRelationFibersAtEveryPoint B S hS X
```

**`AlgebraicGeometry.Space.hasFiniteChartAndRelationFibersAtEveryPoint_iff_alpha_and_beta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean#L241). The attribute's comment: “(gamma) iff (alpha) and (beta)”.

> Condition `(γ)` is equivalent to conditions `(α)` and `(β)` together: for an algebraic
> space over `S`, finiteness of the fibres of every affine étale chart together with its
> self-intersection is equivalent to finiteness of the fibres of every affine étale chart
> together with finiteness of one relation fibre at every point.

```lean
theorem hasFiniteChartAndRelationFibersAtEveryPoint_iff_alpha_and_beta
    (hX : IsAlgebraicSpace B S hS X) :
    HasFiniteChartAndRelationFibersAtEveryPoint B S hS X ↔
      HasFiniteChartFibersAtEveryPoint B S hS X ∧
        HasFiniteRelationFibersAtEveryPoint B S hS X
```

**`AlgebraicGeometry.Space.isAbsolutelyZariskiLocallyQuasiSeparated_of_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean, line 629](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean#L629). The attribute's comment: “(theta) implies (zeta)”.

> Condition `(θ)` implies condition `(ζ)`: a representable algebraic space over `S` is
> Zariski locally quasi-separated.

```lean
theorem isAbsolutelyZariskiLocallyQuasiSeparated_of_isRepresentable
    (hX : IsAlgebraicSpace B S hS X) (h : X.IsRepresentable) :
    IsAbsolutelyZariskiLocallyQuasiSeparated B S hS hZ X
```

**`AlgebraicGeometry.Space.hasFiniteChartAndRelationFibersAtEveryPoint_of_isReasonableSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableImpliesFiniteFibres.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableImpliesFiniteFibres.lean#L72). The attribute's comment: “(delta) implies (gamma)”.

> **Stacks 03JX, `(δ) ⇒ (γ)`.** A reasonable algebraic space satisfies condition `(γ)`:
> above every point of it, every étale chart by an affine scheme has a finite fibre, and so
> does the self-intersection of that chart.

```lean
theorem hasFiniteChartAndRelationFibersAtEveryPoint_of_isReasonableSpace
    (hX : IsAlgebraicSpace B S hS X) (hr : IsReasonableSpace B S hS X) :
    HasFiniteChartAndRelationFibersAtEveryPoint B S hS X
```

**`AlgebraicGeometry.Space.isReasonableSpace_of_isVeryReasonableSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/VeryReasonableImpliesReasonable.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/VeryReasonableImpliesReasonable.lean#L177). The attribute's comment: “(epsilon) implies (delta)”.

> **Stacks 03JX, `(ε) ⇒ (δ)`.** A very reasonable algebraic space over `S` is reasonable:
> every étale chart of it by an affine scheme has universally bounded fibres.
>
> This is also the third implication of Stacks 03M5. The given family of charts is refined by the
> affine opens of its sources, which have universally bounded fibres over the space by
> `AlgebraicGeometry.Space.hasUniversallyBoundedFibers_affineOpen_comp_of_isQuasiCompact`, and
> Stacks 03JT turns one such jointly surjective family into reasonableness.

```lean
theorem isReasonableSpace_of_isVeryReasonableSpace
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (h : IsVeryReasonableSpace B S hS X) :
    IsReasonableSpace B S hS X
```

**`AlgebraicGeometry.Space.isVeryReasonableSpace_of_isAbsolutelyZariskiLocallyQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZariskiLocallyQuasiSeparatedVeryReasonable.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZariskiLocallyQuasiSeparatedVeryReasonable.lean#L238). The attribute's comment: “(zeta) implies (epsilon)”.

> A Zariski locally quasi-separated algebraic space over `S` is very reasonable: it admits a
> jointly surjective family of étale charts by schemes whose two self-intersection projections
> are quasi-compact.

```lean
theorem isVeryReasonableSpace_of_isAbsolutelyZariskiLocallyQuasiSeparated
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (hζ : IsAbsolutelyZariskiLocallyQuasiSeparated B S hS hZ X) :
    IsVeryReasonableSpace B S hS X
```

## Tag 03KE, a lemma

[Tag 03KE](https://stacks.math.columbia.edu/tag/03KE) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_of_isZariskiCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean#L271). The attribute's comment: “the case (theta)”.

> Condition `(θ)` is Zariski local: an algebraic space with a Zariski open covering by
> representable open subspaces is representable.

```lean
theorem isRepresentable_of_isZariskiCover (hX : IsAlgebraicSpace B S hS X)
    (I : Type u) (Xᵢ : I → Subfunctor X) (hcover : IsZariskiCover B S hS I Xᵢ)
    (hθ : ∀ i : I, (Xᵢ i).toFunctor.IsRepresentable) : X.IsRepresentable
```

**`AlgebraicGeometry.Space.hasFiniteChartFibersAtEveryPoint_of_isZariskiCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean#L309). The attribute's comment: “the case (alpha)”.

> Condition `(α)` is Zariski local: an algebraic space with a Zariski open covering by open
> subspaces satisfying condition `(α)` satisfies condition `(α)`.

```lean
theorem hasFiniteChartFibersAtEveryPoint_of_isZariskiCover (hX : IsAlgebraicSpace B S hS X)
    (I : Type u) (Xᵢ : I → Subfunctor X) (hcover : IsZariskiCover B S hS I Xᵢ)
    (hα : ∀ i : I, HasFiniteChartFibersAtEveryPoint B S hS (Xᵢ i).toFunctor) :
    HasFiniteChartFibersAtEveryPoint B S hS X
```

**`AlgebraicGeometry.Space.hasFiniteRelationFibersAtEveryPoint_of_isZariskiCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean#L409). The attribute's comment: “the case (beta)”.

> Condition `(β)` is Zariski local: an algebraic space with a Zariski open covering by open
> subspaces satisfying condition `(β)` satisfies condition `(β)`.

```lean
theorem hasFiniteRelationFibersAtEveryPoint_of_isZariskiCover
    (hX : IsAlgebraicSpace B S hS X) (I : Type u) (Xᵢ : I → Subfunctor X)
    (hcover : IsZariskiCover B S hS I Xᵢ)
    (hβ : ∀ i : I, HasFiniteRelationFibersAtEveryPoint B S hS (Xᵢ i).toFunctor) :
    HasFiniteRelationFibersAtEveryPoint B S hS X
```

**`AlgebraicGeometry.Space.hasFiniteChartAndRelationFibersAtEveryPoint_of_isZariskiCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean, line 438](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean#L438). The attribute's comment: “the case (gamma)”.

> Condition `(γ)` is Zariski local: an algebraic space with a Zariski open covering by open
> subspaces satisfying condition `(γ)` satisfies condition `(γ)`.

```lean
theorem hasFiniteChartAndRelationFibersAtEveryPoint_of_isZariskiCover
    (hX : IsAlgebraicSpace B S hS X) (I : Type u) (Xᵢ : I → Subfunctor X)
    (hcover : IsZariskiCover B S hS I Xᵢ)
    (hγ : ∀ i : I, HasFiniteChartAndRelationFibersAtEveryPoint B S hS (Xᵢ i).toFunctor) :
    HasFiniteChartAndRelationFibersAtEveryPoint B S hS X
```

**`AlgebraicGeometry.Space.isAbsolutelyZariskiLocallyQuasiSeparated_of_isZariskiCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean, line 550](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean#L550). The attribute's comment: “the case (zeta)”.

> Condition `(ζ)` is Zariski local: an algebraic space with a Zariski open covering by open
> subspaces which are Zariski locally quasi-separated is Zariski locally quasi-separated.

```lean
theorem isAbsolutelyZariskiLocallyQuasiSeparated_of_isZariskiCover
    (I : Type u) (Xᵢ : I → Subfunctor X) (hcover : IsZariskiCover B S hS I Xᵢ)
    (hζ : ∀ i : I, IsAbsolutelyZariskiLocallyQuasiSeparated B S hS hZ (Xᵢ i).toFunctor) :
    IsAbsolutelyZariskiLocallyQuasiSeparated B S hS hZ X
```

**`AlgebraicGeometry.Space.isReasonableSpace_of_isZariskiCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableZariskiLocal.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableZariskiLocal.lean#L82). The attribute's comment: “the case (delta)”.

> **Stacks 03KE, the case `(δ)`.** An algebraic space with a Zariski open covering by
> reasonable open subspaces is reasonable.
>
> Given an affine étale chart `φ : h_U ⟶ X`, the point sets of the members of the covering pull
> back to an open cover of the affine scheme `U`, which therefore has a finite refinement by
> affine opens each of which maps into a single member. Each of those affine opens is an affine
> étale chart of the member it maps into, so reasonableness there bounds its fibres, and
> Stacks 03JO carries the bound along the inclusion of the member; the finitely many bounds
> then assemble to one for `φ`.

```lean
theorem isReasonableSpace_of_isZariskiCover
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (I : Type u) (Xᵢ : I → Subfunctor X) (hcover : IsZariskiCover B S hS I Xᵢ)
    (hδ : ∀ i : I, IsReasonableSpace B S hS (Xᵢ i).toFunctor) :
    IsReasonableSpace B S hS X
```

**`AlgebraicGeometry.Space.isVeryReasonableSpace_of_isZariskiCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/VeryReasonableConditions.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/VeryReasonableConditions.lean#L64). The attribute's comment: “property\_epsilon”.

> **Stacks 03KE, the case `(ε)`.** Property `(ε)` of Stacks 03JX — very reasonableness — is
> local for Zariski coverings: a presheaf on the big fppf site of `S` admitting a Zariski
> covering by very reasonable open subspaces is itself very reasonable.

```lean
theorem isVeryReasonableSpace_of_isZariskiCover
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (I : Type u) (Xᵢ : I → Subfunctor X)
    (hcover : IsZariskiCover B S hS I Xᵢ)
    (hε : ∀ i : I, IsVeryReasonableSpace B S hS (Xᵢ i).toFunctor) :
    IsVeryReasonableSpace B S hS X
```

## Tag 03KF, a lemma

[Tag 03KF](https://stacks.math.columbia.edu/tag/03KF) in the Stacks Project.

**`AlgebraicGeometry.Space.isDecentSpace_of_relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PropertyGammaPermanence.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PropertyGammaPermanence.lean#L76). The attribute's comment: “property\_gamma, as condition (4) of Stacks 03JV”.

> Decency passes from the target of a representable morphism of presheaves on the big fppf
> site of `S` to its source, when the source is an algebraic space.

```lean
theorem isDecentSpace_of_relativelyRepresentable
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f) (hY : IsDecentSpace B S hS Y) :
    IsDecentSpace B S hS X
```

**`AlgebraicGeometry.Space.hasFiniteChartAndRelationFibersAtEveryPoint_of_relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PropertyGammaPermanence.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PropertyGammaPermanence.lean#L109). The attribute's comment: “property\_gamma”.

> Let `f : X ⟶ Y` be a representable morphism of algebraic spaces over `S`. If every étale
> chart of `Y` by an affine scheme and the self-intersection of that chart have finite fibres
> above every point, then the same holds for `X`.

```lean
theorem hasFiniteChartAndRelationFibersAtEveryPoint_of_relativelyRepresentable
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f)
    (hYγ : HasFiniteChartAndRelationFibersAtEveryPoint B S hS Y) :
    HasFiniteChartAndRelationFibersAtEveryPoint B S hS X
```

**`AlgebraicGeometry.Space.isReasonableSpace_of_relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonablePermanence.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonablePermanence.lean#L72). The attribute's comment: “property\_delta”.

> **Stacks 03KF, the case `(δ)`, and the reasonable half of Stacks 0ABT.** Property `(δ)`
> of Stacks 03JX — reasonableness — passes from the target of a representable morphism of
> algebraic spaces over `S` to its source.
>
> A jointly surjective family of étale charts of `Y` with universally bounded fibres, which
> reasonableness of `Y` provides through Stacks 03JT, base changes along `f` to a family of
> étale charts of `X`; the bounds survive by Stacks 03JN and joint surjectivity survives
> because the squares are cartesian, so Stacks 03JT applies to `X`.

```lean
theorem isReasonableSpace_of_relativelyRepresentable
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f) (hYr : IsReasonableSpace B S hS Y) :
    IsReasonableSpace B S hS X
```

**`AlgebraicGeometry.Space.hasFiniteRelationFibersAtEveryPoint_of_relativelyRepresentable_of_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RepresentablePermanence.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RepresentablePermanence.lean#L179). The attribute's comment: “property\_beta”.

> **Stacks 03KF, the case `(β)`.** Property `(β)` of Stacks 03JX passes from the target of
> a representable morphism of algebraic spaces over `S` to its source.
>
> Property `(β)` is condition (1) of Stacks 03JU at every point, which is how
> `AlgebraicGeometry.Space.HasFiniteRelationFibersAtEveryPoint` spells it. The source's
> argument runs on condition (4) instead, a monomorphic field-valued representative, so the
> hypothesis on `Y` is carried across the equivalences of Stacks 03JU before
> `AlgebraicGeometry.Space.hasFiniteRelationFibersAtEveryPoint_of_relativelyRepresentable`
> transports it to `X`; that is what makes `Y` an algebraic space a hypothesis here.

```lean
theorem hasFiniteRelationFibersAtEveryPoint_of_relativelyRepresentable_of_target
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f)
    (hYβ : HasFiniteRelationFibersAtEveryPoint B S hS Y) :
    HasFiniteRelationFibersAtEveryPoint B S hS X
```

**`AlgebraicGeometry.Space.isRepresentable_of_relativelyRepresentable_of_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RepresentablePermanence.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RepresentablePermanence.lean#L198). The attribute's comment: “property\_theta”.

> **Stacks 03KF, property `(θ)`.** Property `(θ)` of an algebraic space over `S` is
> representability of its functor of points, so this is the case `𝒫 = (θ)`: for a representable
> morphism `f : X ⟶ Y`, representability of `Y` gives representability of `X`.
>
> Neither the sheaf condition nor an atlas is used, so the implication holds for presheaves on
> any category; that general form is Stacks 03KC.

```lean
theorem isRepresentable_of_relativelyRepresentable_of_target
    (f : X ⟶ Y) (hf : yoneda.relativelyRepresentable f) (hYθ : Y.IsRepresentable) :
    X.IsRepresentable
```

**`AlgebraicGeometry.Space.isVeryReasonableSpace_of_relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/VeryReasonablePermanence.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/VeryReasonablePermanence.lean#L114). The attribute's comment: “property\_epsilon”.

> Property `(ε)` of Stacks 03JX, very reasonableness, passes from the target of a representable
> morphism of presheaves on the big fppf site of `S` to its source.

```lean
theorem isVeryReasonableSpace_of_relativelyRepresentable
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f) (hY : IsVeryReasonableSpace B S hS Y) :
    IsVeryReasonableSpace B S hS X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.5, Tag 03JW](https://stacks.math.columbia.edu/tag/03JW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
