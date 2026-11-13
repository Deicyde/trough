---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.ApproximationHolds, AlgebraicGeometry.Space.ApproximationByPerfectComplexes, AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_of_cohomologySupportedOn, AlgebraicGeometry.Space.isPerfect_rightAdjoint_edsDerivedRestrictEtale_of_cohomologySupportedOn, AlgebraicGeometry.Space.approximationHolds_of_isElementaryDistinguishedSquare, AlgebraicGeometry.Space.approximationHolds_of_approximationHolds_edsEtale, AlgebraicGeometry.Space.approximationHolds_of_affineCover, AlgebraicGeometry.Space.approximationByPerfectComplexes_of_affine
statement: formalized
proof: formalized
---

# 75.14 Approximation by perfect complexes

Section 75.14 of the Stacks Project, [Tag 08HH](https://stacks.math.columbia.edu/tag/08HH). 7 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08HI, a definition

[Tag 08HI](https://stacks.math.columbia.edu/tag/08HI) in the Stacks Project.

**`AlgebraicGeometry.Space.ApproximationHolds`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/Approximation.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/Approximation.lean#L59).

> *Approximation holds* for the triple `(T, E, m)`: some perfect object of `D(𝒪_F)` supported on
> `T` maps to `E` by a map inducing isomorphisms on cohomology in every degree above `m` and a
> surjection in degree `m`.

```lean
noncomputable abbrev ApproximationHolds (T : Set (points B S hS F))
    (E : QuasicoherentDerivedCategory.{u, m} B S hS F hF) (m : ℤ) : Prop
```

## Tag 08HJ, a definition

[Tag 08HJ](https://stacks.math.columbia.edu/tag/08HJ) in the Stacks Project.

**`AlgebraicGeometry.Space.ApproximationByPerfectComplexes`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/Approximation.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/Approximation.lean#L74).

> *Approximation by perfect complexes holds* on `F`: for every closed `T ⊆ |F|` whose open
> complement has quasi-compact inclusion there is an integer `r` such that approximation holds for
> every triple `(T, E, m)` in which `E` is `(m - r)`-pseudo-coherent and `Hⁱ(E)` is supported on `T`
> for every `i ≥ m - r`.

```lean
noncomputable abbrev ApproximationByPerfectComplexes : Prop
```

## Tag 08HK, a lemma

[Tag 08HK](https://stacks.math.columbia.edu/tag/08HK) in the Stacks Project.

**`AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PushforwardOfSupportedPerfectCanonical.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PushforwardOfSupportedPerfectCanonical.lean#L131). The attribute's comment: “Rj\_*E is perfect in D(O\_X) for an elementary distinguished square and E perfect on V supported on j^\{-1}T”.

> **Stacks 08HK.**  Let `S` be a scheme, let `(U ⊆ X, j : V ⟶ X)` be an elementary
> distinguished square of algebraic spaces over `S`, and set `T = |X| \ |U|`.  Let `E` be a
> perfect object of `D(𝒪_V)` supported on `j^{-1}T`.  Then `Rj_*E` is a perfect object of
> `D(𝒪_X)`.
>
> Perfectness is local on `X_étale` along the two morphisms of the square, and `Rj_*E` is `j_!E`,
> whose restriction to `U` vanishes and whose restriction to `V` is the perfect `E`.

```lean
theorem isPerfect_derivedModulePushforward_of_cohomologySupportedOn
    (E : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1
      (edsEtale B S hS hsq).2))
    (hperf : (smallEtaleRingedSite B S hS (edsEtale B S hS hsq).1
      (edsEtale B S hS hsq).2).IsPerfect E)
    (hE : CohomologySupportedOn B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
      (edsEtalePreimageComplementPoints B S hS hsq) E) :
    (smallEtaleRingedSite B S hS W.1 W.2).IsPerfect
      ((derivedModulePushforward B S hS (edsEtaleHom B S hS hsq)).obj E)
```

**`AlgebraicGeometry.Space.isPerfect_rightAdjoint_edsDerivedRestrictEtale_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPushforwardPerfect.lean, line 434](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPushforwardPerfect.lean#L434).

> **Stacks 08HK.**  Let `S` be a scheme, let `(U ⊆ X, j : V ⟶ X)` be an elementary
> distinguished square of algebraic spaces over `S`, and set `T = |X| \ |U|`.  Let `E` be a
> perfect object of `D(𝒪_V)` supported on `j⁻¹(T)`.  Then `Rj_*E` is a perfect object of
> `D(𝒪_X)`.
>
> `Rj_*` is a right adjoint of derived restriction `(-)|_V`, given together with its adjunction,
> as in `AlgebraicGeometry.Space.isPerfect_derivedPushforward_of_cohomologySupportedOn`; this
> determines it up to a unique compatible isomorphism.  The proof is the source's: perfectness is
> local on `X_étale` (`AlgebraicGeometry.Space.isPerfect_of_isPerfect_eds`), the restriction of
> `Rj_*E` to `U` vanishes and its restriction to `V` is `E` (Stacks 08GG (2)(b)).

```lean
theorem isPerfect_rightAdjoint_edsDerivedRestrictEtale_of_cohomologySupportedOn
    (E : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2))
    (hperf : (smallEtaleRingedSite B S hS (edsEtale B S hS hsq).1
      (edsEtale B S hS hsq).2).IsPerfect E)
    (hE : CohomologySupportedOn B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
      (edsEtalePreimageComplementPoints B S hS hsq) E) :
    (smallEtaleRingedSite B S hS W.1 W.2).IsPerfect (RpushD.obj E)
```

## Tag 08HL, a lemma

[Tag 08HL](https://stacks.math.columbia.edu/tag/08HL) in the Stacks Project.

**`AlgebraicGeometry.Space.approximationHolds_of_isElementaryDistinguishedSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationAcrossSquare.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationAcrossSquare.lean#L90).

> **Stacks 08HL.**  Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished square of
> algebraic spaces over a scheme `S`, let `T ⊆ |X| \ |U|` and let `(T, E, m)` be a triple as in
> Stacks 08HI.  If
>
> 1. approximation holds for `(j^{-1}T, E|_V, m)`, and
> 2. the sheaves `Hⁱ(E)` for `i ≥ m` are supported on `T`,
>
> then approximation holds for `(T, E, m)`.

```lean
theorem approximationHolds_of_isElementaryDistinguishedSquare
    (T : Set (points B S hS W.1)) (hTU : T ⊆ edsComplementPoints B S hS Uo)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS W.1 W.2) (m : ℤ)
    (happrox : ApproximationHolds B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
      (pointsMap B S hS (edsEtale B S hS hsq).1 (edsEtaleHom B S hS hsq).hom ⁻¹' T)
      ((quasicoherentDerivedEtalePullback B S hS (edsEtaleHom B S hS hsq)
        (isEtale_edsEtaleHom B S hS hsq)).obj E) m)
    (hsupp : ∀ i : ℤ, m ≤ i →
      supportOfSheaf B S hS W.1
        ((SheafOfModules.toSheaf (etaleRingSheaf B S hS W)).obj
          ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS W.1 W.2) i).obj E.obj)) ⊆ T) :
    ApproximationHolds B S hS W.1 W.2 T E m
```

**`AlgebraicGeometry.Space.approximationHolds_of_approximationHolds_edsEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationExtensionByZero.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationExtensionByZero.lean#L204). The attribute's comment: “for an elementary distinguished square (U ⊆ X, j : V ⟶ X), T ⊆ |X| \ |U| and a triple (T, E, m): approximation for (j^\{-1}T, E|\_V, m) with E|\_V = quasicoherentDerivedEtalePullback of E, together with H^i(E) supported on T for i ≥ m, gives approximation for (T, E, m); nothing else is bound. T is any subset of |X| \ |U|, closedness being unused”.

> **Stacks 08HL.**  Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished square of
> algebraic spaces over a scheme `S`, let `T ⊆ |X| \ |U|` and let `(T, E, m)` be a triple as in
> Stacks 08HI.  If
>
> 1. approximation holds for `(j^{-1}T, E|_V, m)`, and
> 2. the sheaves `Hⁱ(E)` for `i ≥ m` are supported on `T`,
>
> then approximation holds for `(T, E, m)`.
>
> The approximation produced is `j_!P ⟶ j_!(E|_V) ⟶ E` for an approximation `P ⟶ E|_V` of the
> restricted triple; `j_!P = Rj_*P` by Stacks 08GG part (2) clause (c).

```lean
theorem approximationHolds_of_approximationHolds_edsEtale
    (T : Set (points B S hS W.1)) (hTU : T ⊆ edsComplementPoints B S hS Uo)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS W.1 W.2) (m : ℤ)
    (happrox : ApproximationHolds B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
      (pointsMap B S hS (edsEtale B S hS hsq).1 (edsEtaleHom B S hS hsq).hom ⁻¹' T)
      ((quasicoherentDerivedEtalePullback B S hS (edsEtaleHom B S hS hsq)
        (isEtale_edsEtaleHom B S hS hsq)).obj E) m)
    (hsupp : ∀ i : ℤ, m ≤ i →
      supportOfSheaf B S hS W.1
        ((SheafOfModules.toSheaf
            ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS W.1 W.2).O))).obj
          ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS W.1 W.2) i).obj E.obj)) ⊆ T) :
    ApproximationHolds B S hS W.1 W.2 T E m
```

## Tag 08HM, a lemma

[Tag 08HM](https://stacks.math.columbia.edu/tag/08HM) in the Stacks Project.

**`AlgebraicGeometry.Space.approximationHolds_of_affineCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationAffine.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationAffine.lean#L80). The attribute's comment: “first assertion: for X an algebraic space representable by an affine scheme, approximation holds for every triple (T, E, m) such that there exists an integer r ≥ 0 with E m-pseudo-coherent, H^i(E) supported on T for i ≥ m - r + 1 and X \ T a union of r affine opens”.

> **Stacks 08HM.**  Let `S` be a scheme and let `X` be an algebraic space over `S` which is
> representable by an affine scheme.  Then approximation holds (Stacks 08HI) for every triple
> `(T, E, m)` for which there exists an integer `r ≥ 0` such that
>
> 1. `E` is `m`-pseudo-coherent,
> 2. `Hⁱ(E)` is supported on `T` for `i ≥ m - r + 1`,
> 3. `X ∖ T` is the union of `r` affine opens `V₁, …, V_r` of `X`.
>
> This is `AlgebraicGeometry.Space.approximationHolds_of_isAffineSpace`, applied to the integer and
> the affine opens provided.

```lean
theorem approximationHolds_of_affineCover (hXa : IsAffineSpace B S hS X)
    (T : Set (points B S hS X)) (E : QuasicoherentDerivedCategory.{u, u} B S hS X hX) (m : ℤ)
    (h : ∃ r : ℕ,
      (smallEtaleRingedSite B S hS X hX).IsPseudoCoherentFrom E.obj m ∧
      (∀ i : ℤ, m - (r : ℤ) + 1 ≤ i →
        supportOfSheaf B S hS X
          ((SheafOfModules.toSheaf
              ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X hX).O))).obj
            ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X hX) i).obj E.obj)) ⊆ T) ∧
      ∃ V : Fin r → {G : Subfunctor X // IsOpenSubspace B S hS G},
        (∀ k, IsAffineSpace B S hS (V k).1.toFunctor) ∧
        ⋃ k, Set.range (pointsMap B S hS (V k).1.toFunctor (V k).1.ι) = Tᶜ) :
    ApproximationHolds B S hS X hX T E m
```

**`AlgebraicGeometry.Space.approximationByPerfectComplexes_of_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationAffine.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationAffine.lean#L102). The attribute's comment: “second assertion: approximation by perfect complexes holds on an algebraic space representable by an affine scheme”.

> **The "in particular" of Stacks 08HM**: approximation by perfect complexes (Stacks 08HJ)
> holds on an algebraic space representable by an affine scheme.
>
> This is `AlgebraicGeometry.Space.approximationByPerfectComplexes_of_isAffineSpace`.

```lean
theorem approximationByPerfectComplexes_of_affine (hXa : IsAffineSpace B S hS X) :
    ApproximationByPerfectComplexes.{u, u} B S hS X hX
```

**`AlgebraicGeometry.Space.approximationHolds_of_isAffineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationIso.lean, line 413](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationIso.lean#L413). The attribute's comment: “first assertion: approximation holds for every triple (T, E, m) with E m-pseudo-coherent, H^i(E) supported on T for i ≥ m - r + 1 and X \ T a union of r affine opens, for X an algebraic space representable by an affine scheme”.

> **Stacks 08HM.**  Let `S` be a scheme and let `X` be an algebraic space over `S` which is
> representable by an affine scheme.  Then approximation holds (Stacks 08HI) for every triple
> `(Z, E, m)` for which there is an integer `r ≥ 0` with
>
> 1. `E` `m`-pseudo-coherent,
> 2. `Hⁱ(E)` supported on `Z` for `i ≥ m - r + 1`,
> 3. `X ∖ Z` the union of `r` affine opens `V₁, …, V_r` of `X`.
>
> The case `X = h_U` is `AlgebraicGeometry.Space.approximationHolds_of_isAffine_represented`; the
> general case is transported along an isomorphism `X ≅ h_U`
> (`AlgebraicGeometry.Space.approximationHolds_of_iso`).

```lean
theorem approximationHolds_of_isAffineSpace (hXa : IsAffineSpace B S hS F)
    (Z : Set (points B S hS F))
    (E : QuasicoherentDerivedCategory.{u, u} B S hS F hF) (m : ℤ) (r : ℕ)
    (hpc : (smallEtaleRingedSite B S hS F hF).IsPseudoCoherentFrom E.obj m)
    (hsupp : ∀ i : ℤ, m - (r : ℤ) + 1 ≤ i →
      supportOfSheaf B S hS F
        ((SheafOfModules.toSheaf
            ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O))).obj
          ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS F hF) i).obj E.obj)) ⊆ Z)
    (V : Fin r → {G : Subfunctor F // IsOpenSubspace B S hS G})
    (hV : ∀ k, IsAffineSpace B S hS (V k).1.toFunctor)
    (hcover : ⋃ k, Set.range (pointsMap B S hS (V k).1.toFunctor (V k).1.ι) = Zᶜ) :
    ApproximationHolds B S hS F hF Z E m
```

**`AlgebraicGeometry.Space.approximationByPerfectComplexes_of_isAffineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationIso.lean, line 445](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationIso.lean#L445). The attribute's comment: “second assertion: approximation by perfect complexes holds on an algebraic space representable by an affine scheme”.

> **The "in particular" of Stacks 08HM**: approximation by perfect complexes (Stacks 08HJ)
> holds on an algebraic space representable by an affine scheme.

```lean
theorem approximationByPerfectComplexes_of_isAffineSpace (hXa : IsAffineSpace B S hS F) :
    ApproximationByPerfectComplexes.{u, u} B S hS F hF
```

**`AlgebraicGeometry.Space.approximationHolds_and_approximationByPerfectComplexes_of_isAffineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationIsoTag.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationIsoTag.lean#L60).

> **Stacks 08HM.**  Let `S` be a scheme and let `X` be an algebraic space over `S` which is
> representable by an affine scheme.  Then
>
> 1. approximation holds (Stacks 08HI) for every triple `(Z, E, m)` for which there is an integer
>    `r ≥ 0` with
>    1. `E` `m`-pseudo-coherent,
>    2. `Hⁱ(E)` supported on `Z` for `i ≥ m - r + 1`,
>    3. `X ∖ Z` the union of `r` affine opens `V₁, …, V_r` of `X`;
> 2. in particular, approximation by perfect complexes (Stacks 08HJ) holds for `X`.

```lean
theorem approximationHolds_and_approximationByPerfectComplexes_of_isAffineSpace
    (hXa : IsAffineSpace B S hS F) :
    (∀ (Z : Set (points B S hS F))
      (E : QuasicoherentDerivedCategory.{u, u} B S hS F hF) (m : ℤ) (r : ℕ),
      (smallEtaleRingedSite B S hS F hF).IsPseudoCoherentFrom E.obj m →
      (∀ i : ℤ, m - (r : ℤ) + 1 ≤ i →
        supportOfSheaf B S hS F
          ((SheafOfModules.toSheaf
              ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O))).obj
            ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS F hF) i).obj E.obj)) ⊆ Z) →
      ∀ (V : Fin r → {G : Subfunctor F // IsOpenSubspace B S hS G}),
      (∀ k, IsAffineSpace B S hS (V k).1.toFunctor) →
      ⋃ k, Set.range (pointsMap B S hS (V k).1.toFunctor (V k).1.ι) = Zᶜ →
      ApproximationHolds B S hS F hF Z E m) ∧
    ApproximationByPerfectComplexes.{u, u} B S hS F hF
```

## Tag 08HN, a lemma

[Tag 08HN](https://stacks.math.columbia.edu/tag/08HN) in the Stacks Project.

**`AlgebraicGeometry.Space.approximationByPerfectComplexes_of_isElementaryDistinguishedSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationSquare.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationSquare.lean#L136).

> **Stacks 08HN.**  Let `S` be a scheme and let `(U ⊆ X, j : V ⟶ X)` be an elementary
> distinguished square of algebraic spaces over `S`, with `U` quasi-compact, `V` affine and
> `U ×_X V` quasi-compact.  If approximation by perfect complexes holds on `U`, then approximation
> by perfect complexes holds on `X`.

```lean
theorem approximationByPerfectComplexes_of_isElementaryDistinguishedSquare
    {X V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (U : Subfunctor X) (f : V ⟶ X)
    (hsq : IsElementaryDistinguishedSquare B S hS hX U f)
    (hUqc : IsQuasiCompactSpace B S hS U.toFunctor)
    (hVaff : IsAffineSpace B S hS V)
    (hUVqc : IsQuasiCompactSpace B S hS (U.preimage f).toFunctor)
    (hU : ApproximationByPerfectComplexes.{u, u} B S hS U.toFunctor hsq.isOpenSubspace.1) :
    ApproximationByPerfectComplexes.{u, u} B S hS X hX
```

## Tag 08HP, a theorem

[Tag 08HP](https://stacks.math.columbia.edu/tag/08HP) in the Stacks Project.

**`AlgebraicGeometry.Space.approximationByPerfectComplexes_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationQcqs.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationQcqs.lean#L62).

> **Stacks 08HP.**  Let `S` be a scheme and let `X` be a quasi-compact and quasi-separated
> algebraic space over `S`.  Then approximation by perfect complexes holds on `X`.

```lean
theorem approximationByPerfectComplexes_of_qcqs (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (hXqc : IsQuasiCompactSpace B S hS X) (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X) :
    ApproximationByPerfectComplexes.{u, u} B S hS X hX
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.14, Tag 08HH](https://stacks.math.columbia.edu/tag/08HH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
