---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProjectiveSpectrum.Proj.projectivePlane_idealOfClosedSubscheme_isPrincipal, AlgebraicGeometry.ProjectiveSpectrum.Proj.projectivePlane_isCohenMacaulay_iff_hasNoEmbeddedPoints, AlgebraicGeometry.ProjectiveSpectrum.Proj.projectivePlane_isCurve_iff_irreducible, AlgebraicGeometry.ProjectiveSpectrum.Proj.planeCurveGlobalSectionsEquiv, AlgebraicGeometry.ProjectiveSpectrum.Proj.genus_planeCurve, AlgebraicGeometry.ProjectiveSpectrum.Proj.genus_planeCurve_totalDegree, Stacks.Curves.exists_isClosed_smoothAt_isSeparable_finrank_le_totalDegree
statement: formalized
proof: formalized
---

# 53.9 Plane curves

Section 53.9 of the Stacks Project, [Tag 0BYA](https://stacks.math.columbia.edu/tag/0BYA). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BYB, a lemma

[Tag 0BYB](https://stacks.math.columbia.edu/tag/0BYB) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.projectivePlane_idealOfClosedSubscheme_isPrincipal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveIdeal.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveIdeal.lean#L149).

> **Stacks Project, Tag 0BYB.** Let `k` be a field and let `Z` be a closed subscheme of
> `P^2_k = Proj k[T₀, T₁, T₂]` which is equidimensional of dimension one and has no embedded
> points. Then the homogeneous ideal `I(Z) ⊆ k[T₀, T₁, T₂]` corresponding to `Z` is principal.
>
> Equidimensionality of dimension one is the hypothesis that every irreducible component of `Z`
> has `topologicalKrullDim` equal to `1`; see
> `TopologicalSpace.Equidimensional.of_forall_topologicalKrullDim_eq`. This is Tag 0BXU, the
> statement for `P^n_k` with components of dimension `n - 1`, at `n = 2`. For the equivalent
> Cohen--Macaulay form of the hypothesis see
> `projectivePlane_isCohenMacaulay_iff_hasNoEmbeddedPoints`, and for the generator written out see
> `projectivePlane_exists_homogeneous_eq_idealOfClosedSubscheme`.

```lean
theorem projectivePlane_idealOfClosedSubscheme_isPrincipal (hno : HasNoEmbeddedPoints Z)
    (hdim : ∀ W ∈ irreducibleComponents Z, topologicalKrullDim W = 1) :
    (idealOfClosedSubscheme
      (MvPolynomial.homogeneousSubmodule (Fin 3) k) i).IsPrincipal
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.projectivePlane_isCohenMacaulay_iff_hasNoEmbeddedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveIdeal.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveIdeal.lean#L166).

> **Stacks Project, Tag 0BYB, the parenthetical statement.** A closed subscheme `Z` of
> `P^2_k` which is equidimensional of dimension one has no embedded points precisely when it is
> Cohen--Macaulay.
>
> This is Tag 0BXG for schemes of dimension at most one. Both of its hypotheses are automatic
> here: `Z` is locally Noetherian because `i` is a closed immersion, hence locally of finite type,
> into the Noetherian scheme `P^2_k`; and `dim Z ≤ 1` because every irreducible component of `Z`
> has dimension one.

```lean
theorem projectivePlane_isCohenMacaulay_iff_hasNoEmbeddedPoints
    (hdim : ∀ W ∈ irreducibleComponents Z, topologicalKrullDim W = 1) :
    IsCohenMacaulay Z ↔ HasNoEmbeddedPoints Z
```

## Tag 0BYC, a lemma

[Tag 0BYC](https://stacks.math.columbia.edu/tag/0BYC) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.projectivePlane_isCurve_iff_irreducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveIrreducibleEquation.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveIrreducibleEquation.lean#L404).

> **Stacks Project, Tag 0BYC.** Let `k` be a field, let `Z ⊆ 𝐏²_k = Proj k[T₀, T₁, T₂]` be a
> closed subscheme of dimension one and let `I(Z) = (F)`. Then `Z` is a curve over `k` if and only
> if `F` is irreducible.
>
> The hypotheses of [Stacks, Tag 0BYB] under which the generator `F` is produced — `Z`
> equidimensional of dimension one with no embedded points — are not needed beyond `dim Z = 1`,
> which they give for a nonempty `Z`; see
> `AlgebraicGeometry.ProjectiveSpectrum.Proj.projectivePlane_idealOfClosedSubscheme_isPrincipal`
> for that production. "Curve" is [Stacks, Tag 0A23]: a variety over `k` of Krull dimension one,
> with respect to the structure morphism of the polynomial model of the projective plane.

```lean
theorem projectivePlane_isCurve_iff_irreducible (hdim : topologicalKrullDim Z = 1)
    {F : MvPolynomial (Fin 3) k}
    (hF : idealOfClosedSubscheme (MvPolynomial.homogeneousSubmodule (Fin 3) k) i =
      Ideal.span {F}) :
    IsCurve k (i ≫ projToSpecCoeff k 2) ↔ Irreducible F
```

## Tag 0BYD, a lemma

[Tag 0BYD](https://stacks.math.columbia.edu/tag/0BYD) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.planeCurveGlobalSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveGenus.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveGenus.lean#L396). The attribute's comment: “global functions”. References: SGA 7 XXII (6.2), “(6.2.5), special case”.

> **Stacks Project, Tag 0BYD, global functions.** Let `Z ⊆ 𝐏²_k` be as in
> [Stacks, Tag 0BYB], with `I(Z) = (F)` for `F` homogeneous of degree `d`. Then
> `H⁰(Z, 𝒪_Z) = k`.
>
> The source sheafifies the graded resolution of `k[T₀, T₁, T₂]/(F)` into
> `0 → 𝒪(-d) → 𝒪 → i_* 𝒪_Z → 0` and reads the degree-zero window of the resulting long exact
> sequence. Since `d > 0` by `PlaneCurveData.deg_pos`, the two terms `H⁰(𝐏²_k, 𝒪(-d))` and
> `H¹(𝐏²_k, 𝒪(-d))` flanking that window vanish by [Stacks, Tag 01XT], so the restriction map
> `H⁰(𝐏²_k, 𝒪) → H⁰(Z, 𝒪_Z)` is an isomorphism; that is
> `Stacks.ProjectiveSpace.Cohomology.nonempty_structureSheafCohomologyIsoTwistCohomologyZero`. Its
> source is `k` because the degree-zero homogeneous polynomials are the constants.

```lean
def planeCurveGlobalSectionsEquiv {k : Type u} [Field k] (C : PlaneCurveData k) :
    structureSheafCohomology C.toSpec 0 ≃ₗ[k] k
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.genus_planeCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveGenus.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveGenus.lean#L421). The attribute's comment: “the genus formula”.

> **Stacks Project, Tag 0BYD, the genus formula.** Let `Z ⊆ 𝐏²_k` be as in
> [Stacks, Tag 0BYB], with `I(Z) = (F)` for `F` homogeneous of degree `d`. Then the genus of `Z`
> is `(d - 1)(d - 2)/2`.
>
> The source reads the isomorphism `H¹(Z, 𝒪_Z) ≅ H²(𝐏²_k, 𝒪(-d))` off the long exact sequence of
> the sheafified resolution `0 → 𝒪(-d) → 𝒪 → i_* 𝒪_Z → 0`, where it is an isomorphism because
> `H¹(𝐏²_k, 𝒪)` and `H²(𝐏²_k, 𝒪)` both vanish. That is
> `Stacks.ProjectiveSpace.Cohomology`
> `.finrank_structureSheafCohomology_eq_finrank_twistCohomology_neg`, whose input is the
> identification of the ideal sheaf of `Z` with the zero scheme of the section of `𝒪(d)` attached
> to `F`; `F` is nonzero because `Z` is equidimensional of dimension one. What remains is the
> dimension of the right-hand side, which by [Stacks, Tag 01XT] is free on the degree-`-d` Laurent
> monomials with every exponent negative, and those number `(d - 1)(d - 2)/2`.

```lean
theorem genus_planeCurve {k : Type u} [Field k] (C : PlaneCurveData k) :
    genus C.toSpec = (C.deg - 1) * (C.deg - 2) / 2
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.genus_planeCurve_totalDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveGenus.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveGenus.lean#L436). The attribute's comment: “the genus formula, stated at the total degree of the equation”.

> **The genus formula at the degree of the equation.** The genus of a plane curve `Z ⊆ 𝐏²_k`
> cut out by `F` is `(deg(F) - 1)(deg(F) - 2)/2`, where `deg(F)` is `MvPolynomial.totalDegree F`.

```lean
theorem genus_planeCurve_totalDegree {k : Type u} [Field k] (C : PlaneCurveData k) :
    genus C.toSpec = (C.F.totalDegree - 1) * (C.F.totalDegree - 2) / 2
```

## Tag 0CCU, a lemma

[Tag 0CCU](https://stacks.math.columbia.edu/tag/0CCU) in the Stacks Project.

**`Stacks.Curves.exists_isClosed_smoothAt_isSeparable_finrank_le_totalDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveProjectiveSmoothPoint.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveProjectiveSmoothPoint.lean#L99).

> **[Stacks, Tag 0CCU].**  Let `k` be an infinite field and `Z ⊆ 𝐏²_k` a closed subscheme whose
> homogeneous ideal is generated by a nonzero homogeneous `F` of degree `d`.  If the structure
> morphism `Z ⟶ Spec k` is smooth at one point, then there is a **closed** point `z` of `Z` at
> which it is smooth and whose residue field is a finite **separable** extension of `k` of degree
> at most `d`.

```lean
theorem exists_isClosed_smoothAt_isSeparable_finrank_le_totalDegree [Infinite k]
    (i : Z ⟶ Proj (MvPolynomial.homogeneousSubmodule (Fin 3) k)) [IsClosedImmersion i]
    {d : ℕ} (F : MvPolynomial (Fin 3) k) (hF0 : F ≠ 0)
    (hF : F ∈ MvPolynomial.homogeneousSubmodule (Fin 3) k (d • 1))
    (hideal : AlgebraicGeometry.ProjectiveSpectrum.Proj.idealOfClosedSubscheme
      (MvPolynomial.homogeneousSubmodule (Fin 3) k) i = Ideal.span {F})
    (hsmooth : ∃ z' : Z, InfinitesimalLifting.SmoothAt
      (i ≫ Stacks.AlgebraicGeometry.ProjPolyChart.projToSpecCoeff k 2) z') :
    ∃ z : Z, IsClosed ({z} : Set Z) ∧
      InfinitesimalLifting.SmoothAt
        (i ≫ Stacks.AlgebraicGeometry.ProjPolyChart.projToSpecCoeff k 2) z ∧
      (letI : Algebra k (Z.residueField z) :=
          ((Scheme.ΓSpecIso (CommRingCat.of k)).inv ≫
            (i ≫ Stacks.AlgebraicGeometry.ProjPolyChart.projToSpecCoeff k 2).appTop ≫
            Z.Γevaluation z).hom.toAlgebra;
        Module.Finite k (Z.residueField z) ∧
          Algebra.IsSeparable k (Z.residueField z) ∧
          Module.finrank k (Z.residueField z) ≤ F.totalDegree)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.9, Tag 0BYA](https://stacks.math.columbia.edu/tag/0BYA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
