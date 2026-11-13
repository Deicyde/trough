---
declaration: section
origin: cited
lean: Stacks.Divisors.IsDivisorOfRationalDifferential, Stacks.Divisors.isDivisorOfRationalDifferential_weilDivisorOfMeromorphicSection, Stacks.Divisors.exists_isDivisorOfRationalDifferential, AlgebraicGeometry.existsUnique_isDivisorOfRationalDifferential, AlgebraicGeometry.exists_isDivisorOfRationalDifferential_of_isCurve, AlgebraicGeometry.AffinePlaneCurve.partialX_ne_zero_or_partialY_ne_zero, AlgebraicGeometry.AffinePlaneCurve.inv_partialY_smul_D_x_eq_neg_inv_partialX_smul_D_y, AlgebraicGeometry.AffinePlaneCurve.inv_partialY_smul_D_x_ne_zero
statement: formalized
proof: formalized
---

# 111.56 Schemes, Final Exam, Fall 2013

Section 111.56 of the Stacks Project, [Tag 09TV](https://stacks.math.columbia.edu/tag/09TV). 1 tag here is carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09U0, a situation

[Tag 09U0](https://stacks.math.columbia.edu/tag/09U0) in the Stacks Project.

**`Stacks.Divisors.IsDivisorOfRationalDifferential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/MeromorphicOrder/RationalDifferential.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/MeromorphicOrder/RationalDifferential.lean#L79). The attribute's comment: “the divisor of zeros and poles of ω”.

> **Stacks 09U0.** A Weil divisor `D` on `X` is the **divisor of zeros and poles** of the
> rational differential `ω ∈ Ω[K⁄k]`, read through an identification `e` of `K` with the function
> field of `X`, when its coefficient at every prime divisor `Z` is the order of vanishing at `Z`
> of every `g` for which `ω = g · dt` with `t` of order one at `Z`.
>
> On a nonsingular projective curve over a field, taking `ω` to be the distinguished differential
> of an irreducible plane curve makes this the canonical divisor `K_C`.

```lean
def IsDivisorOfRationalDifferential (X : Scheme.{u}) [IsIntegral X] [IsLocallyNoetherian X]
    (e : K ≃+* X.functionField) (ω : Ω[K⁄k]) (D : WeilDivisor X) : Prop
```

**`Stacks.Divisors.isDivisorOfRationalDifferential_weilDivisorOfMeromorphicSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/MeromorphicOrder/RationalDifferential.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/MeromorphicOrder/RationalDifferential.lean#L96). The attribute's comment: “the divisor of zeros and poles of ω”.

> **Stacks 09U0.** The divisor of zeros and poles of a rational differential exists as soon as
> the differential is realized in an invertible module.
>
> Let `L` be a module on `X` that is trivialized near every point, and let `E` realize the
> rational differentials of `K` over `k` inside the generic stalk of `L`, semilinearly over the
> identification `e` of `K` with `R(X)`. If `dt` is realized by a basis of the stalk of `L` at the
> generic point of `Z` whenever `t` has order one at `Z` — which is the local structure of the
> sheaf of differentials on a nonsingular curve — then the Weil divisor of `E ω`, regarded as a
> meromorphic section of `L`, is the divisor of zeros and poles of `ω`.

```lean
theorem isDivisorOfRationalDifferential_weilDivisorOfMeromorphicSection
    (hL : ∀ x : X, IsTrivializedNear L x) (e : K ≃+* X.functionField)
    (E : Ω[K⁄k] →+ L.presheaf.stalk (genericPoint X))
    (hE : ∀ (g : K) (ν : Ω[K⁄k]), E (g • ν) = e g • E ν) (ω : Ω[K⁄k])
    (hbasis : ∀ (Z : PrimeDivisor X) (t : K), X.ord (e t) Z.genericPoint = 1 →
      ∃ m : L.presheaf.stalk Z.genericPoint, IsStalkBasis L Z.genericPoint m ∧
        toGenericStalk L Z.genericPoint m = E (KaehlerDifferential.D k K t)) :
    IsDivisorOfRationalDifferential X e ω (weilDivisorOfMeromorphicSection hL (E ω))
```

**`Stacks.Divisors.exists_isDivisorOfRationalDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/MeromorphicOrder/RationalDifferential.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/MeromorphicOrder/RationalDifferential.lean#L113). The attribute's comment: “the divisor of zeros and poles of ω”.

> **Stacks 09U0.** A rational differential realized in a module trivialized near every point,
> whose exact differentials at uniformizers are bases of the stalks, has a divisor of zeros and
> poles.

```lean
theorem exists_isDivisorOfRationalDifferential
    (hL : ∀ x : X, IsTrivializedNear L x) (e : K ≃+* X.functionField)
    (E : Ω[K⁄k] →+ L.presheaf.stalk (genericPoint X))
    (hE : ∀ (g : K) (ν : Ω[K⁄k]), E (g • ν) = e g • E ν) (ω : Ω[K⁄k])
    (hbasis : ∀ (Z : PrimeDivisor X) (t : K), X.ord (e t) Z.genericPoint = 1 →
      ∃ m : L.presheaf.stalk Z.genericPoint, IsStalkBasis L Z.genericPoint m ∧
        toGenericStalk L Z.genericPoint m = E (KaehlerDifferential.D k K t)) :
    ∃ D : WeilDivisor X, IsDivisorOfRationalDifferential X e ω D
```

**`AlgebraicGeometry.existsUnique_isDivisorOfRationalDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/DivisorOfRationalDifferential.lean, line 534](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/DivisorOfRationalDifferential.lean#L534). The attribute's comment: “the divisor of zeros and poles of ω exists and is unique on a normal curve”.

> **Stacks 09U0.** A nonzero rational differential `ω` on a normal curve over a perfect field
> has a unique divisor of zeros and poles: there is exactly one Weil divisor whose coefficient at
> every prime divisor `Z` is the order of vanishing at `Z` of `g`, for every presentation
> `ω = g · dt` with `t` of order one at `Z`.

```lean
theorem existsUnique_isDivisorOfRationalDifferential
    (k : Type u) [Field k] [PerfectField k] {X : Scheme.{u}} (sX : X ⟶ Spec (.of k))
    [IsCurve k sX] [IsNormal X] [IsLocallyNoetherian X]
    {K : Type u} [Field K] [Algebra k K] (e : K ≃+* X.functionField)
    (he : ∀ a : k,
      e (algebraMap k K a) = @algebraMap k X.functionField _ _ (functionFieldAlgebra k sX) a)
    (ω : Ω[K⁄k]) (hω : ω ≠ 0) :
    ∃! D : WeilDivisor X, IsDivisorOfRationalDifferential X e ω D
```

**`AlgebraicGeometry.exists_isDivisorOfRationalDifferential_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/DivisorOfRationalDifferential.lean, line 556](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/DivisorOfRationalDifferential.lean#L556). The attribute's comment: “the divisor of zeros and poles of ω exists on a normal curve”.

> **Stacks 09U0.** A nonzero rational differential on a normal curve over a perfect field has
> a divisor of zeros and poles.

```lean
theorem exists_isDivisorOfRationalDifferential_of_isCurve
    (k : Type u) [Field k] [PerfectField k] {X : Scheme.{u}} (sX : X ⟶ Spec (.of k))
    [IsCurve k sX] [IsNormal X] [IsLocallyNoetherian X]
    {K : Type u} [Field K] [Algebra k K] (e : K ≃+* X.functionField)
    (he : ∀ a : k,
      e (algebraMap k K a) = @algebraMap k X.functionField _ _ (functionFieldAlgebra k sX) a)
    (ω : Ω[K⁄k]) (hω : ω ≠ 0) :
    ∃ D : WeilDivisor X, IsDivisorOfRationalDifferential X e ω D
```

**`AlgebraicGeometry.AffinePlaneCurve.partialX_ne_zero_or_partialY_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 368](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L368). The attribute's comment: “well-definedness of ω: a partial derivative survives”.

> **Stacks 09U0.** At least one of the two partial derivatives of an irreducible plane
> equation over a perfect field is nonzero in the function field of the curve it cuts out.
> This is what makes the differential `ω = dx/f_y = -dy/f_x` well defined.

```lean
theorem partialX_ne_zero_or_partialY_ne_zero [PerfectField k] :
    C.partialX ≠ 0 ∨ C.partialY ≠ 0
```

**`AlgebraicGeometry.AffinePlaneCurve.inv_partialY_smul_D_x_eq_neg_inv_partialX_smul_D_y`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L496). The attribute's comment: “well-definedness of ω: the two formulas agree”.

> **Stacks 09U0.** Where both partial derivatives are nonzero, the two formulas
> `dx/f_y` and `-dy/f_x` for the distinguished differential agree.

```lean
theorem inv_partialY_smul_D_x_eq_neg_inv_partialX_smul_D_y
    (hx : C.partialX ≠ 0) (hy : C.partialY ≠ 0) :
    C.partialY⁻¹ • KaehlerDifferential.D k C.FunctionField C.x =
      -(C.partialX⁻¹ • KaehlerDifferential.D k C.FunctionField C.y)
```

**`AlgebraicGeometry.AffinePlaneCurve.inv_partialY_smul_D_x_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 515](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L515). The attribute's comment: “well-definedness of ω: dx/f\_y is nonzero”.

> **Stacks 09U0.** If the partial derivative with respect to `y` is nonzero, then
> `dx/f_y` is a nonzero differential.

```lean
theorem inv_partialY_smul_D_x_ne_zero (hy : C.partialY ≠ 0) :
    C.partialY⁻¹ • KaehlerDifferential.D k C.FunctionField C.x ≠ 0
```

**`AlgebraicGeometry.AffinePlaneCurve.neg_inv_partialX_smul_D_y_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 522](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L522). The attribute's comment: “well-definedness of ω: -dy/f\_x is nonzero”.

> **Stacks 09U0.** If the partial derivative with respect to `x` is nonzero, then
> `-dy/f_x` is a nonzero differential.

```lean
theorem neg_inv_partialX_smul_D_y_ne_zero (hx : C.partialX ≠ 0) :
    -(C.partialX⁻¹ • KaehlerDifferential.D k C.FunctionField C.y) ≠ 0
```

**`AlgebraicGeometry.AffinePlaneCurve.differential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 531](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L531). The attribute's comment: “the differential ω”.

> **Stacks 09U0.** The distinguished rational differential `ω = dx/f_y = -dy/f_x` of an
> irreducible affine plane curve.

```lean
def differential : Ω[C.FunctionField⁄k]
```

**`AlgebraicGeometry.AffinePlaneCurve.differential_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 552](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L552). The attribute's comment: “ω is nonzero”.

> **Stacks 09U0.** The distinguished differential of an irreducible plane curve over a
> perfect field is nonzero.

```lean
theorem differential_ne_zero [PerfectField k] : C.differential ≠ 0
```

**`AlgebraicGeometry.ProjectivePlaneCurve`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 586](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L586). The attribute's comment: “the plane-curve situation”.

> **Stacks 09U0.** The data of the plane-curve situation: an irreducible homogeneous
> `F ∈ k[T₀, T₁, T₂]` of degree `d`, not a scalar multiple of `T₀`, together with the affine plane
> curve cut out on the standard chart `T₀ = 1` by the dehomogenization `f(x, y) = F(1, x, y)`,
> whose fraction field of `k[x, y]/(f)` is `K`.
>
> This structure records the input data of the situation. The objects the source builds from it
> are constructed, and their properties proved, in
> `StacksFrontier.AlgebraicGeometry.Curves.PlaneCurveSituation`: the curve `D = V(F)`
> (`AlgebraicGeometry.ProjectivePlaneCurve.curve`), the abstract curve `C` of `K`
> (`AlgebraicGeometry.ProjectivePlaneCurve.abstractCurve`, the normalization of `D`) with
> `K ≃ₐ[k] C.functionField`, the surjection `C ⟶ D`
> (`AlgebraicGeometry.ProjectivePlaneCurve.abstractCurveMap`), bijective over the nonsingular
> locus and an isomorphism when `D` is nonsingular, the differential `ω`
> (`AlgebraicGeometry.ProjectivePlaneCurve.differential`) and `K_C = div(ω)` on `C`
> (`AlgebraicGeometry.ProjectivePlaneCurve.canonicalDivisor`); the complete statement is
> `AlgebraicGeometry.ProjectivePlaneCurve.situation`.
>
> The field `affineChart` is determined by `F` through `affineChart_equation`; its irreducibility
> is a consequence of the other fields, proved as
> `AlgebraicGeometry.ProjectivePlaneCurve.irreducible_dehomCoeff`, and
> `AlgebraicGeometry.ProjectivePlaneCurve.ofEquation` builds the structure from `F` alone.

```lean
structure ProjectivePlaneCurve (k : Type u) [Field k]
```

**`AlgebraicGeometry.ProjectivePlaneCurve.curve`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 630](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L630). The attribute's comment: “the projective plane curve D = V(F)”.

> **Stacks 09U0.** The projective plane curve `D = V(F)`, the closed subscheme
> `Proj (k[T₀, T₁, T₂]/(F))` of the projective plane cut out by the equation `F`.

```lean
abbrev curve : Scheme.{u}
```

**`AlgebraicGeometry.ProjectivePlaneCurve.inclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 636](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L636). The attribute's comment: “the closed immersion of D into the projective plane”.

> **Stacks 09U0.** The closed immersion of the projective plane curve into the projective
> plane.

```lean
def inclusion : D.curve ⟶ D.projectivePlane
```

**`AlgebraicGeometry.ProjectivePlaneCurve.differential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 647](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L647). The attribute's comment: “the differential ω of the plane curve”.

> **Stacks 09U0.** The distinguished rational differential `ω = dx/f_y = -dy/f_x` of the
> plane curve, taken on its standard affine chart.

```lean
def differential : Ω[D.affineChart.FunctionField⁄k]
```

**`AlgebraicGeometry.ProjectivePlaneCurve.situation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveSituation.lean, line 549](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveSituation.lean#L549). The attribute's comment: “the full situation: D, K, the abstract curve C with the map C → D and its properties, ω and K\_C = div(ω) on C”.

> **Stacks Project, Tag 09U0** (Situation: notation for a plane curve). Let `k` be a perfect
> field (the source takes `k` algebraically closed; perfect suffices), `F ∈ k[T₀, T₁, T₂]`
> irreducible and homogeneous of degree `d` with `T₀ ∤ F`, `D = V(F) ⊆ 𝐏²_k`,
> `f = F(1, x, y)`, and `K` the fraction field of `k[x, y]/(f)`. Then:
>
> * `D` is a projective curve over `k`;
> * the abstract curve `C` of `K` (`abstractCurve`, the normalization of `D`) is a nonsingular
>   projective curve over `k` whose function field is `K` (`functionFieldEquivAbstractCurve`);
> * the map `C ⟶ D` (`abstractCurveMap`) is a surjective morphism over `k`, bijective over the
>   nonsingular locus of `D`, and an isomorphism if `D` is nonsingular;
> * `ω = dx/f_y = -dy/f_x ∈ Ω_{K/k}` (`differential`) is well defined and nonzero;
> * `K_C` (`canonicalDivisor`) is the unique divisor of zeros and poles of `ω` on `C`.
>
> All of these are proved here; nothing about `C`, the map `C ⟶ D` or `K_C` is assumed.

```lean
theorem situation :
    IsCurve k D.toSpec ∧ IsProper D.toSpec ∧
    IsCurve k D.abstractCurveToSpec ∧ IsProjectiveVariety k D.abstractCurveToSpec ∧
    IsRegular D.abstractCurve ∧
    D.abstractCurveMap ≫ D.toSpec = D.abstractCurveToSpec ∧
    Function.Surjective D.abstractCurveMap ∧
    (∀ x ∈ regularLocus D.curve, ∃! c : D.abstractCurve, D.abstractCurveMap c = x) ∧
    (IsRegular D.curve → IsIso D.abstractCurveMap) ∧
    (D.affineChart.partialY ≠ 0 →
      D.differential = D.affineChart.partialY⁻¹ •
        KaehlerDifferential.D k D.affineChart.FunctionField D.affineChart.x) ∧
    (D.affineChart.partialX ≠ 0 →
      D.differential = -(D.affineChart.partialX⁻¹ •
        KaehlerDifferential.D k D.affineChart.FunctionField D.affineChart.y)) ∧
    D.differential ≠ 0 ∧
    ∃! KC : Stacks.Divisors.WeilDivisor D.abstractCurve,
      Stacks.Divisors.IsDivisorOfRationalDifferential D.abstractCurve
        D.functionFieldRingEquivAbstractCurve D.differential KC
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 111.56, Tag 09TV](https://stacks.math.columbia.edu/tag/09TV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
