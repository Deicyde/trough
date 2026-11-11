---
declaration: section
origin: cited
lean: AlgebraicGeometry.DeRhamLerayHirsch.isIso_deRhamClassSumMorphism, AlgebraicGeometry.DeRhamLerayHirsch.bijective_sum_deRhamCup_pullback, AlgebraicGeometry.DeRhamLerayHirsch.isIso_lerayHirschMorphism, AlgebraicGeometry.DeRhamLerayHirsch.bijective_sum_deRhamCohomologyCup
statement: formalized
proof: formalized
---

# 50.13 Leray-Hirsch type theorems

Section 50.13 of the Stacks Project, [Tag 0FUL](https://stacks.math.columbia.edu/tag/0FUL). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FMP, a lemma

[Tag 0FMP](https://stacks.math.columbia.edu/tag/0FMP) in the Stacks Project.

**`AlgebraicGeometry.DeRhamLerayHirsch.isIso_deRhamClassSumMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/LerayHirschIsomorphism.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/LerayHirschIsomorphism.lean#L385). The attribute's comment: “the Leray-Hirsch isomorphism for de Rham cohomology: for f : X -> Y smooth proper, classes xi\_i in H^\{n\_i}\_dR(X/Y) whose images in H^*\_dR(X\_y/kappa(y)) form a kappa(y)-basis at every point y give an isomorphism (+)\_i O\_Y[-n\_i] -> Rf\_*Omega^bullet\_\{X/Y} in D(O\_Y); the morphism is constructed from the classes through H^m\_dR(X/Y) = Hom(O\_Y[-m], Rf\_*Omega^bullet\_\{X/Y}), and perfectness and base change of Rf\_*Omega^bullet (Tag 0FM0) are the library's unconditional theorems”.

> **[Stacks, Tag 0FMP], the Leray--Hirsch theorem for de Rham cohomology.** Let `f : X ⟶ Y` be a
> smooth proper morphism of schemes, let `n_1, …, n_N ≥ 0` be integers and let
> `ξ_i ∈ H^{n_i}_{dR}(X/Y)`. If for every point `y ∈ Y` the images of `ξ_1, …, ξ_N` in
> `H^*_{dR}(X_y/κ(y))` form a basis over `κ(y)`, then the morphism
>
> `⨁_{i=1}^N 𝒪_Y[-n_i] ⟶ Rf_*Ω^•_{X/Y}`
>
> associated to `ξ_1, …, ξ_N` is an isomorphism in `D(𝒪_Y)`.
>
> The source and the target are perfect, the target by [Stacks, Tag 0FM0], so it suffices that its
> derived pullback to every point be an isomorphism; the formation of `Rf_*Ω^•_{X/Y}` commutes with
> that base change ([Stacks, Tag 0FM0]), and over `κ(y)` the morphism carries the pullbacks of the
> classes of `1` to the images of the `ξ_i` in the de Rham cohomology of the fibre, which form a
> basis.

```lean
theorem isIso_deRhamClassSumMorphism [Smooth f] [IsProper f] {N : ℕ} (n : Fin N → ℕ)
    (ξ : ∀ i : Fin N, ToType (Scheme.Hom.deRhamCohomology f (n i : ℤ)))
    (hb : HasFibrewiseDeRhamBasis f n ξ) :
    IsIso (deRhamClassSumMorphism f n ξ)
```

## Tag 0FUM, a lemma

[Tag 0FUM](https://stacks.math.columbia.edu/tag/0FUM) in the Stacks Project.

**`AlgebraicGeometry.DeRhamLerayHirsch.bijective_sum_deRhamCup_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LerayHirschAffine.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LerayHirschAffine.lean#L274). The attribute's comment: “Leray-Hirsch over an affine base: for f : X -> Y smooth proper over S with Y and S affine, and classes xi\_i in H^\{n\_i}\_dR(X/S) (n\_i >= 0) whose images in H^*\_dR(X\_y/kappa(y)) form a kappa(y)-basis at every point y of Y, the map (+)\_i H^*\_dR(Y/S) -> H^*\_dR(X/S), (a\_i) |-> sum xi\_i cup f^*a\_i, is an isomorphism, i.e. bijective in every degree N”.

> **[Stacks, Tag 0FUM]**, the Leray–Hirsch theorem over an affine base. Let `f : X ⟶ Y` be a
> smooth proper morphism of schemes over `S`, with `Y` and `S` affine, let `n_1, …, n_r ≥ 0` and let
> `ξ_i ∈ H^{n_i}_{dR}(X/S)` be classes whose images in `H^*_{dR}(X_y/κ(y))` form a basis over
> `κ(y)` for every point `y ∈ Y`. Then
>
> `⨁_{i=1}^r H^*_{dR}(Y/S) ⟶ H^*_{dR}(X/S)`, `(a_1, …, a_r) ↦ ∑ ξ_i ∪ f^*a_i`
>
> is an isomorphism: in every degree `N` the map `⨁_i H^{N-n_i}_{dR}(Y/S) ⟶ H^N_{dR}(X/S)` is
> bijective.

```lean
theorem bijective_sum_deRhamCup_pullback [Smooth f] [IsProper f] [IsAffine Y] [IsAffine S]
    {r : ℕ} (n : Fin r → ℕ)
    (ξ : ∀ i, SheafOfModules.deRhamCohomology (Scheme.Hom.deRhamAlgebras (f ≫ g))
      (SheafOfModules.deRhamDifferential (Scheme.Hom.deRhamAlgebras (f ≫ g))) (n i : ℤ))
    (hb : ∀ y : Y, ∃ b : Module.Basis (Fin r) (Y.residueField y)
        (DirectSum ℤ fun m : ℤ => ↥(fibreDeRhamModule f y m)),
      ∀ i, b i = DirectSum.lof (Y.residueField y) ℤ (fun m : ℤ => ↥(fibreDeRhamModule f y m))
        (n i : ℤ) (fibreClassOverS f g y (n i : ℤ) (ξ i)))
    (N : ℤ) :
    Function.Bijective (fun a : ∀ i, SheafOfModules.deRhamCohomology
        (Scheme.Hom.deRhamAlgebras g)
        (SheafOfModules.deRhamDifferential (Scheme.Hom.deRhamAlgebras g)) (N - n i) =>
      ∑ i, (eqToHom (congrArg (SheafOfModules.deRhamCohomology
          (Scheme.Hom.deRhamAlgebras (f ≫ g))
          (SheafOfModules.deRhamDifferential (Scheme.Hom.deRhamAlgebras (f ≫ g))))
          (add_sub_cancel (n i : ℤ) N))).hom
        (SheafOfModules.deRhamCohomologyCup _ _ (n i) (N - n i) (ξ i)
          (deRhamPullbackModule f g (N - n i) (a i))))
```

## Tag 0FMR, a proposition

[Tag 0FMR](https://stacks.math.columbia.edu/tag/0FMR) in the Stacks Project.

**`AlgebraicGeometry.DeRhamLerayHirsch.isIso_lerayHirschMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/LerayHirschTheorem.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/LerayHirschTheorem.lean#L231). The attribute's comment: “first assertion: for f smooth proper over S and classes ξ\_i ∈ H^\{n\_i}\_dR(X/S) whose images in H^*\_dR(X\_y/y) form a κ(y)-basis for all y ∈ Y, the map ξ~ = ⊕ ξ~\_i[-n\_i] : ⊕ Ω\_\{Y/S}[-n\_i] → Rf\_*Ω\_\{X/S} is an isomorphism in D(Y, (Y → S)^\{-1}O\_S)”.

> **Stacks Project, Proposition 0FMR, the derived statement.** For a smooth proper morphism
> `f : X ⟶ Y` over `S` and classes `ξ_i ∈ H^{n_i}_{dR}(X/S)` whose images in `H^*_{dR}(X_y/y)` form a
> basis over `κ(y)` for every point `y ∈ Y`, the morphism
> `ξ̃ = ⨁ ξ̃_i[-n_i] : ⨁ Ω^•_{Y/S}[-n_i] ⟶ Rf_*Ω^•_{X/S}` is an isomorphism in
> `D(Y, (Y ⟶ S)^{-1}𝒪_S)`.

```lean
theorem isIso_lerayHirschMorphism [Smooth f] [IsProper f] {r : ℕ} (n : Fin r → ℕ)
    (ξ : ∀ i, SheafOfModules.deRhamCohomology (Scheme.Hom.deRhamAlgebras (f ≫ g))
      (SheafOfModules.deRhamDifferential (Scheme.Hom.deRhamAlgebras (f ≫ g))) (n i : ℤ))
    (hb : ∀ y : Y, ∃ b : Module.Basis (Fin r) (Y.residueField y)
        (DirectSum ℤ fun m : ℤ => ↥(fibreDeRhamModule f y m)),
      ∀ i, b i = DirectSum.lof (Y.residueField y) ℤ (fun m : ℤ => ↥(fibreDeRhamModule f y m))
        (n i : ℤ) (fibreClassOverS f g y (n i : ℤ) (ξ i))) :
    IsIso (lerayHirschMorphism f g n ξ)
```

**`AlgebraicGeometry.DeRhamLerayHirsch.bijective_sum_deRhamCohomologyCup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/LerayHirschTheorem.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/LerayHirschTheorem.lean#L263). The attribute's comment: “second assertion: under the same hypotheses the map ⊕\_i H^*\_dR(Y/S) → H^*\_dR(X/S), (a\_1, ..., a\_N) ↦ Σ ξ\_i ∪ f^*a\_i, is an isomorphism (in every degree k, from ⊕\_i H^\{k-n\_i}\_dR(Y/S))”.

> **Stacks Project, Proposition 0FMR, the statement on de Rham cohomology.** For a smooth proper
> morphism `f : X ⟶ Y` over `S` and classes `ξ_i ∈ H^{n_i}_{dR}(X/S)` whose images in
> `H^*_{dR}(X_y/y)` form a basis over `κ(y)` for every point `y ∈ Y`, the map
> `⨁_i H^*_{dR}(Y/S) ⟶ H^*_{dR}(X/S), (a_i) ↦ ∑ ξ_i ∪ f^*a_i` is an isomorphism: in every degree `k`
> the map `⨁_i H^{k - n_i}_{dR}(Y/S) ⟶ H^k_{dR}(X/S)` is bijective.

```lean
theorem bijective_sum_deRhamCohomologyCup [Smooth f] [IsProper f] {r : ℕ} (n : Fin r → ℕ)
    (ξ : ∀ i, SheafOfModules.deRhamCohomology (Scheme.Hom.deRhamAlgebras (f ≫ g))
      (SheafOfModules.deRhamDifferential (Scheme.Hom.deRhamAlgebras (f ≫ g))) (n i : ℤ))
    (hb : ∀ y : Y, ∃ b : Module.Basis (Fin r) (Y.residueField y)
        (DirectSum ℤ fun m : ℤ => ↥(fibreDeRhamModule f y m)),
      ∀ i, b i = DirectSum.lof (Y.residueField y) ℤ (fun m : ℤ => ↥(fibreDeRhamModule f y m))
        (n i : ℤ) (fibreClassOverS f g y (n i : ℤ) (ξ i))) (k : ℤ) :
    Function.Bijective (fun a : ∀ i, SheafOfModules.deRhamCohomology
        (Scheme.Hom.deRhamAlgebras g)
        (SheafOfModules.deRhamDifferential (Scheme.Hom.deRhamAlgebras g)) (k - n i) =>
      ∑ i, (eqToHom (congrArg (SheafOfModules.deRhamCohomology
          (Scheme.Hom.deRhamAlgebras (f ≫ g))
          (SheafOfModules.deRhamDifferential (Scheme.Hom.deRhamAlgebras (f ≫ g))))
          (add_sub_cancel (n i : ℤ) k))).hom
        (SheafOfModules.deRhamCohomologyCup _ _ (n i) (k - n i) (ξ i)
          (DeRhamKatzOdaCech.deRhamPullbackModule f g (k - n i) (a i))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.13, Tag 0FUL](https://stacks.math.columbia.edu/tag/0FUL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
