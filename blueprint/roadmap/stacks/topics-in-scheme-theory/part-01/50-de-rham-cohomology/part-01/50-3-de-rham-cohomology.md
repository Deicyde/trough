---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.deRhamCohomology, AlgebraicGeometry.Scheme.Hom.deRhamCohomologyBaseModule, AlgebraicGeometry.Scheme.Hom.deRhamDerivedSectionsPullback, AlgebraicGeometry.Scheme.Hom.deRhamCohomologyPullback, Stacks.AlgebraicGeometry.AffineDifferentialsIso.deRhamSectionsComplexIso, Stacks.AlgebraicGeometry.AffineDifferentialsIso.derivedDeRhamSectionsIso, Stacks.AlgebraicGeometry.AffineDifferentialsIso.deRhamCohomologyIsoInt, Stacks.AlgebraicGeometry.AffineDifferentialsIso.differentialFormsSectionsIso
statement: formalized
proof: formalized
---

# 50.3 de Rham cohomology

Section 50.3 of the Stacks Project, [Tag 0FL6](https://stacks.math.columbia.edu/tag/0FL6). 6 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FL6, the section

[Tag 0FL6](https://stacks.math.columbia.edu/tag/0FL6) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.deRhamCohomology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Functoriality.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Functoriality.lean#L513). The attribute's comment: “the definition `H^i_dR(X/S) = H^i(RΓ(X, Ω^•_{X/S}))`”.

> **Relative de Rham cohomology** `H^i_{dR}(X/S)` of a morphism of schemes: the `i`-th
> cohomology of the derived global sections of the relative de Rham complex.

```lean
noncomputable abbrev deRhamCohomology (p : X ⟶ S) (i : ℤ) : AddCommGrpCat.{u}
```

**`AlgebraicGeometry.Scheme.Hom.deRhamCohomologyBaseModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Functoriality.lean, line 529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Functoriality.lean#L529). The attribute's comment: “the `H^0(S, 𝒪_S)`-module structure on `H^i_dR(X/S)`”.

> **Relative de Rham cohomology is a module over `H^0(S, 𝒪_S)`**: the de Rham complex is a
> complex of `p^{-1}𝒪_S`-modules, so its hypercohomology is a module over `Γ(X, p^{-1}𝒪_S)`, and
> hence over `H^0(S, 𝒪_S)` along the unit of the inverse-image adjunction.

```lean
noncomputable def deRhamCohomologyBaseModule (p : X ⟶ S) (i : ℤ) :
    ModuleCat.{u} (S.sheaf.obj.obj (Opposite.op ⊤))
```

**`AlgebraicGeometry.Scheme.Hom.deRhamDerivedSectionsPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Functoriality.lean, line 540](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Functoriality.lean#L540). The attribute's comment: “the pullback map `f^* : RΓ(X, Ω^•_{X/S}) ⟶ RΓ(X', Ω^•_{X'/S'})`”.

> **The pullback map `f^* : RΓ(X, Ω^•_{X/S}) ⟶ RΓ(X', Ω^•_{X'/S'})`** of a commutative square
> of schemes: derived global sections of the canonical map of de Rham complexes, followed by the
> identification of derived global sections on `X'` with derived global sections of the derived
> direct image.

```lean
noncomputable def deRhamDerivedSectionsPullback (hcomm : f ≫ p = p' ≫ g) :
    (sectionsFunctor X.toRingedSpace.carrier ⊤).rightDerivedFunctorPlus.obj
        (DerivedCategory.Plus.Q.obj
          (SheafOfModules.deRhamAbelianComplexPlus (deRhamAlgebras p)
            (SheafOfModules.deRhamDifferential (deRhamAlgebras p)))) ⟶
      (sectionsFunctor X'.toRingedSpace.carrier ⊤).rightDerivedFunctorPlus.obj
        (DerivedCategory.Plus.Q.obj
          (SheafOfModules.deRhamAbelianComplexPlus (deRhamAlgebras p')
            (SheafOfModules.deRhamDifferential (deRhamAlgebras p'))))
```

**`AlgebraicGeometry.Scheme.Hom.deRhamCohomologyPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Functoriality.lean, line 561](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Functoriality.lean#L561). The attribute's comment: “the pullback map `f^* : H^i_dR(X/S) ⟶ H^i_dR(X'/S')`”.

> **The pullback map `f^* : H^i_{dR}(X/S) ⟶ H^i_{dR}(X'/S')`** of a commutative square of
> schemes: the map induced on cohomology by the pullback map on derived global sections.

```lean
noncomputable def deRhamCohomologyPullback (hcomm : f ≫ p = p' ≫ g) (i : ℤ) :
    deRhamCohomology p i ⟶ deRhamCohomology p' i
```

## Tag 0FLW, a lemma

[Tag 0FLW](https://stacks.math.columbia.edu/tag/0FLW) in the Stacks Project.

**`Stacks.AlgebraicGeometry.AffineDifferentialsIso.deRhamSectionsComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/DeRhamComplexComparison.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/DeRhamComplexComparison.lean#L270). The attribute's comment: “Γ(Spec A, Ω^•) ≅ Ω^•_{A/R} as a cochain complex of R-modules; not derived”.

> **[Stacks Project, Tag 0FLW] at the level of complexes.** For a morphism of affine schemes
> `Spec φ : Spec A ⟶ Spec R`, the global relative differential forms of `Spec φ` are the algebraic
> de Rham complex `Ω^•_{A/R} = (⋀^•_A Ω[A⁄R], d)` **as a cochain complex of `R`-modules**: the
> degreewise comparison of
> `Stacks.AlgebraicGeometry.AffineDifferentialsIso.differentialFormsSectionsIso` commutes with the
> de Rham differential in every degree, not only in degree zero.
>
> This is the comparison the tag's proof starts from, complete as a statement about complexes.
> The tag's two assertions — that `RΓ(Spec A, Ω^•_{Spec A/Spec R})` is `Ω^•_{A/R}` in `D(R)`, and
> the resulting statement about de Rham cohomology — are *not* proved here, since `Γ` is not `RΓ`;
> the passage needs the affine acyclicity of a quasi-coherent sheaf together with Leray's
> acyclicity lemma, and it is carried out in
> `StacksFrontier.AlgebraicGeometry.AffineDifferentialsIso.DeRhamDerived`, where
> `Stacks.AlgebraicGeometry.AffineDifferentialsIso.derivedDeRhamSectionsIso` and
> `Stacks.AlgebraicGeometry.AffineDifferentialsIso.deRhamCohomologyIsoInt` take this
> isomorphism as their starting point.

```lean
def deRhamSectionsComplexIso : ringDeRhamComplex φ ≅ deRhamSectionsComplex φ
```

**`Stacks.AlgebraicGeometry.AffineDifferentialsIso.derivedDeRhamSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/DeRhamDerived.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/DeRhamDerived.lean#L252). The attribute's comment: “RΓ(Spec A, Ω^•) ≅ Ω^•_{A/R} in D(R)”.

> **[Stacks Project, Tag 0FLW], the derived statement.** For a morphism of affine schemes
> `Spec φ : Spec A ⟶ Spec R` the algebraic de Rham complex `Ω^•_{A/R}` computes the derived global
> sections of the relative de Rham complex:
>
> $$ R\Gamma(\operatorname{Spec} A, \Omega^\bullet_{\operatorname{Spec} A/\operatorname{Spec} R})
>   = \Omega^\bullet_{A/R} \quad\text{in } D(R). $$
>
> Both objects are read in `D(R)`: the left-hand side through
> `Stacks.Cohomology.DerivedSectionsOverBase.derivedSectionsOver` along the base ring map
> `AlgebraicGeometry.Scheme.Hom.affineBaseRingMap`, the right-hand side as the extension by zero of
> `KaehlerDifferential.deRhamComplex`.
>
> The comparison is the composite of three isomorphisms: the complex-level comparison
> `deRhamSectionsComplexIso` of global differential forms with `Ω^•_{A/R}`, the interchange of
> extension by zero with a degreewise functor, and the invertibility of
> `Γ ⟶ RΓ` supplied by Leray's acyclicity lemma at a bounded below complex of acyclic terms.

```lean
def derivedDeRhamSectionsIso :
    DerivedCategory.Q.obj ((ringDeRhamComplex φ).extend ComplexShape.embeddingUpNat) ≅
      (derivedDeRhamSections φ).obj (DerivedCategory.Q.obj (deRhamComplexInt φ))
```

**`Stacks.AlgebraicGeometry.AffineDifferentialsIso.deRhamCohomologyIsoInt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/DeRhamDerived.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/DeRhamDerived.lean#L274). The attribute's comment: “H^i_dR(Spec A/Spec R) ≅ H^i(Ω^•_{A/R})”.

> **[Stacks Project, Tag 0FLW], the cohomology statement.** De Rham cohomology of a morphism of
> affine schemes is the cohomology of the algebraic de Rham complex:
> `H^i_{dR}(Spec A/Spec R) = H^i(Ω^•_{A/R})`, in every integer degree.

```lean
def deRhamCohomologyIsoInt (i : ℤ) :
    ((ringDeRhamComplex φ).extend ComplexShape.embeddingUpNat).homology i ≅
      deRhamCohomologyOver φ i
```

**`Stacks.AlgebraicGeometry.AffineDifferentialsIso.differentialFormsSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/DeRhamSections.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/DeRhamSections.lean#L174). The attribute's comment: “degreewise only: `⋀^p_A Ω[A⁄R] ≅ Γ(Spec A, Ω^p)` for every `p`; no differential”.

> **The global relative differential `p`-forms of `Spec φ : Spec A ⟶ Spec R` are
> `⋀^p_A Ω[A⁄R]`, as `A`-modules.** The sheaf of relative differential `p`-forms is the
> quasi-coherent sheaf attached to that module, and the unit of the adjunction between the
> associated-sheaf functor and global sections recovers a module from its quasi-coherent sheaf.
>
> This is the degreewise half of [Stacks Project, Tag 0FLW]: it matches the terms of the two
> complexes the tag compares, in every degree, and no differential.

```lean
noncomputable def differentialFormsSectionsIso (p : ℕ) :
    ModuleCat.of ↥A ↥(⋀[↥A]^p ↥(CommRingCat.KaehlerDifferential φ)) ≅
      moduleSpecΓFunctor.obj (Scheme.Hom.relativeDifferentialForms (Spec.map φ) (p : ℤ))
```

**`Stacks.AlgebraicGeometry.AffineDifferentialsIso.deRhamComplex_d_zero_one_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/DeRhamSections.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/DeRhamSections.lean#L250). The attribute's comment: “the degree-zero differential square only; no differential in positive degree”.

> **The first differential of the relative de Rham complex of `Spec φ`, read on global
> sections, is the universal derivation of `A` over `R`.** On the degree-zero form `b · 1` attached
> to a global section `b` of `𝒪_{Spec A}` it is the universal differential of the element of `A`
> corresponding to `b`, viewed in the global differential `1`-forms through the degree-one
> comparison.
>
> This is the one square of [Stacks Project, Tag 0FLW] that is matched; the differential in
> positive degree is not.

```lean
theorem deRhamComplex_d_zero_one_apply (b : ↥((Spec A).sheaf.obj.obj (op ⊤))) :
    (((Spec.map φ).deRhamComplex).d 0 1).val.app (op ⊤)
        (b • (Scheme.Hom.deRhamAlgebras (Spec.map φ)).exterior.one.eval (op ⊤)) =
      (oneFormsSectionsIso φ).hom.hom
        (CommRingCat.KaehlerDifferential.d ((Scheme.ΓSpecIso A).hom b))
```

## Tag 0FLX, a lemma

[Tag 0FLX](https://stacks.math.columbia.edu/tag/0FLX) in the Stacks Project.

**`Stacks.DeRhamDirectImage.isQuasicoherent_homology_derivedDeRhamDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DerivedDirectImage.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DerivedDirectImage.lean#L328).

> **Stacks Project, Tag 0FLX.** For a quasi-compact and quasi-separated morphism of schemes
> `p : X ⟶ S` the derived direct image `Rp_*Ω^•_{X/S}` of the relative de Rham complex is an
> object of `D_QCoh(𝒪_S)`: every one of its cohomology sheaves is quasi-coherent.

```lean
theorem isQuasicoherent_homology_derivedDeRhamDirectImage [QuasiCompact f] [QuasiSeparated f]
    (i : ℤ) :
    ((DerivedCategory.Plus.homologyFunctor S.Modules i).obj
      (derivedDeRhamDirectImage f)).IsQuasicoherent
```

**`Stacks.DeRhamDirectImage.derivedCategoryB_derivedDeRhamDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DerivedDirectImage.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DerivedDirectImage.lean#L379).

> **Stacks Project, Tag 0FLX.** `Rp_*Ω^•_{X/S}` is an object of `D_QCoh(𝒪_S)`, in the
> membership form: the object property on `D(𝒪_S)` cutting out the complexes with quasi-coherent
> cohomology holds of it. Since `AlgebraicGeometry.Scheme.Hom.deRhamComplex` is bounded below, the
> derived direct image is read in `D⁺(𝒪_S)` and compared with `D(𝒪_S)` along the inclusion, under
> which the cohomology functors agree.

```lean
theorem derivedCategoryB_derivedDeRhamDirectImage [QuasiCompact f] [QuasiSeparated f] :
    DerivedCategoryB.derivedCategoryB (_root_.SheafOfModules.isQuasicoherent S.ringCatSheaf)
      (DerivedCategory.Plus.ι.obj (derivedDeRhamDirectImage f))
```

## Tag 0FLY, a lemma

[Tag 0FLY](https://stacks.math.columbia.edu/tag/0FLY) in the Stacks Project.

**`AlgebraicGeometry.DeRhamCoherentDirectImage.derivedCategoryB_derivedDeRhamDirectImage_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CoherentDirectImage.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CoherentDirectImage.lean#L277).

> **[Stacks, Tag 0FLY].** For a proper morphism `p : X ⟶ S` with `S` locally Noetherian,
> `Rp_*Ω^•_{X/S}` is an object of `D_Coh(𝒪_S)`.
>
> Coherence of the higher direct images `R^b p_* Ω^a_{X/S}` is [Stacks, Tag 02O5]; this library
> proves it with no hypothesis, in the affine-base form
> `AlgebraicGeometry.ProperCoherenceWitness.higherDirectImageIsCoherentOverAffineBase` that
> `StacksFrontier/AlgebraicGeometry/ProperCoherentImage/Basic.lean` shows equivalent to it.

```lean
theorem derivedCategoryB_derivedDeRhamDirectImage_of_isProper
    [IsLocallyNoetherian S] [IsProper f] :
    DerivedCategoryB.derivedCategoryB
      (fun M => M.IsCoherent) (DerivedCategory.Plus.ι.obj (derivedDeRhamDirectImage f))
```

## Tag 0FLZ, a lemma

[Tag 0FLZ](https://stacks.math.columbia.edu/tag/0FLZ) in the Stacks Project.

**`AlgebraicGeometry.DeRhamCohomologyDirectImage.moduleFinite_deRhamCohomologyBaseModule_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DeRhamCohomologyDirectImage.lean, line 437](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DeRhamCohomologyDirectImage.lean#L437).

> **[Stacks, Tag 0FLZ].** Let `A` be a Noetherian ring and let `X` be a proper scheme over
> `S = Spec A`. Then `H^i_{dR}(X/S)` is a finite `A`-module, for every `i`.
>
> The de Rham cohomology is the library's `AlgebraicGeometry.Scheme.Hom.deRhamCohomology`, read as
> an `A`-module along `A ≅ Γ(Spec A, 𝒪)`; no hypothesis beyond the tag's own is assumed. By
> [Stacks, Tag 0D5W] it is the cohomology of `RΓ(Spec A, Rp_*Ω^•_{X/S})`, whose cohomology sheaves
> are coherent by [Stacks, Tag 0FLY] — unconditionally, [Stacks, Tag 02O5] being discharged in
> this library — and over a Noetherian affine base the cohomology of derived global sections of a
> complex with coherent cohomology sheaves is a finite module.

```lean
theorem moduleFinite_deRhamCohomologyBaseModule_of_isProper [IsNoetherianRing A] [IsProper q]
    (i : ℤ) :
    Module.Finite A
      ((ModuleCat.restrictScalars (Scheme.ΓSpecIso (CommRingCat.of A)).inv.hom).obj
        (Scheme.Hom.deRhamCohomologyBaseModule q i))
```

## Tag 0FM0, a lemma

[Tag 0FM0](https://stacks.math.columbia.edu/tag/0FM0) in the Stacks Project.

**`AlgebraicGeometry.ProperSmoothDeRham.isIso_derivedBaseChangeMap_deRhamComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProperSmoothDeRhamBaseChange.lean, line 552](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProperSmoothDeRhamBaseChange.lean#L552). The attribute's comment: “formation of Rf_*Omega^bullet_X/S commutes with arbitrary change of base: for a proper smooth f and any cartesian square the derived base change map of Tag 08HY along the inverse-image ringed spaces, followed by the canonical map of de Rham complexes, is an isomorphism”.

> **Base change for `Rf_*Ω^•_{X/S}`.** Let `f : X ⟶ S` be a proper smooth morphism of schemes
> and let
>
> ```
> X' --g'--> X
> |          |
> f'         f
> v          v
> S' --g---> S
> ```
>
> be a cartesian square. Write `π : (X, f^{-1}𝒪_S) ⟶ S` and `π' : (X', f'^{-1}𝒪_{S'}) ⟶ S'`, so that
> `Rπ_*Ω^•_{X/S}` is `Rf_*Ω^•_{X/S}` as an object of `D(𝒪_S)`, and let
> `g₀ : (X', f'^{-1}𝒪_{S'}) ⟶ (X, f^{-1}𝒪_S)` be the induced morphism, lying over `g`. Then the
> canonical map
>
> `Lg^*Rπ_*Ω^•_{X/S} ⟶ Rπ'_*Lg₀^*Ω^•_{X/S} ⟶ Rπ'_*Ω^•_{X'/S'}`
>
> — the derived base change map of Stacks 08HY followed by `Rπ'_*` of
> `deRhamBaseChangeComparison` — is an isomorphism.

```lean
theorem isIso_derivedBaseChangeMap_deRhamComplex (hsq : IsPullback g' f' f g) [IsProper f]
    [Smooth f] :
    IsIso (derivedBaseChangeMap (inverseImageBaseMap g' f' f g hsq.w)
        (inverseImageBaseProjection f') (inverseImageBaseProjection f) g.toLRSHom.toShHom
        (inverseImageBaseMap_comp_inverseImageBaseProjection g' f' f g hsq.w)
        (DerivedCategory.Qh.obj ((HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj
          (deRhamComplexInt f))) ≫
      (derivedPushforward (inverseImageBaseProjection f')).map
        (deRhamBaseChangeComparison g' f' f g hsq.w))
```

**`AlgebraicGeometry.ProperSmoothDeRham.isPerfect_derivedPushforward_deRhamComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProperSmoothDeRhamPerfect.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProperSmoothDeRhamPerfect.lean#L177). The attribute's comment: “Rf_*Omega^bullet_X/S is a perfect object of D(O_S) for a proper smooth f: the derived direct image of the relative de Rham complex along (X, f^{-1}O_S) -> S”.

> **[Stacks, Tag 0FM0], perfectness of `Rf_*Ω^•_{X/S}`.** For a proper smooth morphism of
> schemes `f : X ⟶ S`, the derived direct image of the relative de Rham complex along
> `π : (X, f^{-1}𝒪_S) ⟶ S` is a perfect object of `D(𝒪_S)`.
>
> Perfectness is local on `S`. Over an affine open `V ⊆ S` the forms `Ω^p_{X/S}` vanish on
> `f^{-1}V` for `p` large, so the restriction to `V` of `Rπ_*σ_{≥p}Ω^•_{X/S}` vanishes; descending
> along the triangles `σ_{≥p+1} ⟶ σ_{≥p} ⟶ Ω^p[-p]` of the stupid filtration, the outer vertices
> have perfect images — the graded pieces by the perfectness of `Rf_*Ω^p_{X/S}` — and perfectness
> has the two-out-of-three property (Stacks 08CR).

```lean
theorem isPerfect_derivedPushforward_deRhamComplex [IsProper f] [Smooth f] :
    Stacks.Cohomology.PerfectComplexes.IsPerfect (X := S.toRingedSpace)
      ((derivedPushforward (inverseImageBaseProjection f)).obj
        (DerivedCategory.Q.obj (deRhamComplexInt f)))
```

**`AlgebraicGeometry.ProperSmoothDeRham.isIso_derivedBaseChangeMap_forms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProperSmoothFormsDirectImage.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProperSmoothFormsDirectImage.lean#L122). The attribute's comment: “formation of Rf_*Omega^p_X/S commutes with arbitrary change of base: for a proper smooth f and any cartesian square the derived base change map of Tag 08HY at Omega^p_X/S followed by Rf'_* of the canonical map L(g')^*Omega^p_X/S -> Omega^p_X'/S' is an isomorphism”.

> **Base change for `Rf_*Ω^p_{X/S}`.** Let `f : X ⟶ S` be a proper smooth morphism of schemes
> and let
>
> ```
> X' --g'--> X
> |          |
> f'         f
> v          v
> S' --g---> S
> ```
>
> be a cartesian square. Then the canonical map
>
> `Lg^*Rf_*Ω^p_{X/S} ⟶ Rf'_*L(g')^*Ω^p_{X/S} ⟶ Rf'_*Ω^p_{X'/S'}`
>
> — the derived base change map of Stacks 08HY followed by `Rf'_*` of the comparison
> `formsBaseChangeComparison` — is an isomorphism.

```lean
theorem isIso_derivedBaseChangeMap_forms {g' : X' ⟶ X} {f' : X' ⟶ S'} {f : X ⟶ S}
    {g : S' ⟶ S} (hsq : IsPullback g' f' f g) [IsProper f] [Smooth f] (p : ℕ) :
    IsIso (derivedBaseChangeMap g'.toLRSHom.toShHom f'.toLRSHom.toShHom f.toLRSHom.toShHom
        g.toLRSHom.toShHom (toShHom_comm hsq.w) (formsObj f p) ≫
      (derivedPushforward f'.toLRSHom.toShHom).map
        (formsBaseChangeComparison g' f' f g hsq.w p))
```

**`AlgebraicGeometry.ProperSmoothDeRham.isPerfect_derivedPushforward_forms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProperSmoothFormsDirectImage.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProperSmoothFormsDirectImage.lean#L197). The attribute's comment: “Rf_*Omega^p_X/S is a perfect object of D(O_S) for a proper smooth f, for every p >= 0, over an arbitrary base”.

> **Perfectness of `Rf_*Ω^p_{X/S}`.** For a proper smooth morphism of schemes `f : X ⟶ S`
> the derived direct image `Rf_*Ω^p_{X/S}` is a perfect object of `D(𝒪_S)`. Perfectness is local
> on `S`, its restriction to an affine open `V` is the derived direct image of `Ω^p` along the
> base change of `f` to `V` by base change, and over an affine base this is
> `isPerfect_derivedPushforward_forms_of_isAffine`.

```lean
theorem isPerfect_derivedPushforward_forms (f : X ⟶ S) [IsProper f] [Smooth f] (p : ℕ) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect (X := S.toRingedSpace)
      ((derivedPushforward f.toLRSHom.toShHom).obj (formsObj f p))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.3, Tag 0FL6](https://stacks.math.columbia.edu/tag/0FL6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
