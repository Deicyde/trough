---
declaration: module
origin: cited
lean: SU, JetSU, SUAlgebra, JetSUAlgebra, JetSU.val_mul_star, JetSU.star_mul_val, JetSU.det_val, JetSU.star_val_eq_adjugate
statement: formalized
proof: formalized
---

# The local gauge data of `SU(n)`

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.SU.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean): 43 declarations, 20 with a docstring.

## i. Overview

> The gauge group `SU(n)`, with its jets, its Lie algebra and the jets of its Lie algebra,
> packaged as local gauge data `LocalGaugeData.su n`. The jets of gauge transformations are
> the special unitary matrices of formal power series, the Lie algebra `su(n)` is the
> traceless hermitian matrices (`SUAlgebraOver ℂ n`) and its jets the traceless hermitian
> matrices of power series. Evaluation and the constant inclusion act entrywise, the adjoint
> action is conjugation, and the Maurer–Cartan form is `i (∂_μ U) U⁻¹`, hermitian by the
> differentiated unitarity relation and traceless by Jacobi's formula.
>
> This is a presentation by matrices of jets, `LocalGaugeData.suMatrixJets n`, so the laws of
> the local gauge data, its canonical `SUFactor` and its faithfulness come from
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.MatrixJets`. What this file
> supplies is the carriers and the structure maps on them.

## ii. Key results

> - `SU`, `JetSU`, `SUAlgebra`, `JetSUAlgebra` : the carriers.
> - `JetSUAlgebra.mc` : the Maurer–Cartan form.
> - `LocalGaugeData.suMatrixJets` : the presentation of `SU(n)` by matrices of jets.
> - `LocalGaugeData.su` : the local gauge data of `SU(n)`.
> - `LocalGaugeData.suFactor` : its canonical `SU(n)` factor.
> - `LocalGaugeData.instFaithfulSU` : the package is faithful.
> - `LocalGaugeData.instFreeSU` : the package is free.

## iv. References

> * None.

## A. The carriers

**`SU`**, an abbrev, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L65).

> The gauge group `SU(n)`.

```lean
abbrev SU (n : ℕ) : Type
```

**`JetSU`**, an abbrev, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L69).

> Jets of `SU(n)` gauge transformations: special unitary matrices of formal power
> series.

```lean
abbrev JetSU (n : ℕ) : Type
```

**`SUAlgebra`**, an abbrev, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L72).

> The Lie algebra `su(n)`: traceless hermitian matrices.

```lean
abbrev SUAlgebra (n : ℕ) : Type
```

**`JetSUAlgebra`**, an abbrev, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L75).

> Jets of the Lie algebra `su(n)`: traceless hermitian matrices of formal power series.

```lean
abbrev JetSUAlgebra (n : ℕ) : Type
```

## B. The structure maps on the group

**`JetSU.val_mul_star`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L87).

```lean
lemma val_mul_star (U : JetSU n) : U.1 * star U.1 = 1
```

**`JetSU.star_mul_val`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L90).

```lean
lemma star_mul_val (U : JetSU n) : star U.1 * U.1 = 1
```

**`JetSU.det_val`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L93).

```lean
lemma det_val (U : JetSU n) : U.1.det = 1
```

**`JetSU.star_val_eq_adjugate`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L96).

> For a special unitary matrix, the conjugate transpose is the adjugate.

```lean
lemma star_val_eq_adjugate (U : JetSU n) : star U.1 = U.1.adjugate
```

**`JetSU.eval`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L104).

> Evaluation of a jet of an `SU(n)` gauge transformation at the base point: the entrywise
> constant coefficient.

```lean
noncomputable def eval : JetSU n →* SU n
```

**`JetSU.eval_val`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L118).

```lean
lemma eval_val (U : JetSU n) : (eval U).1 =
    (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix U.1
```

**`JetSU.ofConstant`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L123).

> The jet of a constant `SU(n)` gauge transformation: the entrywise inclusion of
> constants.

```lean
noncomputable def ofConstant : SU n →* JetSU n
```

**`JetSU.ofConstant_val`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L137).

```lean
lemma ofConstant_val (u : SU n) : (ofConstant u).1 =
    (C : ℂ →+* SpaceTimeAlgebra).mapMatrix u.1
```

**`JetSU.trace_mcMatrix`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L142).

> The Maurer–Cartan matrix `i (∂_μ U) U†` is traceless, by Jacobi's formula and
> `det U = 1`.

```lean
lemma trace_mcMatrix (μ : Fin 1 ⊕ Fin 3) (U : JetSU n) :
    (Complex.I • (U.1.map (pderiv μ) * star U.1)).trace = 0
```

## C. The structure maps on the Lie algebra

**`JetSUAlgebra.deriv`**, a def, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L160).

> The formal derivative in the direction `μ`, entrywise.

```lean
noncomputable def deriv (μ : Fin 1 ⊕ Fin 3) : JetSUAlgebra n →ₗ[ℝ] JetSUAlgebra n
```

**`JetSUAlgebra.deriv_val`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L174).

```lean
lemma deriv_val (μ : Fin 1 ⊕ Fin 3) (a : JetSUAlgebra n) :
    (deriv μ a).1 = a.1.map (pderiv μ)
```

**`JetSUAlgebra.coord`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L178).

> Multiplication by the coordinate `x_μ`, entrywise.

```lean
noncomputable def coord (μ : Fin 1 ⊕ Fin 3) : JetSUAlgebra n →ₗ[ℝ] JetSUAlgebra n
```

**`JetSUAlgebra.coord_val`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L186).

```lean
lemma coord_val (μ : Fin 1 ⊕ Fin 3) (a : JetSUAlgebra n) :
    (coord μ a).1 = (X μ : SpaceTimeAlgebra) • a.1
```

**`JetSUAlgebra.star_mapMatrix_constantCoeff`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L189).

```lean
lemma star_mapMatrix_constantCoeff (a : JetSUAlgebra n) :
    star ((constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix a.1)
      = (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix a.1
```

**`JetSUAlgebra.trace_mapMatrix_constantCoeff`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L194).

```lean
lemma trace_mapMatrix_constantCoeff (a : JetSUAlgebra n) :
    ((constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix a.1).trace = 0
```

**`JetSUAlgebra.evalLie`**, a def, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L199).

> Evaluation at the base point: the entrywise constant coefficient.

```lean
noncomputable def evalLie : JetSUAlgebra n →ₗ[ℝ] SUAlgebra n
```

**`JetSUAlgebra.evalLie_val`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L212).

```lean
lemma evalLie_val (a : JetSUAlgebra n) :
    (evalLie a).1 = (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix a.1
```

**`JetSUAlgebra.star_mapMatrix_C`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L215).

```lean
lemma star_mapMatrix_C (a : SUAlgebra n) :
    star ((C : ℂ →+* SpaceTimeAlgebra).mapMatrix a.1) =
        (C : ℂ →+* SpaceTimeAlgebra).mapMatrix a.1
```

**`JetSUAlgebra.trace_mapMatrix_C`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L220).

```lean
lemma trace_mapMatrix_C (a : SUAlgebra n) :
    ((C : ℂ →+* SpaceTimeAlgebra).mapMatrix a.1).trace = 0
```

**`JetSUAlgebra.ofConstantLie`**, a def, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L225).

> A constant as a jet: the entrywise constant power series.

```lean
noncomputable def ofConstantLie : SUAlgebra n →ₗ[ℝ] JetSUAlgebra n
```

**`JetSUAlgebra.ofConstantLie_val`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L238).

```lean
lemma ofConstantLie_val (a : SUAlgebra n) :
    (ofConstantLie a).1 = (C : ℂ →+* SpaceTimeAlgebra).mapMatrix a.1
```

**`JetSUAlgebra.adjoint`**, a def, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L242).

> The adjoint action `a ↦ U a U†` of the jets of `SU(n)` on the jets of `su(n)`.

```lean
noncomputable def adjoint : Representation ℝ (JetSU n) (JetSUAlgebra n)
```

**`JetSUAlgebra.adjoint_val`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L247).

```lean
lemma adjoint_val (U : JetSU n) (a : JetSUAlgebra n) :
    (adjoint U a).1 = U.1 * a.1 * star U.1
```

**`JetSUAlgebra.adjointValue`**, a def, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L251).

> The adjoint action `a ↦ U a U†` of `SU(n)` on `su(n)`.

```lean
noncomputable def adjointValue : Representation ℝ (SU n) (SUAlgebra n)
```

**`JetSUAlgebra.adjointValue_val`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L256).

```lean
lemma adjointValue_val (U : SU n) (a : SUAlgebra n) :
    (adjointValue U a).1 = U.1 * a.1 * star U.1
```

## D. The Maurer–Cartan form

**`JetSUAlgebra.mc`**, a def, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L266).

> The Maurer–Cartan form `i (∂_μ U) U†` of an `SU(n)` gauge jet.

```lean
noncomputable def mc (U : JetSU n) (μ : Fin 1 ⊕ Fin 3) : JetSUAlgebra n
```

**`JetSUAlgebra.mc_val`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L272).

```lean
lemma mc_val (U : JetSU n) (μ : Fin 1 ⊕ Fin 3) :
    (mc U μ).1 = Complex.I • (U.1.map (pderiv μ) * star U.1)
```

## E. The presentation and the local gauge data

**`LocalGaugeData.suMatrixJets`**, a def, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L287).

> **The presentation of `SU(n)` by matrices of jets**: the carriers are subtypes of
> matrices and every structure map is the matrix one.

```lean
noncomputable def suMatrixJets (n : ℕ) :
    MatrixJets (Fin n) (SU n) (SUAlgebra n) (JetSU n) (JetSUAlgebra n)
```

**`LocalGaugeData.su`**, a def, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L323).

> **The local gauge data of `SU(n)`**: special unitary jets, traceless hermitian jets
> with the bracket `i (a b − b a)` and the conjugation action, and the Maurer–Cartan form
> `i (∂_μ U) U⁻¹`.

```lean
noncomputable def su (n : ℕ) : LocalGaugeData (SU n) (SUAlgebra n) (JetSU n) (JetSUAlgebra n)
```

**`LocalGaugeData.su_eval`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L328).

```lean
lemma su_eval : (su n).eval = JetSU.eval
```

**`LocalGaugeData.su_ofConstant`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L329).

```lean
lemma su_ofConstant : (su n).ofConstant = JetSU.ofConstant
```

**`LocalGaugeData.su_evalLie_apply`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L330).

```lean
lemma su_evalLie_apply (a : JetSUAlgebra n) : (su n).evalLie a = JetSUAlgebra.evalLie a
```

**`LocalGaugeData.su_ofConstantLie`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L332).

```lean
lemma su_ofConstantLie :
    ((su n).ofConstantLie : SUAlgebra n →ₗ[ℝ] JetSUAlgebra n) = JetSUAlgebra.ofConstantLie
```

**`LocalGaugeData.su_deriv`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L334).

```lean
lemma su_deriv (μ : Fin 1 ⊕ Fin 3) : (su n).deriv μ = JetSUAlgebra.deriv μ
```

**`LocalGaugeData.su_adjointJ`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L335).

```lean
lemma su_adjointJ : (su n).adjointJ = JetSUAlgebra.adjoint
```

**`LocalGaugeData.su_maurerCartan`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L336).

```lean
lemma su_maurerCartan : (su n).maurerCartan = JetSUAlgebra.mc
```

**`LocalGaugeData.suFactor`**, a def, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L339).

> The canonical `SU(n)` factor of the local gauge data of `SU(n)`.

```lean
noncomputable def suFactor (n : ℕ) : SUFactor (su n) (Fin n)
```

**`LocalGaugeData.instFaithfulSU`**, an instance, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L342).

> The local gauge data of `SU(n)` is faithful.

```lean
instance instFaithfulSU : (su n).Faithful
```

**`LocalGaugeData.instFreeSU`**, an instance, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean#L347).

> The local gauge data of `SU(n)` is free. Traceless hermitian Taylor data give a
> traceless hermitian matrix of jets, and the unitary Euler transport of a traceless
> hermitian jet has unit determinant by Jacobi's formula.

```lean
instance instFreeSU : (su n).Free
```

## Depends on

- [Matrix jet groups](localgaugedata-matrixjets.md)
- [The Lie algebra `su(n)` over a `*`-algebra](localgaugedata-su-algebra.md)

## Proof depends on

- [Jacobi's formula for matrices of jets](../../../spaceandtime/spacetime/spacetimealgebra-jacobi.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Basic.lean)
