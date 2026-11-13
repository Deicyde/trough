---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.locallyOfFinitePresentation_iff_isLimitPreservingOnAffineTransitions, AlgebraicGeometry.Scheme.locallyOfFinitePresentation_tfae_directed, locallyOfFinitePresentation_iff_isLimitPreserving_yoneda, AlgebraicGeometry.Scheme.IsLimitPreserving, AlgebraicGeometry.Scheme.locallyOfFinitePresentation_iff_isLimitPreserving_yoneda, AlgebraicGeometry.locallyOfFinitePresentation_of_directedAffineLimit_surjective, AlgebraicGeometry.existsUnique_hom_of_punctured_and_stalk
statement: formalized
proof: formalized
---

# 32.6 Limits and morphisms of finite presentation

Section 32.6 of the Stacks Project, [Tag 01ZB](https://stacks.math.columbia.edu/tag/01ZB). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01ZC, a proposition

[Tag 01ZC](https://stacks.math.columbia.edu/tag/01ZC) in the Stacks Project.

**`AlgebraicGeometry.Scheme.locallyOfFinitePresentation_iff_isLimitPreservingOnAffineTransitions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/LimitPreservingFunctorOfPoints.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/LimitPreservingFunctorOfPoints.lean#L139). The attribute's comment: “parts (1) and (3), with the inverse systems indexed by cofiltered categories rather than by directed sets”. References: EGA IV (8.14.2), “a ⇔ b”.

> A scheme `X` over `S` is locally of finite presentation over `S` if and only if its functor
> of points `h_X = Mor_S(-, X)` turns every cofiltered inverse limit of quasi-compact and
> quasi-separated `S`-schemes with affine transition morphisms into a filtered colimit.
>
> The same characterization with the inverse systems restricted to affine schemes is
> `locallyOfFinitePresentation_iff_isLimitPreserving_yoneda`.

```lean
theorem locallyOfFinitePresentation_iff_isLimitPreservingOnAffineTransitions
    {X S : Scheme.{u}} (f : X ⟶ S) :
    LocallyOfFinitePresentation f ↔
      IsLimitPreservingOnAffineTransitions S (yoneda.obj (Over.mk f))
```

**`AlgebraicGeometry.Scheme.locallyOfFinitePresentation_tfae_directed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/LimitPreservingFunctorOfPoints.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/LimitPreservingFunctorOfPoints.lean#L177). References: EGA IV (17.3.2), “more general”; SGA 3 XI (3.2), “partial”.

> **Stacks 01ZC.** For a morphism of schemes `f : X ⟶ S` the following are equivalent:
>
> 1. `f` is locally of finite presentation;
> 2. for every directed set `Λ` and every inverse system `(T_i)` of affine `S`-schemes over `Λ`,
>    the canonical map `colim_i Mor_S(T_i, X) → Mor_S(lim_i T_i, X)` is bijective;
> 3. for every directed set `Λ` and every inverse system `(T_i)` of `S`-schemes over `Λ` whose
>    transition morphisms are affine and whose members are quasi-compact and quasi-separated, the
>    canonical map `colim_i Mor_S(T_i, X) → Mor_S(lim_i T_i, X)` is bijective.
>
> A directed set is a nonempty preordered type in which any two elements have an upper bound, as in
> the source, taken in the universe of the schemes; an inverse system over it is a functor out of
> `Λᵒᵖ`. Bijectivity of the canonical map is `PreservesColimit` of the functor of points
> `Mor_S(-, X)` for the opposite diagram.
>
> The cofiltered readings of conditions (2) and (3) are
> `locallyOfFinitePresentation_iff_isLimitPreserving_yoneda` and
> `locallyOfFinitePresentation_iff_isLimitPreservingOnAffineTransitions`; condition (1) implies
> the directed forms by specializing them along `Λᵒᵖ`, and the directed form of condition (2)
> implies condition (1) by the directed criterion
> `AlgebraicGeometry.locallyOfFinitePresentation_of_directedAffineLimit_surjective`.

```lean
theorem locallyOfFinitePresentation_tfae_directed {X S : Scheme.{u}} (f : X ⟶ S) :
    List.TFAE
      [ LocallyOfFinitePresentation f,
        ∀ (Λ : Type u) [Preorder Λ] [Nonempty Λ] [IsDirectedOrder Λ] (D : Λᵒᵖ ⥤ Over S),
          (∀ i, IsAffine (D.obj i).left) → PreservesColimit D.op (yoneda.obj (Over.mk f)),
        ∀ (Λ : Type u) [Preorder Λ] [Nonempty Λ] [IsDirectedOrder Λ] (D : Λᵒᵖ ⥤ Over S),
          (∀ (i j : Λᵒᵖ) (g : i ⟶ j), IsAffineHom (D.map g).left) →
          (∀ i, CompactSpace (D.obj i).left) →
          (∀ i, QuasiSeparatedSpace (D.obj i).left) →
            PreservesColimit D.op (yoneda.obj (Over.mk f)) ]
```

Declarations registered for the tag:

- [`locallyOfFinitePresentation_iff_isLimitPreserving_yoneda`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=locallyOfFinitePresentation_iff_isLimitPreserving_yoneda#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Limits/LimitPreservingFunctorOfPoints.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/LimitPreservingFunctorOfPoints.lean#L116) (StacksFrontier): “parts (1) and (2), with the inverse systems indexed by cofiltered categories rather than by directed sets”.

## Tag 05LX, a remark

[Tag 05LX](https://stacks.math.columbia.edu/tag/05LX) in the Stacks Project.

**`AlgebraicGeometry.Scheme.IsLimitPreserving`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/LimitPreservingFunctorOfPoints.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/LimitPreservingFunctorOfPoints.lean#L78). The attribute's comment: “limit preserving functors”. References: SGA 3 XI (3.2), “definition of (*)”.

> **Stacks 05LX.** A functor on schemes over `S` is *limit preserving* when for every
> cofiltered inverse system `{T_i}` of affine schemes over `S` with limit `T` the canonical map
> `colim_i F(T_i) → F(T)` is bijective.

```lean
def IsLimitPreserving (S : Scheme.{u}) (F : (Over S)ᵒᵖ ⥤ Type v) : Prop
```

**`AlgebraicGeometry.Scheme.locallyOfFinitePresentation_iff_isLimitPreserving_yoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/LimitPreservingFunctorOfPoints.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/LimitPreservingFunctorOfPoints.lean#L109). The attribute's comment: “locally of finite presentation iff the functor of points is limit preserving”. References: SGA 3 XI (3.2), “representable case”.

> **Stacks 01ZC in the terminology of limit preserving functors.** A scheme `X` over `S` is
> locally of finite presentation over `S` if and only if its functor of points
> `h_X = Mor_S(-, X)` is limit preserving.

```lean
theorem locallyOfFinitePresentation_iff_isLimitPreserving_yoneda {X S : Scheme.{u}} (f : X ⟶ S) :
    LocallyOfFinitePresentation f ↔ IsLimitPreserving S (yoneda.obj (Over.mk f))
```

## Tag 0CM0, a lemma

[Tag 0CM0](https://stacks.math.columbia.edu/tag/0CM0) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFinitePresentation_of_directedAffineLimit_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/SurjectiveFinitePresentationCriterion.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/SurjectiveFinitePresentationCriterion.lean#L215). The attribute's comment: “if every morphism to `X` over `S` out of the limit of a directed inverse system of affine schemes over `S` factors through a stage, then `f` is locally of finite presentation”. References: EGA IV (17.3.2), “partial”; EGA IV (8.14.2), “partial”; SGA 3 XI (3.2), “partial”.

> If every map to `X` out of the limit of a **directed** inverse system of affine schemes over
> `S` descends to a finite stage, then `X ⟶ S` is locally of finite presentation.
>
> This is Stacks 0CM0: the index categories are the opposites of directed posets in the universe
> of the schemes, the directed inverse systems of the source, rather than arbitrary cofiltered
> categories, which is all the ring-theoretic criterion of Stacks 00QO ever needs. Limit
> preservation in the sense of
> `AlgebraicGeometry.ExtendingFunctors.PreservesAffineLimits` is tested on exactly these index
> categories, so it is this form and not
> `AlgebraicGeometry.locallyOfFinitePresentation_of_affineLimit_surjective` that applies to a
> functor known to be limit preserving in that sense.

```lean
public theorem locallyOfFinitePresentation_of_directedAffineLimit_surjective
    {X S : Scheme.{u}} (f : X ⟶ S)
    (hsurj : ∀ (Λ : Type u) [PartialOrder Λ] [Nonempty Λ] [IsDirectedOrder Λ]
      (D : Λᵒᵖ ⥤ Over S) (c : Cone D), IsLimit c →
      (∀ i, IsAffine (D.obj i).left) →
      ∀ g : c.pt ⟶ Over.mk f,
        ∃ (i : Λᵒᵖ) (gᵢ : D.obj i ⟶ Over.mk f), c.π.app i ≫ gᵢ = g) :
    LocallyOfFinitePresentation f
```

## Tag 0GWT, a lemma

[Tag 0GWT](https://stacks.math.columbia.edu/tag/0GWT) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_hom_of_punctured_and_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/GluingAtClosedPoint.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/GluingAtClosedPoint.lean#L118).

> Morphisms from a scheme are glued uniquely from its punctured complement and the local
> scheme at a closed point, when the target is locally of finite presentation over the base.

```lean
theorem existsUnique_hom_of_punctured_and_stalk
    {S X Y : Scheme.{u}} (fX : X ⟶ S) (fY : Y ⟶ S)
    [LocallyOfFinitePresentation fY] (x : X) (hx : IsClosed ({x} : Set X)) :
    let U : X.Opens := ⟨({x} : Set X)ᶜ, hx.isOpen_compl⟩
    ∀ (_hU : QuasiCompact U.ι)
      (a : U.toScheme ⟶ Y) (b : Spec (X.presheaf.stalk x) ⟶ Y),
      a ≫ fY = U.ι ≫ fX →
      b ≫ fY = X.fromSpecStalk x ≫ fX →
      pullback.fst U.ι (X.fromSpecStalk x) ≫ a =
        pullback.snd U.ι (X.fromSpecStalk x) ≫ b →
      ∃! f : X ⟶ Y,
        (f ≫ fY = fX) ∧ (U.ι ≫ f = a) ∧ (X.fromSpecStalk x ≫ f = b)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.6, Tag 01ZB](https://stacks.math.columbia.edu/tag/01ZB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
