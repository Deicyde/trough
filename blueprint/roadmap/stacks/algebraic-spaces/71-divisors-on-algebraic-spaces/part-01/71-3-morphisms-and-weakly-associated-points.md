---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.weaklyAssociatedPoints_modulePushforward_subset_image_of_isAffineHom, AlgebraicGeometry.Space.affinePushforwardWeaklyAssociatedImage, AlgebraicGeometry.Space.weaklyAssociatedPoints_modulePushforward_eq_image_of_isAffineHom_locallyNoetherian, AlgebraicGeometry.Space.weaklyAssociatedPoints_modulePushforward_eq_image_of_isFinite, AlgebraicGeometry.Space.isWeaklyAssociatedPoint_modulePullback_of_hasFiberLocalRingDimension, AlgebraicGeometry.Space.isWeaklyAssociatedPoint_fibre_of_refines, AlgebraicGeometry.Space.isWeaklyAssociatedPoint_of_fieldBaseChange, AlgebraicGeometry.Space.isWeaklyAssociatedPoint_modulePullback_iff_of_isFinite_of_isFlat
statement: formalized
proof: formalized
---

# 71.3 Morphisms and weakly associated points

Section 71.3 of the Stacks Project, [Tag 0CU1](https://stacks.math.columbia.edu/tag/0CU1). 7 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CU2, a lemma

[Tag 0CU2](https://stacks.math.columbia.edu/tag/0CU2) in the Stacks Project.

**`AlgebraicGeometry.Space.weaklyAssociatedPoints_modulePushforward_subset_image_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceAffineDirectImage.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceAffineDirectImage.lean#L148).

> Let `f : X ⟶ Y` be an affine morphism of algebraic spaces over `S` and let `F` be a
> quasi-coherent `𝒪_X`-module. Then every weakly associated point of `f_*F` is the image of a
> weakly associated point of `F`.

```lean
theorem weaklyAssociatedPoints_modulePushforward_subset_image_of_isAffineHom
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsAffineHom B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite) :
    weaklyAssociatedPoints B S hS Y ((modulePushforward B S hS f).obj F) ⊆
      pointsMap B S hS X.1 f.hom '' weaklyAssociatedPoints B S hS X F
```

**`AlgebraicGeometry.Space.affinePushforwardWeaklyAssociatedImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceAffinePushforward.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceAffinePushforward.lean#L62). The attribute's comment: “the reduction to a target represented by an affine scheme of the site, which is the hypothesis h; that case needs the comparison of the Zariski and small-étale modules of a represented algebraic space, absent here”.

> Let `f : X ⟶ Y` be an affine morphism of algebraic spaces over `S` and let `F` be a
> quasi-coherent `𝒪_X`-module. Granted the hypothesis `h`, the same inclusion for a target
> represented by an affine scheme of the site, every weakly associated point of `f_*F` is the
> image of a weakly associated point of `F`.

```lean
theorem affinePushforwardWeaklyAssociatedImage
    (h : SchemeTargetAffinePushforwardWeaklyAssociatedImage B S hS) :
    AffinePushforwardWeaklyAssociatedImage B S hS
```

## Tag 0CU8, a lemma

[Tag 0CU8](https://stacks.math.columbia.edu/tag/0CU8) in the Stacks Project.

**`AlgebraicGeometry.Space.weaklyAssociatedPoints_modulePushforward_eq_image_of_isAffineHom_locallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceAffineDirectImageLocallyNoetherian.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceAffineDirectImageLocallyNoetherian.lean#L59). The attribute's comment: “WeakAss(f\_*F) = f(WeakAss F) for f affine, X locally Noetherian, F quasi-coherent”.

> Let `f : X ⟶ Y` be an affine morphism of algebraic spaces over `S` and let `F` be a
> quasi-coherent `𝒪_X`-module. If `X` is locally Noetherian, then the weakly associated points of
> `f_*F` are exactly the images of the weakly associated points of `F`.

```lean
theorem weaklyAssociatedPoints_modulePushforward_eq_image_of_isAffineHom_locallyNoetherian
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsAffineHom B S hS f.hom)
    (hX : HasEtaleLocalProperty B S hS X.1
      (fun T : Scheme.{u} => _root_.AlgebraicGeometry.IsLocallyNoetherian T))
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite) :
    weaklyAssociatedPoints B S hS Y ((modulePushforward B S hS f).obj F) =
      pointsMap B S hS X.1 f.hom '' weaklyAssociatedPoints B S hS X F
```

## Tag 0CU9, a lemma

[Tag 0CU9](https://stacks.math.columbia.edu/tag/0CU9) in the Stacks Project.

**`AlgebraicGeometry.Space.weaklyAssociatedPoints_modulePushforward_eq_image_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceFiniteDirectImage.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceFiniteDirectImage.lean#L165).

> **Weakly associated points of a finite direct image.** Let `f : X ⟶ Y` be a finite morphism
> of algebraic spaces over a scheme `S` and let `F` be a quasi-coherent `𝒪_X`-module. Then
> `WeakAss(f_*F) = f(WeakAss(F))`.

```lean
theorem weaklyAssociatedPoints_modulePushforward_eq_image_of_isFinite
    {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsFinite B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) :
    weaklyAssociatedPoints B S hS Y ((modulePushforward B S hS f).obj F) =
      pointsMap B S hS X.1 f.hom '' weaklyAssociatedPoints B S hS X F
```

## Tag 0CUA, a lemma

[Tag 0CUA](https://stacks.math.columbia.edu/tag/0CUA) in the Stacks Project.

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_modulePullback_of_hasFiberLocalRingDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpacePullbackFibreDimension.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpacePullbackFibreDimension.lean#L159). The attribute's comment: “for an arbitrary 𝒪\_Y-module G; the source takes G quasi-coherent”.

> **Stacks 0CUA.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S`, let
> `G` be an `𝒪_Y`-module and let `x ∈ |X|` with image `y = f(x) ∈ |Y|`. If `y` is weakly
> associated to `G`, `f` is flat at `x`, and the local ring of the fibre of `f` at `x` has
> dimension zero (Stacks 04NM), then `x` is weakly associated to `f^*G`.

```lean
theorem isWeaklyAssociatedPoint_modulePullback_of_hasFiberLocalRingDimension (f : X ⟶ Y)
    (G : Modules.{u, u} B S hS Y.1 Y.2) (x : points B S hS X.1)
    (hG : IsWeaklyAssociatedPoint B S hS Y G (pointsMap B S hS X.1 f.hom x))
    (hflat : IsFlatAt B S hS f.hom x)
    (hdim : HasFiberLocalRingDimension 0 B S hS X.2 Y.2 f.hom x) :
    IsWeaklyAssociatedPoint B S hS X ((modulePullback B S hS f).obj G) x
```

## Tag 0CUS, a lemma

[Tag 0CUS](https://stacks.math.columbia.edu/tag/0CUS) in the Stacks Project.

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_fibre_of_refines`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceFibreEtaleRefinement.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceFibreEtaleRefinement.lean#L163). The attribute's comment: “at a refinement of field-valued points of the target, read on the comparison of the two fibres”.

> **Weak association descends along a refinement of field-valued points.** Let `f : X ⟶ Y`
> be a morphism of algebraic spaces over `S`, let `F` be a quasi-coherent `𝒪_X`-module, let `q`
> refine `p` as a field-valued point of `Y` through `κ : q.siteObject ⟶ p.siteObject`, and let `π`
> be the comparison morphism of the fibre of `f` over `q` with the fibre of `f` over `p`,
> compatible with the projections to `X` and presenting the one fibre as the base change of the
> other along `κ`. If a point of the fibre over `q` is weakly associated to the restriction of `F`
> there, then its image in the fibre over `p` is weakly associated to the restriction of `F`
> there.

```lean
theorem isWeaklyAssociatedPoint_fibre_of_refines (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    {p q : FieldValuedPoint B S hS Y.1} (κ : q.siteObject ⟶ p.siteObject)
    {π : fibreAtFieldValuedPoint B S hS f q ⟶ fibreAtFieldValuedPoint B S hS f p}
    (hπ : π ≫ fibreAtFieldValuedPointProjection B S hS f p =
      fibreAtFieldValuedPointProjection B S hS f q)
    (sq : IsPullback π.hom (pullback.snd f.hom (fieldMorphism B S hS Y.1 q))
      (pullback.snd f.hom (fieldMorphism B S hS Y.1 p)) (yoneda.map κ))
    {ζ : points B S hS (fibreAtFieldValuedPoint B S hS f q).1}
    (h : IsWeaklyAssociatedPoint B S hS (fibreAtFieldValuedPoint B S hS f q)
      ((modulePullback B S hS (fibreAtFieldValuedPointProjection B S hS f q)).obj F) ζ) :
    IsWeaklyAssociatedPoint B S hS (fibreAtFieldValuedPoint B S hS f p)
      ((modulePullback B S hS (fibreAtFieldValuedPointProjection B S hS f p)).obj F)
      (pointsMap B S hS (fibreAtFieldValuedPoint B S hS f q).1 π.hom ζ)
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_of_fieldBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceFieldBaseChange.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceFieldBaseChange.lean#L62).

> **Weak association descends along a field extension.** Let `K/k` be a field extension,
> presented by objects `Tk` and `Tk'` of the site with underlying schemes `Spec k` and `Spec K` and
> a morphism `gk : Tk' ⟶ Tk` inducing `Spec K → Spec k`. Let `X` be an algebraic space over
> `Y = h_{Tk}`, let `X' = X ×_Y Y'` be its base change along `g : Y' ⟶ Y` for `Y' = h_{Tk'}`, and
> let `F` be a quasi-coherent `𝒪_X`-module. If a point `y` of `X'` is weakly associated to the
> pullback of `F`, then its image in `X` is weakly associated to `F`.

```lean
theorem isWeaklyAssociatedPoint_of_fieldBaseChange (k K : Type u) [Field k] [Field K]
    [Algebra k K] (Tk Tk' : BigFppfOver B S hS) (gk : Tk' ⟶ Tk)
    (f : X ⟶ Y) (f' : X' ⟶ Y') (g : Y' ⟶ Y) (π : X' ⟶ X) (sq : IsPullback π f' f g)
    (ek : (BigFppfOver.toScheme B S hS).obj Tk ≅ Spec (CommRingCat.of k))
    (eK : (BigFppfOver.toScheme B S hS).obj Tk' ≅ Spec (CommRingCat.of K))
    (hgk : (BigFppfOver.toScheme B S hS).map gk =
      eK.hom ≫ Spec.map (CommRingCat.ofHom (algebraMap k K)) ≫ ek.inv)
    (eY : Y.1 ≅ yoneda.obj Tk) (eY' : Y'.1 ≅ yoneda.obj Tk')
    (hg : g.hom ≫ eY.hom = eY'.hom ≫ yoneda.map gk)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (y : points B S hS X'.1)
    (hy : IsWeaklyAssociatedPoint B S hS X' ((modulePullback B S hS π).obj F) y) :
    IsWeaklyAssociatedPoint B S hS X F (pointsMap B S hS X'.1 π.hom y)
```

## Tag 0CUT, a lemma

[Tag 0CUT](https://stacks.math.columbia.edu/tag/0CUT) in the Stacks Project.

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_modulePullback_iff_of_isFinite_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceFiniteFlatPullback.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceFiniteFlatPullback.lean#L60).

> **Stacks 0CUT.** Let `f : X ⟶ Y` be a finite flat morphism of algebraic spaces over a
> scheme `S`, let `G` be an `𝒪_Y`-module and let `x ∈ |X|` be a point with image `y ∈ |Y|`.
> Then `x ∈ WeakAss(f^*G)` if and only if `y ∈ WeakAss(G)`.
>
> The source takes `G` quasi-coherent; that hypothesis is not needed.

```lean
theorem isWeaklyAssociatedPoint_modulePullback_iff_of_isFinite_of_isFlat (f : X ⟶ Y)
    (hfinite : IsFinite B S hS f.hom) (hflat : IsFlat B S hS f.hom)
    (G : Modules.{u, u} B S hS Y.1 Y.2) (x : points B S hS X.1) :
    IsWeaklyAssociatedPoint B S hS X ((modulePullback B S hS f).obj G) x ↔
      IsWeaklyAssociatedPoint B S hS Y G (pointsMap B S hS X.1 f.hom x)
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPrime_geometricModuleStalk_modulePullback_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpacePullback.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpacePullback.lean#L275). The attribute's comment: “at the étale local ring, for the geometric stalk of the pullback module”.

> **Stacks 0CUT** at the étale local ring, for the geometric stalk of the pullback module.
> Let `f : X ⟶ Y` be a finite flat morphism of algebraic spaces and let `x̄` be a geometric point
> of `X` with image `ȳ`. Then the maximal ideal of `𝒪_{Y, ȳ}` is weakly associated to the
> geometric stalk `G_{ȳ}` exactly when the maximal ideal of `𝒪_{X, x̄}` is weakly associated to
> the geometric stalk `(f^*G)_{x̄}` of the pullback module.

```lean
theorem isWeaklyAssociatedPrime_geometricModuleStalk_modulePullback_iff (f : X ⟶ Y)
    (hfinite : IsFinite B S hS f.hom) (hflat : IsFlat B S hS f.hom)
    (xbar : GeometricPoint B S hS X.1)
    (G : Modules.{u, u} B S hS Y.1 Y.2) :
    letI : IsLocalRing (etaleLocalRing B S hS Y.1 (geometricPointMap f.hom xbar)) :=
      isLocalRing_etaleLocalRing B S hS Y.1 Y.2 (geometricPointMap f.hom xbar)
    letI : IsLocalRing (etaleLocalRing B S hS X.1 xbar) :=
      isLocalRing_etaleLocalRing B S hS X.1 X.2 xbar
    letI : Module (etaleLocalRing B S hS Y.1 (geometricPointMap f.hom xbar))
        (geometricModuleStalk B S hS Y (geometricPointMap f.hom xbar) G) :=
      (geometricModuleStalk B S hS Y (geometricPointMap f.hom xbar) G).isModule
    letI : Module (etaleLocalRing B S hS X.1 xbar)
        (geometricModuleStalk B S hS X xbar ((modulePullback B S hS f).obj G)) :=
      (geometricModuleStalk B S hS X xbar ((modulePullback B S hS f).obj G)).isModule
    (IsWeaklyAssociatedPrime (etaleLocalRing B S hS Y.1 (geometricPointMap f.hom xbar))
          (geometricModuleStalk B S hS Y (geometricPointMap f.hom xbar) G)
          (maximalIdeal (etaleLocalRing B S hS Y.1 (geometricPointMap f.hom xbar))) ↔
      IsWeaklyAssociatedPrime (etaleLocalRing B S hS X.1 xbar)
        (geometricModuleStalk B S hS X xbar ((modulePullback B S hS f).obj G))
        (maximalIdeal (etaleLocalRing B S hS X.1 xbar)))
```

## Tag 0CUU, a lemma

[Tag 0CUU](https://stacks.math.columbia.edu/tag/0CUU) in the Stacks Project.

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_modulePullback_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceEtalePullback.lean, line 551](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceEtalePullback.lean#L551).

> **Weak association along an étale pullback.** Let `f : X ⟶ Y` be an étale morphism of
> algebraic spaces over a scheme `S`, let `G` be an `𝒪_Y`-module and let `x` be a point of `X` with
> image `y`. Then `x` is weakly associated to `f^*G` if and only if `y` is weakly associated to
> `G`.

```lean
theorem isWeaklyAssociatedPoint_modulePullback_iff (f : X ⟶ Y) (hf : IsEtale B S hS f.hom)
    (G : Modules.{u, u} B S hS Y.1 Y.2) (x : points B S hS X.1) :
    IsWeaklyAssociatedPoint B S hS X ((modulePullback B S hS f).obj G) x ↔
      IsWeaklyAssociatedPoint B S hS Y G (pointsMap B S hS X.1 f.hom x)
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_fibre_refines_iff_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceFibreEtaleRefinement.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceFibreEtaleRefinement.lean#L206). The attribute's comment: “at an etale refinement of field-valued points of the target, read on the comparison of the two fibres”.

> **Weak association transfers along an étale refinement of field-valued points.** In the
> situation of `AlgebraicGeometry.Space.isWeaklyAssociatedPoint_fibre_of_refines`, with `F` an
> arbitrary `𝒪_X`-module, if the morphism of field spectra the refinement presents is étale, then a
> point of the fibre over `q` is weakly associated to the restriction of `F` exactly when its image
> in the fibre over `p` is.

```lean
theorem isWeaklyAssociatedPoint_fibre_refines_iff_of_isEtale (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X.1 X.2)
    {p q : FieldValuedPoint B S hS Y.1} (κ : q.siteObject ⟶ p.siteObject)
    (hκ : IsEtale B S hS (yoneda.map κ))
    {π : fibreAtFieldValuedPoint B S hS f q ⟶ fibreAtFieldValuedPoint B S hS f p}
    (hπ : π ≫ fibreAtFieldValuedPointProjection B S hS f p =
      fibreAtFieldValuedPointProjection B S hS f q)
    (sq : IsPullback π.hom (pullback.snd f.hom (fieldMorphism B S hS Y.1 q))
      (pullback.snd f.hom (fieldMorphism B S hS Y.1 p)) (yoneda.map κ))
    (ζ : points B S hS (fibreAtFieldValuedPoint B S hS f q).1) :
    IsWeaklyAssociatedPoint B S hS (fibreAtFieldValuedPoint B S hS f q)
        ((modulePullback B S hS (fibreAtFieldValuedPointProjection B S hS f q)).obj F) ζ ↔
      IsWeaklyAssociatedPoint B S hS (fibreAtFieldValuedPoint B S hS f p)
        ((modulePullback B S hS (fibreAtFieldValuedPointProjection B S hS f p)).obj F)
        (pointsMap B S hS (fibreAtFieldValuedPoint B S hS f q).1 π.hom ζ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.3, Tag 0CU1](https://stacks.math.columbia.edu/tag/0CU1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
