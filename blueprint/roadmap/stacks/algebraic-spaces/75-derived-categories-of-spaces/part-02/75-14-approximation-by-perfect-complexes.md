---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.ApproximationHolds, AlgebraicGeometry.Space.ApproximationByPerfectComplexes, AlgebraicGeometry.Space.isPerfect_derivedPushforward_of_isPerfect_of_cohomologySupportedOn, AlgebraicGeometry.Space.isPerfect_derivedPushforward_of_cohomologySupportedOn, AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_of_cohomologySupportedOn, AlgebraicGeometry.Space.isPerfect_rightAdjoint_edsDerivedRestrictEtale_of_cohomologySupportedOn, AlgebraicGeometry.Space.approximationHolds_of_isElementaryDistinguishedSquare, AlgebraicGeometry.Space.approximationHolds_of_approximationHolds_edsEtale
statement: formalized
proof: formalized
---

# 75.14 Approximation by perfect complexes

Section 75.14 of the Stacks Project, [Tag 08HH](https://stacks.math.columbia.edu/tag/08HH). 7 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08HI, a definition

[Tag 08HI](https://stacks.math.columbia.edu/tag/08HI) in the Stacks Project.

**`AlgebraicGeometry.Space.ApproximationHolds`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/Approximation.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/Approximation.lean#L59).

> *Approximation holds* for the triple `(T, E, m)`: some perfect object of `D(𝒪_F)` supported on
> `T` maps to `E` by a map inducing isomorphisms on cohomology in every degree above `m` and a
> surjection in degree `m`.

```lean
noncomputable abbrev ApproximationHolds (T : Set (points B S hS F))
    (E : QuasicoherentDerivedCategory.{u, m} B S hS F hF) (m : ℤ) : Prop
```

## Tag 08HJ, a definition

[Tag 08HJ](https://stacks.math.columbia.edu/tag/08HJ) in the Stacks Project.

**`AlgebraicGeometry.Space.ApproximationByPerfectComplexes`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/Approximation.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/Approximation.lean#L74).

> *Approximation by perfect complexes holds* on `F`: for every closed `T ⊆ |F|` whose open
> complement has quasi-compact inclusion there is an integer `r` such that approximation holds for
> every triple `(T, E, m)` in which `E` is `(m - r)`-pseudo-coherent and `Hⁱ(E)` is supported on `T`
> for every `i ≥ m - r`.

```lean
noncomputable abbrev ApproximationByPerfectComplexes : Prop
```

## Tag 08HK, a lemma

[Tag 08HK](https://stacks.math.columbia.edu/tag/08HK) in the Stacks Project.

**`AlgebraicGeometry.Space.isPerfect_derivedPushforward_of_isPerfect_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationExtensionByZero.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationExtensionByZero.lean#L107). The attribute's comment: “Rj\_*E is a perfect object of D(O\_X) for E perfect on V and supported on j^\{-1}T, T = |X| \ |U|, for an elementary distinguished square and nothing else bound; Rj\_* is any right adjoint of derived restriction, which pins it”.

> **Stacks 08HK.**  Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished square of algebraic
> spaces over a scheme `S` and set `T = |X| \ |U|`.  If `E` is a perfect object of `D(𝒪_V)`
> supported on `j^{-1}T`, then `Rj_*E` is a perfect object of `D(𝒪_X)`.
>
> `Rj_*` is any right adjoint of derived restriction, which pins it; a total right derived functor
> of the direct image is one, by
> `AlgebraicGeometry.Space.etaleModulePullbackDerivedPushforwardAdjunction`.

```lean
theorem isPerfect_derivedPushforward_of_isPerfect_of_cohomologySupportedOn
    {RpushD : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1
        (edsEtale B S hS hsq).2) ⥤ DerivedCategory (Modules.{u, u} B S hS W.1 W.2)}
    (adjPush : edsDerivedRestrictEtale B S hS hsq ⊣ RpushD)
    (E : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2))
    (hE : (smallEtaleRingedSite B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2).IsPerfect E)
    (hEs : CohomologySupportedOn B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
      (edsEtalePreimageComplementPoints B S hS hsq) E) :
    (smallEtaleRingedSite B S hS W.1 W.2).IsPerfect (RpushD.obj E)
```

**`AlgebraicGeometry.Space.isPerfect_derivedPushforward_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PushforwardOfSupportedPerfect.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PushforwardOfSupportedPerfect.lean#L250). The attribute's comment: “Rj\_*E is a perfect object of D(O\_X) for E perfect on V and supported on j^\{-1}T. CONDITIONAL on three named hypotheses, NONE of which is proved in the library, and which together are the whole of the source's argument apart from the two perfectness facts proved in this file. (i) hlocal: perfectness is local on X\_etale along \{U, V}, the first sentence of the source's proof. The library's form of it, isPerfect\_of\_locally (Tag 08G5 through Tag 08G6 part (1)), is stated for a RingedSite.\{u, u, 0} and the small etale ringed site of an algebraic space is a RingedSite.\{u + 1, u, u}, so it does not apply; the obstruction is inherited from Tag 08FR, which needs the objects and the morphisms of the site in one universe, and is NOT a missing covering. (ii) h2b: clause (2)(b) of Tag 08GG, that the counit (Rj\_*E)|\_V to E is an isomorphism for supported E. SupportedOnComplement.lean proves clauses (1)(a), (1)(b) and (2)(c) and records that (2)(a) and (2)(b) are unproved, the source getting them by a base change of the square to V that the library does not carry. (iii) hUzero: the vanishing of (Rj\_*E)|\_U, which the source gets from E|\_\{V minus j^\{-1}T} = 0 and Tag 08GE; the first half needs H^i(E|\_Y) = H^i(E)|\_Y, unavailable because Mathlib proves no commutation of Functor.mapDerivedCategory with the homology functors, the same gap as the hypothesis hvan there. Tag 08GE itself is proved. What IS proved: the source's deduction, with h2b and hUzero taking the support hypothesis as antecedent so that it is genuinely consumed. Rj\_* enters as a right adjoint of derived restriction together with its adjunction, as in Tag 08HA”.

> **Stacks 08HK.**  Let `S` be a scheme, let `(U ⊆ X, j : V ⟶ X)` be an elementary
> distinguished square of algebraic spaces over `S`, and set `T = |X| \ |U|`.  Let `E` be a
> perfect object of `D(𝒪_V)` supported on `j^{-1}T`.  Then `Rj_*E` is a perfect object of
> `D(𝒪_X)`.
>
> This is the source's own two-sentence proof, granted its three inputs, each of which is a named
> hypothesis here because the library does not have it: `hlocal` is that perfectness is local on
> `X_étale`, `h2b` is clause (2)(b) of Stacks 08GG, and `hUzero` is the vanishing of the
> restriction of `Rj_*E` to `U`.  The implementation notes of this file say exactly what each one
> is and why it is missing.  Both `h2b` and `hUzero` are stated as implications from the support
> hypothesis, which is where the support hypothesis of the source is used.
>
> The two facts about perfectness the passage needs — that a zero object of `D(𝒪)` is perfect and
> that perfectness transports along an isomorphism — are proved in this file for a ringed site,
> unconditionally.

```lean
theorem isPerfect_derivedPushforward_of_cohomologySupportedOn
    (E : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1
      (edsEtale B S hS hsq).2))
    (hperf : (smallEtaleRingedSite B S hS (edsEtale B S hS hsq).1
      (edsEtale B S hS hsq).2).IsPerfect E)
    (hE : CohomologySupportedOn B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
      (edsEtalePreimageComplementPoints B S hS hsq) E)
    (h2b : CohomologySupportedOn B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
        (edsEtalePreimageComplementPoints B S hS hsq) E →
      IsIso (adjPush.counit.app E))
    (hUzero : CohomologySupportedOn B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
        (edsEtalePreimageComplementPoints B S hS hsq) E →
      IsZero ((edsDerivedRestrictOpen B S hS hsq).obj (RpushD.obj E)))
    (hlocal :
      (smallEtaleRingedSite B S hS (edsOpen B S hS hsq).1
          (edsOpen B S hS hsq).2).IsPerfect
          ((edsDerivedRestrictOpen B S hS hsq).obj (RpushD.obj E)) →
        (smallEtaleRingedSite B S hS (edsEtale B S hS hsq).1
            (edsEtale B S hS hsq).2).IsPerfect
            ((edsDerivedRestrictEtale B S hS hsq).obj (RpushD.obj E)) →
          (smallEtaleRingedSite B S hS W.1 W.2).IsPerfect (RpushD.obj E)) :
    (smallEtaleRingedSite B S hS W.1 W.2).IsPerfect (RpushD.obj E)
```

**`AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PushforwardOfSupportedPerfectCanonical.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PushforwardOfSupportedPerfectCanonical.lean#L130).

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

**`AlgebraicGeometry.Space.isPerfect_rightAdjoint_edsDerivedRestrictEtale_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPushforwardPerfect.lean, line 434](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPushforwardPerfect.lean#L434).

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

**`AlgebraicGeometry.Space.approximationHolds_of_isElementaryDistinguishedSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationAcrossSquare.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationAcrossSquare.lean#L90).

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

**`AlgebraicGeometry.Space.approximationHolds_of_approximationHolds_edsEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationExtensionByZero.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationExtensionByZero.lean#L204). The attribute's comment: “for an elementary distinguished square (U ⊆ X, j : V ⟶ X), T ⊆ |X| \ |U| and a triple (T, E, m): approximation for (j^\{-1}T, E|\_V, m) with E|\_V = quasicoherentDerivedEtalePullback of E, together with H^i(E) supported on T for i ≥ m, gives approximation for (T, E, m); nothing else is bound. T is any subset of |X| \ |U|, closedness being unused”.

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

**`AlgebraicGeometry.Space.approximationHolds_of_affineCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationAffine.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationAffine.lean#L294). The attribute's comment: “approximation for a triple. CONDITIONAL. The assembly is the source's own and the library's Tag 08EQ, approximationHolds\_of\_zeroLocus, is genuinely applied; see the module docstring for every carried input and why it is missing”.

> **Stacks 08HM.**  Let `S` be a scheme and let `X` be an algebraic space over `S` which is
> representable by an affine scheme, say by `Spec R`.  Then approximation holds for a triple
> `(T, E, m)` as in Stacks 08HI as soon as, for some `r ≥ 0`, `E` is `m`-pseudo-coherent, the
> sheaves `Hⁱ(E)` are supported on `T` for `i ≥ m - r + 1`, and `T` is the preimage under the
> comparison of points of a closed subset of `Spec R` cut out by `r` elements — which is the form
> of hypothesis (3) that Stacks 08EQ consumes.
>
> The approximation produced is `ε^*P₀ ⟶ ε^*E₀ ≅ E`, for `P₀ ⟶ E₀` the approximation of
> `(V(f₁, …, f_r), E₀, m)` supplied by Stacks 08EQ; the "What is carried" section of this file
> says what each hypothesis is and which of them the library does not prove.

```lean
theorem approximationHolds_of_affineCover
    (R : CommRingCat.{u}) {r : ℕ} (f : Fin r → R)
    (eps : (Spec R).Modules ⥤ Modules.{u, u} B S hS X hX)
    [eps.Additive] [PreservesFiniteLimits eps] [PreservesFiniteColimits eps]
    (ρ : points B S hS X → PrimeSpectrum R) (hρ : Function.Surjective ρ)
    (hstalk : ∀ (G₀ : (Spec R).Modules) (p : points B S hS X),
      p ∉ supportOfSheaf B S hS X
          ((SheafOfModules.toSheaf
              ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X hX).O))).obj (eps.obj G₀)) ↔
        IsZero (TopCat.Presheaf.stalk (X := Spec R) G₀.val.presheaf (ρ p)))
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X hX) (m : ℤ)
    (E₀ : DerivedCategory.{u + 1} (Spec R).Modules)
    (hE₀ : eps.mapDerivedCategory.obj E₀ ≅ E.obj)
    (hqc₀ : ∀ i : ℤ,
      ((DerivedCategory.homologyFunctor (Spec R).Modules i).obj E₀).IsQuasicoherent)
    (hpc : (smallEtaleRingedSite B S hS X hX).IsPseudoCoherentFrom E.obj m)
    (hpcDescend : (smallEtaleRingedSite B S hS X hX).IsPseudoCoherentFrom E.obj m →
      RingedSpace.IsPseudoCoherentFrom (X := (Spec R).toRingedSpace) E₀ m)
    (hperfAscend : ∀ P₀ : DerivedCategory.{u + 1} (Spec R).Modules,
      Stacks.Cohomology.PerfectComplexes.IsPerfect (X := (Spec R).toRingedSpace) P₀ →
        (smallEtaleRingedSite B S hS X hX).IsPerfect (eps.mapDerivedCategory.obj P₀))
    (hsupp : ∀ i : ℤ, m - (r : ℤ) + 1 ≤ i →
      supportOfSheaf B S hS X
        ((SheafOfModules.toSheaf
            ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X hX).O))).obj
          ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X hX) i).obj E.obj)) ⊆
        ρ ⁻¹' PrimeSpectrum.zeroLocus (Set.range f)) :
    ApproximationHolds B S hS X hX (ρ ⁻¹' PrimeSpectrum.zeroLocus (Set.range f)) E m
```

**`AlgebraicGeometry.Space.approximationByPerfectComplexes_of_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationAffine.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationAffine.lean#L399). The attribute's comment: “approximation by perfect complexes for an affine space. CONDITIONAL on the same ε-bridge, plus the presentation of each closed subset with quasi-compact open complement as the preimage of a zero locus of r elements; the deduction from the triple statement is proved”.

> **The "in particular" of Stacks 08HM**: approximation by perfect complexes, in the sense of
> Stacks 08HJ, holds on an algebraic space representable by an affine scheme.
>
> Given, for each closed `T` whose open complement has quasi-compact inclusion, a presentation of
> the corresponding closed subset of `Spec R` as the zero locus of `r` elements — which is what a
> closed subset with retrocompact complement has, by Stacks 00E8, and the step Stacks
> 08EQ identifies as the only missing one in its own hypothesis (3) — the integer of Stacks 08HJ
> is `r`, and the hypotheses of `AlgebraicGeometry.Space.approximationHolds_of_affineCover` follow
> from those of Stacks 08HJ: `m`-pseudo-coherence from `(m - r)`-pseudo-coherence by
> `AlgebraicGeometry.Space.isPseudoCoherentFrom_mono`, and support in the degrees `≥ m - r + 1`
> from support in the degrees `≥ m - r`.

```lean
theorem approximationByPerfectComplexes_of_affine
    (R : CommRingCat.{u})
    (eps : (Spec R).Modules ⥤ Modules.{u, u} B S hS X hX)
    [eps.Additive] [PreservesFiniteLimits eps] [PreservesFiniteColimits eps]
    (ρ : points B S hS X → PrimeSpectrum R) (hρ : Function.Surjective ρ)
    (hstalk : ∀ (G₀ : (Spec R).Modules) (p : points B S hS X),
      p ∉ supportOfSheaf B S hS X
          ((SheafOfModules.toSheaf
              ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X hX).O))).obj (eps.obj G₀)) ↔
        IsZero (TopCat.Presheaf.stalk (X := Spec R) G₀.val.presheaf (ρ p)))
    (hpres : letI : TopologicalSpace (points B S hS X) := pointTopology B S hS X
      ∀ (T : Set (points B S hS X)) (hT : IsClosed T),
        IsQuasiCompact B S hS
            ((openSubspacesOrderIso B S hS X hX).symm ⟨Tᶜ, hT.isOpen_compl⟩).1.ι →
          ∃ (r : ℕ) (g : Fin r → R), T = ρ ⁻¹' PrimeSpectrum.zeroLocus (Set.range g))
    (E₀ : QuasicoherentDerivedCategory.{u, u} B S hS X hX →
      DerivedCategory.{u + 1} (Spec R).Modules)
    (hE₀ : ∀ E : QuasicoherentDerivedCategory.{u, u} B S hS X hX,
      eps.mapDerivedCategory.obj (E₀ E) ≅ E.obj)
    (hqc₀ : ∀ (E : QuasicoherentDerivedCategory.{u, u} B S hS X hX) (i : ℤ),
      ((DerivedCategory.homologyFunctor (Spec R).Modules i).obj (E₀ E)).IsQuasicoherent)
    (hpcDescend : ∀ (E : QuasicoherentDerivedCategory.{u, u} B S hS X hX) (m : ℤ),
      (smallEtaleRingedSite B S hS X hX).IsPseudoCoherentFrom E.obj m →
        RingedSpace.IsPseudoCoherentFrom (X := (Spec R).toRingedSpace) (E₀ E) m)
    (hperfAscend : ∀ P₀ : DerivedCategory.{u + 1} (Spec R).Modules,
      Stacks.Cohomology.PerfectComplexes.IsPerfect (X := (Spec R).toRingedSpace) P₀ →
        (smallEtaleRingedSite B S hS X hX).IsPerfect (eps.mapDerivedCategory.obj P₀)) :
    ApproximationByPerfectComplexes.{u, u} B S hS X hX
```

**`AlgebraicGeometry.Space.approximationHolds_of_isAffineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationIso.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationIso.lean#L412). The attribute's comment: “first assertion: approximation holds for every triple (T, E, m) with E m-pseudo-coherent, H^i(E) supported on T for i ≥ m - r + 1 and X \ T a union of r affine opens, for X an algebraic space representable by an affine scheme”.

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

**`AlgebraicGeometry.Space.approximationByPerfectComplexes_of_isAffineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationIso.lean, line 444](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationIso.lean#L444). The attribute's comment: “second assertion: approximation by perfect complexes holds on an algebraic space representable by an affine scheme”.

> **The "in particular" of Stacks 08HM**: approximation by perfect complexes (Stacks 08HJ)
> holds on an algebraic space representable by an affine scheme.

```lean
theorem approximationByPerfectComplexes_of_isAffineSpace (hXa : IsAffineSpace B S hS F) :
    ApproximationByPerfectComplexes.{u, u} B S hS F hF
```

**`AlgebraicGeometry.Space.approximationHolds_and_approximationByPerfectComplexes_of_isAffineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationIsoTag.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationIsoTag.lean#L60).

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

**`AlgebraicGeometry.Space.approximationByPerfectComplexes_of_isElementaryDistinguishedSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationSquare.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationSquare.lean#L136).

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

**`AlgebraicGeometry.Space.approximationByPerfectComplexes_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationQcqs.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ApproximationQcqs.lean#L62).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
