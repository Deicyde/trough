---
declaration: section
origin: cited
lean: AlgebraicGeometry.isTrivial_of_genus_eq_zero_of_invertibleCurveDegree_eq_zero, AlgebraicGeometry.isZero_cohomologyOverField_one_of_genus_zero_of_degree_pos, AlgebraicGeometry.finrank_cohomologyOverField_zero_eq_degree_add_one_of_genus_zero, AlgebraicGeometry.isRelativelyVeryAmple_and_isClosedImmersion_of_basis, AlgebraicGeometry.exists_planeCurveData_deg_two_of_isGorenstein, AlgebraicGeometry.projectiveLine_tfae, AlgebraicGeometry.ProjectiveLineCriterion.projectiveLine_tfae, AlgebraicGeometry.ProjectiveLineCriterion.exists_iso_projectiveLine_of_invertibleCurveDegree_eq_one
statement: formalized
proof: formalized
---

# 53.10 Curves of genus zero

Section 53.10 of the Stacks Project, [Tag 0C6L](https://stacks.math.columbia.edu/tag/0C6L). 6 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C6M, a lemma

[Tag 0C6M](https://stacks.math.columbia.edu/tag/0C6M) in the Stacks Project.

**`AlgebraicGeometry.isTrivial_of_genus_eq_zero_of_invertibleCurveDegree_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusZeroDegreeZero.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusZeroDegreeZero.lean#L46).

> Let `X` be a proper curve over a field `k` with `H⁰(X, 𝒪_X) = k`. If `X` has genus `0`, then
> every invertible `𝒪_X`-module `ℒ` of degree `0` is trivial.

```lean
public theorem isTrivial_of_genus_eq_zero_of_invertibleCurveDegree_eq_zero [IsCurve k f]
    [IsProper f] [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)] (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.property L]
    (hgenus : genus f = 0)
    (hdeg : invertibleCurveDegree k f
      (IsCurve.topologicalKrullDim_eq_one (k := k) (f := f)).le L = 0) :
    SheafOfModules.IsTrivial X.presheaf X.ringCatSheaf.property L
```

## Tag 0C6T, a lemma

[Tag 0C6T](https://stacks.math.columbia.edu/tag/0C6T) in the Stacks Project.

**`AlgebraicGeometry.isZero_cohomologyOverField_one_of_genus_zero_of_degree_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/Basic.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/Basic.lean#L211). The attribute's comment: “part (1), the clause `dim_k H¹(X, ℒ) = 0`”.

> **[Stacks, Tag 0C6T]: the vanishing `H¹(X, ℒ) = 0` of assertion (1).** Let `X` be a proper
> curve over a field `k` with `H⁰(X, 𝒪_X) = k` and genus zero, and let `ℒ` be an invertible
> `𝒪_X`-module of positive degree. Then `H¹(X, ℒ) = 0`.

```lean
public theorem isZero_cohomologyOverField_one_of_genus_zero_of_degree_pos [IsProper f]
    [IsIntegral X] [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)]
    (hdim : topologicalKrullDim X ≤ 1)
    (L : X.Modules) [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (hgenus : genus f = 0) (hpos : 0 < invertibleCurveDegree k f hdim L) :
    IsZero (cohomologyOverField k f L 1)
```

**`AlgebraicGeometry.finrank_cohomologyOverField_zero_eq_degree_add_one_of_genus_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/Basic.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/Basic.lean#L247). The attribute's comment: “part (1), the clause `dim_k H⁰(X, ℒ) = d + 1`”.

> **[Stacks, Tag 0C6T]: the dimension count `dim_k H⁰(X, ℒ) = d + 1` of assertion (1).** On a
> proper curve over a field with `H⁰(X, 𝒪_X) = k` and genus zero, an invertible module `ℒ` whose
> degree `d` is positive has `dim_k H⁰(X, ℒ) = d + 1`.

```lean
public theorem finrank_cohomologyOverField_zero_eq_degree_add_one_of_genus_zero
    [IsProper f] [IsIntegral X] [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)]
    (hdim : topologicalKrullDim X ≤ 1) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (hgenus : genus f = 0) (hpos : 0 < invertibleCurveDegree k f hdim L) :
    (Module.finrank k (cohomologyOverField k f L 0) : ℤ) =
      invertibleCurveDegree k f hdim L + 1
```

**`AlgebraicGeometry.isRelativelyVeryAmple_and_isClosedImmersion_of_basis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/ProjectiveEmbedding.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/ProjectiveEmbedding.lean#L170). The attribute's comment: “part (2)”.

> **[Stacks, Tag 0C6T] part (2).** Let `X` be a proper integral scheme of dimension at most one
> over a field `k` with `H⁰(X, 𝒪_X) = k` and genus `0`, and let `ℒ` be an invertible `𝒪_X`-module of
> degree `d > 0`. Then `ℒ` is very ample over `k`, and for every basis `s₀, …, s_d` of `H⁰(X, ℒ)` the
> sections generate `ℒ` and the morphism `φ_{(ℒ, (s₀, …, s_d))} : X ⟶ 𝐏^d_k` they define is a closed
> immersion.

```lean
theorem isRelativelyVeryAmple_and_isClosedImmersion_of_basis [IsProper f] [IsIntegral X]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)] (hdim : topologicalKrullDim X ≤ 1)
    (hgenus : genus f = 0) (L : X.Modules) [Stacks.Ample.IsInvertibleModule X L] {d : ℕ}
    (hdeg : invertibleCurveDegree k f hdim L = d) (hd : 0 < d)
    (b : Module.Basis (Fin (d + 1)) k ((restrictScalarsOverBase k f).obj
      ((SheafOfModules.evaluation X.ringCatSheaf (op (⊤ : X.Opens))).obj L))) :
    Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple f L ∧
      ∃ hs : GeneratesStalks (fun j => (show Γ(L, ⊤) from b j)),
        IsClosedImmersion (Stacks.ProjectiveSpaceChartRatio.toPolynomialModel
          (fun j => (show Γ(L, ⊤) from b j)) hs f)
```

## Tag 0C6N, a lemma

[Tag 0C6N](https://stacks.math.columbia.edu/tag/0C6N) in the Stacks Project.

**`AlgebraicGeometry.exists_planeCurveData_deg_two_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/GorensteinConic.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/GorensteinConic.lean#L44).

> Let `X` be a proper curve over a field `k` with `H⁰(X, 𝒪_X) = k`. If `X` is Gorenstein and
> has genus `0`, then `X` is isomorphic over `k` to a plane curve of degree `2`.

```lean
theorem exists_planeCurveData_deg_two_of_isGorenstein [IsCurve k f] [IsProper f]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)] [IsGorenstein X]
    (hgenus : genus f = 0) :
    ∃ C : ProjectiveSpectrum.Proj.PlaneCurveData k, C.deg = 2 ∧
      ∃ e : X ≅ C.Z, e.hom ≫ C.toSpec = f
```

## Tag 0C6U, a proposition

[Tag 0C6U](https://stacks.math.columbia.edu/tag/0C6U) in the Stacks Project.

**`AlgebraicGeometry.projectiveLine_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/ProjectiveLineEquivalences.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/ProjectiveLineEquivalences.lean#L53). The attribute's comment: “the final item (9) of the source is the placeholder `add more here`”.

> **Stacks Project, Tag 0C6U.** Let `X` be a proper curve over a field `k`. The following are
> equivalent:
>
> 1. `X ≅ 𝐏¹_k` over `k`;
> 2. `X` is smooth and geometrically irreducible over `k`, of genus `0`, with an invertible module of
>    odd degree;
> 3. `X` is geometrically integral over `k`, of genus `0`, Gorenstein, with an invertible module of
>    odd degree;
> 4. `H⁰(X, 𝒪_X) = k`, `X` has genus `0`, is Gorenstein, and has an invertible module of odd
>    degree;
> 5. `X` is geometrically integral over `k`, of genus `0`, with an invertible module of degree `1`;
> 6. `H⁰(X, 𝒪_X) = k`, `X` has genus `0`, and has an invertible module of degree `1`;
> 7. `H¹(X, 𝒪_X) = 0` and `X` has an invertible module of degree `1`;
> 8. `H¹(X, 𝒪_X) = 0` and `X` has closed points `x₁, …, xₙ` with normal local rings and
>    `gcd [κ(xᵢ) : k] = 1`.
>
> For `(4) ⇒ (6)`: `ω_X` is invertible of degree `2g - 2 = -2` ([Stacks, Tag 0C19]), and the degrees
> of invertible modules form a subgroup of `ℤ`.

```lean
theorem projectiveLine_tfae [IsCurve k f] [IsProper f] :
    List.TFAE [
      ∃ e : X ≅ AlgebraicGeometry.Proj (Stacks.AlgebraicGeometry.ProjPolyChart.polyGrading k 1),
        e.hom ≫ Stacks.AlgebraicGeometry.ProjPolyChart.projToSpecCoeff k 1 = f,
      Smooth f ∧ GeometricallyIrreducible f ∧ genus f = 0 ∧
        ∃ (L : X.Modules) (_ : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L),
          Odd (invertibleCurveDegree k f (IsCurve.topologicalKrullDim_eq_one (f := f)).le L),
      GeometricallyIntegral f ∧ genus f = 0 ∧ IsGorenstein X ∧
        ∃ (L : X.Modules) (_ : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L),
          Odd (invertibleCurveDegree k f (IsCurve.topologicalKrullDim_eq_one (f := f)).le L),
      IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop) ∧ genus f = 0 ∧ IsGorenstein X ∧
        ∃ (L : X.Modules) (_ : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L),
          Odd (invertibleCurveDegree k f (IsCurve.topologicalKrullDim_eq_one (f := f)).le L),
      GeometricallyIntegral f ∧ genus f = 0 ∧
        ∃ (L : X.Modules) (_ : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L),
          invertibleCurveDegree k f (IsCurve.topologicalKrullDim_eq_one (f := f)).le L = 1,
      IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop) ∧ genus f = 0 ∧
        ∃ (L : X.Modules) (_ : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L),
          invertibleCurveDegree k f (IsCurve.topologicalKrullDim_eq_one (f := f)).le L = 1,
      IsZero (cohomologyOverField k f (SheafOfModules.unit X.ringCatSheaf) 1) ∧
        ∃ (L : X.Modules) (_ : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L),
          invertibleCurveDegree k f (IsCurve.topologicalKrullDim_eq_one (f := f)).le L = 1,
      IsZero (cohomologyOverField k f (SheafOfModules.unit X.ringCatSheaf) 1) ∧
        ∃ (n : ℕ) (x : Fin n → X), (∀ i, IsClosed ({x i} : Set X)) ∧
          (∀ i, IsIntegrallyClosed (X.presheaf.stalk (x i))) ∧
          Finset.univ.gcd (fun i => letI : Algebra k (X.residueField (x i)) :=
              ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation (x i)).hom.toAlgebra
            Module.finrank k (X.residueField (x i))) = 1]
```

**`AlgebraicGeometry.ProjectiveLineCriterion.projectiveLine_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLineCriterion/Characterization.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLineCriterion/Characterization.lean#L177).

> **Stacks Project, Tag 0C6U (characterization of the projective line).** For a proper curve
> `X` over a field `k` the following are equivalent:
> 1. `X ≅ 𝐏¹_k` over `k`;
> 2. `X` is smooth and geometrically irreducible over `k`, has genus `0`, and has an invertible
>    module of odd degree;
> 3. `X` is geometrically integral over `k`, has genus `0`, is Gorenstein, and has an invertible
>    module of odd degree;
> 4. `H⁰(X, 𝒪_X) = k`, `X` has genus `0`, is Gorenstein, and has an invertible module of odd degree;
> 5. `X` is geometrically integral over `k`, has genus `0`, and has an invertible module of degree
>    `1`;
> 6. `H⁰(X, 𝒪_X) = k`, `X` has genus `0`, and has an invertible module of degree `1`;
> 7. `H¹(X, 𝒪_X) = 0` and `X` has an invertible module of degree `1`;
> 8. `H¹(X, 𝒪_X) = 0` and `X` has closed points `x₁, …, xₙ` with normal local rings `𝒪_{X,xᵢ}`
>    and `gcd [κ(xᵢ) : k] = 1`.

```lean
theorem projectiveLine_tfae [IsProper f] [IsCurve k f] :
    List.TFAE
      [Nonempty (Over.mk f ≅
          Over.mk (projectiveSpaceOver 1 (Spec (.of k)) ↘ Spec (.of k))),
        Smooth f ∧ GeometricallyIrreducible f ∧ genus f = 0 ∧
          ∃ (L : X.Modules) (_ : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L),
            Odd (invertibleCurveDegree k f
              (le_of_eq (IsCurve.topologicalKrullDim_eq_one (f := f))) L),
        GeometricallyIntegral f ∧ genus f = 0 ∧ IsGorenstein X ∧
          ∃ (L : X.Modules) (_ : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L),
            Odd (invertibleCurveDegree k f
              (le_of_eq (IsCurve.topologicalKrullDim_eq_one (f := f))) L),
        IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop) ∧ genus f = 0 ∧ IsGorenstein X ∧
          ∃ (L : X.Modules) (_ : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L),
            Odd (invertibleCurveDegree k f
              (le_of_eq (IsCurve.topologicalKrullDim_eq_one (f := f))) L),
        GeometricallyIntegral f ∧ genus f = 0 ∧
          ∃ (L : X.Modules) (_ : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L),
            invertibleCurveDegree k f (le_of_eq (IsCurve.topologicalKrullDim_eq_one (f := f)))
              L = 1,
        IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop) ∧ genus f = 0 ∧
          ∃ (L : X.Modules) (_ : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L),
            invertibleCurveDegree k f (le_of_eq (IsCurve.topologicalKrullDim_eq_one (f := f)))
              L = 1,
        IsZero (cohomologyOverField k f (SheafOfModules.unit X.ringCatSheaf) 1) ∧
          ∃ (L : X.Modules) (_ : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L),
            invertibleCurveDegree k f (le_of_eq (IsCurve.topologicalKrullDim_eq_one (f := f)))
              L = 1,
        IsZero (cohomologyOverField k f (SheafOfModules.unit X.ringCatSheaf) 1) ∧
          ∃ (n : ℕ) (x : Fin n → X), (∀ i, IsClosed ({x i} : Set X)) ∧
            (∀ i, IsNormalRing (X.presheaf.stalk (x i))) ∧
            Finset.univ.gcd (fun i => letI : Algebra k (X.residueField (x i)) :=
                ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation (x i)).hom.toAlgebra
              Module.finrank k (X.residueField (x i))) = 1]
```

**`AlgebraicGeometry.ProjectiveLineCriterion.exists_iso_projectiveLine_of_invertibleCurveDegree_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLineCriterion/ProjectiveLine.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLineCriterion/ProjectiveLine.lean#L252). The attribute's comment: “condition (6) implies condition (1)”.

> **A genus-zero curve with an invertible module of degree one is isomorphic to `ℙ¹_k` over
> `k`.** Let `X` be a proper integral scheme of dimension at most one over a field `k` with
> `H⁰(X, 𝒪_X) = k` and genus `0`, and let `ℒ` be an invertible `𝒪_X`-module of degree `1`. Then
> `X ≅ ℙ¹_k` as schemes over `k`. The isomorphism is the morphism of a basis of `H⁰(X, ℒ)`
> (`exists_iso_proj_of_invertibleCurveDegree_eq_one`), read in the base-change model
> `ℙ¹_k = Spec k ×_{Spec ℤ} ℙ¹_ℤ` through
> `Stacks.AlgebraicGeometry.ProjBaseChange.polynomialComparison`.

```lean
theorem exists_iso_projectiveLine_of_invertibleCurveDegree_eq_one [IsProper f] [IsIntegral X]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)] (hdim : topologicalKrullDim X ≤ 1)
    (hgenus : genus f = 0) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (hdeg : invertibleCurveDegree k f hdim L = 1) :
    Nonempty (Over.mk f ≅ Over.mk (projectiveSpaceOver 1 (Spec (.of k)) ↘ Spec (.of k)))
```

## Tag 0DJB, a lemma

[Tag 0DJB](https://stacks.math.columbia.edu/tag/0DJB) in the Stacks Project.

**`AlgebraicGeometry.exists_projectiveLine_normalization_of_genus_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/SingularGenusZero.lean, line 793](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/SingularGenusZero.lean#L793).

> **[Stacks, Tag 0DJB].** Let `X` be a proper curve over a field `k` with `H⁰(X, 𝒪_X) = k`,
> singular and of genus zero, and let `ν : X' ⟶ X` be its normalization. Then there are a field
> `k'`, a structure morphism `X' ⟶ Spec k'` and points `x' : Spec k' ⟶ X'`, `x : Spec k ⟶ X`
> making the diagram `x' ⟶ X' ⟶ Spec k'` over `x ⟶ X ⟶ Spec k` commute, such that
>
> 1. `k'/k` is a nontrivial finite extension;
> 2. `X' ≅ 𝐏¹_{k'}` over `k'`;
> 3. `x'` is a `k'`-rational point of `X'`;
> 4. `x` is a `k`-rational point of `X`;
> 5. `ν` restricts to an isomorphism `X' ∖ {x'} ≅ X ∖ {x}`;
> 6. `0 ⟶ 𝒪_X ⟶ ν_* 𝒪_{X'} ⟶ 𝒬 ⟶ 0` is short exact and its cokernel `𝒬` is the skyscraper at
>    `x = ν(x')` with value `κ(x') / κ(x)`, the quotient of `κ(x')` by the image of `𝒪_{X, x}`;
>    the point is written `ν(x')`, which is `x` by the commutativity of the left square.
>
> The field is `k' = H⁰(X', 𝒪_{X'})`. The dimension count at the singular points that the source
> runs through the conductor and a bound on commutative subalgebras of a matrix algebra is
> replaced by `Stacks.Curves.finrank_le_two_mul_finrank_quotient_range` and
> `Stacks.Curves.finrank_residueField_eq_one_of_finrank_quotient_range_add_one_eq`, which use
> only that `B / A` is a module over the local ring `A = 𝒪_{X, x}` and that `B / 𝔪_A B` is a
> `k'`-vector space, `B = (ν_* 𝒪_{X'})_x`; see
> `StacksFrontier.AlgebraicGeometry.Curves.SingularGenusZeroAlgebra`.
> The isomorphism `X' ≅ 𝐏¹_{k'}` comes from the degree-one invertible module of the rational point
> `x'` by `AlgebraicGeometry.exists_iso_projectiveLine_of_invertibleCurveDegree_eq_one`.

```lean
theorem exists_projectiveLine_normalization_of_genus_eq_zero (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsCurve k f] [IsProper f]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)]
    (hsing : (singularLocus X).Nonempty) (hgenus : genus f = 0) :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k k')
      (f' : normalizationSchemeOverField k f ⟶ Spec (.of k'))
      (x' : Spec (.of k') ⟶ normalizationSchemeOverField k f) (x : Spec (.of k) ⟶ X),
      -- the diagram commutes
      normalizationOverField k f ≫ f = f' ≫ Spec.map (CommRingCat.ofHom (algebraMap k k')) ∧
      x' ≫ normalizationOverField k f = Spec.map (CommRingCat.ofHom (algebraMap k k')) ≫ x ∧
      -- (1)
      (Module.Finite k k' ∧ 1 < Module.finrank k k') ∧
      -- (2)
      (∃ e : normalizationSchemeOverField k f ≅
          Proj (Stacks.AlgebraicGeometry.ProjPolyChart.polyGrading k' 1),
        e.hom ≫ Stacks.AlgebraicGeometry.ProjPolyChart.projToSpecCoeff k' 1 = f') ∧
      -- (3)
      x' ≫ f' = 𝟙 _ ∧
      -- (4)
      x ≫ f = 𝟙 _ ∧
      -- (5)
      (∃ U : X.Opens, (U : Set X) = {x (IsLocalRing.closedPoint k)}ᶜ ∧
        ((normalizationOverField k f) ⁻¹ᵁ U : Set (normalizationSchemeOverField k f)) =
          {x' (IsLocalRing.closedPoint k')}ᶜ ∧
        IsIso (normalizationOverField k f ∣_ U)) ∧
      -- (6)
      (letI : Algebra
          (X.presheaf.stalk (normalizationOverField k f (x' (IsLocalRing.closedPoint k'))))
          ((normalizationSchemeOverField k f).residueField (x' (IsLocalRing.closedPoint k'))) :=
        ((normalizationOverField k f).stalkMap (x' (IsLocalRing.closedPoint k')) ≫
          (normalizationSchemeOverField k f).residue
            (x' (IsLocalRing.closedPoint k'))).hom.toAlgebra
       (ShortComplex.cokernelSequence (normalizationModuleMap X
          (finite_irreducibleComponents_of_locallyOfFiniteType k f))).ShortExact ∧
        Nonempty (normalizationQuotient X
            (finite_irreducibleComponents_of_locallyOfFiniteType k f) ≅
          skyscraperModule X (normalizationOverField k f (x' (IsLocalRing.closedPoint k')))
            (ModuleCat.of _
              ((normalizationSchemeOverField k f).residueField (x' (IsLocalRing.closedPoint k')) ⧸
                LinearMap.range (Algebra.linearMap
                  (X.presheaf.stalk (normalizationOverField k f (x' (IsLocalRing.closedPoint k'))))
                  ((normalizationSchemeOverField k f).residueField
                    (x' (IsLocalRing.closedPoint k'))))))))
```

## Tag 0DJC, an example

[Tag 0DJC](https://stacks.math.columbia.edu/tag/0DJC) in the Stacks Project.

**`AlgebraicGeometry.exists_pinchedProjectiveLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PinchedProjectiveLine/Basic/NormalizationAndGenus.lean, line 573](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PinchedProjectiveLine/Basic/NormalizationAndGenus.lean#L573).

> **Stacks Project, Tag 0DJC.** For a nontrivial finite extension `K/k`, the pinched
> projective line over `k`: a scheme with the prescribed affine gluing of `Spec A` to `Spec K[Y]`
> along `Spec K[T, T⁻¹]`, with a single singular closed point at the contracted origin, with `k`
> for its global functions, which is a proper curve of genus zero over `k`, and whose canonical
> normalization is `ℙ¹_K`.

```lean
theorem exists_pinchedProjectiveLine [Module.Finite k K]
    (hK : 1 < Module.finrank k K) :
    ∃ (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
      (iA : Spec (.of (pinchedPolynomialRing k K)) ⟶ X)
      (iB : Spec (.of (Polynomial K)) ⟶ X)
      (ν : projectiveLine K ⟶ X)
      (xA : Spec (.of (pinchedPolynomialRing k K))),
      IsOpenImmersion iA ∧
      IsOpenImmersion iB ∧
      (iA ≫ f = Spec.map (CommRingCat.ofHom (pinchedPolynomialConstant k K))) ∧
      (iB ≫ f = Spec.map (CommRingCat.ofHom
        ((Polynomial.C : K →+* Polynomial K).comp (algebraMap k K)))) ∧
      (Set.range iA.base ∪ Set.range iB.base = Set.univ) ∧
      (let pA := pinchedPuncturedChart k K
       let pB := (projectiveLineInversionIso K).hom ≫
         projectiveLinePuncturedChart K
       ∃ (hglue : pA ≫ iA = pB ≫ iB),
         IsIso (pullback.lift pA pB hglue)) ∧
      (xA.asIdeal = (Ideal.span {(Polynomial.X : Polynomial K)}).comap
        (Subring.subtype (pinchedPolynomialRing k K))) ∧
      (singularLocus X = {iA.base xA}) ∧
      IsCurve k f ∧
      IsProper f ∧
      IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop) ∧
      genus f = 0 ∧
      (projectiveLineXChart K ≫ ν =
        pinchedNormalizationAffineChart k K ≫ iA) ∧
      (projectiveLineYChart K ≫ ν = iB) ∧
      (∃ hX : ∀ U : X.Opens, IsCompact (U : Set X) →
          (irreducibleComponents U).Finite,
        ∃ e : projectiveLine K ≅
          Scheme.normalizationScheme X hX,
          ν = e.hom ≫ Scheme.normalization X hX)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.10, Tag 0C6L](https://stacks.math.columbia.edu/tag/0C6L)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
