---
declaration: section
origin: cited
lean: AlgebraicGeometry.isLocalizedModule_restriction_basicOpen_of_qcqs, AlgebraicGeometry.isLocalization_basicOpen_of_qcqs, Stacks.SheafOfModules.sectionLocalizationMap, Stacks.SheafOfModules.sectionLocalizationMap_fraction, Stacks.SheafOfModules.sectionLocalizationMap_smul, Stacks.SheafOfModules.sectionLocalizationMap_injective, Stacks.SheafOfModules.sectionLocalizationMap_bijective, Stacks.SheafOfModules.homAtNonvanishingOpen
statement: formalized
proof: formalized
---

# 28.18 Sections over principal opens

Section 28.18 of the Stacks Project, [Tag 0B5K](https://stacks.math.columbia.edu/tag/0B5K). 5 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01P7, a lemma

[Tag 01P7](https://stacks.math.columbia.edu/tag/01P7) in the Stacks Project.

**`AlgebraicGeometry.isLocalizedModule_restriction_basicOpen_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/Sections.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/Sections.lean#L77). The attribute's comment: “quasi-coherent modules”. References: EGA III (1.4.5), “H⁰, L = 𝒪_X, qcqs”.

> On a quasi-compact, quasi-separated open, restriction of sections of a quasi-coherent
> module to a principal open is localization at the defining function.

```lean
theorem isLocalizedModule_restriction_basicOpen_of_qcqs {X : Scheme.{u}} (M : X.Modules)
    [M.IsQuasicoherent] {U : X.Opens} (hU : IsCompact U.1) (hU' : IsQuasiSeparated U.1)
    (f : Γ(X, U)) :
    letI : Module Γ(X, U) Γ(M, X.basicOpen f) :=
      Module.compHom Γ(M, X.basicOpen f)
        (X.presheaf.map (homOfLE (X.basicOpen_le f)).op).hom
    IsLocalizedModule.Away f
      (Scheme.Modules.restrictionLinearMap M (homOfLE (X.basicOpen_le f)))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isLocalization_basicOpen_of_qcqs`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isLocalization_basicOpen_of_qcqs#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/Sections.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/Sections.lean#L93) (StacksFrontier): “the structure sheaf, for a quasi-compact quasi-separated open”. References: EGA I (1.4.1), “special case”; EGA I (9.3.2), “Case L = O”; EGA I (9.3.3), “special case”; EGA III (1.2.2), “special case”; EGA III (1.4.13), “q = 0 and F = O_X”; EGA III (1.4.6), “degree zero, F = O_X”; EGA III (2.1.2), “special case”.

## Tag 0B5L, an equation

[Tag 0B5L](https://stacks.math.columbia.edu/tag/0B5L) in the Stacks Project.

**`Stacks.SheafOfModules.sectionLocalizationMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/NonvanishingSections/LocalizationMap.lean, line 1079](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/NonvanishingSections/LocalizationMap.lean#L1079).

> The canonical map from degree-zero localized twisted sections to sections on `X_s`.
> It restricts a numerator to `X_s` and divides by the corresponding power of `s`.
> The section is invertible there, so this construction is independent of the fraction
> representative.

```lean
public noncomputable def sectionLocalizationMap (s : L.sections) :
    sectionAtNonvanishingOpen X L F s →+
      F.val.obj (op (nonvanishingOpen L s))
```

**`Stacks.SheafOfModules.sectionLocalizationMap_fraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/NonvanishingSections/LocalizationMap.lean, line 1092](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/NonvanishingSections/LocalizationMap.lean#L1092). The attribute's comment: “homogeneous fraction formula”.

> A homogeneous fraction `m/sⁿ` maps to the section `t` exactly when, on
> `X_s`, the restricted numerator is the tensor product of `t` with `sⁿ`.
> The local invertibility of `sⁿ` makes this condition a characterization.

```lean
public theorem sectionLocalizationMap_fraction (s : L.sections) (n : ℕ)
    (m : ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨(sectionSiteRing X),
      Presheaf.isSheaf_of_isSheaf_comp _ ((sectionSiteRing X)) (forget₂ CommRingCat RingCat)
      ((sectionSiteSheaf X))⟩).obj (F)).obj ((TensorPower.tensorPower (sectionSiteRing X)
      (sectionSiteSheaf X) L
        (n : ℤ))))).val.obj (op (⊤_ (Opens X.toRingedSpace.toPresheafedSpace))))
    (z : sectionAtNonvanishingOpen X L F s)
    (t : F.val.obj (op (nonvanishingOpen L s)))
    (hz : (z : LocalizedModule.Away
      (R := sectionRing (sectionSiteRing X) (sectionSiteSheaf X) L)
      (homogeneousSection X L s)
      (sectionModule (sectionSiteRing X) (sectionSiteSheaf X) L F)) =
        LocalizedModule.mk (S := Submonoid.powers (homogeneousSection X L s))
          (DirectSum.of _ (n : ℤ) m)
          ⟨(homogeneousSection X L s) ^ n, by exact ⟨n, rfl⟩⟩)
    (hdiv :
      ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨(sectionSiteRing X),
        Presheaf.isSheaf_of_isSheaf_comp _ ((sectionSiteRing X)) (forget₂ CommRingCat RingCat)
        ((sectionSiteSheaf X))⟩).obj (F)).obj ((TensorPower.tensorPower (sectionSiteRing X)
        (sectionSiteSheaf X) L
          (n : ℤ))))).val.map (terminal.from _).op m =
      tensorSectionAtOpen X L F
        (nonvanishingOpen L s) n t
        ((TensorPower.tensorPower (sectionSiteRing X) (sectionSiteSheaf X) L
          (n : ℤ)).val.map (terminal.from _).op (sectionPower X L s n))) :
    sectionLocalizationMap X L F s z = t
```

**`Stacks.SheafOfModules.sectionLocalizationMap_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/NonvanishingSections/LocalizationMap.lean, line 1131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/NonvanishingSections/LocalizationMap.lean#L1131). The attribute's comment: “localized-ring linearity”.

> The restriction-and-division map is linear over the induced map from the
> degree-zero homogeneous localization of the section ring to functions on `X_s`.

```lean
public theorem sectionLocalizationMap_smul (s : L.sections) :
    let U := nonvanishingOpen L s
    letI : Module
        ((TensorSheafification.structureSheaf (sectionSiteRing X)
          (sectionSiteSheaf X)).obj.obj (op U))
        (F.val.obj (op U)) := (F.val.obj (op U)).isModule
    ∃ φ : HomogeneousLocalization.Away
        (sectionRingGrading (sectionSiteRing X) (sectionSiteSheaf X) L)
        (homogeneousSection X L s) →+*
          (TensorSheafification.structureSheaf (sectionSiteRing X)
            (sectionSiteSheaf X)).obj.obj (op U),
      ∀ (a : HomogeneousLocalization.Away
          (sectionRingGrading (sectionSiteRing X) (sectionSiteSheaf X) L)
          (homogeneousSection X L s)) (z : sectionAtNonvanishingOpen X L F s),
        sectionLocalizationMap X L F s (a • z) =
          φ a • sectionLocalizationMap X L F s z
```

## Tag 01PW, a lemma

[Tag 01PW](https://stacks.math.columbia.edu/tag/01PW) in the Stacks Project.

**`Stacks.SheafOfModules.sectionLocalizationMap_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/GradedSectionInjective.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/GradedSectionInjective.lean#L442). The attribute's comment: “part (1)”. References: EGA I (9.3.1), “(i)”.

> **[Stacks, Tag 01PW] part (1).** Let `X` be a quasi-compact scheme, let `L` be an invertible
> `𝒪_X`-module, let `s` be a global section of `L` and let `ℱ` be a quasi-coherent `𝒪_X`-module.
> The comparison map of Tag 0B5L
> `(⨁_n Γ(X, ℱ ⊗ L^{⊗ n}))_{(s)} ⟶ Γ(X_s, ℱ|_{X_s})` is injective.

```lean
theorem sectionLocalizationMap_injective [CompactSpace X] [F.IsQuasicoherent] (s : L.sections) :
    Function.Injective (sectionLocalizationMap X L F s)
```

**`Stacks.SheafOfModules.sectionLocalizationMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/GradedSectionInjective.lean, line 1196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/GradedSectionInjective.lean#L1196). The attribute's comment: “part (2)”.

> **[Stacks, Tag 01PW] part (2).** Let `X` be a quasi-compact and quasi-separated scheme, let
> `L` be an invertible `𝒪_X`-module, let `s` be a global section of `L` and let `ℱ` be a
> quasi-coherent `𝒪_X`-module. The comparison map of Tag 0B5L
> `(⨁_n Γ(X, ℱ ⊗ L^{⊗ n}))_{(s)} ⟶ Γ(X_s, ℱ|_{X_s})` is bijective.
>
> Both chart-local steps of the source's proof are theorems here, so the statement asks only for
> the quasi-coherence of `ℱ` and the quasi-compactness and quasi-separatedness of `X`:
> `Stacks.SheafOfModules.hasTwistedChartExtension` is Tag 01P7 on an affine chart trivializing
> `L`, and `Stacks.SheafOfModules.hasTwistedCompactAnnihilation` is part (1) over a quasi-compact
> open.

```lean
theorem sectionLocalizationMap_bijective [CompactSpace X] [QuasiSeparatedSpace X]
    [F.IsQuasicoherent] (s : L.sections) :
    Function.Bijective (sectionLocalizationMap X L F s)
```

## Tag 0B5M, an equation

[Tag 0B5M](https://stacks.math.columbia.edu/tag/0B5M) in the Stacks Project.

**`Stacks.SheafOfModules.homAtNonvanishingOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/NonvanishingGradedHom.lean, line 842](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/NonvanishingGradedHom.lean#L842). The attribute's comment: “graded Hom localization”.

> The degree-zero localization of the actual graded Hom module.

```lean
public noncomputable def homAtNonvanishingOpen (s : L.sections)
```

**`Stacks.SheafOfModules.homLocalizationMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/NonvanishingGradedHom.lean, line 1178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/NonvanishingGradedHom.lean#L1178).

> Restrict a degree-zero localized graded morphism to the open where `s`
> trivializes `L`, dividing its degree-`n` numerator by `sⁿ`.

```lean
public noncomputable def homLocalizationMap (s : L.sections) :
    homAtNonvanishingOpen X L F G s →+
      (F.over (nonvanishingOpen L s) ⟶
        G.over (nonvanishingOpen L s))
```

**`Stacks.SheafOfModules.homLocalizationMap_fraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/NonvanishingGradedHom.lean, line 1221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/NonvanishingGradedHom.lean#L1221). The attribute's comment: “homogeneous fraction formula”.

> A homogeneous morphism `f : F ⟶ G ⊗ Lⁿ`, divided by `sⁿ`, restricts
> to the unique morphism on `X_s` whose tensor product with `sⁿ` is the
> restriction of `f`.

```lean
public theorem homLocalizationMap_fraction (s : L.sections) (n : ℕ)
    (f : F ⟶ (((Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨(sectionSiteRing X), Presheaf.isSheaf_of_isSheaf_comp _ ((sectionSiteRing X))
        (forget₂ CommRingCat RingCat) ((sectionSiteSheaf X))⟩).obj (G)).obj
        ((TensorPower.tensorPower (sectionSiteRing X)
        (sectionSiteSheaf X) L (n : ℤ)))))
    (t : (sheafHomSpace X.toRingedSpace F G).val.obj
        (op (nonvanishingOpen L s)))
    (hdiv :
      ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨(sectionSiteRing X),
          Presheaf.isSheaf_of_isSheaf_comp _ ((sectionSiteRing X)) (forget₂ CommRingCat RingCat)
          ((sectionSiteSheaf X))⟩).obj ((sheafHomSpace X.toRingedSpace F G))).obj
          ((TensorPower.tensorPower (sectionSiteRing X)
          (sectionSiteSheaf X) L (n : ℤ))))).val.map
            (terminal.from _).op
              (homToTwistedSection X L F G n f) =
      tensorSectionAtOpen X L
        (sheafHomSpace X.toRingedSpace F G)
        (nonvanishingOpen L s) n t
        ((TensorPower.tensorPower (sectionSiteRing X)
          (sectionSiteSheaf X) L (n : ℤ)).val.map
            (terminal.from _).op (sectionPower X L s n))) :
    homLocalizationMap X L F G s (homFractionClass X L F G s n f) = ⟨t⟩
```

## Tag 01XQ, a lemma

[Tag 01XQ](https://stacks.math.columbia.edu/tag/01XQ) in the Stacks Project.

**`Stacks.SheafOfModules.homLocalizationMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/GradedHomBijective.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/GradedHomBijective.lean#L108). The attribute's comment: “bijective”.

> **[Stacks, Tag 01XQ] part (2).** Let `X` be a quasi-compact and quasi-separated scheme, let
> `L` be an invertible `𝒪_X`-module, let `s` be a global section of `L`, let `ℱ` be an
> `𝒪_X`-module of finite presentation and let `𝒢` be a quasi-coherent `𝒪_X`-module. The comparison
> map of Tag 0B5M
> `(⨁_n Hom(ℱ, 𝒢 ⊗ L^{⊗ n}))_{(s)} ⟶ Hom_{𝒪_{X_s}}(ℱ|_{X_s}, 𝒢|_{X_s})` is bijective.
>
> The quasi-coherence of `ℱ` that the source assumes throughout the lemma is not carried
> separately: finite presentation implies it, and implies the finite type that part (1) of the tag
> asks for.

```lean
theorem homLocalizationMap_bijective [CompactSpace X] [QuasiSeparatedSpace X]
    [F.IsFinitePresentation] [G.IsQuasicoherent] (s : L.sections) :
    Function.Bijective (homLocalizationMap X L F G s)
```

**`Stacks.SheafOfModules.homLocalizationMap_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/GradedHomInjective.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/GradedHomInjective.lean#L243). The attribute's comment: “injective”.

> **[Stacks, Tag 01XQ] part (1).** Let `X` be a quasi-compact scheme, let `L` be an invertible
> `𝒪_X`-module, let `s` be a global section of `L` and let `ℱ`, `𝒢` be quasi-coherent
> `𝒪_X`-modules with `ℱ` of finite type. The comparison map of Tag 0B5M
> `(⨁_n Hom(ℱ, 𝒢 ⊗ L^{⊗ n}))_{(s)} ⟶ Hom_{𝒪_{X_s}}(ℱ|_{X_s}, 𝒢|_{X_s})` is injective.

```lean
theorem homLocalizationMap_injective (X : Scheme.{u}) [CompactSpace X]
    (L : SheafOfModules.{u} (structureSheafRing X.toRingedSpace))
    [IsInvertible X.toRingedSpace.presheaf
      (structureSheafRing X.toRingedSpace).property L]
    (F G : X.Modules) [F.IsQuasicoherent] [G.IsQuasicoherent] [F.IsFiniteType]
    (s : L.sections) :
    Function.Injective (homLocalizationMap X L F G s)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.18, Tag 0B5K](https://stacks.math.columbia.edu/tag/0B5K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
