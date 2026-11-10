---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.SignTwistSetup.isQuasicoherentOnSite_twist, AlgebraicGeometry.Space.SpacesEtale.isZero_sheafH_of_isEmpty_diagonalComplement, AlgebraicGeometry.Space.isZero_rightDerived_globalSectionsFunctor_of_isSeparated, AlgebraicGeometry.Space.exists_affine_etale_surjective_cover_diagonalComplementQuotient, AlgebraicGeometry.Space.exists_bound_affine_etale_surjective_cover_diagonalComplementQuotient, AlgebraicGeometry.Space.isZero_sheafH_of_data_072C, AlgebraicGeometry.Space.exists_forall_isZero_sheafH_of_isQuasiCompactSpace_072C, AlgebraicGeometry.Space.exists_affine_etale_surjective_cover_hasUniversallyBoundedFibers
statement: formalized
proof: formalized
---

# 69.7 Higher vanishing for quasi-coherent sheaves

Section 69.7 of the Stacks Project, [Tag 0729](https://stacks.math.columbia.edu/tag/0729). 3 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 072A, a lemma

[Tag 072A](https://stacks.math.columbia.edu/tag/072A) in the Stacks Project.

**`AlgebraicGeometry.Space.SignTwistSetup.isQuasicoherentOnSite_twist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleSignTwist.lean, line 577](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleSignTwist.lean#L577).

> **Stacks 072A.** With `S`, `W`, `G`, `U`, `χ` as in Stacks 0727: if `F` is a
> quasi-coherent `𝒪_U`-module, then so is `F ⊗_ℤ ℤ(χ)`.
>
> Quasi-coherence may be checked étale locally, and `ℤ(χ)` is free of rank one on a covering of
> `U`; on each member of that covering a trivializing section identifies the twist with `F`
> itself.

```lean
theorem isQuasicoherentOnSite_twist
    (F : Modules.{u, u + 1} B S hS h.quotient.1 h.quotient.2) (hF : F.IsQuasicoherentOnSite) :
    (h.twist F).IsQuasicoherentOnSite
```

## Tag 072B, a proposition

[Tag 072B](https://stacks.math.columbia.edu/tag/072B) in the Stacks Project.

**`AlgebraicGeometry.Space.SpacesEtale.isZero_sheafH_of_isEmpty_diagonalComplement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/HigherVanishing.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/HigherVanishing.lean#L150). The attribute's comment: “the vanishing H^n(X, F) = 0 above the fibre bound of the chart. The bound used is the degree bound of Stacks 03JL on the fibres of the chart, which is what empties W_p and so what the source's proof uses, rather than the source's stated bound on the cardinality of the topological fibres of the chart; the degree is existentially quantified because the predicate of Stacks 03JL hides its own bound, and the emptiness of W_p above it is proved here. What the source draws from the quasi-compactness and separatedness of X and the affineness of the chart is the vanishing of the rows q > 0 of the E_1-page of Stacks 0728; that rests on the affineness of the quotients U_p = W_p/S_{p+1}, hence on Stacks 071S for a free action of a finite group on an arbitrary algebraic space, which this subtree does not state in any shape, and it is the binder hUpVanishing”.

> Let `S` be a scheme, let `X` be an algebraic space over `S` and let `c : W ⟶ X` be a
> surjective, étale and separated morphism from a scheme whose fibres are universally bounded in the
> sense of [Stacks, Tag 03JL].  If the rows `q > 0` of the first page of the alternating Čech
> spectral sequence of [Stacks, Tag 0728] vanish, then `H^n(X, ℱ) = 0` above the fibre bound of
> `c`.

```lean
theorem isZero_sheafH_of_isEmpty_diagonalComplement (W : BigFppfOver B S hS)
    (c : yoneda.obj W ⟶ X.obj) (hc : IsEtale B S hS c)
    (hsurj : IsSurjective B S hS c) (hsep : IsSeparated B S hS c)
    (hbound : HasUniversallyBoundedFibers B S hS W c)
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{u + 1})
    (hUpVanishing : ∀ (p : ℕ) (q : ℤ), 0 < q →
      IsZero (AddCommGrpCat.of (Abelian.zExt
        ((koszulComplex B S hS X (chartObj B S hS X W c hc)).X p) F q))) :
    ∃ d : ℕ, ∀ n : ℕ, d ≤ n → IsZero (AddCommGrpCat.of (Sheaf.H F n))
```

**`AlgebraicGeometry.Space.isZero_rightDerived_globalSectionsFunctor_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/QuasicoherentHigherVanishing.lean, line 540](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/QuasicoherentHigherVanishing.lean#L540). The attribute's comment: “The reading of d as a degree bound: the base changes of f to fields have degree at most d, which is what the source's proof uses and what Lemma 69.7.3 (Tag 072C) supplies. The literal reading (at most d points in each fibre of |U| → |X|) is neither proved nor refuted here; for it the proof's step W_p = ∅ for p ≥ d fails (Spec k' → Spec k with k'/k separable quadratic: one point per fibre, degree 2), although the conclusion holds in that example. Quasi-compactness of X is implied by the affine surjection and not assumed.”.

> **Stacks 072B.**  Let `X` be a separated algebraic space, `U` an affine scheme and
> `f : U → X` a surjective étale morphism whose base changes to fields are finite locally free of
> degree at most `d`.  Then `Hᵠ(X, ℱ) = 0` for every quasi-coherent `𝒪_X`-module `ℱ` and every
> `q ≥ d`.

```lean
theorem isZero_rightDerived_globalSectionsFunctor_of_isSeparated
    (hZ : B.Contains (⊤_ Scheme.{u})) (X : AlgebraicSpaces B S hS)
    (hsepX : IsAbsolutelySeparated B S hS hZ X.1)
    (W : BigFppfOver B S hS) (hW : IsAffine ((BigFppfOver.toScheme B S hS).obj W))
    (c : yoneda.obj W ⟶ X.obj) (hc : IsEtale B S hS c) (hsurj : IsSurjective B S hS c)
    (d : ℕ) (hd : ∀ (k : Type u) [Field k] (T : BigFppfOver B S hS),
      ((BigFppfOver.toScheme B S hS).obj T ≅ Spec (.of k)) →
      ∀ ξ : yoneda.obj T ⟶ X.obj,
        ∃ (V : BigFppfOver B S hS) (p : V ⟶ T) (i : yoneda.obj V ⟶ yoneda.obj W) (r : ℕ),
          r ≤ d ∧ Stacks.Morphisms.IsFiniteLocallyFreeOfRank
              ((BigFppfOver.toScheme B S hS).map p) r ∧
            IsPullback i (yoneda.map p) c ξ)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite) (q : ℕ) (hq : d ≤ q) :
    IsZero (((Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
      (Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B S hS X.1 X.2).O)).rightDerived q).obj F)
```

## Tag 072C, a lemma

[Tag 072C](https://stacks.math.columbia.edu/tag/072C) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_affine_etale_surjective_cover_diagonalComplementQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplementQuotientCover.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplementQuotientCover.lean#L206). The attribute's comment: “parts (4)-(5), together with parts (1)-(3) restated, for Y a quasi-compact and quasi-separated algebraic space over an arbitrary base scheme S: an affine scheme V_p, a surjective etale morphism V_p -> U_p onto the quotient U_p = W_p/S_{p+1} of Tag 0726, and an integer bounding the degrees of its fibres, for every p -- the source's range 0 <= p <= d being dropped, which is stronger. The integer max(d_p + p) is formed at AlgebraicGeometry.Space.exists_bound_affine_etale_surjective_cover_diagonalComplementQuotient; the vanishing these choices feed is AlgebraicGeometry.Space.isZero_sheafH_of_data_072C”.

> **The choices (1)–(5) of Stacks 072C.** On a quasi-compact, quasi-separated algebraic space
> `Y` over an arbitrary base scheme `S` one may choose an affine scheme `U`, a surjective étale
> morphism `f : U ⟶ Y` and a universal bound on the degrees of its fibres — and then, for *every*
> `p`, an affine scheme `V_p`, a surjective étale morphism `V_p ⟶ U_p` onto the quotient
> `U_p = W_p/S_{p+1}` of [Stacks, Tag 0726], and a universal bound on the degrees of *its*
> fibres.
>
> The separatedness of `f`, under which `W_p` and `U_p` are formed, is produced here rather than
> assumed. The source restricts `p` to `0 ≤ p ≤ d`; the restriction is dropped, which is
> stronger.
>
> Choices (1)–(3) are
> `AlgebraicGeometry.Space.exists_affine_etale_surjective_cover_hasUniversallyBoundedFibers'`, and
> (4)–(5) are that same statement applied to `U_p`, which is quasi-compact by
> `AlgebraicGeometry.Space.SpacesEtale.isQuasiCompactSpace_diagonalComplementQuotient` and
> quasi-separated because it is *separated*, by
> `AlgebraicGeometry.Space.SpacesEtale.isAbsolutelySeparated_diagonalComplementQuotient` and
> [Stacks, Tag 02X3]. Separatedness of `U_p` is what the source itself records — "since `U` is
> separated, the schemes `W_p` are separated, hence `U_p` is separated" — and it needs nothing of
> the base, which is why the base here is an arbitrary scheme.

```lean
theorem exists_affine_etale_surjective_cover_diagonalComplementQuotient
    (hqc : IsQuasiCompactSpace B S hS Y)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ Y) :
    ∃ (U : BigFppfOver B S hS) (g : yoneda.obj U ⟶ Y)
        (het : IsEtale B S hS g) (hsep : IsSeparated B S hS g),
      IsAffine ((BigFppfOver.toScheme B S hS).obj U) ∧
        (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        HasUniversallyBoundedFibers B S hS U g ∧
        ∀ p : ℕ, ∃ (V : BigFppfOver B S hS)
            (f : yoneda.obj V ⟶ (SpacesEtale.diagonalComplementQuotient B S hS
              ⟨Y, hY⟩ (SpacesEtale.chartObj B S hS ⟨Y, hY⟩ U g het)
              (p + 1) hsep).obj),
          IsAffine ((BigFppfOver.toScheme B S hS).obj V) ∧
            (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
              (BigFppfOver.toScheme B S hS)).presheaf f ∧
            IsEtale B S hS f ∧
            HasUniversallyBoundedFibers B S hS V f
```

**`AlgebraicGeometry.Space.exists_bound_affine_etale_surjective_cover_diagonalComplementQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplementQuotientCover.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplementQuotientCover.lean#L265). The attribute's comment: “the integer max(d_p + p), for Y a quasi-compact and quasi-separated algebraic space over an arbitrary base scheme S: a single integer dominating d_p + p on the range where the column p can be nonzero. The d of this statement is the emptiness threshold produced from the fibre bound of choice (3) -- W_q has no points for q > d -- and the domination is asserted for the p with p + 1 <= d. The tag's own bound, max(d_p + p) over 0 <= p <= d for d the fibre bound of choice (3), is the hypothesis of AlgebraicGeometry.Space.isZero_sheafH_of_data_072C, where the vanishing at it is proved”.

> **The integer `max(d_p + p)` of Stacks 072C.** Beside the five choices there is a single
> integer `N` dominating `d_p + p` for every `p` whose column can be nonzero: the `d` produced
> here is the threshold above which `W_q` has no points, got from the fibre bound of choice (3),
> the domination is asserted for the `p` with `p + 1 ≤ d`, and `N` is the maximum of `d_p + p`
> over those.
>
> This is the integer at which [Stacks, Tag 072C] asserts the cohomology of every quasi-coherent
> module to vanish; that vanishing, from these choices, is
> `AlgebraicGeometry.Space.isZero_sheafH_of_data_072C`. What is proved here is that the choices
> (1)–(5) determine such an `N`.

```lean
theorem exists_bound_affine_etale_surjective_cover_diagonalComplementQuotient
    (hqc : IsQuasiCompactSpace B S hS Y)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ Y) :
    ∃ (U : BigFppfOver B S hS) (g : yoneda.obj U ⟶ Y)
        (het : IsEtale B S hS g) (hsep : IsSeparated B S hS g)
        (d : ℕ) (N : ℤ),
      IsAffine ((BigFppfOver.toScheme B S hS).obj U) ∧
        (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        HasUniversallyBoundedFibers B S hS U g ∧
        (∀ q : ℕ, d < q → IsEmpty (points B S hS
          (SpacesEtale.underlying B S hS ⟨Y, hY⟩
            (SpacesEtale.diagonalComplement B S hS ⟨Y, hY⟩
              (SpacesEtale.chartObj B S hS ⟨Y, hY⟩ U g het) q hsep)).obj)) ∧
        ∀ p : ℕ, ∃ (V : BigFppfOver B S hS)
            (f : yoneda.obj V ⟶ (SpacesEtale.diagonalComplementQuotient B S hS
              ⟨Y, hY⟩ (SpacesEtale.chartObj B S hS ⟨Y, hY⟩ U g het)
              (p + 1) hsep).obj) (dp : ℤ),
          IsAffine ((BigFppfOver.toScheme B S hS).obj V) ∧
            (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
              (BigFppfOver.toScheme B S hS)).presheaf f ∧
            IsEtale B S hS f ∧
            BoundsFibreDegrees B S hS V f dp ∧
            (p + 1 ≤ d → dp + p ≤ N)
```

**`AlgebraicGeometry.Space.isZero_sheafH_of_data_072C`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/QuasiSeparatedVanishing.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/QuasiSeparatedVanishing.lean#L226). The attribute's comment: “the conclusion: for X a quasi-compact and quasi-separated algebraic space over a scheme S, given the choices (1)-(5) -- an affine U with a surjective etale U -> X, an integer d bounding its fibre degrees, and for each p <= d an affine V_p with a surjective etale V_p -> U_p = W_{p+1}/S_{p+1} and an integer d_p bounding its fibre degrees -- the cohomology H^q(X, F) vanishes for every quasi-coherent module F and every q at least the source's max(d_p + p) over 0 <= p <= d. The cohomology is the sheaf cohomology of the underlying abelian sheaf of F on the spaces-etale site of X”.

> **The vanishing of [Stacks, Tag 072C] from the choices (1)–(5).**  Let `S` be a scheme and
> let `X` be a quasi-compact and quasi-separated
> algebraic space over `S`.  Choose an affine scheme `U`, a surjective étale morphism `f : U ⟶ X`
> and an integer `d` bounding the degrees of the fibres of `f`; for each `p` with `0 ≤ p ≤ d`
> choose an affine scheme `V_p`, a surjective étale morphism `V_p ⟶ U_p` onto the quotient
> `U_p = W_{p+1}/S_{p+1}` of [Stacks, Tag 0726], and an integer `d_p` bounding the degrees of its
> fibres.  Then
>
> `H^q(X, ℱ) = 0`
>
> for every quasi-coherent `𝒪_X`-module `ℱ` and every `q` at least `max (d_p + p)`.
>
> The bound is the source's, formed as the supremum of `d_p + p` over `0 ≤ p ≤ d`.  The vanishing is
> read on the spaces-étale site of `X`, as the sheaf cohomology of the underlying abelian sheaf of
> `ℱ`; the cohomological descent that identifies that with the derived functors of global sections
> on modules is [Stacks, Tag 03FD].
>
> The one input of the recursion that the recursion cannot supply is the positive-degree vanishing
> on an *affine* algebraic space — the clause of [Stacks, Tag 03DW] in positive degrees,
> `AlgebraicGeometry.Space.SpacesEtale.AffineSerreVanishing`.  It is supplied here by
> `AlgebraicGeometry.Space.SpacesEtale.affineSerreVanishing_of_isZero_cechCohomology`, the
> Čech-to-derived criterion of [Stacks, Tag 03F9] on the cofinal affine objects of the small étale
> site, whose Čech hypothesis is
> `AlgebraicGeometry.Space.SmallEtale.isZero_cechCohomology_comparisonCoefficients_forall`.

```lean
theorem isZero_sheafH_of_data_072C
    (X : AlgebraicSpaces B S hS)
    (hqc : IsQuasiCompactSpace B S hS X.obj)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X.obj)
    (U : BigFppfOver B S hS) (hU : IsAffine ((BigFppfOver.toScheme B S hS).obj U))
    (f : yoneda.obj U ⟶ X.obj) (hf : IsEtale B S hS f) (hfsurj : IsSurjective B S hS f)
    (d : ℕ) (hd : BoundsFibreDegrees B S hS U f (d : ℤ)) (dp : ℕ → ℕ)
    (hdata : ∀ (hsep : IsSeparated B S hS f) (p : ℕ), p ≤ d →
      ∃ (V : BigFppfOver B S hS)
        (g : yoneda.obj V ⟶ (SpacesEtale.diagonalComplementQuotient B S hS X
          (SpacesEtale.chartObj B S hS X U f hf) (p + 1) hsep).obj),
        IsAffine ((BigFppfOver.toScheme B S hS).obj V) ∧
          IsEtale B S hS g ∧ IsSurjective B S hS g ∧
          BoundsFibreDegrees B S hS V g (dp p : ℤ))
    (M : SheafOfModules.{u + 1} (SpacesEtale.spacesEtaleRing B S hS X))
    (hM : M.IsQuasicoherentOnSite)
    (n : ℕ) (hn : (Finset.range (d + 1)).sup (fun p => dp p + p) ≤ n) :
    IsZero (AddCommGrpCat.of (Sheaf.H
      ((SheafOfModules.toSheaf.{u + 1} (SpacesEtale.spacesEtaleRing B S hS X)).obj M) n))
```

**`AlgebraicGeometry.Space.exists_forall_isZero_sheafH_of_isQuasiCompactSpace_072C`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/QuasiSeparatedVanishing.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/QuasiSeparatedVanishing.lean#L292). The attribute's comment: “the tag end to end, over an arbitrary base scheme S: for X a quasi-compact and quasi-separated algebraic space over S there is a single degree N beyond which the sheaf cohomology on the spaces-etale site of X of the underlying abelian sheaf of every quasi-coherent module vanishes. N is constructed in the proof as the source's max(d_p + p) for the choices (1)-(5) made there; the statement quantifies N existentially, and the identification of N with that maximum is stated at AlgebraicGeometry.Space.isZero_sheafH_of_data_072C”.

> **[Stacks, Tag 072C], end to end.**  Let `S` be a scheme and let `X` be a quasi-compact and
> quasi-separated algebraic space over `S`.  Then there is a single degree `N` beyond which the
> cohomology of `X` with quasi-coherent coefficients vanishes:
>
> `H^q(X, ℱ) = 0` for every quasi-coherent `𝒪_X`-module `ℱ` and every `q ≥ N`.
>
> The base is an arbitrary scheme, as in the source.  This is the five choices of the tag,
> `AlgebraicGeometry.Space.exists_affine_etale_surjective_cover_diagonalComplementQuotient`, fed
> into the vanishing they give,
> `AlgebraicGeometry.Space.isZero_sheafH_of_data_072C`, with `N` the source's `max (d_p + p)`
> over `0 ≤ p ≤ d`; the two fibre bounds are produced as integers by
> `AlgebraicGeometry.Space.HasUniversallyBoundedFibers` and enlarged to natural numbers by
> `AlgebraicGeometry.Space.BoundsFibreDegrees.mono`.  The uniformity in `ℱ` — one degree for all
> quasi-coherent coefficients at once — is what the tag asserts and is what makes the Euler
> characteristic of a coherent module a finite alternating sum.

```lean
theorem exists_forall_isZero_sheafH_of_isQuasiCompactSpace_072C
    (X : AlgebraicSpaces B S hS)
    (hqc : IsQuasiCompactSpace B S hS X.obj)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X.obj) :
    ∃ N : ℕ, ∀ (M : SheafOfModules.{u + 1} (SpacesEtale.spacesEtaleRing B S hS X)),
      M.IsQuasicoherentOnSite → ∀ n : ℕ, N ≤ n →
        IsZero (AddCommGrpCat.of (Sheaf.H
          ((SheafOfModules.toSheaf.{u + 1} (SpacesEtale.spacesEtaleRing B S hS X)).obj M) n))
```

**`AlgebraicGeometry.Space.exists_affine_etale_surjective_cover_hasUniversallyBoundedFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologicalDimension.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologicalDimension.lean#L94). The attribute's comment: “parts (1)-(3): an affine scheme U, a surjective étale morphism U ⟶ X, and an integer bounding the degrees of its fibres”.

> **The choices (1)–(3) of Stacks 072C.** A quasi-compact, quasi-separated algebraic space
> carries a surjective étale morphism from an affine scheme whose fibres are universally bounded
> in the sense of Stacks 03JL.

```lean
theorem exists_affine_etale_surjective_cover_hasUniversallyBoundedFibers
    (hqc : IsQuasiCompactSpace B (Spec (.of A)) hA X)
    (hqs : IsAbsolutelyQuasiSeparated B (Spec (.of A)) hA hZ X) :
    ∃ (U : BigFppfOver B (Spec (.of A)) hA) (g : yoneda.obj U ⟶ X),
      IsAffine ((BigFppfOver.toScheme B (Spec (.of A)) hA).obj U) ∧
        (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B (Spec (.of A)) hA)).presheaf g ∧
        IsEtale B (Spec (.of A)) hA g ∧
        HasUniversallyBoundedFibers B (Spec (.of A)) hA U g
```

**`AlgebraicGeometry.Space.exists_forall_isZero_cohomologyOverBase_of_isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologicalDimension.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologicalDimension.lean#L119). The attribute's comment: “the conclusion, uniformly in the quasi-coherent module, with Stacks 072B carried as the hypothesis h072B: the alternating Čech spectral sequence of Stacks 0728 and the quotients U_p that both its proof and the reduction to the separated case need are absent”.

> **Stacks 072C.** On a quasi-compact, quasi-separated algebraic space over `Spec A` there is
> a single degree `N` beyond which the cohomology over `A` of every quasi-coherent `𝒪_X`-module
> vanishes.

```lean
theorem exists_forall_isZero_cohomologyOverBase_of_isQuasiCompactSpace
    (hqc : IsQuasiCompactSpace B (Spec (.of A)) hA X)
    (hqs : IsAbsolutelyQuasiSeparated B (Spec (.of A)) hA hZ X)
    (h072B : ∀ (U : BigFppfOver B (Spec (.of A)) hA) (g : yoneda.obj U ⟶ X),
      IsAffine ((BigFppfOver.toScheme B (Spec (.of A)) hA).obj U) →
      (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B (Spec (.of A)) hA)).presheaf g →
      IsEtale B (Spec (.of A)) hA g →
      HasUniversallyBoundedFibers B (Spec (.of A)) hA U g →
      ∃ N : ℕ, ∀ F : Modules.{u, max (u + 1) w} B (Spec (.of A)) hA X hX,
        F.IsQuasicoherentOnSite → ∀ q, N ≤ q →
          IsZero (cohomologyOverBase.{u, w} A B hA X hX F q)) :
    ∃ N : ℕ, ∀ F : Modules.{u, max (u + 1) w} B (Spec (.of A)) hA X hX,
      F.IsQuasicoherentOnSite → ∀ q, N ≤ q →
        IsZero (cohomologyOverBase.{u, w} A B hA X hX F q)
```

**`AlgebraicGeometry.Space.exists_affine_etale_surjective_cover_hasUniversallyBoundedFibers'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologicalDimensionGeneralBase.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologicalDimensionGeneralBase.lean#L60). The attribute's comment: “parts (1)-(3): an affine scheme U, a surjective étale morphism U ⟶ X, and an integer bounding the degrees of its fibres, for X a quasi-compact and quasi-separated algebraic space over an arbitrary base scheme S”.

> **The choices (1)–(3) of Stacks 072C.** A quasi-compact, quasi-separated algebraic space
> over an arbitrary base scheme `S` carries a surjective étale morphism from an affine scheme
> whose fibres are universally bounded in the sense of Stacks 03JL.
>
> The base is an arbitrary scheme, as in the source: nothing in the two inputs — the affine étale
> chart of [Stacks, Tag 03H6] and the chain `(η) ⇒ (ζ) ⇒ (ε) ⇒ (δ)` of [Stacks, Tag 03JX] —
> restricts it, and quasi-separatedness is taken in the absolute form of [Stacks, Tag 03BS]
> part (3), which does not mention `S` either.

```lean
theorem exists_affine_etale_surjective_cover_hasUniversallyBoundedFibers'
    (hqc : IsQuasiCompactSpace B S hS X)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X) :
    ∃ (U : BigFppfOver B S hS) (g : yoneda.obj U ⟶ X),
      IsAffine ((BigFppfOver.toScheme B S hS).obj U) ∧
        (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        IsEtale B S hS g ∧
        HasUniversallyBoundedFibers B S hS U g
```

**`AlgebraicGeometry.Space.exists_forall_isZero_rightDerived_globalSectionsFunctor_of_isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologicalDimensionUniform.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologicalDimensionUniform.lean#L108). The attribute's comment: “the uniform vanishing degree, for every quasi-coherent module; the value max (d_p + p) of the degree is not part of this statement”.

> **Stacks 072C, the uniform vanishing.**  On a quasi-compact and quasi-separated algebraic
> space `X` there is a single degree `N` beyond which the cohomology of every quasi-coherent
> `𝒪_X`-module vanishes: `Hᑫ(X, 𝓕) = 0` for `q ≥ N`.

```lean
theorem exists_forall_isZero_rightDerived_globalSectionsFunctor_of_isQuasiCompactSpace
    (X : AlgebraicSpaces B S hS) (hqc : IsQuasiCompactSpace B S hS X.1)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1) :
    ∃ N : ℕ, ∀ F : Modules.{u, u} B S hS X.1 X.2, F.IsQuasicoherentOnSite → ∀ q, N ≤ q →
      IsZero (((globalSectionsFunctor.{u + 1, u, u, u}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (smallEtaleRingedSite B S hS X.1 X.2).O)).rightDerived q).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.7, Tag 0729](https://stacks.math.columbia.edu/tag/0729)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
