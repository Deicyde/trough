---
declaration: section
origin: cited
lean: Stacks.ProjectiveCohomology.coe_sectionsTwistEquivAwayGrading_smul, AlgebraicGeometry.ProjectiveSpectrum.Proj.twistingSheaf, AlgebraicGeometry.ProjectiveSpectrum.Proj.twistSheafOfModules, Stacks.AlgebraicGeometry.ProjTwistAwayPiece.coe_sectionsTwistEquivGradedPiece_smul, twistMultiplicationMap, AlgebraicGeometry.ProjectiveSpectrum.Proj.twistSheafMultiplicationMap, AlgebraicGeometry.ProjectiveSpectrum.Proj.globalSectionsRingMap, Stacks.AlgebraicGeometry.ProjTwistSectionRing.globalSectionsRingMap
statement: formalized
proof: formalized
---

# 27.10 Invertible sheaves on Proj

Section 27.10 of the Stacks Project, [Tag 01MM](https://stacks.math.columbia.edu/tag/01MM). 14 tags here are carried by 25 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01MN, a definition

[Tag 01MN](https://stacks.math.columbia.edu/tag/01MN) in the Stacks Project.

**`Stacks.ProjectiveCohomology.coe_sectionsTwistEquivAwayGrading_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjStandardOpenScalars.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjStandardOpenScalars.lean#L134). The attribute's comment: “part (1), the scalar action in the standard-open description of the sections of a twist, written out on the underlying elements of the localization”.

> The identification of `Γ(D₊(f), 𝒪_P(m))` with the degree-`m` part of `A_f` is linear for
> the action of `Γ(P, D₊(f))` read through `AlgebraicGeometry.Proj.awayToSection`: a section
> scaled by the fraction `r` has for underlying element the product of `r.val` with the underlying
> element of the section.

```lean
theorem coe_sectionsTwistEquivAwayGrading_smul (hf : f ∈ 𝒜 k) (hk : 0 < k) (m : ℤ)
    (r : HomogeneousLocalization.Away 𝒜 f)
    (s : (twistingSheaf 𝒜 m).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    ((sectionsTwistEquivAwayGrading 𝒜 hf hk m
        ((ProjectiveSpectrum.Proj.awayToSection 𝒜 f).hom r • s) :
      LocalizedModule.Away f A)) =
      HomogeneousLocalization.val r •
        ((sectionsTwistEquivAwayGrading 𝒜 hf hk m s : LocalizedModule.Away f A))
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.twistingSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjTwist.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjTwist.lean#L168). The attribute's comment: “part (1), twist of the structure sheaf”.

> The `n`-th twist of the structure sheaf on `Proj(S)`.

```lean
public noncomputable abbrev twistingSheaf
    (𝒜 : ℕ → σ) [GradedRing 𝒜] (n : ℤ) :
    SheafOfModules.{u}
      ((sheafCompose (Opens.grothendieckTopology (ProjectiveSpectrum.top 𝒜))
        (forget₂ CommRingCat.{u} RingCat.{u})).obj
        (ProjectiveSpectrum.Proj.structureSheaf 𝒜))
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.twistSheafOfModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjTwist.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjTwist.lean#L178). The attribute's comment: “part (2), twist of a module sheaf”.

> Tensoring an `𝒪_Proj(S)`-module with the `n`-th twisting sheaf.

```lean
public noncomputable def twistSheafOfModules
    (𝒜 : ℕ → σ) [GradedRing 𝒜]
    (F : SheafOfModules.{u}
      ((sheafCompose (Opens.grothendieckTopology (ProjectiveSpectrum.top 𝒜))
        (forget₂ CommRingCat.{u} RingCat.{u})).obj
        (ProjectiveSpectrum.Proj.structureSheaf 𝒜))) (n : ℤ) :
    SheafOfModules.{u}
      ((sheafCompose (Opens.grothendieckTopology (ProjectiveSpectrum.top 𝒜))
        (forget₂ CommRingCat.{u} RingCat.{u})).obj
        (ProjectiveSpectrum.Proj.structureSheaf 𝒜))
```

**`Stacks.AlgebraicGeometry.ProjTwistAwayPiece.coe_sectionsTwistEquivGradedPiece_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistAwayPieceScalars.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistAwayPieceScalars.lean#L58). The attribute's comment: “part (1), the scalar action in the description of the sections of a twist over a standard open as a homogeneous piece of the graded localization, written out on the underlying elements of the localization”.

> The identification `Γ(D₊(f), 𝒪_X(n)) ≅ (A_f)_n` is semilinear for the action of
> `Γ(D₊(f), 𝒪_X)` read through `AlgebraicGeometry.ProjectiveSpectrum.Proj.awayToSection`: a section
> scaled by the fraction `r` has for underlying element the product of `r.val` with the underlying
> element of the section.

```lean
theorem coe_sectionsTwistEquivGradedPiece_smul (hf : f ∈ 𝒜 k) (hk : 0 < k) (n : ℤ)
    (r : HomogeneousLocalization.Away 𝒜 f)
    (s : (twistingSheaf 𝒜 n).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    ((sectionsTwistEquivGradedPiece 𝒜 hf hk n
        ((ProjectiveSpectrum.Proj.awayToSection 𝒜 f).hom r • s) :
      LocalizedModule.Away f A)) =
      HomogeneousLocalization.val r •
        ((sectionsTwistEquivGradedPiece 𝒜 hf hk n s : LocalizedModule.Away f A))
```

## Tag 01MO, an equation

[Tag 01MO](https://stacks.math.columbia.edu/tag/01MO) in the Stacks Project.

Declarations registered for the tag:

- [`twistMultiplicationMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=twistMultiplicationMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProjInvertibleLocus/Basic.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjInvertibleLocus/Basic.lean#L160) (StacksFrontier).

## Tag 03GJ, an equation

[Tag 03GJ](https://stacks.math.columbia.edu/tag/03GJ) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.twistSheafMultiplicationMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistModuleMultiplication.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistModuleMultiplication.lean#L51).

> **The canonical multiplication map `𝒪_X(n) ⊗ ℱ(m) ⟶ ℱ(n + m)`** on `X = Proj S`, for a
> sheaf of `𝒪_X`-modules `ℱ`: reassociate, braid `𝒪(n)` past `ℱ`, reassociate again, and
> multiply the two twists of the structure sheaf together.

```lean
public noncomputable def twistSheafMultiplicationMap
    (F : SheafOfModules.{u}
      ((sheafCompose (Opens.grothendieckTopology (ProjectiveSpectrum.top 𝒮))
        (forget₂ CommRingCat.{u} RingCat.{u})).obj
        (ProjectiveSpectrum.Proj.structureSheaf 𝒮))) (n m : ℤ) :
    (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
        (ProjectiveSpectrum.Proj.structureSheaf 𝒮)).obj ((twistingSheaf 𝒮 n))).obj
        ((twistSheafOfModules 𝒮 F m))) ⟶
      twistSheafOfModules 𝒮 F (n + m)
```

## Tag 01MP, an equation

[Tag 01MP](https://stacks.math.columbia.edu/tag/01MP) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.globalSectionsRingMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistSectionRing.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistSectionRing.lean#L379).

> **The canonical homomorphism of graded rings `S → ⨁_{n ≥ 0} Γ(Proj 𝒮, 𝒪(n))`.** Its
> multiplication on sections is the pointwise product of local fractions, and in each degree it is
> the canonical map from the homogeneous elements; those two formulas determine it.

```lean
public noncomputable def globalSectionsRingMap : GlobalSectionsRingMap 𝒮
```

**`Stacks.AlgebraicGeometry.ProjTwistSectionRing.globalSectionsRingMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistSectionRing/Statement.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistSectionRing/Statement.lean#L210).

> The canonical graded ring map
> `S → ⨁ n ≥ 0, Γ(Proj(S), 𝒪(n))`.

```lean
public def globalSectionsRingMap : GlobalSectionsRingMap 𝒮
```

## Tag 03GK, an equation

[Tag 03GK](https://stacks.math.columbia.edu/tag/03GK) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.globalSectionsPairing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistSectionModule.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistSectionModule.lean#L278).

> **The pairing `(⨁_{n ≥ 0} Γ(X, 𝒪_X(n))) × (⨁_{m ∈ ℤ} Γ(X, ℱ(m))) ⟶ ⨁_{m ∈ ℤ} Γ(X, ℱ(m))`**
> on `X = Proj 𝒮`: the biadditive extension of the canonical multiplication of a global section of
> `𝒪_X(n)` with a global section of `ℱ(m)`.

```lean
public noncomputable def globalSectionsPairing :
    (⨁ n : ℕ, twistGlobalSections 𝒮 n) →+
      (twistedGlobalSections 𝒮 F →+ twistedGlobalSections 𝒮 F)
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.globalSectionsPairing_of_of`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistSectionModule.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistSectionModule.lean#L286).

> The pairing of a global section of `𝒪(n)` with a global section of `ℱ(m)` is their canonical
> product, a global section of `ℱ(n + m)`.

```lean
public theorem globalSectionsPairing_of_of (n : ℕ) (m : ℤ) (s : twistGlobalSections 𝒮 n)
    (t : (twistSheafOfModules 𝒮 F m).val.obj (op ⊤)) :
    globalSectionsPairing 𝒮 F (DirectSum.of _ n s) (DirectSum.of _ m t) =
      DirectSum.of _ ((n : ℤ) + m) (multiplyHomogeneousSections 𝒮 F n m s t)
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.twistedGlobalSectionsModule`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistSectionModule.lean, line 903](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistSectionModule.lean#L903). The attribute's comment: “the module structure on the twisted global sections”.

> **The module `⨁_{m ∈ ℤ} Γ(X, ℱ(m))` over the graded ring `⨁_{n ≥ 0} Γ(X, 𝒪_X(n))`** on
> `X = Proj 𝒮`, for the pairing that multiplies a global section of `𝒪_X(n)` with a global
> section of `ℱ(m)` through the canonical morphism `𝒪_X(n) ⊗ ℱ(m) ⟶ ℱ(n + m)`.

```lean
public noncomputable instance twistedGlobalSectionsModule :
    Module (⨁ n : ℕ, twistGlobalSections 𝒮 n) (twistedGlobalSections 𝒮 F)
```

## Tag 01MQ, an equation

[Tag 01MQ](https://stacks.math.columbia.edu/tag/01MQ) in the Stacks Project.

Declarations registered for the tag:

- [`moduleTwistMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=moduleTwistMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProjShifted/Basic.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjShifted/Basic.lean#L202) (StacksFrontier).

## Tag 01MR, an equation

[Tag 01MR](https://stacks.math.columbia.edu/tag/01MR) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjShiftedSections.globalSectionsModuleMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjShiftedSectionModule.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjShiftedSectionModule.lean#L473).

> **The canonical map of graded `S`-modules `M → ⨁_{n ∈ ℤ} Γ(Proj 𝒮, M(n)~)`.** In degree `n`
> it is the canonical map from the homogeneous elements of degree `n`, and a homogeneous scalar
> acts pointwise on local fractions; those two formulas determine the whole datum.

```lean
public noncomputable def globalSectionsModuleMap : GlobalSectionsModuleMap 𝒮 𝒨
```

## Tag 01MS, a lemma

[Tag 01MS](https://stacks.math.columbia.edu/tag/01MS) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ModuleTwistIso.twistsOnBasicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ModuleTwistIso/StandardOpen.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ModuleTwistIso/StandardOpen.lean#L66). The attribute's comment: “the lemma's five assertions in one statement”.

> Let `f ∈ S` be homogeneous of degree `d`. Restricted to the standard open `D₊(f)`, the twisting
> sheaf `𝒪_X(nd)` is invertible and in fact trivial for every integer `n`, and the three families of
> canonical maps built from it are isomorphisms: `𝒪_X(nd) ⊗ 𝒪_X(m) ⟶ 𝒪_X(nd+m)`,
> `𝒪_X(nd) ⊗ ℱ(m) ⟶ ℱ(nd+m)` for every sheaf of `𝒪_X`-modules `ℱ`, and `M̃ ⊗ 𝒪_X(nd) ⟶ M(nd)~` for
> every graded `S`-module `M`. The second index is arbitrary throughout, and `d` is not assumed
> positive.

```lean
theorem twistsOnBasicOpen {f : S} {d : ℕ} (hf : f ∈ 𝒮 d) :
    (∀ n : ℤ, _root_.AlgebraicGeometry.SheafOfModules.IsInvertible
        ((Over.forget (ProjectiveSpectrum.basicOpen 𝒮 f)).op ⋙
          (ProjectiveSpectrum.Proj.structureSheaf 𝒮).obj)
        ((projRingSheaf 𝒮).over (ProjectiveSpectrum.basicOpen 𝒮 f)).property
        ((twistingSheaf 𝒮 (n * d)).over (ProjectiveSpectrum.basicOpen 𝒮 f))) ∧
      (∀ n : ℤ, _root_.AlgebraicGeometry.SheafOfModules.IsTrivial
        ((Over.forget (ProjectiveSpectrum.basicOpen 𝒮 f)).op ⋙
          (ProjectiveSpectrum.Proj.structureSheaf 𝒮).obj)
        ((projRingSheaf 𝒮).over (ProjectiveSpectrum.basicOpen 𝒮 f)).property
        ((twistingSheaf 𝒮 (n * d)).over (ProjectiveSpectrum.basicOpen 𝒮 f))) ∧
      (∀ n m : ℤ, IsIso
        ((Scheme.Modules.restrictFunctor (AlgebraicGeometry.Proj.basicOpen 𝒮 f).ι).map
          (twistMultiplicationMap 𝒮 ((d : ℤ) * n) m))) ∧
      (∀ (F : SheafOfModules.{u}
          ((sheafCompose (Opens.grothendieckTopology (ProjectiveSpectrum.top 𝒮))
            (forget₂ CommRingCat.{u} RingCat.{u})).obj
            (ProjectiveSpectrum.Proj.structureSheaf 𝒮))) (n m : ℤ), IsIso
        ((Scheme.Modules.restrictFunctor (AlgebraicGeometry.Proj.basicOpen 𝒮 f).ι).map
          (twistSheafMultiplicationMap 𝒮 F ((d : ℤ) * n) m))) ∧
      (∀ (M : Type u) [AddCommGroup M] [Module S M] (τ : Type t) [SetLike τ M]
          [AddSubgroupClass τ M] (𝒨 : ℤ → τ) [DirectSum.Decomposition 𝒨]
          [SetLike.GradedSMul 𝒮 𝒨] (n : ℤ), IsIso
        ((Scheme.Modules.restrictFunctor (AlgebraicGeometry.Proj.basicOpen 𝒮 f).ι).map
          (moduleTwistMap 𝒮 𝒨 ((d : ℤ) * n))))
```

## Tag 01MT, a lemma

[Tag 01MT](https://stacks.math.columbia.edu/tag/01MT) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjTwistDegreeOneCover.isInvertible_twistingSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistDegreeOneCover/Basic.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistDegreeOneCover/Basic.lean#L141). The attribute's comment: “the sheaves 𝒪\_X(n) are invertible”. References: EGA II (3.2.5), “Second assertion”.

> **Stacks 01MT: the sheaves `𝒪_X(n)` are invertible.**
>
> The trivializing sections are the ratios `(f/1)^n` on the standard opens `D₊(f)` with
> `f ∈ S₁`, assembled by
> `Stacks.AlgebraicGeometry.ProjInvertibleLocus.isInvertible_twistingSheaf_of_ratioLocus_eq_top`
> at `d = 1`.

```lean
public theorem isInvertible_twistingSheaf (hcover : DegreeOneCover 𝒮) (n : ℤ) :
    _root_.AlgebraicGeometry.SheafOfModules.IsInvertible (AlgebraicGeometry.Proj 𝒮).presheaf
      (AlgebraicGeometry.Proj 𝒮).ringCatSheaf.2 (twistingSheaf 𝒮 n)
```

**`Stacks.AlgebraicGeometry.ProjTwistDegreeOneCover.isIso_twistMultiplicationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistDegreeOneCover/Basic.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistDegreeOneCover/Basic.lean#L157). The attribute's comment: “equation 01MO is an isomorphism”.

> **Stacks 01MT: Equation 01MO `𝒪_X(n) ⊗ 𝒪_X(m) ⟶ 𝒪_X(n + m)` is an isomorphism**, for all
> integers `n` and `m`.
>
> This is
> `Stacks.AlgebraicGeometry.TwistTensor.isIso_twistMultiplicationMap_of_ratioLocus_eq_top` at
> `k = 1`; the only work is the substitution of `1 * n` for `n`, which has to be done after
> `revert` because the index occurs in the type of the morphism.

```lean
public theorem isIso_twistMultiplicationMap (hcover : DegreeOneCover 𝒮) (n m : ℤ) :
    IsIso (twistMultiplicationMap 𝒮 n m)
```

**`Stacks.AlgebraicGeometry.ProjTwistDegreeOneCover.isIso_twistSheafMultiplicationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistDegreeOneCover/Basic.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistDegreeOneCover/Basic.lean#L187). The attribute's comment: “equation 03GJ is an isomorphism”.

> **Stacks 01MT: Equation 03GJ `𝒪_X(n) ⊗ ℱ(m) ⟶ ℱ(n + m)` is an isomorphism**, for every
> sheaf of `𝒪_X`-modules `ℱ` and all integers `n` and `m`.
>
> The source deduces this clause from the Equation 01MO clause, and so does the proof: by
> construction
> `AlgebraicGeometry.ProjectiveSpectrum.Proj.twistSheafMultiplicationMap` is the composite of
> the inverse associator, the braiding on `𝒪(n) ⊗ ℱ` tensored with `𝒪(m)`, the associator, and
> `𝟙 ℱ ⊗ (Equation 01MO)`.  The first three factors are isomorphisms unconditionally, and the
> fourth is one because the native tensor bifunctor maps the product of two isomorphisms to an
> isomorphism.

```lean
public theorem isIso_twistSheafMultiplicationMap (hcover : DegreeOneCover 𝒮)
    (F : SheafOfModules.{u}
      ((sheafCompose (Opens.grothendieckTopology (ProjectiveSpectrum.top 𝒮))
        (forget₂ CommRingCat.{u} RingCat.{u})).obj
        (ProjectiveSpectrum.Proj.structureSheaf 𝒮))) (n m : ℤ) :
    IsIso (twistSheafMultiplicationMap 𝒮 F n m)
```

**`Stacks.AlgebraicGeometry.ProjTwistDegreeOneCover.nonempty_tensorPowModule_iso_twistingSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistDegreeOneCover/Basic.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistDegreeOneCover/Basic.lean#L258). The attribute's comment: “the induced identification 𝒪\_X(1)^\{⊗ n} ≅ 𝒪\_X(n)”. References: EGA II (2.5.14), “(2.5.14.2)”.

> **Stacks 01MT: the induced identification `𝒪_X(1)^{⊗ n} ≅ 𝒪_X(n)`**, for every integer `n`,
> at the canonical integral tensor power `Stacks.Ample.tensorPowModule` of Tag 01CU.
>
> Both families are carried one degree by the autoequivalence `twistRight` — the tensor powers by
> the addition law of Tag 01CU, the twists by Equation 01MO at `(n, 1)` — and they agree in degree
> one, so `Stacks.AlgebraicGeometry.ProjTwistPowers.nonempty_iso_of_shift` identifies them in
> every degree, negative ones included, with no separate argument.
>
> The library already had this under the stronger hypothesis
> `Algebra.adjoin (𝒮 0) (𝒮 1) = ⊤`, as
> `Stacks.AlgebraicGeometry.ProjTwistPowers.nonempty_tensorPowModule_iso_twistingSheaf`; this is
> the same statement at the source's own printed hypothesis.

```lean
public theorem nonempty_tensorPowModule_iso_twistingSheaf (hcover : DegreeOneCover 𝒮) (n : ℤ) :
    letI := isInvertibleModule_twistingSheaf 𝒮 hcover 1
    Nonempty (Stacks.Ample.tensorPowModule (AlgebraicGeometry.Proj 𝒮) (twistingSheaf 𝒮 1) n ≅
      twistingSheaf 𝒮 n)
```

**`Stacks.AlgebraicGeometry.ProjTwistDegreeOneCover.isIso_moduleTwistMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistDegreeOneCover/Basic.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistDegreeOneCover/Basic.lean#L314). The attribute's comment: “equation 01MQ is an isomorphism”. References: EGA II (2.5.15); EGA II (3.2.8).

> **Stacks 01MT: Equation 01MQ `M̃ ⊗ 𝒪_X(n) ⟶ M(n)̃` is an isomorphism**, for every graded
> `S`-module `M` and every integer `n`.
>
> `isIso_moduleTwistMap_of_ratioLocus_eq_top` at `d = 1`.

```lean
public theorem isIso_moduleTwistMap (hcover : DegreeOneCover 𝒮) (n : ℤ) :
    IsIso (ProjShifted.moduleTwistMap 𝒮 𝒨 n)
```

**`Stacks.AlgebraicGeometry.ProjTwistDegreeOneCover.moduleTwistIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistDegreeOneCover/Basic.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistDegreeOneCover/Basic.lean#L324). The attribute's comment: “the induced isomorphism M̃ ⊗ 𝒪\_X(n) ≅ M(n)~”.

> **Stacks 01MT: the induced isomorphism `M̃ ⊗_{𝒪_X} 𝒪_X(n) = M̃(n) ≅ M(n)̃`.**

```lean
public def moduleTwistIso (hcover : DegreeOneCover 𝒮) (n : ℤ) :
    (((Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨(((AlgebraicGeometry.Proj 𝒮).toRingedSpace)).presheaf,
          (((AlgebraicGeometry.Proj 𝒮).toRingedSpace)).IsSheaf⟩).obj
        ((associatedModuleSheaf 𝒮 𝒨))).obj ((twistingSheaf 𝒮 n))) ≅
      associatedModuleSheaf 𝒮 (shiftedGrading 𝒨 n)
```

## Tag 0AG3, an equation

[Tag 0AG3](https://stacks.math.columbia.edu/tag/0AG3) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjTwistDegreeOneCover.degreeNToTwistedGlobalSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistDegreeOneCover/GlobalSections.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistDegreeOneCover/GlobalSections.lean#L87).

> **Equation 0AG3: the canonical map `M_n ⟶ Γ(X, M̃(n))`.** A homogeneous element of degree
> `n` gives a global section of `M(n)~`, which the isomorphism `M(n)~ ≅ M̃(n)` of Tag 01MT turns
> into a global section of the twist `M̃(n)`.

```lean
public def degreeNToTwistedGlobalSections (hcover : DegreeOneCover 𝒮) (n : ℤ) :
    𝒨 n →+ twistedModuleGlobalSections 𝒮 𝒨 n
```

## Tag 01MU, a lemma

[Tag 01MU](https://stacks.math.columbia.edu/tag/01MU) in the Stacks Project.

**`Stacks.AlgebraicGeometry.GoodOpenClose.isGoodOpen_iff_le_whereInvertible_of_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GoodOpenClose/Basic.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GoodOpenClose/Basic.lean#L156). The attribute's comment: “maximality and goodness of the invertible locus”.

> For `0 < d`, an open is good exactly when it lies in the largest good open
> `whereInvertible 𝒮 d`.

```lean
theorem isGoodOpen_iff_le_whereInvertible_of_pos (d : ℕ) (_hd : 0 < d)
    (U : (AlgebraicGeometry.Proj 𝒮).Opens) :
    IsGoodOpen 𝒮 d U ↔ U ≤ whereInvertible 𝒮 d
```

**`Stacks.AlgebraicGeometry.GoodOpenClose.whereInvertible_eq_iSup_basicOpen_mul_of_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GoodOpenClose/Basic.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GoodOpenClose/Basic.lean#L186). The attribute's comment: “equality of the two open subsets”.

> For `0 < d`, the largest good open `whereInvertible 𝒮 d` is the union of the standard opens
> `D₊(fg)` with `deg f = deg g + d`.

```lean
theorem whereInvertible_eq_iSup_basicOpen_mul_of_pos (d : ℕ) (_hd : 0 < d) :
    whereInvertible 𝒮 d =
      ⨆ (e : ℕ) (f : 𝒮 (e + d)) (g : 𝒮 e),
        AlgebraicGeometry.Proj.basicOpen 𝒮 ((f : S) * (g : S))
```

**`Stacks.AlgebraicGeometry.ModuleTwistIso.moduleTwistMap_isIso_on_whereInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ModuleTwistIso/Basic.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ModuleTwistIso/Basic.lean#L391). The attribute's comment: “comparison for associated modules”.

> On the largest open on which the `d`-divisible twists are invertible and their multiplication
> maps are isomorphisms, the canonical comparison from the tensor product of an associated sheaf
> with such a twist to the associated sheaf of the shifted module is an isomorphism, for every
> graded module and every integral multiple of `d`. The hypothesis `0 < d` is not used.

```lean
theorem moduleTwistMap_isIso_on_whereInvertible (d : ℕ) (_hd : 0 < d) (n : ℤ) :
    IsIso ((Scheme.Modules.restrictFunctor (whereInvertible 𝒮 d).ι).map
      (moduleTwistMap 𝒮 𝒨 ((d : ℤ) * n)))
```

## Tag 01MV, a lemma

[Tag 01MV](https://stacks.math.columbia.edu/tag/01MV) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjInvertibleLocus.nonvanishingLocus_degreeSection_inter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjInvertibleLocus/NonvanishingLocus.lean, line 534](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjInvertibleLocus/NonvanishingLocus.lean#L534).

> **Stacks Tag 01MV.** Let `S` be a graded ring, `X = Proj(S)`, `d ≥ 1`, `n ≥ 1` and
> `f ∈ S_{nd}`. Let `s` be the global section of `𝒪(nd)` attached to `f`. Then, on the open `W_d`
> where the `d`-divisible twists are invertible, the nonvanishing locus of `s` is the standard
> open `D₊(f)`:
>
> `X_s ∩ W_d = D₊(f) ∩ W_d`.
>
> This is stated on `Proj(S)` rather than on the open subscheme `W_d`, which is strictly stronger
> than the form of the source: the statement there is the image of this one under
> `Stacks.SheafOfModules.preimage_nonvanishingLocus`. No positivity of `d` or `n` is needed.

```lean
theorem nonvanishingLocus_degreeSection_inter (d n : ℕ) (f : 𝒮 (n * d)) :
    Stacks.SheafOfModules.nonvanishingLocus
          (X := (AlgebraicGeometry.Proj 𝒮).toRingedSpace)
          (twistingSheaf 𝒮 ((n * d : ℕ) : ℤ))
          (sectionsOfTop _ (degreeSection 𝒮 (n * d) f)) ∩
        (whereInvertible 𝒮 d : Set ↥(AlgebraicGeometry.Proj 𝒮)) =
      (AlgebraicGeometry.Proj.basicOpen 𝒮 (f : S) : Set ↥(AlgebraicGeometry.Proj 𝒮)) ∩
        (whereInvertible 𝒮 d : Set ↥(AlgebraicGeometry.Proj 𝒮))
```

## Tag 01MW, a lemma

[Tag 01MW](https://stacks.math.columbia.edu/tag/01MW) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CommonDegreeTwist.exists_degree_forall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CommonDegreeTwist/AffineSectionBasis.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/CommonDegreeTwist/AffineSectionBasis.lean#L285). The attribute's comment: “degree\_exists”.

> **Stacks Tag 01MW.** Let `S` be a graded ring, `X = Proj(S)` and `Y ⊆ X` a quasi-compact
> open subscheme; write `𝒪_Y(n)` for the restriction of `𝒪_X(n)` to `Y`. Then there is an integer
> `d ≥ 1` such that
>
> 1. `Y` is contained in the open `W_d` of Tag 01MU;
> 2. `𝒪_Y(dn)` is invertible for every `n : ℤ`;
> 3. every multiplication map `𝒪_Y(nd) ⊗_{𝒪_Y} 𝒪_Y(m) ⟶ 𝒪_Y(nd + m)` of Equation 01MO is an
>    isomorphism;
> 4. every comparison map `M̃|_Y ⊗_{𝒪_Y} 𝒪_Y(nd) ⟶ M(nd)~|_Y` of Equation 01MQ is an
>    isomorphism, for every graded `S`-module `M`;
> 5. for `f ∈ S_{nd}` with image `s ∈ Γ(Y, 𝒪_Y(nd))` the nonvanishing locus `Y_s` is
>    `D₊(f) ∩ Y`;
> 6. the opens `Y_s`, for `s ∈ Γ(Y, 𝒪_Y(nd))` with `n ≥ 1`, form a basis for the topology of `Y`;
> 7. so do those among them which are affine.
>
> The degree is the common degree of a finite standard-open cover of `Y`, which quasi-compactness
> produces: `AlgebraicGeometry.Proj.commonDegreeCover`. Each clause is then the corresponding
> result about such a cover, so all seven hold for that one degree.

```lean
theorem exists_degree_forall (Y : (AlgebraicGeometry.Proj 𝒮).Opens)
    (hY : IsCompact (Y : Set (AlgebraicGeometry.Proj 𝒮))) :
    ∃ d : ℕ, 1 ≤ d ∧
      Y ≤ whereInvertible 𝒮 d ∧
      (∀ n : ℤ, SheafOfModules.IsInvertible Y.toScheme.presheaf Y.toScheme.ringCatSheaf.2
        ((Scheme.Modules.pullback Y.ι).obj (twistingSheaf 𝒮 ((d : ℤ) * n)))) ∧
      (∀ n m : ℤ, IsIso ((Scheme.Modules.restrictFunctor Y.ι).map
        (twistMultiplicationMap 𝒮 ((d : ℤ) * n) m))) ∧
      (∀ (M : Type u) [AddCommGroup M] [Module S M] (τ : Type t) [SetLike τ M]
        [AddSubgroupClass τ M] (𝒨 : ℤ → τ) [DirectSum.Decomposition 𝒨]
        [SetLike.GradedSMul 𝒮 𝒨] (n : ℤ),
          IsIso ((Scheme.Modules.restrictFunctor Y.ι).map
            (Stacks.AlgebraicGeometry.ProjShifted.moduleTwistMap 𝒮 𝒨 ((d : ℤ) * n)))) ∧
      (∀ (n : ℕ) (f : 𝒮 (n * d)),
        Stacks.Ample.nonvanishingLocus (restrictedTwist 𝒮 Y ((n * d : ℕ) : ℤ))
            (restrictedDegreeSection 𝒮 Y (n * d) f) =
          ((Y.ι ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen 𝒮 (f : S) : Y.toScheme.Opens) :
            Set Y.toScheme)) ∧
      Opens.IsBasis {V : Y.toScheme.Opens | ∃ n : ℕ, 1 ≤ n ∧
        ∃ s : Γ(restrictedTwist 𝒮 Y ((n * d : ℕ) : ℤ), ⊤),
          (V : Set Y.toScheme) =
            Stacks.Ample.nonvanishingLocus (restrictedTwist 𝒮 Y ((n * d : ℕ) : ℤ)) s} ∧
      Opens.IsBasis {V : Y.toScheme.Opens | ∃ n : ℕ, 1 ≤ n ∧
        ∃ s : Γ(restrictedTwist 𝒮 Y ((n * d : ℕ) : ℤ), ⊤),
          IsAffineOpen V ∧ (V : Set Y.toScheme) =
            Stacks.Ample.nonvanishingLocus (restrictedTwist 𝒮 Y ((n * d : ℕ) : ℤ)) s}
```

## Tag 0B5I, a lemma

[Tag 0B5I](https://stacks.math.columbia.edu/tag/0B5I) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjTwistIntegerComparisonStatement.comparison_existsUnique_functorial_degreeZeroId`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorSectionNonvanishing/ProjTwistIntegerComparisonStatement.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/TensorSectionNonvanishing/ProjTwistIntegerComparisonStatement.lean#L82). The attribute's comment: “the tag's three assertions in one statement, for the canonical graded-module structure on `M = ⨁_{n ∈ ℤ} Γ(X, ℱ(n))`: the comparison morphism `M̃ ⟶ ℱ` exists and is the unique morphism restricting on each positive-degree standard open to `m / f ^ k ↦ m|_{D₊(f)} ⊗ f ^ (-k)`, it commutes with every morphism of sheaves of modules out of `ℱ`, and it returns each global section of `ℱ` to itself through the identification `ℱ(0) ≅ ℱ`”. References: EGA II (2.6.4), “more general”.

> Let `S` be a graded ring, `X = Proj S`, let `ℱ` be a sheaf of `𝒪_X`-modules and let
> `M = ⨁_{n ∈ ℤ} Γ(X, ℱ(n))` be the graded `S`-module of twisted global sections, taken with its
> canonical graded-module structure
> `Stacks.AlgebraicGeometry.ProjTwistedSections.twistedGlobalSectionsModule`. Then there is a
> canonical `𝒪_X`-module map `M̃ ⟶ ℱ`, functorial in `ℱ`, whose induced map `M₀ → Γ(X, ℱ)` is the
> identity.
>
> The three conjuncts are, in order:
>
> 1. **Existence and canonicity.** There is exactly one morphism `M̃ ⟶ ℱ` whose restriction to the
>   standard open `D₊(f)` of each positive-degree homogeneous element is the chart comparison
>   `m / f ^ k ↦ m|_{D₊(f)} ⊗ f ^ (-k)`. The morphism it names is
>   `Stacks.AlgebraicGeometry.ProjTwistIntegerComparison.integerComparison`.
> 2. **Functoriality in `ℱ`.** For every sheaf `𝒢` and every morphism `ψ : ℱ ⟶ 𝒢`, the comparison
>   morphisms of `ℱ` and of `𝒢` form a commuting square with `ψ` and with the morphism of
>   associated sheaves that `ψ` induces on the graded modules of twisted global sections.
> 3. **The degree-zero map is the identity.** A global section `t` of `ℱ` is a degree-zero element
>   of `M` through the identification `ℱ(0) ≅ ℱ` of
>   `Stacks.AlgebraicGeometry.ProjTwistDegreeZeroNormalization.twistZeroCancelIso`; the global
>   section of `M̃` attached to it is sent by the comparison morphism back to `t`.

```lean
theorem comparison_existsUnique_functorial_degreeZeroId
    (F : SheafOfModules.{u} (projRingSheaf 𝒮)) :
    (∃! φ : twistedGlobalSectionsAssociatedSheaf 𝒮 F (twistedGlobalSectionsModule 𝒮 F) ⟶ F,
        ∀ p : PositiveElem 𝒮,
          φ.val.app (op (positiveBasicOpen 𝒮 p)) =
            localComparison 𝒮 F (twistedGlobalSectionsModule 𝒮 F) p) ∧
      (∀ (G : SheafOfModules.{u} (projRingSheaf 𝒮)) (ψ : F ⟶ G),
          twistedGlobalSectionsAssociatedSheafMap 𝒮 (twistedGlobalSectionsModule 𝒮 F)
                (twistedGlobalSectionsModule 𝒮 G) ψ ≫
              integerComparison 𝒮 G (twistedGlobalSectionsModule 𝒮 G) =
            integerComparison 𝒮 F (twistedGlobalSectionsModule 𝒮 F) ≫ ψ) ∧
      (letI := (twistedGlobalSectionsModule 𝒮 F).moduleInst
       letI := (twistedGlobalSectionsModule 𝒮 F).gradedSMul
       ∀ t : F.val.obj (op (⊤ : Opens (ProjectiveSpectrum.top 𝒮))),
        (integerComparison 𝒮 F (twistedGlobalSectionsModule 𝒮 F)).val.app
            (op (⊤ : Opens (ProjectiveSpectrum.top 𝒮)))
            (degreeZeroToGlobalSections 𝒮 (twistedGlobalSectionsGrading 𝒮 F)
              ⟨DirectSum.of (fun k : ℤ => twistedSectionsComponent 𝒮 F k) 0
                  ((twistZeroCancelIso 𝒮 F (rfl : (0 : ℤ) = 0)).inv.val.app
                    (op (⊤ : Opens (ProjectiveSpectrum.top 𝒮))) t),
                (DirectSum.mem_rangeGrading ℤ (fun k : ℤ => twistedSectionsComponent 𝒮 F k) 0
                  _).mpr ⟨_, rfl⟩⟩) = t)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.10, Tag 01MM](https://stacks.math.columbia.edu/tag/01MM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
