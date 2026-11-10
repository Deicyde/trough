---
declaration: section
origin: cited
lean: Stacks.ProjectiveCohomology.isZero_Hgroup_of_lt, Stacks.ProjectiveSpace.exists_epi_biproduct_tensorPowModule, Stacks.ProjectiveSpace.SerreVanishing.moduleFinite_cohomology_of_isCoherent, Stacks.ProjectiveSpace.SerreVanishing.exists_isZero_Hgroup_twist_of_isCoherent, Stacks.ProjectiveSpace.Cohomology.isZero_cohomology_of_lt_zero_or_dim_lt, Stacks.ProjectiveSpace.Cohomology.moduleFinite_truncation_of_isCoherent, Stacks.ProjCoherentDegreeOne.proj_isNoetherian_and_forall_isCoherent, Stacks.AlgebraicGeometry.Proj.isNoetherian_proj
statement: formalized
proof: formalized
---

# 30.14 Coherent sheaves on Proj, I

Section 30.14 of the Stacks Project, [Tag 01YR](https://stacks.math.columbia.edu/tag/01YR). 4 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01YS, a lemma

[Tag 01YS](https://stacks.math.columbia.edu/tag/01YS) in the Stacks Project.

**`Stacks.ProjectiveCohomology.isZero_Hgroup_of_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveCohomology/Basic.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveCohomology/Basic.lean#L256). The attribute's comment: “clause (2), vanishing above the dimension”. References: EGA III (2.2.2), “(ii), P^n case”.

> **[Stacks, Tag 01YS], clause (2).** The cohomology of a quasi-coherent module on projective
> `n`-space over a ring vanishes in every degree above `n`.
>
> Projective space is covered by its `n + 1` standard charts, all affine, and it is separated,
> hence has affine diagonal; [Stacks, Tag 01XI] then bounds the cohomological degree by `n + 1`.
> As the source observes, no Noetherian hypothesis is needed, and the conclusion holds for every
> quasi-coherent module, not only coherent ones. The source's remaining range `i < 0` is vacuous
> in this spelling, where cohomology is indexed by `ℕ`.

```lean
theorem isZero_Hgroup_of_lt (F : (projectiveSpaceOverRing n R).Modules) [F.IsQuasicoherent]
    (q : ℕ) (hq : n < q) :
    IsZero (Hgroup (projectiveSpaceOverRing n R).ringCatSheaf ⊤ q F)
```

**`Stacks.ProjectiveSpace.exists_epi_biproduct_tensorPowModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/CoherentQuotientOfTwists.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/CoherentQuotientOfTwists.lean#L88). The attribute's comment: “assertion (1)”.

> **Assertion (1) of [Stacks, Tag 01YS].** A quasi-coherent module of finite type on projective
> `n`-space over an affine base is a quotient of a finite direct sum of twists
> `𝒪(d₁), …, 𝒪(d_r)` of the structure sheaf, and the degrees may be taken below any prescribed
> integer.
>
> The source assumes the base ring Noetherian and the module coherent; neither is needed, and
> `Stacks.ProjectiveSpace.exists_epi_biproduct_of_isCoherent` is the source's reading.
>
> The proof is the source's: `𝒪(1)` is ample on `ℙⁿ_S`
> (`Stacks.ProjectiveSpace.isAmple_projectiveSpaceTwistingSheaf`), and clause (8) of
> [Stacks, Tag 01Q3] (`Stacks.AmpleLocalGeneration.isQuotientOfNegativeTwists_of_isAmple`) presents
> a finite-type quasi-coherent module as a quotient of a finite direct sum of negative tensor
> powers of an ample invertible module.

```lean
theorem exists_epi_biproduct_tensorPowModule (n : ℕ) (S : Scheme.{u}) [IsAffine S] (k : ℤ)
    (F : (projectiveSpaceOver n S).Modules) (hFqc : F.IsQuasicoherent)
    (hFft : SheafOfModules.IsFiniteType.{u, u, u} F) :
    ∃ (r : ℕ) (d : Fin r → ℤ)
      (b : Bicone fun j : Fin r => tensorPowModule (projectiveSpaceOver n S)
        (projectiveSpaceTwistingSheaf n S) (d j))
      (_ : b.IsBilimit) (p : b.pt ⟶ F), Epi p ∧ ∀ j, d j ≤ k
```

**`Stacks.ProjectiveSpace.SerreVanishing.moduleFinite_cohomology_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/CoherentSerreVanishing.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/CoherentSerreVanishing.lean#L217). The attribute's comment: “(3) finiteness of the cohomology modules”. References: EGA III (2.2.2), “clause (i), special case”.

> **[Stacks, Tag 01YS] clause (3).** Let `R` be a Noetherian ring, `n ≥ 0` and `ℱ` a coherent
> sheaf on `ℙⁿ_R = Proj R[T₀, …, Tₙ]`. For every `i` the cohomology `H^i(ℙⁿ_R, ℱ)` is a finite
> `R`-module.
>
> The proof is the source's descending induction on `i`: it holds above degree `n` because the
> cohomology vanishes there (clause (2)), the twists `𝒪(d)` have finite cohomology
> ([Stacks, Tag 01XT]), and `ℱ` is a quotient of a finite direct sum of twists (clause (1) of the
> same tag), so the long exact sequence of the kernel sequence places `H^i(ℙⁿ_R, ℱ)` between two
> finite modules over the Noetherian ring `R`.

```lean
theorem moduleFinite_cohomology_of_isCoherent [IsNoetherianRing R]
    (F : (AlgebraicGeometry.Proj (polyGrading R n)).Modules)
    (hF : _root_.SheafOfModules.IsCoherent F) (q : ℕ) :
    Module.Finite R
      ((ModuleCat.restrictScalars ((Scheme.ΓSpecIso (CommRingCat.of R)).inv ≫
          (Stacks.AlgebraicGeometry.ProjPolyChart.projToSpecCoeff R n).appTop).hom).obj
        (((Stacks.Cohomology.AffineBase.moduleGlobalSections
          (AlgebraicGeometry.Proj (polyGrading R n))).rightDerived q).obj F))
```

**`Stacks.ProjectiveSpace.SerreVanishing.exists_isZero_Hgroup_twist_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/CoherentSerreVanishing.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/CoherentSerreVanishing.lean#L243). The attribute's comment: “(4) eventual vanishing of the higher cohomology of the twists”.

> **[Stacks, Tag 01YS] clause (4).** Let `R` be a Noetherian ring, `n ≥ 0` and `ℱ` a coherent
> sheaf on `ℙⁿ_R = Proj R[T₀, …, Tₙ]`. For every `i > 0` the cohomology `H^i(ℙⁿ_R, ℱ(d))` vanishes
> for all `d` large enough.
>
> The proof is the source's: `ℱ` is a quotient of a finite direct sum of twists
> (`hasTwistQuotients_polyGrading`, clause (1) of the same tag), the twists are eventually acyclic
> (`hasEventuallyAcyclicTwists_polyGrading`, from the computation of `H^i(ℙⁿ_R, 𝒪(d))` of
> [Stacks, Tag 01XT]), and the dévissage descends on the cohomological degree from the degree above
> which everything vanishes.

```lean
theorem exists_isZero_Hgroup_twist_of_isCoherent [IsNoetherianRing R] (i : ℕ) (hi : 0 < i)
    (F : (AlgebraicGeometry.Proj (polyGrading R n)).Modules)
    (hF : _root_.SheafOfModules.IsCoherent F) :
    ∃ d₀ : ℤ, ∀ d : ℤ, d₀ ≤ d →
      IsZero (Hgroup (projRingSheaf (polyGrading R n)) ⊤ i
        (twistSheafOfModules (polyGrading R n) F d))
```

**`Stacks.ProjectiveSpace.Cohomology.isZero_cohomology_of_lt_zero_or_dim_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/CohomologicalDimension.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/CohomologicalDimension.lean#L64). The attribute's comment: “assertion (2)”. References: EGA III (2.2.2), “(ii), P^n case”.

> **The cohomological dimension of projective space**: the cohomology of a quasi-coherent
> module on projective `n`-space over an affine base vanishes in every degree outside `0, …, n`.

```lean
theorem isZero_cohomology_of_lt_zero_or_dim_lt (n : ℕ) (S : Scheme.{u}) [IsAffine S]
    (F : (projectiveSpaceOver n S).Modules) [F.IsQuasicoherent] (i : ℤ)
    (hi : i < 0 ∨ (n : ℤ) < i) :
    IsZero (((sectionsFunctor (projectiveSpaceOver n S) ⊤).rightDerivedPlus i).obj F)
```

**`Stacks.ProjectiveSpace.Cohomology.moduleFinite_truncation_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/TwistSectionsDegreeOne.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Cohomology/TwistSectionsDegreeOne.lean#L291). The attribute's comment: “(5) finiteness of the graded module of twisted global sections”. References: SGA 2 XII (5.3), “clause (a), case i = 0”.

> **[Stacks, Tag 01YS] clause (5).** Let `R` be a Noetherian ring, `n ≥ 0` and `ℱ` a coherent
> sheaf on `ℙⁿ_R = Proj R[T₀, …, Tₙ]`. For every `k ∈ ℤ` the graded `R[T₀, …, Tₙ]`-module
> `⨁_{d ≥ k} H⁰(ℙⁿ_R, ℱ(d))` is a finite `R[T₀, …, Tₙ]`-module.
>
> The proof is the source's sandwich, now with both halves available: each homogeneous piece
> `Γ(ℙⁿ_R, ℱ(d))` is a finite `R`-module by clause (3) at `i = 0`, and above some degree every
> piece lies in the span of the piece one degree below
> (`exists_forall_subset_span_twistedGlobalSectionsGrading`), so finitely many pieces generate.

```lean
theorem moduleFinite_truncation_of_isCoherent [IsNoetherianRing R]
    (F : SheafOfModules.{u} (projRingSheaf R n))
    (hF : _root_.SheafOfModules.IsCoherent F)
    (D : TwistedGlobalSectionsModule (polyGrading R n) F) (k : ℤ) :
    letI := D.moduleInst
    Module.Finite (MvPolynomial (Fin (n + 1)) R)
      (TwistedGlobalSectionsModule.truncation (polyGrading R n) F D k)
```

## Tag 0AG6, a lemma

[Tag 0AG6](https://stacks.math.columbia.edu/tag/0AG6) in the Stacks Project.

**`Stacks.ProjCoherentDegreeOne.proj_isNoetherian_and_forall_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjCoherentDegreeOne/Main.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjCoherentDegreeOne/Main.lean#L110). References: EGA III (2.2.2).

> **[Stacks, Tag 0AG6].** Let `A` be a graded ring such that `A₀` is Noetherian and `A` is
> generated by finitely many elements of `A₁` over `A₀`. Set `X = Proj A`. Then `X` is a Noetherian
> scheme, and for every coherent `𝒪_X`-module `ℱ`:
>
> 1. there exist an `r ≥ 0`, integers `d₁, …, d_r` and a surjection
>    `⨁_{j = 1, …, r} 𝒪_X(d_j) ⟶ ℱ`;
> 2. for every `p` the cohomology group `H^p(X, ℱ)` is a finite `A₀`-module;
> 3. if `p > 0` then `H^p(X, ℱ(d)) = 0` for all `d` large enough;
> 4. for every `k ∈ ℤ` the graded `A`-module `⨁_{d ≥ k} H⁰(X, ℱ(d))` is a finite `A`-module.

```lean
theorem proj_isNoetherian_and_forall_isCoherent :
    AlgebraicGeometry.IsNoetherian (AlgebraicGeometry.Proj 𝒜) ∧
      ∀ F : SheafOfModules.{u} (projRingSheaf 𝒜), _root_.SheafOfModules.IsCoherent F →
        (∃ (r : ℕ) (d : Fin r → ℤ),
            ∃ φ : (∐ fun j : Fin r => twistingSheaf 𝒜 (d j)) ⟶ F, Epi φ) ∧
          (∀ p : ℕ, Module.Finite (𝒜 0)
            ((ModuleCat.restrictScalars ((Scheme.ΓSpecIso (.of (𝒜 0))).inv ≫
                (AlgebraicGeometry.Proj.toSpecZero 𝒜).appTop).hom).obj
              (((moduleGlobalSections (AlgebraicGeometry.Proj 𝒜)).rightDerived p).obj F))) ∧
          (∀ p : ℕ, 0 < p → ∃ d₀ : ℤ, ∀ d : ℤ, d₀ ≤ d →
            IsZero (Hgroup (projRingSheaf 𝒜) ⊤ p (twistSheafOfModules 𝒜 F d))) ∧
          (∀ k : ℤ,
            letI := (twistedGlobalSectionsModule 𝒜 F).moduleInst
            Module.Finite A (TwistedGlobalSectionsModule.truncation 𝒜 F
              (twistedGlobalSectionsModule 𝒜 F) k))
```

Declarations registered for the tag:

- [`Stacks.AlgebraicGeometry.Proj.isNoetherian_proj`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjNoetherian/Basic.lean#L135), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/ProjNoetherian.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/ProjNoetherian.lean#L29) (StacksFrontier): “proj_noetherian”.

## Tag 0AG7, a lemma

[Tag 0AG7](https://stacks.math.columbia.edu/tag/0AG7) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjLargeDegreeSections.exists_bijective_degreeNToGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjLargeDegreeSections/Basic.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjLargeDegreeSections/Basic.lean#L114). The attribute's comment: “bijectivity in all large degrees, from homogeneous generators of the kernel and of the cokernel annihilated, respectively carried into the image, by a power of the irrelevant ideal”.

> The comparison maps are bijective in all large degrees, with the finiteness input of the
> source replaced by homogeneous generating data for the kernel and the cokernel of the comparison.
>
> In every degree `n` the canonical map `𝒨 n ⟶ Γ(Proj 𝒮, M(n)~)` of Equation 01MR is
> `degreeNToGlobalSections`. Assume `S` is generated in degree one over `𝒮 0` and:
>
> * the kernel is generated degreewise by `x : Fin ck → M` placed in degrees `dx`, and a power of
>   the irrelevant ideal annihilates every `x j`;
> * the cokernel is generated degreewise by sections `y k` of `M(dy k)~`, and a power of the
>   irrelevant ideal carries every `y k` into the image of the comparison.
>
> Then the comparison is bijective in every sufficiently large degree. The statement does not
> assume that `𝒨` is a decomposition of `M`.

```lean
theorem exists_bijective_degreeNToGlobalSections
    (hgen : Algebra.adjoin (𝒮 0) (𝒮 1 : Set S) = ⊤)
    {ck : ℕ} (x : Fin ck → M) (dx : Fin ck → ℤ) (Nx : Fin ck → ℕ)
    (hxtors : ∀ j, ∀ a ∈ (HomogeneousIdeal.irrelevant 𝒮).toIdeal ^ Nx j, a • x j = 0)
    (hxgen : ∀ n : ℤ, (∀ j, dx j ≤ n) → ∀ m : 𝒨 n,
      degreeNToGlobalSections 𝒮 𝒨 n m = 0 →
        ∃ a : (j : Fin ck) → 𝒮 (n - dx j).toNat, (m : M) = ∑ j, (a j : S) • x j)
    {cq : ℕ} (dy : Fin cq → ℤ) (Ny : Fin cq → ℕ)
    (y : (k : Fin cq) → shiftedSectionsComponent 𝒮 𝒨 (dy k))
    (hytors : ∀ (k : Fin cq) (i : ℕ) (a : 𝒮 i),
      (a : S) ∈ (HomogeneousIdeal.irrelevant 𝒮).toIdeal ^ Ny k →
        ∃ m : 𝒨 ((i : ℤ) + dy k),
          homogeneousScalarGlobalSections 𝒮 𝒨 i (dy k) a (y k)
            = degreeNToGlobalSections 𝒮 𝒨 ((i : ℤ) + dy k) m)
    (hygen : ∀ (n : ℤ) (hn : ∀ k, dy k ≤ n) (s : shiftedSectionsComponent 𝒮 𝒨 n),
      ∃ (m : 𝒨 n) (a : (k : Fin cq) → 𝒮 (n - dy k).toNat),
        s = degreeNToGlobalSections 𝒮 𝒨 n m +
          ∑ k, ofDegreeEq 𝒮 𝒨 (show (((n - dy k).toNat : ℤ) + dy k) = n by
              have := hn k; omega)
            (homogeneousScalarGlobalSections 𝒮 𝒨 ((n - dy k).toNat) (dy k) (a k) (y k))) :
    ∃ n₀ : ℤ, ∀ n : ℤ, n₀ ≤ n → Function.Bijective (degreeNToGlobalSections 𝒮 𝒨 n)
```

**`Stacks.AlgebraicGeometry.ProjLargeDegreeSections.exists_bijective_degreeNToGlobalSections_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjLargeDegreeSections/Noetherian.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjLargeDegreeSections/Noetherian.lean#L322). The attribute's comment: “the maps M_n to Gamma(Proj A, M(n)~) of Equation 01MR are isomorphisms in all sufficiently large degrees, for A_0 Noetherian, A generated over A_0 by finitely many elements of A_1, and M a finite graded A-module”.

> Let `S = ⨁_{d ≥ 0} 𝒮 d` be a graded ring whose degree-zero part is Noetherian and which is
> generated over that part by finitely many elements `fam 0, …` of `𝒮 1`, let `M = ⨁_{n ∈ ℤ} 𝒨 n`
> be a finite graded `S`-module and `X = Proj 𝒮`. The canonical maps
>
> `𝒨 n ⟶ Γ(X, M(n)~)`
>
> of Equation 01MR are isomorphisms for all sufficiently large `n`.

```lean
theorem exists_bijective_degreeNToGlobalSections_of_finite [IsNoetherianRing ↥(𝒮 0)]
    [Module.Finite S M] {r : ℕ} (fam : Fin r → S) (hfam : ∀ i, fam i ∈ 𝒮 1)
    (hgen : Algebra.adjoin ↥(𝒮 0) (Set.range fam) = ⊤) :
    ∃ n₀ : ℤ, ∀ n : ℤ, n₀ ≤ n → Function.Bijective (degreeNToGlobalSections 𝒮 𝒨 n)
```

## Tag 0BXD, a proposition

[Tag 0BXD](https://stacks.math.columbia.edu/tag/0BXD) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjSerreCorrespondence.equivalence_coherentQuotientFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/Equivalence.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/Equivalence.lean#L458). The attribute's comment: “the equivalence Mod^fg_A / Mod^fg_{A,torsion} ⟶ Coh(O_X) induced by M ↦ M~, with quasi-inverse F ↦ ⨁_{n ≥ 0} Γ(X, F(n)), at the source's hypotheses: A_0 Noetherian and A generated by finitely many elements of A_1 over A_0. The torsion subcategory is the irrelevant finitely generated graded modules in generation degree one, which for a Noetherian A generated in degree one is the source's Mod^fg_{A,torsion}. The Noetherianity of A, its finite type over A_0 and the quasi-compactness of Proj A are derived from those hypotheses rather than assumed, which is why the statement opens with haveI. The equality clauses pin the functor to M ↦ M~ and the inverse to F ↦ ⨁_{n ≥ 0} Γ(X, F(n)) on the nose, and the last clause says the functor is induced by M ↦ M~”. References: EGA III (2.3.3), “(F), special case”.

> Let `A` be a graded ring such that `A₀` is Noetherian and `A` is generated by finitely many
> elements of `A₁` over `A₀`, and set `X = Proj A`. Then `M ↦ M̃` induces an equivalence
>
> `Mod^fg_A / Mod^fg_{A, torsion} ⟶ Coh(𝒪_X)`
>
> whose quasi-inverse is `ℱ ↦ ⨁_{n ≥ 0} Γ(X, ℱ(n))`.
>
> The third clause is what says the equivalence is *induced* by `M ↦ M̃`: composed with the quotient
> functor and read in all sheaves of `𝒪_X`-modules, its functor is the associated-sheaf functor on
> `Mod^fg_A`.

```lean
theorem equivalence_coherentQuotientFunctor :
    haveI := isNoetherianRing_of_adjoin_range 𝒜 x hx hgen
    haveI := finiteType_of_adjoin_range 𝒜 x hx hgen
    haveI : CompactSpace (AlgebraicGeometry.Proj 𝒜) :=
      QuasiCompact.compactSpace_of_compactSpace (AlgebraicGeometry.Proj.toSpecZero 𝒜)
    ∃ e : IrrelevantQuotient.{u, u, u} 𝒜 (d := 1) Nat.one_pos ≌
            Stacks.SheafOfModules.CoherentModules (projRingSheaf 𝒜),
      e.functor = coherentQuotientFunctor.{u, u} 𝒜 ∧
      e.inverse = nonnegTwistedSectionsQuotientFunctor 𝒜 x hx hgen ∧
      Nonempty (toIrrelevantQuotient.{u, u, u} 𝒜 Nat.one_pos ⋙ e.functor ⋙
        (Stacks.SheafOfModules.coherentModules (projRingSheaf 𝒜)).ι ≅
          finiteAssociatedSheafFunctor.{u, u} 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjSerreCorrespondence.isZero_associatedModuleSheaf_of_isIPowerTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/TorsionVanishing.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/TorsionVanishing.lean#L84). The attribute's comment: “the functor M ↦ M~ kills the torsion modules, the step that lets it be defined on the quotient category; stated for 𝒜₊-power torsion modules, with no finiteness, Noetherian or degree-one generation hypothesis”. References: EGA II (2.5.6), “sufficiency clause”.

> The associated sheaf `M̃` of an `𝒜₊`-power torsion graded module `M` is a zero object.

```lean
theorem isZero_associatedModuleSheaf_of_isIPowerTorsion
    (htor : IsIPowerTorsion S M (HomogeneousIdeal.irrelevant 𝒜).toIdeal) :
    Limits.IsZero (associatedModuleSheaf 𝒜 𝒨)
```

**`Stacks.AlgebraicGeometry.ProjSerreCorrespondence.isZero_associatedModuleSheaf_of_eventually_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/TorsionVanishing.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/TorsionVanishing.lean#L140). The attribute's comment: “the functor M ↦ M~ kills the torsion subcategory, with torsion in the form the source defines the subcategory Mod^fg_{A,torsion}: the homogeneous components vanish in all large degrees; no finiteness hypothesis is used”. References: EGA II (2.5.6), “sufficiency clause”; EGA II (2.7.2), “If M satisfies (TN)”; EGA II (2.7.3), “(ii)”; EGA II (3.4.2), “special case”.

> A graded module whose homogeneous components vanish in all sufficiently large degrees has zero
> associated sheaf.

```lean
theorem isZero_associatedModuleSheaf_of_eventually_eq_zero [DirectSum.Decomposition 𝒨] {N : ℤ}
    (hN : ∀ n : ℤ, N ≤ n → ∀ m : M, m ∈ 𝒨 n → m = 0) :
    Limits.IsZero (associatedModuleSheaf 𝒜 𝒨)
```

**`Stacks.AlgebraicGeometry.ProjSerreCorrespondence.isZero_associatedModuleSheafFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/TorsionVanishing.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/TorsionVanishing.lean#L151). The attribute's comment: “the bundled functor M ↦ M~ sends torsion graded modules to zero objects, the step that lets it be defined on the quotient category”.

> The associated-sheaf functor `M ↦ M̃` sends an `𝒜₊`-power torsion graded module to a zero
> object.

```lean
theorem isZero_associatedModuleSheafFunctor_obj (X : GradedModuleCat.{u, v, w} 𝒜)
    (htor : IsIPowerTorsion S X.carrier (HomogeneousIdeal.irrelevant 𝒜).toIdeal) :
    Limits.IsZero ((associatedModuleSheafFunctor 𝒜).obj X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.14, Tag 01YR](https://stacks.math.columbia.edu/tag/01YR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
