---
declaration: module
origin: cited
lean: couplingPotential, couplingPotential_analyticAt, couplingPotential_hasFDerivAt, couplingPotential_gradient_zero, couplingPotential_iteratedFDeriv_two, couplingPotential_posDef, coupled_spring_potential
statement: formalized
proof: formalized
---

# Coupled spring potential

The module `PhyslibAlpha.ClassicalMechanics.CoupledSpringPotential`, [PhyslibAlpha/ClassicalMechanics/CoupledSpringPotential.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CoupledSpringPotential.lean): 7 declarations, 1 with a docstring.

> The coupled spring potential x₀² + x₀x₁ + x₁² has a local minimum at the origin.

## i. Overview

> As a proof of concept, we use the second derivative test in
> `PhyslibAlpha.Mathematics.PartialDerivativeTest`
> to prove that the coupled spring potential
> `U := fun x : EuclideanSpace ℝ (Fin 2) => (x 0)^2 + x 0 * x 1 + (x 1)^2`
> has a local minimum at zero.
>
> To apply the test we show the potential is analytic, that its gradient vanishes at the origin, and
> that its second derivative quadratic map is positive definite there.

## ii. Key results

> - `couplingPotential` : the potential energy of a pair of coupled springs.
> - `couplingPotential_gradient_zero` : the gradient of the potential vanishes at the origin.
> - `couplingPotential_posDef` : the second derivative quadratic map is positive definite at the
>   origin.
> - `coupled_spring_potential` : the coupled spring potential has a local minimum at zero.

## iv. References

> * None.

## A. The coupled spring potential

**`couplingPotential`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CoupledSpringPotential.lean#L56).

> The potential energy of a pair of coupled springs.

```lean
noncomputable def couplingPotential (x : EuclideanSpace ℝ (Fin 2)) : ℝ
```

## B. Analyticity and derivatives

**`couplingPotential_analyticAt`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CoupledSpringPotential.lean#L68).

```lean
lemma couplingPotential_analyticAt (z : EuclideanSpace ℝ (Fin 2)) :
    AnalyticAt ℝ couplingPotential z
```

**`couplingPotential_hasFDerivAt`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CoupledSpringPotential.lean#L81).

```lean
lemma couplingPotential_hasFDerivAt (x : EuclideanSpace ℝ (Fin 2)) :
    HasFDerivAt couplingPotential
      ((2 * x 0 + x 1) • (EuclideanSpace.proj (𝕜 := ℝ) 0)
        + (x 0 + 2 * x 1) • (EuclideanSpace.proj (𝕜 := ℝ) 1)) x
```

**`couplingPotential_gradient_zero`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CoupledSpringPotential.lean#L97).

```lean
lemma couplingPotential_gradient_zero :
    gradient couplingPotential (!₂[0, 0] : EuclideanSpace ℝ (Fin 2)) = 0
```

**`couplingPotential_iteratedFDeriv_two`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CoupledSpringPotential.lean#L106).

```lean
lemma couplingPotential_iteratedFDeriv_two (z : EuclideanSpace ℝ (Fin 2))
    (a b : EuclideanSpace ℝ (Fin 2)) :
    iteratedFDeriv ℝ 2 couplingPotential z ![a, b]
      = 2 * a 0 * b 0 + a 0 * b 1 + a 1 * b 0 + 2 * a 1 * b 1
```

## C. The local minimum at the origin

**`couplingPotential_posDef`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CoupledSpringPotential.lean#L142).

```lean
lemma couplingPotential_posDef :
    (iteratedFDerivQuadraticMap couplingPotential
    (!₂[0, 0] : EuclideanSpace ℝ (Fin 2))).PosDef
```

**`coupled_spring_potential`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CoupledSpringPotential.lean#L153).

```lean
lemma coupled_spring_potential :
    let U := fun x : EuclideanSpace ℝ (Fin 2) => (x 0)^2 + x 0 * x 1 + (x 1)^2
    IsLocalMin U {
        ofLp := ![0,0]
    }
```

## Depends on

- [The Second Partial Derivatives Test](../mathematics/part-01/partialderivativetest.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/CoupledSpringPotential.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CoupledSpringPotential.lean)
