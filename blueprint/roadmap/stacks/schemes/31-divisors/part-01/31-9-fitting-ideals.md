---
declaration: section
origin: cited
lean: AlgebraicGeometry.fittingIdeal_comap, AlgebraicGeometry.fittingIdeal_isFiniteType, AlgebraicGeometry.fittingIdeal_zero_le_annihilatorIdeal, AlgebraicGeometry.fittingIdeal_zero_support_eq_supp, AlgebraicGeometry.exists_module_on_fittingSubscheme, AlgebraicGeometry.supp_eq_annihilatorIdeal_support, AlgebraicGeometry.isGeneratedByNear_iff_fittingIdeal_stalk_eq_top, AlgebraicGeometry.finiteLocallyFreeOfRank_tfae_fittingIdeal
statement: formalized
proof: formalized
---

# 31.9 Fitting ideals

Section 31.9 of the Stacks Project, [Tag 0C3C](https://stacks.math.columbia.edu/tag/0C3C). 7 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C3D, a lemma

[Tag 0C3D](https://stacks.math.columbia.edu/tag/0C3D) in the Stacks Project.

**`AlgebraicGeometry.fittingIdeal_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/FittingIdeals.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/FittingIdeals.lean#L199).

> **Stacks Project, Tag 0C3D.** Fitting ideal sheaves of finite type
> quasi-coherent modules commute with arbitrary base change.

```lean
theorem fittingIdeal_comap {X Y : Scheme.{u}} (f : X ⟶ Y)
    (F : Y.Modules) [F.IsFiniteType] [F.IsQuasicoherent] (k : ℤ) :
    (fittingIdeal F k).comap f =
      fittingIdeal ((Scheme.Modules.pullback f).obj F) k
```

## Tag 0C3E, a lemma

[Tag 0C3E](https://stacks.math.columbia.edu/tag/0C3E) in the Stacks Project.

**`AlgebraicGeometry.fittingIdeal_isFiniteType`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/FittingIdeals.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/FittingIdeals.lean#L257).

> The Fitting ideals of a finitely presented sheaf of modules are
> quasi-coherent ideals of finite type.

```lean
lemma fittingIdeal_isFiniteType {X : Scheme.{u}} (F : X.Modules)
    [F.IsFinitePresentation] (r : ℕ) :
    Scheme.IdealSheafData.IsFiniteType (fittingIdealOfNat F r)
```

## Tag 0CYX, a lemma

[Tag 0CYX](https://stacks.math.columbia.edu/tag/0CYX) in the Stacks Project.

**`AlgebraicGeometry.fittingIdeal_zero_le_annihilatorIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/FittingSupport.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/FittingSupport.lean#L70). The attribute's comment: “scheme_theoretic_inclusion”.

> **Stacks Project, Tag 0CYX, part (1).** The scheme-theoretic support of a finite type
> quasi-coherent module is a closed subscheme of the one cut out by its zeroth Fitting ideal:
> over every affine open the zeroth Fitting ideal is contained in the annihilator.

```lean
theorem fittingIdeal_zero_le_annihilatorIdeal : fittingIdeal F 0 ≤ annihilatorIdeal' F
```

**`AlgebraicGeometry.fittingIdeal_zero_support_eq_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/FittingSupport.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/FittingSupport.lean#L105). The attribute's comment: “underlying_support”. References: SGA 7 VI (5.1), “more general”.

> **Stacks Project, Tag 0CYX, part (2).** The closed subscheme cut out by the zeroth Fitting
> ideal of a finite type quasi-coherent module has the support of the module as its underlying
> closed set, so it agrees there with the scheme-theoretic support.

```lean
theorem fittingIdeal_zero_support_eq_supp :
    (fittingIdeal F 0).support = SheafOfModules.supp F
```

**`AlgebraicGeometry.exists_module_on_fittingSubscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/FittingSupport.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/FittingSupport.lean#L150). The attribute's comment: “module_on_fitting_subscheme”.

> **Stacks Project, Tag 0CYX, part (3).** A finite type quasi-coherent module is the direct
> image of a finite type quasi-coherent module on the closed subscheme cut out by its zeroth
> Fitting ideal, namely of its own pullback there.

```lean
theorem exists_module_on_fittingSubscheme :
    ∃ (G : (fittingIdeal F 0).subscheme.Modules)
      (_ : (Scheme.Modules.pushforward (fittingIdeal F 0).subschemeι).obj G ≅ F),
      G.IsFiniteType ∧ G.IsQuasicoherent
```

Declarations registered for the tag:

- [`AlgebraicGeometry.supp_eq_annihilatorIdeal_support`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/AnnihilatorSupport.lean#L136), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/FittingSupport.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/FittingSupport.lean#L99) (StacksFrontier): “underlying_support”.

## Tag 0C3F, a lemma

[Tag 0C3F](https://stacks.math.columbia.edu/tag/0C3F) in the Stacks Project.

**`AlgebraicGeometry.isGeneratedByNear_iff_fittingIdeal_stalk_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/FittingIdeals/Basic.lean, line 526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/FittingIdeals/Basic.lean#L526).

> A finite type quasicoherent module is generated by `r` sections near a
> point if and only if the stalk of its `r`th Fitting ideal is the unit ideal.

```lean
public theorem isGeneratedByNear_iff_fittingIdeal_stalk_eq_top
    {X : Scheme.{u}} (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent]
    (r : ℕ) (s : X) :
    IsGeneratedByNear F r s ↔ IdealSheafData.stalk (fittingIdeal F r) s = ⊤
```

## Tag 0C3G, a lemma

[Tag 0C3G](https://stacks.math.columbia.edu/tag/0C3G) in the Stacks Project.

**`AlgebraicGeometry.finiteLocallyFreeOfRank_tfae_fittingIdeal`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FittingRank/Basic.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FittingRank/Basic.lean#L589).

> **Stacks Project, Tag 0C3G.** A finite type quasicoherent module is finite
> locally free of rank `r` if and only if its Fitting ideals vanish below `r`
> and are the unit ideal from `r` onward.

```lean
public lemma finiteLocallyFreeOfRank_tfae_fittingIdeal
    {X : Scheme.{u}} (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent]
    (r : ℕ) :
    List.TFAE [
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank F r,
      (r = 0 ∨ AlgebraicGeometry.fittingIdeal F (r - 1) = ⊥) ∧
        AlgebraicGeometry.fittingIdeal F r = ⊤,
      (∀ k < r, AlgebraicGeometry.fittingIdeal F k = ⊥) ∧
        (∀ k, r ≤ k → AlgebraicGeometry.fittingIdeal F k = ⊤)]
```

## Tag 05P8, a lemma

[Tag 05P8](https://stacks.math.columbia.edu/tag/05P8) in the Stacks Project.

**`AlgebraicGeometry.fittingClosedSubscheme_antitone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/Exhaustion.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/Exhaustion.lean#L65). The attribute's comment: “the Fitting ideals cut out a descending chain of closed subschemes”.

> The closed subschemes cut out by the Fitting ideals of a quasi-coherent module of finite type
> decrease with the index: for `i ≤ j` the `j`-th one admits a morphism over the base scheme to the
> `i`-th one, namely the inclusion of closed subschemes coming from the inclusion of Fitting
> ideals.

```lean
theorem fittingClosedSubscheme_antitone {S : Scheme.{u}} (F : S.Modules) [F.IsFiniteType]
    [F.IsQuasicoherent] {i j : ℕ} (hij : i ≤ j) :
    Nonempty (fittingClosedSubscheme F (j : ℤ) ⟶ fittingClosedSubscheme F (i : ℤ))
```

**`AlgebraicGeometry.fittingClosedSubscheme_iInter_range_eq_empty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/Exhaustion.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/Exhaustion.lean#L76). The attribute's comment: “property (1): the Fitting closed subschemes have empty intersection”.

> The Fitting closed subschemes of a quasi-coherent module of finite type exhaust the base
> scheme: the images in `S` of the subschemes indexed by the natural numbers meet in the empty set.
> Indeed, if `x` lies in an affine open `U` whose module of sections is generated by `n` elements,
> then the `n`-th Fitting ideal is the unit ideal on `U`, so `x` avoids the `n`-th member.

```lean
theorem fittingClosedSubscheme_iInter_range_eq_empty {S : Scheme.{u}} (F : S.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent] :
    (⋂ i : ℕ, Set.range (fittingClosedSubscheme F (i : ℤ)).hom.base) = ∅
```

**`AlgebraicGeometry.fittingClosedSubscheme_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/FinitePresentation.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/FinitePresentation.lean#L85). The attribute's comment: “finite presentation of the morphism Z_r to S”.

> **Stacks Project, Tag 05P8.** The closed subscheme of `S` cut out by the `r`-th Fitting ideal
> of a finitely presented sheaf of modules `F` is of finite presentation over `S`.

```lean
public theorem fittingClosedSubscheme_finitePresentation {S : Scheme.{u}} (F : S.Modules)
    [F.IsFinitePresentation] (r : ℕ) :
    FinitePresentation
      (@fittingClosedSubscheme S F (SheafOfModules.instIsFiniteTypeOfIsFinitePresentation F)
        (SheafOfModules.instIsQuasicoherentOfIsFinitePresentation F) (r : ℤ)).hom
```

**`AlgebraicGeometry.fittingGeneratorOpen_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/FinitePresentation.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/FinitePresentation.lean#L100). The attribute's comment: “finite presentation of the morphism S minus Z_r to S”.

> **Stacks Project, Tag 05P8.** The open complement in `S` of the closed subscheme cut out by
> the `r`-th Fitting ideal of a finitely presented sheaf of modules `F` — the locus where `F` is
> generated by `r` sections — is of finite presentation over `S`.

```lean
public theorem fittingGeneratorOpen_finitePresentation {S : Scheme.{u}} (F : S.Modules)
    [F.IsFinitePresentation] (r : ℕ) :
    FinitePresentation
      (@fittingGeneratorOpen S F (SheafOfModules.instIsFiniteTypeOfIsFinitePresentation F)
        (SheafOfModules.instIsQuasicoherentOfIsFinitePresentation F) r).ι
```

**`AlgebraicGeometry.locallyGenerated_iff_factorsThrough_fittingGeneratorOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/GeneratorOpen.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/GeneratorOpen.lean#L80). The attribute's comment: “property (2): representability of the functor of generation by <= r sections”.

> **Stacks Project, Tag 05P8.** The pullback of a finite type quasi-coherent module `F` along
> `f : T ⟶ S` is generated by `r` sections near every point of `T` if and only if `f` factors
> uniquely through the open complement of the `r`-th Fitting closed subscheme of `F`.

```lean
public theorem locallyGenerated_iff_factorsThrough_fittingGeneratorOpen
    {S T : Scheme.{u}} (F : S.Modules) [F.IsFiniteType] [F.IsQuasicoherent]
    (r : ℕ) (f : T ⟶ S) :
    (∀ t : T, IsGeneratedByNear ((Scheme.Modules.pullback f).obj F) r t) ↔
      ∃! g : T ⟶ (fittingGeneratorOpen F r).toScheme,
        g ≫ (fittingGeneratorOpen F r).ι = f
```

**`AlgebraicGeometry.isImmersion_fittingRankStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/RankStratum.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/RankStratum.lean#L78). The attribute's comment: “property (3): the rank r stratum is a locally closed subscheme”.

> The structural morphism of the rank `r` Fitting stratum is a locally closed immersion: it
> is the inclusion of an open subscheme followed by a closed immersion.

```lean
public theorem isImmersion_fittingRankStratum {S : Scheme.{u}} (F : S.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent] (r : ℕ) :
    IsImmersion (fittingRankStratum F r).hom
```

**`AlgebraicGeometry.rankRFunctor_representableBy_fittingRankStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/RankStratum.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/RankStratum.lean#L199). The attribute's comment: “property (3): representability of the functor of local freeness of rank r”.

> **Stacks Project, Tag 05P8.** The rank `r` functor of a finite type quasi-coherent module
> `F` on `S` is represented by the rank `r` Fitting stratum of `F`, a locally closed subscheme of
> `S`.

```lean
public theorem rankRFunctor_representableBy_fittingRankStratum {S : Scheme.{u}}
    (F : S.Modules) [F.IsFiniteType] [F.IsQuasicoherent] (r : ℕ) :
    Nonempty ((rankRFunctor S F r).RepresentableBy (fittingRankStratum F r))
```

**`AlgebraicGeometry.finitePresentation_fittingRankStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/RankStratumFinitePresentation.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/RankStratumFinitePresentation.lean#L102). The attribute's comment: “finite presentation of the morphism Z_(r-1) minus Z_r to S”.

> **Stacks Project, Tag 05P8.** The structural morphism of the rank `r` Fitting stratum of a
> finitely presented sheaf of modules `F` on `S` — the locally closed subscheme of `S` over which
> `F` pulls back to a module finite locally free of rank `r` — is of finite presentation.

```lean
public theorem finitePresentation_fittingRankStratum {S : Scheme.{u}} (F : S.Modules)
    [F.IsFinitePresentation] (r : ℕ) :
    FinitePresentation
      (@fittingRankStratum S F (SheafOfModules.instIsFiniteTypeOfIsFinitePresentation F)
        (SheafOfModules.instIsQuasicoherentOfIsFinitePresentation F) r).hom
```

**`Stacks.Fitting.idealSheaf_monotone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FittingIdealSheaf.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FittingIdealSheaf.lean#L157). The attribute's comment: “decreasing closed subschemes”.

> **Stacks Project, Tag 05P8.** The Fitting ideal sheaves increase, so the closed subschemes
> they cut out form a decreasing chain.

```lean
theorem idealSheaf_monotone {X : Scheme.{u}} (F : X.Modules) : Monotone (idealSheaf F)
```

## Tag 05P9, a lemma

[Tag 05P9](https://stacks.math.columbia.edu/tag/05P9) in the Stacks Project.

**`AlgebraicGeometry.rankStratum_isFiniteLocallyFreeOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/Flattening.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/Flattening.lean#L391). The attribute's comment: “rank on each stratum”.

> **Stacks Project, Tag 05P9.** The module restricts to a finite locally free module of rank
> `r` on the `r`-th Fitting rank stratum.

```lean
public theorem rankStratum_isFiniteLocallyFreeOfRank (r : ℕ) :
    SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      ((Scheme.Modules.pullback
        (@fittingRankStratum S F (SheafOfModules.instIsFiniteTypeOfIsFinitePresentation F)
          (SheafOfModules.instIsQuasicoherentOfIsFinitePresentation F) r).hom).obj F) r
```

**`AlgebraicGeometry.flat_iff_existsUnique_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/Flattening.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/Flattening.lean#L404). The attribute's comment: “representability”.

> **Stacks Project, Tag 05P9.** A pullback of a finitely presented module is flat exactly when
> the morphism to the base factors, necessarily uniquely, through the flattening stratification —
> the disjoint union of the Fitting rank strata.

```lean
public theorem flat_iff_existsUnique_lift {T : Scheme.{u}} (g : T ⟶ S) :
    SheafOfModules.IsFlat (C := TopologicalSpace.Opens T.toTopCat)
        (J := Opens.grothendieckTopology T.toTopCat) (O := T.sheaf)
        ((Scheme.Modules.pullback g).obj F) ↔
      ∃! h : T ⟶ @flatnessStratification S F
          (SheafOfModules.instIsFiniteTypeOfIsFinitePresentation F)
          (SheafOfModules.instIsQuasicoherentOfIsFinitePresentation F),
        h ≫ @flatnessStratificationHom S F
          (SheafOfModules.instIsFiniteTypeOfIsFinitePresentation F)
          (SheafOfModules.instIsQuasicoherentOfIsFinitePresentation F) = g
```

**`AlgebraicGeometry.flatnessStratification_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/Flattening.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/Flattening.lean#L428). The attribute's comment: “finite presentation of the disjoint union”.

> **Stacks Project, Tag 05P9.** The structural morphism of the flattening stratification is of
> finite presentation: it is locally of finite presentation because each stratum is, quasi-compact
> because the Fitting generator opens exhaust the base, and quasi-separated because it is
> injective.

```lean
public theorem flatnessStratification_finitePresentation :
    FinitePresentation (@flatnessStratificationHom S F
      (SheafOfModules.instIsFiniteTypeOfIsFinitePresentation F)
      (SheafOfModules.instIsQuasicoherentOfIsFinitePresentation F))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.finitePresentation_fittingRankStratum`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/RankStratumFinitePresentation.lean#L102), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/Flattening.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FittingStratification/Flattening.lean#L453) (StacksFrontier): “finite presentation of each stratum”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.9, Tag 0C3C](https://stacks.math.columbia.edu/tag/0C3C)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
