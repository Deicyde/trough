---
declaration: section
origin: cited
lean: Stacks.Cohomology.Cech.isZero_cechCohomology_of_isStandardOpenCover, Stacks.Cohomology.Cech.isZero_hgroup_of_isAffineOpen, Stacks.Duality.Coherator.affineAmplitudeIn_zero_zero_single, Stacks.Cohomology.Affine.isZero_rightDerived_pushforward_of_isAffineHom, Stacks.AffineHigherDirectImage.isZero_rightDerivedPlus_pushforward, Stacks.Cohomology.AffineComparison.cohomologyIsoPushforward, Stacks.AffineCohomologyPushforward.cohomologyPushforwardIso, Stacks.AffineCohomologyResolution.cohomologyPushforwardIso
statement: formalized
proof: formalized
---

# 30.2 Čech cohomology of quasi-coherent sheaves

Section 30.2 of the Stacks Project, [Tag 01X8](https://stacks.math.columbia.edu/tag/01X8). 6 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01X9, a lemma

[Tag 01X9](https://stacks.math.columbia.edu/tag/01X9) in the Stacks Project.

**`Stacks.Cohomology.Cech.isZero_cechCohomology_of_isStandardOpenCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Cech/StandardCoverVanishing.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Cech/StandardCoverVanishing.lean#L424).

> **Positive-degree Čech cohomology of a quasi-coherent module vanishes on a finite standard
> open cover of an affine open.** Here `F` is a quasi-coherent module on the ambient scheme `X`,
> the affine open `U` is covered by the ambient basic opens `X.basicOpen (g i)` attached to a
> finite family `g` of sections over `U` whose basic opens cover `Spec Γ(X, U)`, and Čech
> cohomology is the homology of Mathlib's `cechComplexFunctor` applied to the underlying abelian
> sheaf of `F`.

```lean
theorem isZero_cechCohomology_of_isStandardOpenCover
    (X : Scheme.{u}) (F : X.Modules) [F.IsQuasicoherent]
    (U : X.Opens) (hU : IsAffineOpen U) {n : ℕ} (g : Fin n → Γ(X, U))
    (hg : PrimeSpectrum.IsStandardOpenCoverOfSpectrum g) (p : ℕ) (hp : 0 < p) :
    IsZero (((cechComplexFunctor fun i ↦ X.basicOpen (g i)).obj
      ((SheafOfModules.toSheaf X.ringCatSheaf).obj F).obj).homology p)
```

## Tag 01XB, a lemma

[Tag 01XB](https://stacks.math.columbia.edu/tag/01XB) in the Stacks Project.

**`Stacks.Cohomology.Cech.isZero_hgroup_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Cech/AffineVanishing.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Cech/AffineVanishing.lean#L307). References: EGA III (1.3.1), “more general”; EGA I (5.1.9.2), “more general”; EGA II (5.2.4).

> **Serre vanishing on affine schemes.** The positive-degree cohomology of a
> quasi-coherent module on an affine open of a scheme vanishes.

```lean
theorem isZero_hgroup_of_isAffineOpen (X : Scheme.{u}) (F : X.Modules)
    [F.IsQuasicoherent] (U : X.Opens) (hU : IsAffineOpen U) (p : ℕ) (hp : 0 < p) :
    IsZero (Hgroup X.ringCatSheaf U p F)
```

**`Stacks.Duality.Coherator.affineAmplitudeIn_zero_zero_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/QuasiCoherentAffineAmplitude.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/QuasiCoherentAffineAmplitude.lean#L134). The attribute's comment: “the vanishing in positive degrees, together with left exactness in negative degrees, in the hypercohomology spelling of Coherator.AffineAmplitudeIn at the locally small model”.

> **A quasi-coherent module has affine amplitude in `[0, 0]`.** Placed in degree zero, a
> quasi-coherent `𝒪_X`-module has hypercohomology over every affine open of `X` concentrated in
> degree zero: this is the vanishing in negative degrees of
> `Stacks.Duality.Coherator.isZero_homology_derivedSectionsLocallySmall_single_of_neg` together with
> Serre vanishing ([Stacks, Tag 01XB]) in positive degrees.
>
> It is the hypothesis of [Stacks, Tag 0CSA] at `a = b = 0`, which is what Example
> [Stacks, Tag 0CSB] feeds that tag.

```lean
theorem affineAmplitudeIn_zero_zero_single (M : X.Modules) [M.IsQuasicoherent] :
    AffineAmplitudeIn X 0 0 ((DerivedCategory.singleFunctor X.Modules 0).obj M)
```

## Tag 01XC, a lemma

[Tag 01XC](https://stacks.math.columbia.edu/tag/01XC) in the Stacks Project.

**`Stacks.Cohomology.Affine.isZero_rightDerived_pushforward_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineCohomologyVanishing/Basic.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineCohomologyVanishing/Basic.lean#L241).

> **[Stacks, Tag 01XC].** If `f : X ⟶ S` is an affine morphism of schemes and `F` is a
> quasi-coherent `𝒪_X`-module, then `Rⁱ f_* F` vanishes for every `i > 0`.

```lean
theorem isZero_rightDerived_pushforward_of_isAffineHom {X S : Scheme.{u}} (f : X ⟶ S)
    (F : X.Modules) [IsAffineHom f] [F.IsQuasicoherent] (i : ℤ) (hi : 0 < i) :
    IsZero (((Scheme.Modules.pushforward f).rightDerivedPlus i).obj F)
```

**`Stacks.AffineHigherDirectImage.isZero_rightDerivedPlus_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineHigherDirectImage/Vanishing.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineHigherDirectImage/Vanishing.lean#L239).

> **[Stacks, Tag 01XC].** If `f : X ⟶ S` is an affine morphism of schemes and `F` is a
> quasi-coherent `𝒪_X`-module, then `R ⁱ f_* F = 0` for every `i > 0`.

```lean
theorem isZero_rightDerivedPlus_pushforward [IsAffineHom f] (F : X.Modules)
    [F.IsQuasicoherent] (i : ℤ) (hi : 0 < i) :
    IsZero (((Scheme.Modules.pushforward f).rightDerivedPlus i).obj F)
```

## Tag 089W, a lemma

[Tag 089W](https://stacks.math.columbia.edu/tag/089W) in the Stacks Project.

**`Stacks.Cohomology.AffineComparison.cohomologyIsoPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineCohomologyComparison/Basic.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineCohomologyComparison/Basic.lean#L209).

> **[Stacks, Tag 089W].** For an affine morphism of schemes `f : X ⟶ S` and a quasi-coherent
> `𝒪_X`-module `F`, the cohomology of `F` on `X` is the cohomology of its direct image on `S`, in
> every degree `i ≥ 0`, as modules over `Γ(S, ⊤)` after restriction of scalars along `f^♯`.
>
> The higher direct images vanish ([Stacks, Tag 01XC]), so `F` is acyclic for `f_*`, and the
> direct image of an injective module has acyclic sections ([Stacks, Tag 01EX] part (2)), so the
> right derived functor of `Γ(S, ⊤) ∘ f_*` collapses onto `H^i(S, f_* −)`; the other factor is
> `Γ(X, ⊤)` with its scalars restricted, by [Stacks, Tag 01EZ].

```lean
public def cohomologyIsoPushforward [AlgebraicGeometry.IsAffineHom f]
    (F : X.Modules) [F.IsQuasicoherent] (n : ℕ) :
    (ModuleCat.restrictScalars f.appTop.hom).obj
        (((moduleGlobalSections X).rightDerived n).obj F) ≅
      ((moduleGlobalSections S).rightDerived n).obj
        ((AlgebraicGeometry.Scheme.Modules.pushforward f).obj F)
```

**`Stacks.AffineCohomologyPushforward.cohomologyPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineHigherDirectImage/Natural.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineHigherDirectImage/Natural.lean#L266). The attribute's comment: “the natural isomorphism”. References: EGA II (5.2.3); EGA III (1.3.4), “g to a point”; EGA III (1.3.3).

> **[Stacks, Tag 089W].** For an affine morphism of schemes `f : X ⟶ S`, cohomology of a
> quasi-coherent module is canonically isomorphic to cohomology of its pushforward, *naturally in
> the module*: this is an isomorphism of functors on the category of quasi-coherent
> `𝒪_X`-modules, not a choice of isomorphism for each one.

```lean
def cohomologyPushforwardIso [IsAffineHom f] (i : ℕ) :
    ObjectProperty.ι (SheafOfModules.isQuasicoherent (R := X.ringCatSheaf)) ⋙
        Hfunctor X.ringCatSheaf ⊤ i ≅
      ObjectProperty.ι (SheafOfModules.isQuasicoherent (R := X.ringCatSheaf)) ⋙
        Scheme.Modules.pushforward f ⋙ Hfunctor S.ringCatSheaf ⊤ i
```

**`Stacks.AffineCohomologyResolution.cohomologyPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineMorphismCohomology/Normalized.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineMorphismCohomology/Normalized.lean#L110). The attribute's comment: “the natural isomorphism”. References: EGA II (5.2.3); EGA III (1.3.4), “g to a point”; EGA III (1.3.3).

> **[Stacks, Tag 089W].** For an affine morphism, cohomology of a quasi-coherent module
> is canonically isomorphic to cohomology of its pushforward. The isomorphism is a
> natural isomorphism on the category of quasi-coherent modules, rather than an
> unrelated choice of an isomorphism for each module.

```lean
public noncomputable def cohomologyPushforwardIso [IsAffineHom f] (i : ℕ) :
    ObjectProperty.ι (SheafOfModules.isQuasicoherent X.ringCatSheaf) ⋙
          Hfunctor X.ringCatSheaf ⊤ i ≅
      ObjectProperty.ι (SheafOfModules.isQuasicoherent X.ringCatSheaf) ⋙
          Scheme.Modules.pushforward f ⋙ Hfunctor S.ringCatSheaf ⊤ i
```

**`Stacks.AffineCohomologyResolution.cohomologyPushforwardIso_hom_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineMorphismCohomology/Normalized.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineMorphismCohomology/Normalized.lean#L133). The attribute's comment: “comparison of resolutions”.

> The affine cohomology isomorphism is computed by any map from the pushforward
> of an injective resolution to an injective resolution of the pushforward that
> preserves the augmentation. Global sections of the pushed-forward complex are
> definitionally global sections of the original complex.

```lean
public theorem cohomologyPushforwardIso_hom_eq [IsAffineHom f] (F : X.Modules)
    [F.IsQuasicoherent] (i : ℕ)
    (I : InjectiveResolution (C := SheafOfModules X.ringCatSheaf) F)
    (J : InjectiveResolution (C := SheafOfModules S.ringCatSheaf)
      ((Scheme.Modules.pushforward f).obj F))
    (φ : ((Scheme.Modules.pushforward f).mapHomologicalComplex (ComplexShape.up ℕ)).obj
      I.cocomplex ⟶ J.cocomplex)
    (hφ : (Scheme.Modules.pushforward f).map (I.ι.f 0) ≫ φ.f 0 = J.ι.f 0) :
    (cohomologyPushforwardIso f i).hom.app ⟨F, inferInstance⟩ =
      (I.isoRightDerivedObj (secF X.ringCatSheaf ⊤) i).hom ≫
        HomologicalComplex.homologyMap
          (((secF S.ringCatSheaf ⊤).mapHomologicalComplex (ComplexShape.up ℕ)).map φ) i ≫
        (J.isoRightDerivedObj (secF S.ringCatSheaf ⊤) i).inv
```

**`Stacks.AffineCohomologyResolution.cohomologyPushforwardIso_zero_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineMorphismCohomology/Normalized.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineMorphismCohomology/Normalized.lean#L162). The attribute's comment: “degree-zero normalization”.

> In degree zero, the affine cohomology isomorphism agrees with the ordinary
> identification of global sections through the canonical maps to zeroth right
> derived functors.

```lean
public theorem cohomologyPushforwardIso_zero_hom [IsAffineHom f] :
    Functor.whiskerLeft
          (ObjectProperty.ι (SheafOfModules.isQuasicoherent X.ringCatSheaf))
          (secF X.ringCatSheaf ⊤).toRightDerivedZero ≫
        (cohomologyPushforwardIso f 0).hom =
      Functor.whiskerLeft
          (ObjectProperty.ι (SheafOfModules.isQuasicoherent X.ringCatSheaf))
          (sectionsPushforwardIso f).hom ≫
        Functor.whiskerLeft
          (ObjectProperty.ι (SheafOfModules.isQuasicoherent X.ringCatSheaf) ⋙
            Scheme.Modules.pushforward f)
          (secF S.ringCatSheaf ⊤).toRightDerivedZero
```

## Tag 0BDX, a lemma

[Tag 0BDX](https://stacks.math.columbia.edu/tag/0BDX) in the Stacks Project.

**`AlgebraicGeometry.isAffineHom_diagonal_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AffineDiagonal.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AffineDiagonal.lean#L96). The attribute's comment: “equivalent conditions”.

> **Stacks Project, Tag 0BDX.** For a scheme `X`, the following are
> equivalent: its diagonal is affine; intersections of two affine opens are
> affine; and it admits an affine open cover all of whose nonempty finite
> intersections are affine.

```lean
theorem isAffineHom_diagonal_tfae (X : Scheme.{u}) : List.TFAE [
    IsAffineHom (pullback.diagonal (terminal.from X)),
    ∀ (U V : X.Opens), IsAffineOpen U → IsAffineOpen V → IsAffineOpen (U ⊓ V),
    ∃ 𝒰 : Scheme.AffineOpenCover.{u} X,
      ∀ (p : ℕ) (i : Fin (p + 1) → 𝒰.I₀),
        IsAffineOpen (⨅ j, (𝒰.f (i j)).opensRange)]
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.IsSeparated.isSeparated_terminal_from`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.IsSeparated.isSeparated_terminal_from#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AffineDiagonal.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AffineDiagonal.lean#L49) (StacksFrontier): “separated case: the structure morphism is separated”.
- [`AlgebraicGeometry.IsSeparated.isClosedImmersion_diagonal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsSeparated.isClosedImmersion_diagonal#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AffineDiagonal.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AffineDiagonal.lean#L51) (StacksFrontier): “separated case: the diagonal is a closed immersion”.
- [`AlgebraicGeometry.IsClosedImmersion.instIsAffineHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.instIsAffineHom#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AffineDiagonal.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AffineDiagonal.lean#L53) (StacksFrontier): “separated case: closed immersions are affine”. References: EGA I (4.2.3), “more general”; EGA II (1.2.2); EGA II (1.6.2); SGA 3 VIB (2.9.1), “special case”; SGA 3 XXV (4.3), “partial”.

## Tag 01XD, a lemma

[Tag 01XD](https://stacks.math.columbia.edu/tag/01XD) in the Stacks Project.

**`Stacks.Cohomology.Affine.isIso_cechCohomologyToCohomology_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineCohomologyVanishing/CechAffineCover.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineCohomologyVanishing/CechAffineCover.lean#L100). References: EGA III (1.4.1); EGA III (1.4.2), “more general”.

> **[Stacks, Tag 01XD].** A covering of an open subset of a scheme whose finite intersections
> are all affine opens computes the cohomology of a quasi-coherent module by its Čech complex: the
> canonical comparison of [Stacks, Tag 01EQ] from Čech cohomology to sheaf cohomology is an
> isomorphism of `Γ(U, 𝒪_X)`-modules in every degree.

```lean
public theorem isIso_cechCohomologyToCohomology_of_isAffineOpen
    (X : Scheme.{u}) {I : Type u} (U : X.Opens) (Ui : I → X.Opens) (hU : U = ⨆ i, Ui i)
    (haffine : ∀ (r : ℕ) (s : Fin (r + 1) → I), IsAffineOpen (⨅ k, Ui (s k)))
    (F : X.Modules) [F.IsQuasicoherent] (p : ℕ) :
    IsIso ((cechCohomologyToCohomology X.ringCatSheaf U Ui hU (p : ℤ)).app F)
```

**`Stacks.Cohomology.CechAffineCover.isIso_cechCohomologyToCohomology_app_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineCover/Basic.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineCover/Basic.lean#L86). References: EGA III (1.4.1); EGA III (1.4.2), “more general”.

> **[Stacks, Tag 01XD]: a cover of a scheme whose finite intersections are affine computes the
> cohomology of a quasi-coherent module by its Čech complex.** The canonical comparison
> `Ȟᵖ(𝒰, F) ⟶ Hᵖ(U, F)` of [Stacks, Tag 01EQ] is an isomorphism of `Γ(U, 𝒪_X)`-modules for every
> `p`.

```lean
theorem isIso_cechCohomologyToCohomology_app_of_isAffineOpen
    (haff : ∀ (r : ℕ) (s : Fin (r + 1) → I), IsAffineOpen (⨅ k, Ui (s k)))
    (F : X.Modules) [F.IsQuasicoherent] (p : ℕ) :
    IsIso ((cechCohomologyToCohomology X.ringCatSheaf U Ui hU (p : ℤ)).app F)
```

**`Stacks.Cohomology.Cech.isIso_cechCohomologyToCohomology_app_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Cech/AffineIntersectionComparison.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Cech/AffineIntersectionComparison.lean#L87). References: EGA III (1.4.1).

> **[Stacks, Tag 01XD].** Let `X` be a scheme and let `U` be an open covering of `X` such
> that every intersection `U_{i₀} ⊓ … ⊓ U_{iₚ}` is affine. For a quasi-coherent `𝒪_X`-module `ℱ`
> the canonical comparison from the Čech cohomology of the covering to the cohomology of `ℱ` is
> an isomorphism of `Γ(X, 𝒪_X)`-modules in every degree.

```lean
public theorem isIso_cechCohomologyToCohomology_app_of_isAffineOpen (X : Scheme.{u})
    {I : Type u} (U : I → X.Opens) (hU : IsOpenCover U)
    (hUaffine : ∀ (p : ℕ) (i : Fin (p + 1) → I), IsAffineOpen (⨅ j, U (i j)))
    (F : X.Modules) [F.IsQuasicoherent] (p : ℕ) :
    IsIso ((Stacks.Cohomology.CechDerived.cechCohomologyToCohomology X.ringCatSheaf
      (⊤ : X.Opens) U hU.symm (p : ℤ)).app F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.2, Tag 01X8](https://stacks.math.columbia.edu/tag/01X8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
