---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.stalkDerivedPushforwardIso, AlgebraicGeometry.Space.stalkDerivedPushforwardIso_naturality, AlgebraicGeometry.Space.stalkRightDerivedDirectImageIso, AlgebraicGeometry.Space.stalkRightDerivedDirectImageIso_naturality, AlgebraicGeometry.Space.isIso_kernelMap_and_mono_cokernelMap_directImageStalkMap, AlgebraicGeometry.Space.exists_geometricModuleStalkGerm_modulePushforward, AlgebraicGeometry.Space.geometricModuleStalkGerm_modulePushforward_eq_iff, AlgebraicGeometry.Space.directImageGeometricStalkAddEquiv
statement: formalized
proof: formalized
---

# 81.10 Formal glueing of quasi-coherent modules

Section 81.10 of the Stacks Project, [Tag 0AEP](https://stacks.math.columbia.edu/tag/0AEP). 13 tags here are carried by 30 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AEQ, a lemma

[Tag 0AEQ](https://stacks.math.columbia.edu/tag/0AEQ) in the Stacks Project.

**`AlgebraicGeometry.Space.stalkDerivedPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexDerivedStalk.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexDerivedStalk.lean#L293). The attribute's comment: “the comparison isomorphism, for a commutative (not necessarily cartesian) square and a geometric point of Y lifted to the closed subspace, on the two carried inputs 0AEH part (1) and 015N bundled as DerivedPushforwardSquareData”.

> **Stacks 0AEQ.** Let `f : Y ⟶ X` be a morphism of algebraic spaces over a scheme `S`, let
> `i : Z ⟶ X` and `i' : W ⟶ Y` be closed immersions and let `f' : W ⟶ Z` be an integral
> universally injective morphism making the square commute — in the source `W = f^{-1}Z` and `f'`
> is the base change of `f`. Let `ȳ` be a geometric point of `Y` lying on `W` and let
> `x̄ = f(ȳ)`. For an object `Q` of `D(Y_étale)` all of whose cohomology sheaves are supported on
> `|W|`, the stalk at `x̄` of `Rf_*Q` is the stalk at `ȳ` of `Q`.

```lean
def stalkDerivedPushforwardIso
    [RF.IsRightDerivedFunctor unit
      (HomotopyCategory.quasiIso (abelianSheaves.{u + 1} B S hS Y) (ComplexShape.up ℤ))]
    (d : DerivedPushforwardSquareData B S hS i hi i' hi' f' hf' hf'int hf'inj RF)
    (y : GeometricPoint B S hS Y.1) (w : GeometricPoint B S hS W.1)
    (hw : geometricPointMap i'.hom w = y) (Q : smallEtaleDerivedCategory.{u + 1} B S hS Y)
    (hQ : cohomologySupportedOn.{u + 1} B S hS Y
      (Set.range (pointsMap B S hS W.1 i'.hom)) Q) :
    (smallEtaleDerivedAbelianStalk B S hS (geometricPointMap f.hom y)).obj (RF.obj Q) ≅
      (smallEtaleDerivedAbelianStalk B S hS y).obj Q
```

**`AlgebraicGeometry.Space.stalkDerivedPushforwardIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexDerivedStalk.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexDerivedStalk.lean#L309). The attribute's comment: “naturality of the comparison isomorphism in the supported complex”.

> **Stacks 0AEQ: the comparison is natural.** The identification
> `(Rf_*Q)_{x̄} ≅ Q_ȳ` is natural in the complex `Q` supported on `|W|`.

```lean
theorem stalkDerivedPushforwardIso_naturality
    [RF.IsRightDerivedFunctor unit
      (HomotopyCategory.quasiIso (abelianSheaves.{u + 1} B S hS Y) (ComplexShape.up ℤ))]
    (d : DerivedPushforwardSquareData B S hS i hi i' hi' f' hf' hf'int hf'inj RF)
    (y : GeometricPoint B S hS Y.1) (w : GeometricPoint B S hS W.1)
    (hw : geometricPointMap i'.hom w = y)
    {Q Q' : smallEtaleDerivedCategory.{u + 1} B S hS Y}
    (hQ : cohomologySupportedOn.{u + 1} B S hS Y
      (Set.range (pointsMap B S hS W.1 i'.hom)) Q)
    (hQ' : cohomologySupportedOn.{u + 1} B S hS Y
      (Set.range (pointsMap B S hS W.1 i'.hom)) Q') (g : Q ⟶ Q') :
    (smallEtaleDerivedAbelianStalk B S hS (geometricPointMap f.hom y)).map (RF.map g) ≫
        (stalkDerivedPushforwardIso B S hS f hfr i hi i' hi' f' hf' hf'int hf'inj hsq RF unit d
          y w hw Q' hQ').hom =
      (stalkDerivedPushforwardIso B S hS f hfr i hi i' hi' f' hf' hf'int hf'inj hsq RF unit d
          y w hw Q hQ).hom ≫
        (smallEtaleDerivedAbelianStalk B S hS y).map g
```

**`AlgebraicGeometry.Space.stalkRightDerivedDirectImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexRightDerivedStalk.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexRightDerivedStalk.lean#L358).

> **Stacks 0AEQ.** Let `f : Y ⟶ X` be a morphism of algebraic spaces over a scheme `S`, let
> `i : Z ⟶ X` be a closed immersion and let `f^{-1}Z` be its inverse image, a cartesian square
> `sq` with `f' : f^{-1}Z ⟶ Z` and `i' : f^{-1}Z ⟶ Y`, such that `f'` is integral and universally
> injective. Let `ȳ` be a geometric point of `Y` and `x̄ = f(ȳ)`. Then for every object `Q` of
> `D(Y_étale)` supported on `|f^{-1}Z|` there is an isomorphism `(Rf_*Q)_{x̄} ≅ Q_ȳ` in `D(Ab)`,
> where `Rf_*` is any total right derived functor of the direct image of abelian sheaves along `f`
> and the derived categories are arbitrary models.

```lean
def stalkRightDerivedDirectImageIso (f : Y ⟶ X) (i : Z ⟶ X) (hi : IsClosedImmersion B S hS i.hom)
    (i' : W ⟶ Y) (f' : W ⟶ Z) (sq : IsPullback f' i' i f) (hf'int : IsIntegralHom B S hS f'.hom)
    (hf'inj : UniversallyInjective B S hS f'.hom)
    (RF : DerivedCategory (abelianSheaves.{u + 1} B S hS Y) ⥤
      DerivedCategory (abelianSheaves.{u + 1} B S hS X))
    (α : (smallEtaleAbelianDirectImage B S hS f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso (abelianSheaves.{u + 1} B S hS Y) (ComplexShape.up ℤ))]
    (y : GeometricPoint B S hS Y.1)
    (Q : DerivedCategory (abelianSheaves.{u + 1} B S hS Y))
    (hQ : ∀ n : ℤ, supportOfSheaf B S hS Y.1
      ((DerivedCategory.homologyFunctor (abelianSheaves.{u + 1} B S hS Y) n).obj Q) ⊆
        Set.range (pointsMap B S hS W.1 i'.hom)) :
    (smallEtaleAbelianStalk B S hS (geometricPointMap f.hom y)).mapDerivedCategory.obj
        (RF.obj Q) ≅
      (smallEtaleAbelianStalk B S hS y).mapDerivedCategory.obj Q
```

**`AlgebraicGeometry.Space.stalkRightDerivedDirectImageIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexRightDerivedStalk.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexRightDerivedStalk.lean#L381). The attribute's comment: “naturality of the comparison in the supported complex”.

> **Stacks 0AEQ: the comparison is natural** in the complex `Q` supported on `|f^{-1}Z|`,
> being the value at `Q` of an isomorphism of functors.

```lean
theorem stalkRightDerivedDirectImageIso_naturality (f : Y ⟶ X) (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom)
    (i' : W ⟶ Y) (f' : W ⟶ Z) (sq : IsPullback f' i' i f) (hf'int : IsIntegralHom B S hS f'.hom)
    (hf'inj : UniversallyInjective B S hS f'.hom)
    (RF : DerivedCategory (abelianSheaves.{u + 1} B S hS Y) ⥤
      DerivedCategory (abelianSheaves.{u + 1} B S hS X))
    (α : (smallEtaleAbelianDirectImage B S hS f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso (abelianSheaves.{u + 1} B S hS Y) (ComplexShape.up ℤ))]
    (y : GeometricPoint B S hS Y.1)
    {Q Q' : DerivedCategory (abelianSheaves.{u + 1} B S hS Y)}
    (hQ : ∀ n : ℤ, supportOfSheaf B S hS Y.1
      ((DerivedCategory.homologyFunctor (abelianSheaves.{u + 1} B S hS Y) n).obj Q) ⊆
        Set.range (pointsMap B S hS W.1 i'.hom))
    (hQ' : ∀ n : ℤ, supportOfSheaf B S hS Y.1
      ((DerivedCategory.homologyFunctor (abelianSheaves.{u + 1} B S hS Y) n).obj Q') ⊆
        Set.range (pointsMap B S hS W.1 i'.hom)) (g : Q ⟶ Q') :
    (smallEtaleAbelianStalk B S hS (geometricPointMap f.hom y)).mapDerivedCategory.map
        (RF.map g) ≫
        (stalkRightDerivedDirectImageIso B S hS f i hi i' f' sq hf'int hf'inj RF α y Q' hQ').hom =
      (stalkRightDerivedDirectImageIso B S hS f i hi i' f' sq hf'int hf'inj RF α y Q hQ).hom ≫
        (smallEtaleAbelianStalk B S hS y).mapDerivedCategory.map g
```

## Tag 0AER, a lemma

[Tag 0AER](https://stacks.math.columbia.edu/tag/0AER) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_kernelMap_and_mono_cokernelMap_directImageStalkMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormalGlueingTwoTermStalkComplexGeneral.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormalGlueingTwoTermStalkComplexGeneral.lean#L199). The attribute's comment: “isomorphism on kernels and injection on cokernels of the two-term stalk complexes, for an arbitrary morphism of algebraic spaces”.

> **Stacks 0AER.** Let `f : Y ⟶ X` be a morphism of algebraic spaces over a scheme `S` and
> let `Z ⊆ X` be a closed subspace such that `f^{-1}Z ⟶ Z` is integral and universally
> injective. Let `ȳ` be a geometric point of `Y`, let `x̄ = f(ȳ)` and let `G` be an abelian sheaf
> on the small étale site of `Y`. Writing `V = Y ∖ f^{-1}Z` and `j' : V ⟶ Y` for the inclusion,
> the map of two-term complexes
> ```
> ((f_*G)_x̄ ⟶ (f_*(j'_*(G|_V)))_x̄) ⟶ (G_ȳ ⟶ (j'_*(G|_V))_ȳ)
> ```
> given by the canonical comparison of
> `AlgebraicGeometry.Space.smallEtaleAbelianDirectImageStalkMap` induces an isomorphism on
> kernels and an injection on cokernels.

```lean
theorem isIso_kernelMap_and_mono_cokernelMap_directImageStalkMap (f : Y ⟶ X)
    (Z : ClosedSubspaces B S hS X.1)
    (hint : IsIntegralHom B S hS (Z.1.fromPreimage f.hom))
    (hinj : UniversallyInjective B S hS (Z.1.fromPreimage f.hom))
    (y : GeometricPoint B S hS Y.1) (G : abelianSheaves.{u + 1} B S hS Y) :
    IsIso (kernel.map
        ((smallEtaleAbelianDirectImage B S hS f ⋙
            smallEtaleAbelianStalk B S hS (geometricPointMap f.hom y)).map
          (smallEtaleAbelianRestrictionUnit B S hS f Z G))
        ((smallEtaleAbelianStalk B S hS y).map
          (smallEtaleAbelianRestrictionUnit B S hS f Z G))
        ((smallEtaleAbelianDirectImageStalkMap B S hS f y).app G)
        ((smallEtaleAbelianDirectImageStalkMap B S hS f y).app
          (smallEtaleAbelianRestrictionPushforward B S hS f Z G))
        ((smallEtaleAbelianDirectImageStalkMap B S hS f y).naturality
          (smallEtaleAbelianRestrictionUnit B S hS f Z G))) ∧
      Mono (cokernel.map
        ((smallEtaleAbelianDirectImage B S hS f ⋙
            smallEtaleAbelianStalk B S hS (geometricPointMap f.hom y)).map
          (smallEtaleAbelianRestrictionUnit B S hS f Z G))
        ((smallEtaleAbelianStalk B S hS y).map
          (smallEtaleAbelianRestrictionUnit B S hS f Z G))
        ((smallEtaleAbelianDirectImageStalkMap B S hS f y).app G)
        ((smallEtaleAbelianDirectImageStalkMap B S hS f y).app
          (smallEtaleAbelianRestrictionPushforward B S hS f Z G))
        ((smallEtaleAbelianDirectImageStalkMap B S hS f y).naturality
          (smallEtaleAbelianRestrictionUnit B S hS f Z G)))
```

## Tag 0AES, a lemma

[Tag 0AES](https://stacks.math.columbia.edu/tag/0AES) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_geometricModuleStalkGerm_modulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DirectImageGeometricStalk.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DirectImageGeometricStalk.lean#L232). The attribute's comment: “generation half, for the geometric point stalk expressed as the filtered colimit over the etale neighbourhoods of x-bar, with the sections on Y times\_X V read chartwise; the canonical morphism Spec(O\_\{X, x-bar}) -> X is not constructed, since the etale local ring lives one universe up and its spectrum is not an object of the site, so neither the source's formula nor its quasi-compact, quasi-separated and quasi-coherent hypotheses appear”.

> **Stacks 0AES, the generation half of the colimit form.**  Every element of the geometric
> stalk `(f_*G)_{x̄}` is the germ at `x̄` of a section of `p_V^*G` on `Y ×_X V`, for some small
> étale neighbourhood `V` of `x̄`: that section is a compatible family of sections of `G` over the
> étale scheme charts of `Y` above `Y ×_X V`.

```lean
theorem exists_geometricModuleStalkGerm_modulePushforward (f : Y ⟶ X)
    (z : geometricModuleStalk B S hS X x ((modulePushforward B S hS f).obj G)) :
    ∃ (N : SmallEtaleNeighborhood x) (a : (directImageChartDiagram B S hS f G N.chart).sections),
      geometricModuleStalkGerm B S hS X x ((modulePushforward B S hS f).obj G) N
        ((directImageChartSectionsEquiv B S hS f G N.chart).symm a) = z
```

**`AlgebraicGeometry.Space.geometricModuleStalkGerm_modulePushforward_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DirectImageGeometricStalk.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DirectImageGeometricStalk.lean#L253). The attribute's comment: “separation half, for the geometric point stalk expressed as the filtered colimit over the etale neighbourhoods of x-bar, with the sections on Y times\_X V read chartwise; the canonical morphism Spec(O\_\{X, x-bar}) -> X is not constructed, since the etale local ring lives one universe up and its spectrum is not an object of the site, so neither the source's formula nor its quasi-compact, quasi-separated and quasi-coherent hypotheses appear”.

> **Stacks 0AES, the separation half of the colimit form.**  Two sections of the direct image
> `f_*G` over the chart of a small étale neighbourhood `N` of `x̄` have the same germ in the
> geometric stalk `(f_*G)_{x̄}` exactly when, for some smaller neighbourhood `V`, their chartwise
> sections of `G` over the étale scheme charts of `Y` above `Y ×_X V` agree — that is, exactly
> when they agree in `Γ(Y ×_X V, p_V^*G)`.

```lean
theorem geometricModuleStalkGerm_modulePushforward_eq_iff (f : Y ⟶ X)
    (N : SmallEtaleNeighborhood x)
    (s t : ((modulePushforward B S hS f).obj G).val.obj (op N.chart)) :
    geometricModuleStalkGerm B S hS X x ((modulePushforward B S hS f).obj G) N s =
        geometricModuleStalkGerm B S hS X x ((modulePushforward B S hS f).obj G) N t ↔
      ∃ (M : SmallEtaleNeighborhood x) (g : M ⟶ N), ∀ j,
        directImageChartSection B S hS f G M.chart j
            (((modulePushforward B S hS f).obj G).val.map g.hom.op s) =
          directImageChartSection B S hS f G M.chart j
            (((modulePushforward B S hS f).obj G).val.map g.hom.op t)
```

**`AlgebraicGeometry.Space.directImageGeometricStalkAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DirectImageStalkStrictHenselization.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DirectImageStalkStrictHenselization.lean#L162). The attribute's comment: “(f\_*G)\_xbar = Γ(Y ×\_X Spec(O\_\{X,xbar}), p^*G) for f quasi-compact and quasi-separated and G quasi-coherent, as an isomorphism of abelian groups; the source's p^*F is a misprint for p^*G”.

> **The stalk of a direct image at a geometric point, over the strict henselization.**  Let `X`
> be an algebraic space over `S`, `f : Y ⟶ X` a quasi-compact and quasi-separated morphism, `x̄` a
> geometric point of `X` and `h : Spec(𝒪_{X, x̄}) ⟶ X` the canonical morphism
> (`AlgebraicGeometry.Space.strictHenselizationSpaceHom`).  For a quasi-coherent `𝒪_Y`-module `𝒢`,
>
> `(f_*𝒢)_{x̄} = Γ(Y ×_X Spec(𝒪_{X, x̄}), p^*𝒢)`,
>
> where `p : Y ×_X Spec(𝒪_{X, x̄}) ⟶ Y` is the projection: the geometric stalk of the direct image
> is identified, as an abelian group, with the global sections of the pullback of `𝒢` to the base
> change of `Y` to the strict henselization.  (The source prints `p^*𝓕` for `p^*𝒢`.)
>
> The identification is the composite of: the stalk of `f_*𝒢` at `x̄ = h ∘ t̄` with the stalk of
> `h^*f_*𝒢` at the closed point `t̄` (Stacks 05VQ and the bijectivity of
> `𝒪_{X, x̄} ⟶ 𝒪_{T, t̄}`), that stalk with the global sections of `h^*f_*𝒢` (the closed point has an
> initial neighbourhood), the flat base change `h^*f_*𝒢 ≅ f'_*p^*𝒢` of Stacks 073K, and
> `Γ(T, f'_* -) = Γ(Y ×_X T, -)`.

```lean
def directImageGeometricStalkAddEquiv :
    geometricModuleStalk B S hS X x ((modulePushforward B S hS f).obj G) ≃+
      ((modulePullback B S hS (pullback.fst f (strictHenselizationSpaceHom X x))).obj
        G).sections
```

## Tag 0AET, a lemma

[Tag 0AET](https://stacks.math.columbia.edu/tag/0AET) in the Stacks Project.

**`AlgebraicGeometry.Space.closedSubspaceStalkIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/StalkTorsionOfSupportedComplex.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/StalkTorsionOfSupportedComplex.lean#L355). The attribute's comment: “the stalk I\_x̄ of the ideal sheaf of Z”.

> **Stacks 0AET.** The stalk `I_x̄ ⊆ 𝒪_{X, x̄}` at a geometric point of the ideal sheaf of a
> closed subspace: the ideal of the étale local ring generated by the germs of the local sections
> of the defining ideal.

```lean
noncomputable def closedSubspaceStalkIdeal (X : AlgebraicSpaces B S hS)
    (Z : ClosedSubspaces B S hS X.1) (x : GeometricPoint B S hS X.1) :
    Ideal (etaleLocalRing B S hS X.1 x)
```

**`AlgebraicGeometry.Space.isIPowerTorsion_geometricModuleStalk_homology_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/StalkTorsionOfSupportedComplex.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/StalkTorsionOfSupportedComplex.lean#L423). The attribute's comment: “asserted for the stalk Hⁿ(Q)\_x̄ of the cohomology sheaf rather than for the cohomology Hⁿ(Q\_x̄) of the stalk of Q in D(Ab); the two agree by exactness of the stalk functor at a geometric point, which this development does not have. Stated at module universe m = u”.

> **Stacks 0AET.** Let `X` be an algebraic space over `S`, let `Z ⊆ X` be a closed subspace
> whose inclusion is of finite presentation and let `Q ∈ D_QCoh(𝒪_X)` have all its cohomology
> sheaves supported on `|Z|`.  Then at every geometric point `x̄` the stalk of every cohomology
> sheaf of `Q` is power torsion for the stalk `I_x̄` of the ideal sheaf of `Z`.

```lean
theorem isIPowerTorsion_geometricModuleStalk_homology_of_cohomologySupportedOn
    (X : AlgebraicSpaces B S hS)
    [HasSheafify (smallEtaleRingedSite B S hS X.1 X.2).J AddCommGrpCat.{u}]
    [(smallEtaleRingedSite B S hS X.1 X.2).J.WEqualsLocallyBijective AddCommGrpCat.{u}]
    (Z : ClosedSubspaces B S hS X.1) (hZ : IsFinitePresentation B S hS Z.1.ι)
    (Q : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2)
    (hQ : CohomologySupportedOn B S hS X.1 X.2
      (Set.range (pointsMap B S hS Z.1.toFunctor Z.1.ι)) Q.1)
    (x : GeometricPoint B S hS X.1) (n : ℤ) :
    IsIPowerTorsion (etaleLocalRing B S hS X.1 x)
      (geometricModuleStalk B S hS X x
        ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) n).obj Q.1))
      (closedSubspaceStalkIdeal B S hS X Z x)
```

## Tag 0AEU, a lemma

[Tag 0AEU](https://stacks.math.columbia.edu/tag/0AEU) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_derivedAdjunction_counit_app_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingDerivedEquivalence.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingDerivedEquivalence.lean#L169). The attribute's comment: “corrected statement: the printed one omits that `Z ⟶ X` is of finite presentation, which the source's proof uses and without which it is false (see `errata.md`)”.

> **Stacks 0AEU** (corrected). Let `f : Y ⟶ X` be a morphism of algebraic spaces over `S` and
> `Z ⊆ X` a closed subspace of finite presentation such that `f⁻¹Z ⟶ Z` is an isomorphism and `f` is
> flat at every point of `f⁻¹Z`. Then for every `Q ∈ D_QCoh(𝒪_Y)` supported on `|f⁻¹Z|` the counit
> `Lf^*Rf_*Q ⟶ Q` of the derived adjunction of the morphism of small étale ringed topoi is an
> isomorphism.
>
> The finite presentation of `Z ⟶ X` is missing from the printed statement (an erratum, recorded in
> `errata.md`); the source's proof uses it (through Stacks 0AET and 05E9, which need the ideal of `Z`
> finitely generated), and the printed statement is false without it. Let `A` be the valuation ring
> of the field `ℚ((t^ℚ))` of Hahn series and `I` its maximal ideal, so `I = I²` is not finitely
> generated; let `X = Spec A`, `Z = V(I)`, `Y = Spec B` for the square-zero extension `B = A ⊕ Iε`,
> and `Q = M~` for `M = B / t¹B`. Then `B` is flat over `A`, `A / I ⟶ B / IB` is bijective (so
> `f⁻¹Z ⟶ Z` is an isomorphism) and `M` is supported on `V(IB)`, but the counit, which is the
> action map `M ⊗_A B ⟶ M`, is not injective: this is the machine-checked
> `IPowerTorsion.exists_not_bijective_actionMap_of_support_subset`.

```lean
theorem isIso_derivedAdjunction_counit_app_of_cohomologySupportedOn
    {Y X : AlgebraicSpaces B S hS} (f : Y ⟶ X) (Z : Subfunctor X.1)
    (hZ : IsClosedSubspace B S hS Z) (hZfp : IsFinitePresentation B S hS Z.ι)
    (hfZ : IsIso (Z.fromPreimage f.hom))
    (hflat : ∀ y : points B S hS (Z.preimage f.hom).toFunctor,
      IsFlatAt B S hS f.hom
        (pointsMap B S hS (Z.preimage f.hom).toFunctor (Z.preimage f.hom).ι y))
    (Q : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2)
    (hQ : CohomologySupportedOn B S hS Y.1 Y.2
      (Set.range (pointsMap B S hS (Z.preimage f.hom).toFunctor (Z.preimage f.hom).ι)) Q.1) :
    IsIso ((derivedAdjunction (smallEtaleRingedToposHom B S hS f)).counit.app Q.1)
```

## Tag 0AEV, a situation

[Tag 0AEV](https://stacks.math.columbia.edu/tag/0AEV) in the Stacks Project.

**`AlgebraicGeometry.Space.FormalGlueingSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModules.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModules.lean#L59). The attribute's comment: “standing data and hypotheses”.

> **Stacks 0AEV.** The standing situation for formal glueing of quasi-coherent modules: a
> quasi-compact, quasi-separated morphism `f : Y ⟶ X` of algebraic spaces over `S`, a finitely
> presented closed subspace `Z` of `X` over which `f` is an isomorphism, with `f` flat at every
> point of the inverse image of `Z`.

```lean
structure FormalGlueingSituation
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
```

**`AlgebraicGeometry.Space.FormalGlueingSituation.V_eq_openComplement_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModules.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModules.lean#L105). The attribute's comment: “V = Y minus the inverse image of Z”.

> **Stacks 0AEV.** The inverse image of the open complement of `Z` is the open complement
> of the inverse image of `Z`.

```lean
theorem V_eq_openComplement_preimage (D : FormalGlueingSituation B S hS) :
    D.V = openComplement B S hS (D.Z.preimage D.f)
```

**`AlgebraicGeometry.Space.FormalGlueingSituation.isOpenSubspace_U`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModules.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModules.lean#L115). The attribute's comment: “openness of U”.

> **Stacks 0AEV.** The complement of `Z` is an open subspace of `X`.

```lean
theorem isOpenSubspace_U (D : FormalGlueingSituation B S hS) :
    IsOpenSubspace B S hS D.U
```

**`AlgebraicGeometry.Space.FormalGlueingSituation.isOpenSubspace_V`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModules.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModules.lean#L121). The attribute's comment: “openness of V”.

> **Stacks 0AEV.** The complement of the inverse image of `Z` is an open subspace of `Y`.

```lean
theorem isOpenSubspace_V (D : FormalGlueingSituation B S hS) :
    IsOpenSubspace B S hS D.V
```

## Tag 0AEW, an equation

[Tag 0AEW](https://stacks.math.columbia.edu/tag/0AEW) in the Stacks Project.

**`AlgebraicGeometry.Space.FormalGlueingSituation.overlapPullbackComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesFunctor.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesFunctor.lean#L244). The attribute's comment: “the comparison over the overlap”.

> The canonical identification `(f|_V)^* ∘ j^* ≅ (j')^* ∘ f^*` of the two ways of
> transporting an `𝒪_X`-module to the overlap `V`: both are the inverse image along the common
> composite `V ⟶ X` of the glueing square, by the inverse-image half of Stacks 03LU.

```lean
def overlapPullbackComparison :
    modulePullback B S hS D.openImmersion ⋙ modulePullback B S hS D.overlapRestriction ≅
      modulePullback B S hS D.ambientMorphism ⋙ modulePullback B S hS D.openImmersionOver
```

**`AlgebraicGeometry.Space.FormalGlueingSituation.moduleGlueingData`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesFunctor.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesFunctor.lean#L262). The attribute's comment: “the category of glueing data”.

> **The category `QCoh(Y → X, Z)` of formal glueing data for quasi-coherent modules**: the
> triples `(H, G, φ)` of a quasi-coherent `𝒪_U`-module `H`, a quasi-coherent `𝒪_Y`-module `G` and
> an isomorphism `φ : (f|_V)^*H ≅ G|_V`, with the pairs of module maps commuting with the overlap
> isomorphisms as morphisms.
>
> The category is introduced in the prose of the source immediately before equation (0AEX); it is
> the target of the functor of Stacks 0AEW and the source of the functor of Stacks 0AEX.

```lean
abbrev moduleGlueingData
```

**`AlgebraicGeometry.Space.FormalGlueingSituation.glueingModulesUnconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesFunctorUnconditional.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesFunctorUnconditional.lean#L67).

> The functor `QCoh(𝒪_X) ⥤ QCoh(Y → X, Z)` of formal glueing: a quasi-coherent `𝒪_X`-module
> goes to its restriction to the open complement `U`, its pullback to `Y`, and the canonical
> comparison of the two on the overlap `V`.

```lean
def glueingModulesUnconditional :
    QuasicoherentSheaves.{u, u} B S hS D.spaceX.1 D.spaceX.2 ⥤ D.moduleGlueingData
```

**`AlgebraicGeometry.Space.FormalGlueingSituation.glueingModulesFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesUnconditional.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesUnconditional.lean#L55). The attribute's comment: “the functor, with no hypothesis”.

> The functor `QCoh(𝒪_X) ⥤ QCoh(Y → X, Z)` of formal glueing: a quasi-coherent `𝒪_X`-module
> `F` goes to `(F|_U, f^*F, can)`.

```lean
def glueingModulesFunctor :
    QuasicoherentSheaves.{u, u} B S hS D.spaceX.1 D.spaceX.2 ⥤ D.moduleGlueingData
```

## Tag 0AEX, an equation

[Tag 0AEX](https://stacks.math.columbia.edu/tag/0AEX) in the Stacks Project.

**`AlgebraicGeometry.Space.FormalGlueingSituation.glueingKernelMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesKernel.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesKernel.lean#L287). The attribute's comment: “the map out of the direct sum”.

> **The map `j_*H ⊕ f_*G ⟶ (f ∘ j')_*(G|_V)` of Stacks 0AEX**: the difference of the two
> canonical maps to the direct image from the overlap, so that a pair of sections lies in its
> kernel exactly when the two sections agree on the overlap.

```lean
def glueingKernelMap :
    D.restrictionDirectImage ⊞ D.ambientDirectImage ⟶ D.overlapDirectImage
```

**`AlgebraicGeometry.Space.FormalGlueingSituation.glueingKernelDiagram`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesKernel.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesKernel.lean#L301). The attribute's comment: “the kernel module, as a functor of the glueing triple”.

> **The `𝒪_X`-module `Ker(j_*H ⊕ f_*G ⟶ (f ∘ j')_*(G|_V))` of Stacks 0AEX**, as a functor of
> the glueing triple.  It is the kernel in the category of functors to the `𝒪_X`-modules, so no
> quasi-coherence is assumed and the functoriality is that of a kernel.

```lean
def glueingKernelDiagram :
    D.moduleGlueingComma ⥤ Modules.{u, u} B S hS D.spaceX.1 D.spaceX.2
```

**`AlgebraicGeometry.Space.FormalGlueingSituation.glueingKernelFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesUnconditional.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesUnconditional.lean#L97). The attribute's comment: “the functor, with no hypothesis”.

> The functor `QCoh(Y → X, Z) ⥤ QCoh(𝒪_X)`,
> `(H, G, φ) ↦ Ker(j_*H ⊕ f_*G ⟶ (f ∘ j')_*(G|_V))`.

```lean
def glueingKernelFunctor :
    D.moduleGlueingData ⥤ QuasicoherentSheaves.{u, u} B S hS D.spaceX.1 D.spaceX.2
```

## Tag 0AEY, a lemma

[Tag 0AEY](https://stacks.math.columbia.edu/tag/0AEY) in the Stacks Project.

**`AlgebraicGeometry.Space.FormalGlueingSituation.glueingAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesUnconditional.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesUnconditional.lean#L118). The attribute's comment: “with no hypothesis”.

> The functor `glueingModulesFunctor` is left adjoint to the functor
> `glueingKernelFunctor`.

```lean
def glueingAdjunction : D.glueingModulesFunctor ⊣ D.glueingKernelFunctor
```

## Tag 0AEZ, a lemma

[Tag 0AEZ](https://stacks.math.columbia.edu/tag/0AEZ) in the Stacks Project.

**`AlgebraicGeometry.Space.FormalGlueingSituation.FlatBaseChange.glueingModulesFunctorPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesFlatBaseChangeUnconditional.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesFlatBaseChangeUnconditional.lean#L473). The attribute's comment: “compatibility with the functor of Tag 0AEW”.

> **Stacks 0AEZ, compatibility with the functor of Stacks 0AEW.**  For the base change of the
> formal glueing situation along a flat morphism `g : X' ⟶ X`, the pullback
> `QCoh(𝒪_X) ⥤ QCoh(𝒪_{X'})` of Stacks 03GA and the pullback
> `QCoh(Y → X, Z) ⥤ QCoh(Y' → X', Z')` of glueing triples commute with the functors
> `QCoh(𝒪_X) ⥤ QCoh(Y → X, Z)` and `QCoh(𝒪_{X'}) ⥤ QCoh(Y' → X', Z')` of Stacks 0AEW.

```lean
def glueingModulesFunctorPullbackIso :
    D.glueingModulesFunctor ⋙ c.glueingDataPullback ≅
      quasicoherentPullbackFunctor B S hS c.g ⋙ D'.glueingModulesFunctor
```

**`AlgebraicGeometry.Space.FormalGlueingSituation.FlatBaseChange.glueingKernelFunctorPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesFlatBaseChangeUnconditional.lean, line 500](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesFlatBaseChangeUnconditional.lean#L500). The attribute's comment: “compatibility with the functor of Tag 0AEX”.

> **Stacks 0AEZ, compatibility with the functor of Stacks 0AEX.**  For the base change of the
> formal glueing situation along a flat morphism `g : X' ⟶ X`, the pullback
> `QCoh(𝒪_X) ⥤ QCoh(𝒪_{X'})` of Stacks 03GA and the pullback
> `QCoh(Y → X, Z) ⥤ QCoh(Y' → X', Z')` of glueing triples commute with the functors
> `QCoh(Y → X, Z) ⥤ QCoh(𝒪_X)` and `QCoh(Y' → X', Z') ⥤ QCoh(𝒪_{X'})` of Stacks 0AEX.
>
> The isomorphism is the one transported from
> `AlgebraicGeometry.Space.FormalGlueingSituation.FlatBaseChange.glueingModulesFunctorPullbackIso`
> along the two equivalences of Stacks 0AF0, whose quasi-inverses are the functors of
> Stacks 0AEX.

```lean
def glueingKernelFunctorPullbackIso :
    D.glueingKernelFunctor ⋙ quasicoherentPullbackFunctor B S hS c.g ≅
      c.glueingDataPullback ⋙ D'.glueingKernelFunctor
```

**`AlgebraicGeometry.Space.FormalGlueingSituation.glueingModulesFunctorBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesFlatBaseChangeUnconditional.lean, line 519](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesFlatBaseChangeUnconditional.lean#L519). The attribute's comment: “compatibility with the functor of Tag 0AEW, for the constructed base change along a flat morphism”.

> **Stacks 0AEZ, compatibility with the functor of Stacks 0AEW**, for the base change of the
> situation along a flat morphism `k : X' ⟶ X`, with `Z' = X' ×_X Z` and `Y' = X' ×_X Y`.

```lean
def glueingModulesFunctorBaseChangeIso :
    D.glueingModulesFunctor ⋙ (D.flatBaseChange k hk).glueingDataPullback ≅
      quasicoherentPullbackFunctor B S hS k ⋙ (D.baseChange k).glueingModulesFunctor
```

**`AlgebraicGeometry.Space.FormalGlueingSituation.glueingKernelFunctorBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesFlatBaseChangeUnconditional.lean, line 528](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesFlatBaseChangeUnconditional.lean#L528). The attribute's comment: “compatibility with the functor of Tag 0AEX, for the constructed base change along a flat morphism”.

> **Stacks 0AEZ, compatibility with the functor of Stacks 0AEX**, for the base change of the
> situation along a flat morphism `k : X' ⟶ X`, with `Z' = X' ×_X Z` and `Y' = X' ×_X Y`.

```lean
def glueingKernelFunctorBaseChangeIso :
    D.glueingKernelFunctor ⋙ quasicoherentPullbackFunctor B S hS k ≅
      (D.flatBaseChange k hk).glueingDataPullback ⋙ (D.baseChange k).glueingKernelFunctor
```

## Tag 0AF0, a proposition

[Tag 0AF0](https://stacks.math.columbia.edu/tag/0AF0) in the Stacks Project.

**`AlgebraicGeometry.Space.FormalGlueingSituation.isIso_glueingAdjunction_unit_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesQCohEquivalence.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingModulesQCohEquivalence.lean#L83).

> **Stacks 0AF0.**  In Situation 0AEV the functor `QCoh(𝒪_X) ⥤ QCoh(Y → X, Z)` of Stacks 0AEW is
> an equivalence with quasi-inverse the functor of Stacks 0AEX: the unit and the counit of the
> adjunction of Stacks 0AEY between them are isomorphisms.

```lean
theorem isIso_glueingAdjunction_unit_counit :
    IsIso D.glueingAdjunction.unit ∧ IsIso D.glueingAdjunction.counit
```

## Tag 0AFJ, a lemma

[Tag 0AFJ](https://stacks.math.columbia.edu/tag/0AFJ) in the Stacks Project.

**`AlgebraicGeometry.Space.FormalGlueingSituation.exists_supportedQuasicoherentDerived_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingDerivedEquivalence.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingDerivedEquivalence.lean#L200).

> **Stacks 0AFJ.** In Situation 0AEV (`AlgebraicGeometry.Space.FormalGlueingSituation`), the
> derived direct image `Rf_*` of the morphism of small étale ringed topoi of `f` induces an
> equivalence `D_{QCoh,|f⁻¹Z|}(𝒪_Y) ≌ D_{QCoh,|Z|}(𝒪_X)` with quasi-inverse given by the derived
> pullback `Lf^*`: there is an equivalence whose functor is the restriction of `Rf_*` and whose
> inverse is the restriction of `Lf^*`.

```lean
theorem FormalGlueingSituation.exists_supportedQuasicoherentDerived_equivalence
    (D : FormalGlueingSituation B S hS) :
    letI := HasDerivedCategory.standard (Modules.{u, u} B S hS D.spaceX.1 D.spaceX.2)
    letI := HasDerivedCategory.standard (Modules.{u, u} B S hS D.spaceY.1 D.spaceY.2)
    ∃ e : (supportedQuasicoherentDerived B S hS D.spaceY
        (subspacePointSet B S hS D.Y (D.Z.preimage D.f))).FullSubcategory ≌
      (supportedQuasicoherentDerived B S hS D.spaceX
        (subspacePointSet B S hS D.X D.Z)).FullSubcategory,
      e.functor ⋙ (supportedQuasicoherentDerived B S hS D.spaceX
          (subspacePointSet B S hS D.X D.Z)).ι =
        (supportedQuasicoherentDerived B S hS D.spaceY
          (subspacePointSet B S hS D.Y (D.Z.preimage D.f))).ι ⋙
          derivedPushforward (X := smallEtaleRingedTopos B S hS D.spaceY)
            (Y := smallEtaleRingedTopos B S hS D.spaceX)
            (smallEtaleRingedToposHom B S hS D.ambientMorphism) ∧
      e.inverse ⋙ (supportedQuasicoherentDerived B S hS D.spaceY
          (subspacePointSet B S hS D.Y (D.Z.preimage D.f))).ι =
        (supportedQuasicoherentDerived B S hS D.spaceX
          (subspacePointSet B S hS D.X D.Z)).ι ⋙
          smallEtaleDerivedModulePullback B S hS D.ambientMorphism
```

## Tag 0AF1, a lemma

[Tag 0AF1](https://stacks.math.columbia.edu/tag/0AF1) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_fpqcCovering_refining_openComplement_and_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingCovering.lean, line 950](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingCovering.lean#L950).

> The open complement and the formal-glueing morphism admit an fpqc
> covering refinement.

```lean
theorem exists_fpqcCovering_refining_openComplement_and_source
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (D : FormalGlueingSituation B S hS) :
    ∃ (I : Type u)
      (Xi : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
      (g : ∀ i, Xi i ⟶ D.X),
      (∀ i, IsAlgebraicSpace B S hS (Xi i)) ∧
      IsFpqcCovering B S hS g ∧
      (∀ i, (∃ a : Xi i ⟶ D.U.toFunctor, a ≫ D.U.ι = g i) ∨
        (∃ b : Xi i ⟶ D.Y, b ≫ D.f = g i))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 81.10, Tag 0AEP](https://stacks.math.columbia.edu/tag/0AEP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
