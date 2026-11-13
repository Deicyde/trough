---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor, AlgebraicGeometry.Space.range_le_schemeTheoreticImageSubfunctor, AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_le, AlgebraicGeometry.Space.isClosedSubspace_schemeTheoreticImageSubfunctor, AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_pullback_snd_of_isEtale_of_isQuasiCompact, AlgebraicGeometry.Space.definingIdealSheaf_schemeTheoreticImage_eq_kernelIdealSheaf, AlgebraicGeometry.Space.range_pointsMap_ι_schemeTheoreticImage_eq_closure_of_isQuasiCompact, AlgebraicGeometry.Space.denseRange_pointsMap_toSchemeTheoreticImage_of_isQuasiCompact
statement: formalized
proof: formalized
---

# 67.16 Scheme theoretic image

Section 67.16 of the Stacks Project, [Tag 082W](https://stacks.math.columbia.edu/tag/082W). 7 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 082X, a lemma

[Tag 082X](https://stacks.math.columbia.edu/tag/082X) in the Stacks Project.

**`AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean#L155). The attribute's comment: “underlying subfunctor construction”.

> **Stacks 082X.** The scheme-theoretic image of a morphism of algebraic spaces over `S`:
> the intersection of all closed subspaces of the target containing the image of the
> morphism.

```lean
def schemeTheoreticImageSubfunctor (f : X ⟶ Y) : Subfunctor Y
```

**`AlgebraicGeometry.Space.range_le_schemeTheoreticImageSubfunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean#L161). The attribute's comment: “the morphism factors through the image”.

> **Stacks 082X.** A morphism of algebraic spaces over `S` factors through its
> scheme-theoretic image.

```lean
theorem range_le_schemeTheoreticImageSubfunctor (f : X ⟶ Y) :
    Subfunctor.range f ≤ schemeTheoreticImageSubfunctor B S hS f
```

**`AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean#L168). The attribute's comment: “minimality of the image”.

> **Stacks 082X.** The scheme-theoretic image is contained in every closed subspace of the
> target through which the morphism factors.

```lean
theorem schemeTheoreticImageSubfunctor_le (f : X ⟶ Y) {Z : Subfunctor Y}
    (hZ : IsClosedSubspace B S hS Z) (hfZ : Subfunctor.range f ≤ Z) :
    schemeTheoreticImageSubfunctor B S hS f ≤ Z
```

**`AlgebraicGeometry.Space.isClosedSubspace_schemeTheoreticImageSubfunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean#L175). The attribute's comment: “the image is a closed subspace”.

> **Stacks 082X.** The scheme-theoretic image is a closed subspace of the target.

```lean
theorem isClosedSubspace_schemeTheoreticImageSubfunctor (f : X ⟶ Y)
    (hY : IsAlgebraicSpace B S hS Y) :
    IsClosedSubspace B S hS (schemeTheoreticImageSubfunctor B S hS f)
```

## Tag 082Y, a definition

[Tag 082Y](https://stacks.math.columbia.edu/tag/082Y) in the Stacks Project.

**`AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean#L155). The attribute's comment: “the scheme-theoretic image”.

> **Stacks 082X.** The scheme-theoretic image of a morphism of algebraic spaces over `S`:
> the intersection of all closed subspaces of the target containing the image of the
> morphism.

```lean
def schemeTheoreticImageSubfunctor (f : X ⟶ Y) : Subfunctor Y
```

## Tag 082Z, a lemma

[Tag 082Z](https://stacks.math.columbia.edu/tag/082Z) in the Stacks Project.

**`AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_pullback_snd_of_isEtale_of_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactImageEtaleLocal.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactImageEtaleLocal.lean#L96). The attribute's comment: “part (3): compatibility with étale localization of the target”.

> **Stacks 082Z, part (3).** The scheme-theoretic image of a *quasi-compact* morphism
> `f : X ⟶ Y` of algebraic spaces over `S` commutes with étale base change of the target: for
> `g : V ⟶ Y` étale, the scheme-theoretic image of `X ×_Y V ⟶ V` is the inverse image along `g` of
> the scheme-theoretic image of `f`.
>
> Both sides are closed subspaces of `V`, hence are determined by their defining ideal sheaves,
> and on an étale scheme chart `W` of `V` both of those ideals are the kernel ideal of `f` on the
> chart `g ∘ W` of `Y` — by Stacks 082Z for the base change of `f` and for `f` itself.

```lean
theorem schemeTheoreticImageSubfunctor_pullback_snd_of_isEtale_of_isQuasiCompact
    (f : X ⟶ Y) (g : V ⟶ Y) (hf : IsQuasiCompact B S hS f.hom)
    (hg : IsEtale B S hS g.hom) :
    schemeTheoreticImageSubfunctor B S hS (pullback.snd f.hom g.hom) =
      (schemeTheoreticImageSubfunctor B S hS f.hom).preimage g.hom
```

**`AlgebraicGeometry.Space.definingIdealSheaf_schemeTheoreticImage_eq_kernelIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactImageIdeal.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactImageIdeal.lean#L126). The attribute's comment: “part (2): the image is the closed subspace cut out by that ideal”.

> **Stacks 082Z.** For a quasi-compact morphism `f : X ⟶ Y` of algebraic spaces over `S` the
> scheme-theoretic image of `f` is the closed subspace of `Y` cut out by the kernel of the
> structure map `f♯ : 𝒪_Y ⟶ f_*𝒪_X`: its defining ideal sheaf of Stacks 03MB is that kernel.

```lean
theorem definingIdealSheaf_schemeTheoreticImage_eq_kernelIdealSheaf (f : X ⟶ Y)
    (hf : IsQuasiCompact B S hS f.hom) :
    definingIdealSheaf B S hS Y (schemeTheoreticImage B S hS f.hom Y.2) =
      kernelIdealSheaf B S hS f
```

**`AlgebraicGeometry.Space.range_pointsMap_ι_schemeTheoreticImage_eq_closure_of_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactSchemeTheoreticImageDense.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactSchemeTheoreticImageDense.lean#L54). The attribute's comment: “part (4): the image is dense in the scheme-theoretic image”.

> **Stacks 082Z, part (4).** The set of points of the scheme-theoretic image of a quasi-compact
> morphism of algebraic spaces is the closure of the image of its point map.

```lean
theorem range_pointsMap_ι_schemeTheoreticImage_eq_closure_of_isQuasiCompact (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsQuasiCompact B S hS f) :
    Set.range (pointsMap B S hS (schemeTheoreticImageSubfunctor B S hS f).toFunctor
        (schemeTheoreticImageSubfunctor B S hS f).ι) =
      closure (Set.range (pointsMap B S hS X f))
```

**`AlgebraicGeometry.Space.denseRange_pointsMap_toSchemeTheoreticImage_of_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactSchemeTheoreticImageDense.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactSchemeTheoreticImageDense.lean#L68). The attribute's comment: “part (4): density of the image on points”.

> **Stacks 082Z, part (4)**, read inside the scheme-theoretic image: a quasi-compact morphism of
> algebraic spaces has dense image on the points of its scheme-theoretic image.

```lean
theorem denseRange_pointsMap_toSchemeTheoreticImage_of_isQuasiCompact (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsQuasiCompact B S hS f) :
    DenseRange (pointsMap B S hS X (toSchemeTheoreticImage B S hS f))
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_kernelIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactKernelQuasicoherent.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactKernelQuasicoherent.lean#L84). The attribute's comment: “part (1): the ideal sheaf of the image is quasi-coherent”.

> **The kernel of the structure map of a quasi-compact morphism of algebraic spaces is a
> quasi-coherent sheaf of ideals.**

```lean
theorem isQuasicoherentOnSite_kernelIdealSheaf (f : X ⟶ Y)
    (hf : IsQuasiCompact B S hS f.hom) :
    (kernelIdealSheaf B S hS f).toSheafOfModules.IsQuasicoherentOnSite
```

## Tag 0830, a lemma

[Tag 0830](https://stacks.math.columbia.edu/tag/0830) in the Stacks Project.

**`AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_eq_reducedClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean#L370). The attribute's comment: “part (1): the image is the reduced induced structure on the closure”.

> **Stacks 0830, part (1).** The scheme-theoretic image of a morphism out of a reduced
> algebraic space is the reduced closed subspace supported on the closure of the image of its
> point map.
>
> The identification itself is
> `AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_eq_of_isReduced_of_range_pointsMap_eq`,
> which needs no descent; what it has to be fed is that
> `AlgebraicGeometry.Space.reducedClosedSubspace` is a closed subspace, the existence half of
> Stacks 03IQ. That comes from
> `AlgebraicGeometry.Space.isClosedSubspace_reducedClosedSubspace`
> together with
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isClosedImmersion`, effective
> descent for closed immersions along the surjective étale morphisms of the site.

```lean
theorem schemeTheoreticImageSubfunctor_eq_reducedClosedSubspace (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hXred : HasEtaleLocalProperty B S hS X (fun W : Scheme.{u} => IsReduced W)) :
    schemeTheoreticImageSubfunctor B S hS f =
      reducedClosedSubspace B S hS Y hY
        (closure (Set.range (pointsMap B S hS X f))) isClosed_closure
```

**`AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_pullback_snd_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean, line 407](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean#L407). The attribute's comment: “part (2): compatibility with étale base change of the target”.

> **Stacks 0830, part (2).** The scheme-theoretic image of a morphism out of a reduced
> algebraic space commutes with étale base change of the target: for an étale morphism
> `g : V ⟶ Y`, the scheme-theoretic image of `X ×_Y V ⟶ V` is the inverse image along `g` of the
> scheme-theoretic image of `f`.
>
> By part (1) both sides are reduced closed subspaces, so it is enough to identify their point
> sets and appeal to the uniqueness half of Stacks 03IQ,
> `AlgebraicGeometry.Space.eq_reducedClosedSubspace`. The inverse image along `g` of the reduced
> closed subspace on the closure of the image of `f` is a closed subspace by Stacks 083Q, is
> étale-locally reduced because its projection to that subspace is a base change of `g`, hence
> étale, and has point set the preimage along `|g|` of that closure. That preimage is the closure
> of the image of `X ×_Y V ⟶ V`, because `|g|` is open by Stacks 03IR and the image of
> `X ×_Y V ⟶ V` is the preimage along `|g|` of the image of `f` by Stacks 03H4.

```lean
theorem schemeTheoreticImageSubfunctor_pullback_snd_of_isEtale
    {V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) (g : V ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hV : IsAlgebraicSpace B S hS V)
    (hXred : HasEtaleLocalProperty B S hS X (fun W : Scheme.{u} => IsReduced W))
    (hg : IsEtale B S hS g) :
    schemeTheoreticImageSubfunctor B S hS (pullback.snd f g) =
      (schemeTheoreticImageSubfunctor B S hS f).preimage g
```

## Tag 089B, a lemma

[Tag 089B](https://stacks.math.columbia.edu/tag/089B) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_valuativeSquare_toSchemeTheoreticImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImageValuativePoint.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImageValuativePoint.lean#L189).

> Let `f : X ⟶ Y` be a quasi-compact morphism of algebraic spaces over `S`,
> let `Z` be its scheme-theoretic image and let `z` be a point of `|Z|`. There is a valuation
> ring `A` with fraction field `K`, a morphism `Spec K ⟶ X` and a morphism `Spec A ⟶ Z` making
> the square over the canonical morphism `X ⟶ Z` commute, such that the closed point of
> `Spec A` maps to `z`.

```lean
theorem exists_valuativeSquare_toSchemeTheoreticImage (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsQuasiCompact B S hS f)
    (z : points B S hS (schemeTheoreticImageSubfunctor B S hS f).toFunctor) :
    ∃ (q : ValuativeSquare (toSchemeTheoreticImage B S hS f))
      (w : points B S hS (yoneda.obj (siteObject B S hS q.ring_mem q.base))),
      pointsToScheme B S hS (siteObject B S hS q.ring_mem q.base) w = closedPoint q.R ∧
        pointsMap B S hS (yoneda.obj (siteObject B S hS q.ring_mem q.base)) q.special w = z
```

## Tag 0CP2, a lemma

[Tag 0CP2](https://stacks.math.columbia.edu/tag/0CP2) in the Stacks Project.

**`AlgebraicGeometry.Space.schemeTheoreticImageMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean#L235). The attribute's comment: “the induced morphism of scheme-theoretic images”.

> **Stacks 0CP2.** The morphism of scheme-theoretic images induced by a commutative square
> of algebraic spaces over `S`.

```lean
def schemeTheoreticImageMap (hY₁ : IsAlgebraicSpace B S hS Y₁)
    (hY₂ : IsAlgebraicSpace B S hS Y₂) (hsq : f₁ ≫ q = p ≫ f₂) :
    (schemeTheoreticImageSubfunctor B S hS f₁).toFunctor ⟶
      (schemeTheoreticImageSubfunctor B S hS f₂).toFunctor
```

**`AlgebraicGeometry.Space.schemeTheoreticImageMap_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean#L245). The attribute's comment: “the right square”.

> **Stacks 0CP2**, the right square: the induced morphism of scheme-theoretic images is
> compatible with their inclusions into the targets.

```lean
theorem schemeTheoreticImageMap_ι (hY₁ : IsAlgebraicSpace B S hS Y₁)
    (hY₂ : IsAlgebraicSpace B S hS Y₂) (hsq : f₁ ≫ q = p ≫ f₂) :
    schemeTheoreticImageMap B S hS hY₁ hY₂ hsq ≫
        (schemeTheoreticImageSubfunctor B S hS f₂).ι =
      (schemeTheoreticImageSubfunctor B S hS f₁).ι ≫ q
```

**`AlgebraicGeometry.Space.toSchemeTheoreticImage_comp_schemeTheoreticImageMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImage.lean#L269). The attribute's comment: “the left square”.

> **Stacks 0CP2**, the left square: a morphism of scheme-theoretic images compatible with the
> inclusions into the targets is also compatible with the factorizations of the horizontal
> morphisms through their images.

```lean
theorem toSchemeTheoreticImage_comp_schemeTheoreticImageMap (hsq : f₁ ≫ q = p ≫ f₂)
    (h : (schemeTheoreticImageSubfunctor B S hS f₁).toFunctor ⟶
      (schemeTheoreticImageSubfunctor B S hS f₂).toFunctor)
    (hh : h ≫ (schemeTheoreticImageSubfunctor B S hS f₂).ι =
      (schemeTheoreticImageSubfunctor B S hS f₁).ι ≫ q) :
    toSchemeTheoreticImage B S hS f₁ ≫ h = p ≫ toSchemeTheoreticImage B S hS f₂
```

## Tag 0CP3, a lemma

[Tag 0CP3](https://stacks.math.columbia.edu/tag/0CP3) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_pullback_snd_schemeTheoreticImageSubfunctor_comp_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImagePartialSection.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticImagePartialSection.lean#L139).

> **Stacks 0CP3.** Let `f : X ⟶ Y` be a separated morphism of algebraic spaces over `S`, let
> `V ⊆ Y` be an open subspace whose inclusion into `Y` is quasi-compact, and let `s : V ⟶ X`
> satisfy `s ≫ f = 𝟙 V`.  Let `Y'` be the scheme-theoretic image of `s`, a closed subspace of
> `X`, and let `Y' ⟶ Y` be its inclusion followed by `f`.  Then **`Y' ⟶ Y` is an isomorphism
> over `V`**: the projection `Y' ×_Y V ⟶ V` of its base change along `V ⟶ Y` is an
> isomorphism.

```lean
theorem isIso_pullback_snd_schemeTheoreticImageSubfunctor_comp_of_section
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsSeparated B S hS f)
    (V : Subfunctor Y) (hV : IsOpenSubspace B S hS V)
    (hVqc : IsQuasiCompact B S hS V.ι)
    (s : V.toFunctor ⟶ X) (hs : s ≫ f = V.ι) :
    IsIso (pullback.snd ((schemeTheoreticImageSubfunctor B S hS s).ι ≫ f) V.ι)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.16, Tag 082W](https://stacks.math.columbia.edu/tag/082W)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
