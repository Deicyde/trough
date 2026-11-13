---
declaration: module
origin: cited
lean: walshSign, walshSign_zero_left, walshSign_zero_right, walshSign_one_one, walshSign_comm, walshSign_mul_self, conj_walshSign, norm_walshSign
statement: formalized
proof: formalized
---

# Walsh characters

The module `PhyslibAlpha.Mathematics.SpecialFunctions.Walsh`, [PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean): 22 declarations, 22 with a docstring.

> The Walsh characters on `Fin n → Fin 2` and the orthonormal basis of rescaled Walsh vectors.

## i. Overview

> For `x z : Fin n → Fin 2` the Walsh character `walsh x z = ∏ i, (-1) ^ (x i * z i)` is the
> additive character `z ↦ (-1) ^ (x ⬝ z)` of `(ZMod 2)ⁿ`. The orthogonality relation
> `sum_walsh_mul_walsh` is the explicit form of the orthogonality of characters of a finite
> abelian group, which Mathlib states as `AddChar.wInner_cWeight_eq_boole`. We work with the
> explicit `Fin 2`-indexed form because `Fin n → Fin 2` is what indexes the computational basis
> of `n` qubits. The matrix `Matrix.of walsh`, with entries `(-1) ^ (x ⬝ z)`, is the Sylvester
> Hadamard matrix of order `2 ^ n` in the sense of Mathlib's `Matrix.IsHadamard`.
>
> Rescaling by `(√(2 ^ n))⁻¹`, the vectors `z ↦ (√(2 ^ n))⁻¹ * walsh x z` form an orthonormal
> basis `walshBasis n` of `EuclideanSpace ℂ (Fin n → Fin 2)`, and Parseval's identity for this
> basis is `sum_norm_sq_sum_mul_inv_sqrt_mul_walsh`.

## ii. Key results

> - `walshSign` : the sign `(-1) ^ (j * k)` on `Fin 2`.
> - `walsh` : the Walsh character on `Fin n → Fin 2`.
> - `sum_walsh_mul_walsh` : orthogonality of the Walsh characters.
> - `walshBasis` : the orthonormal basis of rescaled Walsh vectors.
> - `sum_norm_sq_sum_mul_inv_sqrt_mul_walsh` : Parseval's identity for the rescaled Walsh vectors.

## iv. References

> - M. F. Pusey, J. Barrett and T. Rudolph, *On the reality of the quantum state*,
>   Nature Phys. 8, 475–478 (2012), arXiv:1111.3328. [ref: Pusey:2011de]

## A. Signs on `Fin 2`

**`walshSign`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L63).

> The sign `(-1) ^ (j * k)` for `j k : Fin 2`, as a complex number.

```lean
def walshSign (j k : Fin 2) : ℂ
```

**`walshSign_zero_left`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L67).

> The sign `walshSign 0 k` is `1`.

```lean
lemma walshSign_zero_left (k : Fin 2) : walshSign 0 k = 1
```

**`walshSign_zero_right`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L72).

> The sign `walshSign j 0` is `1`.

```lean
lemma walshSign_zero_right (j : Fin 2) : walshSign j 0 = 1
```

**`walshSign_one_one`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L77).

> The sign `walshSign 1 1` is `-1`.

```lean
lemma walshSign_one_one : walshSign 1 1 = -1
```

**`walshSign_comm`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L81).

> The sign `(-1) ^ (j * k)` is symmetric in `j` and `k`.

```lean
lemma walshSign_comm (j k : Fin 2) : walshSign j k = walshSign k j
```

**`walshSign_mul_self`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L85).

> A sign squares to one.

```lean
lemma walshSign_mul_self (j k : Fin 2) : walshSign j k * walshSign j k = 1
```

**`conj_walshSign`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L89).

> A sign equals its complex conjugate.

```lean
lemma conj_walshSign (j k : Fin 2) : starRingEnd ℂ (walshSign j k) = walshSign j k
```

**`norm_walshSign`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L93).

> A sign has unit norm.

```lean
lemma norm_walshSign (j k : Fin 2) : ‖walshSign j k‖ = 1
```

**`sum_walshSign_mul_walshSign`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L97).

> Orthogonality of the signs on `Fin 2`.

```lean
lemma sum_walshSign_mul_walshSign (a b : Fin 2) :
    ∑ k, walshSign a k * walshSign b k = if a = b then 2 else 0
```

## B. Walsh characters

**`walsh`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L109).

> The Walsh character `∏ i, (-1) ^ (x i * z i)` on `Fin n → Fin 2`.

```lean
def walsh (x z : Fin n → Fin 2) : ℂ
```

**`walsh_eq`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L112).

> The Walsh character is the product of the signs of the components.

```lean
lemma walsh_eq (x z : Fin n → Fin 2) : walsh x z = ∏ i, walshSign (x i) (z i)
```

**`walsh_comm`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L115).

> The Walsh character `walsh x z` is symmetric in `x` and `z`.

```lean
lemma walsh_comm (x z : Fin n → Fin 2) : walsh x z = walsh z x
```

**`walsh_mul_self`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L119).

> A Walsh character squares to one.

```lean
lemma walsh_mul_self (x z : Fin n → Fin 2) : walsh x z * walsh x z = 1
```

**`conj_walsh`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L123).

> A Walsh character equals its complex conjugate.

```lean
lemma conj_walsh (x z : Fin n → Fin 2) : starRingEnd ℂ (walsh x z) = walsh x z
```

**`norm_walsh`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L127).

> A Walsh character has unit norm.

```lean
lemma norm_walsh (x z : Fin n → Fin 2) : ‖walsh x z‖ = 1
```

**`sum_walsh_mul_walsh`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L131).

> Orthogonality of the Walsh characters.

```lean
lemma sum_walsh_mul_walsh (x y : Fin n → Fin 2) :
    ∑ z, walsh x z * walsh y z = if x = y then 2 ^ n else 0
```

## C. The Walsh basis

### C.1. Rescaled Walsh vectors

**`walshVec`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L151).

> The rescaled Walsh vector `z ↦ (√(2 ^ n))⁻¹ * walsh x z` in
> `EuclideanSpace ℂ (Fin n → Fin 2)`.

```lean
def walshVec (x : Fin n → Fin 2) : EuclideanSpace ℂ (Fin n → Fin 2)
```

**`walshVec_apply`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L156).

> The component `z` of `walshVec x` is `(√(2 ^ n))⁻¹ * walsh x z`.

```lean
lemma walshVec_apply (x z : Fin n → Fin 2) :
    walshVec x z = (Real.sqrt (2 ^ n))⁻¹ * walsh x z
```

**`orthonormal_walshVec`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L160).

> The rescaled Walsh vectors are orthonormal.

```lean
lemma orthonormal_walshVec : Orthonormal ℂ (walshVec (n := n))
```

### C.2. The orthonormal basis

**`walshBasis`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L185).

> The orthonormal basis of `EuclideanSpace ℂ (Fin n → Fin 2)` formed by the rescaled Walsh
> vectors `walshVec x`.

```lean
def walshBasis (n : ℕ) :
    OrthonormalBasis (Fin n → Fin 2) ℂ (EuclideanSpace ℂ (Fin n → Fin 2))
```

**`coe_walshBasis`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L193).

> The vectors of `walshBasis n` are the rescaled Walsh vectors.

```lean
lemma coe_walshBasis (n : ℕ) : ⇑(walshBasis n) = walshVec
```

### C.3. Parseval's identity

**`sum_norm_sq_sum_mul_inv_sqrt_mul_walsh`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean#L203).

> Parseval's identity for the rescaled Walsh vectors. The vector
> `x ↦ ∑ z, β z * (√(2 ^ n))⁻¹ * walsh x z` has the same squared norm as `β`.

```lean
lemma sum_norm_sq_sum_mul_inv_sqrt_mul_walsh (n : ℕ) (β : (Fin n → Fin 2) → ℂ) :
    ∑ x : Fin n → Fin 2, ‖∑ z, β z * ((Real.sqrt (2 ^ n))⁻¹ * walsh x z)‖ ^ 2 =
      ∑ z, ‖β z‖ ^ 2
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Walsh.lean)
