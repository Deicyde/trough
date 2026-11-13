---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.completionSubspace, AlgebraicGeometry.Space.mem_nthOrderNeighbourhood_iff_isUniversalNthOrderThickening, AlgebraicGeometry.Space.isColimitCompletionSubspaceCocone, AlgebraicGeometry.Space.isPullback_completionSubspaceMap, AlgebraicGeometry.Space.isRepresentableByAlgebraicSpacesULift_completionSubspaceMap, AlgebraicGeometry.FormalSpace.isReduction_completionSubspace, AlgebraicGeometry.FormalSpace.isReduction_completionSubspace', AlgebraicGeometry.FormalSpace.isWeaklyAdic_completionAlongIdeal
statement: formalized
proof: formalized
---

# 87.38 Completion along a closed subspace

Section 87.38 of the Stacks Project, [Tag 0GXT](https://stacks.math.columbia.edu/tag/0GXT). 6 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GXU, a definition

[Tag 0GXU](https://stacks.math.columbia.edu/tag/0GXU) in the Stacks Project.

**`AlgebraicGeometry.Space.completionSubspace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceBaseChange.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceBaseChange.lean#L189). The attribute's comment: “the completion along a closed subspace”.

> **Stacks 0GXU.** The completion `X^∧_Z` of an algebraic space `X` over `S` along a closed
> subspace `Z`: the fppf sheafification of the union of the infinitesimal neighbourhoods of `Z`
> in `X`, which is their colimit `colim Z_n` in fppf sheaves
> (`AlgebraicGeometry.Space.isColimitCompletionSubspaceCocone`).

```lean
def completionSubspace (X : AlgebraicSpaces B S hS) (Z : Subfunctor X.1) :
    Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))
```

**`AlgebraicGeometry.Space.mem_nthOrderNeighbourhood_iff_isUniversalNthOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceNeighbourhoods.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceNeighbourhoods.lean#L138). The attribute's comment: “identification with colim Z\_n: the level n sections are those of Z\_n”.

> **The level `n` condition of the completion subfunctor cuts out `Z_n`.** A section `g` of
> `X` over an object `U` of the site has inverse image of `Z` a universal `n`th order thickening
> exactly when it factors through the `n`th order infinitesimal neighbourhood `Z_n`, the closed
> subspace of `X` cut out by the `(n + 1)`st power of the ideal sheaf of `Z` (Stacks 05ZV).

```lean
theorem mem_nthOrderNeighbourhood_iff_isUniversalNthOrderThickening (n : ℕ)
    (U : BigFppfOver B S hS) (g : X.1.obj (op U)) :
    g ∈ (nthOrderNeighbourhood B S hS X Z n).1.obj (op U) ↔
      IsUniversalNthOrderThickening B S hS n U
        (Z.1.preimage (yonedaEquiv.symm g : yoneda.obj U ⟶ X.1))
```

**`AlgebraicGeometry.Space.isColimitCompletionSubspaceCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceNeighbourhoods.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceNeighbourhoods.lean#L260). The attribute's comment: “identification with colim Z\_n in fppf sheaves”.

> **Stacks 0GXU.** The completion `X^∧_Z = completionSubspace X Z` of an algebraic space `X`
> along a closed subspace `Z` is the colimit `colim Z_n` in fppf sheaves of the `n`th order
> infinitesimal neighbourhoods `Z_n` of Stacks 05ZV, the closed subspaces cut out by the
> `(n + 1)`st powers of the ideal sheaf of `Z`: sheafification is a left adjoint, so it carries
> the presheaf colimit `AlgebraicGeometry.Space.isColimitNeighbourhoodCocone` to a colimit.

```lean
def isColimitCompletionSubspaceCocone : IsColimit (completionSubspaceCocone B S hS X Z)
```

## Tag 0GXV, a lemma

[Tag 0GXV](https://stacks.math.columbia.edu/tag/0GXV) in the Stacks Project.

**`AlgebraicGeometry.Space.isPullback_completionSubspaceMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceBaseChange.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceBaseChange.lean#L274). The attribute's comment: “the square is cartesian”.

> **Stacks 0GXV.** Completion along a closed subspace is compatible with base change: for a
> morphism `f : X' ⟶ X` of algebraic spaces over `S` and a subfunctor `Z` of `X`, in the source a
> closed subspace, the square formed by the completion of `X'` along `Z' = f⁻¹(Z) = X' ×_X Z`,
> the completion of `X` along `Z` and the two ambient sheaves is a cartesian square of fppf
> sheaves.

```lean
theorem isPullback_completionSubspaceMap {X' X : AlgebraicSpaces B S hS} (f : X' ⟶ X)
    (Z : Subfunctor X.1) :
    IsPullback
      (completionSubspaceToAmbient B S hS X' (Z.preimage f.hom))
      (completionSubspaceMap B S hS f Z)
      (sheafifiedULiftMap B S hS f.hom)
      (completionSubspaceToAmbient B S hS X Z)
```

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpacesULift_completionSubspaceMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceBaseChange.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceBaseChange.lean#L288). The attribute's comment: “representable by algebraic spaces”.

> **Stacks 0GXV.** For a morphism `f : X' ⟶ X` of algebraic spaces over `S` and a subfunctor
> `Z` of `X`, in the source a closed subspace, the induced morphism of completions
> `(X')^∧_{f⁻¹(Z)} ⟶ X^∧_Z` is representable by algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpacesULift_completionSubspaceMap
    {X' X : AlgebraicSpaces B S hS} (f : X' ⟶ X) (Z : Subfunctor X.1) :
    IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS
      (completionSubspaceMap B S hS f Z).hom
```

## Tag 0GXW, a lemma

[Tag 0GXW](https://stacks.math.columbia.edu/tag/0GXW) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isReduction_completionSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAlongClosedSubspaceReduction.lean, line 638](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAlongClosedSubspaceReduction.lean#L638). The attribute's comment: “the whole statement, under the additional hypothesis that the canonical morphism `Z ⟶ X^∧_Z` is a representable thickening; that is Tag 0AI9 for a colimit of algebraic spaces, which is available here only for a colimit of affine objects of the site”.

> **Stacks 0GXW.** Let `X` be an algebraic space over `S` and let `Z ⊆ X` be a closed
> subspace. The reduction of the completion `X^∧_Z` of `X` along `Z` is `Z_red`: the composite
> `Z_red ⟶ Z ⟶ X^∧_Z` exhibits `Z_red` as the reduction of the completion.
>
> The hypothesis is that the canonical morphism `Z ⟶ X^∧_Z` is a representable thickening. That
> is exactly what it is: `Z = Z_0` is a stage of the colimit presentation of `X^∧_Z` by the
> infinitesimal neighbourhoods of `Z`, whose transition morphisms are thickenings, so Stacks
> 0AI9 applies. The library has Stacks 0AI9 only for a colimit of *affine* objects of the site,
> `AlgebraicGeometry.FormalSpace.isThickening_colimitι`, which is why the property is carried
> here as a hypothesis; see the module docstring.

```lean
theorem isReduction_completionSubspace
    (hc : Space.IsRepresentableThickeningULift.{u + 1} B S hS
      (closedSubspaceToCompletionSubspace B S hS hX Z hZ).hom) :
    IsReduction B S hS (Space.completionSubspace B S hS ⟨X, hX⟩ Z)
      (reductionOfClosedSubspaceSheaf B S hS hX Z hZ)
      (reductionInclusion B S hS hX Z hZ ≫
        closedSubspaceToCompletionSubspace B S hS hX Z hZ)
```

**`AlgebraicGeometry.FormalSpace.isReduction_completionSubspace'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceThickening.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceThickening.lean#L240).

> **Stacks 0GXW.** Let `X` be an algebraic space over `S` and let `Z ⊆ X` be a closed
> subspace. The reduction of the completion `X^∧_Z` of `X` along `Z` is `Z_red`: the composite
> `Z_red ⟶ Z ⟶ X^∧_Z` exhibits `Z_red` as the reduction of the completion.
>
> Both morphisms are representable thickenings — the first because `Z_red` is a closed subspace
> of `X` contained in `Z` with the same point set, the second by
> `AlgebraicGeometry.FormalSpace.isRepresentableThickeningULift_toCompletionSubspace` — and
> `Z_red` is a reduced algebraic space, so the composite exhibits it as the reduction.
>
> This is the unconditional form of
> `AlgebraicGeometry.FormalSpace.isReduction_completionSubspace`, which takes the
> representability of `Z ⟶ X^∧_Z` as a hypothesis.

```lean
theorem isReduction_completionSubspace' :
    IsReduction B S hS (Space.completionSubspace B S hS ⟨X, hX⟩ Z)
      (reductionOfClosedSubspaceSheaf B S hS hX Z hZ)
      (reductionInclusion B S hS hX Z hZ ≫
        closedSubspaceToCompletionSubspace B S hS hX Z hZ)
```

## Tag 0GXX, a lemma

[Tag 0GXX](https://stacks.math.columbia.edu/tag/0GXX) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isWeaklyAdic_completionAlongIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionAlongIdeal.lean, line 849](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionAlongIdeal.lean#L849). The attribute's comment: “clause (1): weakly adic”.

> **Stacks 0GXX (1).** For an affine scheme `X = Spec A` over `S` and the closed subscheme
> `Z ⊆ X` of an ideal `I ⊆ A`, the completion `X^∧_Z` of `X` along `Z` is a weakly adic affine
> formal algebraic space: it is the formal spectrum of the `I`-adic completion of `A`, whose
> topology is given by the closures of the powers of the ideal generated by `I`.

```lean
public theorem isWeaklyAdic_completionAlongIdeal (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {A : Type u} [CommRing A] (f : Spec (.of A) ⟶ S)
    (hA : B.Contains (Spec (.of A))) (I : Ideal A) :
    IsWeaklyAdic B S hS (completionAlongIdeal B S hS f hA I)
```

**`AlgebraicGeometry.FormalSpace.isAdic_and_iso_formalSpectrum_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionAlongIdeal.lean, line 930](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionAlongIdeal.lean#L930). The attribute's comment: “clause (2): formal spectrum of the adic completion”. References: EGA I (10.8.5), “affine case Spf(Â)”; EGA I (10.10.1), “Spf(A) = X\_\{/X}”; EGA III (5.1.1), “Spf(A) ≅ Ŷ”.

> **Stacks 0GXX (2).** If `I` is finitely generated then the completion `X^∧_Z` of
> `X = Spec A` along the closed subscheme `Z` of `I` is `Spf (A^∧)` for the `I`-adic completion
> `A^∧` of `A`: the topology of `A^∧` is the adic topology of the ideal `I A^∧`, and `X^∧_Z` is
> the formal spectrum of `A^∧`.

```lean
public theorem isAdic_and_iso_formalSpectrum_adicCompletion (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) {A : Type u} [CommRing A] (f : Spec (.of A) ⟶ S)
    (hA : B.Contains (Spec (.of A))) (I : Ideal A) (hI : I.FG) :
    _root_.IsAdic (Ideal.map (algebraMap A (AdicCompletion I A)) I) ∧
      Nonempty (completionAlongIdeal B S hS f hA I ≅
        formalSpectrum (adicCompletionQuotientSystem B S hS f hA I))
```

**`AlgebraicGeometry.FormalSpace.isAdicStar_completionAlongIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionAlongIdeal.lean, line 943](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionAlongIdeal.lean#L943). The attribute's comment: “clause (3): adic star”.

> **Stacks 0GXX (3).** If `I` is finitely generated — equivalently, if the closed subscheme
> `Z ⊆ X = Spec A` of `I` is of finite presentation over `X` — then the completion `X^∧_Z` is an
> adic\* affine formal algebraic space: it is presented by the `I`-adic completion of `A`, which
> is adic with the finitely generated ideal of definition `I A^∧`.

```lean
public theorem isAdicStar_completionAlongIdeal (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {A : Type u} [CommRing A] (f : Spec (.of A) ⟶ S)
    (hA : B.Contains (Spec (.of A))) (I : Ideal A) (hI : I.FG) :
    IsAdicStar B S hS (completionAlongIdeal B S hS f hA I)
```

**`AlgebraicGeometry.FormalSpace.isNoetherian_completionAlongIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceLocalTypes.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceLocalTypes.lean#L411). The attribute's comment: “clause (4): Noetherian”. References: EGA I (10.8.6), “special case”.

> **Stacks 0GXX (4).** For an affine scheme `X = Spec A` over `S` with `A` Noetherian and the
> closed subscheme `Z ⊆ X` of an ideal `J ⊆ A`, the completion `X^∧_Z` of `X` along `Z` is a
> Noetherian affine formal algebraic space: it is presented by the `J`-adic completion of `A`,
> which is a Noetherian ring by Stacks 0316 and which is adic with the finitely generated ideal
> of definition `J A^∧` by Stacks 0GXX (2), the ideal `J` being finitely generated because `A` is
> Noetherian.

```lean
theorem isNoetherian_completionAlongIdeal {A : Type u} [CommRing A] [IsNoetherianRing A]
    (str : Spec (.of A) ⟶ S) (hA : B.Contains (Spec (.of A))) (J : Ideal A) :
    IsNoetherian B S hS (completionAlongIdeal B S hS str hA J)
```

## Tag 0GXY, a lemma

[Tag 0GXY](https://stacks.math.columbia.edu/tag/0GXY) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isLocallyWeaklyAdic_completionSubspace_of_isClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceAtlas.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceAtlas.lean#L424). The attribute's comment: “part (1): locally weakly adic”.

> **Stacks 0GXY (1).** Let `S` be a scheme, let `X` be an algebraic space over `S` and let
> `Z ⊆ X` be a closed subspace. The completion `X^∧_Z` of `X` along `Z` is *locally weakly
> adic*.
>
> The completions of the affine étale charts of `X` along the inverse images of `Z` form an atlas
> of `X^∧_Z` (Stacks 0GXV), each is the completion of an affine scheme along an ideal, hence
> weakly adic by Stacks 0GXX (1), and `X^∧_Z` satisfies the set-theoretic condition of Stacks
> 0AIS by `AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_completionSubspace`.

```lean
theorem isLocallyWeaklyAdic_completionSubspace_of_isClosedSubspace {X : AlgebraicSpaces B S hS}
    (Z : Subfunctor X.1) (hZ : Space.IsClosedSubspace B S hS Z) :
    IsLocallyWeaklyAdic B S hS (Space.completionSubspace B S hS X Z)
```

**`AlgebraicGeometry.FormalSpace.isLocallyAdicStar_completionSubspace_of_isClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceAtlas.lean, line 443](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceAtlas.lean#L443). The attribute's comment: “part (2): locally adic star”.

> **Stacks 0GXY (2).** Let `S` be a scheme, let `X` be an algebraic space over `S` and let
> `Z ⊆ X` be a closed subspace such that `Z ⟶ X` is of finite presentation. The completion
> `X^∧_Z` of `X` along `Z` is *locally adic\**.
>
> As in clause (1), with the members of the atlas adic\* by Stacks 0GXX (3): finite presentation
> of `Z ⟶ X` makes the ideal cutting out the inverse image of `Z` on an affine chart finitely
> generated, `AlgebraicGeometry.Space.fg_closedChartIdeal_of_isLocallyOfFinitePresentation`.

```lean
theorem isLocallyAdicStar_completionSubspace_of_isClosedSubspace {X : AlgebraicSpaces B S hS}
    (Z : Subfunctor X.1) (hZ : Space.IsClosedSubspace B S hS Z)
    (hZfp : Space.IsFinitePresentation B S hS Z.ι) :
    IsLocallyAdicStar B S hS (Space.completionSubspace B S hS X Z)
```

**`AlgebraicGeometry.FormalSpace.isLocallyNoetherian_completionSubspace_of_isClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceAtlas.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceAtlas.lean#L464). The attribute's comment: “part (3): locally Noetherian”.

> **Stacks 0GXY (3).** Let `S` be a scheme, let `X` be a locally Noetherian algebraic space
> over `S` and let `Z ⊆ X` be a closed subspace. The completion `X^∧_Z` of `X` along `Z` is
> *locally Noetherian*.
>
> As in clause (1), with the members of the atlas Noetherian by Stacks 0GXX (4),
> `AlgebraicGeometry.FormalSpace.isNoetherian_completionAlongIdeal`: local Noetherianness of `X`
> is local in the étale topology (Stacks 03E8), so every étale chart of `X` is a locally
> Noetherian scheme and its ring of regular functions is Noetherian.

```lean
theorem isLocallyNoetherian_completionSubspace_of_isClosedSubspace {X : AlgebraicSpaces B S hS}
    (Z : Subfunctor X.1) (hZ : Space.IsClosedSubspace B S hS Z)
    (hXN : Space.HasEtaleLocalProperty B S hS X.1
      (fun T : Scheme.{u} ↦ _root_.AlgebraicGeometry.IsLocallyNoetherian T)) :
    IsLocallyNoetherian B S hS (Space.completionSubspace B S hS X Z)
```

**`AlgebraicGeometry.FormalSpace.isLocallyWeaklyAdic_completionSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceLocalTypes.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceLocalTypes.lean#L336). The attribute's comment: “part (1): locally weakly adic; charts and 0AIS condition assumed”.

> **Stacks 0GXY (1).** Let `S` be a scheme, let `X` be an algebraic space over `S` and let
> `Z ⊆ X` be a closed subspace. The completion `X^∧_Z` of `X` along `Z` is *locally weakly
> adic*: the completions of the affine charts of `X` along the inverse images of `Z` form an
> atlas of `X^∧_Z`, and each of them is a weakly adic affine formal algebraic space by Stacks
> 0GXX (1).
>
> The charts of `X` and the identification of their completions with completions of affine
> schemes along ideals are carried as hypotheses, as is the set-theoretic condition of Stacks
> 0AIS; see the section "What is assumed" of this file.

```lean
theorem isLocallyWeaklyAdic_completionSubspace
    {X : AlgebraicSpaces B S hS} (Z : Subfunctor X.1)
    {Ix : Type (u + 1)} (Xi : Ix → AlgebraicSpaces B S hS) (f : ∀ i, Xi i ⟶ X)
    (hf : ∀ i, ∃ hfi : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS
        (Space.sheafifiedULiftMap B S hS (f i).hom).hom,
      Space.HasPropertyULift.{u + 1} B S hS
        (fun _ _ q ↦ Space.IsEtaleULift.{u + 1} B S hS q.hom)
        (Space.sheafifiedULiftMap B S hS (f i).hom).hom hfi)
    (hcov : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
          Sheaf.instHasColimitsOfSize
        Sheaf.IsLocallySurjective
          (Sigma.desc fun i ↦ Space.sheafifiedULiftMap B S hS (f i).hom))
    (hchart : ∀ i, ∃ (A : Type u) (_ : CommRing A) (str : Spec (.of A) ⟶ S)
      (hA : B.Contains (Spec (.of A))) (J : Ideal A),
      Nonempty (Space.completionSubspace B S hS (Xi i) (Z.preimage (f i).hom) ≅
        completionAlongIdeal B S hS str hA J))
    (hset : SatisfiesSetTheoreticCondition B S hS (Space.completionSubspace B S hS X Z)) :
    IsLocallyWeaklyAdic B S hS (Space.completionSubspace B S hS X Z)
```

**`AlgebraicGeometry.FormalSpace.isLocallyAdicStar_completionSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceLocalTypes.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceLocalTypes.lean#L373). The attribute's comment: “part (2): locally adic star; charts and 0AIS condition assumed”.

> **Stacks 0GXY (2).** Let `S` be a scheme, let `X` be an algebraic space over `S` and let
> `Z ⊆ X` be a closed subspace with `Z ⟶ X` of finite presentation. The completion `X^∧_Z` of
> `X` along `Z` is *locally adic\**: the completions of the affine charts of `X` along the
> inverse images of `Z` form an atlas of `X^∧_Z`, and each of them is an adic\* affine formal
> algebraic space by Stacks 0GXX (3), finite presentation of `Z ⟶ X` saying on an affine chart
> `Spec A` that the ideal cutting out the inverse image of `Z` is finitely generated.
>
> The charts of `X` and the identification of their completions with completions of affine
> schemes along finitely generated ideals are carried as hypotheses, as is the set-theoretic
> condition of Stacks 0AIS; see the section "What is assumed" of this file.

```lean
theorem isLocallyAdicStar_completionSubspace
    {X : AlgebraicSpaces B S hS} (Z : Subfunctor X.1)
    {Ix : Type (u + 1)} (Xi : Ix → AlgebraicSpaces B S hS) (f : ∀ i, Xi i ⟶ X)
    (hf : ∀ i, ∃ hfi : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS
        (Space.sheafifiedULiftMap B S hS (f i).hom).hom,
      Space.HasPropertyULift.{u + 1} B S hS
        (fun _ _ q ↦ Space.IsEtaleULift.{u + 1} B S hS q.hom)
        (Space.sheafifiedULiftMap B S hS (f i).hom).hom hfi)
    (hcov : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
          Sheaf.instHasColimitsOfSize
        Sheaf.IsLocallySurjective
          (Sigma.desc fun i ↦ Space.sheafifiedULiftMap B S hS (f i).hom))
    (hchart : ∀ i, ∃ (A : Type u) (_ : CommRing A) (str : Spec (.of A) ⟶ S)
      (hA : B.Contains (Spec (.of A))) (J : Ideal A), J.FG ∧
      Nonempty (Space.completionSubspace B S hS (Xi i) (Z.preimage (f i).hom) ≅
        completionAlongIdeal B S hS str hA J))
    (hset : SatisfiesSetTheoreticCondition B S hS (Space.completionSubspace B S hS X Z)) :
    IsLocallyAdicStar B S hS (Space.completionSubspace B S hS X Z)
```

**`AlgebraicGeometry.FormalSpace.isLocallyNoetherian_completionSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceLocalTypes.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceLocalTypes.lean#L436). The attribute's comment: “part (3): locally Noetherian; charts and 0AIS condition assumed”.

> **Stacks 0GXY (3).** Let `S` be a scheme, let `X` be a locally Noetherian algebraic space
> over `S` and let `Z ⊆ X` be a closed subspace. The completion `X^∧_Z` of `X` along `Z` is
> *locally Noetherian*: the completions of the affine charts of `X` along the inverse images of
> `Z` form an atlas of `X^∧_Z`, and each of them is presented by the adic completion of the
> Noetherian chart ring, which is adic with a finitely generated ideal of definition by Stacks
> 0GXX (2).
>
> The charts of `X` and the identification of their completions with completions of Noetherian
> affine schemes along ideals are carried as hypotheses, as is the set-theoretic condition of
> Stacks 0AIS; see the section "What is assumed" of this file.

```lean
theorem isLocallyNoetherian_completionSubspace
    {X : AlgebraicSpaces B S hS} (Z : Subfunctor X.1)
    {Ix : Type (u + 1)} (Xi : Ix → AlgebraicSpaces B S hS) (f : ∀ i, Xi i ⟶ X)
    (hf : ∀ i, ∃ hfi : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS
        (Space.sheafifiedULiftMap B S hS (f i).hom).hom,
      Space.HasPropertyULift.{u + 1} B S hS
        (fun _ _ q ↦ Space.IsEtaleULift.{u + 1} B S hS q.hom)
        (Space.sheafifiedULiftMap B S hS (f i).hom).hom hfi)
    (hcov : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
          Sheaf.instHasColimitsOfSize
        Sheaf.IsLocallySurjective
          (Sigma.desc fun i ↦ Space.sheafifiedULiftMap B S hS (f i).hom))
    (hchart : ∀ i, ∃ (A : Type u) (_ : CommRing A) (str : Spec (.of A) ⟶ S)
      (hA : B.Contains (Spec (.of A))) (J : Ideal A) (_ : IsNoetherianRing A),
      Nonempty (Space.completionSubspace B S hS (Xi i) (Z.preimage (f i).hom) ≅
        completionAlongIdeal B S hS str hA J))
    (hset : SatisfiesSetTheoreticCondition B S hS (Space.completionSubspace B S hS X Z)) :
    IsLocallyNoetherian B S hS (Space.completionSubspace B S hS X Z)
```

## Tag 0H8N, a lemma

[Tag 0H8N](https://stacks.math.columbia.edu/tag/0H8N) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_completionSubspaceComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceComparison.lean, line 480](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceComparison.lean#L480). The attribute's comment: “the comparison is an isomorphism for a closed subspace of finite presentation”.

> **Stacks 0H8N, the positive half.** Let `X` be an algebraic space over `S` and let `Z ⊆ X`
> be a closed subspace with point set `T = |Z|`. If `Z ⟶ X` is of finite presentation, the
> canonical morphism `c : X^∧_Z ⟶ X_{/T}` is an isomorphism.
>
> Both sides are sheafifications of subfunctors of `X`, and `c` is the sheafification of the
> inclusion of the first into the second. That inclusion is injective on sections, hence locally
> injective; and it is locally surjective because the affine objects of the site generate the
> fppf topology (Stacks 021V) and over an affine object the two subfunctors agree, by
> `AlgebraicGeometry.Space.mem_completionSubspaceSubfunctor_of_hasImageIn_of_isAffine`. A locally
> bijective morphism of sheaves of types is an isomorphism.
>
> The negative half of the source's statement — that `c` is *not* an isomorphism in general — is
> not formalized here; see the module documentation.

```lean
theorem isIso_completionSubspaceComparison (X : AlgebraicSpaces B S hS) (Z : Subfunctor X.1)
    (hZ : IsClosedSubspace B S hS Z) (hfp : IsFinitePresentation B S hS Z.ι) :
    IsIso (completionSubspaceComparison B S hS X Z)
```

**`AlgebraicGeometry.Space.not_isIso_completionSubspaceComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceCounterexample.lean, line 514](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSubspaceCounterexample.lean#L514). The attribute's comment: “the comparison is not an isomorphism in general”.

> **Stacks 0H8N, the negative half.** There are a scheme `S` in a big fppf site `B`, an
> algebraic space `X` over `S` and a closed subspace `Z ⊆ X` for which the canonical morphism
> `c : X^∧_Z ⟶ X_{/T}`, `T = |Z|`, is **not** an isomorphism.
>
> Take `A = ℤ[x₀, x₁, x₂, …]`, `S = X = Spec A` and `Z = Spec (A ⧸ I)` the closed subscheme cut
> out by `I = (x₀, x₁, x₂, …)`, which is not of finite presentation. The section
> `Spec (A ⧸ (xₙ ^ (n+1) : n)) ⟶ Spec A` is supported on `|Z|`, because every variable is
> nilpotent in the quotient and so dies in any field-valued point; but no infinitesimal
> neighbourhood of `Z` contains it, not even after an fppf covering, because the exponent needed
> to kill `xₘ` in the quotient grows with `m` while a covering supplies only finitely many
> exponents and detects vanishing faithfully.

```lean
theorem not_isIso_completionSubspaceComparison :
    ∃ (B : BigFppfSite.{0}) (S : Scheme.{0}) (hS : B.Contains S)
      (X : AlgebraicSpaces B S hS) (Z : Subfunctor X.1),
      IsClosedSubspace B S hS Z ∧
        ¬ IsIso (completionSubspaceComparison B S hS X Z)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.38, Tag 0GXT](https://stacks.math.columbia.edu/tag/0GXT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
