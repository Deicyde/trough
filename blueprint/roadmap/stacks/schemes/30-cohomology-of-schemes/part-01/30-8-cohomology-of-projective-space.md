---
declaration: section
origin: cited
lean: Stacks.ProjectiveSpace.Cohomology.twistCohomologyIsoHomogeneous, Stacks.ProjectiveSpace.Cohomology.twistCohomologyIsoNegative, Stacks.ProjectiveSpace.Cohomology.isZero_twistCohomology, Stacks.ProjectiveSpace.Cohomology.twistCohomologyMonomial, Stacks.ProjectiveSpace.Cohomology.bijective_degreeSection_line, Stacks.ProjectiveSpace.Cohomology.serreTwistCohomology, Stacks.ProjectiveSpace.Cohomology.serreTwistCohomology_degreeZero_baseChange, Stacks.ProjectiveSpace.Cohomology.serreTwistCohomology_degreeTop_baseChange
statement: formalized
proof: formalized
---

# 30.8 Cohomology of projective space

Section 30.8 of the Stacks Project, [Tag 01XS](https://stacks.math.columbia.edu/tag/01XS). 5 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01XT, a lemma

[Tag 01XT](https://stacks.math.columbia.edu/tag/01XT) in the Stacks Project.

**`Stacks.ProjectiveSpace.Cohomology.twistCohomologyIsoHomogeneous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/TwistCohomologyMonomial.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/TwistCohomologyMonomial.lean#L232). The attribute's comment: “degree zero, nonnegative twist”.

> **[Stacks, Tag 01XT], the degree-zero row.** For `d ≥ 0` the module `H⁰(ℙⁿ_R, 𝒪(d))` is the
> module of degree-`d` homogeneous polynomials in `T₀, …, Tₙ`, for every `n ≥ 0`.

```lean
def twistCohomologyIsoHomogeneous (R : Type u) [CommRing R] (n : ℕ) (d : ℤ) (hd : 0 ≤ d) :
    twistCohomology R n d 0 ≅
      ModuleCat.of R (MvPolynomial.homogeneousSubmodule (Fin (n + 1)) R d.toNat)
```

**`Stacks.ProjectiveSpace.Cohomology.twistCohomologyIsoNegative`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/TwistCohomologyMonomial.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/TwistCohomologyMonomial.lean#L246). The attribute's comment: “top degree, negative twist”.

> **[Stacks, Tag 01XT], the top-degree row.** For `d < 0` the module `Hⁿ(ℙⁿ_R, 𝒪(d))` is the
> degree-`d` part of `(T₀ ⋯ Tₙ)⁻¹ R[T₀⁻¹, …, Tₙ⁻¹]`, the free `R`-module on the degree-`d` Laurent
> monomials with every exponent negative, for every `n ≥ 0`.

```lean
def twistCohomologyIsoNegative (R : Type u) [CommRing R] (n : ℕ) (d : ℤ) (hd : d < 0) :
    twistCohomology R n d n ≅ ModuleCat.of R (negativeTwistPart R n d)
```

**`Stacks.ProjectiveSpace.Cohomology.isZero_twistCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/TwistCohomologyMonomial.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/TwistCohomologyMonomial.lean#L257). The attribute's comment: “all other cases”.

> **[Stacks, Tag 01XT], the vanishing row.** Outside the two cases `q = 0, d ≥ 0` and
> `q = n, d < 0` the module `H^q(ℙⁿ_R, 𝒪(d))` is zero, for every `n ≥ 0`.

```lean
theorem isZero_twistCohomology (R : Type u) [CommRing R] (n : ℕ) (d : ℤ) (q : ℕ)
    (hq : ¬ ((q = 0 ∧ 0 ≤ d) ∨ (q = n ∧ d < 0))) :
    IsZero (twistCohomology R n d q)
```

**`Stacks.ProjectiveSpace.Cohomology.twistCohomologyMonomial`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/TwistCohomologyMonomial.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/TwistCohomologyMonomial.lean#L309). References: EGA III (2.1.13), “more general”; EGA III (2.1.14), “more general”; SGA 7 XIX (1.2), “special case”.

> **The cohomology of the twists of the structure sheaf on projective space.** For every
> commutative ring `R`, every `n ≥ 0` and every integer `d`, `H^q(ℙⁿ_R, 𝒪(d))` is the degree-`d`
> part of `R[T₀, …, Tₙ]` when `q = 0` and `d ≥ 0`, is the degree-`d` part of
> `(T₀ ⋯ Tₙ)⁻¹ R[T₀⁻¹, …, Tₙ⁻¹]` when `q = n` and `d < 0`, and is zero otherwise, as
> `R`-modules.

```lean
def twistCohomologyMonomial (R : Type u) [CommRing R] (n : ℕ) (d : ℤ) :
    TwistCohomologyMonomial R n d
```

**`Stacks.ProjectiveSpace.Cohomology.bijective_degreeSection_line`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/TwistSectionsBijective.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/TwistSectionsBijective.lean#L87). The attribute's comment: “degree zero, nonnegative twist, for the projective line over a field: the canonical map of Equation 01MP from the degree-d binary forms to the sections of O(d) is bijective”. References: EGA II (8.14.11), “Case Y = Spec k”.

> **`Γ(𝐏¹_k, 𝒪(d))` is the module of binary forms of degree `d`, through the canonical map
> of Equation [Stacks, Tag 01MP].**
>
> For `k` a field and every `d ≥ 0`, the degree-`d` section map
> `(k[T₀, T₁])_d ⟶ Γ(𝐏¹_k, 𝒪(d))` is bijective. This is the `n = 1` case of
> `Stacks.ProjectiveSpace.Cohomology.bijective_degreeSection`, which is injective because
> `k[T₀, …, Tₙ]` is a domain and surjective because
> `Stacks.ProjectiveSpace.Cohomology.homogeneousIsoTwistSections` makes the two sides `k`-vector
> spaces of the same finite dimension.
>
> Together with the multiplicativity across degrees of
> `Stacks.AlgebraicGeometry.ProjTwistSectionRing.mul_degreeSection` this is the identification of
> the graded ring `⨁_d Γ(𝐏¹_k, 𝒪(d))` with `k[T₀, T₁]`.

```lean
theorem bijective_degreeSection_line (k : Type u) [Field k] (d : ℕ) :
    Function.Bijective (degreeSection (polyGrading k 1) d)
```

## Tag 01XU, an equation

[Tag 01XU](https://stacks.math.columbia.edu/tag/01XU) in the Stacks Project.

**`Stacks.ProjectiveSpace.Cohomology.serreTwistCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreComputation.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreComputation.lean#L285). References: EGA III (2.1.13), “more general”; SGA 7 XIX (1.2), “special case”.

> **Serre's computation of the cohomology of the twists of the structure sheaf on projective
> space.** For a commutative ring `R`, `n = m + 1 ≥ 1` and every integer `d`,
> `H^q(ℙⁿ_R, 𝒪(d))` is the degree-`d` part of `R[T₀, …, Tₙ]` for `q = 0`, is zero for
> `q ≠ 0, n`, and is `Hom_R((R[T₀, …, Tₙ])_{-n-1-d}, R)` for `q = n`, as `R`-modules.

```lean
def serreTwistCohomology (R : Type u) [CommRing R] (m : ℕ) (d : ℤ) :
    SerreTwistCohomology R m d
```

## Tag 01XV, a lemma

[Tag 01XV](https://stacks.math.columbia.edu/tag/01XV) in the Stacks Project.

**`Stacks.ProjectiveSpace.Cohomology.serreTwistCohomology_degreeZero_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafBaseChange/TwistBaseChange.lean, line 584](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafBaseChange/TwistBaseChange.lean#L584). The attribute's comment: “base change along R → S on H^0, through Equation 01XU”.

> **[Stacks, Tag 01XV], base change on `H⁰`.** For a ring map `φ : R → S`, the base-change map
> `H⁰(ℙⁿ_R, 𝒪(d)) ⟶ H⁰(ℙⁿ_S, 𝒪(d))` — the map on cohomology attached to the pullback along
> `ℙⁿ_S ⟶ ℙⁿ_R` and the identification of the pullback of `𝒪(d)` with `𝒪(d)` — is, through the
> identifications of [Stacks, Equation 01XU] of `H⁰(ℙⁿ_R, 𝒪(d))` with `(R[T₀, …, Tₙ])_d` and of
> `H⁰(ℙⁿ_S, 𝒪(d))` with `(S[T₀, …, Tₙ])_d`, the coefficientwise base change
> `(R[T₀, …, Tₙ])_d ⟶ (S[T₀, …, Tₙ])_d`. Here `n = N + 1` and `d` is any integer.

```lean
theorem serreTwistCohomology_degreeZero_baseChange (N : ℕ) (d : ℤ)
    (x : twistCohomology R (N + 1) d 0) :
    ConcreteCategory.hom (serreTwistCohomology S N d).degreeZero.hom
        (ConcreteCategory.hom (Stacks.Cohomology.CechIso.fMapCohomology (projModelMap (N + 1) φ)
          (ProjectiveSpectrum.Proj.twistingSheaf (polyGrading S (N + 1)) d)
          (ProjectiveSpectrum.Proj.twistingSheaf (polyGrading R (N + 1)) d)
          (twistBaseChangeFMap φ (N + 1) d) 0) x) =
      baseChangeChart φ (N + 1) d ∅
        (ConcreteCategory.hom (serreTwistCohomology R N d).degreeZero.hom x)
```

**`Stacks.ProjectiveSpace.Cohomology.serreTwistCohomology_degreeTop_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafBaseChange/TwistBaseChange.lean, line 614](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafBaseChange/TwistBaseChange.lean#L614). The attribute's comment: “base change along R → S on H^n, through Equation 01XU”.

> **[Stacks, Tag 01XV], base change on `Hⁿ`.** For a ring map `φ : R → S`, the base-change map
> `Hⁿ(ℙⁿ_R, 𝒪(d)) ⟶ Hⁿ(ℙⁿ_S, 𝒪(d))` is, through the identifications of
> [Stacks, Equation 01XU] of `Hⁿ` with `Hom((R[T₀, …, Tₙ])_{-n-1-d}, R)` and with
> `Hom((S[T₀, …, Tₙ])_{-n-1-d}, S)`, the base change of functionals: the functional attached to the
> base change of a class takes the value `φ (λ h)` on the base change of `h`, where `λ` is the
> functional attached to the class. Since the base changes of the monomials span
> `(S[T₀, …, Tₙ])_{-n-1-d}`, this determines it. Here `n = N + 1` and `d` is any integer.

```lean
theorem serreTwistCohomology_degreeTop_baseChange (N : ℕ) (d : ℤ)
    (x : twistCohomology R (N + 1) d (N + 1))
    (h : twistChart R (N + 1) (-d - (((N + 1 : ℕ) : ℤ) + 1)) (∅ : Set (Fin (N + 1 + 1)))) :
    ConcreteCategory.hom (serreTwistCohomology S N d).degreeTop.hom
        (ConcreteCategory.hom (Stacks.Cohomology.CechIso.fMapCohomology (projModelMap (N + 1) φ)
          (ProjectiveSpectrum.Proj.twistingSheaf (polyGrading S (N + 1)) d)
          (ProjectiveSpectrum.Proj.twistingSheaf (polyGrading R (N + 1)) d)
          (twistBaseChangeFMap φ (N + 1) d) (N + 1)) x)
        (baseChangeChart φ (N + 1) (-d - (((N + 1 : ℕ) : ℤ) + 1)) ∅ h) =
      φ (ConcreteCategory.hom (serreTwistCohomology R N d).degreeTop.hom x h)
```

**`Stacks.ProjectiveSpace.Cohomology.zeroDim_degreeZero_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafBaseChange/ZeroDim.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafBaseChange/ZeroDim.lean#L175). The attribute's comment: “n = 0: multiplication by a homogeneous f on H^0, d ≥ 0, through Tag 01XT”.

> **[Stacks, Tag 01XV] for `n = 0`, multiplication on `H⁰`, corrected.** On `ℙ⁰_R` the two
> rows of [Stacks, Equation 01XU] both concern `H⁰` and hold only under the side conditions of
> [Stacks, Tag 01XT]. For `d ≥ 0`, through the identification of `H⁰(ℙ⁰_R, 𝒪(d))` with
> `(R[T₀])_d`, the map induced by multiplication by `f`, homogeneous of degree `m`, is
> multiplication by `f`.

```lean
theorem zeroDim_degreeZero_mul {m : ℕ} {d e : ℤ} (f : MvPolynomial (Fin (0 + 1)) R)
    (hf : f.IsHomogeneous m) (hde : d + m = e) (hd : 0 ≤ d) (x : twistCohomology R 0 d 0) :
    LinearEquiv.ofEq _ _ (twistChart_univ_eq_empty_zeroDim R (show 0 ≤ e by omega))
        (ConcreteCategory.hom (twistCohomologyIsoChartUnivZeroDim R e).hom
          (ConcreteCategory.hom ((ModuleCat.restrictScalars.{u} (coeffScalar R 0)).map
          (((Stacks.Cohomology.sectionsFunctor (AlgebraicGeometry.Proj (polyGrading R 0))
            ⊤).rightDerived 0).map (twistScalarSheafMap (polyGrading R 0) m d e
              (by omega) ⟨f, (MvPolynomial.mem_homogeneousSubmodule m f).2 hf⟩))) x)) =
      chartMul (chartOfHomogeneous R 0 f hf) hde ∅
        (LinearEquiv.ofEq _ _ (twistChart_univ_eq_empty_zeroDim R hd)
          (ConcreteCategory.hom (twistCohomologyIsoChartUnivZeroDim R d).hom x))
```

**`Stacks.ProjectiveSpace.Cohomology.zeroDim_degreeTop_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafBaseChange/ZeroDim.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafBaseChange/ZeroDim.lean#L194). The attribute's comment: “n = 0: multiplication on H^n is the contragredient, d + m < 0, through Tag 01XT”.

> **[Stacks, Tag 01XV] for `n = 0`, multiplication on `Hⁿ`, corrected.** For `d + m < 0`,
> through the identification of `H⁰(ℙ⁰_R, 𝒪(d))` with `Hom_R((R[T₀])_{-1-d}, R)` by the residue
> pairing, the map induced by multiplication by `f`, homogeneous of degree `m`, is the
> contragredient of multiplication by `f`, `(R[T₀])_{-1-(d+m)} ⟶ (R[T₀])_{-1-d}`.

```lean
theorem zeroDim_degreeTop_mul {m : ℕ} {d e : ℤ} (f : MvPolynomial (Fin (0 + 1)) R)
    (hf : f.IsHomogeneous m) (hde : d + m = e) (he : e < 0) (x : twistCohomology R 0 d 0)
    (h : twistChart R 0 (-e - (((0 : ℕ) : ℤ) + 1)) (∅ : Set (Fin (0 + 1)))) :
    topDualEquiv R 0 e (LinearEquiv.ofEq _ _ (twistChart_univ_eq_negativeTwistPart_zeroDim R he)
        (ConcreteCategory.hom (twistCohomologyIsoChartUnivZeroDim R e).hom
          (ConcreteCategory.hom ((ModuleCat.restrictScalars.{u} (coeffScalar R 0)).map
          (((Stacks.Cohomology.sectionsFunctor (AlgebraicGeometry.Proj (polyGrading R 0))
            ⊤).rightDerived 0).map (twistScalarSheafMap (polyGrading R 0) m d e
              (by omega) ⟨f, (MvPolynomial.mem_homogeneousSubmodule m f).2 hf⟩))) x))) h =
      topDualEquiv R 0 d (LinearEquiv.ofEq _ _
          (twistChart_univ_eq_negativeTwistPart_zeroDim R (show d < 0 by omega))
          (ConcreteCategory.hom (twistCohomologyIsoChartUnivZeroDim R d).hom x))
        (chartMul (chartOfHomogeneous R 0 f hf) (show -e - (((0 : ℕ) : ℤ) + 1) + m =
          -d - (((0 : ℕ) : ℤ) + 1) by omega) ∅ h)
```

**`Stacks.ProjectiveSpace.Cohomology.zeroDim_degreeZero_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafBaseChange/ZeroDim.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafBaseChange/ZeroDim.lean#L217). The attribute's comment: “n = 0: base change along R → S on H^0, d ≥ 0, through Tag 01XT”.

> **[Stacks, Tag 01XV] for `n = 0`, base change on `H⁰`, corrected.** For `d ≥ 0`, through the
> identifications of `H⁰(ℙ⁰, 𝒪(d))` with `(R[T₀])_d` and `(S[T₀])_d`, the base-change map is the
> coefficientwise base change.

```lean
theorem zeroDim_degreeZero_baseChange (d : ℤ) (hd : 0 ≤ d) (x : twistCohomology R 0 d 0) :
    LinearEquiv.ofEq _ _ (twistChart_univ_eq_empty_zeroDim S hd)
        (ConcreteCategory.hom (twistCohomologyIsoChartUnivZeroDim S d).hom
          (ConcreteCategory.hom (Stacks.Cohomology.CechIso.fMapCohomology (projModelMap 0 φ)
          (ProjectiveSpectrum.Proj.twistingSheaf (polyGrading S 0) d)
          (ProjectiveSpectrum.Proj.twistingSheaf (polyGrading R 0) d)
          (twistBaseChangeFMap φ 0 d) 0) x)) =
      baseChangeChart φ 0 d ∅ (LinearEquiv.ofEq _ _ (twistChart_univ_eq_empty_zeroDim R hd)
        (ConcreteCategory.hom (twistCohomologyIsoChartUnivZeroDim R d).hom x))
```

**`Stacks.ProjectiveSpace.Cohomology.zeroDim_degreeTop_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafBaseChange/ZeroDim.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafBaseChange/ZeroDim.lean#L234). The attribute's comment: “n = 0: base change along R → S on H^n, d < 0, through Tag 01XT”.

> **[Stacks, Tag 01XV] for `n = 0`, base change on `Hⁿ`, corrected.** For `d < 0`, through the
> identifications of `H⁰(ℙ⁰, 𝒪(d))` with `Hom_R((R[T₀])_{-1-d}, R)` and with
> `Hom_S((S[T₀])_{-1-d}, S)` by the residue pairing, the functional attached to the base change of a
> class takes the value `φ (λ h)` on the base change of `h`.

```lean
theorem zeroDim_degreeTop_baseChange (d : ℤ) (hd : d < 0) (x : twistCohomology R 0 d 0)
    (h : twistChart R 0 (-d - (((0 : ℕ) : ℤ) + 1)) (∅ : Set (Fin (0 + 1)))) :
    topDualEquiv S 0 d (LinearEquiv.ofEq _ _ (twistChart_univ_eq_negativeTwistPart_zeroDim S hd)
        (ConcreteCategory.hom (twistCohomologyIsoChartUnivZeroDim S d).hom
          (ConcreteCategory.hom (Stacks.Cohomology.CechIso.fMapCohomology (projModelMap 0 φ)
          (ProjectiveSpectrum.Proj.twistingSheaf (polyGrading S 0) d)
          (ProjectiveSpectrum.Proj.twistingSheaf (polyGrading R 0) d)
          (twistBaseChangeFMap φ 0 d) 0) x)))
        (baseChangeChart φ 0 (-d - (((0 : ℕ) : ℤ) + 1)) ∅ h) =
      φ (topDualEquiv R 0 d (LinearEquiv.ofEq _ _
        (twistChart_univ_eq_negativeTwistPart_zeroDim R hd)
          (ConcreteCategory.hom (twistCohomologyIsoChartUnivZeroDim R d).hom x)) h)
```

**`Stacks.ProjectiveSpace.Cohomology.serreTwistCohomology_degreeZero_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafFunctoriality.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafFunctoriality.lean#L339). The attribute's comment: “multiplication by a homogeneous f on H^0, through Equation 01XU”.

> **[Stacks, Tag 01XV], multiplication on `H⁰`.** For `f ∈ R[T₀, …, Tₙ]` homogeneous of degree
> `m`, the map `H⁰(ℙⁿ_R, 𝒪(d)) ⟶ H⁰(ℙⁿ_R, 𝒪(d + m))` induced by the morphism of sheaves
> `𝒪(d) ⟶ 𝒪(d + m)` given by multiplication by `f` is, through the identification of
> [Stacks, Equation 01XU] of `H⁰(ℙⁿ_R, 𝒪(d))` with `(R[T₀, …, Tₙ])_d`, multiplication by `f`
> `(R[T₀, …, Tₙ])_d ⟶ (R[T₀, …, Tₙ])_{d+m}`. Here `n = N + 1` and `d` is any integer.

```lean
theorem serreTwistCohomology_degreeZero_mul (N : ℕ) {m : ℕ} {d e : ℤ}
    (f : MvPolynomial (Fin (N + 1 + 1)) R) (hf : f.IsHomogeneous m) (hde : d + m = e) :
    (ModuleCat.restrictScalars.{u} (coeffScalar R (N + 1))).map
          (((Stacks.Cohomology.sectionsFunctor (AlgebraicGeometry.Proj (polyGrading R (N + 1)))
            ⊤).rightDerived 0).map (twistScalarSheafMap (polyGrading R (N + 1)) m d e
              (by omega) ⟨f, (MvPolynomial.mem_homogeneousSubmodule m f).2 hf⟩)) ≫
        (serreTwistCohomology R N e).degreeZero.hom =
      (serreTwistCohomology R N d).degreeZero.hom ≫
        ModuleCat.ofHom (chartMul (chartOfHomogeneous R (N + 1) f hf) hde ∅)
```

**`Stacks.ProjectiveSpace.Cohomology.serreTwistCohomology_degreeTop_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafFunctoriality.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/SerreSheafFunctoriality.lean#L361). The attribute's comment: “multiplication by a homogeneous f on H^n is the contragredient, through Equation 01XU”.

> **[Stacks, Tag 01XV], multiplication on `Hⁿ`.** For `f ∈ R[T₀, …, Tₙ]` homogeneous of degree
> `m`, the map `Hⁿ(ℙⁿ_R, 𝒪(d)) ⟶ Hⁿ(ℙⁿ_R, 𝒪(d + m))` induced by the morphism of sheaves
> `𝒪(d) ⟶ 𝒪(d + m)` given by multiplication by `f` is, through the identifications of
> [Stacks, Equation 01XU] of `Hⁿ(ℙⁿ_R, 𝒪(d))` with `Hom_R((R[T₀, …, Tₙ])_{-n-1-d}, R)`, the
> contragredient of multiplication by `f`
> `(R[T₀, …, Tₙ])_{-n-1-(d+m)} ⟶ (R[T₀, …, Tₙ])_{-n-1-d}`. Here `n = N + 1` and `d` is any
> integer.

```lean
theorem serreTwistCohomology_degreeTop_mul (N : ℕ) {m : ℕ} {d e : ℤ}
    (f : MvPolynomial (Fin (N + 1 + 1)) R) (hf : f.IsHomogeneous m) (hde : d + m = e) :
    (ModuleCat.restrictScalars.{u} (coeffScalar R (N + 1))).map
          (((Stacks.Cohomology.sectionsFunctor (AlgebraicGeometry.Proj (polyGrading R (N + 1)))
            ⊤).rightDerived (N + 1)).map (twistScalarSheafMap (polyGrading R (N + 1)) m d e
              (by omega) ⟨f, (MvPolynomial.mem_homogeneousSubmodule m f).2 hf⟩)) ≫
        (serreTwistCohomology R N e).degreeTop.hom =
      (serreTwistCohomology R N d).degreeTop.hom ≫
        ModuleCat.ofHom
          (chartMul (chartOfHomogeneous R (N + 1) f hf)
            (dualDegree_add_of_add N hde) ∅).dualMap
```

## Tag 01XW, a lemma

[Tag 01XW](https://stacks.math.columbia.edu/tag/01XW) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjectiveSpaceHigherDirectImage.isIso_app_structureMorphism_projectiveSpaceOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpaceHigherDirectImage/DegreeZero.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpaceHigherDirectImage/DegreeZero.lean#L158). The attribute's comment: “the degree-zero clause at the zeroth twist, sectionwise and for the underived direct image: the structure morphism of ℙⁿ_S induces an isomorphism Γ(S, V) ≅ Γ(ℙⁿ_S, f⁻¹V) for every affine open V of the base, which is f_* 𝒪 = 𝒪_S on a basis of opens. The degree-zero row at every twist, assembled as an isomorphism of module sheaves on S and in the R⁰ f_* spelling, is ProjectiveSpaceHigherDirectImage.baseDegreeSheafIsoPushforwardTwistOver and ...baseDegreeSheafIsoRightDerivedPushforwardTwistOver in ...DegreeZeroRow; the whole display, its three rows in one statement at n >= 1, is ...rightDerivedPlusPushforwardTwistOverDisplay in ...Display”.

> **The degree-zero identification `f_* 𝒪_{ℙⁿ_S} = 𝒪_S`.** For the structure morphism
> `f : ℙⁿ_S ⟶ S` over an arbitrary scheme `S` and an arbitrary `n`, the canonical map
> `𝒪_S ⟶ f_* 𝒪_{ℙⁿ_S}` is an isomorphism on the sections over every affine open `V` of the base:
> `f` induces an isomorphism `Γ(S, V) ≅ Γ(ℙⁿ_S, f⁻¹V)`.
>
> Since the affine opens form a basis of `S` and a morphism of sheaves that is invertible on a
> basis is invertible, this is the full assertion that the direct image of the structure sheaf of
> `ℙⁿ_S` is the structure sheaf of `S`.

```lean
theorem isIso_app_structureMorphism_projectiveSpaceOver (n : ℕ) (S : Scheme.{u}) {V : S.Opens}
    (hV : IsAffineOpen V) : IsIso ((projectiveSpaceOver n S ↘ S).app V)
```

**`Stacks.AlgebraicGeometry.ProjectiveSpaceHigherDirectImage.rightDerivedPlusPushforwardTwistOverDisplay`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpaceHigherDirectImage/Display.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpaceHigherDirectImage/Display.lean#L110). The attribute's comment: “the display whole, at n = m + 1 >= 1, for every scheme S and every integer twist d: R^0 f_* O(d) = (O_S[T_0, ..., T_n])_d, R^q f_* O(d) = 0 for every q /= 0, n, and R^n f_* O(d) = Hom_{O_S}((O_S[T_0, ..., T_n])_{-n-1-d}, O_S). At n = 0 the display's first and third rows speak about the same degree and disagree, so n >= 1 is the range in which it is a consistent assertion”.

> **The display of [Stacks, Tag 01XW].** For the structure morphism `f : ℙⁿ_S ⟶ S` of
> projective `n`-space over an arbitrary scheme `S`, with `n = m + 1 ≥ 1`, and for every integer
> twist `d`:
>
> * `R⁰ f_* 𝒪(d) ≅ (𝒪_S[T₀, …, Tₙ])_d`, the degree-`d` part of the polynomial algebra on the base;
> * `Rᵠ f_* 𝒪(d) = 0` for every integer `q` with `q ≠ 0` and `q ≠ n`;
> * `Rⁿ f_* 𝒪(d) ≅ Hom_{𝒪_S}((𝒪_S[T₀, …, Tₙ])_{-n-1-d}, 𝒪_S)`.
>
> The three components are `baseDegreeSheafIsoRightDerivedPushforwardTwistOver`, whose hypothesis
> `0 ≤ d ∨ 0 < n` is discharged by `n = m + 1 ≥ 1`, then
> `MiddleVanishing.isZero_rightDerivedPlus_pushforward_twistOver_of_ne`, then
> `rightDerivedPlusTopIsoDualBaseDegreeSheaf`.
>
> The source's display is inconsistent at `n = 0`, where its first and third rows apply to the same
> degree and disagree, so `n ≥ 1` is the range in which it asserts something; see the module
> docstring.

```lean
def rightDerivedPlusPushforwardTwistOverDisplay (m : ℕ) (S : Scheme.{u}) (d : ℤ) :
    PProd (baseDegreeSheaf (m + 1) S d ≅
        ((Scheme.Modules.pushforward (projectiveSpaceOver (m + 1) S ↘ S)).rightDerivedPlus 0).obj
          (twistOver (m + 1) S d))
      (PProd (∀ q : ℤ, q ≠ 0 → q ≠ ((m + 1 : ℕ) : ℤ) →
            IsZero (((Scheme.Modules.pushforward
              (projectiveSpaceOver (m + 1) S ↘ S)).rightDerivedPlus q).obj
                (twistOver (m + 1) S d)))
        (((Scheme.Modules.pushforward (projectiveSpaceOver (m + 1) S ↘ S)).rightDerivedPlus
              ((m + 1 : ℕ) : ℤ)).obj (twistOver (m + 1) S d) ≅
          dualSheaf (baseDegreeSheaf (m + 1) S (-((m + 1 : ℕ) : ℤ) - 1 - d))))
```

**`Stacks.AlgebraicGeometry.ProjectiveSpaceHigherDirectImage.MiddleVanishing.isZero_rightDerivedPlus_pushforward_twistOver_of_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpaceHigherDirectImage/MiddleVanishing.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpaceHigherDirectImage/MiddleVanishing.lean#L238). The attribute's comment: “the vanishing row, whole: R^q f_* 𝒪(d) = 0 for every q ≠ 0, n, every scheme S, every n and every integer d. The q = 0 row is ProjectiveSpaceHigherDirectImage.baseDegreeSheafIsoRightDerivedPushforwardTwistOver in ...DegreeZeroRow; the q = n row is ...rightDerivedPlusTopIsoDualBaseDegreeSheaf in ...TopDegreeRowGeneral, for every twist d over an arbitrary base. The whole display, its three rows in one statement at n >= 1, is ...rightDerivedPlusPushforwardTwistOverDisplay in ...Display”.

> **The vanishing row of [Stacks, Tag 01XW].** For the structure morphism `f : ℙⁿ_S ⟶ S` over
> an arbitrary scheme `S`, an arbitrary `n` and an arbitrary integer `d`, the higher direct image
> `Rᵠ f_* 𝒪(d)` is zero in every degree `q` with `q ≠ 0` and `q ≠ n`.

```lean
theorem isZero_rightDerivedPlus_pushforward_twistOver_of_ne (n : ℕ) (S : Scheme.{u}) (d : ℤ)
    (q : ℤ) (hq0 : q ≠ 0) (hqn : q ≠ (n : ℤ)) :
    IsZero (((Scheme.Modules.pushforward (projectiveSpaceOver n S ↘ S)).rightDerivedPlus q).obj
      (twistOver n S d))
```

## Tag 01XX, a lemma

[Tag 01XX](https://stacks.math.columbia.edu/tag/01XX) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjectiveBundleCohomology.higherDirectImageZeroIso_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/BaseChangeCompatibility.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/BaseChangeCompatibility.lean#L118). The attribute's comment: “compatibility with base change, the q = 0 row: for g : S' → S and E' ≅ g^*E, the base change map g^* R^0 π_* O(d) → R^0 π'_* O(d) followed by R^0 π'_* O(d) ≅ Sym^d(E') is g^*(R^0 π_* O(d) ≅ Sym^d(E)) followed by g^* Sym^d(E) ≅ Sym^d(E'), for every d ≥ 0 and n ≥ 1”.

> **[Stacks, Tag 01XX], compatibility with base change, the row `q = 0`**: for a morphism of
> schemes `g : S' ⟶ S`, `E` finite locally free of constant rank `n + 1` with `n ≥ 1`, `E' ≅ g^*E`
> and every `d ≥ 0`, the base change map `g^* R⁰π_* 𝒪_{𝐏(E)}(d) ⟶ R⁰π'_* 𝒪_{𝐏(E')}(d)` corresponds,
> under the identifications `R⁰π_* 𝒪(d) ≅ Sym^d(E)` and `R⁰π'_* 𝒪(d) ≅ Sym^d(E')`, to
> `g^* Sym^d(E) ≅ Sym^d(E')`.

```lean
public theorem higherDirectImageZeroIso_baseChange (hn : 1 ≤ n) (d : ℕ) :
    bundleTwistBaseChange g E hfree E' hE D D' 0 (d : ℤ) ≫
        (higherDirectImageZeroIso E' (isFiniteLocallyFreeOfRank_of_iso_pullback g E hfree E' hE)
          D' hn d).hom =
      (Scheme.Modules.pullback g).map (higherDirectImageZeroIso E hfree D hn d).hom ≫
        bundleSymBaseChange g E hfree E' hE (d : ℤ)
```

**`Stacks.AlgebraicGeometry.ProjectiveBundleCohomology.higherDirectImageTopIso_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/BaseChangeCompatibility.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/BaseChangeCompatibility.lean#L161). The attribute's comment: “compatibility with base change, the q = n row: for g : S' → S and E' ≅ g^*E, the base change map g^* R^n π_* O(d) → R^n π'_* O(d) followed by R^n π'_* O(d) ≅ SheafHom(Sym^(-n-1-d)(E') ⊗ ∧^(n+1) E', O_S') is g^*(R^n π_* O(d) ≅ SheafHom(Sym^(-n-1-d)(E) ⊗ ∧^(n+1) E, O_S)) followed by the canonical map g^* SheafHom(M, O_S) → SheafHom(g^* M, O_S') and g^*(Sym^(-n-1-d)(E) ⊗ ∧^(n+1) E) ≅ Sym^(-n-1-d)(E') ⊗ ∧^(n+1) E', for every integer d and n ≥ 1”.

> **[Stacks, Tag 01XX], compatibility with base change, the row `q = n`**: for a morphism of
> schemes `g : S' ⟶ S`, `E` finite locally free of constant rank `n + 1` with `n ≥ 1`, `E' ≅ g^*E`
> and every integer `d`, the base change map `g^* Rⁿ π_* 𝒪_{𝐏(E)}(d) ⟶ Rⁿ π'_* 𝒪_{𝐏(E')}(d)`
> corresponds, under the identifications `Rⁿ π_* 𝒪(d) ≅ SheafHom(Sym^{-n-1-d}(E) ⊗ ⋀ⁿ⁺¹ E, 𝒪_S)`
> and `Rⁿ π'_* 𝒪(d) ≅ SheafHom(Sym^{-n-1-d}(E') ⊗ ⋀ⁿ⁺¹ E', 𝒪_{S'})`, to the canonical map
> `g^* SheafHom(Sym^{-n-1-d}(E) ⊗ ⋀ⁿ⁺¹ E, 𝒪_S) ⟶ SheafHom(Sym^{-n-1-d}(E') ⊗ ⋀ⁿ⁺¹ E', 𝒪_{S'})`.

```lean
public theorem higherDirectImageTopIso_baseChange (hn : 1 ≤ n) (d : ℤ) :
    bundleTwistBaseChange g E hfree E' hE D D' n d ≫
        (higherDirectImageTopIso E' (isFiniteLocallyFreeOfRank_of_iso_pullback g E hfree E' hE)
          D' hn d).hom =
      (Scheme.Modules.pullback g).map (higherDirectImageTopIso E hfree D hn d).hom ≫
        bundleTopTargetBaseChange g E hfree E' hE d
```

**`Stacks.AlgebraicGeometry.ProjectiveBundleCohomology.isIso_bundleTwistBaseChange_of_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/BaseChangeCompatibility.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/BaseChangeCompatibility.lean#L179). The attribute's comment: “compatibility with base change, the vanishing rows: for g : S' → S, E' ≅ g^*E and q ≠ 0, n the base change map g^* R^q π_* O(d) → R^q π'_* O(d) is an isomorphism between zero modules, for every integer d”.

> **[Stacks, Tag 01XX], compatibility with base change, the vanishing rows**: for `q ≠ 0, n` the
> base change map `g^* R^q π_* 𝒪_{𝐏(E)}(d) ⟶ R^q π'_* 𝒪_{𝐏(E')}(d)` is an isomorphism of zero
> modules, for every integer `d`.

```lean
public theorem isIso_bundleTwistBaseChange_of_ne (q : ℕ) (d : ℤ) (hq0 : q ≠ 0) (hqn : q ≠ n) :
    IsIso (bundleTwistBaseChange g E hfree E' hE D D' q d)
```

**`Stacks.AlgebraicGeometry.ProjectiveBundleCohomology.isIso_bundleTwistBaseChange_zero_of_neg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/BaseChangeCompatibility.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/BaseChangeCompatibility.lean#L194). The attribute's comment: “compatibility with base change, the q = 0 row for d < 0: for g : S' → S and E' ≅ g^*E the base change map g^* R^0 π_* O(d) → R^0 π'_* O(d) is an isomorphism between zero modules, for n ≥ 1”.

> **[Stacks, Tag 01XX], compatibility with base change, the row `q = 0` for `d < 0`**: the base
> change map `g^* R⁰π_* 𝒪_{𝐏(E)}(d) ⟶ R⁰π'_* 𝒪_{𝐏(E')}(d)` is an isomorphism of zero modules.

```lean
public theorem isIso_bundleTwistBaseChange_zero_of_neg (hn : 1 ≤ n) {d : ℤ} (hd : d < 0) :
    IsIso (bundleTwistBaseChange g E hfree E' hE D D' 0 d)
```

**`Stacks.AlgebraicGeometry.ProjectiveBundleCohomology.higherDirectImage_iso_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/IsoTopRowIso.lean, line 744](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/IsoTopRowIso.lean#L744). The attribute's comment: “compatibility with isomorphisms between locally free sheaves, every row: for an isomorphism e : E ≅ E' of finite locally free modules of constant rank n + 1, n ≥ 1, over an arbitrary scheme S, the maps R^q π_* O(d) → R^q π'_* O(d) induced by e and P(E') ≅ P(E) carry the identification R^0 π_* O(d) ≅ Sym^d(E) to R^0 π'_* O(d) ≅ Sym^d(E') under Sym^d(e) for d ≥ 0, are zero for q = 0, d < 0 and for q ≠ 0, n, and carry R^n π_* O(d) ≅ SheafHom(Sym^(-n-1-d)(E) ⊗ ∧^(n+1) E, O_S) to the same identification for E' under the dual of Sym^(-n-1-d)(e⁻¹) ⊗ ∧^(n+1)(e⁻¹), for every integer d”.

> **[Stacks, Tag 01XX]: the identifications of the higher direct images of the twists on a
> projective bundle are compatible with isomorphisms between locally free sheaves.** Let
> `e : E ≅ E'` be an isomorphism of finite locally free `𝒪_S`-modules of constant rank `n + 1`,
> `n ≥ 1`, inducing `𝐏(E') ≅ 𝐏(E)` over `S` and the maps
> `R^q π_* 𝒪_{𝐏(E)}(d) ⟶ R^q π'_* 𝒪_{𝐏(E')}(d)` (`higherDirectImageIsoMap`). For every pair
> `(q, d)` of integers:
> * `q = 0`, `d ≥ 0`: the identifications `R⁰π_* 𝒪(d) ≅ Sym^d` correspond under `Sym^d(e)`;
> * `q = 0`, `d < 0`, and `q ≠ 0, n`: the induced map is zero, between modules that vanish;
> * `q = n`: the identifications `Rⁿ π_* 𝒪(d) ≅ SheafHom(Sym^{-n-1-d}(E) ⊗ ⋀ⁿ⁺¹ E, 𝒪_S)`
>   correspond under the dual of `Sym^{-n-1-d}(e⁻¹) ⊗ ⋀ⁿ⁺¹(e⁻¹)`.

```lean
public theorem higherDirectImage_iso_compatible :
    (∀ d : ℕ, higherDirectImageIsoMap hfree hfree' e D D' 0 d ≫
        (higherDirectImageZeroIso E' hfree' D' hn d).hom =
      (higherDirectImageZeroIso E hfree D hn d).hom ≫ (symHom hfree hfree' e.hom).app (d : ℤ)) ∧
    (∀ d : ℤ, d < 0 → higherDirectImageIsoMap hfree hfree' e D D' 0 d = 0) ∧
    (∀ q d : ℤ, q ≠ 0 → q ≠ n → higherDirectImageIsoMap hfree hfree' e D D' q d = 0) ∧
    (∀ d : ℤ,
      haveI := isQuasicoherent_of_isFiniteLocallyFreeOfRank E hfree
      haveI := isQuasicoherent_of_isFiniteLocallyFreeOfRank E' hfree'
      higherDirectImageIsoMap hfree hfree' e D D' (n : ℤ) d ≫
          (higherDirectImageTopIso E' hfree' D' hn d).hom =
        (higherDirectImageTopIso E hfree D hn d).hom ≫ topRowTargetMap hfree hfree' e d)
```

**`Stacks.AlgebraicGeometry.ProjectiveBundleCohomology.isZero_higherDirectImage_twist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/Statement.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/Statement.lean#L81). The attribute's comment: “the vanishing row: R^q π_* O(d) = 0 for q ≠ 0, n, every integer d and every integer q, for E finite locally free of constant rank n + 1 over an arbitrary scheme S”. References: EGA III (2.1.15), “partial”.

> For `E` finite locally free of constant rank `n + 1` with projective bundle `π : 𝐏(E) ⟶ S`,
> `R^q π_* 𝒪_{𝐏(E)}(d) = 0` for every integer `d` and every integer `q` with `q ≠ 0` and `q ≠ n`.

```lean
public theorem isZero_higherDirectImage_twist (d q : ℤ) (hq0 : q ≠ 0) (hqn : q ≠ n) :
    IsZero (((Scheme.Modules.pushforward
        (relativeProj (bundleAlgebra E hfree)).toBase).rightDerivedPlus
      q).obj (D.algebra.piece d))
```

**`Stacks.AlgebraicGeometry.ProjectiveBundleCohomology.isIso_symToPushforwardTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/Statement.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/Statement.lean#L92). The attribute's comment: “the q = 0 row in degrees d ≥ 0, in the canonical form: the map Sym^d(E) → π_* O(d) of Tag 01NR is an isomorphism, for n ≥ 1”.

> **The canonical map `Sym^d(E) ⟶ π_* 𝒪_{𝐏(E)}(d)` is an isomorphism**, for `n ≥ 1` and
> `d ≥ 0`.

```lean
public theorem isIso_symToPushforwardTwist (hn : 1 ≤ n) (d : ℕ) : IsIso (D.ψ d)
```

**`Stacks.AlgebraicGeometry.ProjectiveBundleCohomology.higherDirectImageZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/Statement.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/Statement.lean#L99). The attribute's comment: “the q = 0 row, d ≥ 0: R^0 π_* O(d) ≅ Sym^d(E), for n ≥ 1”.

> `R^0 π_* 𝒪_{𝐏(E)}(d) ≅ Sym^d(E)` for `d ≥ 0`: the comparison `R^0π_* = π_*` of
> [Stacks, Tag 05TD] followed by the inverse of the canonical map of Tag 01NR.

```lean
public def higherDirectImageZeroIso (hn : 1 ≤ n) (d : ℕ) :
    ((Scheme.Modules.pushforward (relativeProj (bundleAlgebra E hfree)).toBase).rightDerivedPlus
      0).obj (D.algebra.piece (d : ℤ)) ≅ (bundleAlgebra E hfree).piece (d : ℤ)
```

**`Stacks.AlgebraicGeometry.ProjectiveBundleCohomology.isZero_higherDirectImage_zero_of_neg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/Statement.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/Statement.lean#L107). The attribute's comment: “the q = 0 row, d < 0: R^0 π_* O(d) = 0 = Sym^d(E), for n ≥ 1”.

> For `d < 0`, both `R^0 π_* 𝒪_{𝐏(E)}(d)` and `Sym^d(E)` vanish.

```lean
public theorem isZero_higherDirectImage_zero_of_neg (hn : 1 ≤ n) {d : ℤ} (hd : d < 0) :
    IsZero (((Scheme.Modules.pushforward
        (relativeProj (bundleAlgebra E hfree)).toBase).rightDerivedPlus
      0).obj (D.algebra.piece d)) ∧ IsZero ((bundleAlgebra E hfree).piece d)
```

**`Stacks.AlgebraicGeometry.ProjectiveBundleCohomology.higherDirectImageTopIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/Statement.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundleCohomology/Statement.lean#L122). The attribute's comment: “the q = n row, every integer d: R^n π_* O(d) ≅ SheafHom(Sym^(-n-1-d)(E) ⊗ ∧^(n+1) E, O_S), for E finite locally free of constant rank n + 1 over an arbitrary scheme S, n ≥ 1”. References: EGA III (2.1.16), “(ii)”.

> For `n ≥ 1` and every integer `d`,
> `Rⁿ π_* 𝒪_{𝐏(E)}(d) ≅ SheafHom(Sym^{-n-1-d}(E) ⊗ ⋀ⁿ⁺¹ E, 𝒪_S)`. For `d ≤ -n - 1` it is induced
> by the multiplication pairing `𝒪(d) ⊗ π^* Sym^{-n-1-d}(E) ⟶ 𝒪(-n-1)` and the trace
> `Rⁿ π_* 𝒪(-n-1) ≅ (⋀ⁿ⁺¹ E)^∨`; for `d ≥ -n` both sides vanish.

```lean
public def higherDirectImageTopIso (hn : 1 ≤ n) (d : ℤ) :
    ((Scheme.Modules.pushforward (relativeProj (bundleAlgebra E hfree)).toBase).rightDerivedPlus
      (n : ℤ)).obj (D.algebra.piece d) ≅
      Stacks.AlgebraicGeometry.ReflexiveModules.dualSheaf
        ((Stacks.ProjectionFormula.tensorRightInvertible S
          (Scheme.Modules.exteriorPower E ((n + 1 : ℕ) : ℤ))).obj
          ((bundleAlgebra E hfree).piece (-(n : ℤ) - 1 - d)))
```

**`Stacks.AlgebraicGeometry.ProjectiveBundleVanishing.isZero_rightDerivedPlus_pushforward_twist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpaceHigherDirectImage/BundleTwistVanishing.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpaceHigherDirectImage/BundleTwistVanishing.lean#L391). The attribute's comment: “the vanishing clause in the degrees above the relative dimension and below zero”. References: EGA III (2.1.15), “partial”.

> **The higher direct images of the twists on a projective bundle vanish outside the relative
> dimension.** Let `E` be an `𝒪_S`-module which is finite locally free of constant rank `n + 1`,
> let `π : 𝐏(E) = Proj_S(Sym(E)) ⟶ S` be the structure morphism of its projective bundle and let
> `𝒪_{𝐏(E)}(d)` be the degree-`d` homogeneous piece of a family of twists on it. Then
> `R^q π_* 𝒪_{𝐏(E)}(d)` is zero whenever `q < 0` or `q > n`.
>
> Below degree zero this is the vanishing of any right derived functor in negative degrees. Above
> degree `n` the affine opens over which `E` is free form a basis of `S`, over such an open the
> section ring of `Sym(E)` is generated by `n + 1` degree-one elements, and
> `Stacks.AlgebraicGeometry.ProjectiveBundleVanishing.isZero_rightDerivedPlus_pushforward_piece`
> turns that into the vanishing. The vanishing in every degree `q ≠ 0, n` is
> `Stacks.AlgebraicGeometry.ProjectiveBundleCohomology.isZero_higherDirectImage_twist`.

```lean
public theorem isZero_rightDerivedPlus_pushforward_twist (n : ℕ)
    (hqc : Stacks.SymGraded.IsQuasicoherentPieces E)
    (hfree : Scheme.Modules.IsFiniteLocallyFreeOfRank E (n + 1))
    (D : TwistData (Stacks.SymGraded.schemeSheafGradedAlgebra E hqc)) (d : ℤ) (q : ℤ)
    (hq : q < 0 ∨ (n : ℤ) < q) :
    IsZero (((Scheme.Modules.pushforward
        (relativeProj (Stacks.SymGraded.schemeSheafGradedAlgebra E hqc)).toBase).rightDerivedPlus
      q).obj (D.algebra.piece d))
```

**`Stacks.AlgebraicGeometry.ProjectiveBundleVanishing.TopDegree.topCohomologyTwistIsoSymTensorDet`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpaceHigherDirectImage/TopDegreeTwistIdentification.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpaceHigherDirectImage/TopDegreeTwistIdentification.lean#L100). The attribute's comment: “the q = n identification for an affine base S = Spec R and a free module E = R^(n+1), n ≥ 1, on the cohomology module H^n(P(E), O(d))”.

> **The top cohomology of the twists on projective space**: for a commutative ring `R`, for
> `n = m + 1 ≥ 1`, an integer `d` and a natural number `k` with `k = -n - 1 - d`,
>
>   `H^n(𝐏(E), 𝒪(d)) ≅ Hom_R(Sym^k(E) ⊗_R ⋀^{n+1}E, R)`,  `E = R^{⊕ n+1}`,
>
> as `R`-modules.

```lean
public def topCohomologyTwistIsoSymTensorDet (R : Type u) [CommRing R] (m : ℕ) (d : ℤ) (k : ℕ)
    (hk : (k : ℤ) = -((m + 1 : ℕ) : ℤ) - 1 - d) :
    Stacks.ProjectiveSpace.Cohomology.twistCohomology R (m + 1) d (m + 1) ≅
      ModuleCat.of R
        (TensorProduct R (SymPow.symmetricPower k R (Fin (m + 1 + 1) → R))
            (⋀[R]^(m + 1 + 1) (Fin (m + 1 + 1) → R)) →ₗ[R] R)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.8, Tag 01XS](https://stacks.math.columbia.edu/tag/01XS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
