---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_directed_limit_isFinitePresentation_of_isAffineHom, AlgebraicGeometry.Space.integralFiniteSystemOfIsIntegralHom, AlgebraicGeometry.Space.exists_integralFiniteSystem_of_isFinite, AlgebraicGeometry.Space.exists_isLimit_closedSubspaces_of_isClosedImmersion, AlgebraicGeometry.Space.hasClosedSubspaceApproximation_of_invariantIdeals, AlgebraicGeometry.Space.exists_isFinitePresentation_isClosedImmersion_of_isQuasiAffineHom, AlgebraicGeometry.Space.exists_isFinitePresentation_isClosedImmersion_of_isQuasiAffineHom_of_qcqs, AlgebraicGeometry.Space.exists_isClosedImmersion_isFinitePresentation_of_isLocallyOfFiniteType
statement: formalized
proof: formalized
---

# 70.11 Finite type closed in finite presentation

Section 70.11 of the Stacks Project, [Tag 07SP](https://stacks.math.columbia.edu/tag/07SP). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0870, a lemma

[Tag 0870](https://stacks.math.columbia.edu/tag/0870) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_directed_limit_isFinitePresentation_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismDirectedLimit.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismDirectedLimit.lean#L52). The attribute's comment: “the whole statement, under the source's hypotheses only: a directed inverse system of algebraic spaces affine and of finite presentation over Y, with X its limit and the projections compatible with f”.

> **Stacks 0870.** Let `S` be a scheme and let `f : X ⟶ Y` be an affine morphism of algebraic
> spaces over `S`.  If `Y` is quasi-compact and quasi-separated, then `X` is a directed limit
> `X = lim X_i` of algebraic spaces `X_i` affine over `Y` and of finite presentation over `Y`.
>
> The system is indexed by the opposite of a nonempty directed preorder, so it is an inverse
> system; `t` is the family of structure morphisms `X_i ⟶ Y`, which are affine and of finite
> presentation, `p` is the family of projections `X ⟶ X_i`, each of which composes with the
> structure morphism to `f`, and `X` is the limit of the underlying presheaves, that is, of the
> fppf sheaves.

```lean
theorem exists_directed_limit_isFinitePresentation_of_isAffineHom
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsAffineHom B S hS f)
    (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y) :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (D : Iᵒᵖ ⥤ ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
      (t : D ⟶ (Functor.const Iᵒᵖ).obj Y) (p : (Functor.const Iᵒᵖ).obj X ⟶ D)
      (_ : IsLimit (Cone.mk X p)),
      (∀ i, IsAlgebraicSpace B S hS (D.obj i)) ∧
        (∀ i, IsAffineHom B S hS (t.app i)) ∧
          (∀ i, IsFinitePresentation B S hS (t.app i)) ∧
            ∀ i, p.app i ≫ t.app i = f
```

## Tag 09YA, a lemma

[Tag 09YA](https://stacks.math.columbia.edu/tag/09YA) in the Stacks Project.

**`AlgebraicGeometry.Space.integralFiniteSystemOfIsIntegralHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralMorphismDirectedLimit.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralMorphismDirectedLimit.lean#L97).

> **Stacks 09YA.** An integral morphism `f : X ⟶ Y` of algebraic spaces over `S`, with `Y`
> quasi-compact and quasi-separated, presents `X` as a directed limit `X = lim X_i` of algebraic
> spaces `X_i` finite and of finite presentation over `Y`.
>
> The system is a directed inverse system of algebraic spaces over `Y` indexed by a nonempty
> directed preorder, with a cone from `X` compatible with `f` which is a limit cone; every stage is
> finite and of finite presentation over `Y`
> (`AlgebraicGeometry.Space.IntegralFiniteSystem`).  The stages are the relative spectra
> `\underline{Spec}_Y(𝒜_i)` (Stacks 081W) of the finite, finitely presented algebras of
> Stacks 082C presenting `f_* 𝒪_X`.

```lean
def integralFiniteSystemOfIsIntegralHom (f : X ⟶ Y) (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hf : IsIntegralHom B S hS f)
    (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y) :
    IntegralFiniteSystem B S hS f
```

## Tag 07VR, a lemma

[Tag 07VR](https://stacks.math.columbia.edu/tag/07VR) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_integralFiniteSystem_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteMorphismLimitSystem.lean, line 523](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteMorphismLimitSystem.lean#L523). The attribute's comment: “finite X ⟶ Y, Y qcqs: X = lim of finite f.p. X\_i ⟶ Y, closed immersion transitions”.

> **Stacks 07VR.** Let `S` be a scheme and let `f : X ⟶ Y` be a finite morphism of algebraic
> spaces over `S`, with `Y` quasi-compact and quasi-separated.  Then `X` is the limit of a directed
> inverse system of algebraic spaces `X_i`, finite and of finite presentation over `Y`, whose
> transition morphisms are closed immersions.
>
> The direct-image algebra `f_* 𝒪_X` is a finite quasi-coherent `𝒪_Y`-algebra
> (`AlgebraicGeometry.Space.isFinite_pushforwardAlgebra_of_isFinite`); Stacks 086Z
> (`Space.exists_directed_isFinite_isFinitePresentation_locallySurjective_of_isFinite`)
> writes it as a directed colimit of finite algebras of finite presentation with surjective
> transition maps; and `X_i = \underline{Spec}_Y(𝒜_i)` is the limit presentation by
> `AlgebraicGeometry.Space.exists_integralFiniteSystem_of_isFinite_of_presentation`.

```lean
theorem exists_integralFiniteSystem_of_isFinite {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hfin : IsFinite B S hS f)
    (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y) :
    ∃ s : IntegralFiniteSystem B S hS f,
      letI := s.indexPreorder
      ∀ (i j : s.indexType) (h : i ≤ j),
        IsClosedImmersion B S hS (s.diagram.map (homOfLE h).op)
```

## Tag 0A0U, a lemma

[Tag 0A0U](https://stacks.math.columbia.edu/tag/0A0U) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isLimit_closedSubspaces_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ClosedImmersionFinitePresentationLimit.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ClosedImmersionFinitePresentationLimit.lean#L106).

> Let `S` be a scheme and let `f : X ⟶ Y` be a closed immersion of algebraic spaces over `S`,
> with `Y` quasi-compact and quasi-separated. Then `X` is a directed limit `X = lim X_i`: there are a
> nonempty directed index set and an inverse system of closed subspaces `X_i ⊆ Y` whose transition
> morphisms are closed immersions and whose inclusions `X_i ⟶ Y` are closed immersions of finite
> presentation, together with a limiting cone with vertex `X` whose legs `X ⟶ X_i` compose with the
> inclusions to `f`.

```lean
theorem exists_isLimit_closedSubspaces_of_isClosedImmersion (Y : AlgebraicSpaces B S hS)
    (hYqc : IsQuasiCompactSpace B S hS Y.1) (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y.1)
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y.1)
    (hf : IsClosedImmersion B S hS f) :
    ∃ (I : Type u) (_ : Preorder I) (_ : IsDirected I (· ≤ ·)) (_ : Nonempty I)
      (Z : I → ClosedSubspaces B S hS Y.1) (hZ : ∀ ⦃i j : I⦄, i ≤ j → (Z j).1 ≤ (Z i).1)
      (hle : ∀ i, Subfunctor.range f ≤ (Z i).1),
      (∀ ⦃i j : Iᵒᵖ⦄ (g : i ⟶ j), IsClosedImmersion B S hS
        ((closedSubspaceDiagram B S hS (fun i => (Z i).1) hZ).map g)) ∧
      (∀ i, IsClosedImmersion B S hS (Z i).1.ι ∧ IsFinitePresentation B S hS (Z i).1.ι) ∧
      (∀ i, ((closedSubspaceCone B S hS (fun i => (Z i).1) hZ (Subfunctor.range f) hle).extend
        (Subfunctor.toRange f)).π.app (op i) ≫ (Z i).1.ι = f) ∧
      Nonempty (IsLimit ((closedSubspaceCone B S hS (fun i => (Z i).1) hZ (Subfunctor.range f)
        hle).extend (Subfunctor.toRange f)))
```

**`AlgebraicGeometry.Space.hasClosedSubspaceApproximation_of_invariantIdeals`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ClosedSubspaceApproximation.lean, line 575](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ClosedSubspaceApproximation.lean#L575). The attribute's comment: “given the approximating family of invariant ideal sheaves on a chart, which is Stacks 0829 for the ideal sheaf of `X` read on that chart”.

> **Stacks 0A0U.** Let `S` be a scheme and let `X ⊆ Y` be a closed subspace of an algebraic
> space `Y` over `S`.  Then `X` is a directed inverse limit `X = lim X_i` of closed subspaces of
> `Y` whose transition morphisms are closed immersions and whose structure morphisms `X_i ⟶ Y` are
> closed immersions of finite presentation, as soon as the ideal sheaf cut out by `X` on a
> surjective étale scheme chart `V ⟶ Y` is the supremum of a monotone family of invariant ideal
> sheaves of `𝒪_V` each of which cuts out a closed subspace of finite presentation over `Y`.
>
> The approximating family is the hypothesis: it is what Stacks 0829 supplies for the ideal sheaf
> of `X`, read on the chart `V`, together with Stacks 084Q for the finite presentation of the
> stages.  Everything else is proved here and unconditionally: each member of the family cuts out
> a closed subspace of `Y` by étale descent, its chart ideal on `V` is the given ideal sheaf, the
> family of subspaces is antitone with `X` contained in every member, and the inclusions exhibit
> `X` as the inverse limit.

```lean
theorem hasClosedSubspaceApproximation_of_invariantIdeals [Preorder I] [IsDirected I (· ≤ ·)]
    (i₀ : I) (X : ClosedSubspaces B S hS Y.1) (hK : Monotone K)
    (hsup : (⨆ i, K i) = etaleChartKer B S hS Y X (chartOfSurjectiveEtale B S hS Y he))
    (hfp : ∀ i, IsFinitePresentation B S hS
      (invariantSubspace B S hS φ (Subobject.mk (K i).subschemeι)).ι) :
    HasClosedSubspaceApproximation B S hS Y X
```

## Tag 0871, a lemma

[Tag 0871](https://stacks.math.columbia.edu/tag/0871) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isFinitePresentation_isClosedImmersion_of_isQuasiAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/QuasiAffineClosedInFinitePresentation.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/QuasiAffineClosedInFinitePresentation.lean#L139). The attribute's comment: “for a target represented by a quasi-compact quasi-separated object of the site; a general algebraic-space target needs the unproved direction of 086S and Stacks 0870”.

> A morphism of algebraic spaces over `S` which is locally of finite type and quasi-affine,
> whose target is the functor of points of a quasi-compact, quasi-separated scheme of the site, is a
> closed immersion into an algebraic space of finite presentation over that target.

```lean
theorem exists_isFinitePresentation_isClosedImmersion_of_isQuasiAffineHom
    {Z : BigFppfOver B S hS} {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ yoneda.obj Z)
    (hX : IsAlgebraicSpace B S hS X)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hqa : IsQuasiAffineHom B S hS f)
    (hZqc : CompactSpace ((BigFppfOver.toScheme B S hS).obj Z))
    (hZqs : QuasiSeparatedSpace ((BigFppfOver.toScheme B S hS).obj Z)) :
    ∃ (X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f' : X' ⟶ yoneda.obj Z) (i : X ⟶ X'),
      IsAlgebraicSpace B S hS X' ∧ IsFinitePresentation B S hS f' ∧
        IsClosedImmersion B S hS i ∧ i ≫ f' = f
```

**`AlgebraicGeometry.Space.exists_isFinitePresentation_isClosedImmersion_of_isQuasiAffineHom_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/QuasiAffineClosedInFinitePresentationQcqs.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/QuasiAffineClosedInFinitePresentationQcqs.lean#L119).

> Let `S` be a scheme and let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S` which is locally of finite type and quasi-affine, with `Y` quasi-compact and
> quasi-separated.  Then there are a morphism of finite presentation `f' : X' ⟶ Y` and a closed
> immersion `i : X ⟶ X'` with `i ≫ f' = f`.

```lean
theorem exists_isFinitePresentation_isClosedImmersion_of_isQuasiAffineHom_of_qcqs
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hft : IsLocallyOfFiniteType B S hS f) (hfqa : IsQuasiAffineHom B S hS f)
    (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y) :
    ∃ (X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f' : X' ⟶ Y) (i : X ⟶ X'),
      IsAlgebraicSpace B S hS X' ∧ IsFinitePresentation B S hS f' ∧
        IsClosedImmersion B S hS i ∧ i ≫ f' = f
```

## Tag 0872, a lemma

[Tag 0872](https://stacks.math.columbia.edu/tag/0872) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.exists_isClosedImmersion_isFinitePresentation_of_isLocallyOfFiniteType`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteTypeClosedInFinitePresentation.lean#L45), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteTypeClosedInFinitePresentationTag.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteTypeClosedInFinitePresentationTag.lean#L25) (StacksFrontier): “a morphism of algebraic spaces over `S`, locally of finite type, with source and target quasi-compact and quasi-separated, is a closed immersion `i : X ⟶ X'` followed by a morphism of finite presentation `f' : X' ⟶ Y` with `i ≫ f' = f`”.

## Tag 0873, a proposition

[Tag 0873](https://stacks.math.columbia.edu/tag/0873) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isClosedImmersion_isSeparated_isFinitePresentation_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperLimitOfFinitePresentationEmbedding.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperLimitOfFinitePresentationEmbedding.lean#L196).

> Let `f : X ⟶ Y` be a separated morphism of finite type of algebraic spaces over `S`, with `Y`
> quasi-compact and quasi-separated. Then there are a separated morphism of finite presentation
> `f' : X' ⟶ Y` and a closed immersion `i : X ⟶ X'` with `i ≫ f' = f`.

```lean
theorem exists_isClosedImmersion_isSeparated_isFinitePresentation_of_isFiniteType
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hft : IsFiniteType B S hS f)
    (hsep : IsSeparated B S hS f) (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y) :
    ∃ (X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (i : X ⟶ X') (f' : X' ⟶ Y),
      IsAlgebraicSpace B S hS X' ∧ IsClosedImmersion B S hS i ∧ IsSeparated B S hS f' ∧
        IsFinitePresentation B S hS f' ∧ i ≫ f' = f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.11, Tag 07SP](https://stacks.math.columbia.edu/tag/07SP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
