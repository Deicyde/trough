---
declaration: module
origin: cited
lean: StandardModel.JetGaugeAlgebra, StandardModel.JetGaugeAlgebra.toSU3Matrix, StandardModel.JetGaugeAlgebra.toSU2Matrix, StandardModel.JetGaugeAlgebra.toU1Value, StandardModel.JetGaugeAlgebra.toVal, StandardModel.JetGaugeAlgebra.toVal_fst, StandardModel.JetGaugeAlgebra.toVal_snd_fst, StandardModel.JetGaugeAlgebra.toVal_snd_snd
statement: formalized
proof: formalized
---

# The jet gauge algebra

The module `PhyslibAlpha.Particles.StandardModel.GaugeAlgebra.JetGaugeAlgebra`, [PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean): 83 declarations (4 instances with no name), 30 with a docstring.

## i. Overview

> We define `JetGaugeAlgebra` as the Lie algebra of `JetGaugeGroupI`,
> defined explicitly as traceless self-adjoint matrices, and giving it an instance `LieAlgebra`.
> This is a matrix Lie algebra, so the bracket is given by the commutator of matrices.
>
> Note here that `JetGaugeAlgebra` is a module over `ℝ` not `ℂ` or `SpaceTimeAlgebra`.
>
> On this Lie algebra define a preferred basis, `basis`, indexed by
> `basisIndex × Multiset (Fin 1 ⊕ Fin 3)`.
> Here `basisIndex` is the sum `Fin 8 ⊕ Fin 3 ⊕ Fin 1`. The first factor
> corresponds to the Gell-Mann matrices which form a basis of `su(3)`,
> the second factor corresponds to the Pauli matrices which form a basis of `su(2)`,
> and the third factor corresponds to the identity matrix which forms a basis of `u(1)`.
>
> We let `structuralConstant` (typically called `f`) be the structure constants of the Lie algebra
> with respect to this preferred basis, so that
> ```
>   [basis i, basis j] = i * ∑ k, structuralConstant i j k • basis k
> ```
>
> On `JetGaugeAlgebra` we define the adjoint representation of `JetGaugeGroupI`,
> `adjointRep`, which acts via `x ↦ g * x * g⁻¹`.
>
> There is also a derivative `deriv : Fin 1 ⊕ Fin 3 → JetLieAlgebra →ₗ[ℝ] JetLieAlgebra`
> whose action can be defined componentwise in terms of the basis.
>
> The derivative acts on brackets via the Leibniz rule:
> ```
>   deriv μ [x, y] = [deriv μ x, y] + [x, deriv μ y]
> ```

## ii. Key results

> - `JetGaugeAlgebra` : the jet gauge algebra: the Lie-algebra analogue of `JetGaugeGroupI`, with one
>   factor per gauge group factor — traceless self-adjoint `3 × 3` and `2 × 2` matrices and a
>   self-adjoint scalar, all with coefficients in the ring `SpaceTimeAlgebra` of formal power series
>   in the spacetime coordinates

## iv. References

> * None.

**`StandardModel.JetGaugeAlgebra`**, an abbrev, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L81).

> The jet gauge algebra: the Lie-algebra analogue of `JetGaugeGroupI`, with one factor per gauge
> group factor — traceless self-adjoint `3 × 3` and `2 × 2` matrices and a self-adjoint scalar, all
> with coefficients in the ring `SpaceTimeAlgebra` of formal power series in the spacetime
> coordinates. The Maurer–Cartan forms of the jet gauge group are valued here, hermiticity being
> `star_maurerCartanSU3` and its companions.

```lean
abbrev JetGaugeAlgebra
```

## A. Basic projections

**`StandardModel.JetGaugeAlgebra.toSU3Matrix`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L97).

> The `su(3)`-factor component of an element of the jet gauge algebra.

```lean
def toSU3Matrix (a : JetGaugeAlgebra) : Matrix (Fin 3) (Fin 3) SpaceTimeAlgebra
```

**`StandardModel.JetGaugeAlgebra.toSU2Matrix`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L100).

> The `su(2)`-factor component of an element of the jet gauge algebra.

```lean
def toSU2Matrix (a : JetGaugeAlgebra) : Matrix (Fin 2) (Fin 2) SpaceTimeAlgebra
```

**`StandardModel.JetGaugeAlgebra.toU1Value`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L103).

> The `u(1)`-factor component of an element of the jet gauge algebra.

```lean
def toU1Value (a : JetGaugeAlgebra) :  SpaceTimeAlgebra
```

**`StandardModel.JetGaugeAlgebra.toVal`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L107).

> The underlying matrix value of an element of the jet gauge algebra, as a
> product of matrices.

```lean
def toVal (a : JetGaugeAlgebra) :
    Matrix (Fin 3) (Fin 3) SpaceTimeAlgebra × Matrix (Fin 2)
        (Fin 2) SpaceTimeAlgebra × SpaceTimeAlgebra
```

**`StandardModel.JetGaugeAlgebra.toVal_fst`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L113).

```lean
lemma toVal_fst (a : JetGaugeAlgebra) : a.toVal.1 = a.toSU3Matrix
```

**`StandardModel.JetGaugeAlgebra.toVal_snd_fst`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L116).

```lean
lemma toVal_snd_fst (a : JetGaugeAlgebra) : a.toVal.2.1 = a.toSU2Matrix
```

**`StandardModel.JetGaugeAlgebra.toVal_snd_snd`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L119).

```lean
lemma toVal_snd_snd (a : JetGaugeAlgebra) : a.toVal.2.2 = a.toU1Value
```

**`StandardModel.JetGaugeAlgebra.ext_of_matrix`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L122).

```lean
lemma ext_of_matrix {a b : JetGaugeAlgebra} (h1 : a.toSU3Matrix = b.toSU3Matrix)
    (h2 : a.toSU2Matrix = b.toSU2Matrix) (h3 : a.toU1Value = b.toU1Value) : a = b
```

## B. Constructor from a product of matrices

**`StandardModel.JetGaugeAlgebra.ofMatrixProd`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L136).

> A jet of the gauge algebra from a triple of matrices of jets: the `SU(3)` and `SU(2)`
> components self-adjoint and traceless, the `U(1)` component self-adjoint.

```lean
def ofMatrixProd (A : Matrix (Fin 3) (Fin 3) SpaceTimeAlgebra ×
    Matrix (Fin 2) (Fin 2) SpaceTimeAlgebra × SpaceTimeAlgebra)
        (hA : star A.1 = A.1 ∧ A.1.trace = 0)
    (hB : star A.2.1 = A.2.1 ∧ A.2.1.trace = 0) (hC : star A.2.2 = A.2.2) : JetGaugeAlgebra
```

**`StandardModel.JetGaugeAlgebra.ofMatrixProd_toSU3Matrix`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L143).

```lean
lemma ofMatrixProd_toSU3Matrix (A : Matrix (Fin 3) (Fin 3) SpaceTimeAlgebra ×
    Matrix (Fin 2) (Fin 2) SpaceTimeAlgebra × SpaceTimeAlgebra)
        (hA : star A.1 = A.1 ∧ A.1.trace = 0)
    (hB : star A.2.1 = A.2.1 ∧ A.2.1.trace = 0) (hC : star A.2.2 = A.2.2) :
    (ofMatrixProd A hA hB hC).toSU3Matrix = A.1
```

**`StandardModel.JetGaugeAlgebra.ofMatrixProd_toSU2Matrix`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L150).

```lean
lemma ofMatrixProd_toSU2Matrix (A : Matrix (Fin 3) (Fin 3) SpaceTimeAlgebra ×
    Matrix (Fin 2) (Fin 2) SpaceTimeAlgebra × SpaceTimeAlgebra)
        (hA : star A.1 = A.1 ∧ A.1.trace = 0)
    (hB : star A.2.1 = A.2.1 ∧ A.2.1.trace = 0) (hC : star A.2.2 = A.2.2) :
    (ofMatrixProd A hA hB hC).toSU2Matrix = A.2.1
```

**`StandardModel.JetGaugeAlgebra.ofMatrixProd_toU1Value`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L157).

```lean
lemma ofMatrixProd_toU1Value (A : Matrix (Fin 3) (Fin 3) SpaceTimeAlgebra ×
    Matrix (Fin 2) (Fin 2) SpaceTimeAlgebra × SpaceTimeAlgebra)
        (hA : star A.1 = A.1 ∧ A.1.trace = 0)
    (hB : star A.2.1 = A.2.1 ∧ A.2.1.trace = 0) (hC : star A.2.2 = A.2.2) :
    (ofMatrixProd A hA hB hC).toU1Value = A.2.2
```

## C. The Lie algebra instance

**`StandardModel.JetGaugeAlgebra.add_toSU3Matrix`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L170).

```lean
lemma add_toSU3Matrix (a b : JetGaugeAlgebra) :
    (a + b).toSU3Matrix = a.toSU3Matrix + b.toSU3Matrix
```

**`StandardModel.JetGaugeAlgebra.add_toSU2Matrix`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L174).

```lean
lemma add_toSU2Matrix (a b : JetGaugeAlgebra) :
    (a + b).toSU2Matrix = a.toSU2Matrix + b.toSU2Matrix
```

**`StandardModel.JetGaugeAlgebra.add_toU1Value`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L178).

```lean
lemma add_toU1Value (a b : JetGaugeAlgebra) :
    (a + b).toU1Value = a.toU1Value + b.toU1Value
```

**`StandardModel.JetGaugeAlgebra.toSU3Matrix_sum`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L181).

```lean
lemma toSU3Matrix_sum {ι : Type*} (t : Finset ι) (f : ι → JetGaugeAlgebra) :
    (∑ i ∈ t, f i).toSU3Matrix = ∑ i ∈ t, (f i).toSU3Matrix
```

**`StandardModel.JetGaugeAlgebra.toSU2Matrix_sum`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L185).

```lean
lemma toSU2Matrix_sum {ι : Type*} (t : Finset ι) (f : ι → JetGaugeAlgebra) :
    (∑ i ∈ t, f i).toSU2Matrix = ∑ i ∈ t, (f i).toSU2Matrix
```

**`StandardModel.JetGaugeAlgebra.toU1Value_sum`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L189).

```lean
lemma toU1Value_sum {ι : Type*} (t : Finset ι) (f : ι → JetGaugeAlgebra) :
    (∑ i ∈ t, f i).toU1Value = ∑ i ∈ t, (f i).toU1Value
```

**`StandardModel.JetGaugeAlgebra.zero_toSU3Matrix`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L194).

```lean
lemma zero_toSU3Matrix : (0 : JetGaugeAlgebra).toSU3Matrix = 0
```

**`StandardModel.JetGaugeAlgebra.zero_toSU2Matrix`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L197).

```lean
lemma zero_toSU2Matrix : (0 : JetGaugeAlgebra).toSU2Matrix = 0
```

**`StandardModel.JetGaugeAlgebra.zero_toU1Value`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L200).

```lean
lemma zero_toU1Value : (0 : JetGaugeAlgebra).toU1Value = 0
```

**`StandardModel.JetGaugeAlgebra.smul_toSU3Matrix`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L203).

```lean
lemma smul_toSU3Matrix (r : ℝ) (a : JetGaugeAlgebra) :
    (r • a).toSU3Matrix = r • a.toSU3Matrix
```

**`StandardModel.JetGaugeAlgebra.smul_toSU2Matrix`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L207).

```lean
lemma smul_toSU2Matrix (r : ℝ) (a : JetGaugeAlgebra) :
    (r • a).toSU2Matrix = r • a.toSU2Matrix
```

**`StandardModel.JetGaugeAlgebra.smul_toU1Value`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L211).

```lean
lemma smul_toU1Value (r : ℝ) (a : JetGaugeAlgebra) :
    (r • a).toU1Value = r • a.toU1Value
```

**`StandardModel.JetGaugeAlgebra.sub_toSU3Matrix`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L215).

```lean
lemma sub_toSU3Matrix (a b : JetGaugeAlgebra) :
    (a - b).toSU3Matrix = a.toSU3Matrix - b.toSU3Matrix
```

**`StandardModel.JetGaugeAlgebra.sub_toSU2Matrix`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L219).

```lean
lemma sub_toSU2Matrix (a b : JetGaugeAlgebra) :
    (a - b).toSU2Matrix = a.toSU2Matrix - b.toSU2Matrix
```

**`StandardModel.JetGaugeAlgebra.sub_toU1Value`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L223).

```lean
lemma sub_toU1Value (a b : JetGaugeAlgebra) :
    (a - b).toU1Value = a.toU1Value - b.toU1Value
```

**An instance with no name**, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L230).

> The bracket on the jet gauge algebra: `I` times the matrix commutator on the
> `su(3)` and `su(2)` factors, and zero on the (commutative) `u(1)` factor. The
> factor of `I` is what makes the bracket of two hermitian matrices hermitian
> again; it is also why the bracket is only `ℝ`-bilinear, not `ℂ`-bilinear.

```lean
noncomputable instance : Bracket JetGaugeAlgebra JetGaugeAlgebra
```

**`StandardModel.JetGaugeAlgebra.bracket_toSU3Matrix`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L250).

```lean
lemma bracket_toSU3Matrix (a b : JetGaugeAlgebra) :
    ⁅a, b⁆.toSU3Matrix =
      Complex.I • (a.toSU3Matrix * b.toSU3Matrix - b.toSU3Matrix * a.toSU3Matrix)
```

**`StandardModel.JetGaugeAlgebra.bracket_toSU2Matrix`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L255).

```lean
lemma bracket_toSU2Matrix (a b : JetGaugeAlgebra) :
    ⁅a, b⁆.toSU2Matrix =
      Complex.I • (a.toSU2Matrix * b.toSU2Matrix - b.toSU2Matrix * a.toSU2Matrix)
```

**`StandardModel.JetGaugeAlgebra.bracket_toU1Value`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L260).

```lean
lemma bracket_toU1Value (a b : JetGaugeAlgebra) :
    ⁅a, b⁆.toU1Value = 0
```

**An instance with no name**, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L263).

```lean
noncomputable instance : LieRing JetGaugeAlgebra
```

**An instance with no name**, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L277).

```lean
noncomputable instance : LieAlgebra ℝ JetGaugeAlgebra
```

## D. The derivative on the jet gauge algebra

**`StandardModel.JetGaugeAlgebra.deriv`**, a def, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L290).

> The formal derivative in the direction `μ` on the jet gauge algebra, acting
> entrywise on each factor. It preserves hermiticity since `star` commutes with
> `pderiv`, and tracelessness since the trace of the entrywise derivative is the
> derivative of the trace.

```lean
noncomputable def deriv (μ : Fin 1 ⊕ Fin 3) : JetGaugeAlgebra →ₗ[ℝ] JetGaugeAlgebra
```

**`StandardModel.JetGaugeAlgebra.deriv_toSU3Matrix`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L322).

```lean
lemma deriv_toSU3Matrix (μ : Fin 1 ⊕ Fin 3) (a : JetGaugeAlgebra) :
    (deriv μ a).toSU3Matrix = a.toSU3Matrix.map (pderiv μ)
```

**`StandardModel.JetGaugeAlgebra.deriv_toSU2Matrix`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L326).

```lean
lemma deriv_toSU2Matrix (μ : Fin 1 ⊕ Fin 3) (a : JetGaugeAlgebra) :
    (deriv μ a).toSU2Matrix = a.toSU2Matrix.map (pderiv μ)
```

**`StandardModel.JetGaugeAlgebra.deriv_toU1Value`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L330).

```lean
lemma deriv_toU1Value (μ : Fin 1 ⊕ Fin 3) (a : JetGaugeAlgebra) :
    (deriv μ a).toU1Value = pderiv μ a.toU1Value
```

## E. Multiplication by the coordinates

**`StandardModel.JetGaugeAlgebra.coord`**, a def, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L342).

> Multiplication by the spacetime coordinate `x_μ`, entrywise on each factor. It
> preserves hermiticity since the coordinates are self-adjoint, and tracelessness since
> it is a scalar.

```lean
noncomputable def coord (μ : Fin 1 ⊕ Fin 3) : JetGaugeAlgebra →ₗ[ℝ] JetGaugeAlgebra
```

**`StandardModel.JetGaugeAlgebra.coord_toSU3Matrix`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L362).

```lean
lemma coord_toSU3Matrix (μ : Fin 1 ⊕ Fin 3) (a : JetGaugeAlgebra) :
    (coord μ a).toSU3Matrix = (X μ : SpaceTimeAlgebra) • a.toSU3Matrix
```

**`StandardModel.JetGaugeAlgebra.coord_toSU2Matrix`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L366).

```lean
lemma coord_toSU2Matrix (μ : Fin 1 ⊕ Fin 3) (a : JetGaugeAlgebra) :
    (coord μ a).toSU2Matrix = (X μ : SpaceTimeAlgebra) • a.toSU2Matrix
```

**`StandardModel.JetGaugeAlgebra.coord_toU1Value`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L370).

```lean
lemma coord_toU1Value (μ : Fin 1 ⊕ Fin 3) (a : JetGaugeAlgebra) :
    (coord μ a).toU1Value = (X μ : SpaceTimeAlgebra) * a.toU1Value
```

**`StandardModel.JetGaugeAlgebra.deriv_coord`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L374).

> The Leibniz rule for a coordinate: `∂_μ (x_ν a) = x_ν ∂_μ a + δ_{μν} a`.

```lean
lemma deriv_coord (μ ν : Fin 1 ⊕ Fin 3) (a : JetGaugeAlgebra) :
    deriv μ (coord ν a) = coord ν (deriv μ a) + if μ = ν then a else 0
```

**`StandardModel.JetGaugeAlgebra.coord_lie`**, a lemma, [line 403](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L403).

> The coordinates are central for the bracket.

```lean
lemma coord_lie (μ : Fin 1 ⊕ Fin 3) (a b : JetGaugeAlgebra) :
    ⁅coord μ a, b⁆ = coord μ ⁅a, b⁆
```

**`StandardModel.JetGaugeAlgebra.deriv_comm`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L411).

> Formal derivatives on the jet gauge algebra commute.

```lean
lemma deriv_comm (μ ν : Fin 1 ⊕ Fin 3) (a : JetGaugeAlgebra) :
    deriv μ (deriv ν a) = deriv ν (deriv μ a)
```

**`StandardModel.JetGaugeAlgebra.deriv_bracket`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L422).

> The derivative is a derivation of the bracket: the Leibniz rule
> `deriv μ ⁅x, y⁆ = ⁅deriv μ x, y⁆ + ⁅x, deriv μ y⁆`.

```lean
lemma deriv_bracket (μ : Fin 1 ⊕ Fin 3) (x y : JetGaugeAlgebra) :
    deriv μ ⁅x, y⁆ = ⁅deriv μ x, y⁆ + ⁅x, deriv μ y⁆
```

## F. The iterated derivative

**An instance with no name**, [line 458](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L458).

> Post-composition with `deriv` is right-commutative, since formal derivatives
> commute (`deriv_comm`). This is what allows iterated derivatives to be indexed by a
> `Multiset` of directions.

```lean
instance : RightCommutative
    (fun (D : JetGaugeAlgebra →ₗ[ℝ] JetGaugeAlgebra) (μ : Fin 1 ⊕ Fin 3) => D.comp (deriv μ))
```

**`StandardModel.JetGaugeAlgebra.iteratedDeriv`**, a def, [line 466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L466).

> The iterated formal derivative on the jet gauge algebra, in the (unordered, since
> derivatives commute) directions given by the multiset `μs`.

```lean
noncomputable def iteratedDeriv (μs : Multiset (Fin 1 ⊕ Fin 3)) :
    JetGaugeAlgebra →ₗ[ℝ] JetGaugeAlgebra
```

**`StandardModel.JetGaugeAlgebra.iteratedDeriv_zero`**, a lemma, [line 471](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L471).

```lean
lemma iteratedDeriv_zero : iteratedDeriv 0 = LinearMap.id
```

**`StandardModel.JetGaugeAlgebra.iteratedDeriv_cons`**, a lemma, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L474).

```lean
lemma iteratedDeriv_cons (μ : Fin 1 ⊕ Fin 3) (μs : Multiset (Fin 1 ⊕ Fin 3)) :
    iteratedDeriv (μ ::ₘ μs) = (deriv μ).comp (iteratedDeriv μs)
```

**`StandardModel.JetGaugeAlgebra.iteratedDeriv_add`**, a lemma, [line 490](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L490).

> The iterated derivative is additive in the multiset of directions: deriving
> along `s + t` is deriving along `t` and then along `s`.

```lean
lemma iteratedDeriv_add (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    iteratedDeriv (s + t) = (iteratedDeriv s).comp (iteratedDeriv t)
```

**`StandardModel.JetGaugeAlgebra.iteratedDeriv_singleton`**, a lemma, [line 499](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L499).

```lean
lemma iteratedDeriv_singleton (μ : Fin 1 ⊕ Fin 3) :
    iteratedDeriv ({μ} : Multiset (Fin 1 ⊕ Fin 3)) = deriv μ
```

**`StandardModel.JetGaugeAlgebra.iteratedDeriv_toSU3Matrix`**, a lemma, [line 504](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L504).

```lean
lemma iteratedDeriv_toSU3Matrix (s : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra) :
    (iteratedDeriv s a).toSU3Matrix =
      a.toSU3Matrix.map fun f => SpaceTimeAlgebra.iteratedPDeriv s f
```

**`StandardModel.JetGaugeAlgebra.iteratedDeriv_toSU2Matrix`**, a lemma, [line 515](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L515).

```lean
lemma iteratedDeriv_toSU2Matrix (s : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra) :
    (iteratedDeriv s a).toSU2Matrix =
      a.toSU2Matrix.map fun f => SpaceTimeAlgebra.iteratedPDeriv s f
```

**`StandardModel.JetGaugeAlgebra.iteratedDeriv_toU1Value`**, a lemma, [line 526](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L526).

```lean
lemma iteratedDeriv_toU1Value (s : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra) :
    (iteratedDeriv s a).toU1Value = SpaceTimeAlgebra.iteratedPDeriv s a.toU1Value
```

## G. Taylor coefficients and evaluation at the base point

**`StandardModel.JetGaugeAlgebra.taylorCoeff`**, a def, [line 548](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L548).

> The Taylor coefficient of an element of the jet gauge algebra at the monomial
> given by the multiset `r` of spacetime directions, taken entrywise, as an
> `ℝ`-linear map to the constant gauge algebra `GaugeAlgebra`.
>
> For `r ≠ 0` this is only linear: the coefficient of a product is a convolution of
> coefficients, so it does not respect the bracket. The zeroth coefficient does; see
> `eval` for that morphism of Lie algebras.

```lean
noncomputable def taylorCoeff (r : Multiset (Fin 1 ⊕ Fin 3)) :
    JetGaugeAlgebra →ₗ[ℝ] GaugeAlgebra
```

**`StandardModel.JetGaugeAlgebra.taylorCoeff_toSU3Matrix`**, a lemma, [line 583](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L583).

```lean
lemma taylorCoeff_toSU3Matrix (r : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra) :
    (taylorCoeff r a).toSU3Matrix = a.toSU3Matrix.map (coeff r.toFinsupp)
```

**`StandardModel.JetGaugeAlgebra.taylorCoeff_toSU2Matrix`**, a lemma, [line 587](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L587).

```lean
lemma taylorCoeff_toSU2Matrix (r : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra) :
    (taylorCoeff r a).toSU2Matrix = a.toSU2Matrix.map (coeff r.toFinsupp)
```

**`StandardModel.JetGaugeAlgebra.taylorCoeff_toU1Value`**, a lemma, [line 591](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L591).

```lean
lemma taylorCoeff_toU1Value (r : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra) :
    (taylorCoeff r a).toU1Value = coeff r.toFinsupp a.toU1Value
```

**`StandardModel.JetGaugeAlgebra.taylorCoeff_zero_bracket`**, a lemma, [line 596](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L596).

> The zeroth Taylor coefficient respects the bracket, since the constant coefficient
> of a product of jets is the product of the constant coefficients.

```lean
lemma taylorCoeff_zero_bracket (a b : JetGaugeAlgebra) :
    taylorCoeff 0 ⁅a, b⁆ = ⁅taylorCoeff 0 a, taylorCoeff 0 b⁆
```

**`StandardModel.JetGaugeAlgebra.eval`**, a def, [line 609](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L609).

> Evaluation of the jet gauge algebra at the base point: the zeroth Taylor
> coefficient, as a morphism of Lie algebras.

```lean
noncomputable def eval : JetGaugeAlgebra →ₗ⁅ℝ⁆ GaugeAlgebra
```

**`StandardModel.JetGaugeAlgebra.ofConstant`**, a def, [line 615](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L615).

> The inclusion of the constant gauge algebra into the jet gauge algebra: the jets
> with no spacetime dependence, given entrywise by the constant power series. This is
> a section of `eval`.

```lean
noncomputable def ofConstant : GaugeAlgebra →ₗ[ℝ] JetGaugeAlgebra
```

**`StandardModel.JetGaugeAlgebra.ofConstant_toSU3Matrix`**, a lemma, [line 651](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L651).

```lean
lemma ofConstant_toSU3Matrix (a : GaugeAlgebra) :
    (ofConstant a).toSU3Matrix = a.toSU3Matrix.map (C : ℂ → SpaceTimeAlgebra)
```

**`StandardModel.JetGaugeAlgebra.ofConstant_toSU2Matrix`**, a lemma, [line 655](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L655).

```lean
lemma ofConstant_toSU2Matrix (a : GaugeAlgebra) :
    (ofConstant a).toSU2Matrix = a.toSU2Matrix.map (C : ℂ → SpaceTimeAlgebra)
```

**`StandardModel.JetGaugeAlgebra.ofConstant_toU1Value`**, a lemma, [line 659](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L659).

```lean
lemma ofConstant_toU1Value (a : GaugeAlgebra) :
    (ofConstant a).toU1Value = C a.toU1Value
```

**`StandardModel.JetGaugeAlgebra.eval_apply`**, a lemma, [line 662](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L662).

```lean
lemma eval_apply (a : JetGaugeAlgebra) : eval a = taylorCoeff 0 a
```

**`StandardModel.JetGaugeAlgebra.eval_ofConstant`**, a lemma, [line 665](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L665).

```lean
lemma eval_ofConstant (a : GaugeAlgebra) : eval (ofConstant a) = a
```

**`StandardModel.JetGaugeAlgebra.eval_toSU3Matrix_apply`**, a lemma, [line 674](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L674).

```lean
lemma eval_toSU3Matrix_apply (a : JetGaugeAlgebra) (i j : Fin 3) :
    (eval a).toSU3Matrix i j = constantCoeff (a.toSU3Matrix i j)
```

**`StandardModel.JetGaugeAlgebra.eval_toSU2Matrix_apply`**, a lemma, [line 680](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L680).

```lean
lemma eval_toSU2Matrix_apply (a : JetGaugeAlgebra) (i j : Fin 2) :
    (eval a).toSU2Matrix i j = constantCoeff (a.toSU2Matrix i j)
```

**`StandardModel.JetGaugeAlgebra.eval_toU1Value_eq`**, a lemma, [line 686](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L686).

```lean
lemma eval_toU1Value_eq (a : JetGaugeAlgebra) :
    (eval a).toU1Value = constantCoeff a.toU1Value
```

**`StandardModel.JetGaugeAlgebra.eval_coord`**, a lemma, [line 693](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L693).

> A coordinate multiple vanishes at the base point.

```lean
lemma eval_coord (μ : Fin 1 ⊕ Fin 3) (a : JetGaugeAlgebra) : eval (coord μ a) = 0
```

**`StandardModel.JetGaugeAlgebra.eval_iteratedDeriv_toSU3Matrix`**, a lemma, [line 702](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L702).

> The `su(3)` component of the base-point Taylor coefficients.

```lean
lemma eval_iteratedDeriv_toSU3Matrix (x : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra) :
    (eval (iteratedDeriv x a)).toSU3Matrix
      = a.toSU3Matrix.map fun f => constantCoeff (SpaceTimeAlgebra.iteratedPDeriv x f)
```

**`StandardModel.JetGaugeAlgebra.eval_iteratedDeriv_toSU2Matrix`**, a lemma, [line 709](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L709).

> The `su(2)` component of the base-point Taylor coefficients.

```lean
lemma eval_iteratedDeriv_toSU2Matrix (x : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra) :
    (eval (iteratedDeriv x a)).toSU2Matrix
      = a.toSU2Matrix.map fun f => constantCoeff (SpaceTimeAlgebra.iteratedPDeriv x f)
```

**`StandardModel.JetGaugeAlgebra.eval_iteratedDeriv_toU1Value`**, a lemma, [line 716](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L716).

> The `u(1)` component of the base-point Taylor coefficients.

```lean
lemma eval_iteratedDeriv_toU1Value (x : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra) :
    (eval (iteratedDeriv x a)).toU1Value
      = constantCoeff (SpaceTimeAlgebra.iteratedPDeriv x a.toU1Value)
```

**`StandardModel.JetGaugeAlgebra.ext_of_eval_iteratedDeriv`**, a lemma, [line 724](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L724).

> Taylor determinacy: a jet gauge algebra element is determined by the base-point
> values of its iterated derivatives.

```lean
lemma ext_of_eval_iteratedDeriv {x y : JetGaugeAlgebra}
    (h : ∀ s, eval (iteratedDeriv s x) = eval (iteratedDeriv s y)) : x = y
```

## H. The basis

## I. The adjoint representation of Jet Gauge group

**`StandardModel.JetGaugeAlgebra.adjointMap`**, a def, [line 811](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L811).

> The adjoint action of an element `U` of the jet gauge group on the jet gauge algebra,
> acting on the `su(3)` and `su(2)` factors by `a ↦ U a U⁻¹`, with `U⁻¹ = star U` by
> unitarity, and trivially on the `u(1)` factor since `SpaceTimeAlgebra` is commutative.
> Hermiticity is preserved since `star (U a (star U)) = U (star a) (star U)`, and
> tracelessness since the trace is invariant under conjugation.

```lean
noncomputable def adjointMap (U : JetGaugeGroupI) : JetGaugeAlgebra →ₗ[ℝ] JetGaugeAlgebra
```

**`StandardModel.JetGaugeAlgebra.adjointMap_toSU3Matrix`**, a lemma, [line 840](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L840).

```lean
lemma adjointMap_toSU3Matrix (U : JetGaugeGroupI) (a : JetGaugeAlgebra) :
    (adjointMap U a).toSU3Matrix = U.1.1 * a.toSU3Matrix * star U.1.1
```

**`StandardModel.JetGaugeAlgebra.adjointMap_toSU2Matrix`**, a lemma, [line 844](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L844).

```lean
lemma adjointMap_toSU2Matrix (U : JetGaugeGroupI) (a : JetGaugeAlgebra) :
    (adjointMap U a).toSU2Matrix = U.2.1.1 * a.toSU2Matrix * star U.2.1.1
```

**`StandardModel.JetGaugeAlgebra.adjointMap_toU1Value`**, a lemma, [line 848](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L848).

```lean
lemma adjointMap_toU1Value (U : JetGaugeGroupI) (a : JetGaugeAlgebra) :
    (adjointMap U a).toU1Value = a.toU1Value
```

**`StandardModel.JetGaugeAlgebra.adjoint`**, a def, [line 853](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L853).

> The adjoint representation of the jet gauge group on the jet gauge algebra,
> `U ↦ (a ↦ U a U⁻¹)` factorwise.

```lean
noncomputable def adjoint : Representation ℝ JetGaugeGroupI JetGaugeAlgebra
```

**`StandardModel.JetGaugeAlgebra.eval_adjointMap`**, a lemma, [line 864](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L864).

> At the base point the adjoint action of a gauge jet is the adjoint action of its
> value: the constant coefficient of `U x U†` is `U₀ x₀ U₀†`.

```lean
lemma eval_adjointMap (U : JetGaugeGroupI) (x : JetGaugeAlgebra) :
    eval (adjointMap U x) = GaugeAlgebra.adjoint U.eval (eval x)
```

**`StandardModel.JetGaugeAlgebra.ofConstant_lie`**, a lemma, [line 886](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L886).

> The constant inclusion is a morphism of Lie algebras: constants bracket to
> constants.

```lean
lemma ofConstant_lie (a b : GaugeAlgebra) :
    ofConstant ⁅a, b⁆ = ⁅ofConstant a, ofConstant b⁆
```

**`StandardModel.JetGaugeAlgebra.adjointMap_lie`**, a lemma, [line 899](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean#L899).

> The adjoint action preserves the bracket: conjugation is an automorphism of the
> Lie algebra, using unitarity to cancel the inner `U† U` factors.

```lean
lemma adjointMap_lie (U : JetGaugeGroupI) (x y : JetGaugeAlgebra) :
    adjointMap U ⁅x, y⁆ = ⁅adjointMap U x, adjointMap U y⁆
```

## Depends on

- [The gauge algebra of the Standard Model](../part-03/gaugealgebra-basic.md)
- [The jet gauge group](gaugegroup-jetgaugegroup-basic.md)

## Proof depends on

- [Matrices over the jet ring](../../../spaceandtime/spacetime/spacetimealgebra-matrix.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/JetGaugeAlgebra.lean)
