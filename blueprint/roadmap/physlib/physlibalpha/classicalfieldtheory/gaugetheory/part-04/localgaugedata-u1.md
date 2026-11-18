---
declaration: module
origin: cited
lean: U1, JetU1, U1AlgebraOver, U1Algebra, JetU1Algebra, U1AlgebraOver.bracket_eq_zero, JetU1.eval, JetU1.eval_val
statement: formalized
proof: formalized
---

# The local gauge data of `U(1)`

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.U1`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean): 38 declarations (4 instances with no name), 19 with a docstring.

## i. Overview

> The abelian gauge group `U(1)`, with its jets, its Lie algebra and the jets of its Lie
> algebra, packaged as local gauge data `LocalGaugeData.u1`. The jets of gauge
> transformations are the unitary formal power series, the Lie algebra is the self-adjoint
> (real) scalars and its jets the self-adjoint power series, with vanishing bracket and
> trivial adjoint action. The Maurer–Cartan form is `i (∂_μ u) u⁻¹`.
>
> Read as `1 × 1` matrices, this is a presentation by matrices of jets,
> `LocalGaugeData.u1MatrixJets`, so the laws of the local gauge data and its faithfulness come
> from `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.MatrixJets`. What this file
> supplies is the carriers, the structure maps on them, and the canonical `U1Factor`.

## ii. Key results

> - `U1`, `JetU1`, `U1Algebra`, `JetU1Algebra` : the carriers.
> - `LocalGaugeData.u1MatrixJets` : the presentation of `U(1)` by `1 × 1` matrices of jets.
> - `LocalGaugeData.u1` : the local gauge data of `U(1)`.
> - `LocalGaugeData.u1Factor` : its canonical `U(1)` factor.
> - `LocalGaugeData.instFaithfulU1` : the package is faithful.
> - `LocalGaugeData.instFreeU1` : the package is free.

## iv. References

> * None.

## A. The carriers

**`U1`**, an abbrev, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L62).

> The gauge group `U(1)`.

```lean
abbrev U1 : Type
```

**`JetU1`**, an abbrev, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L65).

> Jets of `U(1)` gauge transformations: unitary formal power series.

```lean
abbrev JetU1 : Type
```

**`U1AlgebraOver`**, an abbrev, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L69).

> The Lie algebra `u(1)` over a `*`-ring: the self-adjoint elements, with vanishing
> bracket.

```lean
abbrev U1AlgebraOver (R : Type) [Ring R] [StarRing R] : Type
```

**`U1Algebra`**, an abbrev, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L72).

> The Lie algebra `u(1)`: the self-adjoint (real) scalars.

```lean
abbrev U1Algebra : Type
```

**`JetU1Algebra`**, an abbrev, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L75).

> Jets of the Lie algebra `u(1)`: the self-adjoint formal power series.

```lean
abbrev JetU1Algebra : Type
```

**An instance with no name**, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L81).

```lean
instance : Bracket (U1AlgebraOver R) (U1AlgebraOver R)
```

**`U1AlgebraOver.bracket_eq_zero`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L84).

```lean
lemma bracket_eq_zero (a b : U1AlgebraOver R) : ⁅a, b⁆ = 0
```

**An instance with no name**, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L86).

```lean
instance : LieRing (U1AlgebraOver R)
```

**An instance with no name**, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L92).

```lean
instance [Algebra ℝ R] [StarModule ℝ R] : LieAlgebra ℝ (U1AlgebraOver R)
```

**An instance with no name**, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L97).

```lean
instance : Module.Finite ℝ U1Algebra
```

## B. The structure maps

**`JetU1.eval`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L109).

> Evaluation of a jet of a `U(1)` gauge transformation at the base point.

```lean
noncomputable def eval : JetU1 →* U1
```

**`JetU1.eval_val`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L119).

```lean
lemma eval_val (u : JetU1) : (eval u : ℂ) = constantCoeff (u : SpaceTimeAlgebra)
```

**`JetU1.ofConstant`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L122).

> The jet of a constant `U(1)` gauge transformation.

```lean
noncomputable def ofConstant : U1 →* JetU1
```

**`JetU1.ofConstant_val`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L132).

```lean
lemma ofConstant_val (u : U1) : (ofConstant u : SpaceTimeAlgebra) = C (u : ℂ)
```

**`JetU1.deriv`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L135).

> The formal derivative of a `u(1)` jet.

```lean
noncomputable def deriv (μ : Fin 1 ⊕ Fin 3) : JetU1Algebra →ₗ[ℝ] JetU1Algebra
```

**`JetU1.deriv_val`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L145).

```lean
lemma deriv_val (μ : Fin 1 ⊕ Fin 3) (a : JetU1Algebra) :
    (deriv μ a : SpaceTimeAlgebra) = pderiv μ a
```

**`JetU1.coord`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L150).

> Multiplication of a `u(1)` jet by the coordinate `x_μ`.

```lean
noncomputable def coord (μ : Fin 1 ⊕ Fin 3) : JetU1Algebra →ₗ[ℝ] JetU1Algebra
```

**`JetU1.coord_val`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L158).

```lean
lemma coord_val (μ : Fin 1 ⊕ Fin 3) (a : JetU1Algebra) :
    (coord μ a : SpaceTimeAlgebra) = (X μ : SpaceTimeAlgebra) * a
```

**`JetU1.evalLie`**, a def, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L162).

> Evaluation of a `u(1)` jet at the base point.

```lean
noncomputable def evalLie : JetU1Algebra →ₗ[ℝ] U1Algebra
```

**`JetU1.evalLie_val`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L172).

```lean
lemma evalLie_val (a : JetU1Algebra) : (evalLie a : ℂ) = constantCoeff (a : SpaceTimeAlgebra)
```

**`JetU1.ofConstantLie`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L175).

> A constant as a `u(1)` jet.

```lean
noncomputable def ofConstantLie : U1Algebra →ₗ[ℝ] JetU1Algebra
```

**`JetU1.ofConstantLie_val`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L185).

```lean
lemma ofConstantLie_val (a : U1Algebra) : (ofConstantLie a : SpaceTimeAlgebra) = C (a : ℂ)
```

## C. The Maurer–Cartan form

**`JetU1.star_mcVal`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L194).

> The Maurer–Cartan scalar `i (∂_μ u) u⁻¹` of a unitary jet is self-adjoint.

```lean
lemma star_mcVal (u : JetU1) (μ : Fin 1 ⊕ Fin 3) :
    star (Complex.I • (pderiv μ (u : SpaceTimeAlgebra) * star (u : SpaceTimeAlgebra)))
      = Complex.I • (pderiv μ (u : SpaceTimeAlgebra) * star (u : SpaceTimeAlgebra))
```

**`JetU1.mc`**, a def, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L210).

> The Maurer–Cartan form `i (∂_μ u) u⁻¹` of a `U(1)` jet.

```lean
noncomputable def mc (u : JetU1) (μ : Fin 1 ⊕ Fin 3) : JetU1Algebra
```

**`JetU1.mc_val`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L214).

```lean
lemma mc_val (u : JetU1) (μ : Fin 1 ⊕ Fin 3) :
    (mc u μ : SpaceTimeAlgebra) = Complex.I •
        (pderiv μ (u : SpaceTimeAlgebra) * star (u : SpaceTimeAlgebra))
```

## D. The presentation and the local gauge data

**`LocalGaugeData.u1MatrixJets`**, a def, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L232).

> **The presentation of `U(1)` by `1 × 1` matrices of jets.**

```lean
noncomputable def u1MatrixJets : MatrixJets (Fin 1) U1 U1Algebra JetU1 JetU1Algebra
```

**`LocalGaugeData.u1`**, a def, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L286).

> **The local gauge data of `U(1)`**: unitary jets, self-adjoint scalar jets with
> vanishing bracket and trivial adjoint action, and the Maurer–Cartan form
> `i (∂_μ u) u⁻¹`.

```lean
noncomputable def u1 : LocalGaugeData U1 U1Algebra JetU1 JetU1Algebra
```

**`LocalGaugeData.u1_eval`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L289).

```lean
lemma u1_eval : u1.eval = JetU1.eval
```

**`LocalGaugeData.u1_ofConstant`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L290).

```lean
lemma u1_ofConstant : u1.ofConstant = JetU1.ofConstant
```

**`LocalGaugeData.u1_evalLie_apply`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L291).

```lean
lemma u1_evalLie_apply (a : JetU1Algebra) : u1.evalLie a = JetU1.evalLie a
```

**`LocalGaugeData.u1_ofConstantLie`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L292).

```lean
lemma u1_ofConstantLie : u1.ofConstantLie = JetU1.ofConstantLie
```

**`LocalGaugeData.u1_deriv`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L293).

```lean
lemma u1_deriv (μ : Fin 1 ⊕ Fin 3) : u1.deriv μ = JetU1.deriv μ
```

**`LocalGaugeData.u1_maurerCartan`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L294).

```lean
lemma u1_maurerCartan : u1.maurerCartan = JetU1.mc
```

**`LocalGaugeData.u1_adjointJ`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L295).

```lean
lemma u1_adjointJ (u : JetU1) (a : JetU1Algebra) : u1.adjointJ u a = a
```

**`LocalGaugeData.u1_iteratedDeriv_val`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L298).

> The iterated derivative on `u(1)` jets is the iterated formal derivative.

```lean
lemma u1_iteratedDeriv_val (s : Multiset (Fin 1 ⊕ Fin 3)) (a : JetU1Algebra) :
    (u1.iteratedDeriv s a : SpaceTimeAlgebra) =
      SpaceTimeAlgebra.iteratedPDeriv s (a : SpaceTimeAlgebra)
```

**`LocalGaugeData.instFaithfulU1`**, an instance, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L309).

> The local gauge data of `U(1)` is faithful.

```lean
instance instFaithfulU1 : u1.Faithful
```

**`LocalGaugeData.instFreeU1`**, an instance, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L313).

> The local gauge data of `U(1)` is free. Real Taylor data give a self-adjoint jet, and
> the unitary Euler transport of a `1 × 1` matrix is a unitary jet.

```lean
instance instFreeU1 : u1.Free
```

## E. The canonical factor

**`LocalGaugeData.u1Factor`**, a def, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean#L337).

> The canonical `U(1)` factor of the local gauge data of `U(1)`.

```lean
noncomputable def u1Factor : U1Factor u1
```

## Depends on

- [Matrix jet groups](localgaugedata-matrixjets.md)
- [Scalar matrices](../../../mathematics/part-02/formathlib/datastructures-matrix-scalar.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/U1.lean)
