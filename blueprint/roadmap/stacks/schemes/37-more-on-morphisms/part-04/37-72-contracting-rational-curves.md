---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_firstCohomologyStructureSheaf_fiber_of_isZero_firstDirectImage, Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_firstCohomologyStructureSheaf_fiber_of_isZero_firstDirectImage_baseChange, Stacks.AlgebraicGeometry.TopDegreeBaseChange.exists_isOpen_isZero_restrict_firstDirectImage_of_isZero_cohomologyOne_fiber, Stacks.AlgebraicGeometry.TopDegreeBaseChange.exists_isOpen_isZero_restrict_firstDirectImage_of_isPullback_of_isZero_cohomologyOne_fiber, Stacks.AlgebraicGeometry.TopDegreeBaseChange.exists_isOpen_firstDirectImage_vanishes_universally, Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_higherDirectImage_of_one_lt_of_isProper, Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_cohomology_of_notMem_zero_one_of_isAffine, Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_cohomology_one_of_generatingSections_of_isAffine
statement: formalized
proof: formalized
---

# 37.72 Contracting rational curves

Section 37.72 of the Stacks Project, [Tag 0E7E](https://stacks.math.columbia.edu/tag/0E7E). 8 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E7F, a lemma

[Tag 0E7F](https://stacks.math.columbia.edu/tag/0E7F) in the Stacks Project.

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_firstCohomologyStructureSheaf_fiber_of_isZero_firstDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreFirstCohomology.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreFirstCohomology.lean#L371). The attribute's comment: “part (1)”. References: EGA III (7.9.10.1), “partial”.

> **[Stacks, Tag 0E7F], part (1).** Let `f : X ⟶ Y` be proper and let `y ∈ Y` be a point whose
> fibre has dimension at most one. If `R¹ f_* 𝒪_X = 0`, then `H¹(X_y, 𝒪_{X_y}) = 0`.
>
> [Stacks, Tag 0E7D] part (2) shrinks `Y` to an affine open `V ∋ y` above which the higher direct
> images of quasi-coherent modules vanish in degrees above one, and
> `isZero_firstCohomologyStructureSheaf_fiber_of_vanishing_restrict` concludes over `V`.

```lean
theorem isZero_firstCohomologyStructureSheaf_fiber_of_isZero_firstDirectImage
    (f : X ⟶ Y) [IsProper f] (y : Y)
    (hdim : topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞))
    (hR : IsZero (firstDirectImageStructureSheaf f)) :
    IsZero (firstCohomologyStructureSheaf (f.fiber y))
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_firstCohomologyStructureSheaf_fiber_of_isZero_firstDirectImage_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreFirstCohomology.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreFirstCohomology.lean#L391). The attribute's comment: “part (2)”. References: EGA III (7.9.10.1), “partial”.

> **[Stacks, Tag 0E7F], part (2).** Let `f : X ⟶ Y` be proper and let `y ∈ Y` be a point whose
> fibre has dimension at most one. If there is a morphism `g : Y' ⟶ Y` with `y` in its image such
> that the base change `f' : X ×_Y Y' ⟶ Y'` of `f` by `g` has `R¹ f'_* 𝒪_{X'} = 0`, then
> `H¹(X_y, 𝒪_{X_y}) = 0`.
>
> [Stacks, Tag 0E7D] part (2) shrinks `Y` to an affine open `V ∋ y` above which the higher direct
> images of quasi-coherent modules vanish in degrees above one, and
> `isZero_firstCohomologyStructureSheaf_fiber_of_vanishing_restrict_baseChange` concludes over
> `V`.

```lean
theorem isZero_firstCohomologyStructureSheaf_fiber_of_isZero_firstDirectImage_baseChange
    (f : X ⟶ Y) [IsProper f] (y : Y)
    (hdim : topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞))
    {Y' : Scheme.{u}} (g : Y' ⟶ Y) (hy : y ∈ Set.range g)
    (hR : IsZero (firstDirectImageStructureSheaf (pullback.snd f g))) :
    IsZero (firstCohomologyStructureSheaf (f.fiber y))
```

## Tag 0E7G, a lemma

[Tag 0E7G](https://stacks.math.columbia.edu/tag/0E7G) in the Stacks Project.

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.exists_isOpen_isZero_restrict_firstDirectImage_of_isZero_cohomologyOne_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/ContractingRationalCurves.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/ContractingRationalCurves.lean#L215). The attribute's comment: “the clauses of Tags 0EX4 and 0EX3 (b) are the hypotheses `hft`, `hbc`”.

> **[Stacks, Tag 0E7G].** Let `f : X ⟶ Y` be proper and let `y ∈ Y` be a point whose fibre has
> dimension at most one and satisfies `H¹(X_y, 𝒪_{X_y}) = 0`. Then there is an open `V ∋ y` with
> `R¹ f_* 𝒪_X|_V = 0`, and `R¹ f'_* 𝒪_{X'} = 0` for the base change along every `g : Y' ⟶ V`.
>
> The hypothesis on the fibre makes `R¹ (f_y)_* 𝒪_{X_y}` vanish over the affine base `Spec κ(y)`,
> hence by `hbc` the pullback of `R¹ f_* 𝒪_X` along `Spec κ(y) ⟶ Y`; so `y` misses the support of
> `R¹ f_* 𝒪_X` by [Stacks, Tag 056J]. The support is closed because of the finite-type clause
> `hft`, which gives the neighbourhood `V`. Universality after base change is `hbc` again, applied
> to `g ≫ V.ι` and read through the compatibility of pullback with composition.

```lean
theorem exists_isOpen_isZero_restrict_firstDirectImage_of_isZero_cohomologyOne_fiber
    (f : X ⟶ Y) [IsProper f] (y : Y)
    (_hdim : topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞))
    (hft : (firstDirectImageStructureSheaf f).IsFiniteType)
    (hbc : FirstDirectImageCommutesBaseChange f)
    (hH : IsZero (firstCohomologyStructureSheaf (f.fiber y))) :
    ∃ V : Y.Opens, y ∈ V ∧
      IsZero ((Scheme.Modules.restrictFunctor V.ι).obj (firstDirectImageStructureSheaf f)) ∧
      ∀ (Y' : Scheme.{u}) (g : Y' ⟶ V.toScheme),
        IsZero (firstDirectImageStructureSheaf (pullback.snd f (g ≫ V.ι)))
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.exists_isOpen_isZero_restrict_firstDirectImage_of_isPullback_of_isZero_cohomologyOne_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/VanishingNeighbourhood.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/VanishingNeighbourhood.lean#L195).

> **[Stacks, Tag 0E7G].** Let `f : X ⟶ Y` be proper and let `y ∈ Y` be a point with
> `dim(X_y) ≤ 1` and `H¹(X_y, 𝒪_{X_y}) = 0`. Then there is an open neighbourhood `V` of `y` such
> that `R¹ f_* 𝒪_X|_V = 0`, and the same holds after base change by any `Y' ⟶ V`: for every
> cartesian square `X' ⟶ X`, `f' : X' ⟶ Y'`, `g : Y' ⟶ Y` over `f` with `g(Y') ⊆ V`,
> `R¹ f'_* 𝒪_{X'} = 0`.
>
> The source's proof: shrink to an open `W ∋ y` over which all fibres have dimension at most one
> ([Stacks, Tag 02FZ]); there `R¹ f_* 𝒪_X` is of finite type ([Stacks, Tag 0EX4],
> `firstDirectImageFiniteTypeOfFibreDimensionOne`) and its pullback to `Spec κ(y)` is `R¹` of the
> fibre, which vanishes; so `y` is outside the closed support ([Stacks, Tag 056J]), and `V` is the
> complement of the support in `W` (`exists_isOpen_firstDirectImage_vanishes_of_factor`). For a
> base change along `g` into `V`, the pullback of `R¹ f_* 𝒪_X` along `g` factors through its
> restriction to `V`, which is zero, and over `W` this pullback is `R¹ f'_* 𝒪_{X'}`
> (`isZero_pullback_firstDirectImage_iff_of_factor_of_isPullback`, the vanishing form of
> [Stacks, Tag 0EX3]).

```lean
theorem exists_isOpen_isZero_restrict_firstDirectImage_of_isPullback_of_isZero_cohomologyOne_fiber
    (f : X ⟶ Y) [IsProper f] (y : Y)
    (hdim : topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞))
    (hH : IsZero (firstCohomologyStructureSheaf (f.fiber y))) :
    ∃ V : Y.Opens, y ∈ V ∧
      IsZero ((Scheme.Modules.restrictFunctor V.ι).obj (firstDirectImageStructureSheaf f)) ∧
      ∀ ⦃X' Y' : Scheme.{u}⦄ {g' : X' ⟶ X} {f' : X' ⟶ Y'} {g : Y' ⟶ Y},
        IsPullback g' f' f g → Set.range g ⊆ V → IsZero (firstDirectImageStructureSheaf f')
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.exists_isOpen_firstDirectImage_vanishes_universally`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/VanishingNeighbourhood.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/VanishingNeighbourhood.lean#L239).

> **[Stacks, Tag 0E7G].** Let `f : X ⟶ Y` be proper and let `y ∈ Y` be a point with
> `dim(X_y) ≤ 1` and `H¹(X_y, 𝒪_{X_y}) = 0`. Then there is an open neighbourhood `V` of `y` such
> that `R¹ f_* 𝒪_X|_V = 0`, and `R¹ f'_* 𝒪_{X'} = 0` for the base change `f'` of `f` along every
> `Y' ⟶ V`.
>
> The source's proof: shrink to an open `W ∋ y` over which all fibres have dimension at most one
> ([Stacks, Tag 02FZ]); there `R¹ f_* 𝒪_X` is of finite type ([Stacks, Tag 0EX4]) and its pullback
> to `Spec κ(y)` is `R¹` of the fibre, which vanishes; so `y` is outside the closed support
> ([Stacks, Tag 056J]). This is
> `exists_isOpen_isZero_restrict_firstDirectImage_of_isPullback_of_isZero_cohomologyOne_fiber`
> read on the cartesian square of the chosen pullback along `g ≫ V.ι`.

```lean
theorem exists_isOpen_firstDirectImage_vanishes_universally (f : X ⟶ Y) [IsProper f] (y : Y)
    (hdim : topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞))
    (hH : IsZero (firstCohomologyStructureSheaf (f.fiber y))) :
    ∃ V : Y.Opens, y ∈ V ∧
      IsZero ((Scheme.Modules.restrictFunctor V.ι).obj (firstDirectImageStructureSheaf f)) ∧
      ∀ (Y' : Scheme.{u}) (g : Y' ⟶ V.toScheme),
        IsZero (firstDirectImageStructureSheaf (pullback.snd f (g ≫ V.ι)))
```

## Tag 0E7H, a lemma

[Tag 0E7H](https://stacks.math.columbia.edu/tag/0E7H) in the Stacks Project.

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_higherDirectImage_of_one_lt_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionOneCohomologyVanishing.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionOneCohomologyVanishing.lean#L102). The attribute's comment: “clause (1)”.

> **[Stacks, Tag 0E7H] clause (1).** For a proper morphism `f : X ⟶ Y` all of whose fibres
> have dimension at most one and a quasi-coherent `ℱ` on `X`, `Rᵖ f_* ℱ = 0` for every `p > 1`.
>
> This is [Stacks, Tag 0E7D] at `d = 1`. The tag's hypothesis `H¹(X_y, 𝒪_{X_y}) = 0` is not used
> for this clause and is not imposed.

```lean
theorem isZero_higherDirectImage_of_one_lt_of_isProper {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsProper f] (hdim : ∀ y : Y, topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞))
    (F : X.Modules) [F.IsQuasicoherent] (p : ℤ) (hp : 1 < p) :
    IsZero (((Scheme.Modules.pushforward f).rightDerivedPlus p).obj F)
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_cohomology_of_notMem_zero_one_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionOneCohomologyVanishing.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionOneCohomologyVanishing.lean#L116). The attribute's comment: “clause (3)”.

> **[Stacks, Tag 0E7H] clause (3).** For a proper morphism `f : X ⟶ Y` onto an affine scheme
> all of whose fibres have dimension at most one and a quasi-coherent `ℱ` on `X`,
> `Hᵖ(X, ℱ) = 0` for every `p ∉ {0, 1}`.
>
> Negative degrees vanish for formal reasons, and degrees above one by [Stacks, Tag 0E7D] over an
> affine base. The tag's hypothesis `H¹(X_y, 𝒪_{X_y}) = 0` is not used for this clause and is not
> imposed.

```lean
theorem isZero_cohomology_of_notMem_zero_one_of_isAffine {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsProper f] [IsAffine Y]
    (hdim : ∀ y : Y, topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞))
    (F : X.Modules) [F.IsQuasicoherent] (p : ℤ) (hp : p ∉ ({0, 1} : Set ℤ)) :
    IsZero (((Stacks.Cohomology.AffineBase.moduleGlobalSections X).rightDerivedPlus p).obj F)
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_cohomology_one_of_generatingSections_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionOneCohomologyVanishing.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionOneCohomologyVanishing.lean#L196). The attribute's comment: “clause (4)”.

> **[Stacks, Tag 0E7H] clause (4).** Let `f : X ⟶ Y` be a proper morphism onto an affine
> scheme such that `dim(X_y) ≤ 1` and `H¹(X_y, 𝒪_{X_y}) = 0` for every `y ∈ Y`, and let `ℱ` be a
> quasi-coherent `𝒪_X`-module which is globally generated. Then `H¹(X, ℱ) = 0`.
>
> `R¹ f_* 𝒪_X` is of finite type by [Stacks, Tag 0EX4] at `d = 1`
> (`firstDirectImageFiniteTypeOfFibreDimensionOne`), and the rest is
> `isZero_cohomology_one_of_generatingSections_of_isFiniteType`.

```lean
theorem isZero_cohomology_one_of_generatingSections_of_isAffine {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsProper f] [IsAffine Y]
    (hdim : ∀ y : Y, topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞))
    (hfib : ∀ y : Y, IsZero (firstCohomologyStructureSheaf (f.fiber y)))
    (F : X.Modules) [F.IsQuasicoherent] (σ : SheafOfModules.GeneratingSections F) :
    IsZero (((Stacks.Cohomology.AffineBase.moduleGlobalSections X).rightDerivedPlus 1).obj F)
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_higherDirectImage_one_of_epi_pullback_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionOneCohomologyVanishing.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionOneCohomologyVanishing.lean#L210). The attribute's comment: “clause (2)”.

> **[Stacks, Tag 0E7H] clause (2).** Let `f : X ⟶ Y` be a proper morphism such that
> `dim(X_y) ≤ 1` and `H¹(X_y, 𝒪_{X_y}) = 0` for every `y ∈ Y`, let `ℱ` be a quasi-coherent
> `𝒪_X`-module, and suppose there is a surjection `f^*𝒢 ⟶ ℱ` with `𝒢` quasi-coherent on `Y`.
> Then `R¹ f_* ℱ = 0`.

```lean
theorem isZero_higherDirectImage_one_of_epi_pullback_of_isProper {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsProper f]
    (hdim : ∀ y : Y, topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞))
    (hfib : ∀ y : Y, IsZero (firstCohomologyStructureSheaf (f.fiber y)))
    (F : X.Modules) [F.IsQuasicoherent] (G : Y.Modules) [G.IsQuasicoherent]
    (p : (Scheme.Modules.pullback f).obj G ⟶ F) (hp : Epi p) :
    IsZero (((Scheme.Modules.pushforward f).rightDerivedPlus 1).obj F)
```

## Tag 0E7I, a lemma

[Tag 0E7I](https://stacks.math.columbia.edu/tag/0E7I) in the Stacks Project.

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.epi_unitToPushforwardUnit_of_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/SurjectivityAfterBaseChange.lean, line 816](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/SurjectivityAfterBaseChange.lean#L816).

> **[Stacks, Tag 0E7I].** Let `f : X ⟶ Y` be a proper morphism of schemes such that
> `dim(X_y) ≤ 1` and `H¹(X_y, 𝒪_{X_y}) = 0` for every `y ∈ Y`, and suppose `𝒪_Y ⟶ f_* 𝒪_X` is
> surjective. Then `𝒪_{Y'} ⟶ f'_* 𝒪_{X'}` is surjective for every base change `f'` of `f`.
>
> Surjectivity is local on the base, and around each point of `Y'` there is an affine open mapping
> into an affine open of `Y`; over such a pair the restricted base change is a base change of
> `f ∣_ W` along a morphism of affine schemes, which factors as a closed immersion followed by a
> flat morphism through the spectrum of a polynomial algebra. The flat half is
> `surjective_appTop_of_flat_base`, and the closed-immersion half is
> `surjective_appTop_of_closedImmersion_base`, where clause (4) of [Stacks, Tag 0E7H] is
> applied to the ideal sheaf of the closed immersion.
>
> Mathlib's `IsProper` is separated, universally closed and locally of finite type; universal
> closedness gives quasi-compactness, so this is Stacks' notion of proper.

```lean
theorem epi_unitToPushforwardUnit_of_baseChange
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f]
    (hdim : ∀ y : Y, topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞))
    (hfib : ∀ y : Y, IsZero (firstCohomologyStructureSheaf (f.fiber y)))
    (hsurj : Epi (Scheme.Modules.unitToPushforwardUnit f))
    {Y' : Scheme.{u}} (g : Y' ⟶ Y) :
    Epi (Scheme.Modules.unitToPushforwardUnit (pullback.snd f g))
```

## Tag 0E7J, a lemma

[Tag 0E7J](https://stacks.math.columbia.edu/tag/0E7J) in the Stacks Project.

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.exists_isOpen_flat_fibreDimension_vanishing_epi_near_specialFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/SpecialFibreNeighbourhood.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/SpecialFibreNeighbourhood.lean#L334).

> **[Stacks, Tag 0E7J].** Let `X --f--> Y --q--> S` be morphisms of schemes and let `s ∈ S`.
> Write `f_s : X_s ⟶ Y_s` for the induced morphism of fibres over `s` (in the two spellings
> `Stacks.Flatness.fiberHom f q s` and `pullback.snd f (q.fiberι s)` of `X_s = X ×_Y Y_s`).
> Assume
>
> 1. `X ⟶ S` is locally of finite presentation and flat at the points of `X_s`,
> 2. `f` is proper,
> 3. the fibres of `f_s` have dimension at most one and `R¹ f_{s,*} 𝒪_{X_s} = 0`,
> 4. `𝒪_{Y_s} ⟶ f_{s,*} 𝒪_{X_s}` is surjective.
>
> Then there is an open `Y_s ⊆ V ⊆ Y` such that (a) `f⁻¹(V)` is flat over `S`, (b)
> `dim(X_y) ≤ 1` for `y ∈ V`, (c) `R¹ f_* 𝒪_X|_V = 0`, (d) `𝒪_V ⟶ f_* 𝒪_X|_V` is surjective,
> and (b), (c) and (d) remain true after base change of `f⁻¹(V) ⟶ V` by any `Y' ⟶ V`.
>
> (a) and (b) are `exists_isOpen_flat_and_fibreDimension_le_one`; (c) and its persistence are
> [Stacks, Tag 0E7G] along `Y_s` (`exists_isOpen_firstDirectImage_vanishes_of_factor`); (d) is
> `exists_isOpen_notMem_supp_cokernel_unit` at every point of `Y_s`, and its persistence is
> [Stacks, Tag 0E7I] (`epi_unitToPushforwardUnit_of_baseChange`), whose hypotheses on the fibres
> follow from the persistence of (b) and (c).

```lean
theorem exists_isOpen_flat_fibreDimension_vanishing_epi_near_specialFibre (f : X ⟶ Y)
    (q : Y ⟶ S) (s : S) [LocallyOfFinitePresentation (f ≫ q)] [IsProper f]
    (hflat : ∀ x : X, (f ≫ q) x = s → IsFlatAt (f ≫ q).toLRSHom.toShHom x)
    (hdim : ∀ y : q.fiber s,
      topologicalKrullDim ((Stacks.Flatness.fiberHom f q s).fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞))
    (hR : IsZero (firstDirectImageStructureSheaf (pullback.snd f (q.fiberι s))))
    (hsurj : Epi (Scheme.Modules.unitToPushforwardUnit (pullback.snd f (q.fiberι s)))) :
    ∃ V : Y.Opens, (∀ y : Y, q y = s → y ∈ V) ∧
      Flat ((f ⁻¹ᵁ V).ι ≫ (f ≫ q)) ∧
      (∀ y : Y, y ∈ V → topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞)) ∧
      IsZero ((Scheme.Modules.restrictFunctor V.ι).obj (firstDirectImageStructureSheaf f)) ∧
      Epi ((Scheme.Modules.restrictFunctor V.ι).map (Scheme.Modules.unitToPushforwardUnit f)) ∧
      ∀ (Y' : Scheme.{u}) (g : Y' ⟶ V.toScheme),
        (∀ y' : Y', topologicalKrullDim ((pullback.snd (f ∣_ V) g).fiber y') ≤
          ((1 : ℕ) : WithBot ℕ∞)) ∧
        IsZero (firstDirectImageStructureSheaf (pullback.snd (f ∣_ V) g)) ∧
        Epi (Scheme.Modules.unitToPushforwardUnit (pullback.snd (f ∣_ V) g))
```

## Tag 0E7K, a lemma

[Tag 0E7K](https://stacks.math.columbia.edu/tag/0E7K) in the Stacks Project.

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.isIso_directImageStructureSheafBaseChangeMap_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/DirectImageStructureSheafCommutesBaseChange.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/DirectImageStructureSheafCommutesBaseChange.lean#L129). The attribute's comment: “clause (b): formation of f_* 𝒪_X commutes with arbitrary base change S' ⟶ S”.

> **[Stacks, Tag 0E7K], clause (b).** Let `X ⟶ Y ⟶ S` be a commutative triangle of schemes with
> `X ⟶ S` flat, let `f : X ⟶ Y` be proper with `dim(X_y) ≤ 1` for every `y ∈ Y`, and suppose
> `R¹ f_* 𝒪_X = 0`. Then formation of `f_* 𝒪_X` commutes with arbitrary base change `S' ⟶ S`:
> for `Y' = Y ×_S S'` and `X' = X ×_Y Y'`, the canonical comparison
> `(Y' ⟶ Y)^* f_* 𝒪_X ⟶ f'_* 𝒪_{X'}` is an isomorphism.

```lean
theorem isIso_directImageStructureSheafBaseChangeMap_of_flat {X Y S : Scheme.{u}} (f : X ⟶ Y)
    (q : Y ⟶ S) [Flat (f ≫ q)] [IsProper f]
    (hdim : ∀ y : Y, topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞))
    (hR : IsZero (firstDirectImageStructureSheaf f)) {S' : Scheme.{u}} (h : S' ⟶ S) :
    IsIso (directImageStructureSheafBaseChangeMap f (pullback.fst q h))
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.isFlatOver_directImageStructureSheaf_of_fibreDimension_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/DirectImageStructureSheafCommutesBaseChange.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/DirectImageStructureSheafCommutesBaseChange.lean#L142). The attribute's comment: “clause (a): f_* 𝒪_X is flat over S”.

> **[Stacks, Tag 0E7K], clause (a).** Let `X ⟶ Y ⟶ S` be a commutative triangle of schemes with
> `X ⟶ S` flat, let `f : X ⟶ Y` be proper with `dim(X_y) ≤ 1` for every `y ∈ Y`, and suppose
> `R¹ f_* 𝒪_X = 0`. Then `f_* 𝒪_X` is flat over `S`.

```lean
theorem isFlatOver_directImageStructureSheaf_of_fibreDimension_le_one {X Y S : Scheme.{u}}
    (f : X ⟶ Y) (q : Y ⟶ S) [Flat (f ≫ q)] [IsProper f]
    (hdim : ∀ y : Y, topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞))
    (hR : IsZero (firstDirectImageStructureSheaf f)) :
    IsFlatOver q.toLRSHom.toShHom (directImageStructureSheaf f)
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.isFlatOver_directImageStructureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/DirectImageStructureSheafFlat.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/DirectImageStructureSheafFlat.lean#L107). The attribute's comment: “clause (a): flatness of `f_* 𝒪_X` over the base”.

> Let `X ⟶ Y ⟶ S` be a commutative triangle of schemes with `X ⟶ S` flat, let `f : X ⟶ Y` be
> proper with `dim(X_y) ≤ 1` for every `y ∈ Y`, and suppose `R¹ f_* 𝒪_X = 0`. Then `f_* 𝒪_X` is
> flat over `S`.

```lean
theorem isFlatOver_directImageStructureSheaf (hcoh : CohomologyVanishesAboveOne.{u})
    {X Y S : Scheme.{u}} (f : X ⟶ Y) (q : Y ⟶ S) [Flat (f ≫ q)] [IsProper f]
    (hdim : ∀ y : Y, topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞))
    (hR : IsZero (firstDirectImageStructureSheaf f)) :
    IsFlatOver q.toLRSHom.toShHom (directImageStructureSheaf f)
```

## Tag 0E7L, a lemma

[Tag 0E7L](https://stacks.math.columbia.edu/tag/0E7L) in the Stacks Project.

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.exists_isOpen_isIso_unitToPushforwardUnit_of_specialFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/StructureSheafIsoNearSpecialFibreReduction.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/StructureSheafIsoNearSpecialFibreReduction.lean#L442).

> **[Stacks, Tag 0E7L].** Let `X --f--> Y --q--> S` be a commutative triangle of schemes and
> `s ∈ S`. Assume
> 1. `X ⟶ S` is locally of finite presentation and flat at the points of `X_s`,
> 2. `Y ⟶ S` is locally of finite presentation,
> 3. `f` is proper,
> 4. the fibres of `f_s : X_s ⟶ Y_s` have dimension `≤ 1` and `R¹f_{s,*}𝒪_{X_s} = 0`,
> 5. `𝒪_{Y_s} ⟶ f_{s,*}𝒪_{X_s}` is an isomorphism.
>
> Then there is an open `Y_s ⊂ V ⊂ Y` such that (a) `V` is flat over `S`, (b) `f⁻¹(V)` is flat
> over `S`, (c) `dim(X_y) ≤ 1` for `y ∈ V`, (d) `R¹f_*𝒪_X|_V = 0`, (e) `𝒪_V ⟶ f_*𝒪_X|_V` is an
> isomorphism, and (a) – (e) remain true after base change of `f⁻¹(V) ⟶ V` by any `S' ⟶ S`
> (for the base change `X' ⟶ V'` of `f⁻¹(V) ⟶ V`, the open of (a) – (e) being all of `V'`).
>
> In the hypotheses, `f_s` is the base change of `f` along `Y_s ⟶ Y` for (4) on `R¹` and for (5),
> and `(f ≫ q).fiber s ⟶ q.fiber s` for the dimension bound of (4); these are the same morphism
> up to the canonical isomorphism `X ×_Y Y_s ≅ X_s`.
>
> The proof is the source's. Near each `y ∈ Y_s` one restricts to affine opens of `Y` and `S`
> over which `X` is flat; the situation is the base change of a Noetherian model
> (`exists_noetherianModel`, [Stacks, Tags 01ZM, 081F, 04AI]), the special-fibre hypotheses
> descend to the image point of the model base along a faithfully flat field extension, and over
> the Noetherian model the stalk maps of `𝒪_Y ⟶ f_*𝒪_X` are bijective near the special fibre
> (surjective by coherence of the cokernel, [Stacks, Tag 02O5], and Nakayama; injective by the
> local flatness criterion, [Stacks, Tag 00ME]); this is carried back by [Stacks, Tag 0E7K] (b).
> Conclusions (a) and (e) and the persistence then follow from [Stacks, Tag 0E7K] on `V`
> (`conclusions_of_isOpen`).

```lean
theorem exists_isOpen_isIso_unitToPushforwardUnit_of_specialFibre (f : X ⟶ Y) (q : Y ⟶ S) (s : S)
    [LocallyOfFinitePresentation (f ≫ q)]
    [LocallyOfFinitePresentation q] [IsProper f]
    (hflat : ∀ x : X, (f ≫ q) x = s → IsFlatAt (f ≫ q).toLRSHom.toShHom x)
    (hdim : ∀ y : q.fiber s, topologicalKrullDim ((Stacks.Flatness.fiberHom f q s).fiber y) ≤
      ((1 : ℕ) : WithBot ℕ∞))
    (hR : IsZero (firstDirectImageStructureSheaf (pullback.snd f (q.fiberι s))))
    (hiso : IsIso (Scheme.Modules.unitToPushforwardUnit (pullback.snd f (q.fiberι s)))) :
    ∃ V : Y.Opens, (∀ y : Y, q y = s → y ∈ V) ∧
      Flat (V.ι ≫ q) ∧
      Flat ((f ⁻¹ᵁ V).ι ≫ (f ≫ q)) ∧
      (∀ y : Y, y ∈ V → topologicalKrullDim (f.fiber y) ≤ ((1 : ℕ) : WithBot ℕ∞)) ∧
      IsZero ((Scheme.Modules.restrictFunctor V.ι).obj (firstDirectImageStructureSheaf f)) ∧
      IsIso ((Scheme.Modules.restrictFunctor V.ι).map (Scheme.Modules.unitToPushforwardUnit f)) ∧
      ∀ ⦃S' : Scheme.{u}⦄ (h : S' ⟶ S),
        Flat (pullback.snd (V.ι ≫ q) h) ∧
        Flat (pullback.snd (f ∣_ V) (pullback.fst (V.ι ≫ q) h) ≫ pullback.snd (V.ι ≫ q) h) ∧
        (∀ y' : (pullback (V.ι ≫ q) h : Scheme.{u}), topologicalKrullDim
          ((pullback.snd (f ∣_ V) (pullback.fst (V.ι ≫ q) h)).fiber y') ≤
            ((1 : ℕ) : WithBot ℕ∞)) ∧
        IsZero (firstDirectImageStructureSheaf
          (pullback.snd (f ∣_ V) (pullback.fst (V.ι ≫ q) h))) ∧
        IsIso (Scheme.Modules.unitToPushforwardUnit
          (pullback.snd (f ∣_ V) (pullback.fst (V.ι ≫ q) h)))
```

## Tag 0E24, a lemma

[Tag 0E24](https://stacks.math.columbia.edu/tag/0E24) in the Stacks Project.

**`Stacks.PicardFibreTrivial.pullback_injective_and_exists_pullback_iso_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardFibreTrivial/Basic.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardFibreTrivial/Basic.lean#L203).

> **Stacks Project, Tag 0E24.** Let `f : X ⟶ Y` be a proper morphism onto a Noetherian scheme
> such that `f_* 𝒪_X = 𝒪_Y`, such that the fibres of `f` have dimension at most one, and such
> that `H¹(X_y, 𝒪_{X_y}) = 0` for every `y ∈ Y`. Then `f^* : Pic(Y) ⟶ Pic(X)` is a bijection
> onto the subgroup of classes of invertible `𝒪_X`-modules `ℒ` with `ℒ|_{X_y} ≅ 𝒪_{X_y}` for all
> `y ∈ Y`: on isomorphism classes of invertible modules `f^*` is injective, and an invertible `ℒ`
> is isomorphic to a pullback `f^* 𝒩` of an invertible `𝒪_Y`-module exactly when it is trivial on
> every fibre.
>
> The source also asks for `X` to be Noetherian; that follows from the other hypotheses (`f` is
> proper over a Noetherian base) and is not needed.

```lean
theorem pullback_injective_and_exists_pullback_iso_iff (f : X ⟶ Y) [IsProper f] [IsNoetherian Y]
    (hO : IsIso (SheafOfModules.unitToPushforwardObjUnit f.toRingCatSheafHom))
    (hdim : ∀ y : Y, topologicalKrullDim (f.fiber y) ≤ 1)
    (hH1 : ∀ y : Y, IsZero (cohomologyOverField (Y.residueField y) (f.fiberToSpecResidueField y)
      (SheafOfModules.unit (f.fiber y).ringCatSheaf) 1)) :
    (∀ M N : Y.Modules,
      Stacks.SheafOfModules.IsInvertible Y.presheaf
        (structureSheafRing Y.toRingedSpace).property M →
      Stacks.SheafOfModules.IsInvertible Y.presheaf
        (structureSheafRing Y.toRingedSpace).property N →
      Nonempty ((Scheme.Modules.pullback f).obj M ≅ (Scheme.Modules.pullback f).obj N) →
      Nonempty (M ≅ N)) ∧
    ∀ L : X.Modules,
      Stacks.SheafOfModules.IsInvertible X.presheaf
        (structureSheafRing X.toRingedSpace).property L →
      ((∃ M : Y.Modules,
          Stacks.SheafOfModules.IsInvertible Y.presheaf
            (structureSheafRing Y.toRingedSpace).property M ∧
          Nonempty ((Scheme.Modules.pullback f).obj M ≅ L)) ↔
        ∀ y : Y, Nonempty ((Scheme.Modules.pullback (f.fiberι y)).obj L ≅
          SheafOfModules.unit (f.fiber y).ringCatSheaf))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.72, Tag 0E7E](https://stacks.math.columbia.edu/tag/0E7E)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
