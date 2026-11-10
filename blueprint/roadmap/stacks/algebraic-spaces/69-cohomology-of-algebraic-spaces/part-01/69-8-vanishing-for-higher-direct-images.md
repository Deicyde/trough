---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_forall_isZero_rightDerived_modulePushforward_of_qcqs, AlgebraicGeometry.Space.exists_forall_isZero_rightDerived_modulePushforward, AlgebraicGeometry.Space.exists_forall_isZero_rightDerived_modulePushforward_of_representable, AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isQuasicoherentOnSite, AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isAffineHom, AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_isAffineHom, AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isAffineHom_of_isQuasicoherent, AlgebraicGeometry.Space.cohomologyCollapseIsoOfIsAffineHom
statement: formalized
proof: formalized
---

# 69.8 Vanishing for higher direct images

Section 69.8 of the Stacks Project, [Tag 073F](https://stacks.math.columbia.edu/tag/073F). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 073G, a lemma

[Tag 073G](https://stacks.math.columbia.edu/tag/073G) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_forall_isZero_rightDerived_modulePushforward_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/HigherDirectImageUniformBound.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/HigherDirectImageUniformBound.lean#L503).

> **[Stacks, Tag 073G].**  Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of
> algebraic spaces over `S`, with `Y` quasi-compact.  There is a single degree `n(X → Y)` such that
> for every algebraic space `Y'`, every morphism `Y' ⟶ Y`, every algebraic space `X'` making
> `X' ⟶ X`, `X' ⟶ Y'` a cartesian square over `f`, and every quasi-coherent `𝒪_{X'}`-module `𝓕'`,
> the higher direct images `R^q f'_*𝓕'` vanish for `q ≥ n(X → Y)`.

```lean
theorem exists_forall_isZero_rightDerived_modulePushforward_of_qcqs {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hYqc : IsQuasiCompactSpace B S hS Y.1) :
    ∃ N : ℕ, ∀ (Y' X' : AlgebraicSpaces B S hS) (g : Y' ⟶ Y) (i' : X' ⟶ X) (f' : X' ⟶ Y'),
      IsPullback i' f' f g →
      ∀ F' : Modules.{u, u} B S hS X'.1 X'.2, F'.IsQuasicoherentOnSite → ∀ q : ℕ, N ≤ q →
        IsZero (((modulePushforward B S hS f').rightDerived q).obj F')
```

**`AlgebraicGeometry.Space.exists_forall_isZero_rightDerived_modulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniformHigherDirectImageVanishing.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniformHigherDirectImageVanishing.lean#L252). The attribute's comment: “the source's quantifier order -- one n from f alone, outside the base change, the module and the degree -- and step (2) of its proof, the reduction of an arbitrary base to a scheme base. No number is produced: hscheme (that bound over a scheme base: Stacks 0720, 0733 and 072C) and h03F3 (Stacks 03F3(1), needed by 03LX) are carried; Y quasi-compact not assumed”.

> **[Stacks, Tag 073G], with the scheme-base case carried.**  Let `f : X ⟶ Y` be a
> quasi-compact and quasi-separated morphism of algebraic spaces over `S`.  Then there is a single
> degree `n(X → Y)` such that for every algebraic space `Y'`, every morphism `Y' ⟶ Y`, every
> algebraic space `X'` making `X' ⟶ X`, `X' ⟶ Y'` a cartesian square over `f`, and every
> quasi-coherent `𝒪_{X'}`-module `𝓕'`, the higher direct images `R^q f'_*𝓕'` vanish for
> `q ≥ n(X → Y)`.
>
> The quantifiers are the source's and in the source's order: `n(X → Y)` is produced once and for
> all from `f`, before any base change and before any coefficient module.  The uniformity in `Y'`
> is what `AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_schemeBase` supplies;
> the integer itself comes from `hscheme`, the case of a base which is a scheme, which is **not**
> proved in this development.

```lean
theorem exists_forall_isZero_rightDerived_modulePushforward {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (h03F3 : ∀ (Z W : AlgebraicSpaces B S hS) (i : W ⟶ Z) (hi : IsEtale B S hS i.hom),
      (etaleModulePullback.{u, u} B S hS i hi).PreservesInjectiveObjects)
    (hscheme : ∃ N : ℕ, SchemeBaseUniformVanishing B S hS f N) :
    ∃ N : ℕ, ∀ (Y' X' : AlgebraicSpaces B S hS) (g : Y' ⟶ Y) (i' : X' ⟶ X) (f' : X' ⟶ Y'),
      IsPullback i' f' f g →
      ∀ F' : Modules.{u, u} B S hS X'.1 X'.2, F'.IsQuasicoherentOnSite → ∀ q : ℕ, N ≤ q →
        have := hasInjectiveResolutions_modules B S hS X'.1 X'.2
        IsZero (((modulePushforward B S hS f').rightDerived q).obj F')
```

**`AlgebraicGeometry.Space.exists_forall_isZero_rightDerived_modulePushforward_of_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniformHigherDirectImageVanishing.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniformHigherDirectImageVanishing.lean#L332). The attribute's comment: “the same for a REPRESENTABLE f, with h03F3 discharged: there the chartwise identification is Stacks 071Z, which proves Stacks 03F3(1). hscheme is still carried and Y quasi-compact is still not assumed”.

> **[Stacks, Tag 073G] for a representable morphism, with only the scheme-base case carried.**
> Let `f : X ⟶ Y` be a representable, quasi-compact and quasi-separated morphism of algebraic
> spaces over `S`.  Then there is a single degree `n(X → Y)` above which every higher direct image
> of every quasi-coherent module along every base change of `f` vanishes.
>
> This is `AlgebraicGeometry.Space.exists_forall_isZero_rightDerived_modulePushforward` with the
> injective-preservation hypothesis `h03F3` discharged by representability.

```lean
theorem exists_forall_isZero_rightDerived_modulePushforward_of_representable
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : yoneda.relativelyRepresentable f.hom)
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hscheme : ∃ N : ℕ, SchemeBaseUniformVanishing B S hS f N) :
    ∃ N : ℕ, ∀ (Y' X' : AlgebraicSpaces B S hS) (g : Y' ⟶ Y) (i' : X' ⟶ X) (f' : X' ⟶ Y'),
      IsPullback i' f' f g →
      ∀ F' : Modules.{u, u} B S hS X'.1 X'.2, F'.IsQuasicoherentOnSite → ∀ q : ℕ, N ≤ q →
        have := hasInjectiveResolutions_modules B S hS X'.1 X'.2
        IsZero (((modulePushforward B S hS f').rightDerived q).obj F')
```

## Tag 073H, a lemma

[Tag 073H](https://stacks.math.columbia.edu/tag/073H) in the Stacks Project.

**`AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineHigherPushforwardUnconditional.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineHigherPushforwardUnconditional.lean#L44).

> For an affine morphism `f : X ⟶ Y` of algebraic spaces over `S`, a quasi-coherent
> `𝒪_X`-module `𝓕` and `n > 0`, the higher direct image vanishes: `R^n f_* 𝓕 = 0`.

```lean
theorem isZero_rightDerived_modulePushforward_of_isQuasicoherentOnSite
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (haff : IsAffineHom B S hS f.hom)
    (G : Modules.{u, u} B S hS X.1 X.2) (hG : G.IsQuasicoherentOnSite) (n : ℕ) (hn : 0 < n) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    IsZero (((modulePushforward B S hS f).rightDerived n).obj G)
```

**`AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineHigherPushforwardVanishing.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineHigherPushforwardVanishing.lean#L255). The attribute's comment: “the reduction of the source's statement along étale scheme charts, by Stacks 071Z; the affine case of the source's proof — the étale-site analogue of Stacks 01XC, that is Stacks 03DW — is carried as the hypothesis `h03DW` and is not proved”.

> **Stacks 073H with the affine case carried as `h03DW`.**
>
> If `f : X ⟶ Y` is an affine morphism of algebraic spaces over `S` whose chart base changes have
> vanishing degree-`n` higher direct images, then `R^n f_* 𝓕 = 0`.
>
> This is the previous theorem with representability supplied by
> `AlgebraicGeometry.Space.relativelyRepresentable_of_isAffineHom`.  The source's statement is
> this one for `n > 0` and quasi-coherent `𝓕` with `h03DW` discharged; neither restriction on `n`
> nor on `𝓕` is used by the reduction, and `h03DW` is not available in this repository.

```lean
theorem isZero_rightDerived_modulePushforward_of_isAffineHom {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsAffineHom B S hS f.hom)
    (F : Modules.{u, u} B S hS X.obj X.property) (n : ℕ)
    (h03DW : ChartwiseIsZeroHigherDirectImage B S hS f
      (relativelyRepresentable_of_isAffineHom B S hS f hf) F n) :
    have := hasInjectiveResolutions_modules B S hS X.obj X.property
    IsZero (((modulePushforward B S hS f).rightDerived n).obj F)
```

**`AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineHigherPushforwardVanishingUnconditional.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineHigherPushforwardVanishingUnconditional.lean#L140).

> Let `f : X ⟶ Y` be an affine morphism of algebraic spaces over a scheme `S` contained in a
> big fppf site `B`, and let `𝓕` be a quasi-coherent `𝒪_X`-module. Then the higher direct images
> `R^p f_* 𝓕` vanish for `p > 0`, the direct image being
> `AlgebraicGeometry.Space.modulePushforward`.

```lean
theorem isZero_rightDerived_modulePushforward_isAffineHom (f : X ⟶ Y)
    (haff : IsAffineHom B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) (p : ℕ) (hp : 0 < p) :
    IsZero (((modulePushforward B S hS f).rightDerived p).obj F)
```

**`AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isAffineHom_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismHigherDirectImageVanishing.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismHigherDirectImageVanishing.lean#L99).

> **Stacks 073H.** Let `f : X ⟶ Y` be an affine morphism of algebraic spaces over `S` and let
> `𝓕` be a quasi-coherent `𝒪_X`-module.  Then `R^n f_*𝓕 = 0` for every `n > 0`.
>
> The direct image along the representable `f` is the direct image along base change of étale
> charts (`AlgebraicGeometry.Space.modulePushforwardChartIso`); by Stacks 072W its higher direct
> images vanish once the cohomology of `𝓕` vanishes over the base changes of a covering family of
> each chart of `Y`; the affine charts form such a family, their base changes are affine charts of
> `X` because `f` is affine, and over an affine chart a quasi-coherent module has no higher
> cohomology.

```lean
theorem isZero_rightDerived_modulePushforward_of_isAffineHom_of_isQuasicoherent (f : X ⟶ Y)
    (hf : IsAffineHom B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) (n : ℕ) (hn : 0 < n) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    IsZero (((modulePushforward B S hS f).rightDerived n).obj F)
```

## Tag 0D2U, a lemma

[Tag 0D2U](https://stacks.math.columbia.edu/tag/0D2U) in the Stacks Project.

**`AlgebraicGeometry.Space.cohomologyCollapseIsoOfIsAffineHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismCohomologyCollapse.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismCohomologyCollapse.lean#L171). The attribute's comment: “Leray collapse of the source's one-line proof; carries two unproved hypotheses, `h03DW` (073H's own) and `h072Z` (072Z via 0731(3)) -- see the notes”.

> **Stacks 0D2U with `h03DW` and `h072Z` carried.**
>
> Let `f : X ⟶ Y` be an affine morphism of algebraic spaces over `S` and `𝓕` an `𝒪_X`-module.
> Then the cohomology of `𝓕` on `X` — computed as the derived functor of `Γ(Y, f_* −)` — is the
> cohomology of `f_*𝓕` on `Y`, in every degree.
>
> This is the previous isomorphism with representability supplied by
> `AlgebraicGeometry.Space.relativelyRepresentable_of_isAffineHom`, so that `h03DW` is exactly the
> hypothesis carried by
> `AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isAffineHom`, the library's
> form of Stacks 073H.  The source's statement is this one with `h03DW` and `h072Z`
> discharged, for a quasi-coherent `𝓕`; quasi-coherence is not used, and neither hypothesis is
> available in this repository.

```lean
def cohomologyCollapseIsoOfIsAffineHom (f : X ⟶ Y) (hf : IsAffineHom B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2)
    (h03DW : ∀ n, 0 < n → ChartwiseIsZeroHigherDirectImage B S hS f
      (relativelyRepresentable_of_isAffineHom B S hS f hf) F n)
    (h072Z : AcyclicPushforwardOfInjective B S hS f) (i : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    have := enoughInjectives_modules B S hS Y.1 Y.2
    (((modulePushforward B S hS f ⋙ globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O))).rightDerived i).obj F ≅
      ((globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O))).rightDerived i).obj
        ((modulePushforward B S hS f).obj F))
```

**`AlgebraicGeometry.Space.cohomologyUliftIsoOfIsAffineHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismCohomologyOverRing.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismCohomologyOverRing.lean#L359).

> **Stacks 0D2U.** Let `f : X ⟶ Y` be an affine morphism of algebraic spaces over `S` and `𝓕`
> a quasi-coherent `𝒪_X`-module. Then `Hⁱ(X, 𝓕) = Hⁱ(Y, f_*𝓕)` for every `i ≥ 0`.
>
> The cohomology is that of the universe lifts of the two modules to the universe of the small
> étale sites, the universe in which `AlgebraicGeometry.Space.eulerCharacteristic` (Stacks 0DN1)
> is taken; the isomorphism is one of abelian groups, and of `A`-modules for any ring maps to the
> global functions compatible with `f`
> (`AlgebraicGeometry.Space.cohomologyUliftOverRingIsoOfIsAffineHom`).

```lean
def cohomologyUliftIsoOfIsAffineHom.{w} (haff : IsAffineHom B S hS f.hom)
    (G : Modules.{u, u} B S hS X.1 X.2) (hG : G.IsQuasicoherentOnSite) (q : ℕ) :
    (forget₂ _ AddCommGrpCat.{max (u + 1) w}).obj
        ((globalModuleCohomology.{u + 1, u, u, w}
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O)) q).obj
          (SheafOfModules.uliftForPresentation.{u + 1, u, u, u, max (u + 1) w} G)) ≅
      (forget₂ _ AddCommGrpCat.{max (u + 1) w}).obj
        ((globalModuleCohomology.{u + 1, u, u, w}
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O)) q).obj
          (SheafOfModules.uliftForPresentation.{u + 1, u, u, u, max (u + 1) w}
            ((modulePushforward B S hS f).obj G)))
```

**`AlgebraicGeometry.Space.cohomologyCollapseIsoOfIsFlatOfIsAffineHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatAffineCohomologyCollapse.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatAffineCohomologyCollapse.lean#L78). The attribute's comment: “for a FLAT affine morphism, with both of 0D2U's hypotheses discharged; flatness is not the source's hypothesis and is used only to reach 072Z's conclusion through 0730 instead -- see the notes”.

> Let `f : X ⟶ Y` be a flat affine morphism of algebraic spaces over `S` and `𝓕` a
> quasi-coherent `𝒪_X`-module. Then for every `i` the `i`-th right derived functor of `Γ(Y, f_*−)`
> at `𝓕` is isomorphic to the `i`-th cohomology of `f_*𝓕` on `Y`.

```lean
def cohomologyCollapseIsoOfIsFlatOfIsAffineHom (f : X ⟶ Y) (haff : IsAffineHom B S hS f.hom)
    (hflat : IsFlat B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) (i : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    have := enoughInjectives_modules B S hS Y.1 Y.2
    (((modulePushforward B S hS f ⋙ globalSectionsFunctor.{u + 1, u, u, u}
          (ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O)).rightDerived i).obj F ≅
      ((globalSectionsFunctor.{u + 1, u, u, u}
          (ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O)).rightDerived i).obj
        ((modulePushforward B S hS f).obj F))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.cohomologyIsoOfIsAffineHom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismCohomologyIso.lean#L228), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismCohomologyCollapseUnconditional.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismCohomologyCollapseUnconditional.lean#L128) (StacksFrontier).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.8, Tag 073F](https://stacks.math.columbia.edu/tag/073F)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
