---
declaration: module
origin: cited
lean: Lorentz.SL2C.rotationZToAxis, Lorentz.SL2C.rotationZToAxis_zero_apply, Lorentz.SL2C.rotationZToAxis_one_apply, Lorentz.SL2C.rotationZToAxis_two_apply, Lorentz.SL2C.rotationZToAxis_zero_inv_apply, Lorentz.SL2C.rotationZToAxis_one_inv_apply, Lorentz.SL2C.rotationZToAxis_two_inv_apply, Lorentz.SL2C.rotationZToAxis_zero_mul_diagonal_mul_inv
statement: formalized
proof: formalized
---

# Coordinate-axis rotations in `SL(2,ℂ)`

The module `Physlib.Relativity.SL2C.AxisRotations`, [Physlib/Relativity/SL2C/AxisRotations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/AxisRotations.lean): 10 declarations, 10 with a docstring.

> This file defines chosen `SL(2,ℂ)` rotations carrying the `z`-axis to a selected coordinate axis.
> The spatial-axis convention is `0 = x`, `1 = y`, and `2 = z`; consequently, the rotation associated
> with axis `2` is the identity.
>
> Conjugation by these rotations transports a matrix written in the diagonal `z`-axis basis to
> the corresponding coordinate-axis basis. This provides the common change of basis used by
> coordinate-axis boosts and later constructions based on diagonal representatives.
>
> The main declarations are:
>
> - `rotationZToAxis`, the indexed family of rotations;
> - `rotationZToAxis_zero_apply` and its companions, their matrix entries;
> - `rotationZToAxis_zero_mul_diagonal_mul_inv` and its companions, their action on a
>   diagonal matrix.

**`Lorentz.SL2C.rotationZToAxis`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/AxisRotations.lean#L37).

> The `SL(2,ℂ)` rotation carrying the `z`-axis to axis `i`.

```lean
noncomputable def rotationZToAxis : Fin 3 → SL(2,ℂ)
```

**`Lorentz.SL2C.rotationZToAxis_zero_apply`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/AxisRotations.lean#L50).

> The matrix entries of the rotation carrying the `z`-axis to the `x`-axis.

```lean
lemma rotationZToAxis_zero_apply (j k : Fin 2) :
    (rotationZToAxis 0).1 j k =
      ((((Real.sqrt 2 : ℝ) : ℂ))⁻¹ • !![1, -1; 1, 1]) j k
```

**`Lorentz.SL2C.rotationZToAxis_one_apply`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/AxisRotations.lean#L55).

> The matrix entries of the rotation carrying the `z`-axis to the `y`-axis.

```lean
lemma rotationZToAxis_one_apply (j k : Fin 2) :
    (rotationZToAxis 1).1 j k =
      ((((Real.sqrt 2 : ℝ) : ℂ))⁻¹ • !![1, Complex.I; Complex.I, 1]) j k
```

**`Lorentz.SL2C.rotationZToAxis_two_apply`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/AxisRotations.lean#L60).

> The rotation carrying the `z`-axis to itself is the identity matrix.

```lean
lemma rotationZToAxis_two_apply (j k : Fin 2) :
    (rotationZToAxis 2).1 j k = (1 : Matrix (Fin 2) (Fin 2) ℂ) j k
```

**`Lorentz.SL2C.rotationZToAxis_zero_inv_apply`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/AxisRotations.lean#L64).

> The matrix entries of the inverse rotation from the `x`-axis to the `z`-axis.

```lean
lemma rotationZToAxis_zero_inv_apply (j k : Fin 2) :
    ((rotationZToAxis 0)⁻¹).1 j k =
      ((((Real.sqrt 2 : ℝ) : ℂ))⁻¹ • !![1, 1; -1, 1]) j k
```

**`Lorentz.SL2C.rotationZToAxis_one_inv_apply`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/AxisRotations.lean#L71).

> The matrix entries of the inverse rotation from the `y`-axis to the `z`-axis.

```lean
lemma rotationZToAxis_one_inv_apply (j k : Fin 2) :
    ((rotationZToAxis 1)⁻¹).1 j k =
      ((((Real.sqrt 2 : ℝ) : ℂ))⁻¹ • !![1, -Complex.I; -Complex.I, 1]) j k
```

**`Lorentz.SL2C.rotationZToAxis_two_inv_apply`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/AxisRotations.lean#L78).

> The inverse rotation from the `z`-axis to itself is the identity matrix.

```lean
lemma rotationZToAxis_two_inv_apply (j k : Fin 2) :
    ((rotationZToAxis 2)⁻¹).1 j k = (1 : Matrix (Fin 2) (Fin 2) ℂ) j k
```

**`Lorentz.SL2C.rotationZToAxis_zero_mul_diagonal_mul_inv`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/AxisRotations.lean#L85).

> Conjugating `diag(a, b)` by the rotation to the `x`-axis expresses it in the `x`-axis
> basis.

```lean
lemma rotationZToAxis_zero_mul_diagonal_mul_inv (a b : ℂ) :
    (rotationZToAxis 0).1 * !![a, 0; 0, b] * ((rotationZToAxis 0)⁻¹).1 =
      !![(a + b) / 2, (a - b) / 2; (a - b) / 2, (a + b) / 2]
```

**`Lorentz.SL2C.rotationZToAxis_one_mul_diagonal_mul_inv`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/AxisRotations.lean#L100).

> Conjugating `diag(a, b)` by the rotation to the `y`-axis expresses it in the `y`-axis
> basis.

```lean
lemma rotationZToAxis_one_mul_diagonal_mul_inv (a b : ℂ) :
    (rotationZToAxis 1).1 * !![a, 0; 0, b] * ((rotationZToAxis 1)⁻¹).1 =
      !![(a + b) / 2, -Complex.I * (a - b) / 2;
        Complex.I * (a - b) / 2, (a + b) / 2]
```

**`Lorentz.SL2C.rotationZToAxis_two_mul_diagonal_mul_inv`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/AxisRotations.lean#L118).

> Conjugating `diag(a, b)` by the identity rotation leaves it unchanged.

```lean
lemma rotationZToAxis_two_mul_diagonal_mul_inv (a b : ℂ) :
    (rotationZToAxis 2).1 * !![a, 0; 0, b] * ((rotationZToAxis 2)⁻¹).1 =
      !![a, 0; 0, b]
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Relativity/SL2C/AxisRotations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/AxisRotations.lean)
