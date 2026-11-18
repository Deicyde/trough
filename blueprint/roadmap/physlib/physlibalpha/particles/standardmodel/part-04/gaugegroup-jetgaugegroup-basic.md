---
declaration: module
origin: cited
lean: StandardModel.JetGaugeGroupI, StandardModel.JetGaugeGroupI.toVal, StandardModel.JetGaugeGroupI.mapMatrix_constantCoeff_star, StandardModel.JetGaugeGroupI.evalSU, StandardModel.JetGaugeGroupI.evalU1, StandardModel.JetGaugeGroupI.eval, StandardModel.JetGaugeGroupI.deriv, StandardModel.JetGaugeGroupI.deriv_mul
statement: formalized
proof: formalized
---

# The jet gauge group

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.JetGaugeGroup.Basic`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean): 21 declarations, 12 with a docstring.

## i. Overview

> For the Standard Model on Minkowski spacetime,
> gauge transforms are maps from spacetime to the gauge group `G := SU(3) × SU(2) × U(1)`.
>
> If one is considering a gauge transformation `g` at a point `x`, its action
> on all the fields and their derivatives at `x` is determined by the
> value of `g` and all its derivatives at `x`.  The collection of all
> possible values of `g` and their derivatives at `x` is called the *jet* of `g` at `x`.
> These form a group, which we call `JetGaugeGroupI`.
>
> The group `JetGaugeGroupI` acts on all the fields and their derivatives at `x`,
> every gauge transformation `g` has a corresponding element of `JetGaugeGroupI`,
> and the action of `g` on the fields and their derivatives at `x` is determined by this element.
>
> Thus locally it is enough to consider the action of `JetGaugeGroupI` on the fields and
> their derivatives at a point, instead of the full set of gauge transformations on spacetime,
> which is large and unwieldy.
>
> A Lagrangian at a point x is a polynomial in the fields and
>  finitely many of their derivatives at x — that is the whole of
>  its input. Symmetries of such an expression can therefore only
>  ever see fields through that same finite window, and so a
>  symmetry given by a function g : M → G can only act through the
>  data g(x), ∂g(x), ∂²g(x), …. Two gauge transformations with the
>  same Taylor expansion at x are indistinguishable to every
>  Lagrangian at x: the honest symmetry group is not C^∞(M, G) but
>  its quotient by that equivalence, the group of jets at x.
>
>
> So we want to work with Taylor expansions rather than functions.
> The key observation is that Taylor expansions can be added and
> multiplied just like numbers: the coefficients of a product are
> given by the familiar sums of binomial coefficients times pairs
> of derivatives, which is just the Leibniz rule. This makes them a
> ring, which we call SpaceTimeAlgebra — it plays the same role that ℂ does
> for ordinary numbers, only its elements record a value together
> with all of its derivatives.
>
> Now, a group like SU(3), SU(2), or U(1) is defined by equations
>  in matrix entries — U*U = 1, det U = 1 — and nothing in those
>  equations demands that the entries be complex numbers. They make
>  sense whenever the entries can be added, multiplied, and
>  conjugated. In particular, they make sense for matrices whose
>  entries are Taylor expansions. Writing down the Standard Model
>  gauge group with entries in SpaceTimeAlgebra instead of ℂ gives
>  JetGaugeGroupI, and unwinding the definitions shows this is
>  precisely the group of Taylor expansions of gauge
>  transformations: an element is a g(x) together with all its
>  derivatives, constrained to be unitary order by order.
>
> The payoff is that the derivative bookkeeping disappears into th
>  ring multiplication. Products, inverses, and the adjoint action
>   of jets are just the group operations of JetGaugeGroupI, so
>   facts like "the jet of the inverse is the inverse of the jet"
>   hold for free instead of needing a separate check at each
>   order. We use infinite Taylor expansions rather than truncating
>   at some order k, so that a single group acts on Lagrangians of
>   every derivative order at once. The resulting group is blind to
>   everything global — topology, winding, large gauge
>   transformations — which is exactly right, since so is a
>   Lagrangian at a point.

## ii. Key results

> - `JetGaugeGroupI` : the jets of gauge transformations, the gauge group with coefficients
>   in `SpaceTimeAlgebra`.
> - `JetGaugeGroupI.eval`, `JetGaugeGroupI.ofConstant` : evaluation at the base point and
>   the constant jets, with `eval_ofConstant`.
> - `JetGaugeGroupI.deriv` : the entrywise formal derivative of a jet, with the Leibniz rule
>   `deriv_mul` and the hermiticity and tracelessness of `i (∂_μ U) U⁻¹` that make the
>   Maurer–Cartan form take values in the jet gauge algebra.

## iv. References

> * None.

## A. The jet gauge group

> The ring `SpaceTimeAlgebra` of formal power series in the spacetime coordinates, in which
> jets of fields and of gauge transformations are valued, is defined in
> `PhyslibAlpha.SpaceAndTime.SpaceTime.SpaceTimeDerivAlgebra`, together with the algebra of derivative
> symbols `SpaceTimeDerivAlgebraℂ` and the action `SpaceTimeDerivAlgebraℂ.jetRingAction`
> of the jet ring on it.

**`StandardModel.JetGaugeGroupI`**, an abbrev, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L128).

> The group of formal infinite-order jets, at a spacetime point, of local gauge
> transformations of the Standard Model: the `R`-points of the gauge group for `R`
> the ring `SpaceTimeAlgebra` of formal power series in the spacetime coordinates.
>
> Since gauge transformations multiply pointwise, jets multiply as power series and
> the group structure is that of the matrix groups over `SpaceTimeAlgebra`. The unitarity and
> determinant constraints hold as power-series identities, i.e. at every jet order.
>
> Evaluation at the base point recovers `GaugeGroupI`; see `JetGaugeGroupI.eval`.

```lean
abbrev JetGaugeGroupI : Type
```

**`StandardModel.JetGaugeGroupI.toVal`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L136).

> The underlying matrix value of an element of `JetGaugeGroupI`.

```lean
def toVal (U : JetGaugeGroupI) : Matrix (Fin 3) (Fin 3) SpaceTimeAlgebra × Matrix (Fin 2)
    (Fin 2) SpaceTimeAlgebra × SpaceTimeAlgebra
```

## B. Evaluation at the base point

> The constant coefficient of a power series is its value at the base point of the
> jet. Applied entrywise it sends jets of gauge transformations to their zeroth-order
> parts, giving a group homomorphism `JetGaugeGroupI →* GaugeGroupI`.

**`StandardModel.JetGaugeGroupI.mapMatrix_constantCoeff_star`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L151).

> Entrywise evaluation at the base point commutes with the conjugate transpose.

```lean
lemma mapMatrix_constantCoeff_star {n : Type} [Fintype n] [DecidableEq n]
    (A : Matrix n n SpaceTimeAlgebra) :
    (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix (star A) =
      star ((constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix A)
```

**`StandardModel.JetGaugeGroupI.evalSU`**, a def, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L160).

> Evaluation of a jet of a special-unitary gauge transformation at the base point:
> the entrywise constant coefficient.

```lean
noncomputable def evalSU (n : Type) [Fintype n] [DecidableEq n] :
    specialUnitaryGroup n SpaceTimeAlgebra →* specialUnitaryGroup n ℂ
```

**`StandardModel.JetGaugeGroupI.evalU1`**, a def, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L176).

> Evaluation of a jet of a `U(1)` gauge transformation at the base point: the
> constant coefficient.

```lean
noncomputable def evalU1 : unitary SpaceTimeAlgebra →* unitary ℂ
```

**`StandardModel.JetGaugeGroupI.eval`**, a def, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L188).

> Evaluation of a jet of a gauge transformation at the base point, projecting the
> jet gauge group onto the gauge group `GaugeGroupI` by taking zeroth-order parts on
> each factor.

```lean
noncomputable def eval : JetGaugeGroupI →* GaugeGroupI
```

## C. The derivative

> We define the derivative of an element of `JetGaugeGroupI` as a product of matrices,
> and give some properties of it related to the Maurer–Cartan form.

**`StandardModel.JetGaugeGroupI.deriv`**, a def, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L203).

> The derivative of an element of `JetGaugeGroupI` returning
> a product of matrices.

```lean
noncomputable def deriv (μ : Fin 1 ⊕ Fin 3) (U : JetGaugeGroupI) :
    Matrix (Fin 3) (Fin 3) SpaceTimeAlgebra × Matrix (Fin 2)
        (Fin 2) SpaceTimeAlgebra × SpaceTimeAlgebra
```

**`StandardModel.JetGaugeGroupI.deriv_mul`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L209).

```lean
lemma deriv_mul (μ : Fin 1 ⊕ Fin 3) (U V : JetGaugeGroupI) :
    deriv μ (U * V) = deriv μ U * V.toVal + U.toVal * deriv μ V
```

**`StandardModel.JetGaugeGroupI.deriv_one`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L231).

```lean
lemma deriv_one (μ : Fin 1 ⊕ Fin 3) : deriv μ (1 : JetGaugeGroupI) = 0
```

**`StandardModel.JetGaugeGroupI.star_deriv`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L242).

```lean
lemma star_deriv (μ : Fin 1 ⊕ Fin 3) (U : JetGaugeGroupI) :
    star (deriv μ U) = deriv μ (star U)
```

**`StandardModel.JetGaugeGroupI.deriv_mul_inv_toVal_SU3_traceless`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L256).

```lean
lemma deriv_mul_inv_toVal_SU3_traceless (μ : Fin 1 ⊕ Fin 3) (U : JetGaugeGroupI) :
    (Complex.I • (deriv μ U * (U⁻¹).toVal)).1.trace = 0
```

**`StandardModel.JetGaugeGroupI.deriv_mul_inv_toVal_SU2_traceless`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L281).

```lean
lemma deriv_mul_inv_toVal_SU2_traceless (μ : Fin 1 ⊕ Fin 3) (U : JetGaugeGroupI) :
    (Complex.I • (deriv μ U * (U⁻¹).toVal)).2.1.trace = 0
```

**`StandardModel.JetGaugeGroupI.star_deriv_mul_inv_toVal_SU3`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L304).

```lean
lemma star_deriv_mul_inv_toVal_SU3 (μ : Fin 1 ⊕ Fin 3) (U : JetGaugeGroupI) :
    star ((Complex.I • (deriv μ U * (U⁻¹).toVal)).1) =
    (Complex.I • (deriv μ U * (U⁻¹).toVal)).1
```

**`StandardModel.JetGaugeGroupI.star_deriv_mul_inv_toVal_SU2`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L328).

```lean
lemma star_deriv_mul_inv_toVal_SU2 (μ : Fin 1 ⊕ Fin 3) (U : JetGaugeGroupI) :
    star ((Complex.I • (deriv μ U * (U⁻¹).toVal)).2.1) =
    (Complex.I • (deriv μ U * (U⁻¹).toVal)).2.1
```

**`StandardModel.JetGaugeGroupI.star_deriv_mul_inv_toVal_U1`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L352).

```lean
lemma star_deriv_mul_inv_toVal_U1 (μ : Fin 1 ⊕ Fin 3) (U : JetGaugeGroupI) :
    star ((Complex.I • (deriv μ U * (U⁻¹).toVal)).2.2) =
    (Complex.I • (deriv μ U * (U⁻¹).toVal)).2.2
```

## D. Constant jets

> The constant power series embed the gauge group `GaugeGroupI` into the jet gauge
> group, as the jets of constant (global) gauge transformations. This is a section of
> the evaluation `eval`.

**`StandardModel.JetGaugeGroupI.mapMatrix_C_star`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L385).

> Entrywise inclusion of constants commutes with the conjugate transpose.

```lean
lemma mapMatrix_C_star {n : Type} [Fintype n] [DecidableEq n] (A : Matrix n n ℂ) :
    (C : ℂ →+* SpaceTimeAlgebra).mapMatrix (star A) = star
        ((C : ℂ →+* SpaceTimeAlgebra).mapMatrix A)
```

**`StandardModel.JetGaugeGroupI.ofConstantSU`**, a def, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L393).

> The jet of a constant special-unitary gauge transformation: the entrywise
> inclusion of constants.

```lean
noncomputable def ofConstantSU (n : Type) [Fintype n] [DecidableEq n] :
    specialUnitaryGroup n ℂ →* specialUnitaryGroup n SpaceTimeAlgebra
```

**`StandardModel.JetGaugeGroupI.ofConstantU1`**, a def, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L408).

> The jet of a constant `U(1)` gauge transformation: the inclusion of constants.

```lean
noncomputable def ofConstantU1 : unitary ℂ →* unitary SpaceTimeAlgebra
```

**`StandardModel.JetGaugeGroupI.ofConstant`**, a def, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L419).

> The embedding of the gauge group into the jet gauge group as the jets of
> constant (global) gauge transformations.

```lean
noncomputable def ofConstant : GaugeGroupI →* JetGaugeGroupI
```

**`StandardModel.JetGaugeGroupI.eval_ofConstant`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L425).

> Evaluating the jet of a constant gauge transformation at the base point recovers
> the gauge transformation: `ofConstant` is a section of `eval`.

```lean
lemma eval_ofConstant (g : GaugeGroupI) : eval (ofConstant g) = g
```

**`StandardModel.JetGaugeGroupI.deriv_ofConstant`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean#L436).

```lean
lemma deriv_ofConstant (μ : Fin 1 ⊕ Fin 3) (U₀ : GaugeGroupI) :
    deriv μ (JetGaugeGroupI.ofConstant U₀) = 0
```

## Depends on

- [The Standard Model Gauge Group](../../../../physlib/particles/standardmodel/gaugegroup/basic.md)
- [Complex conjugation in the spacetime algebra](../../../../physlib/spaceandtime/spacetime/spacetimealgebra-star.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Basic.lean)
