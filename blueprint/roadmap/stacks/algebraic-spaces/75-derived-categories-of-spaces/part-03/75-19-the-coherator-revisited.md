---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isLeftAdjoint_ι_derivedCategoryB_isQuasicoherentOnSite, AlgebraicGeometry.Space.quasicoherentDerivedInclusion_isLeftAdjoint_of_qcqs, AlgebraicGeometry.Space.quasicoherentDerivedPushforwardCompCoheratorIso, AlgebraicGeometry.Space.coherator_edsMayerVietoris_triangle, AlgebraicGeometry.Space.exists_isZero_homology_coherator_obj, AlgebraicGeometry.Space.isDerivedLimit_coherator_obj, AlgebraicGeometry.Space.nonempty_homology_chartSections_iso_of_isDerivedLimit_single, AlgebraicGeometry.Space.isZero_homology_chartSections_of_isDerivedLimit_single
statement: formalized
proof: formalized
---

# 75.19 The coherator revisited

Section 75.19 of the Stacks Project, [Tag 0CR3](https://stacks.math.columbia.edu/tag/0CR3). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CR4, a lemma

[Tag 0CR4](https://stacks.math.columbia.edu/tag/0CR4) in the Stacks Project.

**`AlgebraicGeometry.Space.isLeftAdjoint_ι_derivedCategoryB_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoherator.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoherator.lean#L365).

> **Stacks 0CR4.**  Let `S` be a scheme and `X` a quasi-compact and quasi-separated algebraic
> space over `S`.  The inclusion functor `D_QCoh(𝒪_X) ⥤ D(𝒪_X)` has a right adjoint, the coherator
> `DQ_X`.
>
> This is the source's first proof: the induction principle of Stacks 08GP
> (`AlgebraicGeometry.Space.isLeftAdjoint_ι_of_forall_isAffineSpace`) from the affine case
> (`AlgebraicGeometry.Space.isLeftAdjoint_ι_of_isAffineSpace`).  The statement holds at every model
> of the derived category `D(𝒪_X)`, by the model comparison
> `StacksDraft.DerivedModel.isLeftAdjoint_ι_derivedCategoryB_of_model`.

```lean
theorem isLeftAdjoint_ι_derivedCategoryB_isQuasicoherentOnSite
    (X : AlgebraicSpaces B S hS) (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (h : HasDerivedCategory.{w} (Modules.{u, u} B S hS X.1 X.2)) :
    (@DerivedCategoryB.derivedCategoryB _ _ _ h
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))).ι.IsLeftAdjoint
```

**`AlgebraicGeometry.Space.quasicoherentDerivedInclusion_isLeftAdjoint_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/QcqsCoherator.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/QcqsCoherator.lean#L109).

> **Stacks 0CR4.**  Let `S` be a scheme and let `X` be a quasi-compact and quasi-separated
> algebraic space over `S`.  The inclusion functor `D_QCoh(𝒪_X) ⥤ D(𝒪_X)` has a right adjoint.
>
> The proof is the source's first one; see the module documentation.  The conclusion is
> `CategoryTheory.Functor.IsLeftAdjoint`, the existence of a right adjoint, which is what the tag
> asserts.

```lean
theorem quasicoherentDerivedInclusion_isLeftAdjoint_of_qcqs
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hFqc : IsQuasiCompactSpace B S hS F) (hFqs : IsAbsolutelyQuasiSeparated B S hS hZ F) :
    (qcohDerivedProp B S hS ⟨F, hF⟩).ι.IsLeftAdjoint
```

## Tag 0CR5, a lemma

[Tag 0CR5](https://stacks.math.columbia.edu/tag/0CR5) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.quasicoherentDerivedPushforwardCompCoheratorIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedAdjunction.lean#L102), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardTags.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardTags.lean#L29) (StacksFrontier).

## Tag 0CR6, a remark

[Tag 0CR6](https://stacks.math.columbia.edu/tag/0CR6) in the Stacks Project.

**`AlgebraicGeometry.Space.coherator_edsMayerVietoris_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CoheratorMayerVietoris.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CoheratorMayerVietoris.lean#L298).

> **Stacks 0CR6.**  Let `S` be a scheme and `(U ⊆ X, j_V : V ⟶ X)` an elementary distinguished
> square of algebraic spaces over `S` (here `X = W`, `U = Uo`, `j_V = fV`) with `X`, `U` and `V`
> quasi-compact and quasi-separated, and let `P = U ×_X V`.
>
> 1. *The functors `DQ_X`, `DQ_U`, `DQ_V`, `DQ_P` exist*: the four inclusions
>    `D_QCoh ⥤ D` have right adjoints (Stacks 0CR4, at the four spaces; `P` is quasi-compact and
>    quasi-separated by `AlgebraicGeometry.Space.isQuasiCompact_edsInterHom` and
>    `AlgebraicGeometry.Space.isQuasiSeparated_edsInterHom`).
> 2. *The canonical triangle*: for every choice of these right adjoints, with their adjunctions,
>    and every `K` in `D(𝒪_X)` there is a distinguished triangle
>
>    `DQ_X(K) ⟶ Rj_{U,*}DQ_U(K|_U) ⊕ Rj_{V,*}DQ_V(K|_V) ⟶ Rj_{P,*}DQ_P(K|_P) ⟶ DQ_X(K)[1]`
>
>    **whose two maps are the canonical ones**: the exact functor `DQ_X` applied to the two maps of
>    the Mayer–Vietoris triangle of Stacks 08GW
>    (`AlgebraicGeometry.Space.exists_mem_distTriang_edsDerivedRestrictPushMayerVietorisLowerShriek`,
>    whose maps are written out here verbatim: the derived units `K ⟶ R(j_{Y,*}(K|_Y))` and the
>    difference of the derived comparisons `R(j_{U,*}(K|_U)) ⟶ R(j_{P,*}(K|_P))`,
>    `R(j_{V,*}(K|_V)) ⟶ R(j_{P,*}(K|_P))`), conjugated by the three isomorphisms
>    `DQ_X(R(j_{Y,*}(K|_Y))) ≅ Rj_{Y,*}DQ_Y(K|_Y)`
>    (`AlgebraicGeometry.Space.coheratorRestrictPushObjIso`), which are Stacks 0CR5 for the étale
>    morphism `j_Y` composed with `DQ_X` of the canonical identification
>    `R(j_{Y,*}((-)|_Y)) ≅ Rj_{Y,*}((-)|_Y)`.  Only the connecting map is existentially
>    quantified, as in Stacks 08GW.
>
> `Rj_{Y,*}` is the chosen total right derived functor of the direct image along `j_Y`, and the
> derived categories are the standard model `HasDerivedCategory.standard`, in which Stacks 08GW is
> stated.  The hypotheses are the source's: `hWqc`, `hWqs` say that `X` is quasi-compact and
> quasi-separated, `hUqc`, `hUqs` that `U` is, and `hVqc`, `hVqs` that `V` is (quasi-separated in
> the absolute sense, over `Spec ℤ`, as in Stacks 0CR4).

```lean
theorem coherator_edsMayerVietoris_triangle
    (hWqc : IsQuasiCompactSpace B S hS W.1)
    (hWqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal W.1)
    (hUqc : IsQuasiCompactSpace B S hS Uo.toFunctor)
    (hUqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Uo.toFunctor)
    (hVqc : IsQuasiCompactSpace B S hS V)
    (hVqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal V) :
    ((qcohDerivedCategoryB B S hS W).ι.IsLeftAdjoint ∧
      (qcohDerivedCategoryB B S hS (edsOpen B S hS hsq)).ι.IsLeftAdjoint ∧
      (qcohDerivedCategoryB B S hS (edsEtale B S hS hsq)).ι.IsLeftAdjoint ∧
      (qcohDerivedCategoryB B S hS (edsInter B S hS hsq)).ι.IsLeftAdjoint) ∧
    ∀ (DQX : DerivedCategory (Modules.{u, u} B S hS W.1 W.2) ⥤
        (qcohDerivedCategoryB B S hS W).FullSubcategory)
      (adjX : (qcohDerivedCategoryB B S hS W).ι ⊣ DQX)
      (DQU : DerivedCategory (Modules.{u, u} B S hS (edsOpen B S hS hsq).1
          (edsOpen B S hS hsq).2) ⥤
        (qcohDerivedCategoryB B S hS (edsOpen B S hS hsq)).FullSubcategory)
      (adjU : (qcohDerivedCategoryB B S hS (edsOpen B S hS hsq)).ι ⊣ DQU)
      (DQV : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1
          (edsEtale B S hS hsq).2) ⥤
        (qcohDerivedCategoryB B S hS (edsEtale B S hS hsq)).FullSubcategory)
      (adjV : (qcohDerivedCategoryB B S hS (edsEtale B S hS hsq)).ι ⊣ DQV)
      (DQP : DerivedCategory (Modules.{u, u} B S hS (edsInter B S hS hsq).1
          (edsInter B S hS hsq).2) ⥤
        (qcohDerivedCategoryB B S hS (edsInter B S hS hsq)).FullSubcategory)
      (adjP : (qcohDerivedCategoryB B S hS (edsInter B S hS hsq)).ι ⊣ DQP)
      (K : DerivedCategory (Modules.{u, u} B S hS W.1 W.2)),
      ∃ δ, Triangle.mk
        (biprod.lift
          ((qcohDerivedCategoryB B S hS W).ι.map (DQX.map
            ((derivedUnitOfNatTrans (edsAdjOpen B S hS hsq).unit
              (edsDerivedRestrictPushOpen B S hS hsq)
              (edsTotalRightDerivedUnitOpen B S hS hsq)).app K)) ≫
            (coheratorRestrictPushObjIso B S hS (edsOpenHom B S hS hsq)
              (isEtale_edsOpenHom B S hS hsq)
              (isQuasiCompact_of_isQuasiCompactSpace B S hS B.contains_terminal W.2 hWqs hUqc _)
              (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS B.contains_terminal
                (edsOpen B S hS hsq).2 hUqs _)
              (edsDerivedRestrictPushOpen B S hS hsq) (edsTotalRightDerivedUnitOpen B S hS hsq)
              DQX adjX DQU adjU K).hom)
          ((qcohDerivedCategoryB B S hS W).ι.map (DQX.map
            ((derivedUnitOfNatTrans (edsAdjEtale B S hS hsq).unit
              (edsDerivedRestrictPushEtale B S hS hsq)
              (edsTotalRightDerivedUnitEtale B S hS hsq)).app K)) ≫
            (coheratorRestrictPushObjIso B S hS (edsEtaleHom B S hS hsq)
              (isEtale_edsEtaleHom B S hS hsq)
              (isQuasiCompact_of_isQuasiCompactSpace B S hS B.contains_terminal W.2 hWqs hVqc _)
              (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS B.contains_terminal
                (edsEtale B S hS hsq).2 hVqs _)
              (edsDerivedRestrictPushEtale B S hS hsq) (edsTotalRightDerivedUnitEtale B S hS hsq)
              DQX adjX DQV adjV K).hom))
        (biprod.desc
          ((coheratorRestrictPushObjIso B S hS (edsOpenHom B S hS hsq)
              (isEtale_edsOpenHom B S hS hsq)
              (isQuasiCompact_of_isQuasiCompactSpace B S hS B.contains_terminal W.2 hWqs hUqc _)
              (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS B.contains_terminal
                (edsOpen B S hS hsq).2 hUqs _)
              (edsDerivedRestrictPushOpen B S hS hsq) (edsTotalRightDerivedUnitOpen B S hS hsq)
              DQX adjX DQU adjU K).inv ≫
            (qcohDerivedCategoryB B S hS W).ι.map (DQX.map
            ((Functor.rightDerivedNatTrans (edsDerivedRestrictPushOpen B S hS hsq)
              (edsDerivedRestrictPushInter B S hS hsq)
              (edsTotalRightDerivedUnitOpen B S hS hsq)
              (edsTotalRightDerivedUnitInter B S hS hsq)
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
              (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                (conjugateEquiv ((edsAdjOpen B S hS hsq).comp
                    (edsLowerShriekAdjOpen B S hS hsq))
                  ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
                  (edsShriekOpenComparison B S hS hsq (edsLowerShriekAdjOpen B S hS hsq)
                    (edsLowerShriekAdjInter B S hS hsq)))
                (ComplexShape.up ℤ)) DerivedCategory.Qh)).app K)) ≫
            (coheratorRestrictPushObjIso B S hS (edsInterHom B S hS hsq)
              (isEtale_edsInterHom B S hS hsq)
              (isQuasiCompact_edsInterHom B S hS hsq hWqs hUqc hVqc)
              (isQuasiSeparated_edsInterHom B S hS hsq hUqs hVqs)
              (edsDerivedRestrictPushInter B S hS hsq) (edsTotalRightDerivedUnitInter B S hS hsq)
              DQX adjX DQP adjP K).hom)
          ((coheratorRestrictPushObjIso B S hS (edsEtaleHom B S hS hsq)
              (isEtale_edsEtaleHom B S hS hsq)
              (isQuasiCompact_of_isQuasiCompactSpace B S hS B.contains_terminal W.2 hWqs hVqc _)
              (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS B.contains_terminal
                (edsEtale B S hS hsq).2 hVqs _)
              (edsDerivedRestrictPushEtale B S hS hsq) (edsTotalRightDerivedUnitEtale B S hS hsq)
              DQX adjX DQV adjV K).inv ≫
            (qcohDerivedCategoryB B S hS W).ι.map (DQX.map
            (-((Functor.rightDerivedNatTrans (edsDerivedRestrictPushEtale B S hS hsq)
              (edsDerivedRestrictPushInter B S hS hsq)
              (edsTotalRightDerivedUnitEtale B S hS hsq)
              (edsTotalRightDerivedUnitInter B S hS hsq)
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
              (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                (conjugateEquiv ((edsAdjEtale B S hS hsq).comp
                    (edsLowerShriekAdjEtale B S hS hsq))
                  ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
                  (edsShriekEtaleComparison B S hS hsq (edsLowerShriekAdjEtale B S hS hsq)
                    (edsLowerShriekAdjInter B S hS hsq)))
                (ComplexShape.up ℤ)) DerivedCategory.Qh)).app K))) ≫
            (coheratorRestrictPushObjIso B S hS (edsInterHom B S hS hsq)
              (isEtale_edsInterHom B S hS hsq)
              (isQuasiCompact_edsInterHom B S hS hsq hWqs hUqc hVqc)
              (isQuasiSeparated_edsInterHom B S hS hsq hUqs hVqs)
              (edsDerivedRestrictPushInter B S hS hsq) (edsTotalRightDerivedUnitInter B S hS hsq)
              DQX adjX DQP adjP K).hom))
        δ ∈ distTriang (DerivedCategory (Modules.{u, u} B S hS W.1 W.2))
```

## Tag 0CSS, a lemma

[Tag 0CSS](https://stacks.math.columbia.edu/tag/0CSS) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isZero_homology_coherator_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorBounded.lean, line 757](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorBounded.lean#L757).

> **Stacks 0CSS.**  Let `S` be a scheme and `X` a quasi-compact and quasi-separated algebraic
> space over `S`, and let `DQ_X` be the right adjoint of the inclusion `D_QCoh(𝒪_X) ⥤ D(𝒪_X)`
> (Stacks 0CR4; any right adjoint, with its adjunction).  There is an integer `N = N(X)` such that
> for all integers `a`, `b` and every `K` in `D(𝒪_X)` with `H^i(U, K) = 0` for every affine `U`
> étale over `X` and every `i ∉ [a, b]`, the cohomology sheaves `H^i(DQ_X(K))` vanish for
> `i ∉ [a, b + N]`.
>
> The affine `U` étale over `X` are the étale charts `U` of `X` whose scheme is affine, and
> `H^i(U, K)` is the `i`-th cohomology of the complex of sections over `U` of a K-injective complex
> `I` representing `K`, i.e. of the unbounded derived sections `RΓ(U, K)`; the hypothesis is asked
> of every such representative.

```lean
theorem exists_isZero_homology_coherator_obj (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (DQ : DerivedCategory (Modules.{u, u} B S hS X.1 X.2) ⥤
      (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))).FullSubcategory)
    (adj : (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      (ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))).ι ⊣ DQ) :
    ∃ N : ℤ, ∀ (a b : ℤ) (K : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)),
      (∀ U : SmallEtale B S hS X.1, IsAffineChart B S hS X.1 U →
        ∀ I : CochainComplex (Modules.{u, u} B S hS X.1 X.2) ℤ, I.IsKInjective →
          Nonempty (DerivedCategory.Q.obj I ≅ K) → ∀ i : ℤ, i < a ∨ b < i →
            IsZero ((((chartSectionsAb B S hS X U).mapHomologicalComplex
              (ComplexShape.up ℤ)).obj I).homology i)) →
      ∀ i : ℤ, i < a ∨ b + N < i →
        IsZero ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) i).obj
          ((DerivedCategoryB.derivedCategoryB
            (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
              (ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))).ι.obj (DQ.obj K)))
```

## Tag 0CST, an example

[Tag 0CST](https://stacks.math.columbia.edu/tag/0CST) in the Stacks Project.

**`AlgebraicGeometry.Space.isDerivedLimit_coherator_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorInverseLimit.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorInverseLimit.lean#L107). The attribute's comment: “assertion DQ\_X(R lim F\_n) = (R lim in D\_QCoh(O\_X))(F\_n): for every right adjoint DQ of the inclusion D\_QCoh(O\_X) -> D(O\_X), at every model of D(O\_X), and every inverse system in D\_QCoh(O\_X); DQ\_X exists on a qcqs X by 0CR4”.

> **Stacks 0CST, the coherator commutes with derived limits.**  Let `X` be an algebraic space
> over `S`, `DQ` a right adjoint of the inclusion `ι : D_QCoh(𝒪_X) ⥤ D(𝒪_X)` and `F` an inverse
> system in `D_QCoh(𝒪_X)`.  If `L` is a derived limit of `F` computed in `D(𝒪_X)`, then the
> product of `F` exists in `D_QCoh(𝒪_X)` and `DQ L` is a derived limit of `F` there:
> `DQ_X(R lim Fₙ) = (R lim in D_QCoh(𝒪_X))(Fₙ)`.
>
> Such a `DQ` exists when `X` is quasi-compact and quasi-separated, by Stacks 0CR4
> (`AlgebraicGeometry.Space.isLeftAdjoint_ι_derivedCategoryB_isQuasicoherentOnSite`); the system of
> the source is the system of quasi-coherent sheaves `(𝓕ₙ)`, placed in degree `0`.

```lean
theorem isDerivedLimit_coherator_obj
    (DQ : DerivedCategory (Modules.{u, u} B S hS X.1 X.2) ⥤
      (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))).FullSubcategory)
    (adj : (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      (ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))).ι ⊣ DQ)
    (F : ℕᵒᵖ ⥤ (DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))).FullSubcategory)
    [HasProduct fun n : ℕ ↦ (F ⋙ (DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))).ι).obj (op n)]
    (L : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hL : IsDerivedLimit (F ⋙ (DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))).ι) L) :
    ∃ h : HasProduct fun n : ℕ ↦ F.obj (op n),
      letI := h
      IsDerivedLimit F (DQ.obj L)
```

**`AlgebraicGeometry.Space.nonempty_homology_chartSections_iso_of_isDerivedLimit_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorInverseLimit.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorInverseLimit.lean#L254). The attribute's comment: “assertion H^i(U, K) = H^i(R lim Gamma(U, F\_n)) for K = R lim F\_n in D(O\_X) and U affine etale over X; R lim Gamma(U, F\_n) is any derived limit in D(Ab), at any models; H^i(U, K) is computed on a K-injective representative, as in 0CSS”.

> **Stacks 0CST, `H^i(U, K) = H^i(R lim Γ(U, 𝓕ₙ))`.**  Let `(𝓕ₙ)` be an inverse system of
> quasi-coherent `𝒪_X`-modules on an algebraic space `X`, let `L = R lim 𝓕ₙ` be a derived limit in
> `D(𝒪_X)` of the system `(𝓕ₙ)` placed in degree `0`, and let `U` be an affine étale chart of `X`.
> Then for every derived limit `R = R lim Γ(U, 𝓕ₙ)` in `D(Ab)` of the abelian groups `Γ(U, 𝓕ₙ)`
> placed in degree `0`, and every `i`, `H^i(U, L) ≅ H^i(R)`.
>
> `H^i(U, L)` is the cohomology of the complex of sections over `U` of any K-injective complex `I`
> representing `L`.

```lean
theorem nonempty_homology_chartSections_iso_of_isDerivedLimit_single
    (𝓕 : ℕᵒᵖ ⥤ Modules.{u, u} B S hS X.1 X.2)
    (hqc : ∀ n : ℕ, (𝓕.obj (op n)).IsQuasicoherentOnSite)
    [HasProduct fun n : ℕ ↦
      (𝓕 ⋙ DerivedCategory.singleFunctor (Modules.{u, u} B S hS X.1 X.2) 0).obj (op n)]
    (L : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hL : IsDerivedLimit (𝓕 ⋙ DerivedCategory.singleFunctor _ 0) L)
    (U : SmallEtale B S hS X.1) (hU : IsAffineChart B S hS X.1 U)
    (I : CochainComplex (Modules.{u, u} B S hS X.1 X.2) ℤ) (hI : I.IsKInjective)
    (eI : Nonempty (DerivedCategory.Q.obj I ≅ L))
    [HasProduct fun n : ℕ ↦ (𝓕 ⋙ chartSectionsAb B S hS X U ⋙
      DerivedCategory.singleFunctor AddCommGrpCat.{u} 0).obj (op n)]
    (R : DerivedCategory AddCommGrpCat.{u})
    (hR : IsDerivedLimit (𝓕 ⋙ chartSectionsAb B S hS X U ⋙
      DerivedCategory.singleFunctor AddCommGrpCat.{u} 0) R)
    (i : ℤ) :
    Nonempty ((((chartSectionsAb B S hS X U).mapHomologicalComplex (ComplexShape.up ℤ)).obj
      I).homology i ≅ (DerivedCategory.homologyFunctor AddCommGrpCat.{u} i).obj R)
```

**`AlgebraicGeometry.Space.isZero_homology_chartSections_of_isDerivedLimit_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorInverseLimit.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorInverseLimit.lean#L289). The attribute's comment: “assertion H^i(U, R lim F\_n) = 0 for i outside [0, 1] and U affine etale over X, at any model of D(O\_X)”.

> **Stacks 0CST, `H^i(U, K) = 0` unless `i ∈ [0, 1]`.**  Let `(𝓕ₙ)` be an inverse system of
> quasi-coherent `𝒪_X`-modules on an algebraic space `X` and `L = R lim 𝓕ₙ` a derived limit in
> `D(𝒪_X)` of the system `(𝓕ₙ)` placed in degree `0`.  Then `H^i(U, L) = 0` for every affine étale
> chart `U` of `X` and every `i ∉ [0, 1]`.

```lean
theorem isZero_homology_chartSections_of_isDerivedLimit_single
    (𝓕 : ℕᵒᵖ ⥤ Modules.{u, u} B S hS X.1 X.2)
    (hqc : ∀ n : ℕ, (𝓕.obj (op n)).IsQuasicoherentOnSite)
    [HasProduct fun n : ℕ ↦
      (𝓕 ⋙ DerivedCategory.singleFunctor (Modules.{u, u} B S hS X.1 X.2) 0).obj (op n)]
    (L : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hL : IsDerivedLimit (𝓕 ⋙ DerivedCategory.singleFunctor _ 0) L)
    (U : SmallEtale B S hS X.1) (hU : IsAffineChart B S hS X.1 U)
    (I : CochainComplex (Modules.{u, u} B S hS X.1 X.2) ℤ) (hI : I.IsKInjective)
    (eI : Nonempty (DerivedCategory.Q.obj I ≅ L)) (i : ℤ) (hi : i < 0 ∨ 1 < i) :
    IsZero ((((chartSectionsAb B S hS X U).mapHomologicalComplex (ComplexShape.up ℤ)).obj
      I).homology i)
```

**`AlgebraicGeometry.Space.exists_isZero_homology_coherator_obj_of_isDerivedLimit_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorInverseLimit.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorInverseLimit.lean#L344). The attribute's comment: “conclusion: the R lim in D\_QCoh(O\_X), i.e. DQ\_X(R lim F\_n), lies in D^b\_QCoh(O\_X) and has vanishing cohomology sheaves in negative degrees (in [0, 1 + N], N = N(X) uniform), by 0CSS; at the standard model, the one of 0CSS”.

> **Stacks 0CST, `DQ_X(R lim 𝓕ₙ)` is in `D^b_QCoh(𝒪_X)` with no negative cohomology.**  Let
> `X` be a quasi-compact and quasi-separated algebraic space over `S` and `DQ` a right adjoint of
> the inclusion `D_QCoh(𝒪_X) ⥤ D(𝒪_X)`.  There is an integer `N` such that for every inverse system
> `(𝓕ₙ)` of quasi-coherent `𝒪_X`-modules and every derived limit `L = R lim 𝓕ₙ` in `D(𝒪_X)` of
> `(𝓕ₙ)` placed in degree `0`, the cohomology sheaves `H^i(DQ L)` vanish for `i < 0` and for
> `i > 1 + N`.  By `AlgebraicGeometry.Space.isDerivedLimit_coherator_obj`, `DQ L` is the `R lim`
> of `(𝓕ₙ)` in `D_QCoh(𝒪_X)`.
>
> This is Stacks 0CSS (`AlgebraicGeometry.Space.exists_isZero_homology_coherator_obj`) with
> `[a, b] = [0, 1]`.

```lean
theorem exists_isZero_homology_coherator_obj_of_isDerivedLimit_single (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (DQ : DerivedCategory (Modules.{u, u} B S hS X.1 X.2) ⥤
      (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))).FullSubcategory)
    (adj : (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      (ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))).ι ⊣ DQ) :
    ∃ N : ℤ, ∀ (𝓕 : ℕᵒᵖ ⥤ Modules.{u, u} B S hS X.1 X.2),
      (∀ n : ℕ, (𝓕.obj (op n)).IsQuasicoherentOnSite) →
      ∀ [HasProduct fun n : ℕ ↦
        (𝓕 ⋙ DerivedCategory.singleFunctor (Modules.{u, u} B S hS X.1 X.2) 0).obj (op n)]
        (L : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)),
        IsDerivedLimit (𝓕 ⋙ DerivedCategory.singleFunctor _ 0) L →
        ∀ i : ℤ, i < 0 ∨ 1 + N < i →
          IsZero ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) i).obj
            ((DerivedCategoryB.derivedCategoryB
              (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
                (ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))).ι.obj (DQ.obj L)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.19, Tag 0CR3](https://stacks.math.columbia.edu/tag/0CR3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
