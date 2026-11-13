---
declaration: section
origin: cited
lean: Stacks.Chow.projectiveBundleProjection_twist_eq_zero_of_lt, Stacks.Chow.projectiveBundle_projection, Stacks.Chow.projectiveBundle_formula, Stacks.Chow.bijective_projectiveBundleFormulaMap, Stacks.Chow.flatPullbackChow_bijective_vectorBundleToBase_zero, Stacks.Chow.flatPullbackChow_bijective_vectorBundleToBase, Stacks.Chow.flatPullbackChow_bijective_vectorBundleToBase_factorsGeneral, Stacks.Chow.flatPullbackChow_bijective_of_isAffineSpaceBundle_zero
statement: formalized
proof: formalized
---

# 42.36 Projective space bundle formula

Section 42.36 of the Stacks Project, [Tag 02TV](https://stacks.math.columbia.edu/tag/02TV). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02TW, a lemma

[Tag 02TW](https://stacks.math.columbia.edu/tag/02TW) in the Stacks Project.

**`Stacks.Chow.projectiveBundleProjection_twist_eq_zero_of_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleProjectionFormula.lean, line 502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleProjectionFormula.lean#L502). The attribute's comment: “vanishing below the fibre dimension: the assertion for s < r - 1, with no hypothesis. The projective bundle enters as a flat, proper morphism of relative dimension r - 1 over the base (Stacks 02TX) and its twist as an invertible module; Stacks 02S1 for the flat pullback, Stacks 02SO and 02TI for the cap product and Stacks 02S2 for the pushforward are all supplied from this development. The top fibre power, that the pushforward at s = r - 1 is α itself, is NOT proved here. What it still needs is the mapping-in half of the universal property of relative Proj, Stacks 01O4, to produce the section Z -> pi^-1(Z) whose image the r - 1 sections cut out; the other two ingredients the source's proof uses are now available, Stacks 02TM unconditionally and the rational sections of O\_P(1) as Stacks.ProjectiveBundleTwist.twistSectionGerm”.

> **Stacks 02TW, vanishing below the fibre dimension, with no hypothesis.** For `s < r - 1`,
>
>   `π_*(c₁(L)^s ∩ π^*α) = 0`  in  `A_{k+(r-1)-s}(X)`,
>
> for `L` the twist `O_P(1)` of the projective bundle. Nothing is assumed beyond the geometry of
> the bundle: `π` is flat, proper and of relative dimension `r - 1` over the base, which for the
> projective bundle of a finite locally free module of rank `r` is Stacks 02TX
> (`Stacks.RelativeProj.isProper_projectiveBundleToBase`,
> `Stacks.RelativeProj.locallyOfFiniteType_projectiveBundleToBase` and
> `Stacks.SymGraded.relativeDimension_freeProjectiveBundleToBase`), and `L` is an invertible
> module on `P`, which the twist is.
>
> The three inputs the operation is built from are all theorems here: Stacks 02S1 for the flat
> pullback is `Stacks.Chow.projectiveBundleFlatPullbackFactors`, Stacks 02SO and 02TI for the cap
> with `c₁(L)` are `Stacks.Chow.invertibleChernCap`, and Stacks 02S2 for the pushforward is
> `Stacks.Chow.properPushforwardFactorsThroughRationalEquivalence_of_isProper`. The vanishing
> itself is the dimension count of
> `Stacks.Chow.properChowPushforward_iteratedChernCapOnChow_flatPullbackChow_eq_zero`.

```lean
theorem projectiveBundleProjection_twist_eq_zero_of_lt (L : P.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible P.sheaf.obj P.ringCatSheaf.property L]
    (s : ℕ) (hs : s < r - 1) (k : ℤ) (α : chowGroup C sX k) :
    projectiveBundleProjection C sX sP π hsP r hπ
      (projectiveBundleFlatPullbackFactors C sX sP π hsP r hπ)
      (invertibleChernCap C sP L) s k α = 0
```

**`Stacks.Chow.projectiveBundle_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProjectiveBundleFormula/Formula.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProjectiveBundleFormula/Formula.lean#L149).

> For the projective bundle `π : P ⟶ X` of a module of rank `n + 1`, `α ∈ A_k(X)` and `s ≤ n`,
> the class `π_*(c₁(𝒪_P(1))^s ∩ π^*α) ∈ A_{k+n-s}(X)` is `0` if `s < n` and is `α` if `s = n`.

```lean
theorem projectiveBundle_projection (s : ℕ) (hs : s ≤ n) (k m : ℤ) (h : k + n = m + s)
    (α : chowGroup C sX k) :
    letI := AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.isFiniteLocallyFree E
      (n + 1)
    letI := flat_bundleProj E n
    letI := locallyOfFiniteType_bundleProj E n
    bundleProjection C sX (bundleProj E ≫ sX) (bundleProj E) rfl n
        (relativeDimension_bundleProj E n) (invCap C (bundleProj E ≫ sX) (bundleTwist E)) s k m
        h α =
      if hsn : s = n then chowGroupCast C sX (by subst hsn; omega) α else 0
```

## Tag 02TX, a lemma

[Tag 02TX](https://stacks.math.columbia.edu/tag/02TX) in the Stacks Project.

**`Stacks.Chow.projectiveBundle_formula`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProjectiveBundleFormula/Formula.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProjectiveBundleFormula/Formula.lean#L168).

> The projective space bundle formula for the projective bundle of a module of rank `n + 1`: the
> map `⨁_{i ≤ n} A_{k+i}(X) ⟶ A_{k+n}(P)`, `(α_i) ↦ ∑_i c₁(𝒪_P(1))^i ∩ π^*α_i`, is bijective.

```lean
theorem projectiveBundle_formula (k : ℤ) :
    letI := AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.isFiniteLocallyFree E
      (n + 1)
    letI := flat_bundleProj E n
    letI := locallyOfFiniteType_bundleProj E n
    Function.Bijective (bundleMap C sX (bundleProj E ≫ sX) (bundleProj E) rfl n
      (relativeDimension_bundleProj E n) (invCap C (bundleProj E ≫ sX) (bundleTwist E)) k)
```

**`Stacks.Chow.bijective_projectiveBundleFormulaMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProjectiveBundleFormula/FormulaOfRank.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProjectiveBundleFormula/FormulaOfRank.lean#L121). References: SGA 7 XVII (5.3), “more general”.

> **The projective space bundle formula.** Let `X` be locally of finite type over the
> base `S` of chapter 42, `ℰ` a finite locally free `𝒪_X`-module of rank `r` and
> `(π : P ⟶ X, 𝒪_P(1))` its projective bundle. Then the map
> `⨁_{i = 0}^{r - 1} A_{k+i}(X) ⟶ A_{k+r-1}(P)`, `(α_i) ↦ ∑_i c₁(𝒪_P(1))^i ∩ π^*α_i`, is an
> isomorphism, for every `k`.

```lean
theorem bijective_projectiveBundleFormulaMap (k : ℤ) :
    Function.Bijective (projectiveBundleFormulaMap E r C sX k)
```

## Tag 02TY, a lemma

[Tag 02TY](https://stacks.math.columbia.edu/tag/02TY) in the Stacks Project.

**`Stacks.Chow.flatPullbackChow_bijective_vectorBundleToBase_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/VectorBundleAffineSpaceBundle.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/VectorBundleAffineSpaceBundle.lean#L262). The attribute's comment: “the isomorphism in rank zero, the bundle now the relative spectrum of the symmetric algebra of a finite locally free sheaf of rank zero rather than an abstract affine-space bundle”.

> **Stacks 02TY in rank zero, for the relative spectrum of the symmetric algebra.** Let `X` be
> locally of finite type over the base of chapter 42, let `ℰ` be a finite locally free sheaf of rank
> zero on `X` and let `p : E = Spec_X(Sym(ℰ)) ⟶ X` be the associated vector bundle. Then
> `p^* : A_k(X) ⟶ A_k(E)` is bijective for every `k`.
>
> The bundle is the relative spectrum of `Sym(ℰ)`, which is the tag's own object;
> `Stacks.Chow.isAffineSpaceBundle_vectorBundleToBase` supplies the local triviality that
> `Stacks.Chow.flatPullbackChow_bijective_of_isAffineSpaceBundle_zero` needs, and the flatness,
> local finite type and relative dimension of `p` come from it as well. The instance of Stacks 02S1
> that writes the map down is not an extra assumption: a rank-zero bundle projection is an
> isomorphism, so it is produced by
> `Stacks.Chow.flatPullbackFactorsThroughRationalEquivalence_of_isIso`.

```lean
theorem flatPullbackChow_bijective_vectorBundleToBase_zero (C : ChowSituation.{u})
    {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (E : X.Modules)
    [E.IsQuasicoherent]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E 0] (k : ℤ) :
    letI _ := locallyOfFiniteType_vectorBundleToBase E 0
    letI _ := flat_vectorBundleToBase E 0
    letI _ := isIso_vectorBundleToBase_zero E
    Function.Bijective (flatPullbackChow C
      (Scheme.Modules.vectorBundleToBase X E ≫ sX) sX
      (Scheme.Modules.vectorBundleToBase X E) rfl 0
      (relativeDimension_vectorBundleToBase E 0) k
      (flatPullbackFactorsThroughRationalEquivalence_of_isIso C
        (Scheme.Modules.vectorBundleToBase X E ≫ sX) sX
        (Scheme.Modules.vectorBundleToBase X E) rfl
        (relativeDimension_vectorBundleToBase E 0) k))
```

**`Stacks.Chow.flatPullbackChow_bijective_vectorBundleToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/VectorBundleChowBijective.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/VectorBundleChowBijective.lean#L340).

> **[Stacks, Tag 02TY].** Let `(S, δ)` be as in Situation 02QL, let `X` be locally of finite type
> over `S`, let `ℰ` be a finite locally free `𝒪_X`-module of rank `r` and let
> `p : E = \underline{\Spec}(\Sym^*(ℰ)) ⟶ X` be the associated vector bundle. Then
>
>   `p^* : A_k(X) ⟶ A_{k+r}(E)`
>
> is an isomorphism for every `k`.
>
> Surjectivity is [Stacks, Tag 02TT] for the affine-space bundle `p`; injectivity is
> `Stacks.Chow.flatPullbackChow_injective_vectorBundleToBase`. The instance `[E.IsQuasicoherent]`,
> which the construction of `𝐕(ℰ)` takes, restricts nothing: a finite locally free module is
> quasi-coherent, by
> `Stacks.AlgebraicGeometry.CoherenceCriteria.isQuasicoherent_of_isFiniteLocallyFree`, and the
> instance is a proposition.

```lean
theorem flatPullbackChow_bijective_vectorBundleToBase {X : Scheme.{u}} (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (E : X.Modules) [E.IsQuasicoherent] (r : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r] (k : ℤ) :
    letI := locallyOfFiniteType_vectorBundleToBase E r
    letI := flat_vectorBundleToBase E r
    Function.Bijective (flatPullbackChowOfRelativeDimension C
      (Scheme.Modules.vectorBundleToBase X E ≫ sX) sX (Scheme.Modules.vectorBundleToBase X E)
      rfl r (relativeDimension_vectorBundleToBase E r) k)
```

**`Stacks.Chow.flatPullbackChow_bijective_vectorBundleToBase_factorsGeneral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/VectorBundleFlatPullback.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/VectorBundleFlatPullback.lean#L121).

> **Stacks 02TY.** Let `X` be locally of finite type over the base of chapter 42, let `ℰ` be a
> finite locally free `𝒪_X`-module of rank `r` and let `p : Spec_X(Sym(ℰ)) ⟶ X` be its vector
> bundle. Then flat pullback `p^* : A_k(X) ⟶ A_{k+r}(Spec_X(Sym(ℰ)))` is bijective for every `k`.
>
> This is `Stacks.Chow.flatPullbackChow_bijective_vectorBundleToBase`, stated with the flat
> pullback `Stacks.Chow.flatPullbackChow` and without the instance `[E.IsQuasicoherent]`, which a
> finite locally free module satisfies
> (`Stacks.AlgebraicGeometry.CoherenceCriteria.isQuasicoherent_of_isFiniteLocallyFree`).

```lean
theorem flatPullbackChow_bijective_vectorBundleToBase_factorsGeneral (C : ChowSituation.{u})
    {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (E : X.Modules) (r : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r] (k : ℤ) :
    letI := AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.isFiniteLocallyFree E r
    letI _ := locallyOfFiniteType_vectorBundleToBase E r
    letI _ := flat_vectorBundleToBase E r
    Function.Bijective (flatPullbackChow C
      (Scheme.Modules.vectorBundleToBase X E ≫ sX) sX
      (Scheme.Modules.vectorBundleToBase X E) rfl r
      (relativeDimension_vectorBundleToBase E r) k
      (flatPullbackFactorsThroughRationalEquivalence_general C _ sX _ rfl r _ k))
```

**`Stacks.Chow.flatPullbackChow_bijective_of_isAffineSpaceBundle_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/VectorBundlePullbackIso.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/VectorBundlePullbackIso.lean#L149). The attribute's comment: “the isomorphism in rank zero, the projection carried as an affine-space bundle of rank zero rather than as the relative spectrum of a symmetric algebra”.

> **Stacks 02TY in rank zero.** Let `X` be locally of finite type over the base of chapter 42,
> let `ℰ` be a finite locally free sheaf of rank `0` on `X` and let `p : E ⟶ X` be the associated
> vector bundle. Then `p^* : CH_k(X) ⟶ CH_{k+0}(E)` is bijective, which is the assertion of Stacks
> 02TY for `r = 0`.
>
> The bundle projection is carried as an affine-space bundle of rank zero, `p` being Zariski-locally
> on `X` the projection `𝔸^0_U ⟶ U`; a rank-zero vector bundle projection has that property. Such a
> `p` is an isomorphism, so the assertion is
> `Stacks.Chow.flatPullbackChow_bijective_of_isIso`. The instance of Stacks 02S1 needed to write the
> map down is not an extra assumption: it is supplied by
> `Stacks.Chow.flatPullbackFactorsThroughRationalEquivalence_of_isIso`.
>
> Neither half is proved here for `r ≥ 1`. The source proof forms the projective space bundle
> `P = P(ℰ ⊕ 𝒪_X)` with its tautological invertible sheaf, identifies `𝒪_P(D) = 𝒪_P(1)` for the
> divisor `D = Z(s)` at infinity by Stacks 01X0, writes `E` as `P ∖ D`, and then runs the
> localization sequence of Stacks 02RX against the projective bundle formula of Stacks 02TX for `P`
> and for `D`.
>
> Of those inputs **Stacks 02TR is proved**, in both of its equalities and at Chow level for an
> arbitrary class: `Stacks.Chow.gysinChowOfInvertible_flatPullbackChow` gives
> `i^* p^* α = (p|_D)^* α` and `Stacks.Chow.firstChernClassCapChow_flatPullbackChow` gives
> `c₁(ℒ) ∩ p^* α = i_*((p|_D)^* α)`
> (`StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierFlatPullbackChow.lean:385, 463`,
> with the cycle-level forms at
> `StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierFlatPullback.lean:178, 241, 289`).
>
> What is still missing is Stacks 02TX, which is not proved in this repository — it is available
> only as the two hypotheses `Stacks.Chow.ProjectiveBundleRelationInjective` and
> `Stacks.Chow.ProjectiveBundleRelationSurjective`. Its surjectivity half alone is Stacks 02TT,
> which is itself proved here only in relative dimension zero, and it may not be carried as a
> hypothesis, being a conjunct of the conclusion. So the `r ≥ 1` case remains out of reach, but on
> account of 02TX and 02TT, not of 02TR.

```lean
theorem flatPullbackChow_bijective_of_isAffineSpaceBundle_zero (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] (f : X ⟶ Y) [LocallyOfFiniteType f] [AlgebraicGeometry.Flat f]
    (hbase : f ≫ sY = sX) (hf : AlgebraicGeometry.RelativeDimension f 0)
    (hbundle : IsAffineSpaceBundle f 0) (k : ℤ)
    (hfac : FlatPullbackFactorsThroughRationalEquivalence C sX sY f hbase 0 hf k) :
    Function.Bijective (flatPullbackChow C sX sY f hbase 0 hf k hfac)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.36, Tag 02TV](https://stacks.math.columbia.edu/tag/02TV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
