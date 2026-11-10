---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.exists_flat_isClosedImmersion_of_isLocallyNoetherian, AlgebraicGeometry.FormalSpace.exists_flatPart_of_isLocallyNoetherian_of_isAdicComplete, AlgebraicGeometry.FormalSpace.isIso_or_isInitial_flatPart_of_isRigEtale_of_isRigSurjective_diagonal, AlgebraicGeometry.FormalSpace.factorsAdicCompleteDvrPoints_of_rigEtaleDiagonal, AlgebraicGeometry.FormalSpace.isRigSurjective_iff_factorsAdicCompleteDvrPoints_of_diagonal, AlgebraicGeometry.FormalSpace.isRigSurjective_iff_factorsAdicCompleteDvrPoints_of_rigEtale_diagonal
statement: formalized
proof: formalized
---

# 88.22 Formal algebraic spaces over cdvrs

Section 88.22 of the Stacks Project, [Tag 0GD7](https://stacks.math.columbia.edu/tag/0GD7). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GD8, a lemma

[Tag 0GD8](https://stacks.math.columbia.edu/tag/0GD8) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_flat_isClosedImmersion_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FlatPartOverCdvr.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FlatPartOverCdvr.lean#L415). The attribute's comment: “both halves of the conclusion — the closed immersion with `X'` flat over `A`, and the factorization of every locally Noetherian `Y ⟶ X` flat over `A` through it — with the five inputs this library does not carry as named hypotheses. `hpart` is the affine half as a statement about formal spectra: its ring-theoretic content, that the quotient of the presenting ring by its `A`-torsion is flat over `A` and receives every homomorphism into a flat `A`-algebra, is proved here as `Algebra.exists_flat_quotient_of_isDiscreteValuationRing`, while its geometric realization needs the adic Noetherian quotient topology, a `QuotientSystem` for the quotient, Stacks 0ANP for a closed immersion out of a surjective presenting homomorphism and Stacks 0GCD for flatness out of a flat one, none of which this library carries. `hdesc` is the gluing step, Stacks 02WW with Bootstrap 046J and Spaces 03KD, carried in this library only as the quotient sheaf of a relation with the étale-equivalence-relation hypothesis undischarged, 046J only conditionally on Stacks 0AMP and Stacks 0421, and 03KD only for presheaves of `Type u`. `hfac` is the descent of a factorization through a closed immersion along an affine étale covering, Stacks 03KD with the monomorphism property of Stacks 0AQB. `hrefine` is the covering of a test object by the charts of the fibre products with the atlas, which is Stacks 0AJ3, the refinement of Stacks 0AJ2, Stacks 0AQ8 and Stacks 0GCG. `hloc` bundles the four hypotheses of `isFlat_tfae`, this library's Stacks 0GCD, namely Stacks 0AJ3, the refinement of Stacks 0AJ2 and the locality axioms of Stacks 0GC9 read through Stacks 0AN8 and Stacks 0AN9. Completeness of `A` is carried for faithfulness; the source's argument uses only that `A` is a discrete valuation ring, and the ring-theoretic half proved here needs only that it is a Bézout domain”.

> **Stacks 0GD8.** Let `A` be a complete discrete valuation ring and let `X` be a locally
> Noetherian formal algebraic space over `S` with a structure morphism `p : X ⟶ Spf A`. Then
> there is a closed immersion `ι : X' ⟶ X` of formal algebraic spaces with `X'` locally
> Noetherian and flat over `A` such that every morphism `q : Y ⟶ X` with `Y` a locally
> Noetherian formal algebraic space flat over `A` factors through `ι`.
>
> The atlas of `X` supplied by the locally Noetherian hypothesis is turned into a family of
> affine flat parts by `hpart`; those are mutually compatible, since the universal property of
> one of them applies to any Noetherian affine formal algebraic space flat over `A` mapping to
> the corresponding chart, so they glue by `hdesc` to a closed immersion `ι : X' ⟶ X` whose
> sources form an affine étale covering of `X'`. That covering exhibits `X'` as locally
> Noetherian, and reading condition (4) of Stacks 0GCD on it gives flatness of `X'` over `A`.
> For the universal property, `hrefine` covers a test object `Y` by Noetherian affine formal
> algebraic spaces which are flat over `A` and map to the charts of `X`; each of them factors
> through the corresponding flat part and hence through `X'`, and `hfac` glues those
> factorizations.

```lean
theorem exists_flat_isClosedImmersion_of_isLocallyNoetherian
    [IsDomain A] [IsDiscreteValuationRing A] [IsNoetherianRing A]
    (_hAadic : TopologicalRing.IsAdic A)
    (_hAcomplete : IsAdicComplete (IsLocalRing.maximalIdeal A) A)
    (hSpfAaffine : IsAffineFormalAlgebraicSpace B S hS (formalSpectrum D))
    (hSpfA : IsFormalAlgebraicSpace B S hS (formalSpectrum D))
    {X : FppfSheaf B S hS} (hX : IsLocallyNoetherian B S hS X) (p : X ⟶ formalSpectrum D)
    (hpart : HasAffineFlatParts B S hS D p)
    (hdesc : FlatPartsDescend B S hS D p)
    (hfac : FactorizationDescendsAlongAffineEtaleCover B S hS)
    (hrefine : HasFlatAffineCoverOfFlat B S hS D p)
    (hloc : FlatnessLocalityInputs B S hS D) :
    ∃ (X' : FppfSheaf B S hS) (ι : X' ⟶ X),
      IsClosedImmersion B S hS ι ∧ IsLocallyNoetherian B S hS X' ∧
        IsFlat B S hS (ι ≫ p) ∧
        ∀ (Y : FppfSheaf B S hS) (q : Y ⟶ X), IsLocallyNoetherian B S hS Y →
          IsFlat B S hS (q ≫ p) → ∃ r : Y ⟶ X', r ≫ ι = q
```

**`AlgebraicGeometry.FormalSpace.exists_flatPart_of_isLocallyNoetherian_of_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FlatPartOverCdvrFull.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FlatPartOverCdvrFull.lean#L70).

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

**`AlgebraicGeometry.FormalSpace.isIso_or_isInitial_flatPart_of_isRigEtale_of_isRigSurjective_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FlatPartRigEtaleDiagonalUnconditional.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FlatPartRigEtaleDiagonalUnconditional.lean#L103).

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

**`AlgebraicGeometry.FormalSpace.factorsAdicCompleteDvrPoints_of_rigEtaleDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveRigEtaleDiagonal.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveRigEtaleDiagonal.lean#L318). The attribute's comment: “the complete discrete valuation ring lifting criterion is necessary for rig-surjectivity, granting Stacks 0AQ8, Stacks 0GD1 read through Stacks 0AQ3, Stacks 0AKY for the formal spectrum of a complete discrete valuation ring, Stacks 0GCD for an extension of such rings, and Stacks 0GD9 with Stacks 0GD8; see the module docstring for each”.

> **Stacks 0GDA**, the substantial direction, carrying five hypotheses. Let `f : X ⟶ Y` be a
> morphism of formal algebraic spaces over `S` with `X` locally Noetherian, `f` locally of finite
> type and `Δ_f : X ⟶ X ×_Y X` rig-étale and rig-surjective. If `f` is rig-surjective then every
> adic morphism `Spf R ⟶ Y`, with `R` a complete discrete valuation ring, lifts to `X` over `R`
> itself.
>
> Rig-surjectivity provides an extension `R ⊂ R'` of complete discrete valuation rings and a
> lift `Spf R' ⟶ X` of the point `p`. In the fibre product `W = Spf R ×_Y X` the projection
> `p₁ : W ⟶ Spf R` is locally of finite type by Stacks 0AQ5 and `W` is locally Noetherian by
> `h0AQ8`, which is Stacks 0AQ8; the relative diagonal `Δ_{p₁}` is a base change of `Δ_f` along
> the comparison morphism `W ×_{Spf R} W ⟶ X ×_Y X`, which is a base change of `p` and hence
> representable by algebraic spaces, so `Δ_{p₁}` is rig-étale by `h0GD1`, which is Stacks 0GD1,
> and rig-surjective by Stacks 0AQS. Hence `h0GD9`, which is Stacks 0GD9 together with Stacks
> 0GD8, gives the flat part `ι : W' ⟶ W` of `W` over `R` and the dichotomy. The lift
> `Spf R' ⟶ W` is flat over `R` by `hextFlat`, which is Stacks 0GCD, and `Spf R'` is locally
> Noetherian by `hSpfNoeth`, which is Stacks 0AKY, so the lift factors through `W'` and the
> second alternative of the dichotomy is impossible. Therefore `ι ≫ p₁` is an isomorphism and
> `inv (ι ≫ p₁) ≫ ι ≫ p₂` is the factorisation wanted.
>
> Local Noetherianity of `Y` is a hypothesis of Stacks 0GDA and is kept as `_hY`; the proof does
> not use it, obtaining local Noetherianity of `X ×_Y X` from that of `X` instead.

```lean
theorem factorsAdicCompleteDvrPoints_of_rigEtaleDiagonal
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (_hY : IsLocallyNoetherian B S hS Y)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hdiagEtale : IsRigEtale B S hS (pullback.diagonal f))
    (hdiagSurj : IsRigSurjective B S hS (pullback.diagonal f))
    (h0AQ8 : FibreProductIsLocallyNoetherian B S hS)
    (h0GD1 : RigEtaleIsStableUnderRepresentableBaseChange B S hS)
    (hSpfNoeth : FormalSpectrumOfCompleteDvrIsLocallyNoetherian B S hS)
    (hextFlat : FormalSpectrumMapOfDvrExtensionIsFlat B S hS)
    (h0GD9 : FlatPartOfRigEtaleDiagonalIsBaseOrPointless B S hS)
    (hrig : IsRigSurjective B S hS f) :
    FactorsAdicCompleteDvrPoints B S hS f
```

**`AlgebraicGeometry.FormalSpace.isRigSurjective_iff_factorsAdicCompleteDvrPoints_of_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveRigEtaleDiagonal.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveRigEtaleDiagonal.lean#L408). The attribute's comment: “granting Stacks 0AQ8, Stacks 0GD1 read through Stacks 0AQ3, Stacks 0AKY for the formal spectrum of a complete discrete valuation ring, Stacks 0GCD for an extension of such rings, and Stacks 0GD9 with Stacks 0GD8, all five used by the forward implication only; see the module docstring for each”.

> **Stacks 0GDA**, carrying five hypotheses. Let `f : X ⟶ Y` be a morphism of formal
> algebraic spaces over `S` with `X` and `Y` locally Noetherian, `f` locally of finite type and
> the relative diagonal `Δ_f : X ⟶ X ×_Y X` rig-étale and rig-surjective. Then `f` is
> rig-surjective if and only if every adic morphism `Spf R ⟶ Y`, with `R` a complete discrete
> valuation ring, lifts to a morphism `Spf R ⟶ X`.
>
> The direction the source calls trivial is
> `AlgebraicGeometry.FormalSpace.isRigSurjective_of_factorsAdicCompleteDvrPoints`, which needs
> none of the hypotheses. The five carried hypotheses are used by the other direction only; see
> the module docstring.

```lean
theorem isRigSurjective_iff_factorsAdicCompleteDvrPoints_of_diagonal
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hdiagEtale : IsRigEtale B S hS (pullback.diagonal f))
    (hdiagSurj : IsRigSurjective B S hS (pullback.diagonal f))
    (h0AQ8 : FibreProductIsLocallyNoetherian B S hS)
    (h0GD1 : RigEtaleIsStableUnderRepresentableBaseChange B S hS)
    (hSpfNoeth : FormalSpectrumOfCompleteDvrIsLocallyNoetherian B S hS)
    (hextFlat : FormalSpectrumMapOfDvrExtensionIsFlat B S hS)
    (h0GD9 : FlatPartOfRigEtaleDiagonalIsBaseOrPointless B S hS) :
    IsRigSurjective B S hS f ↔ FactorsAdicCompleteDvrPoints B S hS f
```

**`AlgebraicGeometry.FormalSpace.isRigSurjective_iff_factorsAdicCompleteDvrPoints_of_rigEtale_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveRigEtaleDiagonalCriterion.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveRigEtaleDiagonalCriterion.lean#L162).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
