---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.QuasicoherentDerivedCategory, AlgebraicGeometry.Space.quasicoherentDerivedComparisonSchemeUniverse, AlgebraicGeometry.Space.derivedQuasicoherent_tfae, AlgebraicGeometry.Space.hasCoproducts_quasicoherentDerivedCategory_ringUniverse, AlgebraicGeometry.Space.isLimit_cohomology_of_isDerivedLimit_of_epi, AlgebraicGeometry.Space.isDerivedLimit_single_limit_homology_unconditional, AlgebraicGeometry.Space.isZero_cohomology_limit_homology_of_isAffineChart_unconditional, AlgebraicGeometry.Space.derivedQuasicoherent_etaleModulePullback
statement: formalized
proof: formalized
---

# 75.5 Derived category of quasi-coherent modules

Section 75.5 of the Stacks Project, [Tag 071W](https://stacks.math.columbia.edu/tag/071W). 9 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 071X, a definition

[Tag 071X](https://stacks.math.columbia.edu/tag/071X) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasicoherentDerivedCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedCategory.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedCategory.lean#L66).

> **Stacks 071X.** The category `D_QCoh(𝒪_F)`: the full subcategory of the unbounded derived
> category of `𝒪_F`-modules whose objects have quasi-coherent cohomology sheaves in every
> degree.

```lean
noncomputable abbrev QuasicoherentDerivedCategory
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    [HasSheafify (smallEtaleRingedSite B S hS F hF).J AddCommGrpCat.{m}]
    [(smallEtaleRingedSite B S hS F hF).J.WEqualsLocallyBijective AddCommGrpCat.{m}]
```

## Tag 08F1, an equation

[Tag 08F1](https://stacks.math.columbia.edu/tag/08F1) in the Stacks Project.

**`AlgebraicGeometry.Space.quasicoherentDerivedComparisonSchemeUniverse`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedComparison.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedComparison.lean#L310).

> **Stacks 08F1**, the comparison functor `D(QCoh(𝒪_F)) ⥤ D_QCoh(𝒪_F)` of an algebraic space,
> with its `𝒪_F`-modules taken at the universe of the schemes, where the source assumes them.
>
> It has no open input.  What the functor needs of Properties of Spaces, Lemma 03M1 — the lemma
> Stacks 08F1 points at for the comparison to make sense — is the closure of quasi-coherence under
> kernels, under cokernels and under finite direct sums, and all three hold at this universe: the
> kernel clause is
> `AlgebraicGeometry.Space.isClosedUnderKernels_quasicoherentSheaves_schemeUniverse`, the cokernel
> clause is `AlgebraicGeometry.Space.isClosedUnderCokernels_quasicoherentSheaves`, and the
> direct-sum clause is the instance
> `SheafOfModules.isQuasicoherentOnSite_isClosedUnderFiniteProducts`.

```lean
noncomputable def quasicoherentDerivedComparisonSchemeUniverse :
    letI := isClosedUnderKernels_quasicoherentSheaves_schemeUniverse B S hS F hF
    letI := isClosedUnderCokernels_quasicoherentSheaves B S hS F hF
    DerivedCategory (QuasicoherentSheaves.{u, u} B S hS F hF) ⥤
      QuasicoherentDerivedCategory.{u, u} B S hS F hF
```

## Tag 08F2, a lemma

[Tag 08F2](https://stacks.math.columbia.edu/tag/08F2) in the Stacks Project.

**`AlgebraicGeometry.Space.derivedQuasicoherent_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedEtaleLocal.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedEtaleLocal.lean#L200).

> **Stacks 08F2.**  Let `E` be an object of `D(𝒪_X)` on an algebraic space `X`.  The following
> are equivalent: `E` lies in `D_QCoh(𝒪_X)`; `Lφ^*E` lies in `D_QCoh(𝒪_U)` for every étale scheme
> chart `φ : U → X` with `U` affine; the same for every étale scheme chart; the same for one étale
> scheme chart surjective on points; and `Lf^*E` lies in `D_QCoh(𝒪_Y)` for one étale morphism
> `f : Y ⟶ X` of algebraic spaces surjective on points.
>
> All five are the corresponding conditions of Stacks 03M0 applied to the cohomology sheaves of
> `E`, the passage between `Hⁿ(Lf^*E)` and `f^*(HⁿE)` being
> `AlgebraicGeometry.Space.derivedQuasicoherentPullback_iff`.

```lean
theorem derivedQuasicoherent_tfae (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) :
    List.TFAE
      [DerivedCategoryB.derivedCategoryB
          (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
            ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))) E,
        ∀ A : SmallEtale B S hS X.1,
          IsAffine ((BigFppfOver.toScheme B S hS).obj ((SmallEtale.toOver B S hS X.1).obj A)) →
          DerivedQuasicoherentPullback B S hS (chartToSpace B S hS X A)
            (isEtale_chartToSpace B S hS X A) E,
        ∀ A : SmallEtale B S hS X.1,
          DerivedQuasicoherentPullback B S hS (chartToSpace B S hS X A)
            (isEtale_chartToSpace B S hS X A) E,
        ∃ A : SmallEtale B S hS X.1, IsSurjective B S hS A.1.hom ∧
          DerivedQuasicoherentPullback B S hS (chartToSpace B S hS X A)
            (isEtale_chartToSpace B S hS X A) E,
        ∃ (Z : AlgebraicSpaces B S hS) (g : Z ⟶ X) (hg : IsEtale B S hS g.hom),
          IsSurjective B S hS g.hom ∧ DerivedQuasicoherentPullback B S hS g hg E]
```

## Tag 08F3, a lemma

[Tag 08F3](https://stacks.math.columbia.edu/tag/08F3) in the Stacks Project.

**`AlgebraicGeometry.Space.hasCoproducts_quasicoherentDerivedCategory_ringUniverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedDirectSums.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedDirectSums.lean#L173).

> **Stacks 08F3.**  Let `F` be an algebraic space over a scheme `S` contained in a big fppf
> site `B`.  Then `D_QCoh(𝒪_F)`, the derived category of `𝒪_F`-modules with quasi-coherent
> cohomology, has direct sums.
>
> The tag lands at the module universe `u` of the structure rings, because the `←` direction of
> Descent, Proposition 03DX(2) is available only there, and at a free module universe the
> direct-sum clause of Stacks 03M1 would have to be assumed instead of proved.
>
> This is `AlgebraicGeometry.Space.hasCoproducts_quasicoherentDerivedCategory` with its hypothesis
> discharged by `AlgebraicGeometry.Space.isQuasicoherentOnSite_sigma_of_h03DX`, fed with
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_iff_isCartesianOnAffineCharts`.

```lean
theorem hasCoproducts_quasicoherentDerivedCategory_ringUniverse :
    HasCoproducts.{u} (QuasicoherentDerivedCategory.{u, u} B S hS F hF)
```

## Tag 0D3E, a lemma

[Tag 0D3E](https://stacks.math.columbia.edu/tag/0D3E) in the Stacks Project.

**`AlgebraicGeometry.Space.isLimit_cohomology_of_isDerivedLimit_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedLimitsCohomology.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedLimitsCohomology.lean#L201). The attribute's comment: “clause (1): H^q(R lim K\_n) = lim H^q(K\_n), as the canonical limiting cone; the source's citation 0A09 is applied with its hypotheses on the affine étale charts of the space discharged (they cover the small étale site; a quasi-coherent module is acyclic on one; a surjection of quasi-coherent modules is surjective on its sections there). The module universe is the universe of the structure rings”.

> **Stacks Project, Tag 0D3E, clause (1).** Let `S` be a scheme, let `X` be an algebraic space
> over `S` and let `(K_n)` be an inverse system in `D_QCoh(𝒪_X)` whose transition maps
> `H^q(K_{n+1}) ⟶ H^q(K_n)` on cohomology sheaves are surjective.  If `L` is a derived inverse
> limit of the system then `H^q(L) = lim H^q(K_n)`: the cone on the degree-`q` cohomology sheaves
> whose legs are induced by the projections of a derived-limit triangle for `L` is a limit cone.
>
> This is Tag 0A09 —
> `Stacks.Cohomology.DerivedLimitAcyclic.LargeSite.isLimit_cohomology_of_isDerivedLimit`, its
> content with Tag 0BKZ supplied on a site whose objects live above its morphisms — on the small
> étale site of `X`, with the source's two checks on the
> affine objects of that site discharged: the affine étale charts cover it, and a quasi-coherent
> module both is acyclic on an affine chart and receives surjections on its sections there, which
> makes each tower of sections Mittag-Leffler and kills its first derived inverse limit.

```lean
theorem isLimit_cohomology_of_isDerivedLimit_of_epi
    (K : ℕᵒᵖ ⥤ DerivedCategory (Modules.{u, u} B S hS F hF))
    (hqc : ∀ (n : ℕ) (q : ℤ), ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS F hF) q).obj (K.obj ⟨n⟩)).IsQuasicoherentOnSite)
    (hsurj : ∀ (n : ℕ) (q : ℤ), Epi ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS F hF) q).map (K.map (homOfLE (Nat.le_succ n)).op)))
    (L : DerivedCategory (Modules.{u, u} B S hS F hF))
    (hL : IsDerivedLimit K L) (q : ℤ) :
    ∃ p : L ⟶ ∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩,
      (∃ δ : (∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
        Triangle.mk p (Pi.lift fun n : ℕ ↦
          Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n -
            Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) (n + 1) ≫
              K.map (homOfLE (Nat.le_succ n)).op) δ ∈
          distTriang (DerivedCategory (Modules.{u, u} B S hS F hF))) ∧
      ∃ τ : (Functor.const ℕᵒᵖ).obj
          ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS F hF) q).obj L) ⟶
          K ⋙ DerivedCategory.homologyFunctor (Modules.{u, u} B S hS F hF) q,
        (∀ n : ℕ, τ.app ⟨n⟩ =
          (DerivedCategory.homologyFunctor (Modules.{u, u} B S hS F hF) q).map
            (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n)) ∧
        Nonempty (IsLimit (Cone.mk _ τ))
```

**`AlgebraicGeometry.Space.isDerivedLimit_single_limit_homology_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedLimitsCohomology.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedLimitsCohomology.lean#L247). The attribute's comment: “clause (2): R lim H^q(K\_n) = lim H^q(K\_n); the source's citations are applied with their hypotheses on the affine étale charts of the space discharged (they cover the small étale site; a quasi-coherent module is acyclic on one; a surjection of quasi-coherent modules is surjective on its sections there). The module universe is the universe of the structure rings”.

> **Stacks Project, Tag 0D3E, clause (2).** Under the same hypotheses,
> `R lim H^q(K_n) = lim H^q(K_n)`: the ordinary inverse limit of the degree-`q` cohomology
> sheaves, placed in degree zero, is a derived inverse limit of the system of those sheaves.
>
> This is `AlgebraicGeometry.Space.isDerivedLimit_single_limit_homology` with its three named
> hypotheses supplied: `hcover` by
> `AlgebraicGeometry.Space.hasEnoughObjects_isAffineChart`, `h03DWab` by
> `AlgebraicGeometry.Space.isZero_rightDerived_sectionsFunctor_of_isAffineChart` and `h03DWepi` by
> `AlgebraicGeometry.Space.epi_sectionsFunctor_map_of_isQuasicoherentOnSite`.

```lean
theorem isDerivedLimit_single_limit_homology_unconditional
    (K : ℕᵒᵖ ⥤ DerivedCategory (Modules.{u, u} B S hS F hF))
    (hqc : ∀ (n : ℕ) (q : ℤ), ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS F hF) q).obj (K.obj ⟨n⟩)).IsQuasicoherentOnSite)
    (hsurj : ∀ (n : ℕ) (q : ℤ), Epi ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS F hF) q).map (K.map (homOfLE (Nat.le_succ n)).op)))
    (q : ℤ) :
    ∃ h : HasProduct (fun n : ℕ =>
        ((K ⋙ DerivedCategory.homologyFunctor (Modules.{u, u} B S hS F hF) q) ⋙
          DerivedCategory.singleFunctor (Modules.{u, u} B S hS F hF) 0).obj ⟨n⟩),
      @IsDerivedLimit (DerivedCategory (Modules.{u, u} B S hS F hF)) _ _ _ _ _ _
        ((K ⋙ DerivedCategory.homologyFunctor (Modules.{u, u} B S hS F hF) q) ⋙
          DerivedCategory.singleFunctor (Modules.{u, u} B S hS F hF) 0) h
        ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS F hF) 0).obj
          (limit (K ⋙ DerivedCategory.homologyFunctor
            (Modules.{u, u} B S hS F hF) q)))
```

**`AlgebraicGeometry.Space.isZero_cohomology_limit_homology_of_isAffineChart_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedLimitsCohomology.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedLimitsCohomology.lean#L283). The attribute's comment: “clause (3): H^p(U, lim H^q(K\_n)) = 0 for p > 0 and U an affine étale chart; the source's citations are applied with their hypotheses on the affine étale charts of the space discharged (they cover the small étale site; a quasi-coherent module is acyclic on one; a surjection of quasi-coherent modules is surjective on its sections there). The module universe is the universe of the structure rings”.

> **Stacks Project, Tag 0D3E, clause (3).** Under the same hypotheses, for every affine étale
> chart `U` of `X` and every `p > 0` we have `H^p(U, lim H^q(K_n)) = 0`.
>
> This is `AlgebraicGeometry.Space.isZero_cohomology_limit_homology_of_isAffineChart` with its
> three named hypotheses supplied, exactly as in
> `AlgebraicGeometry.Space.isDerivedLimit_single_limit_homology_unconditional`.  The source states
> the vanishing for an affine open of `X`; every affine open is an affine object of the small
> étale site, and the statement is given for all of them, as the source's own proof is.

```lean
theorem isZero_cohomology_limit_homology_of_isAffineChart_unconditional
    (K : ℕᵒᵖ ⥤ DerivedCategory (Modules.{u, u} B S hS F hF))
    (hqc : ∀ (n : ℕ) (q : ℤ), ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS F hF) q).obj (K.obj ⟨n⟩)).IsQuasicoherentOnSite)
    (hsurj : ∀ (n : ℕ) (q : ℤ), Epi ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS F hF) q).map (K.map (homOfLE (Nat.le_succ n)).op)))
    (q : ℤ) (U : SmallEtale B S hS F) (hU : IsAffineChart B S hS F U)
    (p : ℕ) (hp : 0 < p) :
    IsZero (((Stacks.Cohomology.SiteInverseLimits.sectionsFunctor
      (smallEtaleRingedSite B S hS F hF) U).rightDerived p).obj
      (limit (K ⋙ DerivedCategory.homologyFunctor
        (Modules.{u, u} B S hS F hF) q)))
```

## Tag 08F4, a lemma

[Tag 08F4](https://stacks.math.columbia.edu/tag/08F4) in the Stacks Project.

**`AlgebraicGeometry.Space.derivedQuasicoherent_etaleModulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedEtalePullback.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedEtalePullback.lean#L86). The attribute's comment: “for étale morphisms of algebraic spaces”.

> **Stacks 08F4 for an étale morphism of algebraic spaces.**  If `E` is an object of `D(𝒪_X)`
> all of whose cohomology sheaves are quasi-coherent and `f : Y ⟶ X` is étale, then every
> cohomology sheaf of `Lf^*E` is quasi-coherent.
>
> The étale pullback is exact, so `Hⁿ(Lf^*E) ≅ f^*(HⁿE)`, and `f^*` preserves quasi-coherence of a
> module by the `(1) ⟹ (2)` direction of Stacks 03M0.

```lean
theorem derivedQuasicoherent_etaleModulePullback (f : Y ⟶ X) (hf : IsEtale B S hS f.hom)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))) E) :
    DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O)))
      ((etaleModulePullback B S hS f hf).mapDerivedCategory.obj E)
```

**`AlgebraicGeometry.Space.quasicoherentDerivedEtalePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedEtalePullback.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedEtalePullback.lean#L103). The attribute's comment: “for étale morphisms of algebraic spaces, the restriction D\_QCoh(𝒪\_X) ⥤ D\_QCoh(𝒪\_Y)”.

> **Stacks 08F4 for an étale morphism of algebraic spaces, as a functor.**  The derived
> pullback along an étale morphism `f : Y ⟶ X` restricts to a functor
> `D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` between the derived categories of complexes with quasi-coherent
> cohomology.

```lean
noncomputable def quasicoherentDerivedEtalePullback (f : Y ⟶ X) (hf : IsEtale B S hS f.hom) :
    QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2 ⥤
      QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2
```

**`AlgebraicGeometry.Space.derivedQuasicoherent_smallEtaleDerivedModulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPullback.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPullback.lean#L188).

> Let `f : Y ⟶ X` be a morphism of algebraic spaces over `S`.  The derived pullback `Lf^*`,
> the total left derived functor `AlgebraicGeometry.Space.smallEtaleDerivedModulePullback` of
> degreewise pullback along the morphism of small étale ringed topoi of `f`, sends `D_QCoh(𝒪_X)`
> into `D_QCoh(𝒪_Y)`: if every cohomology sheaf of `E ∈ D(𝒪_X)` is quasi-coherent, then so is
> every cohomology sheaf of `Lf^*E`.

```lean
theorem derivedQuasicoherent_smallEtaleDerivedModulePullback (f : Y ⟶ X)
    (E : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hE : DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))) E) :
    DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O)))
      ((smallEtaleDerivedModulePullback B S hS f).obj E)
```

**`AlgebraicGeometry.Space.quasicoherentDerivedPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPullback.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPullback.lean#L227). The attribute's comment: “the restriction D\_QCoh(𝒪\_X) ⥤ D\_QCoh(𝒪\_Y) of Lf^*, for an arbitrary morphism”.

> The derived pullback `Lf^*` along an arbitrary morphism `f : Y ⟶ X` of algebraic spaces
> restricts to a functor `D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` between the full subcategories of complexes
> with quasi-coherent cohomology (Stacks 071X).

```lean
noncomputable def quasicoherentDerivedPullback (f : Y ⟶ X) :
    (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))) :
      ObjectProperty (DerivedCategory
        (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))).FullSubcategory ⥤
    (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O))) :
      ObjectProperty (DerivedCategory
        (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y)))).FullSubcategory
```

## Tag 08F5, a lemma

[Tag 08F5](https://stacks.math.columbia.edu/tag/08F5) in the Stacks Project.

**`AlgebraicGeometry.Space.derivedQuasicoherent_derivedTensor_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedTensor.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedTensor.lean#L321). The attribute's comment: “the case of two quasi-coherent modules placed in degree zero, the left one K-flat”.

> **Stacks 08F5 for two quasi-coherent modules placed in degree zero, the left one K-flat.**
> Let `X` be an algebraic space, let `T` be a derived tensor product on `𝒪_X`, and let `M` and `N`
> be quasi-coherent `𝒪_X`-modules with `M[0]` K-flat.  Then `M[0] ⊗^L_{𝒪_X} N[0]` lies in
> `D_QCoh(𝒪_X)`.
>
> Membership in `D_QCoh(𝒪_X)` is the object property `DerivedCategoryB.derivedCategoryB` for
> quasi-coherence that `AlgebraicGeometry.Space.QuasicoherentDerivedCategory` of Stacks 071X is
> the full subcategory on, so no new predicate appears.  The content is
> `Stacks.SheafOfModules.DerivedTensorProduct.isQuasicoherentOnSite_homology_tensor_single` on the
> small étale ringed site of `X`; the general case of Stacks 08F5 is not proved, and the module
> docstring records the four missing inputs.

```lean
theorem derivedQuasicoherent_derivedTensor_single
    (T : DerivedTensorProduct.{u + 1, u, u, d} (smallEtaleRingedSite B S hS F hF))
    (M N : Modules.{u, u} B S hS F hF)
    (hM : Stacks.SheafOfModules.IsKFlat (smallEtaleRingedSite B S hS F hF).O
      ((CochainComplex.singleFunctor (Modules.{u, u} B S hS F hF) 0).obj M))
    (hMq : M.IsQuasicoherentOnSite) (hNq : N.IsQuasicoherentOnSite) :
    DerivedCategoryB.derivedCategoryB
      (_root_.SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O)))
      ((T.tensor.obj
          ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS F hF) 0).obj M)).obj
        ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS F hF) 0).obj N))
```

**`AlgebraicGeometry.Space.derivedQuasicoherent_derivedTensor_single'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedTensor.lean, line 339](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedTensor.lean#L339). The attribute's comment: “the case of two quasi-coherent modules placed in degree zero, the right one K-flat”.

> **Stacks 08F5 for two quasi-coherent modules placed in degree zero, the right one K-flat.**
> The mirror of `AlgebraicGeometry.Space.derivedQuasicoherent_derivedTensor_single`, read through
> `Stacks.SheafOfModules.DerivedTensorProduct.isQuasicoherentOnSite_homology_tensor_single'`.

```lean
theorem derivedQuasicoherent_derivedTensor_single'
    (T : DerivedTensorProduct.{u + 1, u, u, d} (smallEtaleRingedSite B S hS F hF))
    (M N : Modules.{u, u} B S hS F hF)
    (hN : Stacks.SheafOfModules.IsKFlat (smallEtaleRingedSite B S hS F hF).O
      ((CochainComplex.singleFunctor (Modules.{u, u} B S hS F hF) 0).obj N))
    (hMq : M.IsQuasicoherentOnSite) (hNq : N.IsQuasicoherentOnSite) :
    DerivedCategoryB.derivedCategoryB
      (_root_.SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O)))
      ((T.tensor.obj
          ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS F hF) 0).obj M)).obj
        ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS F hF) 0).obj N))
```

**`AlgebraicGeometry.Space.derivedQuasicoherent_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedTensorArbitrary.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedTensorArbitrary.lean#L214).

> **Stacks 08F5.**  Let `X` be an algebraic space over a scheme `S`.  For objects `K`, `L` of
> `D_QCoh(𝒪_X)` the derived tensor product `K ⊗^𝐋_{𝒪_X} L` is in `D_QCoh(𝒪_X)`.
>
> Here `𝒪_X`-modules are the sheaves of modules on the small étale ringed site of `X`,
> `D_QCoh(𝒪_X)` is `AlgebraicGeometry.Space.QuasicoherentDerivedCategory` of Stacks 071X, the full
> subcategory of the unbounded derived category on the objects with quasi-coherent cohomology
> sheaves, and `⊗^𝐋_{𝒪_X}` is an arbitrary derived tensor product datum `T` on that ringed site —
> for instance the canonical one, `Stacks.SheafOfModules.canonicalDerivedTensorProduct` of
> Stacks 06YU.  `K` and `L` are arbitrary objects of `D_QCoh(𝒪_X)`, with no boundedness.
>
> The proof represents `K` by a K-flat complex `P` (Stacks 06YS) and `L` by any complex `L'`, so
> that `K ⊗^𝐋 L ≅ Q(Tot(P ⊗ L'))` by the K-flat comparison of `T`, and concludes by
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_homology_tensorComplex`; see the module docstring.

```lean
theorem derivedQuasicoherent_derivedTensor
    (T : Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, u + 1}
      (smallEtaleRingedSite B S hS F hF))
    (K L : QuasicoherentDerivedCategory.{u, u} B S hS F hF) :
    DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O)))
      ((T.tensor.obj K.obj).obj L.obj)
```

**`AlgebraicGeometry.Space.qcohDerived_smallEtaleDerivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedTensorClosed.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedTensorClosed.lean#L136).

> **Stacks 08F5.** Let `X` be an algebraic space over a scheme `S`. For objects `K`, `L` of
> `D_QCoh(𝒪_X)` the derived tensor product `K ⊗^L_{𝒪_X} L` is in `D_QCoh(𝒪_X)`.

```lean
theorem qcohDerived_smallEtaleDerivedTensor (X : AlgebraicSpaces B S hS)
    (K L : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hK : QcohDerived B S hS X K) (hL : QcohDerived B S hS X L) :
    QcohDerived B S hS X (((smallEtaleDerivedTensor B S hS X).obj K).obj L)
```

## Tag 08F6, a lemma

[Tag 08F6](https://stacks.math.columbia.edu/tag/08F6) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_of_isDerivedLimit_truncGETower_ringUniverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedLimitsCohomology.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedLimitsCohomology.lean#L316). The attribute's comment: “the source's statement: E in D\_QCoh is the derived limit of its truncations τ\_\{≥ -n} E. The source's two inputs are theorems of this library: the affine étale charts cover the small étale site (04JS) and a quasi-coherent module has no higher cohomology on an affine étale chart (the étale-site analogue of 01XB); the countable product of the tower exists in D(𝒪\_X). The module universe is the universe of the structure rings”.

> **Stacks Project, Tag 08F6.**  Let `S` be a scheme, let `X` be an algebraic space over `S` and
> let `E` be an object of `D_QCoh(𝒪_X)`.  Then the canonical map from `E` to a derived limit `L` of
> the tower `n ↦ τ_{≥ -n} E` of canonical truncations from below is an isomorphism.
>
> The derived limit is presented by its structural morphism `p` to the product of the tower together
> with the distinguished triangle `hL` characterising it, and the map `c` out of `E` is the canonical
> one because its composites with the product projections are required to be the truncation maps.
> The product exists by `AlgebraicGeometry.Space.hasProductsOfShape_nat_derivedCategory_modules`, so
> the only hypothesis is the quasi-coherence of the cohomology sheaves of `E`.

```lean
theorem isIso_of_isDerivedLimit_truncGETower_ringUniverse
    (E : DerivedCategory (Modules.{u, u} B S hS F hF))
    (hE : ∀ q : ℤ, ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS F hF) q).obj E).IsQuasicoherentOnSite)
    (L : DerivedCategory (Modules.{u, u} B S hS F hF))
    (c : E ⟶ L)
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower
      (Modules.{u, u} B S hS F hF) E).obj ⟨n⟩)
    (δ : (∏ᶜ fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower
      (Modules.{u, u} B S hS F hF) E).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧)
    (hL : Triangle.mk p (Pi.lift fun n : ℕ ↦
      Pi.π (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower
        (Modules.{u, u} B S hS F hF) E).obj ⟨n⟩) n -
        Pi.π (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower
          (Modules.{u, u} B S hS F hF) E).obj ⟨n⟩) (n + 1) ≫
          (Stacks.DerivedLimit.truncGETower
            (Modules.{u, u} B S hS F hF) E).map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (Modules.{u, u} B S hS F hF)))
    (hc : ∀ n : ℕ, c ≫ p ≫ Pi.π (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower
      (Modules.{u, u} B S hS F hF) E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) :
    IsIso c
```

## Tag 08F7, a lemma

[Tag 08F7](https://stacks.math.columbia.edu/tag/08F7) in the Stacks Project.

**`AlgebraicGeometry.Space.isZero_homology_rightDerived_of_isZero_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedFunctorAmplitude.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedFunctorAmplitude.lean#L132). The attribute's comment: “the i < a half of assertion (3); the upper bound b + N - 1, where the integer N and the hypotheses (2), (3) on F enter, is not proved — it needs the clause q > 0 of Stacks 03DW, which this repository does not carry”.

> **Stacks 08F7, the `i < a` half of assertion (3).** Let `S` be a scheme, let `X` be an
> algebraic space over `S`, let `F : Mod(𝒪_X) ⥤ Ab` be an additive functor and let `(RF, α)` be a
> right derived functor of `F` on `D(𝒪_X)`.  Let `E` be an object of `D_QCoh(𝒪_X)` with
> `H ^ j (E) = 0` for `j < a`.  Then `H ^ i (RF E) = 0` for `i < a`.
>
> This is the half of assertion (3) that bounds `RF E` from below.  The source gets it from
> assertion (1); here it is the left t-exactness of a right derived functor out of a Grothendieck
> abelian category with enough injectives,
> `Stacks.SmallDerivedCategory.isGE_obj_of_isGE`, which is Stacks 05TC part (1).
>
> Neither the quasi-coherence of `E`, nor the source's hypotheses (2) and (3) on `F`, nor the
> integer `N` is used: `N` governs only the upper bound `b + N - 1`, which is the other half of
> assertion (3).

```lean
theorem isZero_homology_rightDerived_of_isZero_lt
    (E : DerivedCategory (Modules.{u, m} B S hS X hX))
    (hqc : ∀ q : ℤ, ((DerivedCategory.homologyFunctor
      (Modules.{u, m} B S hS X hX) q).obj E).IsQuasicoherentOnSite)
    (a : ℤ)
    (hE : ∀ j : ℤ, j < a → IsZero ((DerivedCategory.homologyFunctor
      (Modules.{u, m} B S hS X hX) j).obj E))
    (i : ℤ) (hi : i < a) :
    IsZero ((DerivedCategory.homologyFunctor AddCommGrpCat.{m} i).obj (RF.obj E))
```

**`AlgebraicGeometry.Space.isIso_homologyFunctor_map_rightDerived_truncLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedFunctorAmplitude.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedFunctorAmplitude.lean#L165). The attribute's comment: “assertion (1), as the source proves it, by citing Derived Categories 05TC; the hypotheses (2), (3) on F and the integer N play no part in that assertion and are not binders”.

> **Stacks 08F7, assertion (1).** Let `S` be a scheme, let `X` be an algebraic space over `S`,
> let `F : Mod(𝒪_X) ⥤ Ab` be an additive functor and let `(RF, α)` be a right derived functor of
> `F` on `D(𝒪_X)`.  Then for every object `E` of `D_QCoh(𝒪_X)` and every `i ≤ a` the canonical
> truncation map `τ_{≤ a} E ⟶ E` induces an isomorphism
> `H ^ i (RF (τ_{≤ a} E)) ⟶ H ^ i (RF E)`.
>
> The argument is the source's, which cites Derived Categories, Lemma [Stacks, Tag 05TC].  The
> functor `RF` is triangulated, so it carries the canonical truncation triangle
> `τ_{≤ a} E ⟶ E ⟶ τ_{≥ a + 1} E` to a distinguished triangle; its third vertex lies in degrees
> `≥ a + 1` by left t-exactness of `RF`, so `H ^ i` and `H ^ (i - 1)` vanish on it for `i ≤ a`,
> and the long exact homology sequence makes the first map invertible on `H ^ i`.
>
> Neither the quasi-coherence of `E`, nor the source's hypotheses (2) and (3) on `F`, nor the
> integer `N` is used — none of them occurs in Tag 05TC either.

```lean
theorem isIso_homologyFunctor_map_rightDerived_truncLE
    (E : DerivedCategory (Modules.{u, m} B S hS X hX))
    (hqc : ∀ q : ℤ, ((DerivedCategory.homologyFunctor
      (Modules.{u, m} B S hS X hX) q).obj E).IsQuasicoherentOnSite)
    (a i : ℤ) (hi : i ≤ a) :
    IsIso ((DerivedCategory.homologyFunctor AddCommGrpCat.{m} i).map
      (RF.map ((DerivedCategory.TStructure.t.truncLEι a).app E)))
```

**`AlgebraicGeometry.Space.isZero_homology_rightDerived_of_isZero_gt_unbounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedFunctorAmplitudeUnbounded.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedFunctorAmplitudeUnbounded.lean#L448). The attribute's comment: “assertion (3), the upper bound b + N - 1, and the sole registration of that half: H^i(RF E) = 0 for i > b + N - 1 once H^j(E) = 0 for j > b, for every E of D\_QCoh with no boundedness hypothesis, so for a = -infinity too. Hypothesis (2) on F is the binder PreservesLimitsOfShape (Discrete N) F, hypothesis (3) is hRF, hypothesis (1) is unused”.

> **Stacks 08F7, assertion (3), the upper bound, for every `E` of `D_QCoh(𝒪_X)`.** Let `S` be a
> scheme, let `X` be an algebraic space over `S`, let `F : Mod(𝒪_X) ⥤ Ab` be an additive functor
> commuting with countable direct products and let `(RF, α)` be a right derived functor of `F` on
> `D(𝒪_X)`.  Let `N ≥ 0` be an integer such that `R^pF(ℱ) = 0` for every quasi-coherent `ℱ` and
> every `p ≥ N`, which is the source's hypothesis (3).  Let `E` be an object of `D_QCoh(𝒪_X)` with
> `H ^ j (E) = 0` for `j > b`.  Then `H ^ i (RF E) = 0` for `i > b + N - 1`.
>
> Nothing is assumed about the lower endpoint `a` of the source's range `-∞ ≤ a ≤ b ≤ ∞`, so this
> is the case `a = -∞` as well; the vanishing for `i < a` when `a` is finite is the other half of
> assertion (3) and is
> `AlgebraicGeometry.Space.isZero_homology_rightDerived_of_isZero_lt`.  The source's hypothesis (2)
> on `F` is the binder `[PreservesLimitsOfShape (Discrete ℕ) F]`; it is used, unlike in the bounded
> statements, because the proof passes through the derived limit `E = R lim τ_{≥ -n} E`.
>
> This is the sole registration of the upper bound of assertion (3); no form of that clause
> assuming in addition that `E` is bounded below is stated in the library, the bounded case being
> confined to the `private` ingredient
> `AlgebraicGeometry.Space.isLE_rightDerived_obj_of_bounded`.

```lean
theorem isZero_homology_rightDerived_of_isZero_gt_unbounded (N : ℕ)
    (hRF : ∀ M : Modules.{u, u} B S hS X hX, M.IsQuasicoherentOnSite →
      ∀ p : ℤ, (N : ℤ) ≤ p → IsZero ((F.rightDerivedPlus p).obj M))
    (E : DerivedCategory (Modules.{u, u} B S hS X hX))
    (hqc : ∀ q : ℤ, ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS X hX) q).obj E).IsQuasicoherentOnSite)
    (b : ℤ)
    (hEb : ∀ j : ℤ, b < j → IsZero ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS X hX) j).obj E))
    (i : ℤ) (hi : b + (N : ℤ) - 1 < i) :
    IsZero ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} i).obj (RF.obj E))
```

**`AlgebraicGeometry.Space.isIso_homologyFunctor_map_rightDerived_truncGE_unbounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedFunctorAmplitudeUnbounded.lean, line 486](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedFunctorAmplitudeUnbounded.lean#L486). The attribute's comment: “assertion (2), and the sole registration of it: H^i(RF E) -> H^i(RF(tau\_\{>= b - N + 1} E)) is an isomorphism for i >= b, for every E of D\_QCoh with no boundedness hypothesis. Hypothesis (2) on F is the binder PreservesLimitsOfShape (Discrete N) F, hypothesis (3) is hRF, hypothesis (1) is unused”.

> **Stacks 08F7, assertion (2), for every `E` of `D_QCoh(𝒪_X)`.** Let `S` be a scheme, let `X`
> be an algebraic space over `S`, let `F : Mod(𝒪_X) ⥤ Ab` be an additive functor commuting with
> countable direct products and let `(RF, α)` be a right derived functor of `F` on `D(𝒪_X)`.  Let
> `N ≥ 0` be an integer such that `R^pF(ℱ) = 0` for every quasi-coherent `ℱ` and every `p ≥ N`, the
> source's hypothesis (3).  Then for every object `E` of `D_QCoh(𝒪_X)` and every `i ≥ b` the
> canonical truncation map `E ⟶ τ_{≥ b - N + 1} E` induces an isomorphism
> `H ^ i (RF E) ⟶ H ^ i (RF (τ_{≥ b - N + 1} E))`.
>
> No boundedness hypothesis on `E` is made.  The canonical truncation triangle
> `τ_{≤ b - N} E ⟶ E ⟶ τ_{≥ b - N + 1} E` is carried by `RF` to a distinguished triangle, `RF`
> being triangulated; its first vertex lies in degrees `≤ b - 1` by
> `AlgebraicGeometry.Space.isLE_rightDerived_obj_of_isLE`, which needs no lower bound, so `H ^ i`
> and `H ^ (i + 1)` vanish on it for `i ≥ b`, and the long exact homology sequence makes the second
> map invertible on `H ^ i`.
>
> This is the sole registration of assertion (2); no form of it assuming in addition that `E` is
> bounded below is stated in the library, the bounded case being confined to the `private`
> ingredient `AlgebraicGeometry.Space.isLE_rightDerived_obj_of_bounded`.

```lean
theorem isIso_homologyFunctor_map_rightDerived_truncGE_unbounded (N : ℕ)
    (hRF : ∀ M : Modules.{u, u} B S hS X hX, M.IsQuasicoherentOnSite →
      ∀ p : ℤ, (N : ℤ) ≤ p → IsZero ((F.rightDerivedPlus p).obj M))
    (E : DerivedCategory (Modules.{u, u} B S hS X hX))
    (hqc : ∀ q : ℤ, ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS X hX) q).obj E).IsQuasicoherentOnSite)
    (b i : ℤ) (hi : b ≤ i) :
    IsIso ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} i).map
      (RF.map ((DerivedCategory.TStructure.t.truncGEπ (b - (N : ℤ) + 1)).app E)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.5, Tag 071W](https://stacks.math.columbia.edu/tag/071W)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
