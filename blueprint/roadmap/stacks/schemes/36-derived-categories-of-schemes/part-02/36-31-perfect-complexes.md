---
declaration: section
origin: cited
lean: AlgebraicGeometry.DerivedFibreBetti.isPseudoCoherent_derivedPullback, AlgebraicGeometry.DerivedFibreBetti.derivedFiberBetti_derivedPullback, AlgebraicGeometry.DerivedFibreBetti.isLocallyConstructible_derivedFiberBetti_preimage, AlgebraicGeometry.DerivedFibreBetti.upperSemicontinuous_derivedFiberBetti, AlgebraicGeometry.DerivedFibreBetti.isLocallyConstant_chiDerivedFibre, AlgebraicGeometry.Scheme.Modules.nonempty_iso_singleFunctor_restrict_iff_le, AlgebraicGeometry.Scheme.Modules.isZero_homology_singleDegreeRankOpen, AlgebraicGeometry.Scheme.Modules.nonempty_iso_singleFunctor_restrict_singleDegreeRankOpen
statement: formalized
proof: formalized
---

# 36.31 Perfect complexes

Section 36.31 of the Stacks Project, [Tag 0BDH](https://stacks.math.columbia.edu/tag/0BDH). 4 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BDI, a lemma

[Tag 0BDI](https://stacks.math.columbia.edu/tag/0BDI) in the Stacks Project.

**`AlgebraicGeometry.DerivedFibreBetti.isPseudoCoherent_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/DerivedFibreBettiBaseChange.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/DerivedFibreBettiBaseChange.lean#L229). The attribute's comment: “base_change”.

> **Tag 0BDI, base change: the derived pullback of a pseudo-coherent object is
> pseudo-coherent.**  This is what makes the derived-fibre Betti function of `Lf^* E` available
> from the pseudo-coherence of `E` alone.
>
> A single complex has to work for every `m`, so the representative is chosen once —
> `DerivedCategory.Q.objPreimage` — and Tag 09U7 is applied in each degree, its `m`-specific
> representative being transported onto that one choice by Tag 08CC part (2).

```lean
public theorem isPseudoCoherent_derivedPullback
    (E : DerivedCategory X.Modules)
    (hE : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E) :
    RingedSpace.IsPseudoCoherent (X := Y.toRingedSpace)
      ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f.toLRSHom.toShHom).obj E)
```

**`AlgebraicGeometry.DerivedFibreBetti.derivedFiberBetti_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/DerivedFibreBettiBaseChange.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/DerivedFibreBettiBaseChange.lean#L256). The attribute's comment: “base_change”.

> **Tag 0BDI, base change: the derived-fibre Betti function commutes with base change.**  For a
> morphism of schemes `f : Y ⟶ X` the `i`-th derived-fibre Betti function of `Lf^* E` is the
> pullback along `f` of the `i`-th derived-fibre Betti function of `E`.
>
> The pseudo-coherence of `Lf^* E` that the left-hand side needs is supplied by
> `isPseudoCoherent_derivedPullback`, so `E`'s own pseudo-coherence is the only hypothesis.  The
> function does not use its pseudo-coherence argument, so nothing is lost by fixing it: the
> underlying dimension equality is `finrank_residueFibre_eq`, which has no pseudo-coherence
> hypothesis at all.

```lean
public theorem derivedFiberBetti_derivedPullback
    (E : DerivedCategory X.Modules)
    (hE : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E)
    (i : ℤ) :
    derivedFiberBetti Y ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      f.toLRSHom.toShHom).obj E)
        (isPseudoCoherent_derivedPullback f E hE) i =
      derivedFiberBetti X E hE i ∘ f.base
```

**`AlgebraicGeometry.DerivedFibreBetti.isLocallyConstructible_derivedFiberBetti_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/DerivedFibreBettiConstructible.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/DerivedFibreBettiConstructible.lean#L104). The attribute's comment: “part (3): for E a pseudo-coherent object of D(O_X) on a scheme X, the level sets of the functions beta_i are locally constructible in X. beta_i is AlgebraicGeometry.DerivedFibreBetti.derivedFiberBetti, the dimension over the residue field of the degree-i cohomology of the derived fibre read through global sections on Spec kappa(x), the level set at n is the preimage of the singleton n, and pseudo-coherence of E is the only hypothesis. The affine case is proved, not assumed: it is StacksDraft.Perfect.isConstructible_fibreBetti_preimage, which runs the source's argument through the rank loci of a bounded-above finite free model -- over a field the ideal of r-by-r minors of a matrix is the unit ideal exactly when r is at most its rank (StacksDraft.MinorRank.minorIdeal_eq_top_iff_le_rank), so the locus where the rank at p is at least r is the complement of the zero locus of a finitely generated ideal and hence retrocompact, which is what semi-continuity does not give”.

> **[Stacks, Tag 0BDI], part (3): the level sets of the derived-fibre Betti functions are
> locally constructible.**  Let `X` be a scheme and let `E` be a pseudo-coherent object of
> `D(𝒪_X)`.  For every `i` and every `n` the set of points `x` with
> `dim_{κ(x)} H^i(Li_x^* E) = n` is locally constructible in `X`.
>
> By [Stacks, Tag 054C] it is enough to check that the restriction to each affine open `U` is
> constructible.  The open immersion `hU.fromSpec : Spec Γ(X, U) ⟶ X` is a homeomorphism onto the
> subspace `U`, so that restriction is constructible exactly when its preimage along `fromSpec` is;
> and that preimage is a level set of the derived-fibre Betti function of the derived pullback of
> `E`, by part (1) of the tag, to which the affine case applies.

```lean
public theorem isLocallyConstructible_derivedFiberBetti_preimage (X : Scheme.{u})
    (E : DerivedCategory X.Modules)
    (hE : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E) (i : ℤ) (n : ℕ) :
    IsLocallyConstructible (derivedFiberBetti X E hE i ⁻¹' {n})
```

**`AlgebraicGeometry.DerivedFibreBetti.upperSemicontinuous_derivedFiberBetti`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/DerivedFibreBettiSemicontinuity.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/DerivedFibreBettiSemicontinuity.lean#L84). The attribute's comment: “part (2): for E a pseudo-coherent object of D(O_X) on a scheme X, the function beta_i sending x to dim_{kappa(x)} H^i(Li_x^* E) is upper semi-continuous. beta_i is AlgebraicGeometry.DerivedFibreBetti.derivedFiberBetti, the dimension over the residue field of the degree-i cohomology of the derived fibre read through global sections on Spec kappa(x), and pseudo-coherence of E is the only hypothesis”.

> **[Stacks, Tag 0BDI], part (2): the derived-fibre Betti functions are upper
> semi-continuous.**  Let `X` be a scheme and let `E` be a pseudo-coherent object of `D(𝒪_X)`.  For
> every `i` the function `x ↦ dim_{κ(x)} H^i(Li_x^* E)` is upper semi-continuous on `X`.
>
> Every point lies in an affine open `U`, and `U` is the image of the open immersion
> `hU.fromSpec : Spec Γ(X, U) ⟶ X`; the derived pullback of `E` along it is pseudo-coherent, so the
> affine case applies there, and upper semi-continuity is local on the source.

```lean
public theorem upperSemicontinuous_derivedFiberBetti (X : Scheme.{u})
    (E : DerivedCategory X.Modules)
    (hE : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E) (i : ℤ) :
    UpperSemicontinuous (derivedFiberBetti X E hE i)
```

## Tag 0BDJ, a lemma

[Tag 0BDJ](https://stacks.math.columbia.edu/tag/0BDJ) in the Stacks Project.

**`AlgebraicGeometry.DerivedFibreBetti.isLocallyConstant_chiDerivedFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/DerivedFibreEulerCharacteristic.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/DerivedFibreEulerCharacteristic.lean#L348). References: EGA III (7.9.3), “more general”; SGA 6 III (5.4.1), “a) rank, scheme case”; SGA 6 III (5.5), “(i), scheme case”.

> **Stacks 0BDJ.** The derived-fibre Euler characteristic of a perfect object of `D(𝒪_X)` on a
> scheme is locally constant.
>
> Near any point, Tag 0BCJ represents `E` by a bounded complex of finite free modules on an open
> `V`; base change along the open immersion `V ⟶ X` (Tag 0BDI) identifies the Euler characteristic
> on `V` with the restriction of the one on `X`, and on `V` it is the constant
> `∑ (-1)^i rank(P^i)`.

```lean
public theorem isLocallyConstant_chiDerivedFibre (X : Scheme.{u})
    (E : DerivedCategory X.Modules)
    (hE : RingedSpace.IsPerfect.{u, u + 1} (X := X.toRingedSpace) E) :
    IsLocallyConstant (chiDerivedFibre X E (isPseudoCoherent_of_isPerfect E hE))
```

## Tag 0BDK, a lemma

[Tag 0BDK](https://stacks.math.columbia.edu/tag/0BDK) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.nonempty_iso_singleFunctor_restrict_iff_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SingleDegreeRankOpen.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SingleDegreeRankOpen.lean#L305). The attribute's comment: “the open description”.

> **The open subscheme of [stacks 0BDK] is characterised by the first description.** An open of
> `X` is contained in `singleDegreeRankOpen` exactly when the restriction of `E` to it is isomorphic
> to a finite locally free module of rank `r` placed in degree `i`; so `singleDegreeRankOpen` is the
> largest open subscheme on which `E` has that shape.

```lean
theorem nonempty_iso_singleFunctor_restrict_iff_le (V : X.Opens) :
    (∃ M : V.toScheme.Modules,
        AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} M r ∧
          Nonempty ((restrictFunctor V.ι).mapDerivedCategory.obj E ≅
            (DerivedCategory.singleFunctor V.toScheme.Modules i).obj M)) ↔
      V ≤ singleDegreeRankOpen E i r
```

**`AlgebraicGeometry.Scheme.Modules.isZero_homology_singleDegreeRankOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SingleDegreeRankOpen.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SingleDegreeRankOpen.lean#L316). The attribute's comment: “the open description”.

> **The cohomology of `E` vanishes outside degree `i` on the open subscheme of [stacks 0BDK].**

```lean
theorem isZero_homology_singleDegreeRankOpen (j : ℤ) (hj : j ≠ i) :
    IsZero ((DerivedCategory.homologyFunctor
        (singleDegreeRankOpen E i r).toScheme.Modules j).obj
      ((restrictFunctor (singleDegreeRankOpen E i r).ι).mapDerivedCategory.obj E))
```

**`AlgebraicGeometry.Scheme.Modules.nonempty_iso_singleFunctor_restrict_singleDegreeRankOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SingleDegreeRankOpen.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SingleDegreeRankOpen.lean#L327). The attribute's comment: “the open description”.

> **On the open subscheme of [stacks 0BDK] the derived module `E` is its own degree-`i`
> cohomology sheaf placed in degree `i`.** This is the first half of description (1) of the tag.

```lean
theorem nonempty_iso_singleFunctor_restrict_singleDegreeRankOpen :
    Nonempty ((restrictFunctor (singleDegreeRankOpen E i r).ι).mapDerivedCategory.obj E ≅
      (DerivedCategory.singleFunctor (singleDegreeRankOpen E i r).toScheme.Modules i).obj
        ((DerivedCategory.homologyFunctor
            (singleDegreeRankOpen E i r).toScheme.Modules i).obj
          ((restrictFunctor (singleDegreeRankOpen E i r).ι).mapDerivedCategory.obj E)))
```

**`AlgebraicGeometry.Scheme.Modules.isFiniteLocallyFreeOfRank_homology_singleDegreeRankOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SingleDegreeRankOpen.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SingleDegreeRankOpen.lean#L339). The attribute's comment: “the open description”.

> **On the open subscheme of [stacks 0BDK] the degree-`i` cohomology sheaf of `E` is finite
> locally free of rank `r`.** This is the second half of description (1) of the tag.

```lean
theorem isFiniteLocallyFreeOfRank_homology_singleDegreeRankOpen :
    AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      ((DerivedCategory.homologyFunctor
          (singleDegreeRankOpen E i r).toScheme.Modules i).obj
        ((restrictFunctor (singleDegreeRankOpen E i r).ι).mapDerivedCategory.obj E)) r
```

**`AlgebraicGeometry.Scheme.Modules.factorsThrough_singleDegreeRankOpen_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SingleDegreeRankOpen.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SingleDegreeRankOpen.lean#L354). The attribute's comment: “the universal property for open immersions, restriction for the derived pullback”.

> **The universal property of the open subscheme of [stacks 0BDK], for open immersions.** An open
> immersion `f : Y ⟶ X` factors through `singleDegreeRankOpen` exactly when the restriction of `E`
> along `f` is isomorphic to a finite locally free module of rank `r` placed in degree `i`.
>
> This is description (2) of the tag for an open immersion, with the exact restriction functor along
> `f` in place of the derived pullback; the tag states it for an arbitrary morphism and the derived
> pullback.

```lean
theorem factorsThrough_singleDegreeRankOpen_iff {Y : Scheme.{u}} (f : Y ⟶ X)
    [IsOpenImmersion f] :
    (∃ g : Y ⟶ (singleDegreeRankOpen E i r).toScheme,
        g ≫ (singleDegreeRankOpen E i r).ι = f) ↔
      ∃ M : Y.Modules,
        AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} M r ∧
          Nonempty ((restrictFunctor f).mapDerivedCategory.obj E ≅
            (DerivedCategory.singleFunctor Y.Modules i).obj M)
```

**`AlgebraicGeometry.Scheme.Modules.existsUnique_opens_singleDegreeRank_int`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SingleDegreeRankOpenInt.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SingleDegreeRankOpenInt.lean#L111). The attribute's comment: “THE WHOLE TAG, at the source's INTEGER rank: the existence of an open subscheme satisfying description (1), both of its clauses, and description (2) in both directions for an ARBITRARY morphism of schemes and the derived pullback Lf^*E, together with the UNIQUENESS that makes the two descriptions a characterisation. The only premise is the source's own, that E be perfect. The rank clause is read at each point, as the source states it; for a non-negative rank the witness is AlgebraicGeometry.Scheme.Modules.singleDegreeRankOpen and the statement is AlgebraicGeometry.Scheme.Modules.existsUnique_opens_singleDegreeRank, and for a negative rank the witness is the empty open subscheme”.

> **[Stacks, Tag 0BDK].** Let `X` be a scheme, let `E ∈ D(𝒪_X)` be perfect and let `i, r` be
> integers. There is a unique open subscheme `U ⊆ X` characterised by the following:
>
> 1. `E|_U ≅ H^i(E|_U)[-i]` and `H^i(E|_U)` is a locally free `𝒪_U`-module of rank `r`,
> 2. a morphism `f : Y ⟶ X` factors through `U` if and only if `Lf^* E` is isomorphic to a locally
>    free module of rank `r` placed in degree `i`.
>
> "Locally free of rank `r`" for an integer `r` is read, as the source states it, at each point: a
> sheaf of modules has it when every point has a neighbourhood on which the sheaf is free of rank
> `r`. For `r ≥ 0` that is finite local freeness of rank `r` and the statement is
> `existsUnique_opens_singleDegreeRank` with its witness `singleDegreeRankOpen E i r`; for `r < 0`
> the condition forces the scheme to be empty, and the open subscheme is `⊥`.

```lean
theorem existsUnique_opens_singleDegreeRank_int (E : DerivedCategory X.Modules)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E)
    (i r : ℤ) :
    ∃! U : X.Opens,
      (Nonempty ((restrictFunctor U.ι).mapDerivedCategory.obj E ≅
            (DerivedCategory.singleFunctor U.toScheme.Modules i).obj
              ((DerivedCategory.homologyFunctor U.toScheme.Modules i).obj
                ((restrictFunctor U.ι).mapDerivedCategory.obj E))) ∧
          ∀ _ : U.toScheme, ∃ n : ℕ, (n : ℤ) = r ∧
            AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
              ((DerivedCategory.homologyFunctor U.toScheme.Modules i).obj
                ((restrictFunctor U.ι).mapDerivedCategory.obj E)) n) ∧
        ∀ (Y : Scheme.{u}) (f : Y ⟶ X),
          (∃ g : Y ⟶ U.toScheme, g ≫ U.ι = f) ↔
            ∃ M : Y.Modules,
              (∀ _ : Y, ∃ n : ℕ, (n : ℤ) = r ∧
                  AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} M n) ∧
                Nonempty ((derivedPullback f.toLRSHom.toShHom).obj E ≅
                  (DerivedCategory.singleFunctor Y.Modules i).obj M)
```

**`AlgebraicGeometry.Scheme.Modules.factorsThrough_singleDegreeRankOpen_iff_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SingleDegreeRankOpenUniversal.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SingleDegreeRankOpenUniversal.lean#L405). The attribute's comment: “part (2): the universal property along an arbitrary morphism, rank r : N”.

> Let `E` be a perfect object of `D(𝒪_X)`, `i` an integer and `r` a natural number. A morphism
> of schemes `f : Y ⟶ X` factors through `singleDegreeRankOpen E i r` exactly when `Lf^*E` is
> isomorphic to a finite locally free `𝒪_Y`-module of rank `r` placed in degree `i`.

```lean
theorem factorsThrough_singleDegreeRankOpen_iff_derivedPullback
    (hE : RingedSpace.IsPerfect.{u, u + 1} (X := X.toRingedSpace) E) {Y : Scheme.{u}}
    (f : Y ⟶ X) :
    (∃ g : Y ⟶ (singleDegreeRankOpen E i r).toScheme,
        g ≫ (singleDegreeRankOpen E i r).ι = f) ↔
      ∃ M : Y.Modules,
        AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} M r ∧
          Nonempty ((derivedPullback f.toLRSHom.toShHom).obj E ≅
            (DerivedCategory.singleFunctor Y.Modules i).obj M)
```

## Tag 0BDL, a lemma

[Tag 0BDL](https://stacks.math.columbia.edu/tag/0BDL) in the Stacks Project.

**`AlgebraicGeometry.BottomRankStratum.isBottomRankStratum_fittingRankStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BottomRankStratum.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/BottomRankStratum.lean#L335). The attribute's comment: “parts (1) and (2), for E a finite type quasi-coherent module placed in degree a”.

> **The rank `s` Fitting stratum is a bottom rank `s` stratum for a module placed in degree
> `a`.** Its structural morphism is a locally closed immersion and it represents the rank `s`
> functor of `F` ([stacks 05P8]), which for a module placed in degree `a` is the condition of being
> universally of bottom rank `s`.
>
> This is descriptions (1) and (2) of [stacks 0BDL] for an `E` which is a module placed in degree
> `a`.

```lean
public theorem isBottomRankStratum_fittingRankStratum (F : X.Modules) [F.IsFiniteType]
    [F.IsQuasicoherent] (a : ℤ) (s : ℕ) :
    IsBottomRankStratum ((DerivedCategory.singleFunctor X.Modules a).obj F) a s
      (fittingRankStratum F s).hom
```

**`AlgebraicGeometry.BottomRankStratum.pullbackHomologySingleCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BottomRankStratum.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/BottomRankStratum.lean#L371). The attribute's comment: “part (3), for E a module placed in degree a”.

> **`H^a(L(g ∘ j)^* E) ≅ g^* H^a(Lj^* E)` for `E` a module placed in degree `a`.** This is
> part (3) of [stacks 0BDL]: a morphism factoring as `Y ⟶ Z ⟶ X` has its degree-`a` cohomology of
> the derived pullback the ordinary pullback along `g` of the one on `Z`.
>
> Both sides are identified with an ordinary pullback of `F` by `pullbackHomologySingleIso`, and
> the two ordinary pullbacks are identified by `AlgebraicGeometry.Scheme.Modules.pullbackComp`, so
> the isomorphism is a composite of canonical maps and not merely an abstract isomorphism of
> locally free modules of the same rank.

```lean
public def pullbackHomologySingleCompIso (F : X.Modules) (a : ℤ) {Y Z : Scheme.{u}} (j : Z ⟶ X)
    (g : Y ⟶ Z) :
    pullbackHomology ((DerivedCategory.singleFunctor X.Modules a).obj F) a (g ≫ j) ≅
      (Scheme.Modules.pullback g).obj
        (pullbackHomology ((DerivedCategory.singleFunctor X.Modules a).obj F) a j)
```

**`AlgebraicGeometry.BottomRankStratum.factorsThrough_fittingRankStratum_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BottomRankStratum.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/BottomRankStratum.lean#L388). The attribute's comment: “part (4), (a) iff (b), for E a finite type quasi-coherent module in degree a”.

> **A morphism factors through the rank `s` Fitting stratum exactly when `H^a(Lf^* E)` is
> finite locally free of rank `s`.** This is the equivalence of (a) and (b) in part (4) of
> [stacks 0BDL] for `E` a module placed in degree `a`.
>
> No bound on the derived-fibre Betti numbers is needed: the quantification over further morphisms
> in description (2) costs nothing for a module placed in degree `a`, because the ordinary pullback
> of a finite locally free module of rank `s` is again one.

```lean
public theorem factorsThrough_fittingRankStratum_iff (F : X.Modules) [F.IsFiniteType]
    [F.IsQuasicoherent] (a : ℤ) (s : ℕ) {Y : Scheme.{u}} (f : Y ⟶ X) :
    (∃ g : Y ⟶ (fittingRankStratum F s).left, g ≫ (fittingRankStratum F s).hom = f) ↔
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
        (pullbackHomology ((DerivedCategory.singleFunctor X.Modules a).obj F) a f) s
```

**`AlgebraicGeometry.BottomRankStratum.isBottomRankStratum_finitePresentation_fittingRankStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BottomRankStratum.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/BottomRankStratum.lean#L405). The attribute's comment: “parts (1), (2) and finite presentation, E a finitely presented module in degree a”.

> **The rank `s` Fitting stratum of a finitely presented module is a bottom rank `s` stratum
> whose structural morphism is of finite presentation.** This is descriptions (1) and (2) of
> [stacks 0BDL] together with its assertion that `j : Z ⟶ X` is of finite presentation, for `E` a
> finitely presented module placed in degree `a`.
>
> The finite presentation is `AlgebraicGeometry.finitePresentation_fittingRankStratum`; the two
> halves are stated together because the tag's "moreover" is about the same `j` that descriptions
> (1) and (2) characterise.

```lean
public theorem isBottomRankStratum_finitePresentation_fittingRankStratum (F : X.Modules)
    [F.IsFinitePresentation] (a : ℤ) (s : ℕ) :
    IsBottomRankStratum ((DerivedCategory.singleFunctor X.Modules a).obj F) a s
        (@fittingRankStratum X F (SheafOfModules.instIsFiniteTypeOfIsFinitePresentation F)
          (SheafOfModules.instIsQuasicoherentOfIsFinitePresentation F) s).hom ∧
      FinitePresentation
        (@fittingRankStratum X F (SheafOfModules.instIsFiniteTypeOfIsFinitePresentation F)
          (SheafOfModules.instIsQuasicoherentOfIsFinitePresentation F) s).hom
```

**`AlgebraicGeometry.BottomRankStratum.isClosedImmersion_fittingRankStratum_of_isGeneratedByNear`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BottomRankStratum.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/BottomRankStratum.lean#L443). The attribute's comment: “part (4), closedness of j, E a module in degree a, Betti bound as generation”.

> **When the module is generated by `s` sections near every point, the rank `s` Fitting stratum
> is a closed subscheme.** This is the closedness assertion of part (4) of [stacks 0BDL] for `E` a
> module placed in degree `a`, with the hypothesis `β_a ≤ s` in the form it takes for such an `E`:
> `β_a(x)` is the dimension of the fibre of `F` at `x`, so `β_a(x) ≤ s` says that `F` needs at most
> `s` generators near `x`.
>
> Under that hypothesis the `s`-th Fitting ideal is the unit ideal, so the open subscheme cut out
> of the Fitting closed subscheme of index `s - 1` by the generator open of index `s` is the whole
> of it, and the structural morphism of the stratum is that closed immersion up to an
> isomorphism.

```lean
public theorem isClosedImmersion_fittingRankStratum_of_isGeneratedByNear (F : X.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent] (s : ℕ) (hgen : ∀ x : X, IsGeneratedByNear F s x) :
    IsClosedImmersion (fittingRankStratum F s).hom
```

**`AlgebraicGeometry.BottomRankStratum.exists_isBottomRankStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BottomRankStratumMain.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/BottomRankStratumMain.lean#L355).

> **The bottom rank stratum of a perfect complex.** Let `E` be perfect of Tor amplitude in
> `[a, b]` and `r` a natural number. There is a locally closed immersion `j : Z ⟶ X` with
> `H^a(Lj^* E)` finite locally free of rank `r`, through which a morphism `f : Y ⟶ X` factors
> exactly when `H^a(L(g ∘ f)^* E)` is finite locally free of rank `r` for every `g : Y' ⟶ Y`
> (`IsBottomRankStratum`). The morphism `j` is of finite presentation, and
> `H^a(L(g ∘ j)^* E) ≅ g^* H^a(Lj^* E)` for every `g : Y ⟶ Z`. If `β_a ≤ r` everywhere, then `j` is
> a closed immersion, a morphism `f` factors through `Z` exactly when `H^a(Lf^* E)` is finite
> locally free of rank `r`, and, when `r = 1`, exactly when the scalar action
> `𝒪_Y ⟶ SheafHom(H^a(Lf^* E), H^a(Lf^* E))` is a monomorphism.

```lean
theorem exists_isBottomRankStratum (E : DerivedCategory X.Modules)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E) (a b : ℤ)
    (htor : Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace E a b) (r : ℕ) :
    ∃ (Z : Scheme.{u}) (j : Z ⟶ X), IsBottomRankStratum E a r j ∧ FinitePresentation j ∧
      (∀ (Y : Scheme.{u}) (g : Y ⟶ Z), Nonempty (pullbackHomology E a (g ≫ j) ≅
        (Scheme.Modules.pullback g).obj (pullbackHomology E a j))) ∧
      ((∀ x : X, DerivedFibreBetti.derivedFiberBetti X E
          (Scheme.Modules.isPseudoCoherent_of_isPerfect E hE) a x ≤ r) →
        IsClosedImmersion j ∧
        (∀ (Y : Scheme.{u}) (f : Y ⟶ X), (∃ g : Y ⟶ Z, g ≫ j = f) ↔
          SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (pullbackHomology E a f) r) ∧
        (r = 1 → ∀ (Y : Scheme.{u}) (f : Y ⟶ X), (∃ g : Y ⟶ Z, g ≫ j = f) ↔
          Mono (Stacks.SheafOfModules.scalarAction Y.toRingedSpace (pullbackHomology E a f)
            (Stacks.Cohomology.SheafHomComplex.sheafHom Y.sheaf _ _))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.31, Tag 0BDH](https://stacks.math.columbia.edu/tag/0BDH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
