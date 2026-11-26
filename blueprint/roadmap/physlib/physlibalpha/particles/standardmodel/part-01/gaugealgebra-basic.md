---
declaration: module
origin: cited
lean: StandardModel.GaugeAlgebra, StandardModel.GaugeAlgebra.toSU3Matrix, StandardModel.GaugeAlgebra.toSU2Matrix, StandardModel.GaugeAlgebra.toU1Value, StandardModel.GaugeAlgebra.ext_of_matrix, StandardModel.GaugeAlgebra.ofMatrixProd, StandardModel.GaugeAlgebra.ofMatrixProd_toSU3Matrix, StandardModel.GaugeAlgebra.ofMatrixProd_toSU2Matrix
statement: formalized
proof: formalized
---

# The gauge algebra of the Standard Model

The module `PhyslibAlpha.Particles.StandardModel.GaugeAlgebra.Basic`, [PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean): 35 declarations (5 instances with no name), 14 with a docstring.

> The Lie algebra of `SU(3) × SU(2) × U(1)` in the hermitian convention, with its adjoint action.

## i. Overview

> The gauge algebra of the Standard Model is the Lie algebra of `GaugeGroupI`, the direct sum of
> the Lie algebras of `SU(3)`, `SU(2)` and `U(1)`. Following the physics convention, its elements
> are written with hermitian generators. An element is a triple `(c₃, c₂, c₁)` of a traceless
> hermitian `3 × 3` matrix, a traceless hermitian `2 × 2` matrix and a real scalar, and the
> corresponding element of the matrix Lie algebra is `diag(i c₃, i c₂, i c₁)`. The bracket is
> therefore `i` times the matrix commutator, which keeps hermitian matrices hermitian but is only
> real-bilinear. The identification with the Lie algebra of the global gauge group is
> `gaugeAlgebraEquiv`, in `GaugeGroup/LieAlgebra.lean`.
>
> The gauge group acts on its gauge algebra by conjugation of the `su(3)` and `su(2)` factors,
> leaving the abelian `u(1)` factor fixed.

## ii. Key results

> - `StandardModel.GaugeAlgebra` : the gauge algebra of the Standard Model.
> - `StandardModel.GaugeAlgebra.toSU3Matrix`, `StandardModel.GaugeAlgebra.toSU2Matrix`,
>   `StandardModel.GaugeAlgebra.toU1Value` : the components of an element in the three factors.
> - The instance `LieAlgebra ℝ GaugeAlgebra` : the bracket `i [a, b]` on each factor.
> - `StandardModel.GaugeAlgebra.adjoint` : the adjoint action of the gauge group.

## iv. References

> * None.

**`StandardModel.GaugeAlgebra`**, an abbrev, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L63).

> The gauge algebra of the Standard Model, the Lie algebra of `GaugeGroupI` in the hermitian
> convention. It has one factor per gauge group factor, the traceless self-adjoint `3 × 3` and
> `2 × 2` complex matrices and the self-adjoint (that is, real) scalars. It is identified with
> the Lie algebra of `globalGaugeGroup` by `gaugeAlgebraEquiv`.

```lean
abbrev GaugeAlgebra
```

**An instance with no name**, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L72).

> The self-adjoint scalars form a finite-dimensional real vector space, through the
> identification with the corresponding submodule.

```lean
instance : Module.Finite ℝ (selfAdjoint ℂ)
```

**An instance with no name**, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L76).

> The gauge algebra is a finite-dimensional real vector space.

```lean
instance : Module.Finite ℝ GaugeAlgebra
```

## A. Basic projections

**`StandardModel.GaugeAlgebra.toSU3Matrix`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L87).

> The `su(3)`-factor component of an element of the gauge algebra.

```lean
def toSU3Matrix (a : GaugeAlgebra) : Matrix (Fin 3) (Fin 3) ℂ
```

**`StandardModel.GaugeAlgebra.toSU2Matrix`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L90).

> The `su(2)`-factor component of an element of the gauge algebra.

```lean
def toSU2Matrix (a : GaugeAlgebra) : Matrix (Fin 2) (Fin 2) ℂ
```

**`StandardModel.GaugeAlgebra.toU1Value`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L93).

> The `u(1)`-factor component of an element of the gauge algebra.

```lean
def toU1Value (a : GaugeAlgebra) : ℂ
```

**`StandardModel.GaugeAlgebra.ext_of_matrix`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L97).

> Two elements of the gauge algebra with the same three components are equal.

```lean
lemma ext_of_matrix {a b : GaugeAlgebra} (h1 : a.toSU3Matrix = b.toSU3Matrix)
    (h2 : a.toSU2Matrix = b.toSU2Matrix) (h3 : a.toU1Value = b.toU1Value) : a = b
```

## B. Constructor from a product of matrices

**`StandardModel.GaugeAlgebra.ofMatrixProd`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L111).

> The element of the gauge algebra constructed from a triple of matrices satisfying
> the relevant hermiticity and tracelessness conditions.

```lean
def ofMatrixProd (A : Matrix (Fin 3) (Fin 3) ℂ ×
    Matrix (Fin 2) (Fin 2) ℂ × ℂ) (hA : star A.1 = A.1 ∧ A.1.trace = 0)
    (hB : star A.2.1 = A.2.1 ∧ A.2.1.trace = 0) (hC : star A.2.2 = A.2.2) : GaugeAlgebra
```

**`StandardModel.GaugeAlgebra.ofMatrixProd_toSU3Matrix`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L117).

```lean
lemma ofMatrixProd_toSU3Matrix (A : Matrix (Fin 3) (Fin 3) ℂ ×
    Matrix (Fin 2) (Fin 2) ℂ × ℂ) (hA : star A.1 = A.1 ∧ A.1.trace = 0)
    (hB : star A.2.1 = A.2.1 ∧ A.2.1.trace = 0) (hC : star A.2.2 = A.2.2) :
    (ofMatrixProd A hA hB hC).toSU3Matrix = A.1
```

**`StandardModel.GaugeAlgebra.ofMatrixProd_toSU2Matrix`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L123).

```lean
lemma ofMatrixProd_toSU2Matrix (A : Matrix (Fin 3) (Fin 3) ℂ ×
    Matrix (Fin 2) (Fin 2) ℂ × ℂ) (hA : star A.1 = A.1 ∧ A.1.trace = 0)
    (hB : star A.2.1 = A.2.1 ∧ A.2.1.trace = 0) (hC : star A.2.2 = A.2.2) :
    (ofMatrixProd A hA hB hC).toSU2Matrix = A.2.1
```

**`StandardModel.GaugeAlgebra.ofMatrixProd_toU1Value`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L129).

```lean
lemma ofMatrixProd_toU1Value (A : Matrix (Fin 3) (Fin 3) ℂ ×
    Matrix (Fin 2) (Fin 2) ℂ × ℂ) (hA : star A.1 = A.1 ∧ A.1.trace = 0)
    (hB : star A.2.1 = A.2.1 ∧ A.2.1.trace = 0) (hC : star A.2.2 = A.2.2) :
    (ofMatrixProd A hA hB hC).toU1Value = A.2.2
```

## C. The Lie algebra instance

**`StandardModel.GaugeAlgebra.add_toSU3Matrix`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L141).

```lean
lemma add_toSU3Matrix (a b : GaugeAlgebra) :
    (a + b).toSU3Matrix = a.toSU3Matrix + b.toSU3Matrix
```

**`StandardModel.GaugeAlgebra.add_toSU2Matrix`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L145).

```lean
lemma add_toSU2Matrix (a b : GaugeAlgebra) :
    (a + b).toSU2Matrix = a.toSU2Matrix + b.toSU2Matrix
```

**`StandardModel.GaugeAlgebra.add_toU1Value`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L149).

```lean
lemma add_toU1Value (a b : GaugeAlgebra) :
    (a + b).toU1Value = a.toU1Value + b.toU1Value
```

**`StandardModel.GaugeAlgebra.zero_toSU3Matrix`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L153).

```lean
lemma zero_toSU3Matrix : (0 : GaugeAlgebra).toSU3Matrix = 0
```

**`StandardModel.GaugeAlgebra.zero_toSU2Matrix`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L156).

```lean
lemma zero_toSU2Matrix : (0 : GaugeAlgebra).toSU2Matrix = 0
```

**`StandardModel.GaugeAlgebra.zero_toU1Value`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L159).

```lean
lemma zero_toU1Value : (0 : GaugeAlgebra).toU1Value = 0
```

**`StandardModel.GaugeAlgebra.smul_toSU3Matrix`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L162).

```lean
lemma smul_toSU3Matrix (r : ℝ) (a : GaugeAlgebra) :
    (r • a).toSU3Matrix = r • a.toSU3Matrix
```

**`StandardModel.GaugeAlgebra.smul_toSU2Matrix`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L166).

```lean
lemma smul_toSU2Matrix (r : ℝ) (a : GaugeAlgebra) :
    (r • a).toSU2Matrix = r • a.toSU2Matrix
```

**`StandardModel.GaugeAlgebra.smul_toU1Value`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L170).

```lean
lemma smul_toU1Value (r : ℝ) (a : GaugeAlgebra) :
    (r • a).toU1Value = r • a.toU1Value
```

**An instance with no name**, [line 177](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L177).

> The bracket on the gauge algebra, `I` times the matrix commutator on the `su(3)` and `su(2)`
> factors and zero on the commutative `u(1)` factor. The factor of `I` is what makes the
> bracket of two hermitian matrices hermitian again. It is also why the bracket is only
> `ℝ`-bilinear, not `ℂ`-bilinear.

```lean
noncomputable instance : Bracket GaugeAlgebra GaugeAlgebra
```

**`StandardModel.GaugeAlgebra.bracket_toSU3Matrix`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L197).

```lean
lemma bracket_toSU3Matrix (a b : GaugeAlgebra) :
    ⁅a, b⁆.toSU3Matrix =
      Complex.I • (a.toSU3Matrix * b.toSU3Matrix - b.toSU3Matrix * a.toSU3Matrix)
```

**`StandardModel.GaugeAlgebra.bracket_toSU2Matrix`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L202).

```lean
lemma bracket_toSU2Matrix (a b : GaugeAlgebra) :
    ⁅a, b⁆.toSU2Matrix =
      Complex.I • (a.toSU2Matrix * b.toSU2Matrix - b.toSU2Matrix * a.toSU2Matrix)
```

**`StandardModel.GaugeAlgebra.bracket_toU1Value`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L207).

```lean
lemma bracket_toU1Value (a b : GaugeAlgebra) :
    ⁅a, b⁆.toU1Value = 0
```

**An instance with no name**, [line 211](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L211).

> The gauge algebra is a Lie ring under the bracket `i [a, b]`.

```lean
noncomputable instance : LieRing GaugeAlgebra
```

**An instance with no name**, [line 226](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L226).

> The gauge algebra is a real Lie algebra.

```lean
noncomputable instance : LieAlgebra ℝ GaugeAlgebra
```

## D. The adjoint action of the gauge group

**`StandardModel.GaugeAlgebra.conj_mem`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L238).

> The conjugate of a hermitian traceless matrix by a unitary matrix is hermitian and
> traceless.

```lean
lemma conj_mem {n : ℕ} {U A : Matrix (Fin n) (Fin n) ℂ}
    (hU : U ∈ Matrix.unitaryGroup (Fin n) ℂ) (hA : star A = A) (htr : A.trace = 0) :
    star (U * A * star U) = U * A * star U ∧ (U * A * star U).trace = 0
```

**`StandardModel.GaugeAlgebra.adjointMap`**, a def, [line 248](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L248).

> The linear map by which one gauge group element acts on the gauge algebra in the
> adjoint action. It is conjugation by the corresponding unitary on the `su(3)` and `su(2)`
> factors, and the identity on the commutative `u(1)` factor.

```lean
noncomputable def adjointMap (g : GaugeGroupI) : GaugeAlgebra →ₗ[ℝ] GaugeAlgebra
```

**`StandardModel.GaugeAlgebra.adjointMap_toSU3Matrix`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L269).

```lean
lemma adjointMap_toSU3Matrix (g : GaugeGroupI) (a : GaugeAlgebra) :
    (adjointMap g a).toSU3Matrix = g.toSU3.1 * a.toSU3Matrix * star g.toSU3.1
```

**`StandardModel.GaugeAlgebra.adjointMap_toSU2Matrix`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L273).

```lean
lemma adjointMap_toSU2Matrix (g : GaugeGroupI) (a : GaugeAlgebra) :
    (adjointMap g a).toSU2Matrix = g.toSU2.1 * a.toSU2Matrix * star g.toSU2.1
```

**`StandardModel.GaugeAlgebra.adjointMap_toU1Value`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L277).

```lean
lemma adjointMap_toU1Value (g : GaugeGroupI) (a : GaugeAlgebra) :
    (adjointMap g a).toU1Value = a.toU1Value
```

**`StandardModel.GaugeAlgebra.adjoint`**, a def, [line 283](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L283).

> The adjoint action of the gauge group on its gauge algebra. It is conjugation by the
> corresponding unitary on the `su(3)` and `su(2)` factors, and the trivial action on the
> commutative `u(1)` factor.

```lean
noncomputable def adjoint : Representation ℝ GaugeGroupI GaugeAlgebra
```

**`StandardModel.GaugeAlgebra.adjoint_toSU3Matrix`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L312).

```lean
lemma adjoint_toSU3Matrix (g : GaugeGroupI) (a : GaugeAlgebra) :
    (adjoint g a).toSU3Matrix = g.toSU3.1 * a.toSU3Matrix * star g.toSU3.1
```

**`StandardModel.GaugeAlgebra.adjoint_toSU2Matrix`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L316).

```lean
lemma adjoint_toSU2Matrix (g : GaugeGroupI) (a : GaugeAlgebra) :
    (adjoint g a).toSU2Matrix = g.toSU2.1 * a.toSU2Matrix * star g.toSU2.1
```

**`StandardModel.GaugeAlgebra.adjoint_toU1Value`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L320).

```lean
lemma adjoint_toU1Value (g : GaugeGroupI) (a : GaugeAlgebra) :
    (adjoint g a).toU1Value = a.toU1Value
```

## Depends on

- [The Standard Model Gauge Group](../../../../physlib/particles/standardmodel/gaugegroup/basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean)
