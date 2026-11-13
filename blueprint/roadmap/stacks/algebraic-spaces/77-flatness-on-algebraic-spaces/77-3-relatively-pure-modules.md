---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsSpacePureAbove, AlgebraicGeometry.Space.IsSpacePureRelative, AlgebraicGeometry.Space.IsPureAbove, AlgebraicGeometry.Space.IsUniversallyPureAbove, AlgebraicGeometry.Space.IsUniversallyPureRelative, AlgebraicGeometry.Space.IsPureRelative, AlgebraicGeometry.Space.isUniversallyPureAbove_iff_forall_baseChange_isPureAbove, AlgebraicGeometry.Space.isUniversallyPureRelative_iff_forall_baseChange_isPureRelative
statement: formalized
proof: formalized
---

# 77.3 Relatively pure modules

Section 77.3 of the Stacks Project, [Tag 0CVC](https://stacks.math.columbia.edu/tag/0CVC). 6 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CVD, a definition

[Tag 0CVD](https://stacks.math.columbia.edu/tag/0CVD) in the Stacks Project.

**`AlgebraicGeometry.Space.IsSpacePureAbove`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProper.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProper.lean#L291). The attribute's comment: “part (3)”.

> **Stacks 0CVD, part (3).** The algebraic space `X` is *pure above `y`* when its structure
> sheaf `𝒪_X` is pure above `y`.
>
> The module of the situation plays no role: the condition is part (1) for the situation with the
> same morphism and the same chosen point whose module is `𝒪_X`.

```lean
def IsSpacePureAbove (P : PrePureSituation.{u, u} B S hS) : Prop
```

**`AlgebraicGeometry.Space.IsSpacePureRelative`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProper.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProper.lean#L301). The attribute's comment: “part (6)”.

> **Stacks 0CVD, part (6).** The algebraic space `X` is *`Y`-pure*, or *pure relative to
> `Y`*, when its structure sheaf `𝒪_X` is pure relative to `Y`.
>
> This is part (5) for the situation whose module is `𝒪_X`; neither the module nor the chosen
> point of the situation plays a role, the latter because purity relative to `Y` varies it over
> all of `|Y|`.

```lean
def IsSpacePureRelative (P : PrePureSituation.{u, u} B S hS) : Prop
```

**`AlgebraicGeometry.Space.IsPureAbove`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean#L216). The attribute's comment: “part (1), as the failure of condition (4) of Stacks 0CVB”.

> **Stacks 0CVD, part (1).** The module is *pure above `y`* when no impurity of `F` above `y`
> has its structure morphism `T ⟶ Y` quasi-finite at `t`.
>
> This is the failure of condition (4) of Stacks 0CVB, which is the condition the proof of
> Stacks 0CVF works with.

```lean
def IsPureAbove (P : PrePureSituation.{u, u} B S hS) : Prop
```

**`AlgebraicGeometry.Space.IsUniversallyPureAbove`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean#L222). The attribute's comment: “part (2)”.

> **Stacks 0CVD, part (2).** The module is *universally pure above `y`* when there is no
> impurity of `F` above `y` at all.

```lean
def IsUniversallyPureAbove (P : PrePureSituation.{u, u} B S hS) : Prop
```

**`AlgebraicGeometry.Space.IsUniversallyPureRelative`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean#L234). The attribute's comment: “part (4)”.

> **Stacks 0CVD, part (4).** The module is *universally pure relative to `Y`* when it is
> universally pure above every point of `Y`.
>
> The chosen point of the situation is irrelevant: the condition varies it over all of `|Y|`.

```lean
def IsUniversallyPureRelative (P : PrePureSituation.{u, u} B S hS) : Prop
```

**`AlgebraicGeometry.Space.IsPureRelative`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean#L242). The attribute's comment: “part (5)”.

> **Stacks 0CVD, part (5).** The module is *pure relative to `Y`* when it is pure above every
> point of `Y`.
>
> The chosen point of the situation is irrelevant: the condition varies it over all of `|Y|`.

```lean
def IsPureRelative (P : PrePureSituation.{u, u} B S hS) : Prop
```

## Tag 0CVE, a lemma

[Tag 0CVE](https://stacks.math.columbia.edu/tag/0CVE) in the Stacks Project.

**`AlgebraicGeometry.Space.isUniversallyPureAbove_iff_forall_baseChange_isPureAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean, line 576](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean#L576). The attribute's comment: “the equivalence left implicit by the source”.

> **Stacks 0CVE.** A finite type quasi-coherent module is universally pure above `y` exactly
> when, for every morphism `(Y', y') ⟶ (Y, y)` of pointed algebraic spaces, its base change
> `F_{Y'}` is pure above `y'`.
>
> The source lists the two conditions without the connective; they are equivalent, as the
> statement of the analogous Stacks 05J6 for schemes makes explicit. The consequence the source
> draws for purity relative to the whole base is
> `isUniversallyPureRelative_iff_forall_baseChange_isPureRelative`.
>
> Both directions are formal, as the source says: an impurity of a base change is an impurity of
> `F` by `isImpurity_alongBaseChange_iff`, and conversely an impurity diagram `(T, t' ⤳ t, ξ)` of
> `F` is an impurity of the base change along `(T, t) ⟶ (Y, y)` itself, whose structure morphism
> is the identity and hence quasi-finite at `t`.

```lean
theorem isUniversallyPureAbove_iff_forall_baseChange_isPureAbove
    (P : PrePureSituation.{u, u} B S hS) :
    IsUniversallyPureAbove P ↔ ∀ c : PointedOver P, IsPureAbove c.baseChange
```

**`AlgebraicGeometry.Space.isUniversallyPureRelative_iff_forall_baseChange_isPureRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean, line 677](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean#L677). The attribute's comment: “the 'in particular' clause: universally pure relative to Y iff every base change is pure relative to Y'”.

> **Stacks 0CVE, the closing clause.** The module is universally pure relative to `Y` exactly
> when, for every morphism `Y' ⟶ Y` of algebraic spaces, its base change `F_{Y'}` is pure
> relative to `Y'`.
>
> This is formal, as the source says, and is the pointwise equivalence
> `AlgebraicGeometry.Space.isUniversallyPureAbove_iff_forall_baseChange_isPureAbove` read at every
> point of the base at once: a pointed morphism `(Y', y') ⟶ (Y, y)` is a morphism `Y' ⟶ Y`
> together with a point `y'` of `Y'` whose image is `y`, and the two sides quantify over all `y`
> and all such `y'` in the two possible orders.

```lean
theorem isUniversallyPureRelative_iff_forall_baseChange_isPureRelative
    (P : PrePureSituation.{u, u} B S hS) :
    IsUniversallyPureRelative P ↔
      ∀ (Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hY' : IsAlgebraicSpace B S hS Y')
        (g : Y' ⟶ P.Y), P.IsPureRelativeAlong hY' g
```

## Tag 0CVF, a lemma

[Tag 0CVF](https://stacks.math.columbia.edu/tag/0CVF) in the Stacks Project.

**`AlgebraicGeometry.Space.isPureAbove_baseChange_of_isQuasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean, line 595](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean#L595).

> **Stacks 0CVF.** If `(Y', y') ⟶ (Y, y)` is a morphism of pointed algebraic spaces with
> `Y' ⟶ Y` quasi-finite at `y'`, and the module is pure above `y`, then its base change `F_{Y'}`
> is pure above `y'`.
>
> An impurity of `F_{Y'}` above `y'` whose structure morphism is quasi-finite at `t` is an
> impurity of `F` above `y` whose structure morphism is quasi-finite at `t`, by
> `isQuasiFiniteAt_comp`, the pointwise form of Stacks 03XK that the source appeals to.
>
> Purity above `y` is written out in the hypothesis rather than named: the condition stated there
> is `AlgebraicGeometry.Space.IsPureAbove` of Stacks 0CVD part (1), definitionally and on the
> nose, so a consumer holding that predicate may pass it directly.

```lean
theorem isPureAbove_baseChange_of_isQuasiFiniteAt (P : PrePureSituation.{u, u} B S hS)
    (c : PointedOver P)
    (hqf : IsQuasiFiniteAt B S hS c.g c.y')
    (hP : ∀ D : ImpurityDiagram P, IsQuasiFiniteAt B S hS D.g D.t → ¬ D.IsImpurity) :
    IsPureAbove c.baseChange
```

## Tag 0CVG, a lemma

[Tag 0CVG](https://stacks.math.columbia.edu/tag/0CVG) in the Stacks Project.

**`AlgebraicGeometry.Space.isPureAbove_of_isFlatAt`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/ImpurityFlatAscent.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/ImpurityFlatAscent.lean#L206). The attribute's comment: “part (1)”.

> **Stacks 0CVG, part (1).** In the situation of Stacks 0CV6, let `(Y₁, y₁) ⟶ (Y, y)` be a
> morphism of pointed algebraic spaces with `Y₁ ⟶ Y` flat at `y₁`. If the base change `F_{Y₁}`
> is pure above `y₁`, then `F` is pure above `y`. This is
> `AlgebraicGeometry.Space.isPureAbove_of_isPureAbove_baseChange_of_isFlatAt`.

```lean
alias isPureAbove_of_isFlatAt
```

**`AlgebraicGeometry.Space.isUniversallyPureAbove_of_isFlatAt`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/ImpurityFlatAscent.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/ImpurityFlatAscent.lean#L214). The attribute's comment: “part (2)”.

> **Stacks 0CVG, part (2).** In the situation of Stacks 0CV6, let `(Y₁, y₁) ⟶ (Y, y)` be a
> morphism of pointed algebraic spaces with `Y₁ ⟶ Y` flat at `y₁`. If the base change `F_{Y₁}`
> is universally pure above `y₁`, then `F` is universally pure above `y`. This is
> `AlgebraicGeometry.Space.isUniversallyPureAbove_of_isUniversallyPureAbove_baseChange_of_isFlatAt`.

```lean
alias isUniversallyPureAbove_of_isFlatAt
```

**`AlgebraicGeometry.Space.isPureAbove_of_isPureAbove_baseChange_of_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityFlatDescent.lean, line 547](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityFlatDescent.lean#L547). The attribute's comment: “part (1)”.

> **Stacks 0CVG, part (1).** If `(Y₁, y₁) ⟶ (Y, y)` is a morphism of pointed algebraic
> spaces with `Y₁ ⟶ Y` flat at `y₁` and the base change `F_{Y₁}` is pure above `y₁`, then `F` is
> pure above `y`.

```lean
theorem isPureAbove_of_isPureAbove_baseChange_of_isFlatAt (P : PrePureSituation.{u, u} B S hS)
    (c : PointedOver P) (hflat : IsFlatAt B S hS c.g c.y')
    (hpure : IsPureAbove c.baseChange) :
    IsPureAbove P
```

## Tag 0CVH, a lemma

[Tag 0CVH](https://stacks.math.columbia.edu/tag/0CVH) in the Stacks Project.

**`AlgebraicGeometry.Space.ClosedSubspaceModule.isPureAbove_situation_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityClosedImmersion.lean, line 540](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityClosedImmersion.lean#L540). The attribute's comment: “pure above y, granting as hin affine base change (Stacks 02KG) on the base changes of the situation”.

> **Stacks 0CVH, purity above `y`.** In the situation of Stacks 0CV6, let `i : Z ⟶ X` be a
> closed immersion and suppose `ℱ = i_*𝒢` for a finite type quasi-coherent `𝒪_Z`-module `𝒢`.
> Then `𝒢` is pure above `y` exactly when `ℱ` is.
>
> An impurity of `𝒢` above `y` whose structure morphism is quasi-finite at `t` is such an impurity
> of `ℱ` above `y`, and conversely; this is Stacks 0CV4 on the base changes, together with the
> fact that `Z_T ⟶ X_T` is a closed embedding on points.
>
> The inputs of `AlgebraicGeometry.Space.ClosedSubspaceModule.BaseChangeInput` — affine base
> change on the base changes — are hypotheses.

```lean
theorem isPureAbove_situation_iff
    (hin : c.BaseChangeInput) :
    IsPureAbove c.situation ↔ IsPureAbove P
```

**`AlgebraicGeometry.Space.ClosedSubspaceModule.isUniversallyPureAbove_situation_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityClosedImmersion.lean, line 563](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityClosedImmersion.lean#L563). The attribute's comment: “universally pure above y, granting as hin affine base change (Stacks 02KG) on the base changes of the situation”.

> **Stacks 0CVH, universal purity above `y`.** In the situation of Stacks 0CV6, let
> `i : Z ⟶ X` be a closed immersion and suppose `ℱ = i_*𝒢` for a finite type quasi-coherent
> `𝒪_Z`-module `𝒢`. Then `𝒢` is universally pure above `y` exactly when `ℱ` is.
>
> An impurity of `𝒢` above `y` is an impurity of `ℱ` above `y`, and conversely.
>
> The inputs of `AlgebraicGeometry.Space.ClosedSubspaceModule.BaseChangeInput` — affine base
> change on the base changes — are hypotheses.

```lean
theorem isUniversallyPureAbove_situation_iff
    (hin : c.BaseChangeInput) :
    IsUniversallyPureAbove c.situation ↔ IsUniversallyPureAbove P
```

**`AlgebraicGeometry.Space.ClosedSubspaceModule.isPureAbove_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityClosedImmersionBaseChange.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityClosedImmersionBaseChange.lean#L70). The attribute's comment: “pure above y”.

> **Stacks 0CVH, purity above `y`.** In the situation of Stacks 0CV6, let `i : Z ⟶ X` be a
> closed immersion and suppose `ℱ = i_*𝒢` for a finite type quasi-coherent `𝒪_Z`-module `𝒢`.
> Then `𝒢` is pure above `y` if and only if `ℱ` is pure above `y`.

```lean
theorem isPureAbove_iff : IsPureAbove c.situation ↔ IsPureAbove P
```

**`AlgebraicGeometry.Space.ClosedSubspaceModule.isUniversallyPureAbove_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityClosedImmersionBaseChange.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityClosedImmersionBaseChange.lean#L78). The attribute's comment: “universally pure above y”.

> **Stacks 0CVH, universal purity above `y`.** In the situation of Stacks 0CV6, let
> `i : Z ⟶ X` be a closed immersion and suppose `ℱ = i_*𝒢` for a finite type quasi-coherent
> `𝒪_Z`-module `𝒢`.  Then `𝒢` is universally pure above `y` if and only if `ℱ` is universally
> pure above `y`.

```lean
theorem isUniversallyPureAbove_iff :
    IsUniversallyPureAbove c.situation ↔ IsUniversallyPureAbove P
```

## Tag 0CVI, a lemma

[Tag 0CVI](https://stacks.math.columbia.edu/tag/0CVI) in the Stacks Project.

**`AlgebraicGeometry.Space.isUniversallyPureAbove_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProper.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProper.lean#L171). The attribute's comment: “part (2): a finite type quasi-coherent module on the source of a proper morphism is universally pure above every point of the target”.

> **Stacks 0CVI, part (2).** In the situation of Stacks 0CV6, if `f : X ⟶ Y` is proper then
> the module `ℱ` is universally pure above `y`.
>
> A proper morphism is universally closed, and a universally closed morphism admits no impurity
> diagram. Since the point `y` of the situation is arbitrary, this is purity of `ℱ` relative
> to `Y`.

```lean
theorem isUniversallyPureAbove_of_isProper (P : PrePureSituation.{u, u} B S hS)
    (hf : IsProper B S hS P.f) : IsUniversallyPureAbove P
```

**`AlgebraicGeometry.Space.ClosedSubspaceModule.isUniversallyPureAbove_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProper.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProper.lean#L190). The attribute's comment: “part (1) in general form, taking the closed-immersion presentation of the module as data”.

> **Stacks 0CVI, part (1), in general form.** In the situation of Stacks 0CV6, let
> `i : Z ⟶ X` be a closed immersion and suppose `ℱ = i_*𝒢` for a finite type quasi-coherent
> `𝒪_Z`-module `𝒢`. If the composite `Z ⟶ Y` is proper, then `ℱ` is universally pure above `y`.
>
> This is part (2) applied to the situation on `Z`, transferred to `ℱ` by Stacks 0CVH. The
> source states the hypothesis as properness of the support of `ℱ` over `Y` and then reduces to
> part (2) exactly this way, at the scheme-theoretic support; see
> `AlgebraicGeometry.Space.isUniversallyPureAbove_of_isProper_schemeTheoreticSupport`.
>
> The input of Stacks 0CVH, affine base change on the base changes of the situation, is
> `AlgebraicGeometry.Space.ClosedSubspaceModule.baseChangeInput`.

```lean
theorem ClosedSubspaceModule.isUniversallyPureAbove_of_isProper
    {P : PrePureSituation.{u, u} B S hS} (c : ClosedSubspaceModule P)
    (hZY : IsProper B S hS (c.i.hom ≫ P.f)) :
    IsUniversallyPureAbove P
```

**`AlgebraicGeometry.Space.isUniversallyPureAbove_of_isProper_schemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProper.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProper.lean#L238). The attribute's comment: “part (1) at the scheme-theoretic support, naming the support's closed-subspace data”.

> **Stacks 0CVI, part (1).** In the situation of Stacks 0CV6, if the scheme-theoretic
> support of `ℱ` is proper over `Y`, then `ℱ` is universally pure above `y`.
>
> This is the general form above at the closed-immersion presentation of `ℱ` furnished by its
> scheme-theoretic support, Stacks 07U1, and the module on it of Stacks 07U0.
>
> The two arguments `hZ` and `hid` are not assumptions about the geometry but the closed-subspace
> data of the scheme-theoretic support, which
> `AlgebraicGeometry.Space.exists_isClosedSubspace_schemeTheoreticSupport` produces from
> quasi-coherence of the module together with its finite type in the sectionwise sense of
> Stacks 03DL(5); they are taken as arguments because every other hypothesis here, the
> properness assumption included, is stated about the closed subspace they exhibit.

```lean
theorem isUniversallyPureAbove_of_isProper_schemeTheoreticSupport
    (P : PrePureSituation.{u, u} B S hS)
    (hZ : IsClosedSubspace B S hS (schemeTheoreticSupport B S hS P.sourceSpace P.F))
    (hid : definingIdealSheaf B S hS P.sourceSpace
        ⟨schemeTheoreticSupport B S hS P.sourceSpace P.F, hZ⟩ =
      annihilatorIdealSheaf B S hS P.sourceSpace P.F)
    (hZY : IsProper B S hS ((closedSubspaceInclusion B S hS P.sourceSpace
      ⟨schemeTheoreticSupport B S hS P.sourceSpace P.F, hZ⟩).hom ≫ P.f)) :
    IsUniversallyPureAbove P
```

**`AlgebraicGeometry.Space.isUniversallyPureAbove_structure_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProper.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProper.lean#L319). The attribute's comment: “part (3): the source of a proper decent morphism is universally pure above every point of the target”.

> **Stacks 0CVI, part (3).** If `f : X ⟶ Y` is a proper decent morphism of algebraic spaces
> over `S`, then `X` is universally pure above every point of `Y`, that is, universally pure
> relative to `Y`.
>
> This is part (2) for the situation whose module is the structure sheaf of `X`.

```lean
theorem isUniversallyPureAbove_structure_of_isProper
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hdec : IsDecent B S hS f) (hf : IsProper B S hS f) (y : points B S hS Y) :
    IsUniversallyPureAbove
      (structurePrePureSituation hX hY f (IsProper.isFiniteType B S hS hf) hdec y)
```

**`AlgebraicGeometry.Space.ClosedSubspaceModule.isUniversallyPureAbove_of_isProper_comp`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProperSupport.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProperSupport.lean#L72). The attribute's comment: “part (1), for any presentation of the module as the direct image along a closed immersion whose composite to the target is proper”.

> **Stacks 0CVI, part (1), for a closed-immersion presentation of the module.** In the
> situation of Stacks 0CV6, let `i : Z ⟶ X` be a closed immersion and suppose `ℱ = i_*𝒢` for a
> finite type quasi-coherent `𝒪_Z`-module `𝒢`. If the composite `Z ⟶ Y` is proper, then `ℱ` is
> universally pure above `y`.
>
> This is part (2) applied to the situation on `Z`, transferred to `ℱ` by Stacks 0CVH; it is
> `AlgebraicGeometry.Space.ClosedSubspaceModule.isUniversallyPureAbove_of_isProper`.

```lean
alias ClosedSubspaceModule.isUniversallyPureAbove_of_isProper_comp
```

**`AlgebraicGeometry.Space.isUniversallyPureAbove_of_isProper_supportSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProperSupport.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityProperSupport.lean#L105). The attribute's comment: “part (1): a finite type quasi-coherent module whose scheme-theoretic support is proper over the target is universally pure above every point of the target”.

> **Stacks 0CVI, part (1).** In the situation of Stacks 0CV6, if the support of `ℱ` is proper
> over `Y`, then `ℱ` is universally pure above `y`; the point `y` being arbitrary, `ℱ` is
> universally pure relative to `Y`.
>
> The support is the scheme-theoretic support `Z` of Stacks 07U1, and properness over `Y` is
> properness of the composite `Z ⟶ X ⟶ Y`. The proof is the source's: by Stacks 07U0 the module
> is `i_*𝒢` for a finite type quasi-coherent `𝒪_Z`-module `𝒢`, and the closed-immersion form
> above applies.

```lean
theorem isUniversallyPureAbove_of_isProper_supportSubspace
    (P : PrePureSituation.{u, u} B S hS)
    (hZY : IsProper B S hS
      ((closedSubspaceInclusion B S hS P.sourceSpace P.supportSubspace).hom ≫ P.f)) :
    IsUniversallyPureAbove P
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 77.3, Tag 0CVC](https://stacks.math.columbia.edu/tag/0CVC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
