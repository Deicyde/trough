---
declaration: section
origin: cited
lean: Stacks.Divisors.IsDivisorOfRationalDifferential, Stacks.Divisors.isDivisorOfRationalDifferential_weilDivisorOfMeromorphicSection, Stacks.Divisors.exists_isDivisorOfRationalDifferential, AlgebraicGeometry.AffinePlaneCurve.partialX_ne_zero_or_partialY_ne_zero, AlgebraicGeometry.AffinePlaneCurve.inv_partialY_smul_D_x_eq_neg_inv_partialX_smul_D_y, AlgebraicGeometry.AffinePlaneCurve.inv_partialY_smul_D_x_ne_zero, AlgebraicGeometry.AffinePlaneCurve.neg_inv_partialX_smul_D_y_ne_zero, AlgebraicGeometry.AffinePlaneCurve.differential
statement: formalized
proof: formalized
---

# 111.56 Schemes, Final Exam, Fall 2013

Section 111.56 of the Stacks Project, [Tag 09TV](https://stacks.math.columbia.edu/tag/09TV). 1 tag here is carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09U0, a situation

[Tag 09U0](https://stacks.math.columbia.edu/tag/09U0) in the Stacks Project.

**`Stacks.Divisors.IsDivisorOfRationalDifferential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/MeromorphicOrder/RationalDifferential.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/MeromorphicOrder/RationalDifferential.lean#L79). The attribute's comment: “the divisor of zeros and poles of ω”.

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

**`Stacks.Divisors.isDivisorOfRationalDifferential_weilDivisorOfMeromorphicSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/MeromorphicOrder/RationalDifferential.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/MeromorphicOrder/RationalDifferential.lean#L96). The attribute's comment: “the divisor of zeros and poles of ω”.

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

**`Stacks.Divisors.exists_isDivisorOfRationalDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/MeromorphicOrder/RationalDifferential.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/MeromorphicOrder/RationalDifferential.lean#L113). The attribute's comment: “the divisor of zeros and poles of ω”.

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

**`AlgebraicGeometry.AffinePlaneCurve.partialX_ne_zero_or_partialY_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L358). The attribute's comment: “well-definedness of ω: a partial derivative survives”.

> **Stacks 09U0.** At least one of the two partial derivatives of an irreducible plane
> equation over a perfect field is nonzero in the function field of the curve it cuts out.
> This is what makes the differential `ω = dx/f_y = -dy/f_x` well defined.

```lean
theorem partialX_ne_zero_or_partialY_ne_zero [PerfectField k] :
    C.partialX ≠ 0 ∨ C.partialY ≠ 0
```

**`AlgebraicGeometry.AffinePlaneCurve.inv_partialY_smul_D_x_eq_neg_inv_partialX_smul_D_y`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 486](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L486). The attribute's comment: “well-definedness of ω: the two formulas agree”.

> **Stacks 09U0.** Where both partial derivatives are nonzero, the two formulas
> `dx/f_y` and `-dy/f_x` for the distinguished differential agree.

```lean
theorem inv_partialY_smul_D_x_eq_neg_inv_partialX_smul_D_y
    (hx : C.partialX ≠ 0) (hy : C.partialY ≠ 0) :
    C.partialY⁻¹ • KaehlerDifferential.D k C.FunctionField C.x =
      -(C.partialX⁻¹ • KaehlerDifferential.D k C.FunctionField C.y)
```

**`AlgebraicGeometry.AffinePlaneCurve.inv_partialY_smul_D_x_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L505). The attribute's comment: “well-definedness of ω: dx/f_y is nonzero”.

> **Stacks 09U0.** If the partial derivative with respect to `y` is nonzero, then
> `dx/f_y` is a nonzero differential.

```lean
theorem inv_partialY_smul_D_x_ne_zero (hy : C.partialY ≠ 0) :
    C.partialY⁻¹ • KaehlerDifferential.D k C.FunctionField C.x ≠ 0
```

**`AlgebraicGeometry.AffinePlaneCurve.neg_inv_partialX_smul_D_y_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 512](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L512). The attribute's comment: “well-definedness of ω: -dy/f_x is nonzero”.

> **Stacks 09U0.** If the partial derivative with respect to `x` is nonzero, then
> `-dy/f_x` is a nonzero differential.

```lean
theorem neg_inv_partialX_smul_D_y_ne_zero (hx : C.partialX ≠ 0) :
    -(C.partialX⁻¹ • KaehlerDifferential.D k C.FunctionField C.y) ≠ 0
```

**`AlgebraicGeometry.AffinePlaneCurve.differential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 521](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L521). The attribute's comment: “the differential ω”.

> **Stacks 09U0.** The distinguished rational differential `ω = dx/f_y = -dy/f_x` of an
> irreducible affine plane curve.

```lean
def differential : Ω[C.FunctionField⁄k]
```

**`AlgebraicGeometry.AffinePlaneCurve.differential_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L542). The attribute's comment: “ω is nonzero”.

> **Stacks 09U0.** The distinguished differential of an irreducible plane curve over a
> perfect field is nonzero.

```lean
theorem differential_ne_zero [PerfectField k] : C.differential ≠ 0
```

**`AlgebraicGeometry.ProjectivePlaneCurve`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 562](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L562). The attribute's comment: “the plane-curve situation”.

> **Stacks 09U0.** An irreducible projective plane curve `D = V(F)` over a field, together
> with the affine plane curve cut out on the standard chart `X₀ = 1` by the dehomogenization
> `f(x, y) = F(1, x, y)`.
>
> The irreducibility of the dehomogenization is carried as a field rather than deduced from the
> irreducibility of `F` and the assumption that `F` is not a scalar multiple of the first
> coordinate.

```lean
structure ProjectivePlaneCurve (k : Type u) [Field k]
```

**`AlgebraicGeometry.ProjectivePlaneCurve.curve`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 606](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L606). The attribute's comment: “the projective plane curve D = V(F)”.

> **Stacks 09U0.** The projective plane curve `D = V(F)`, as the reduced induced closed
> subscheme of the projective plane on the vanishing set of `F`.

```lean
def curve : Scheme.{u}
```

**`AlgebraicGeometry.ProjectivePlaneCurve.inclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 612](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L612). The attribute's comment: “the closed immersion of D into the projective plane”.

> **Stacks 09U0.** The closed immersion of the projective plane curve into the projective
> plane.

```lean
def inclusion : D.curve ⟶ D.projectivePlane
```

**`AlgebraicGeometry.ProjectivePlaneCurve.differential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PlaneCurveDifferential.lean#L618). The attribute's comment: “the differential ω of the plane curve”.

> **Stacks 09U0.** The distinguished rational differential `ω = dx/f_y = -dy/f_x` of the
> plane curve, taken on its standard affine chart.

```lean
def differential : Ω[D.affineChart.FunctionField⁄k]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 111.56, Tag 09TV](https://stacks.math.columbia.edu/tag/09TV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
