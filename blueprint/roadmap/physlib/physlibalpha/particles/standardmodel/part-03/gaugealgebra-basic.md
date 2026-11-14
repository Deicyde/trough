---
declaration: module
origin: cited
lean: StandardModel.GaugeAlgebra, StandardModel.GaugeAlgebra.toSU3Matrix, StandardModel.GaugeAlgebra.toSU2Matrix, StandardModel.GaugeAlgebra.toU1Value, StandardModel.GaugeAlgebra.ext_of_matrix, StandardModel.GaugeAlgebra.ofMatrixProd, StandardModel.GaugeAlgebra.ofMatrixProd_toSU3Matrix, StandardModel.GaugeAlgebra.ofMatrixProd_toSU2Matrix
statement: formalized
proof: formalized
---

# The gauge algebra of the Standard Model

The module `PhyslibAlpha.Particles.StandardModel.GaugeAlgebra.Basic`, [PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean): 35 declarations (5 instances with no name), 10 with a docstring.

## i. Overview

> The gauge algebra of the Standard Model is the Lie algebra of
> `GaugeGroupI`, which is the direct sum of the Lie algebras of `SU(3)`, `SU(2)` and `U(1)`.
> This is a matrix Lie algebra, so the bracket is given by the commutator of matrices.

## ii. Key results

> - `GaugeAlgebra` : the gauge algebra of the Standard Model: the Lie algebra of `GaugeGroupI`, with
>   one factor per gauge group factor — traceless self-adjoint `3 × 3` and `2 × 2` complex matrices
>   and a self-adjoint (i
> - `toSU3Matrix` : the `su(3)`-factor component of an element of the gauge algebra
> - `toSU2Matrix` : the `su(2)`-factor component of an element of the gauge algebra
> - `toU1Value` : the `u(1)`-factor component of an element of the gauge algebra

## iv. References

> * None.

**`StandardModel.GaugeAlgebra`**, an abbrev, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L54).

> The gauge algebra of the Standard Model: the Lie algebra of `GaugeGroupI`, with one
> factor per gauge group factor — traceless self-adjoint `3 × 3` and `2 × 2` complex
> matrices and a self-adjoint (i.e. real) scalar. This is the constant-coefficient
> analogue of `JetGaugeAlgebra`, and the value at the base point of the jets it contains.

```lean
abbrev GaugeAlgebra
```

**An instance with no name**, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L63).

> The self-adjoint scalars form a finite-dimensional real vector space, through the
> identification with the corresponding submodule.

```lean
instance : Module.Finite ℝ (selfAdjoint ℂ)
```

**An instance with no name**, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L66).

```lean
instance : Module.Finite ℝ GaugeAlgebra
```

## A. Basic projections

**`StandardModel.GaugeAlgebra.toSU3Matrix`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L77).

> The `su(3)`-factor component of an element of the gauge algebra.

```lean
def toSU3Matrix (a : GaugeAlgebra) : Matrix (Fin 3) (Fin 3) ℂ
```

**`StandardModel.GaugeAlgebra.toSU2Matrix`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L80).

> The `su(2)`-factor component of an element of the gauge algebra.

```lean
def toSU2Matrix (a : GaugeAlgebra) : Matrix (Fin 2) (Fin 2) ℂ
```

**`StandardModel.GaugeAlgebra.toU1Value`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L83).

> The `u(1)`-factor component of an element of the gauge algebra.

```lean
def toU1Value (a : GaugeAlgebra) : ℂ
```

**`StandardModel.GaugeAlgebra.ext_of_matrix`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L86).

```lean
lemma ext_of_matrix {a b : GaugeAlgebra} (h1 : a.toSU3Matrix = b.toSU3Matrix)
    (h2 : a.toSU2Matrix = b.toSU2Matrix) (h3 : a.toU1Value = b.toU1Value) : a = b
```

## B. Constructor from a product of matrices

**`StandardModel.GaugeAlgebra.ofMatrixProd`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L100).

> The element of the gauge algebra constructed from a triple of matrices satisfying
> the relevant hermiticity and tracelessness conditions.

```lean
def ofMatrixProd (A : Matrix (Fin 3) (Fin 3) ℂ ×
    Matrix (Fin 2) (Fin 2) ℂ × ℂ) (hA : star A.1 = A.1 ∧ A.1.trace = 0)
    (hB : star A.2.1 = A.2.1 ∧ A.2.1.trace = 0) (hC : star A.2.2 = A.2.2) : GaugeAlgebra
```

**`StandardModel.GaugeAlgebra.ofMatrixProd_toSU3Matrix`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L106).

```lean
lemma ofMatrixProd_toSU3Matrix (A : Matrix (Fin 3) (Fin 3) ℂ ×
    Matrix (Fin 2) (Fin 2) ℂ × ℂ) (hA : star A.1 = A.1 ∧ A.1.trace = 0)
    (hB : star A.2.1 = A.2.1 ∧ A.2.1.trace = 0) (hC : star A.2.2 = A.2.2) :
    (ofMatrixProd A hA hB hC).toSU3Matrix = A.1
```

**`StandardModel.GaugeAlgebra.ofMatrixProd_toSU2Matrix`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L112).

```lean
lemma ofMatrixProd_toSU2Matrix (A : Matrix (Fin 3) (Fin 3) ℂ ×
    Matrix (Fin 2) (Fin 2) ℂ × ℂ) (hA : star A.1 = A.1 ∧ A.1.trace = 0)
    (hB : star A.2.1 = A.2.1 ∧ A.2.1.trace = 0) (hC : star A.2.2 = A.2.2) :
    (ofMatrixProd A hA hB hC).toSU2Matrix = A.2.1
```

**`StandardModel.GaugeAlgebra.ofMatrixProd_toU1Value`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L118).

```lean
lemma ofMatrixProd_toU1Value (A : Matrix (Fin 3) (Fin 3) ℂ ×
    Matrix (Fin 2) (Fin 2) ℂ × ℂ) (hA : star A.1 = A.1 ∧ A.1.trace = 0)
    (hB : star A.2.1 = A.2.1 ∧ A.2.1.trace = 0) (hC : star A.2.2 = A.2.2) :
    (ofMatrixProd A hA hB hC).toU1Value = A.2.2
```

## C. The Lie algebra instance

**`StandardModel.GaugeAlgebra.add_toSU3Matrix`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L130).

```lean
lemma add_toSU3Matrix (a b : GaugeAlgebra) :
    (a + b).toSU3Matrix = a.toSU3Matrix + b.toSU3Matrix
```

**`StandardModel.GaugeAlgebra.add_toSU2Matrix`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L134).

```lean
lemma add_toSU2Matrix (a b : GaugeAlgebra) :
    (a + b).toSU2Matrix = a.toSU2Matrix + b.toSU2Matrix
```

**`StandardModel.GaugeAlgebra.add_toU1Value`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L138).

```lean
lemma add_toU1Value (a b : GaugeAlgebra) :
    (a + b).toU1Value = a.toU1Value + b.toU1Value
```

**`StandardModel.GaugeAlgebra.zero_toSU3Matrix`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L142).

```lean
lemma zero_toSU3Matrix : (0 : GaugeAlgebra).toSU3Matrix = 0
```

**`StandardModel.GaugeAlgebra.zero_toSU2Matrix`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L145).

```lean
lemma zero_toSU2Matrix : (0 : GaugeAlgebra).toSU2Matrix = 0
```

**`StandardModel.GaugeAlgebra.zero_toU1Value`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L148).

```lean
lemma zero_toU1Value : (0 : GaugeAlgebra).toU1Value = 0
```

**`StandardModel.GaugeAlgebra.smul_toSU3Matrix`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L151).

```lean
lemma smul_toSU3Matrix (r : ℝ) (a : GaugeAlgebra) :
    (r • a).toSU3Matrix = r • a.toSU3Matrix
```

**`StandardModel.GaugeAlgebra.smul_toSU2Matrix`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L155).

```lean
lemma smul_toSU2Matrix (r : ℝ) (a : GaugeAlgebra) :
    (r • a).toSU2Matrix = r • a.toSU2Matrix
```

**`StandardModel.GaugeAlgebra.smul_toU1Value`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L159).

```lean
lemma smul_toU1Value (r : ℝ) (a : GaugeAlgebra) :
    (r • a).toU1Value = r • a.toU1Value
```

**An instance with no name**, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L166).

> The bracket on the gauge algebra: `I` times the matrix commutator on the
> `su(3)` and `su(2)` factors, and zero on the (commutative) `u(1)` factor. The
> factor of `I` is what makes the bracket of two hermitian matrices hermitian
> again; it is also why the bracket is only `ℝ`-bilinear, not `ℂ`-bilinear.

```lean
noncomputable instance : Bracket GaugeAlgebra GaugeAlgebra
```

**`StandardModel.GaugeAlgebra.bracket_toSU3Matrix`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L186).

```lean
lemma bracket_toSU3Matrix (a b : GaugeAlgebra) :
    ⁅a, b⁆.toSU3Matrix =
      Complex.I • (a.toSU3Matrix * b.toSU3Matrix - b.toSU3Matrix * a.toSU3Matrix)
```

**`StandardModel.GaugeAlgebra.bracket_toSU2Matrix`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L191).

```lean
lemma bracket_toSU2Matrix (a b : GaugeAlgebra) :
    ⁅a, b⁆.toSU2Matrix =
      Complex.I • (a.toSU2Matrix * b.toSU2Matrix - b.toSU2Matrix * a.toSU2Matrix)
```

**`StandardModel.GaugeAlgebra.bracket_toU1Value`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L196).

```lean
lemma bracket_toU1Value (a b : GaugeAlgebra) :
    ⁅a, b⁆.toU1Value = 0
```

**An instance with no name**, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L199).

```lean
noncomputable instance : LieRing GaugeAlgebra
```

**An instance with no name**, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L213).

```lean
noncomputable instance : LieAlgebra ℝ GaugeAlgebra
```

## D. The adjoint action of the global gauge group

**`StandardModel.GaugeAlgebra.conj_mem`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L225).

> The conjugate of a hermitian traceless matrix by a unitary matrix is hermitian and
> traceless.

```lean
lemma conj_mem {n : ℕ} {U A : Matrix (Fin n) (Fin n) ℂ}
    (hU : U ∈ Matrix.unitaryGroup (Fin n) ℂ) (hA : star A = A) (htr : A.trace = 0) :
    star (U * A * star U) = U * A * star U ∧ (U * A * star U).trace = 0
```

**`StandardModel.GaugeAlgebra.adjointMap`**, a def, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L235).

> The linear map by which one gauge group element acts on the gauge algebra in the
> adjoint action: conjugation by the corresponding unitary on the `su(3)` and `su(2)`
> factors, and the identity on the commutative `u(1)` factor.

```lean
noncomputable def adjointMap (g : GaugeGroupI) : GaugeAlgebra →ₗ[ℝ] GaugeAlgebra
```

**`StandardModel.GaugeAlgebra.adjointMap_toSU3Matrix`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L256).

```lean
lemma adjointMap_toSU3Matrix (g : GaugeGroupI) (a : GaugeAlgebra) :
    (adjointMap g a).toSU3Matrix = g.toSU3.1 * a.toSU3Matrix * star g.toSU3.1
```

**`StandardModel.GaugeAlgebra.adjointMap_toSU2Matrix`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L260).

```lean
lemma adjointMap_toSU2Matrix (g : GaugeGroupI) (a : GaugeAlgebra) :
    (adjointMap g a).toSU2Matrix = g.toSU2.1 * a.toSU2Matrix * star g.toSU2.1
```

**`StandardModel.GaugeAlgebra.adjointMap_toU1Value`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L264).

```lean
lemma adjointMap_toU1Value (g : GaugeGroupI) (a : GaugeAlgebra) :
    (adjointMap g a).toU1Value = a.toU1Value
```

**`StandardModel.GaugeAlgebra.adjoint`**, a def, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L270).

> **The adjoint action of the global gauge group on its gauge algebra**: conjugation by
> the corresponding unitary on the `su(3)` and `su(2)` factors, and the trivial action on
> the commutative `u(1)` factor.

```lean
noncomputable def adjoint : Representation ℝ GaugeGroupI GaugeAlgebra
```

**`StandardModel.GaugeAlgebra.adjoint_toSU3Matrix`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L299).

```lean
lemma adjoint_toSU3Matrix (g : GaugeGroupI) (a : GaugeAlgebra) :
    (adjoint g a).toSU3Matrix = g.toSU3.1 * a.toSU3Matrix * star g.toSU3.1
```

**`StandardModel.GaugeAlgebra.adjoint_toSU2Matrix`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L303).

```lean
lemma adjoint_toSU2Matrix (g : GaugeGroupI) (a : GaugeAlgebra) :
    (adjoint g a).toSU2Matrix = g.toSU2.1 * a.toSU2Matrix * star g.toSU2.1
```

**`StandardModel.GaugeAlgebra.adjoint_toU1Value`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean#L307).

```lean
lemma adjoint_toU1Value (g : GaugeGroupI) (a : GaugeAlgebra) :
    (adjoint g a).toU1Value = a.toU1Value
```

## Depends on

- [The Standard Model Gauge Group](../../../../physlib/particles/standardmodel/gaugegroup/basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basic.lean)
