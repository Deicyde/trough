---
declaration: section
origin: cited
lean: Stacks.Duality.isDualizingComplex_iff_exists_affineOpenCover, Stacks.Duality.IsDualizingComplex, AlgebraicGeometry.isIso_affineDerivedTildeHomComparison_of_finite_homology, AlgebraicGeometry.isIso_affineDerivedTildeHomComparison, Stacks.SheafOfModules.derivedSheafHomEvaluation_isIso_of_boundedCoherent, Stacks.SheafOfModules.derivedSheafHomEvaluation_isIso_of_coherent_finiteTorDimension, Stacks.Duality.dualizingDerivedSheafHomFunctor, Stacks.Duality.dualizingDerivedSheafHomBiduality
statement: formalized
proof: formalized
---

# 48.2 Dualizing complexes on schemes

Section 48.2 of the Stacks Project, [Tag 0A85](https://stacks.math.columbia.edu/tag/0A85). 8 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A86, a lemma

[Tag 0A86](https://stacks.math.columbia.edu/tag/0A86) in the Stacks Project.

**`Stacks.Duality.isDualizingComplex_iff_exists_affineOpenCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexCoverCriterion.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexCoverCriterion.lean#L414).

> **Stacks Project, Tag 0A86.** On a locally Noetherian scheme an object of `D(𝒪_X)` is a
> dualizing complex — it carries a dualizing model at every affine open — exactly when it carries
> one at the members of a single affine open cover.

```lean
theorem isDualizingComplex_iff_exists_affineOpenCover {K : DerivedCategory X.Modules} :
    IsDualizingComplex K ↔
      ∃ (ι : Type u) (U : ι → X.Opens) (hU : ∀ i, IsAffineOpen (U i)),
        (⨆ i, U i = ⊤) ∧ ∀ i, HasDualizingModelOn K (U i) (hU i)
```

## Tag 0A87, a definition

[Tag 0A87](https://stacks.math.columbia.edu/tag/0A87) in the Stacks Project.

**`Stacks.Duality.IsDualizingComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexScheme.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexScheme.lean#L113).

> **Stacks Project, Tag 0A87.** A *dualizing complex* on a locally Noetherian scheme `X` is an
> object of `D(𝒪_X)` which, over every affine open `U ⊆ X`, is the associated sheaf of a dualizing
> complex over `Γ(X, U)`.
>
> By [Stacks, Tag 0A86] it is enough to check this on the members of a single affine open cover.

```lean
abbrev IsDualizingComplex (K : DerivedCategory X.Modules) : Prop
```

## Tag 0A88, a lemma

[Tag 0A88](https://stacks.math.columbia.edu/tag/0A88) in the Stacks Project.

**`AlgebraicGeometry.isIso_affineDerivedTildeHomComparison_of_finite_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineCoherentHomFiniteInjectiveDimension.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineCoherentHomFiniteInjectiveDimension.lean#L171).

> **Stacks Tag 0A88.** Let `R` be a Noetherian ring and `X = Spec R`. For `K` an object of
> `D_Coh(R)` — all of whose cohomology modules are finite, with no boundedness hypothesis — and `L`
> an object of `D(R)` of finite injective dimension, the canonical comparison
>
> `(R Hom_R(K, L))~ ⟶ R𝓗om_{𝒪_X}(K̃, L̃)`
>
> is an isomorphism, which is the asserted equality of the two objects in `D(𝒪_X)`.

```lean
theorem isIso_affineDerivedTildeHomComparison_of_finite_homology (R : CommRingCat.{u})
    [IsNoetherianRing R] (K L : DerivedCategory (ModuleCat.{u} R))
    (hK : ∀ i : ℤ, Module.Finite R
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) i).obj K))
    (hL : StacksDraft.InjectiveDimension.HasFiniteInjectiveDimension L) :
    IsIso (affineDerivedTildeHomComparison R K L)
```

**`AlgebraicGeometry.isIso_affineDerivedTildeHomComparison`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedHom/Comparison.lean, line 667](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedHom/Comparison.lean#L667). The attribute's comment: “proved for K perfect and L arbitrary over any R, rather than for K in D\_Coh(R) and L of finite injective dimension over a Noetherian R; the comparison is the canonical morphism, identified as such by affineDerivedTildeHomComparison\_perfect”.

> **Stacks Tag 0A88, for a perfect source.** For `X = Spec R` and `K, L` in `D(R)` the
> canonical comparison
>
> `R SheafHom_{O_X}(K̃, L̃) ⟶ (R Hom_R(K, L))̃`
>
> is invertible when `K` is perfect, with no hypothesis on `L`. This is the conclusion of Tag 0A88
> — that the two objects agree in `D(O_X)` — read for the canonical morphism between them, which
> is what `affineDerivedTildeHomComparison_perfect` identifies it as.
>
> The source's hypotheses are `K` in `D_Coh(R)` and `L` of finite injective dimension, over a
> Noetherian `R`. The form proved here replaces the condition on `K` by perfectness and drops the
> condition on `L` and the Noetherian hypothesis on `R` altogether: the proof is the reduction of
> clause (3)(b) of Tag 0A6H to bounded finite-projective sources with K-injective targets, where
> both the comparison and the model isomorphism are the same five-fold composite, and that
> reduction asks nothing of `L`. Neither hypothesis set contains the other, so this is Tag 0A88 in
> the form this development's proof supports rather than in the source's form.

```lean
public lemma isIso_affineDerivedTildeHomComparison (R : CommRingCat.{u})
    (K L : DerivedCategory (ModuleCat.{u} R))
    (hK : StacksDraft.Perfect.IsPerfect K) :
    IsIso (affineDerivedTildeHomComparison R K L)
```

## Tag 0G4I, a lemma

[Tag 0G4I](https://stacks.math.columbia.edu/tag/0G4I) in the Stacks Project.

**`Stacks.SheafOfModules.derivedSheafHomEvaluation_isIso_of_boundedCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InternalHomEvaluation/CoherentEvaluation.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InternalHomEvaluation/CoherentEvaluation.lean#L187). The attribute's comment: “case (1): on a Noetherian scheme, K bounded above with coherent cohomology, L bounded below with coherent cohomology, all three in D\_QCoh, M of finite injective dimension affine locally”.

> Let `X` be a Noetherian scheme and let `K`, `L`, `M` be objects of `D_QCoh(O_X)` with
> `K ∈ D^-_Coh(O_X)`, `L ∈ D^+_Coh(O_X)` and `M` of finite injective dimension affine locally. Then
> the evaluation morphism
>
> `RSheafHom(L, M) ⊗^L_{O_X} K ⟶ RSheafHom(RSheafHom(K, L), M)`
>
> of [Stacks, Tag 0A8U] is an isomorphism.

```lean
theorem derivedSheafHomEvaluation_isIso_of_boundedCoherent [IsNoetherian X]
    (K L M : DerivedCategory (StructureSheafModules X.sheaf))
    (h : IsBoundedCoherentTriple X K L M) :
    IsIso (derivedSheafHomEvaluation X.sheaf K L M)
```

**`Stacks.SheafOfModules.derivedSheafHomEvaluation_isIso_of_coherent_finiteTorDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InternalHomEvaluation/CoherentEvaluation.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InternalHomEvaluation/CoherentEvaluation.lean#L209). The attribute's comment: “case (2): on a Noetherian scheme, K and L with coherent cohomology, all three in D\_QCoh, RSheafHom(L, M) of finite tor dimension, L and M of finite injective dimension affine locally”.

> Let `X` be a Noetherian scheme and let `K`, `L`, `M` be objects of `D_QCoh(O_X)` with `K`
> and `L` in `D_Coh(O_X)`, with `RSheafHom(L, M)` of finite tor dimension, and with `L` and `M` of
> finite injective dimension affine locally. Then the evaluation morphism
>
> `RSheafHom(L, M) ⊗^L_{O_X} K ⟶ RSheafHom(RSheafHom(K, L), M)`
>
> of [Stacks, Tag 0A8U] is an isomorphism.

```lean
theorem derivedSheafHomEvaluation_isIso_of_coherent_finiteTorDimension [IsNoetherian X]
    (K L M : DerivedCategory (StructureSheafModules X.sheaf))
    (h : IsCoherentFiniteTorTriple X K L M) :
    IsIso (derivedSheafHomEvaluation X.sheaf K L M)
```

## Tag 0A89, a lemma

[Tag 0A89](https://stacks.math.columbia.edu/tag/0A89) in the Stacks Project.

**`Stacks.Duality.dualizingDerivedSheafHomFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDuality.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDuality.lean#L267). The attribute's comment: “the functor D = R SheafHom(-, K) on D(O\_X)”. References: SGA 5 III (6.2), “partial”.

> **Stacks Project, Tag 0A89.** The functor `D = R𝓗om_{𝒪_X}(-, K)` of the lemma: derived
> internal Hom into `K` as a contravariant functor `D(𝒪_X)ᵒᵖ ⥤ D(𝒪_X)` on a scheme.
>
> As on the affine side (`Dualizing.dualizingDerivedHomFunctor`, which carries the corresponding
> fragment of [Stacks, Tag 0A7C]) it is defined for an arbitrary `K`; that `K` be a dualizing
> complex is what makes `D` an anti-equivalence of `D_Coh(𝒪_X)`, a separate assertion of the tag,
> which is `Stacks.Duality.coherentDualizingDerivedSheafHom_isEquivalence` — see the section
> "Where the rest of Tag 0A89 lives" above.

```lean
def dualizingDerivedSheafHomFunctor :
    (DerivedCategory X.Modules)ᵒᵖ ⥤ DerivedCategory X.Modules
```

**`Stacks.Duality.dualizingDerivedSheafHomBiduality`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDuality.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDuality.lean#L291). The attribute's comment: “the canonical biduality morphism id → D ∘ D”.

> **Stacks Project, Tag 0A89.** The canonical morphism `id → D ∘ D` of the lemma, for
> `D = R𝓗om_{𝒪_X}(-, K)` on a scheme: the natural transformation
> `𝟭 ⟶ opOp ⋙ D.op ⋙ D` whose component at `L` is the biduality morphism
>
> `L ⟶ R𝓗om_{𝒪_X}(R𝓗om_{𝒪_X}(L, K), K)`
>
> of `Stacks.SheafOfModules.derivedSheafHomBidualMap`.
>
> Here the morphism is constructed, for an arbitrary `K`, exactly as `Dualizing.derivedBiduality`
> constructs the affine one; that it is an isomorphism at every object of `D_Coh(𝒪_X)` is
> `Stacks.Duality.isIso_dualizingDerivedSheafHomBiduality_app`, the counterpart of
> `Dualizing.dualizingDerivedHom_biduality_isIso`.

```lean
def dualizingDerivedSheafHomBiduality :
    Functor.id (DerivedCategory X.Modules) ⟶
      opOp (DerivedCategory X.Modules) ⋙ (dualizingDerivedSheafHomFunctor X K).op ⋙
        dualizingDerivedSheafHomFunctor X K
```

**`Stacks.Duality.isIso_dualizingDerivedSheafHomBiduality_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDualityBiduality.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDualityBiduality.lean#L157). The attribute's comment: “canonical biduality”.

> **Stacks Project, Tag 0A89.** The canonical biduality morphism
>
> `L ⟶ R𝓗om_{𝒪_X}(R𝓗om_{𝒪_X}(L, K), K)`
>
> is an isomorphism, for `K` a dualizing complex on a locally Noetherian scheme `X` and `L` an
> object of `D_Coh(𝒪_X)`.
>
> The morphism is the left unitor read backwards, the homothety of `K` whiskered by `L`, and the
> derived evaluation morphism of [Stacks, Tag 0A8U] at `(L, K, K)`
> (`Stacks.SheafOfModules.isIso_derivedSheafHomBidualMap`). The homothety of a dualizing complex
> is invertible (`Stacks.Duality.isIso_derivedSheafHomothety_of_isDualizingComplex`), and the
> evaluation morphism is invertible at a source with coherent cohomology sheaves
> (`Stacks.Duality.isIso_derivedSheafHomEvaluation_of_isDualizingComplex`).

```lean
theorem isIso_dualizingDerivedSheafHomBiduality_app [IsLocallyNoetherian X]
    {K : DerivedCategory X.Modules} (hK : IsDualizingComplex K) (L : DerivedCategory X.Modules)
    (hL : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj L).IsCoherent) :
    IsIso ((dualizingDerivedSheafHomBiduality X K).app L)
```

**`Stacks.Duality.coherentDualizingDerivedSheafHom_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDualityBiduality.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDualityBiduality.lean#L213). The attribute's comment: “the anti-equivalence on coherent objects”.

> **Stacks Project, Tag 0A89.** `D = R𝓗om_{𝒪_X}(-, K)` is an anti-equivalence of
> `D_Coh(𝒪_X)`, for `K` a dualizing complex on a locally Noetherian scheme `X`: canonical
> biduality is a natural isomorphism, and a contravariant functor whose square is naturally
> isomorphic to the identity is an equivalence.

```lean
theorem coherentDualizingDerivedSheafHom_isEquivalence (X : Scheme.{u}) [IsLocallyNoetherian X]
    {K : DerivedCategory X.Modules} (hK : IsDualizingComplex K) :
    (coherentDualizingDerivedSheafHomFunctor X hK).IsEquivalence
```

**`Stacks.Duality.boundedCoherentDualizingDerivedSheafHom_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDualityBiduality.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDualityBiduality.lean#L280). The attribute's comment: “the bounded anti-equivalence”.

> **Stacks Project, Tag 0A89.** `D = R𝓗om_{𝒪_X}(-, K)` is an anti-equivalence of
> `D^b_Coh(𝒪_X)`, for `K` a dualizing complex on a quasi-compact locally Noetherian scheme `X`.

```lean
theorem boundedCoherentDualizingDerivedSheafHom_isEquivalence (X : Scheme.{u})
    [IsLocallyNoetherian X] [CompactSpace X] {K : DerivedCategory X.Modules}
    (hK : IsDualizingComplex K) :
    (boundedCoherentDualizingDerivedSheafHomFunctor X hK).IsEquivalence
```

**`Stacks.Duality.derivedCategoryBMinus_isCoherent_dualizingDerivedSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDualityBounded.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDualityBounded.lean#L284). The attribute's comment: “exchange of bounded below and bounded above”.

> On a quasi-compact locally Noetherian scheme, `D = R𝓗om_{𝒪_X}(-, K)` carries `D⁺_Coh(𝒪_X)`
> into `D⁻_Coh(𝒪_X)`, for `K` a dualizing complex.

```lean
theorem derivedCategoryBMinus_isCoherent_dualizingDerivedSheafHom [CompactSpace X]
    {K : DerivedCategory X.Modules} (hK : IsDualizingComplex K)
    (L : DerivedCategory X.Modules)
    (hL : DerivedCategoryB.derivedCategoryBPlus (A := X.Modules) (isCoherentSheaf X) L) :
    DerivedCategoryB.derivedCategoryBMinus (A := X.Modules) (isCoherentSheaf X)
      ((dualizingDerivedSheafHomFunctor X K).obj (op L))
```

**`Stacks.Duality.derivedCategoryBPlus_isCoherent_dualizingDerivedSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDualityBounded.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDualityBounded.lean#L302). The attribute's comment: “exchange of bounded above and bounded below”.

> On a quasi-compact locally Noetherian scheme, `D = R𝓗om_{𝒪_X}(-, K)` carries `D⁻_Coh(𝒪_X)`
> into `D⁺_Coh(𝒪_X)`, for `K` a dualizing complex.
>
> Together with `Stacks.Duality.derivedCategoryBMinus_isCoherent_dualizingDerivedSheafHom` this is
> the assertion that `D` **exchanges** the two subcategories.

```lean
theorem derivedCategoryBPlus_isCoherent_dualizingDerivedSheafHom [CompactSpace X]
    {K : DerivedCategory X.Modules} (hK : IsDualizingComplex K)
    (L : DerivedCategory X.Modules)
    (hL : DerivedCategoryB.derivedCategoryBMinus (A := X.Modules) (isCoherentSheaf X) L) :
    DerivedCategoryB.derivedCategoryBPlus (A := X.Modules) (isCoherentSheaf X)
      ((dualizingDerivedSheafHomFunctor X K).obj (op L))
```

**`Stacks.Duality.derivedCategoryBBounded_isCoherent_dualizingDerivedSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDualityBounded.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDualityBounded.lean#L323). The attribute's comment: “preservation of bounded coherent objects”.

> On a quasi-compact locally Noetherian scheme, `D = R𝓗om_{𝒪_X}(-, K)` carries
> `D^b_Coh(𝒪_X)` into itself, for `K` a dualizing complex.
>
> This is the preservation statement, the counterpart of the
> `"preservation of bounded coherent objects"` fragment of the affine decomposition of
> [Stacks, Tag 0A7C]; it is what makes `D` a functor on `D^b_Coh(𝒪_X)`, and the anti-equivalence
> the tag asserts there is
> `Stacks.Duality.boundedCoherentDualizingDerivedSheafHom_isEquivalence`.

```lean
theorem derivedCategoryBBounded_isCoherent_dualizingDerivedSheafHom [CompactSpace X]
    {K : DerivedCategory X.Modules} (hK : IsDualizingComplex K)
    (L : DerivedCategory X.Modules)
    (hL : DerivedCategoryB.derivedCategoryBBounded (A := X.Modules) (isCoherentSheaf X) L) :
    DerivedCategoryB.derivedCategoryBBounded (A := X.Modules) (isCoherentSheaf X)
      ((dualizingDerivedSheafHomFunctor X K).obj (op L))
```

**`Stacks.Duality.derivedCategoryB_isCoherent_dualizingDerivedSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDualityCoherence.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedDualityCoherence.lean#L228). The attribute's comment: “preservation of coherent objects”.

> **Stacks Project, Tag 0A89.** `D = R𝓗om_{𝒪_X}(-, K)` carries `D_Coh(𝒪_X)` into
> `D_Coh(𝒪_X)`, for `K` a dualizing complex on a locally Noetherian scheme `X`.
>
> This is the second assertion of the lemma, the one the anti-equivalence of `D_Coh(𝒪_X)` is
> phrased against. `D_Coh(𝒪_X)` is unbounded: the hypothesis on `L` and the conclusion are both
> membership in `DerivedCategoryB.derivedCategoryB (Stacks.Duality.isCoherentSheaf X)`, the
> `D_B(A)` construction of [Stacks, Tag 06UP] at coherence, which is what
> `Stacks.Duality.CoherentDerivedCategory` is the full subcategory on.

```lean
theorem derivedCategoryB_isCoherent_dualizingDerivedSheafHom
    (X : Scheme.{u}) [IsLocallyNoetherian X]
    {K : DerivedCategory X.Modules} (hK : IsDualizingComplex K)
    (L : DerivedCategory X.Modules)
    (hL : DerivedCategoryB.derivedCategoryB (A := X.Modules) (isCoherentSheaf X) L) :
    DerivedCategoryB.derivedCategoryB (A := X.Modules) (isCoherentSheaf X)
      ((dualizingDerivedSheafHomFunctor X K).obj (op L))
```

**`Stacks.Duality.mem_coherentDerivedCategory_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedSubcategory.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDerivedSubcategory.lean#L69). The attribute's comment: “K is an object of D\_Coh(O\_X)”.

> A dualizing complex on a locally Noetherian scheme is an object of `D_Coh(𝒪_X)`: every one of
> its cohomology sheaves is coherent.

```lean
theorem mem_coherentDerivedCategory_of_isDualizingComplex {K : DerivedCategory X.Modules}
    (hK : IsDualizingComplex K) :
    DerivedCategoryB.derivedCategoryB (A := X.Modules) (isCoherentSheaf X) K
```

**`Stacks.Duality.coherentDuality_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDuality.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDuality.lean#L226).

> Let `K` be a dualizing complex on a locally Noetherian scheme
> `X`. Then `K` is an object of `D_Coh(𝒪_X)`, and `D = R𝓗om(-, K)` carries `D_Coh(𝒪_X)` into itself
> and induces an anti-equivalence `D : D_Coh(𝒪_X) → D_Coh(𝒪_X)` which comes with the canonical
> isomorphism `id → D ∘ D`, the biduality morphisms `L → R𝓗om(R𝓗om(L, K), K)`. If `X` is
> quasi-compact, `D` exchanges `D^+_Coh(𝒪_X)` and `D^-_Coh(𝒪_X)` and induces an anti-equivalence
> `D^b_Coh(𝒪_X) → D^b_Coh(𝒪_X)`.

```lean
theorem coherentDuality_spec :
    DerivedCategoryB.derivedCategoryB (A := X.Modules) (isCoherentSheaf X) K ∧
    (∀ L : DerivedCategory X.Modules,
      DerivedCategoryB.derivedCategoryB (A := X.Modules) (isCoherentSheaf X) L →
      DerivedCategoryB.derivedCategoryB (A := X.Modules) (isCoherentSheaf X)
        (((derivedSheafHom X.sheaf).obj (op L)).obj K)) ∧
    (coherentDuality X hK).IsEquivalence ∧
    IsIso (coherentBiduality X hK) ∧
    (∀ [CompactSpace X],
      (∀ L : DerivedCategory X.Modules,
        DerivedCategoryB.derivedCategoryB (A := X.Modules) (isCoherentSheaf X) L →
        (DerivedCategoryB.IsBoundedBelow L ↔
          DerivedCategoryB.IsBoundedAbove (((derivedSheafHom X.sheaf).obj (op L)).obj K)) ∧
        (DerivedCategoryB.IsBoundedAbove L ↔
          DerivedCategoryB.IsBoundedBelow (((derivedSheafHom X.sheaf).obj (op L)).obj K))) ∧
      (boundedCoherentDuality X hK).IsEquivalence)
```

## Tag 0ATP, a lemma

[Tag 0ATP](https://stacks.math.columbia.edu/tag/0ATP) in the Stacks Project.

**`Stacks.Duality.exists_isInvertible_tensor_iso_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingComplexUniqueness.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingComplexUniqueness.lean#L140).

> **[Stacks, Tag 0ATP].** Let `X` be a locally Noetherian scheme and let `K`, `K'` be dualizing
> complexes on `X` ([Stacks, Tag 0A87]). Then `K'` is isomorphic to `K ⊗^𝐋_{𝒪_X} L` for some
> invertible object `L` of `D(𝒪_X)` ([Stacks, Tag 0FFN]), the monoidal structure being that of
> [Stacks, Tag 0FPT].
>
> The proof is the source's, with `L = R𝓗om_{𝒪_X}(K, K')`: `L` is invertible
> (`Stacks.Duality.isInvertible_derivedSheafHom_of_isDualizingComplex`) and the evaluation
> `L ⊗^𝐋 K ⟶ K'` is an isomorphism
> (`Stacks.Duality.isIso_derivedSheafHomCounit_of_isDualizingComplex`), both because they hold
> affine locally.

```lean
theorem exists_isInvertible_tensor_iso_of_isDualizingComplex [IsLocallyNoetherian X]
    (K K' : DerivedCategory X.Modules) (hK : IsDualizingComplex K)
    (hK' : IsDualizingComplex K') :
    letI := Scheme.Modules.derivedMonoidal X
    ∃ L : DerivedCategory X.Modules,
      MonoidalCategory.IsInvertible L ∧ Nonempty (K' ≅ K ⊗ L)
```

## Tag 0AWF, a lemma

[Tag 0AWF](https://stacks.math.columbia.edu/tag/0AWF) in the Stacks Project.

**`Stacks.Duality.isUniversallyCatenary_and_isDimensionFunction_associatedShiftFunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DerivedStalkModel.lean, line 532](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DerivedStalkModel.lean#L532).

> Let `X` be a locally Noetherian scheme and `K` a dualizing complex on `X`. Then `X` is
> universally catenary, and the function `δ : X → ℤ` defined by `x ↦ δ(x)` such that
> `ω^•_{X,x}⟦-δ(x)⟧` is a normalized dualizing complex over `𝒪_{X,x}` is a dimension function.
>
> Here `δ` is `Stacks.Duality.associatedShiftFunction K`, and `ω^•_{X,x}` is the derived stalk of
> `K` at `x`, computed degreewise on any complex `E` representing `K`
> (`Stacks.Duality.derivedStalkOfComplex`). The second conjunct says that `δ(x)` is *the* integer
> of the source: for every representative `E`, `ω^•_{X,x}⟦-n⟧` is a normalized dualizing complex
> exactly when `n = δ(x)`. The third says that `δ` is a dimension function.

```lean
theorem isUniversallyCatenary_and_isDimensionFunction_associatedShiftFunction
    [IsLocallyNoetherian X] {K : DerivedCategory X.Modules} (hK : IsDualizingComplex K) :
    AlgebraicGeometry.Scheme.IsUniversallyCatenary X ∧
      (∀ (x : X) (E : CochainComplex X.Modules ℤ), Nonempty (DerivedCategory.Q.obj E ≅ K) →
        ∀ n : ℤ, Dualizing.IsNormalizedDualizingComplex.{u, u} (A := X.presheaf.stalk x)
            ((derivedStalkOfComplex x E)⟦-n⟧) ↔ n = associatedShiftFunction K x) ∧
      ∃ d : TopologicalSpace.DimensionFunction X, ∀ x : X, d x = associatedShiftFunction K x
```

## Tag 0ECM, a lemma

[Tag 0ECM](https://stacks.math.columbia.edu/tag/0ECM) in the Stacks Project.

**`Stacks.Duality.extSheaf_stalk_degree_range_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafClauses.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafClauses.lean#L87). The attribute's comment: “clause (1): E^i\_x ≠ 0 → δ(x) ≤ i ≤ δ(x) + dim Supp(F\_x), for E^i the Ext sheaf Ext^\{-i}(F, K) of a dualizing complex K with its associated dimension function δ”.

> **Stacks Project, Tag 0ECM, clause (1).** For a coherent module `F` on a locally Noetherian
> scheme and a dualizing complex `K` with associated dimension function `δ`, a nonzero stalk of the
> Ext sheaf `𝓔ⁱ = 𝓔xt^{-i}(F, K)` at `x` forces `δ(x) ≤ i ≤ δ(x) + dim Supp(F_x)`; in particular that
> dimension is finite.

```lean
theorem extSheaf_stalk_degree_range_of_isDualizingComplex (F : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] {K : DerivedCategory X.Modules}
    (hK : IsDualizingComplex K) (x : X) (i : ℤ)
    (hi : Nontrivial ↑((extSheafOf F K i).presheaf.stalk x)) :
    associatedShiftFunction K x ≤ i ∧ ∃ d : ℕ,
      Module.supportDim ↑(X.presheaf.stalk x) ↑(F.presheaf.stalk x) = (d : WithBot ℕ∞) ∧
        i ≤ associatedShiftFunction K x + d
```

**`Stacks.Duality.supportDim_extSheaf_stalk_le_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafClauses.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafClauses.lean#L101). The attribute's comment: “clause (2): dim Supp(E^\{i + δ(x)}\_x) ≤ i, for E^i the Ext sheaf Ext^\{-i}(F, K) of a dualizing complex K with its associated dimension function δ”.

> **Stacks Project, Tag 0ECM, clause (2).** The stalk of `𝓔^{i + δ(x)}` at `x` has support of
> dimension at most `i`; for `i < 0` the bound is `⊥`, which says that the stalk vanishes.

```lean
theorem supportDim_extSheaf_stalk_le_of_isDualizingComplex (F : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] {K : DerivedCategory X.Modules}
    (hK : IsDualizingComplex K) (x : X) (i : ℤ) :
    Module.supportDim ↑(X.presheaf.stalk x)
        ↑((extSheafOf F K (i + associatedShiftFunction K x)).presheaf.stalk x) ≤
      if 0 ≤ i then ((i.toNat : ℕ∞) : WithBot ℕ∞) else ⊥
```

**`Stacks.Duality.depth_stalk_eq_iInf_nontrivial_extSheaf_stalk_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafClauses.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafClauses.lean#L114). The attribute's comment: “clause (3): depth(F\_x) = least i ≥ 0 with E^\{i + δ(x)}\_x ≠ 0, for E^i the Ext sheaf Ext^\{-i}(F, K) of a dualizing complex K with its associated dimension function δ”.

> **Stacks Project, Tag 0ECM, clause (3).** The depth of `F_x` is the least `i ≥ 0` for which the
> stalk of `𝓔^{i + δ(x)}` at `x` is nonzero. If all of these stalks vanish, both sides are `⊤`.

```lean
theorem depth_stalk_eq_iInf_nontrivial_extSheaf_stalk_of_isDualizingComplex (F : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] {K : DerivedCategory X.Modules}
    (hK : IsDualizingComplex K) (x : X) :
    Module.depth ↑(X.presheaf.stalk x) (IsLocalRing.maximalIdeal ↑(X.presheaf.stalk x))
        ↑(F.presheaf.stalk x) =
      ⨅ (k : ℕ) (_ : Nontrivial
        ↑((extSheafOf F K ((k : ℤ) + associatedShiftFunction K x)).presheaf.stalk x)), (k : ℕ∞)
```

**`Stacks.Duality.exists_nontrivial_extSheaf_stalk_iff_depth_add_le_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafClauses.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafClauses.lean#L129). The attribute's comment: “clause (4): x ∈ Supp(⊕\_\{j ≤ i} E^j) ↔ depth(F\_x) + δ(x) ≤ i, for E^i the Ext sheaf Ext^\{-i}(F, K) of a dualizing complex K with its associated dimension function δ”.

> **Stacks Project, Tag 0ECM, clause (4).** A point `x` lies in the support of `⨁_{j ≤ i} 𝓔^j` —
> that is, some `𝓔^j` with `j ≤ i` has nonzero stalk at `x` — exactly when the depth of `F_x` is
> finite and `depth(F_x) + δ(x) ≤ i`.

```lean
theorem exists_nontrivial_extSheaf_stalk_iff_depth_add_le_of_isDualizingComplex (F : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] {K : DerivedCategory X.Modules}
    (hK : IsDualizingComplex K) (x : X) (i : ℤ) :
    (∃ j : ℤ, j ≤ i ∧ Nontrivial ↑((extSheafOf F K j).presheaf.stalk x)) ↔
      ∃ n : ℕ, Module.depth ↑(X.presheaf.stalk x)
            (IsLocalRing.maximalIdeal ↑(X.presheaf.stalk x)) ↑(F.presheaf.stalk x) = (n : ℕ∞) ∧
          (n : ℤ) + associatedShiftFunction K x ≤ i
```

**`Stacks.Duality.isCoherent_extSheafOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafCoherent.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafCoherent.lean#L99). The attribute's comment: “the coherence assertion: for F coherent on a locally Noetherian scheme and K a dualizing complex, each Ext sheaf E^i = Ext^\{-i}(F, K) is a coherent O\_X-module”. References: SGA 6 I (3.7), “Clause b), special case”.

> **The first assertion of [Stacks, Tag 0ECM].** Let `X` be a locally Noetherian scheme, `K` a
> dualizing complex on `X` and `F` a coherent `𝒪_X`-module. Then every Ext sheaf
> `𝓔ⁱ = 𝓔xt^{-i}_{𝒪_X}(F, K)` is a coherent `𝒪_X`-module.

```lean
theorem isCoherent_extSheafOf (F : X.Modules) [hF : _root_.SheafOfModules.IsCoherent F]
    {K : DerivedCategory X.Modules} (hK : IsDualizingComplex K) (i : ℤ) :
    _root_.SheafOfModules.IsCoherent (extSheafOf F K i)
```

**`Stacks.Duality.extSheaf_stalk_degree_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafDepthDimension.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafDepthDimension.lean#L112). The attribute's comment: “clause (1): E^i\_x ≠ 0 → δ(x) ≤ i ≤ δ(x) + dim Supp(F\_x), given IsStalkwiseDualExt”.

> **Stacks Project, Tag 0ECM, clause (1).** For a coherent module `F` on a locally Noetherian
> scheme and a dualizing complex `K` with dimension function `δ`, a nonzero stalk of the Ext sheaf
> `𝓔ⁱ` at `x` forces `δ(x) ≤ i ≤ δ(x) + dim Supp(F_x)`; in particular that dimension is finite.

```lean
theorem extSheaf_stalk_degree_range (F : X.Modules) [_root_.SheafOfModules.IsCoherent F]
    (K : DerivedCategory X.Modules) (δ : X → ℤ) (E : ℤ → X.Modules)
    (hE : IsStalkwiseDualExt F K δ E) (x : X) (i : ℤ)
    (hi : Nontrivial ↑((E i).presheaf.stalk x)) :
    δ x ≤ i ∧ ∃ d : ℕ,
      Module.supportDim ↑(X.presheaf.stalk x) ↑(F.presheaf.stalk x) = (d : WithBot ℕ∞) ∧
        i ≤ δ x + d
```

**`Stacks.Duality.supportDim_extSheaf_stalk_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafDepthDimension.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafDepthDimension.lean#L130). The attribute's comment: “clause (2): dim Supp(E^\{i + δ(x)}\_x) ≤ i, given IsStalkwiseDualExt”.

> **Stacks Project, Tag 0ECM, clause (2).** The stalk of `𝓔^{i + δ(x)}` at `x` has support of
> dimension at most `i`; for `i < 0` the bound is `⊥`, which says that the stalk vanishes.

```lean
theorem supportDim_extSheaf_stalk_le (F : X.Modules) [_root_.SheafOfModules.IsCoherent F]
    (K : DerivedCategory X.Modules) (δ : X → ℤ) (E : ℤ → X.Modules)
    (hE : IsStalkwiseDualExt F K δ E) (x : X) (i : ℤ) :
    Module.supportDim ↑(X.presheaf.stalk x) ↑((E (i + δ x)).presheaf.stalk x) ≤
      if 0 ≤ i then ((i.toNat : ℕ∞) : WithBot ℕ∞) else ⊥
```

**`Stacks.Duality.depth_stalk_eq_iInf_nontrivial_extSheaf_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafDepthDimension.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafDepthDimension.lean#L145). The attribute's comment: “clause (3): depth(F\_x) = least i ≥ 0 with E^\{i + δ(x)}\_x ≠ 0, given IsStalkwiseDualExt”.

> **Stacks Project, Tag 0ECM, clause (3).** The depth of `F_x` is the least `i ≥ 0` for which
> the stalk of `𝓔^{i + δ(x)}` at `x` is nonzero.  If all of these stalks vanish, both sides are
> `⊤`.

```lean
theorem depth_stalk_eq_iInf_nontrivial_extSheaf_stalk (F : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] (K : DerivedCategory X.Modules) (δ : X → ℤ)
    (E : ℤ → X.Modules) (hE : IsStalkwiseDualExt F K δ E) (x : X) :
    Module.depth ↑(X.presheaf.stalk x) (IsLocalRing.maximalIdeal ↑(X.presheaf.stalk x))
        ↑(F.presheaf.stalk x) =
      ⨅ (k : ℕ) (_ : Nontrivial ↑((E ((k : ℤ) + δ x)).presheaf.stalk x)), (k : ℕ∞)
```

**`Stacks.Duality.exists_nontrivial_extSheaf_stalk_iff_depth_add_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafDepthDimension.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ExtSheafDepthDimension.lean#L166). The attribute's comment: “clause (4): x ∈ Supp(⊕\_\{j ≤ i} E^j) ↔ depth(F\_x) + δ(x) ≤ i, given IsStalkwiseDualExt”.

> **Stacks Project, Tag 0ECM, clause (4).** A point `x` lies in the support of
> `⨁_{j ≤ i} 𝓔^j` — that is, some `𝓔^j` with `j ≤ i` has nonzero stalk at `x` — exactly when the
> depth of `F_x` is finite and `depth(F_x) + δ(x) ≤ i`.

```lean
theorem exists_nontrivial_extSheaf_stalk_iff_depth_add_le (F : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] (K : DerivedCategory X.Modules) (δ : X → ℤ)
    (E : ℤ → X.Modules) (hE : IsStalkwiseDualExt F K δ E) (x : X) (i : ℤ) :
    (∃ j : ℤ, j ≤ i ∧ Nontrivial ↑((E j).presheaf.stalk x)) ↔
      ∃ n : ℕ, Module.depth ↑(X.presheaf.stalk x)
            (IsLocalRing.maximalIdeal ↑(X.presheaf.stalk x)) ↑(F.presheaf.stalk x) = (n : ℕ∞) ∧
          (n : ℤ) + δ x ≤ i
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.2, Tag 0A85](https://stacks.math.columbia.edu/tag/0A85)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
