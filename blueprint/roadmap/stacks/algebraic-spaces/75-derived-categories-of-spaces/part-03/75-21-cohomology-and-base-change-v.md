---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.geometricStalkBaseChangeCohomologyMap, AlgebraicGeometry.Space.canonicalGeometricStalkBaseChangeCohomologyMap, AlgebraicGeometry.Space.tfae_geometricPointwiseBaseChange, AlgebraicGeometry.Space.isIso_smallEtaleDerivedBaseChangeComp_of_geometricPointwiseBaseChange, AlgebraicGeometry.Space.geometricPointwiseBaseChange_tensor, AlgebraicGeometry.Space.geometricPointwiseBaseChange_sheafHom_of_isPerfect, AlgebraicGeometry.Space.geometricPointwiseBaseChange_sheafHom_of_isPseudoCoherent, Stacks.Examples.PseudoCoherentSheafHomBaseChange.not_forall_geometricPointwiseBaseChange_sheafHom_of_isPseudoCoherent
statement: formalized
proof: formalized
---

# 75.21 Cohomology and base change, V

Section 75.21 of the Stacks Project, [Tag 0DKE](https://stacks.math.columbia.edu/tag/0DKE). 6 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DKF, an equation

[Tag 0DKF](https://stacks.math.columbia.edu/tag/0DKF) in the Stacks Project.

**`AlgebraicGeometry.Space.geometricStalkBaseChangeCohomologyMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkCohomologyMap.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkCohomologyMap.lean#L280). The attribute's comment: “the map, given the derived pullback-stalk comparison `ps`”.

> **Stacks Project, Equation 0DKF.** The canonical map
>
> `H^n(K_x̄ ⊗ᴸ_{𝒪_{Y,ȳ}} 𝒪_{Y',ȳ'}) ⊗_{(𝒪_{X,x̄} ⊗_{𝒪_{Y,ȳ}} 𝒪_{Y',ȳ'})} 𝒪_{X',x̄'} ⟶ H^n(K'_x̄')`
>
> of `𝒪_{X',x̄'}`-modules attached to a commutative square of algebraic spaces, a geometric point
> `x̄'` of `X'`, objects `K` of `D(𝒪_X)` and `K'` of `D(𝒪_{X'})` and a morphism
> `φ : L(g')^*K ⟶ K'`.  No cartesianness, Tor independence or quasi-coherence is required.
>
> It is built, not chosen: the `𝒪_{X,x̄} ⊗_{𝒪_{Y,ȳ}} 𝒪_{Y',ȳ'}`-module structure on the source is
> `RingTheory.TorIndependence.baseChangeCohomologyModule` and the map is
> `RingTheory.TorIndependence.ringBaseChangeCohomologyMap`, the adjoint of the Stacks 065Z
> comparison followed by `φ`.
>
> Two premises are carried, and the construction is complete relative to them.  The instance
> argument `Functor.HasLeftDerivedFunctor` is the existence of `L(g')^*` itself, carried as
> `AlgebraicGeometry.Space.smallEtaleDerivedModulePullback` carries it, because the K-flat
> resolutions of Stacks 06YS are available in this tree only on a site which is
> `CategoryTheory.SmallCategory`.  The morphism `ps` is the derived pullback-stalk comparison
> `K_x̄ ⊗ᴸ_{𝒪_{X,x̄}} 𝒪_{X',x̄'} ⟶ (L(g')^*K)_x̄'`, which the source states as an equality and
> which nothing in this tree constructs for algebraic spaces.

```lean
def geometricStalkBaseChangeCohomologyMap
    (f : X ⟶ Y) (g : Y' ⟶ Y) (f' : X' ⟶ Y') (g' : X' ⟶ X) (w : g' ≫ f = f' ≫ g)
    (x' : GeometricPoint B S hS X'.1)
    [(smallEtaleModulePullbackOnHomotopy B S hS g').HasLeftDerivedFunctor
      (smallEtaleModuleQuasiIso B S hS X)]
    (K : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (K' : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X')))
    (φ : (smallEtaleDerivedModulePullback B S hS g').obj K ⟶ K')
    (ps : (CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, u}
          (stalkStructureMap B S hS g' x').hom).functor.obj
        ((geometricDerivedStalk B S hS (geometricPointMap g'.hom x')).obj K) ⟶
      (geometricDerivedStalk B S hS x').obj
        ((smallEtaleDerivedModulePullback B S hS g').obj K))
    (n : ℤ)
```

**`AlgebraicGeometry.Space.canonicalGeometricStalkBaseChangeCohomologyMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkCohomologyMapCanonical.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkCohomologyMapCanonical.lean#L65).

> **Stacks Project, Equation 0DKF.** The canonical map
>
> `H^n(K_x̄ ⊗ᴸ_{𝒪_{Y,ȳ}} 𝒪_{Y',ȳ'}) ⊗_{(𝒪_{X,x̄} ⊗_{𝒪_{Y,ȳ}} 𝒪_{Y',ȳ'})} 𝒪_{X',x̄'} ⟶ H^n(K'_x̄')`
>
> of `𝒪_{X',x̄'}`-modules attached to a commutative square of algebraic spaces, a geometric point
> `x̄'` of `X'`, objects `K` of `D(𝒪_X)` and `K'` of `D(𝒪_{X'})` and a morphism
> `φ : L(g')^*K ⟶ K'`.  No cartesianness, Tor independence or quasi-coherence is required.
>
> It is built, not chosen: the `𝒪_{X,x̄} ⊗_{𝒪_{Y,ȳ}} 𝒪_{Y',ȳ'}`-module structure on the source is
> `RingTheory.TorIndependence.baseChangeCohomologyModule` and the map is
> `RingTheory.TorIndependence.ringBaseChangeCohomologyMap`, the adjoint of the Stacks 065Z
> comparison, precomposed with the derived pullback-stalk comparison
> `K_x̄ ⊗ᴸ_{𝒪_{X,x̄}} 𝒪_{X',x̄'} ⟶ (L(g')^*K)_x̄'` and followed by `φ`.

```lean
def canonicalGeometricStalkBaseChangeCohomologyMap
    (f : X ⟶ Y) (g : Y' ⟶ Y) (f' : X' ⟶ Y') (g' : X' ⟶ X) (w : g' ≫ f = f' ≫ g)
    (x' : GeometricPoint B S hS X'.1)
    (K : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (K' : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X')))
    (φ : (smallEtaleDerivedModulePullback B S hS g').obj K ⟶ K')
    (n : ℤ)
```

## Tag 0DKG, a lemma

[Tag 0DKG](https://stacks.math.columbia.edu/tag/0DKG) in the Stacks Project.

**`AlgebraicGeometry.Space.tfae_geometricPointwiseBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricPointwiseBaseChangeTFAE.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricPointwiseBaseChangeTFAE.lean#L50).

> **Stacks 0DKG.** For a cartesian square of algebraic spaces, `K ∈ D_QCoh(𝒪_X)`,
> `K' ∈ D_QCoh(𝒪_{X'})` and `φ : L(g')^*K ⟶ K'`, the following are equivalent:
> (1) the map of Equation 0DKF is an isomorphism at every geometric point of `X'` in every degree;
> (2) for every diagram of schemes `U ⟶ V ⟵ V'` étale over `X ⟶ Y ⟵ Y'` with `U' = V' ×_V U`, the
> conditions of Stacks 0DJ8 hold for `La^*K` and `L(a')^*K'`;
> (3) they hold for some such diagram with `U' ⟶ X'` surjective.

```lean
theorem tfae_geometricPointwiseBaseChange {X Y X' Y' : AlgebraicSpaces B S hS} {f : X ⟶ Y}
    {g : Y' ⟶ Y} {f' : X' ⟶ Y'} {g' : X' ⟶ X} (sq : IsPullback g' f' f g)
    (K : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hK : QcohDerived B S hS X K)
    (K' : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X')))
    (hK' : QcohDerived B S hS X' K')
    (φ : (smallEtaleDerivedModulePullback B S hS g').obj K ⟶ K') :
    List.TFAE [GeometricPointwiseBaseChange B S hS f g f' g' sq.w K K' φ,
      EtaleDiagramChartwiseBaseChange f g f' g' K hK K' hK' φ,
      SurjectiveDiagramChartwiseBaseChange f g f' g' K hK K' hK' φ]
```

## Tag 0DKH, a lemma

[Tag 0DKH](https://stacks.math.columbia.edu/tag/0DKH) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_smallEtaleDerivedBaseChangeComp_of_geometricPointwiseBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricPointwiseBaseChangeIso.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricPointwiseBaseChangeIso.lean#L44).

> **Stacks 0DKH.** For a cartesian square of algebraic spaces with `f` quasi-compact and
> quasi-separated, `K ∈ D_QCoh(𝒪_X)`, `K' ∈ D_QCoh(𝒪_{X'})` and `φ : L(g')^*K ⟶ K'` satisfying the
> equivalent conditions of Stacks 0DKG (in the form of condition (1)), the composite
> `Lg^*Rf_*K ⟶ Rf'_*L(g')^*K ⟶ Rf'_*K'` is an isomorphism.

```lean
theorem isIso_smallEtaleDerivedBaseChangeComp_of_geometricPointwiseBaseChange
    {X Y X' Y' : AlgebraicSpaces B S hS} {f : X ⟶ Y} {g : Y' ⟶ Y} {f' : X' ⟶ Y'}
    {g' : X' ⟶ X} (sq : IsPullback g' f' f g) (hfqc : IsQuasiCompact B S hS f.hom)
    (hfqs : IsQuasiSeparated B S hS f.hom)
    (K : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hK : QcohDerived B S hS X K)
    (K' : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X')))
    (hK' : QcohDerived B S hS X' K')
    (φ : (smallEtaleDerivedModulePullback B S hS g').obj K ⟶ K')
    (h : GeometricPointwiseBaseChange B S hS f g f' g' sq.w K K' φ) :
    IsIso (smallEtaleDerivedBaseChangeComp B S hS f g f' g' sq.w K K' φ)
```

## Tag 0DKI, a lemma

[Tag 0DKI](https://stacks.math.columbia.edu/tag/0DKI) in the Stacks Project.

**`AlgebraicGeometry.Space.geometricPointwiseBaseChange_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/GeometricPointwiseBaseChangeTensorSheafHom.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/GeometricPointwiseBaseChangeTensorSheafHom.lean#L84). The attribute's comment: “(1)”.

> **The conditions of Stacks 0DKG pass to derived tensor products** (Stacks 0DKI (1)). For a
> cartesian square, `E`, `K` with quasi-coherent cohomology on `X`, `K'` on `X'` and
> `φ : L(g')^*K ⟶ K'` satisfying the conditions of Stacks 0DKG, they hold for
> `L(g')^*(E ⊗ᴸ K) ⟶ L(g')^*E ⊗ᴸ K'`, Stacks 07A4 followed by `L(g')^*E ⊗ᴸ φ`.

```lean
theorem geometricPointwiseBaseChange_tensor (sq : IsPullback g' f' f g)
    (E K : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hE : QcohDerived B S hS X E) (hK : QcohDerived B S hS X K)
    (K' : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X')))
    (hK' : QcohDerived B S hS X' K')
    (φ : (smallEtaleDerivedModulePullback B S hS g').obj K ⟶ K')
    (h : GeometricPointwiseBaseChange B S hS f g f' g' sq.w K K' φ) :
    GeometricPointwiseBaseChange B S hS f g f' g' sq.w
      (((smallEtaleDerivedTensor B S hS X).obj E).obj K)
      (((smallEtaleDerivedTensor B S hS X').obj
        ((smallEtaleDerivedModulePullback B S hS g').obj E)).obj K')
      ((smallEtaleDerivedPullbackTensorIso g').hom.app (E, K) ≫
        ((smallEtaleDerivedTensor B S hS X').obj
          ((smallEtaleDerivedModulePullback B S hS g').obj E)).map φ)
```

**`AlgebraicGeometry.Space.geometricPointwiseBaseChange_sheafHom_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/GeometricPointwiseBaseChangeTensorSheafHom.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/GeometricPointwiseBaseChangeTensorSheafHom.lean#L111). The attribute's comment: “(2)”.

> **The conditions of Stacks 0DKG pass to the derived internal Hom out of a perfect object**
> (Stacks 0DKI (2)). For a cartesian square, `E` perfect and `K` with quasi-coherent cohomology on
> `X`, `K'` with quasi-coherent cohomology on `X'` and `φ : L(g')^*K ⟶ K'` satisfying the conditions
> of Stacks 0DKG, they hold for `L(g')^*R𝓗om(E, K) ⟶ R𝓗om(L(g')^*E, K')`, the map of Stacks 08JF
> followed by `R𝓗om(L(g')^*E, φ)`.

```lean
theorem geometricPointwiseBaseChange_sheafHom_of_isPerfect (sq : IsPullback g' f' f g)
    (E : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hE : RingedSite.IsPerfect (smallEtaleRingedSite B S hS X.1 X.2) E)
    (K : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hK : QcohDerived B S hS X K)
    (K' : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X')))
    (hK' : QcohDerived B S hS X' K')
    (φ : (smallEtaleDerivedModulePullback B S hS g').obj K ⟶ K')
    (h : GeometricPointwiseBaseChange B S hS f g f' g' sq.w K K' φ) :
    GeometricPointwiseBaseChange B S hS f g f' g' sq.w
      (((smallEtaleDerivedSheafHom B S hS X).obj (op E)).obj K)
      (((smallEtaleDerivedSheafHom B S hS X').obj
        (op ((smallEtaleDerivedModulePullback B S hS g').obj E))).obj K')
      (smallEtaleDerivedPullbackSheafHomMap g' E K ≫
        ((smallEtaleDerivedSheafHom B S hS X').obj
          (op ((smallEtaleDerivedModulePullback B S hS g').obj E))).map φ)
```

**`AlgebraicGeometry.Space.geometricPointwiseBaseChange_sheafHom_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/GeometricPointwiseBaseChangeTensorSheafHom.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/GeometricPointwiseBaseChangeTensorSheafHom.lean#L144). The attribute's comment: “(3), corrected: g of finite Tor dimension added; (3) as written is false, see Stacks.Examples.PseudoCoherentSheafHomBaseChange”.

> **The conditions of Stacks 0DKG pass to the derived internal Hom out of a pseudo-coherent
> object, for `g` of finite Tor dimension** (Stacks 0DKI (3), corrected). Part (3) of the source has
> no condition on `g` and is false as written: see
> `not_forall_geometricPointwiseBaseChange_sheafHom_of_isPseudoCoherent` in the namespace
> `Stacks.Examples.PseudoCoherentSheafHomBaseChange` (`A = ℤ/4`, `g : Spec ℤ/2 ⟶ Spec A`, where the
> map of Equation 0DKF fails in degree `1`). The source proof commutes the infinite products of
> `Hom^•(E_x, K_x)` with `⊗ᴸ R'`, which needs `R'` of finite Tor dimension. No boundedness of `K'` is
> assumed: on every affine étale chart it follows from the conditions for `(K, K', φ)`.

```lean
theorem geometricPointwiseBaseChange_sheafHom_of_isPseudoCoherent (sq : IsPullback g' f' f g)
    (hg : HasFiniteTorDimension g)
    (E : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hE : RingedSite.IsPseudoCoherent (smallEtaleRingedSite B S hS X.1 X.2) E)
    (K : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hK : DerivedCategoryB.derivedCategoryBPlus
          (A := SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X))
          (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
            ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))) K)
    (K' : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X')))
    (hK' : QcohDerived B S hS X' K')
    (φ : (smallEtaleDerivedModulePullback B S hS g').obj K ⟶ K')
    (h : GeometricPointwiseBaseChange B S hS f g f' g' sq.w K K' φ) :
    GeometricPointwiseBaseChange B S hS f g f' g' sq.w
      (((smallEtaleDerivedSheafHom B S hS X).obj (op E)).obj K)
      (((smallEtaleDerivedSheafHom B S hS X').obj
        (op ((smallEtaleDerivedModulePullback B S hS g').obj E))).obj K')
      (smallEtaleDerivedPullbackSheafHomMap g' E K ≫
        ((smallEtaleDerivedSheafHom B S hS X').obj
          (op ((smallEtaleDerivedModulePullback B S hS g').obj E))).map φ)
```

**`Stacks.Examples.PseudoCoherentSheafHomBaseChange.not_forall_geometricPointwiseBaseChange_sheafHom_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/PseudoCoherentSheafHomBaseChange.lean, line 908](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/PseudoCoherentSheafHomBaseChange.lean#L908). The attribute's comment: “(3) as written is false: the erratum's counterexample, A = Z/4, g : Spec Z/2 → Spec A”.

> **Stacks 0DKI (3) is false as written.** It is not true that
> for every cartesian square `g' ≫ f = f' ≫ g` of algebraic spaces, `K ∈ D_QCoh(𝒪_X)` bounded below
> and `φ : L(g')^*K ⟶ K'` in `D_QCoh(𝒪_{X'})` satisfying the conditions of Stacks 0DKG, and every
> pseudo-coherent `E`, the conditions of Stacks 0DKG hold for
> `L(g')^*R𝓗om(E, K) ⟶ R𝓗om(L(g')^*E, K')` (Stacks 08JF followed by `R𝓗om(L(g')^*E, φ)`). The
> counterexample has `Y = S = Spec ℤ/4` and `g : Spec ℤ/2 ⟶ S`, which has infinite Tor dimension:
> `not_geometricPointwiseBaseChange_sheafHom_residueObj`. The corrected statement, with `g` of finite
> Tor dimension, is
> `AlgebraicGeometry.Space.geometricPointwiseBaseChange_sheafHom_of_isPseudoCoherent`.

```lean
theorem not_forall_geometricPointwiseBaseChange_sheafHom_of_isPseudoCoherent :
    ¬ ∀ (B : BigFppfSite.{0}) (S : Scheme.{0}) (hS : B.Contains S)
      (X Y X' Y' : AlgebraicSpaces B S hS) (f : X ⟶ Y) (g : Y' ⟶ Y) (f' : X' ⟶ Y') (g' : X' ⟶ X)
      (sq : IsPullback g' f' f g)
      (K : DerivedCategory (SheafOfModules.{0} (ringedToposStructureRingSheaf B S hS X))),
      QcohDerived B S hS X K →
      ∀ (K' : DerivedCategory (SheafOfModules.{0} (ringedToposStructureRingSheaf B S hS X'))),
      QcohDerived B S hS X' K' →
      ∀ (φ : (smallEtaleDerivedModulePullback B S hS g').obj K ⟶ K'),
      GeometricPointwiseBaseChange B S hS f g f' g' sq.w K K' φ →
      DerivedCategoryB.IsBoundedBelow K →
      ∀ (E : DerivedCategory (SheafOfModules.{0} (ringedToposStructureRingSheaf B S hS X))),
      RingedSite.IsPseudoCoherent (smallEtaleRingedSite B S hS X.1 X.2) E →
      GeometricPointwiseBaseChange B S hS f g f' g' sq.w
        (((smallEtaleDerivedSheafHom B S hS X).obj (op E)).obj K)
        (((smallEtaleDerivedSheafHom B S hS X').obj
          (op ((smallEtaleDerivedModulePullback B S hS g').obj E))).obj K')
        (smallEtaleDerivedPullbackSheafHomMap g' E K ≫
          ((smallEtaleDerivedSheafHom B S hS X').obj
            (op ((smallEtaleDerivedModulePullback B S hS g').obj E))).map φ)
```

## Tag 0A1K, a lemma

[Tag 0A1K](https://stacks.math.columbia.edu/tag/0A1K) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_smallEtaleDerivedBaseChangeComp_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeIso.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeIso.lean#L117).

> **Stacks 0A1K.** For a cartesian square of algebraic spaces with `f` quasi-compact and
> quasi-separated, `E ∈ D_QCoh(𝒪_X)` and a bounded above complex `𝒢^•` of quasi-coherent
> `𝒪_X`-modules flat over `Y`, the base change map
> `Lg^*Rf_*(E ⊗^L 𝒢^•) ⟶ Rf'_*(L(g')^*E ⊗^L (g')^*𝒢^•)` is an isomorphism.

```lean
theorem isIso_smallEtaleDerivedBaseChangeComp_derivedTensor
    (sq : IsPullback g' f' f g) (hfqc : IsQuasiCompact B S hS f.hom)
    (hfqs : IsQuasiSeparated B S hS f.hom)
    (E : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hE : QcohDerived B S hS X E)
    (G : CochainComplex (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)) ℤ)
    (hGb : ∃ b : ℤ, ∀ i, b < i → IsZero (G.X i)) (hq : ∀ n, (G.X n).IsQuasicoherentOnSite)
    (hfl : ∀ n, IsFlatOver B S hS X.2 f.hom (G.X n)) :
    IsIso (smallEtaleDerivedBaseChangeComp B S hS f g f' g' sq.w
      (((smallEtaleDerivedTensor B S hS X).obj E).obj (DerivedCategory.Q.obj G))
      (((smallEtaleDerivedTensor B S hS X').obj
        ((smallEtaleDerivedModulePullback B S hS g').obj E)).obj
        (DerivedCategory.Q.obj (((modulePullback B S hS g').mapHomologicalComplex
          (ComplexShape.up ℤ)).obj G)))
      ((smallEtaleDerivedPullbackTensorIso g').hom.app (E, DerivedCategory.Q.obj G) ≫
        ((smallEtaleDerivedTensor B S hS X').obj
          ((smallEtaleDerivedModulePullback B S hS g').obj E)).map
          (smallEtaleDerivedModulePullbackQComparison g' G)))
```

## Tag 08JQ, a lemma

[Tag 08JQ](https://stacks.math.columbia.edu/tag/08JQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_smallEtaleDerivedSheafHomBaseChangeMap_and_not_forall_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeSheafHomErratum.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeSheafHomErratum.lean#L79). The attribute's comment: “erratum: as printed, part (2) (E pseudo-coherent, G bounded and flat over Y, an arbitrary base change g) is false, refuted for X = Y = Spec Z/4, f = id, E = (Z/4/2)~, G = O\_X and g the closed point Spec Z/2 -> Spec Z/4 (third conjunct); it holds when g has finite Tor dimension (second conjunct); part (1) holds as printed (first conjunct)”.

> Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of algebraic spaces,
> `E ∈ D(𝒪_X)` and `𝒢^•` a complex of quasi-coherent `𝒪_X`-modules, each `𝒢^n` flat over `Y`. For
> every cartesian square, the base change map
> `Lg^*Rf_*R𝓗om(E, 𝒢^•) ⟶ Rf'_*R𝓗om(L(g')^*E, (g')^*𝒢^•)` is an isomorphism if
>
> 1. `E` is perfect and `𝒢^•` is bounded above (the source's part (1), at its hypotheses), or
> 2. `E` is pseudo-coherent, `𝒢^•` is bounded, and `g` has finite Tor dimension.
>
> Part (2) as printed, for an arbitrary base change `g`, is false, and the third conjunct proves
> it: it fails for `X = Y = Spec ℤ/4`, `f = id`, `E = (ℤ/4 ⧸ 2)^~`, `𝒢^• = 𝒪_X` and
> `g = g' : Spec ℤ/2 ⟶ Spec ℤ/4`, where the source of the map lies in `D^{≤ 0}` (`ℤ/4` is
> self-injective) and the target has nonzero cohomology in degree `1`
> (`not_forall_isIso_smallEtaleDerivedSheafHomBaseChangeMap_of_isPseudoCoherent`, in the namespace
> `AlgebraicGeometry.Space.SheafHomBaseChangeCounterexample`). The source proves (2) through
> Stacks 0DKH and 0DKI (3); Stacks 0DKI (3) needs `g` of finite Tor dimension, and with that
> condition the proof goes through
> (`AlgebraicGeometry.Space.isIso_smallEtaleDerivedSheafHomBaseChangeMap_of_isPseudoCoherent`). The
> morphism `Spec ℤ/2 ⟶ Spec ℤ/4` of the counterexample does not have finite Tor dimension.

```lean
theorem isIso_smallEtaleDerivedSheafHomBaseChangeMap_and_not_forall_isIso
    (f : X ⟶ Y) (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (E : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (G : CochainComplex (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)) ℤ)
    (hq : ∀ n, (G.X n).IsQuasicoherentOnSite)
    (hfl : ∀ n, IsFlatOver B S hS X.2 f.hom (G.X n)) :
    (RingedSite.IsPerfect (smallEtaleRingedSite B S hS X.1 X.2) E →
      (∃ b : ℤ, ∀ i, b < i → IsZero (G.X i)) →
      ∀ {X' Y' : AlgebraicSpaces B S hS} (g : Y' ⟶ Y) (f' : X' ⟶ Y') (g' : X' ⟶ X)
        (sq : IsPullback g' f' f g),
        IsIso (smallEtaleDerivedSheafHomBaseChangeMap f g f' g' sq.w E G)) ∧
    (RingedSite.IsPseudoCoherent (smallEtaleRingedSite B S hS X.1 X.2) E →
      (∃ a b : ℤ, ∀ i, (i < a ∨ b < i) → IsZero (G.X i)) →
      ∀ {X' Y' : AlgebraicSpaces B S hS} (g : Y' ⟶ Y) (f' : X' ⟶ Y') (g' : X' ⟶ X)
        (sq : IsPullback g' f' f g), HasFiniteTorDimension g →
        IsIso (smallEtaleDerivedSheafHomBaseChangeMap f g f' g' sq.w E G)) ∧
    ¬ ∀ {B : BigFppfSite.{0}} {S : Scheme.{0}} {hS : B.Contains S} {X Y : AlgebraicSpaces B S hS}
      (f : X ⟶ Y), IsQuasiCompact B S hS f.hom → IsQuasiSeparated B S hS f.hom →
      ∀ (E : DerivedCategory (SheafOfModules.{0} (ringedToposStructureRingSheaf B S hS X))),
        RingedSite.IsPseudoCoherent (smallEtaleRingedSite B S hS X.1 X.2) E →
      ∀ (G : CochainComplex (SheafOfModules.{0} (ringedToposStructureRingSheaf B S hS X)) ℤ),
        (∀ n, (G.X n).IsQuasicoherentOnSite) → (∀ n, IsFlatOver B S hS X.2 f.hom (G.X n)) →
        (∃ a b : ℤ, ∀ i, (i < a ∨ b < i) → IsZero (G.X i)) →
      ∀ {X' Y' : AlgebraicSpaces B S hS} (g : Y' ⟶ Y) (f' : X' ⟶ Y') (g' : X' ⟶ X)
        (sq : IsPullback g' f' f g),
        IsIso (smallEtaleDerivedSheafHomBaseChangeMap f g f' g' sq.w E G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.21, Tag 0DKE](https://stacks.math.columbia.edu/tag/0DKE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
