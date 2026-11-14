---
declaration: module
origin: cited
lean: ProbabilisticTheory.JordanAlgebra.IsJordanProjection.peirce_polynomial, ProbabilisticTheory.JordanAlgebra.IsJordanProjection.peirceOne, ProbabilisticTheory.JordanAlgebra.IsJordanProjection.mem_peirceOne_iff, ProbabilisticTheory.JordanAlgebra.IsJordanProjection.peirceZero, ProbabilisticTheory.JordanAlgebra.IsJordanProjection.mem_peirceZero_iff, ProbabilisticTheory.JordanAlgebra.IsJordanProjection.peirceHalf, ProbabilisticTheory.JordanAlgebra.IsJordanProjection.mem_peirceHalf_iff, ProbabilisticTheory.JordanAlgebra.IsJordanProjection.disjoint_peirceZero_peirceHalf
statement: formalized
proof: formalized
---

# Peirce decomposition

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Quadratic.Projection`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean): 26 declarations, 26 with a docstring.

> The Peirce decomposition for a Jordan projection `p`; `U_p` projects onto the `1`-component.

## i. Overview

> For a Jordan projection `p` every observable splits into the Peirce components where `L_p` acts by
> `1`, `½` and `0`. The quadratic representation `U_p` is the idempotent projection onto the
> `1`-component.

## ii. Key results

> - `JordanAlgebra.IsJordanProjection.peirceOne` : the `1`-component.
> - `JordanAlgebra.IsJordanProjection.peirce_decomposition` : the Peirce decomposition.
> - `JordanAlgebra.IsJordanProjection.quadRep_range_eq_peirceOne` : `U_p` projects onto the
>   `1`-component.
> - `JordanAlgebra.IsJordanProjection.quadRep_comp_self` : `U_p` is idempotent.

## iv. References

> * None.

## A. The Peirce polynomial

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.peirce_polynomial`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L57).

> If `p` is idempotent, multiplication by `p` obeys the Peirce polynomial
> `2 L_p^3 - 3 L_p^2 + L_p = 0`.  This is a specialization of the polarized Jordan identity and
> is the exact algebraic fact needed to make `U_p` an idempotent compression.

```lean
lemma IsJordanProjection.peirce_polynomial [IsCommJordan E] {p : E}
    (hp : IsJordanProjection p) (x : E) :
    (2 : ℝ) • (p * (p * (p * x))) - (3 : ℝ) • (p * (p * x)) + p * x = 0
```

## B. The Peirce-`1` compression

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.peirceOne`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L75).

> The Peirce-`1` eigenspace of a Jordan projection: the fixed submodule of multiplication by
> `p`.  This is purely algebraic; no order or norm structure is involved.

```lean
def IsJordanProjection.peirceOne [SMulCommClass ℝ E E] (p : E) : Submodule ℝ E
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.mem_peirceOne_iff`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L79).

> Membership in the Peirce-`1` space is exactly the eigenvalue-one equation.

```lean
lemma IsJordanProjection.mem_peirceOne_iff [SMulCommClass ℝ E E] (p x : E) :
    x ∈ IsJordanProjection.peirceOne p ↔ p * x = x
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.peirceZero`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L85).

> The Peirce-`0` eigenspace of a projection.

```lean
def IsJordanProjection.peirceZero [SMulCommClass ℝ E E] (p : E) : Submodule ℝ E
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.mem_peirceZero_iff`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L89).

> Membership in the Peirce-`0` space is exactly annihilation by `p`.

```lean
lemma IsJordanProjection.mem_peirceZero_iff [SMulCommClass ℝ E E] (p x : E) :
    x ∈ IsJordanProjection.peirceZero p ↔ p * x = 0
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.peirceHalf`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L96).

> The Peirce-`1/2` eigenspace of a projection.  The equation is written without division so it
> works directly with the real linear-map structure.

```lean
def IsJordanProjection.peirceHalf [SMulCommClass ℝ E E] (p : E) : Submodule ℝ E
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.mem_peirceHalf_iff`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L100).

> Membership in the Peirce-`1/2` space is exactly `2 (p ∘ x) = x`.

```lean
lemma IsJordanProjection.mem_peirceHalf_iff [SMulCommClass ℝ E E] (p x : E) :
    x ∈ IsJordanProjection.peirceHalf p ↔ (2 : ℝ) • (p * x) = x
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.disjoint_peirceZero_peirceHalf`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L107).

> The Peirce-`0` and Peirce-`1/2` spaces intersect only at zero.

```lean
lemma IsJordanProjection.disjoint_peirceZero_peirceHalf [SMulCommClass ℝ E E] (p : E) :
    Disjoint (IsJordanProjection.peirceZero p) (IsJordanProjection.peirceHalf p)
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.disjoint_peirceZero_peirceOne`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L116).

> The Peirce-`0` and Peirce-`1` spaces intersect only at zero.

```lean
lemma IsJordanProjection.disjoint_peirceZero_peirceOne [SMulCommClass ℝ E E] (p : E) :
    Disjoint (IsJordanProjection.peirceZero p) (IsJordanProjection.peirceOne p)
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.disjoint_peirceHalf_peirceOne`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L125).

> The Peirce-`1/2` and Peirce-`1` spaces intersect only at zero.

```lean
lemma IsJordanProjection.disjoint_peirceHalf_peirceOne [SMulCommClass ℝ E E] (p : E) :
    Disjoint (IsJordanProjection.peirceHalf p) (IsJordanProjection.peirceOne p)
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.eq_zero_of_peirce_sum_eq_zero`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L138).

> The three Peirce eigenspaces are jointly direct: a vanishing sum of a `0`, `1/2`, and `1`
> eigenvector has all three summands equal to zero.

```lean
lemma IsJordanProjection.eq_zero_of_peirce_sum_eq_zero [SMulCommClass ℝ E E] (p : E)
    {x₀ xhalf x₁ : E} (hx₀ : x₀ ∈ IsJordanProjection.peirceZero p)
    (hxhalf : xhalf ∈ IsJordanProjection.peirceHalf p)
    (hx₁ : x₁ ∈ IsJordanProjection.peirceOne p) (hsum : x₀ + xhalf + x₁ = 0) :
    x₀ = 0 ∧ xhalf = 0 ∧ x₁ = 0
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.peirceZeroPart`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L175).

> The algebraic Peirce-`0` component of `x` relative to `p`.

```lean
def IsJordanProjection.peirceZeroPart (p x : E) : E
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.peirceHalfPart`**, a def, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L179).

> The algebraic Peirce-`1/2` component of `x` relative to `p`.

```lean
def IsJordanProjection.peirceHalfPart (p x : E) : E
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.mul_peirceZeroPart`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L183).

> The Peirce-`0` component is annihilated by `p`.

```lean
lemma IsJordanProjection.mul_peirceZeroPart [SMulCommClass ℝ E E] [IsCommJordan E] {p : E}
    (hp : IsJordanProjection p) (x : E) : p * IsJordanProjection.peirceZeroPart p x = 0
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.peirceZeroPart_mem`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L197).

> The algebraic zero component belongs to the Peirce-`0` subspace.

```lean
lemma IsJordanProjection.peirceZeroPart_mem [SMulCommClass ℝ E E] [IsCommJordan E] {p : E}
    (hp : IsJordanProjection p) (x : E) :
    IsJordanProjection.peirceZeroPart p x ∈ IsJordanProjection.peirceZero p
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.two_smul_mul_peirceHalfPart`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L203).

> The Peirce-`1/2` component has eigenvalue `1/2` for multiplication by `p`.

```lean
lemma IsJordanProjection.two_smul_mul_peirceHalfPart [SMulCommClass ℝ E E] [IsCommJordan E]
    {p : E} (hp : IsJordanProjection p) (x : E) :
    (2 : ℝ) • (p * IsJordanProjection.peirceHalfPart p x) =
      IsJordanProjection.peirceHalfPart p x
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.peirceHalfPart_mem`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L224).

> The algebraic half component belongs to the Peirce-`1/2` subspace.

```lean
lemma IsJordanProjection.peirceHalfPart_mem [SMulCommClass ℝ E E] [IsCommJordan E] {p : E}
    (hp : IsJordanProjection p) (x : E) :
    IsJordanProjection.peirceHalfPart p x ∈ IsJordanProjection.peirceHalf p
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.peirce_decomposition`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L231).

> Every element has a canonical algebraic Peirce decomposition.  The three summands have
> eigenvalues `0`, `1/2`, and `1` respectively; the `1` summand is `U_p x`.

```lean
lemma IsJordanProjection.peirce_decomposition [SMulCommClass ℝ E E] {p : E}
    (hp : IsJordanProjection p) (x : E) :
    IsJordanProjection.peirceZeroPart p x + IsJordanProjection.peirceHalfPart p x + U p x = x
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.mul_quadRep`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L239).

> Quadratic compression by a projection lands in the Peirce-`1` eigenspace.

```lean
lemma IsJordanProjection.mul_quadRep [SMulCommClass ℝ E E] [IsCommJordan E] {p : E}
    (hp : IsJordanProjection p) (x : E) : p * U p x = U p x
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.quadRep_mem_peirceOne`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L258).

> The `U_p` summand in `peirce_decomposition` belongs to the Peirce-`1` subspace.

```lean
lemma IsJordanProjection.quadRep_mem_peirceOne [SMulCommClass ℝ E E] [IsCommJordan E] {p : E}
    (hp : IsJordanProjection p) (x : E) : U p x ∈ IsJordanProjection.peirceOne p
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.quadRep_eq_self_of_mul_eq_self`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L263).

> Quadratic compression fixes every Peirce-`1` element.

```lean
lemma IsJordanProjection.quadRep_eq_self_of_mul_eq_self [SMulCommClass ℝ E E]
    {p x : E} (hp : IsJordanProjection p) (hx : p * x = x) : U p x = x
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.quadRep_range_eq_peirceOne`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L270).

> For a projection, quadratic compression is exactly the algebraic projection onto the
> Peirce-`1` eigenspace.

```lean
lemma IsJordanProjection.quadRep_range_eq_peirceOne [SMulCommClass ℝ E E] [IsCommJordan E]
    {p : E} (hp : IsJordanProjection p) :
    LinearMap.range (U p) = IsJordanProjection.peirceOne p
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.quadRep_comp_self`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L282).

> Quadratic compression by an idempotent is idempotent: `U_p ∘ U_p = U_p`.
> Consequently, `U_p` is a purely algebraic projection onto its range.

```lean
lemma IsJordanProjection.quadRep_comp_self [SMulCommClass ℝ E E] [IsCommJordan E] {p : E}
    (hp : IsJordanProjection p) (x : E) :
    U p (U p x) = U p x
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.quadRep_eq_self_of_mem_range`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L308).

> Every element in the range of `U_p` is fixed by `U_p`.

```lean
lemma IsJordanProjection.quadRep_eq_self_of_mem_range [SMulCommClass ℝ E E] [IsCommJordan E]
    {p x : E}
    (hp : IsJordanProjection p) (y : E) (hy : x = U p y) : U p x = x
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.quadRep_sub_quadRep`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L314).

> The residual after quadratic compression lies in the kernel of that compression.

```lean
lemma IsJordanProjection.quadRep_sub_quadRep [SMulCommClass ℝ E E] [IsCommJordan E]
    {p x : E} (hp : IsJordanProjection p) :
    U p (x - U p x) = 0
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_add_sub_quadRep`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean#L320).

> `x = U_p x + (x - U_p x)`.

```lean
lemma quadRep_add_sub_quadRep [SMulCommClass ℝ E E] (p x : E) :
    U p x + (x - U p x) = x
```

## Depends on

- [Moments, variance and Jordan projections](../part-01/observable.md)

## Proof depends on

- [Power-associativity](power-associative.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Projection.lean)
