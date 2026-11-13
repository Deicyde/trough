---
declaration: section
origin: cited
lean: AlgebraicGeometry.derivedIso_koszulOfLift, AlgebraicGeometry.exists_koszulDescription_and_flat_quotient_of_fibrewise_koszul, Module.Flat.isRegular_and_flat_quotient_ofList_smul_of_isRegular_maximalIdeal, StacksDraft.Perfect.exists_away_koszul_description, AlgebraicGeometry.exists_isIso_baseChange_of_isIso_fiber, AlgebraicGeometry.exists_opens_nonempty_iso_constantFamily_of_isRelativeEquivalenceKernel, AlgebraicGeometry.exists_opens_iso_constantFamily_of_isRelativeEquivalenceKernel
statement: formalized
proof: formalized
---

# 57.16 No deformations

Section 57.16 of the Stacks Project, [Tag 0G0M](https://stacks.math.columbia.edu/tag/0G0M). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G0N, a lemma

[Tag 0G0N](https://stacks.math.columbia.edu/tag/0G0N) in the Stacks Project.

**`AlgebraicGeometry.derivedIso_koszulOfLift`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/NoDeformations/LiftedKoszul.lean, line 420](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/NoDeformations/LiftedKoszul.lean#L420). The attribute's comment: “lifted\_koszul”.

> The chosen finite-free lift of the closed-fibre Koszul complex represents the Koszul
> complex of its lifted first differential.

```lean
public lemma derivedIso_koszulOfLift
    (S : FlatLocalKoszulDeformationSituation.{u}) :
    letI : CommRing S.A := S.commRingA
    let I := Ideal.map (algebraMap S.R S.A) (IsLocalRing.maximalIdeal S.R)
    ∀ (P : CochainComplex (ModuleCat.{u} S.A) ℤ)
      (f : Fin S.r → S.A),
      Nonempty (DerivedCategory.Q.obj P ≅ S.K) →
      Nonempty
        (((ModuleCat.extendScalars (Ideal.Quotient.mk I)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj P ≅
          (Koszul.seqComplex S.residueSequence).extend ComplexShape.embeddingDownNat) →
      (∀ n : ℕ,
        Nonempty (P.X (-(n : ℤ)) ≅
          ModuleCat.of S.A (Fin (S.r.choose n) → S.A))) →
      (∀ i : ℤ, 0 < i → IsZero (P.X i)) →
      (∃ (e₀ : P.X 0 ≅ ModuleCat.of S.A S.A)
        (e₁ : P.X (-1) ≅ ModuleCat.of S.A (Fin S.r → S.A)),
        (∀ i, f i = e₀.hom.hom ((P.d (-1) 0).hom
          (e₁.inv.hom (Pi.single i 1)))) ∧
        (∀ i, Ideal.Quotient.mk I (f i) = S.residueSequence i)) →
      Nonempty
        (S.K ≅ DerivedCategory.Q.obj
          ((Koszul.seqComplex f).extend ComplexShape.embeddingDownNat))
```

**`AlgebraicGeometry.exists_koszulDescription_and_flat_quotient_of_fibrewise_koszul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/NoDeformations/LiftedKoszulExistence.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/NoDeformations/LiftedKoszulExistence.lean#L120). The attribute's comment: “The hypotheses are packaged as `FlatLocalKoszulDeformationSituation`. The Koszul complex is Mathlib's exterior-algebra complex `Koszul.seqComplex`, placed in cohomological degrees by `ComplexShape.embeddingDownNat`, and `K` is identified with its image under `DerivedCategory.Q`. The ideal `(f₁, …, f_r)` is `Ideal.span (Set.range f)` and "regular sequence" is Mathlib's `RingTheory.Sequence.IsRegular`, which is Definition 00LF verbatim.”.

> **The lifted sequence of [Stacks, Tag 0G0N] is regular with flat quotient.** In a flat local
> deformation situation `R → A` whose closed fibre is Koszul on the regular sequence `f̄`, there is a
> sequence `f` in `A` reducing to `f̄` modulo `𝔪_R A` which is regular in `A`, whose quotient
> `A/(f)` is flat over `R`, and whose Koszul complex represents the deformed perfect complex `K` in
> `D(A)`.

```lean
public theorem exists_koszulDescription_and_flat_quotient_of_fibrewise_koszul
    (S : FlatLocalKoszulDeformationSituation.{u}) :
    letI : CommRing S.A := S.commRingA
    let I := Ideal.map (algebraMap S.R S.A) (IsLocalRing.maximalIdeal S.R)
    ∃ f : Fin S.r → S.A,
      (∀ i, Ideal.Quotient.mk I (f i) = S.residueSequence i) ∧
        RingTheory.Sequence.IsRegular S.A (List.ofFn f) ∧
          Module.Flat S.R (S.A ⧸ Ideal.span (Set.range f)) ∧
            Nonempty (S.K ≅ DerivedCategory.Q.obj
              ((Koszul.seqComplex f).extend ComplexShape.embeddingDownNat))
```

Declarations registered for the tag:

- [`Module.Flat.isRegular_and_flat_quotient_ofList_smul_of_isRegular_maximalIdeal`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/RegularSequenceOverBase.lean#L173), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/NoDeformations/FlatQuotient.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/NoDeformations/FlatQuotient.lean#L31) (StacksFrontier): “flat\_quotient”.

## Tag 0G0P, a lemma

[Tag 0G0P](https://stacks.math.columbia.edu/tag/0G0P) in the Stacks Project.

**`StacksDraft.Perfect.exists_away_koszul_description`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/KoszulSpreadingOut.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/KoszulSpreadingOut.lean#L404).

> **Stacks Project, Tag 0G0P.** A local Koszul presentation of a perfect complex, with flat
> quotient, spreads to some principal neighbourhood of the prime.

```lean
theorem exists_away_koszul_description {R S : Type u} [CommRing R] [CommRing S] [Algebra R S]
    [IsNoetherianRing R] [IsNoetherianRing S] [Algebra.FiniteType R S] [Module.Flat R S]
    (q : Ideal S) [q.IsPrime]
    (K : DerivedCategory (ModuleCat.{u} S)) (hK : StacksDraft.Perfect.IsPerfect K)
    {r : ℕ} (f : Fin r → Localization.AtPrime q)
    (hf : RingTheory.Sequence.IsRegular (Localization.AtPrime q) (List.ofFn f))
    (hflat : Module.Flat R (Localization.AtPrime q ⧸ Ideal.span (Set.range f)))
    (hiso : Nonempty
      ((derivedExtensionScalarsGeneral.{u, u, u}
          (algebraMap S (Localization.AtPrime q))).functor.obj K ≅
        DerivedCategory.Q.obj
          ((Koszul.seqComplex f).extend ComplexShape.embeddingDownNat))) :
    ∃ (g : S) (hg : g ∉ q) (f' : Fin r → Localization.Away g),
      (∀ i, localizationAwayToAtPrime g q hg (f' i) = f i) ∧
      RingTheory.Sequence.IsRegular (Localization.Away g) (List.ofFn f') ∧
      Module.Flat R (Localization.Away g ⧸ Ideal.span (Set.range f')) ∧
      Nonempty
        ((derivedExtensionScalarsGeneral.{u, u, u}
            (algebraMap S (Localization.Away g))).functor.obj K ≅
          DerivedCategory.Q.obj
            ((Koszul.seqComplex f').extend ComplexShape.embeddingDownNat))
```

## Tag 0G0Q, a lemma

[Tag 0G0Q](https://stacks.math.columbia.edu/tag/0G0Q) in the Stacks Project.

**`AlgebraicGeometry.exists_isIso_baseChange_of_isIso_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/IsomorphismOnFibre.lean, line 450](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/IsomorphismOnFibre.lean#L450). References: EGA III (4.6.7), “(ii)”.

> **Stacks Project, Tag 0G0Q.** Let `X` and `Y` be proper over a Noetherian scheme `S`, with
> `X` flat over `S`. An `S`-morphism `X ⟶ Y` which is an isomorphism on the fibre at `s` is an
> isomorphism after base change to some open neighbourhood of `s`.

```lean
public theorem exists_isIso_baseChange_of_isIso_fiber
    {S : Scheme.{u}} [IsNoetherian S] {X Y : Over S} (p : X ⟶ Y)
    [IsProper X.hom] [IsProper Y.hom] [Flat X.hom] (s : S)
    [IsIso ((Over.pullback (S.fromSpecResidueField s)).map p).left] :
    ∃ U : S.Opens, s ∈ U ∧ IsIso ((Over.pullback U.ι).map p).left
```

## Tag 0G0R, a lemma

[Tag 0G0R](https://stacks.math.columbia.edu/tag/0G0R) in the Stacks Project.

**`AlgebraicGeometry.exists_opens_nonempty_iso_constantFamily_of_isRelativeEquivalenceKernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/NoDeformations/Rigidity.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/NoDeformations/Rigidity.lean#L288).

> **[Stacks, Tag 0G0R].** Let `k` be a field, `q : S ⟶ Spec k` of finite type, `s` a
> `k`-rational point of `S` (a section of `q`), and `g : Y ⟶ S` smooth and proper. Let
> `X = Y_s ×_k S` be the constant family with fibre `Y_s = Y ×_S Spec k`. If `K` is the Fourier-Mukai
> kernel of a relative equivalence from `X` to `Y` over `S` whose derived restriction along the
> comparison morphism `i : Y_s ×_k Y_s ⟶ X ×_S Y` is the diagonal kernel `Δ_{Y_s/k,*}𝒪_{Y_s}`, then
> there is an open `U ⊆ S` containing the point `s` picks out with `Y|_U` isomorphic to `Y_s ×_k U`
> over `U`.

```lean
theorem exists_opens_nonempty_iso_constantFamily_of_isRelativeEquivalenceKernel
    (rational : s ≫ q = 𝟙 _)
    (K : DerivedCategory (Limits.pullback (constantFamilyπ q g s) g).Modules)
    (relEquiv : IsRelativeEquivalenceKernel (constantFamilyπ q g s) g K)
    (restrict : Nonempty ((derivedPullback
        (fibreSquareToProductComparison q g s rational).toLRSHom.toShHom).obj K ≅
      diagonalKernel (fibreAtRationalPointπ g s))) :
    ∃ U : S.Opens, Set.range s.base ⊆ (U : Set S) ∧
      Nonempty ((Over.pullback U.ι).obj (Over.mk g) ≅
        Over.mk (Limits.pullback.snd (fibreAtRationalPointπ g s) (U.ι ≫ q)))
```

## Tag 0G0S, a lemma

[Tag 0G0S](https://stacks.math.columbia.edu/tag/0G0S) in the Stacks Project.

**`AlgebraicGeometry.exists_opens_iso_constantFamily_of_isRelativeEquivalenceKernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/NoDeformations/LocalTriviality.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/NoDeformations/LocalTriviality.lean#L242).

> **[Stacks, Tag 0G0S].** Let `k` be algebraically closed, `X ⟶ Spec k`
> smooth and proper, `g : Y ⟶ S` smooth and proper with `S` of finite type over `k`, and `K` the
> Fourier-Mukai kernel of a relative equivalence from `X ×_k S` to `Y` over `S`. Then every point of
> `S` has an open neighbourhood `U` over which `Y` is the constant family `Y₀ ×_k U` of some smooth
> proper `Y₀` over `k`.
>
> At each `k`-rational point `s` this is `exists_opens_iso_constantFamily_of_rationalPoint` with
> `Y₀ = Y_s`, smooth and proper as a base change of `g`; the opens so obtained cover `S` by
> `AlgebraicGeometry.exists_mem_opens_of_rationalPoints` (`S` is Jacobson and its closed points
> are `k`-rational).

```lean
theorem exists_opens_iso_constantFamily_of_isRelativeEquivalenceKernel [IsAlgClosed k]
    (K : DerivedCategory (pullback (pullback.snd a q) g).Modules)
    (hK : IsRelativeEquivalenceKernel (pullback.snd a q) g K) :
    ∀ x : S, ∃ U : S.Opens, x ∈ U ∧ ∃ Y₀ : Over (Spec (.of k)),
      Smooth Y₀.hom ∧ IsProper Y₀.hom ∧
        Nonempty ((Over.pullback U.ι).obj (Over.mk g) ≅ (Over.pullback (U.ι ≫ q)).obj Y₀)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.16, Tag 0G0M](https://stacks.math.columbia.edu/tag/0G0M)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
