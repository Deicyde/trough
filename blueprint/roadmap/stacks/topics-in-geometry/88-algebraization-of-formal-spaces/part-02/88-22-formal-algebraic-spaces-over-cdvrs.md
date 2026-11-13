---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.exists_flatPart_of_isLocallyNoetherian_of_isAdicComplete, AlgebraicGeometry.FormalSpace.isIso_or_isInitial_flatPart_of_isRigEtale_of_isRigSurjective_diagonal, AlgebraicGeometry.FormalSpace.isRigSurjective_iff_factorsAdicCompleteDvrPoints_of_rigEtale_diagonal
statement: formalized
proof: formalized
---

# 88.22 Formal algebraic spaces over cdvrs

Section 88.22 of the Stacks Project, [Tag 0GD7](https://stacks.math.columbia.edu/tag/0GD7). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GD8, a lemma

[Tag 0GD8](https://stacks.math.columbia.edu/tag/0GD8) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_flatPart_of_isLocallyNoetherian_of_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FlatPartOverCdvrFull.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FlatPartOverCdvrFull.lean#L80).

> **Stacks 0GD8.** Let `A` be a complete discrete valuation ring, carrying its `𝔪`-adic
> topology, and let `X` be a locally Noetherian formal algebraic space over `S` with a structure
> morphism `p : X ⟶ Spf A`. Then there is a closed immersion `ι : X' ⟶ X` of formal algebraic
> spaces with `X'` locally Noetherian and flat over `A` such that every morphism `q : Y ⟶ X` with
> `Y` a locally Noetherian formal algebraic space flat over `A` factors through `ι`.
>
> The members `Uᵢ` of a Noetherian atlas of `X` carry affine flat parts `Zᵢ ⟶ Uᵢ`, the formal
> spectra of the quotients by the `A`-torsion of their presenting rings; these glue to `ι`, the
> `Zᵢ` forming an atlas of `X'`, on which flatness of `X'` over `A` is read off by Remark 0ANI.
> A test object `Y` is covered by Noetherian affine charts flat over `A` mapping to the `Uᵢ`;
> each factors through the corresponding `Zᵢ`, and the factorizations descend along the
> covering because `ι` is a monomorphism.
>
> The hypotheses are the source's: `hA` and `hAc` say that `A` carries its `𝔪`-adic topology
> and is complete for it, which is what "complete discrete valuation ring" means and what makes
> `formalSpectrum D` the formal spectrum `Spf A`. The conclusion contains both halves of the
> source's, and records in addition that `X'` is locally Noetherian.

```lean
theorem exists_flatPart_of_isLocallyNoetherian_of_isAdicComplete
    [IsDomain A] [IsDiscreteValuationRing A]
    (hA : _root_.IsAdic (IsLocalRing.maximalIdeal A))
    (hAc : IsAdicComplete (IsLocalRing.maximalIdeal A) A)
    {X : FppfSheaf B S hS} (hX : IsLocallyNoetherian B S hS X) (p : X ⟶ formalSpectrum D) :
    ∃ (X' : FppfSheaf B S hS) (ι : X' ⟶ X),
      IsClosedImmersion B S hS ι ∧ IsLocallyNoetherian B S hS X' ∧
        IsFlat B S hS (ι ≫ p) ∧
        ∀ (Y : FppfSheaf B S hS) (q : Y ⟶ X), IsLocallyNoetherian B S hS Y →
          IsFlat B S hS (q ≫ p) → ∃ r : Y ⟶ X', r ≫ ι = q
```

## Tag 0GD9, a lemma

[Tag 0GD9](https://stacks.math.columbia.edu/tag/0GD9) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isIso_or_isInitial_flatPart_of_isRigEtale_of_isRigSurjective_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FlatPartRigEtaleDiagonalUnconditional.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FlatPartRigEtaleDiagonalUnconditional.lean#L103).

> **Stacks 0GD9.** Let `A` be a complete discrete valuation ring, carrying its `𝔪`-adic
> topology, let `X` be a locally Noetherian formal algebraic space over `S` with a structure
> morphism `p : X ⟶ Spf A` locally of finite type, and let `ι : X' ⟶ X` be as in Stacks 0GD8: a
> closed immersion with `X'` flat over `A` through which every morphism `Y ⟶ X` from a locally
> Noetherian formal algebraic space flat over `A` factors. If the relative diagonal
> `X ⟶ X ×_{Spf A} X` is rig-étale and rig-surjective, then `X' = Spf A` or `X' = ∅`: the
> structure morphism `ι ≫ p` of `X'` is an isomorphism, or `X'` is initial.
>
> `X'` is locally Noetherian, being locally of finite type over `X` (Stacks 0AQ7). The relative
> diagonal of `ι ≫ p` is the base change of that of `p` along the adic comparison
> `X' ×_{Spf A} X' ⟶ X ×_{Spf A} X`, `ι` being a monomorphism, so it is rig-étale (Stacks 0GD1) and
> rig-surjective (Stacks 0AQS), and
> `isIso_or_isInitial_of_isFlat_of_isRigEtale_of_isRigSurjective_diagonal` applies to `ι ≫ p`.

```lean
theorem isIso_or_isInitial_flatPart_of_isRigEtale_of_isRigSurjective_diagonal
    [IsDomain A] [IsDiscreteValuationRing A]
    (hAadic : _root_.IsAdic (IsLocalRing.maximalIdeal A))
    (hAc : IsAdicComplete (IsLocalRing.maximalIdeal A) A)
    {X X' : FppfSheaf B S hS} (hX : IsLocallyNoetherian B S hS X) (p : X ⟶ formalSpectrum D)
    (hp : IsLocallyOfFiniteType B S hS p) (ι : X' ⟶ X) (hιclosed : IsClosedImmersion B S hS ι)
    (hX'flat : IsFlat B S hS (ι ≫ p))
    (_hX'univ : ∀ (Y : FppfSheaf B S hS) (q : Y ⟶ X), IsLocallyNoetherian B S hS Y →
      IsFlat B S hS (q ≫ p) → ∃ r : Y ⟶ X', r ≫ ι = q)
    (hdiagE : IsRigEtale B S hS (pullback.diagonal p))
    (hdiagS : IsRigSurjective B S hS (pullback.diagonal p)) :
    IsIso (ι ≫ p) ∨ Nonempty (IsInitial X')
```

## Tag 0GDA, a lemma

[Tag 0GDA](https://stacks.math.columbia.edu/tag/0GDA) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSurjective_iff_factorsAdicCompleteDvrPoints_of_rigEtale_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveRigEtaleDiagonalCriterion.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveRigEtaleDiagonalCriterion.lean#L162). The attribute's comment: “The whole statement, under exactly the source's hypotheses.”.

> **Stacks 0GDA.** Let `f : X ⟶ Y` be a morphism of formal algebraic spaces over `S` with `X`
> and `Y` locally Noetherian, `f` locally of finite type, and the relative diagonal
> `Δ_f : X ⟶ X ×_Y X` rig-étale and rig-surjective. Then `f` is rig-surjective if and only if
> every adic morphism `Spf R ⟶ Y`, with `R` a complete discrete valuation ring, lifts to a
> morphism `Spf R ⟶ X`.

```lean
theorem isRigSurjective_iff_factorsAdicCompleteDvrPoints_of_rigEtale_diagonal
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hdiagEtale : IsRigEtale B S hS (pullback.diagonal f))
    (hdiagSurj : IsRigSurjective B S hS (pullback.diagonal f)) :
    IsRigSurjective B S hS f ↔ FactorsAdicCompleteDvrPoints B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.22, Tag 0GD7](https://stacks.math.columbia.edu/tag/0GD7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
