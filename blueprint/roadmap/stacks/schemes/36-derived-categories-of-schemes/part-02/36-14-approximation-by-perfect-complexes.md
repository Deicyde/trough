---
declaration: section
origin: cited
lean: AlgebraicGeometry.HasPerfectApproximation, AlgebraicGeometry.HasApproximationByPerfectComplexes, AlgebraicGeometry.hasPerfectApproximation_of_open, AlgebraicGeometry.PerfectApproximation.approximationHolds_of_affineCover, AlgebraicGeometry.PerfectApproximation.approximationByPerfectComplexes_of_isAffine, AlgebraicGeometry.PerfectApproximation.hasApproximationByPerfectComplexes_of_isAffine, AlgebraicGeometry.PerfectApproximation.hasApproximationByPerfectComplexes_of_sup_affine, AlgebraicGeometry.PerfectApproximation.approximationByPerfectComplexes_sup_affine
statement: formalized
proof: formalized
---

# 36.14 Approximation by perfect complexes

Section 36.14 of the Stacks Project, [Tag 08EL](https://stacks.math.columbia.edu/tag/08EL). 6 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08EM, a definition

[Tag 08EM](https://stacks.math.columbia.edu/tag/08EM) in the Stacks Project.

**`AlgebraicGeometry.HasPerfectApproximation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/Defs.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/Defs.lean#L65).

> Approximation holds for the triple `(T, E, m)`: there is a perfect object of the derived
> category of `𝒪_X`-modules, cohomologically supported on `T`, mapping to `E` by a map which is an
> isomorphism on cohomology in every degree above `m` and an epimorphism on cohomology in
> degree `m`.

```lean
abbrev HasPerfectApproximation (X : Scheme.{u}) (T : Set X)
    (E : DerivedCategory.{u + 1} X.Modules) (m : ℤ) : Prop
```

## Tag 08EN, a definition

[Tag 08EN](https://stacks.math.columbia.edu/tag/08EN) in the Stacks Project.

**`AlgebraicGeometry.HasApproximationByPerfectComplexes`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/Defs.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/Defs.lean#L79).

> The scheme `X` satisfies approximation by perfect complexes: for every closed subset `T`
> with retrocompact complement there is an integer `r` such that every sufficiently
> pseudo-coherent derived object with quasi-coherent cohomology supported on `T` in high degrees
> admits a perfect approximation.

```lean
abbrev HasApproximationByPerfectComplexes (X : Scheme.{u}) : Prop
```

## Tag 08EP, a lemma

[Tag 08EP](https://stacks.math.columbia.edu/tag/08EP) in the Stacks Project.

**`AlgebraicGeometry.hasPerfectApproximation_of_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Approximation/OpenSubscheme.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/Approximation/OpenSubscheme.lean#L276).

> **Stacks Project, Tag 08EP.** Let `T` be a closed subset of a scheme `X` contained in an
> open subscheme `U`, and let `E` be an object of the derived category of `𝒪_X`-modules whose
> cohomology vanishes off `T` in every degree at least `m`. If approximation by a perfect complex
> holds for the restriction of `E` to `U`, relative to the preimage of `T` and the same degree
> `m`, then it holds for `E`.
>
> The perfect object is the extension by zero `j_! P` of an approximation `P` over `U`: it is
> perfect because the derived pushforward of a perfect object with closed support is perfect
> (Stacks 08DP) and agrees there with extension by zero (Stacks 08DF), and its cohomology is
> supported on `T` because extension by zero preserves the support. The map to `E` is the
> extension by zero of the approximation, followed by the derived counit of `j_! ⊣ j^*`; the
> support hypothesis on `E` makes the underived counit invertible on each cohomology sheaf in
> degree at least `m`, and hence the derived counit invertible on cohomology there.

```lean
theorem hasPerfectApproximation_of_open
    (X : Scheme.{u}) (U : X.Opens) (T : Set X) (hT : IsClosed T) (hTU : T ⊆ (U : Set X))
    (E : DerivedCategory.{u + 1} X.Modules) (m : ℤ)
    (hApprox : HasPerfectApproximation (U : Scheme.{u})
      ((fun x : U ↦ (x.1 : X)) ⁻¹' T)
      ((RingedSpace.restrictModules X.toRingedSpace U).mapDerivedCategory.obj E) m)
    (hSupport : ∀ i : ℤ, m ≤ i → ∀ x : X, x ∉ T →
      IsZero (TopCat.Presheaf.stalk (X := X)
        (((DerivedCategory.homologyFunctor X.Modules i).obj E).val.presheaf) x)) :
    HasPerfectApproximation X T E m
```

## Tag 08EQ, a lemma

[Tag 08EQ](https://stacks.math.columbia.edu/tag/08EQ) in the Stacks Project.

**`AlgebraicGeometry.PerfectApproximation.approximationHolds_of_affineCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/AffineCover.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/AffineCover.lean#L386). The attribute's comment: “first assertion: approximation for triples on an affine scheme”.

> Let `X` be an affine scheme. Approximation holds for every triple `(T, E, m)` with `E` an
> object of `D_QCoh(𝒪_X)` for which there is an integer `r ≥ 0` such that
>
> 1. `E` is `m`-pseudo-coherent,
> 2. `Hⁱ(E)` is supported on `T` for `i ≥ m - r + 1`,
> 3. `X ∖ T` is the union of `r` affine opens `U₁, …, U_r`.

```lean
theorem approximationHolds_of_affineCover (X : Scheme.{u}) [IsAffine X] (T : Set X)
    {r : ℕ} (U : Fin r → X.Opens) (hU : ∀ k, IsAffineOpen (U k))
    (hcover : ((⨆ k, U k : X.Opens) : Set X) = Tᶜ)
    (E : DerivedCategory.{u + 1} X.Modules) (m : ℤ)
    (hqc : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj E).IsQuasicoherent)
    (hpc : RingedSpace.IsPseudoCoherentFrom (X := X.toRingedSpace) E m)
    (hsupp : ∀ i : ℤ, m - (r : ℤ) + 1 ≤ i → ∀ x : X, x ∉ T →
      IsZero (TopCat.Presheaf.stalk (X := X)
        (((DerivedCategory.homologyFunctor X.Modules i).obj E).val.presheaf) x)) :
    ApproximationHolds X T E m
```

**`AlgebraicGeometry.PerfectApproximation.approximationByPerfectComplexes_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/AffineScheme.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/AffineScheme.lean#L256). The attribute's comment: “second assertion: approximation by perfect complexes on an affine scheme”.

> **Approximation by perfect complexes holds on an affine scheme.** This is the second
> assertion of [Stacks, Tag 08EQ]: the case of `Spec R`,
> `AlgebraicGeometry.PerfectApproximation.approximationByPerfectComplexes_spec`, transported
> along `AlgebraicGeometry.Scheme.isoSpec`.

```lean
theorem approximationByPerfectComplexes_of_isAffine (X : Scheme.{u}) [IsAffine X] :
    ApproximationByPerfectComplexes X
```

**`AlgebraicGeometry.PerfectApproximation.hasApproximationByPerfectComplexes_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/AffineScheme.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/AffineScheme.lean#L264). The attribute's comment: “second assertion: approximation by perfect complexes on an affine scheme”.

> **Approximation by perfect complexes holds on an affine scheme**, in the encoding of
> `AlgebraicGeometry.HasApproximationByPerfectComplexes`.

```lean
theorem hasApproximationByPerfectComplexes_of_isAffine (X : Scheme.{u}) [IsAffine X] :
    HasApproximationByPerfectComplexes X
```

## Tag 08ER, a lemma

[Tag 08ER](https://stacks.math.columbia.edu/tag/08ER) in the Stacks Project.

**`AlgebraicGeometry.PerfectApproximation.hasApproximationByPerfectComplexes_of_sup_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/QuasiCompactQuasiSeparated.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/QuasiCompactQuasiSeparated.lean#L356).

> Let `X = U ∪ V` be an open cover with `U` quasi-compact, `V` affine and `U ∩ V`
> quasi-compact. If approximation by perfect complexes holds on `U`, then it holds on `X`.

```lean
theorem hasApproximationByPerfectComplexes_of_sup_affine {X : Scheme.{u}} (U V : X.Opens)
    (hUV : U ⊔ V = ⊤) (hU : IsCompact (U : Set X)) (hV : IsAffineOpen V)
    (hUVc : IsCompact ((U : Set X) ∩ V)) (h : HasApproximationByPerfectComplexes U.toScheme) :
    HasApproximationByPerfectComplexes X
```

**`AlgebraicGeometry.PerfectApproximation.approximationByPerfectComplexes_sup_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/UnionAffine.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/UnionAffine.lean#L124). The attribute's comment: “approximation by perfect complexes passes from a quasi-compact open to its union with an affine open meeting it in a quasi-compact open; nothing is carried, and the statement is at the standard derived category of the sheaves of modules of the scheme, the model the whole chapter is written at”.

> **[Stacks, Tag 08ER].** Let `X` be a scheme, let `X = U ∪ V` be an open covering with `U`
> quasi-compact, `V` affine and `U ∩ V` quasi-compact. If approximation by perfect complexes holds
> on `U`, then it holds on `X`.
>
> The integer attached to a closed subset `T` with retrocompact complement is `a + b`, where `a`
> is the integer attached on `U` to `T ∩ U` and `b` the integer attached on `V` to `T ∖ U`, both
> taken nonnegative. Given a triple `(T, E, m)` satisfying the hypotheses for that integer, the
> approximation is built by induction on the largest degree in which the cohomology of `E`
> survives on `U`: below `m - b` the cohomology of `E` is supported on `T ∖ U ⊆ V` in all relevant
> degrees and [Stacks, Tag 08EQ] on `V` together with [Stacks, Tag 08EP] finishes, while above it
> the glueing step of [Stacks, Tag 09IM] turns an approximation on `U` in that degree into a
> perfect object on `X` surjective there, and the cone of the resulting map survives on `U` in one
> degree fewer.

```lean
theorem approximationByPerfectComplexes_sup_affine (X : Scheme.{u}) (U V : X.Opens)
    (hVaff : IsAffineOpen V) (hcover : U ⊔ V = ⊤)
    (hUc : IsCompact (U : Set X)) (hUVc : IsCompact ((U ⊓ V : X.Opens) : Set X))
    (hUapp : ApproximationByPerfectComplexes (U : Scheme.{u})) :
    ApproximationByPerfectComplexes X
```

**`AlgebraicGeometry.PerfectApproximation.hasApproximationByPerfectComplexes_sup_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/UnionAffine.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/UnionAffine.lean#L287). The attribute's comment: “the same statement in the second encoding of the property of Tag 08EN; nothing is carried, and the derived category is the standard model, as in the first encoding”.

> **[Stacks, Tag 08ER]**, in the encoding of
> `AlgebraicGeometry.HasApproximationByPerfectComplexes`.

```lean
theorem hasApproximationByPerfectComplexes_sup_affine (X : Scheme.{u}) (U V : X.Opens)
    (hVaff : IsAffineOpen V) (hcover : U ⊔ V = ⊤)
    (hUc : IsCompact (U : Set X)) (hUVc : IsCompact ((U ⊓ V : X.Opens) : Set X))
    (hUapp : HasApproximationByPerfectComplexes (U : Scheme.{u})) :
    HasApproximationByPerfectComplexes X
```

## Tag 08ES, a theorem

[Tag 08ES](https://stacks.math.columbia.edu/tag/08ES) in the Stacks Project.

**`AlgebraicGeometry.PerfectApproximation.approximationByPerfectComplexes_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/Qcqs.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/Qcqs.lean#L65). The attribute's comment: “approximation by perfect complexes on a quasi-compact quasi-separated scheme; nothing is carried, and the statement is at the standard derived category of the sheaves of modules of the scheme, the model the whole chapter is written at”.

> **[Stacks, Tag 08ES].** Approximation by perfect complexes holds on every quasi-compact and
> quasi-separated scheme.
>
> The induction principle of [Stacks, Tag 08DR] applied to the property that approximation holds
> on an open subscheme: the affine case is [Stacks, Tag 08EQ] and the union step is
> [Stacks, Tag 08ER].

```lean
theorem approximationByPerfectComplexes_of_qcqs (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] : ApproximationByPerfectComplexes X
```

**`AlgebraicGeometry.PerfectApproximation.hasApproximationByPerfectComplexes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/QuasiCompactQuasiSeparated.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/QuasiCompactQuasiSeparated.lean#L485).

> Approximation by perfect complexes holds on every quasi-compact and quasi-separated scheme.

```lean
theorem hasApproximationByPerfectComplexes (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] : HasApproximationByPerfectComplexes X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.14, Tag 08EL](https://stacks.math.columbia.edu/tag/08EL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
