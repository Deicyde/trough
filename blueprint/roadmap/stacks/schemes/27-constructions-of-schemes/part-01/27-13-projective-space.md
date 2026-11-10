---
declaration: section
origin: cited
lean: Stacks.ProjectiveFromSections.toProjectiveSpaceOver, Stacks.ProjectiveSpaceModuli.bijective_pointsOfHom, Stacks.ProjectiveSpaceModuli.pointsEquiv, Stacks.ProjectiveSpaceModuli.pointsOfHom_comp, AlgebraicGeometry.projectiveSpace, AlgebraicGeometry.projectiveSpaceIntegralIso, AlgebraicGeometry.projectiveSpaceOver, AlgebraicGeometry.projectiveSpaceOverRing
statement: formalized
proof: formalized
---

# 27.13 Projective space

Section 27.13 of the Stacks Project, [Tag 01ND](https://stacks.math.columbia.edu/tag/01ND). 9 tags here are carried by 21 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01ND, the section

[Tag 01ND](https://stacks.math.columbia.edu/tag/01ND) in the Stacks Project.

**`Stacks.ProjectiveFromSections.toProjectiveSpaceOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveFromSections/Morphism.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveFromSections/Morphism.lean#L118). The attribute's comment: “the notation phi_(L, (s_0, ..., s_n)) of the section, as data: the morphism to P^n_S attached to an invertible module with n + 1 generating global sections, pinned on each standard chart. The scheme P^n_S itself is Tag 01NF (AlgebraicGeometry.projectiveSpaceOver). The section's characterisation of the morphism by L = phi^* O(1) and s_i = phi^* T_i is NOT proved: the comparison of L with the pullback of the hyperplane sheaf is the twist identification recorded as missing in StacksFrontier/AlgebraicGeometry/AmpleProjectiveImmersion/Basic.lean. The representability statement Tag 01NE is likewise not proved, only this direction of it”.

> **The morphism `φ_{(L, (s₀, …, sₙ))} : X ⟶ ℙⁿ_S` of Section 27.13**, attached to a structure
> morphism `f : X ⟶ S`, an invertible `𝒪_X`-module `L` and a generating family of `n + 1` global
> sections of `L`. It is the morphism to the integral model paired with `f`; no compatibility has
> to be checked, `ℙⁿ_S` being a fibre product over the terminal scheme.

```lean
def toProjectiveSpaceOver {S : Scheme.{u}} (f : X ⟶ S) : X ⟶ projectiveSpaceOver n S
```

## Tag 01NE, a lemma

[Tag 01NE](https://stacks.math.columbia.edu/tag/01NE) in the Stacks Project.

**`Stacks.ProjectiveSpaceModuli.bijective_pointsOfHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpaceModuli/Basic.lean, line 501](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpaceModuli/Basic.lean#L501). The attribute's comment: “the bijection on points”.

> Projective `n`-space over the integers represents the functor sending a scheme `X` to the
> set of pairs `(L, (s₀, …, sₙ))` with `L` an invertible `𝒪_X`-module and the `sᵢ` generating
> global sections, up to an isomorphism matching the sections: the classifying map is a
> bijection.

```lean
theorem bijective_pointsOfHom :
    Function.Bijective (pointsOfHom (X := X) (n := n))
```

**`Stacks.ProjectiveSpaceModuli.pointsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpaceModuli/Basic.lean, line 508](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpaceModuli/Basic.lean#L508). The attribute's comment: “the representing bijection”.

> The bijection between morphisms `X ⟶ ℙⁿ_ℤ` and invertible modules with `n + 1` generating
> global sections up to isomorphism.

```lean
def pointsEquiv (X : Scheme.{u}) (n : ℕ) :
    (X ⟶ projectiveSpaceAtUniverse.{u} n) ≃ Points X n
```

**`Stacks.ProjectiveSpaceModuli.pointsOfHom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpaceModuli/Basic.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpaceModuli/Basic.lean#L570). The attribute's comment: “naturality of the bijection in the test scheme”.

> The classifying map is natural in the test scheme: the pair attached to `h ≫ g` is the
> pullback along `h` of the pair attached to `g`.

```lean
theorem pointsOfHom_comp (h : Y ⟶ X) (g : X ⟶ projectiveSpaceAtUniverse.{u} n) :
    pointsOfHom (h ≫ g) = pullbackPoints h (pointsOfHom g)
```

## Tag 01NF, a definition

[Tag 01NF](https://stacks.math.columbia.edu/tag/01NF) in the Stacks Project.

**`AlgebraicGeometry.projectiveSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpace.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpace.lean#L61). The attribute's comment: “projective space over the integers”.

> Projective `n`-space over the integers.

```lean
public noncomputable def projectiveSpace (n : ℕ) : Scheme.{0}
```

**`AlgebraicGeometry.projectiveSpaceIntegralIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpace.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpace.lean#L78). The attribute's comment: “canonical comparison of integral models”.

> The canonical comparison between the literal integral model and its universe-zero copy.

```lean
public noncomputable def projectiveSpaceIntegralIso (n : ℕ) :
    projectiveSpace n ≅ projectiveSpaceAtUniverse.{0} n
```

**`AlgebraicGeometry.projectiveSpaceOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpace.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpace.lean#L138). The attribute's comment: “projective space over a scheme”.

> Projective `n`-space over `S`, by base change from the integers.

```lean
public noncomputable abbrev projectiveSpaceOver (n : ℕ) (S : Scheme.{u}) : Scheme.{u}
```

**`AlgebraicGeometry.projectiveSpaceOverRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpace.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpace.lean#L181). The attribute's comment: “projective space over a ring”.

> Projective `n`-space over a commutative ring `R`.

```lean
public noncomputable abbrev projectiveSpaceOverRing (n : ℕ) (R : CommRingCat.{u}) : Scheme.{u}
```

## Tag 01NG, a lemma

[Tag 01NG](https://stacks.math.columbia.edu/tag/01NG) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpace.basicOpenXIsoAffineSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceCharts.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceCharts.lean#L121). The attribute's comment: “affine-space charts”.

> **The standard open at a homogeneous coordinate of projective `n`-space over the integers is
> affine `n`-space over the integers.**
>
> The identification sends the affine coordinate indexed by `j ≠ i` to the ratio `T_j / T_i`.

```lean
public noncomputable def basicOpenXIsoAffineSpace (i : Fin (n + 1)) :
    (Proj.basicOpen (MvPolynomial.homogeneousSubmodule (Fin (n + 1)) ℤ)
      (MvPolynomial.X i)).toScheme ≅ AffineSpace (Fin n) (Spec (.of ℤ))
```

**`Stacks.ProjectiveChart.iSup_basicOpen_X_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveChart/Basic.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveChart/Basic.lean#L350). The attribute's comment: “standard-open covering”.

> The homogeneous coordinate standard opens cover projective space.

```lean
theorem iSup_basicOpen_X_eq_top (n : ℕ) :
    (⨆ i : Fin (n + 1),
      Proj.basicOpen (MvPolynomial.homogeneousSubmodule (Fin (n + 1)) R)
        (MvPolynomial.X i)) = ⊤
```

**`Stacks.ProjectiveChart.basicOpen_X_iso_affineSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveChart/Basic.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveChart/Basic.lean#L374). The attribute's comment: “affine-space charts”.

> The standard open at a homogeneous coordinate is affine `n`-space.

```lean
noncomputable def basicOpen_X_iso_affineSpace (A : Type) [CommRing A] (n : ℕ)
    (i : Fin (n + 1)) :
    (Proj.basicOpen (MvPolynomial.homogeneousSubmodule (Fin (n + 1)) A)
      (MvPolynomial.X i)).toScheme ≅ AffineSpace (Fin n) (Spec (.of A))
```

**`Stacks.ProjectiveSpace.iSup_basicOpen_X_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Dimension/Basic.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Dimension/Basic.lean#L95). The attribute's comment: “standard-open covering”.

> **The standard opens `D₊(Xᵢ)` cover `Proj` of the polynomial algebra graded by total
> degree.** For `R = ℤ` and `σ = Fin (n + 1)` this is the standard covering of projective
> `n`-space over the integers.

```lean
theorem iSup_basicOpen_X_eq_top (R : Type u) [CommRing R] (σ : Type v) :
    (⨆ i : σ, Proj.basicOpen (homogeneousSubmodule σ R) (X i)) = ⊤
```

## Tag 01NH, a lemma

[Tag 01NH](https://stacks.math.columbia.edu/tag/01NH) in the Stacks Project.

**`AlgebraicGeometry.projectiveSpaceOver.isProper`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceProper.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceProper.lean#L89). The attribute's comment: “universally closed”.

> Projective `n`-space over a scheme `S` is proper over `S`. In particular the structure
> morphism `ℙⁿ_S ⟶ S` is universally closed, assertion (4) of Stacks 01NH.

```lean
instance isProper (n : ℕ) (S : Scheme.{u}) : IsProper ((projectiveSpaceOver n S) ↘ S)
```

**`AlgebraicGeometry.projectiveSpaceOver.valuativeCriterion_existence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceStructureMorphism.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceStructureMorphism.lean#L61). The attribute's comment: “existence part of the valuative criterion”.

> **Stacks 01NH (3), existence.** The structure morphism of projective `n`-space over a scheme
> `S` satisfies the existence part of the valuative criterion.

```lean
theorem valuativeCriterion_existence (n : ℕ) (S : Scheme.{u}) :
    ValuativeCriterion.Existence (projectiveSpaceOver n S ↘ S)
```

**`AlgebraicGeometry.projectiveSpaceOver.valuativeCriterion_uniqueness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceStructureMorphism.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceStructureMorphism.lean#L70). The attribute's comment: “uniqueness part of the valuative criterion”.

> **Stacks 01NH (3), uniqueness.** The structure morphism of projective `n`-space over a scheme
> `S` satisfies the uniqueness part of the valuative criterion.

```lean
theorem valuativeCriterion_uniqueness (n : ℕ) (S : Scheme.{u}) :
    ValuativeCriterion.Uniqueness (projectiveSpaceOver n S ↘ S)
```

Declarations registered for the tag:

- [`Stacks.HProjective.isSeparated_over`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/HProjective/Basic.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceStructureMorphism.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceStructureMorphism.lean#L52) (StacksFrontier): “separated”.
- [`AlgebraicGeometry.projectiveSpaceOver.quasiCompact`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/SmoothProjectiveVariety.lean#L123), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceStructureMorphism.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceStructureMorphism.lean#L54) (StacksFrontier): “quasi-compact”.

## Tag 01WD, a lemma

[Tag 01WD](https://stacks.math.columbia.edu/tag/01WD) in the Stacks Project.

**`AlgebraicGeometry.Segre.isClosedImmersion_segreMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Segre/ChartSurjective.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Segre/ChartSurjective.lean#L379). The attribute's comment: “the integral models”. References: EGA II (4.3.3), “over Spec ℤ”.

> **The Segre morphism of the integral models is a closed immersion.**

```lean
theorem isClosedImmersion_segreMorphism (n m : ℕ) :
    IsClosedImmersion (segreMorphism.{u} n m)
```

**`AlgebraicGeometry.Segre.hasSegreEmbeddingSharp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Segre/ChartSurjective.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Segre/ChartSurjective.lean#L398). The attribute's comment: “over an arbitrary base”. References: EGA II (4.3.3).

> **[Stacks, Tag 01WD] over an arbitrary base.** For every scheme `S` and all `n m`, there is a
> closed immersion `ℙⁿ_S ×_S ℙᵐ_S ⟶ ℙ^{nm + n + m}_S` over `S`.

```lean
theorem hasSegreEmbeddingSharp (S : Scheme.{u}) : HasSegreEmbeddingSharp S
```

**`Stacks.AlgebraicGeometry.SegreProdIso.exists_segreEmbedding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SegreProdIso/Main.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SegreProdIso/Main.lean#L362). References: EGA II (4.3.3).

> **Stacks Tag 01WD.**  Over an arbitrary base scheme `S` the product `ℙⁿ_S ×_S ℙᵐ_S` admits a
> closed immersion into `ℙ^{nm+n+m}_S` over `S`.

```lean
public theorem exists_segreEmbedding (S : Scheme.{u}) :
    ∃ f : pullback ((projectiveSpaceOver n S) ↘ S) ((projectiveSpaceOver m S) ↘ S) ⟶
        projectiveSpaceOver (n * m + n + m) S,
      IsClosedImmersion f ∧
        f ≫ ((projectiveSpaceOver (n * m + n + m) S) ↘ S) =
          pullback.fst ((projectiveSpaceOver n S) ↘ S) ((projectiveSpaceOver m S) ↘ S) ≫
            ((projectiveSpaceOver n S) ↘ S)
```

## Tag 03GL, a lemma

[Tag 03GL](https://stacks.math.columbia.edu/tag/03GL) in the Stacks Project.

**`Stacks.ClosedSubschemeProjectiveSpace.closedSubscheme_iso_projQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedSubschemeProjectiveSpace/Basic.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ClosedSubschemeProjectiveSpace/Basic.lean#L109). The attribute's comment: “the closed subscheme is the Proj of the quotient”. References: EGA II (2.9.2), “(ii), special case”.

> **Stacks Tag 03GL, third assertion: `Z = Proj(R[T₀, …, Tₙ]/I)`.** Let `R` be an arbitrary
> commutative ring and let `i : Z ⟶ ℙⁿ_R` be a closed subscheme of projective `n`-space over `R`.
> Let `I ⊆ R[T₀, …, Tₙ]` be the homogeneous ideal generated by the homogeneous polynomials whose
> twisted global section pulls back to zero on `Z` — the ideal whose degree-`d` part is
> `Ker(R[T₀, …, Tₙ]_d ⟶ Γ(Z, 𝒪(d)|_Z))`, by the two assertions of the tag registered on
> `Stacks.AlgebraicGeometry.IdealOfClosedSubscheme.mem_idealOfClosedSubscheme_iff` and
> `Stacks.AlgebraicGeometry.IdealOfClosedSubscheme.idealOfClosedSubscheme_isHomogeneous`.
>
> Then `Z` is isomorphic to `Proj(R[T₀, …, Tₙ]/I)`, compatibly with the two morphisms into `ℙⁿ_R`:
> the closed immersion `i` itself, and the canonical morphism
> `Stacks.ClosedSubschemeProjQuotient.ambientHom` read through the comparison. So the two are equal
> as closed subschemes of projective space.
>
> No hypothesis is placed on `R`; in particular it need not be Noetherian.

```lean
theorem closedSubscheme_iso_projQuotient {Z : Scheme.{u}}
    (i : Z ⟶ AlgebraicGeometry.projectiveSpaceOverRing n (CommRingCat.of R))
    [IsClosedImmersion i] :
    ∃ e : Z ≅ projQuotient (polyGrading R n) (i ≫ (comparisonIso R n).hom),
      e.hom ≫ ambientHom (polyGrading R n) (i ≫ (comparisonIso R n).hom) ≫
        (comparisonIso R n).inv = i
```

Declarations registered for the tag:

- [`Stacks.AlgebraicGeometry.IdealOfClosedSubscheme.idealOfClosedSubscheme_isHomogeneous`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/IdealOfClosedSubscheme/Basic.lean#L306), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/IdealRegistration/Tags.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/IdealRegistration/Tags.lean#L94) (StacksFrontier): “the ideal is graded”.
- [`Stacks.AlgebraicGeometry.IdealOfClosedSubscheme.mem_idealOfClosedSubscheme_iff`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/IdealOfClosedSubscheme/Basic.lean#L278), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/IdealRegistration/Tags.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/IdealRegistration/Tags.lean#L97) (StacksFrontier): “the degreewise kernels”.

## Tag 03GM, a lemma

[Tag 03GM](https://stacks.math.columbia.edu/tag/03GM) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjTwistComparisonIso.gradedModule_and_isIso_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorSectionNonvanishing/ProjTwistComparisonIsoStatement.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorSectionNonvanishing/ProjTwistComparisonIsoStatement.lean#L125). The attribute's comment: “both assertions of the tag in one statement, for a quasi-coherent `ℱ` on `ℙᵐ_R`: the twisted global sections `M = ⨁_{d ≥ 0} Γ(ℙᵐ_R, ℱ(d))` form a graded `R[T₀, …, Tₘ]`-module -- internally graded, with the grading of the ring acting on the grading of `M`, the action being the multiplication map of the twists of Equation 03GK -- and the canonical comparison `M̃ ⟶ ℱ`, the unique morphism restricting on each positive-degree standard open `D₊(f)` to `x / f ^ n ↦ x|_{D₊(f)} ⊗ f ^ (-n)`, is an isomorphism”.

> **[Stacks, Tag 03GM].** Let `R` be a ring and let `ℱ` be a quasi-coherent sheaf on
> `ℙᵐ_R`. For `d ≥ 0` put `M_d = Γ(ℙᵐ_R, ℱ(d))`. Then `M = ⨁_{d ≥ 0} M_d` is a graded
> `R[T₀, …, Tₘ]`-module and there is a canonical isomorphism `ℱ = M̃`.
>
> The first conjunct is the graded-module assertion, in three parts: the integer grading
> decomposes `M` internally, the grading of `R[T₀, …, Tₘ]` acts on that grading, and the action of
> a homogeneous element is the multiplication map of the twists of Equation 03GK. The second and
> third are the canonical isomorphism: the comparison `M̃ ⟶ ℱ` is the unique morphism restricting
> on each positive-degree standard open `D₊(f)` to `x / f ^ n ↦ x|_{D₊(f)} ⊗ f ^ (-n)`, and it is
> invertible.
>
> The source's omitted injectivity and surjectivity arguments are
> `Stacks.AlgebraicGeometry.ProjTwistChartBijective.exists_pow_smul_eq_zero_of_numerSection_eq_zero`
> and `Stacks.AlgebraicGeometry.ProjTwistChartBijective.exists_numerSection_eq`.

```lean
theorem gradedModule_and_isIso_comparison
    (F : SheafOfModules.{u} (projRingSheaf (projectiveGrading m R)))
    (hqc : SheafOfModules.IsQuasicoherent
      (R := (AlgebraicGeometry.Proj (projectiveGrading m R)).ringCatSheaf) F) :
    (DirectSum.IsInternal (moduleGrading (projectiveGrading m R) F) ∧
        SetLike.GradedSMul (projectiveGrading m R)
          (moduleGrading (projectiveGrading m R) F) ∧
        ∀ (e k : ℕ) (a : projectiveGrading m R e)
          (s : twistSections (projectiveGrading m R) F k),
          (a : MvPolynomial (Fin (m + 1)) R) •
              DirectSum.of (twistSections (projectiveGrading m R) F) k s =
            DirectSum.of (twistSections (projectiveGrading m R) F) (e + k)
              (gsmul (projectiveGrading m R) F a.2 k (e + k) rfl s)) ∧
      (∃! φ : associatedTwistSectionSheaf (projectiveGrading m R) F ⟶ F,
          ∀ p : PositiveElem (projectiveGrading m R),
            φ.val.app (op (positiveBasicOpen (projectiveGrading m R) p)) =
              positiveChartHom (projectiveGrading m R) F p) ∧
      IsIso (comparison (projectiveGrading m R) F)
```

## Tag 0B3B, a lemma

[Tag 0B3B](https://stacks.math.columbia.edu/tag/0B3B) in the Stacks Project.

**`Stacks.SheafOfModules.kernelTensorGeneratingSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Generators/KernelTensorInvertible.lean, line 668](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Generators/KernelTensorInvertible.lean#L668).

> **Stacks 0B3B.** Let `L` be an invertible sheaf of modules on a locally ringed space, let
> `s : I → Γ(X, L)` be global sections generating `L`, and let `F` be the kernel of the induced map
> `O_X^{⊕I} ⟶ L`. Then `F ⊗ L` is generated by global sections, by the Koszul sections
> `e_i ⊗ s_j − e_j ⊗ s_i`.

```lean
noncomputable def kernelTensorGeneratingSections (g : L.GeneratingSections) :
    ((((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
        (⟨X.presheaf, X.IsSheaf⟩ : Sheaf (JX X) CommRingCat.{u})).obj ((kernel g.π))).obj
        (L))).GeneratingSections
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.13, Tag 01ND](https://stacks.math.columbia.edu/tag/01ND)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
