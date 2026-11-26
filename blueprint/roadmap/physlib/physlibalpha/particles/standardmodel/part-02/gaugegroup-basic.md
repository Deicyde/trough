---
declaration: module
origin: cited
lean: StandardModel.cubeRootOfUnity, StandardModel.cubeRootOfUnity_isPrimitiveRoot, StandardModel.cubeRootOfUnity_pow_three, StandardModel.cubeRootOfUnity_ne_zero, StandardModel.cubeRootOfUnity_pow_mod, StandardModel.cubeRootOfUnity_mul_star, StandardModel.su3_inv_apply, StandardModel.su2_inv_apply
statement: formalized
proof: formalized
---

# A cube root of unity and the factors of a gauge transformation

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.Basic`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean): 21 declarations, 21 with a docstring.

> The root of unity `ω = exp (2 π i / 3)`, and the inverses and factors of gauge transformations.

## i. Overview

> `Physlib.Particles.StandardModel.GaugeGroup.Basic` carries the gauge group `GaugeGroupI` of
> the Standard Model and its discrete quotients. One scalar recurs throughout the structure of its
> non-abelian factors, the primitive cube root of unity `ω = exp (2 π i / 3)`. The element
> `ω • 1` generates the centre of `SU(3)`, the cyclic colour permutation has eigenvalues the
> powers of `ω`, and `diag(ω, ω²)` lies in `SU(2)`. Collected here are the facts about `ω` those
> uses need. It is a primitive cube root of unity, it cubes to one, it is nonzero and of modulus
> one, and its powers only see the exponent modulo three.
>
> The colour, isospin and hypercharge laws each constrain one factor of a gauge transformation
> `(U, V, t)`. The inverse of a unitary matrix is its conjugate transpose, so the entries of the
> inverse of an element of `SU(3)` or `SU(2)` are the conjugated transposed entries, and the
> inverse of a unitary scalar is its conjugate. The inverse of a transformation acting in one
> factor alone acts in that factor alone, by the inverse. Every gauge transformation is the
> product of its three factors, so an element fixed by each factor separately is gauge invariant.

## ii. Key results

> - `StandardModel.cubeRootOfUnity` : the primitive cube root of unity `ω = exp (2 π i / 3)`.
> - `StandardModel.cubeRootOfUnity_isPrimitiveRoot` : it is a primitive cube root of unity.
> - `StandardModel.cubeRootOfUnity_pow_three`, `StandardModel.cubeRootOfUnity_pow_mod` : it cubes
>   to one, so its powers only see the exponent modulo three.
> - `StandardModel.cubeRootOfUnity_ne_zero`, `StandardModel.cubeRootOfUnity_mul_star` : it is
>   nonzero and of modulus one.
> - `StandardModel.su3_inv_apply`, `StandardModel.su2_inv_apply` : the entries of an inverse in
>   `SU(3)` or `SU(2)` are the conjugated transposed entries.
> - `StandardModel.inv_su3Elt`, `StandardModel.inv_su2Elt` : the inverse of a colour or isospin
>   transformation is the transformation of the inverse.
> - `StandardModel.toSU3_su3Elt` and its eight companions : the three factors of a colour,
>   isospin or hypercharge transformation.
> - `StandardModel.forall_repGauge_eq_self` : an element fixed by each of the three factors of the
>   gauge group is gauge invariant.

## iv. References

> The gauge group and its quotients are in `Physlib.Particles.StandardModel.GaugeGroup.Basic`.

## A. A primitive cube root of unity

> `ω = exp (2 π i / 3)` appears in both non-abelian factors: `ω • 1` generates the centre of
> `SU(3)`, the cyclic colour permutation has eigenvalues the powers of `ω`, and `diag(ω, ω²)`
> lies in `SU(2)`.

**`StandardModel.cubeRootOfUnity`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L78).

> The primitive cube root of unity `ω = exp (2 π i / 3)`.

```lean
noncomputable def cubeRootOfUnity : ℂ
```

**`StandardModel.cubeRootOfUnity_isPrimitiveRoot`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L81).

> `ω` is a primitive cube root of unity.

```lean
lemma cubeRootOfUnity_isPrimitiveRoot : IsPrimitiveRoot cubeRootOfUnity 3
```

**`StandardModel.cubeRootOfUnity_pow_three`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L86).

> `ω` cubes to one.

```lean
lemma cubeRootOfUnity_pow_three : cubeRootOfUnity ^ 3 = 1
```

**`StandardModel.cubeRootOfUnity_ne_zero`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L90).

> `ω` is nonzero, being a value of the complex exponential.

```lean
lemma cubeRootOfUnity_ne_zero : cubeRootOfUnity ≠ 0
```

**`StandardModel.cubeRootOfUnity_pow_mod`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L93).

> Powers of `ω` only see the exponent modulo three.

```lean
lemma cubeRootOfUnity_pow_mod (m : ℕ) :
    cubeRootOfUnity ^ (m % 3) = cubeRootOfUnity ^ m
```

**`StandardModel.cubeRootOfUnity_mul_star`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L99).

> `ω` has modulus one.

```lean
lemma cubeRootOfUnity_mul_star : cubeRootOfUnity * star cubeRootOfUnity = 1
```

## B. Inverses and factors of gauge transformations

> The inverse of a unitary matrix is its conjugate transpose. This section records what that says
> for the entries of inverses in `SU(3)` and `SU(2)`, for unitary scalars, and for the colour and
> isospin transformations `(U, 1, 1)` and `(1, V, 1)`, and the colour, isospin and hypercharge
> factors of `(U, 1, 1)`, `(1, V, 1)` and `(1, 1, t)`. A gauge transformation `(U, V, t)` is the
> product of these three, which turns three separate invariances into gauge invariance.

**`StandardModel.su3_inv_apply`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L118).

> The entries of the inverse of an `SU(3)` element are the conjugated transposed
> entries, the inverse of a unitary matrix being its conjugate transpose.

```lean
lemma su3_inv_apply (U : specialUnitaryGroup (Fin 3) ℂ) (a b : Fin 3) :
    (U⁻¹).1 a b = conj (U.1 b a)
```

**`StandardModel.su2_inv_apply`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L125).

> The entries of the inverse of an `SU(2)` element are the conjugated transposed
> entries.

```lean
lemma su2_inv_apply (U : specialUnitaryGroup (Fin 2) ℂ) (a b : Fin 2) :
    (U⁻¹).1 a b = conj (U.1 b a)
```

**`StandardModel.unitary_inv_coe`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L131).

> The inverse of a unitary scalar is its conjugate.

```lean
lemma unitary_inv_coe (t : unitary ℂ) : ((t⁻¹ : unitary ℂ) : ℂ) = star (t : ℂ)
```

**`StandardModel.inv_su3Elt`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L135).

> The inverse of a colour gauge transformation is the colour transformation of the
> inverse.

```lean
lemma inv_su3Elt (U : specialUnitaryGroup (Fin 3) ℂ) :
    ((U, 1, 1) : GaugeGroupI)⁻¹ = ((U⁻¹, 1, 1) : GaugeGroupI)
```

**`StandardModel.inv_su2Elt`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L141).

> The inverse of an isospin gauge transformation is the isospin transformation of the
> inverse.

```lean
lemma inv_su2Elt (V : specialUnitaryGroup (Fin 2) ℂ) :
    ((1, V, 1) : GaugeGroupI)⁻¹ = ((1, V⁻¹, 1) : GaugeGroupI)
```

**`StandardModel.toSU3_su3Elt`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L146).

> The colour factor of a colour gauge transformation.

```lean
lemma toSU3_su3Elt (U : specialUnitaryGroup (Fin 3) ℂ) :
    GaugeGroupI.toSU3 ((U, 1, 1) : GaugeGroupI) = U
```

**`StandardModel.toSU2_su3Elt`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L150).

> The isospin factor of a colour gauge transformation is trivial.

```lean
lemma toSU2_su3Elt (U : specialUnitaryGroup (Fin 3) ℂ) :
    GaugeGroupI.toSU2 ((U, 1, 1) : GaugeGroupI) = 1
```

**`StandardModel.toU1_su3Elt`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L154).

> The hypercharge factor of a colour gauge transformation is trivial.

```lean
lemma toU1_su3Elt (U : specialUnitaryGroup (Fin 3) ℂ) :
    GaugeGroupI.toU1 ((U, 1, 1) : GaugeGroupI) = 1
```

**`StandardModel.toSU3_su2Elt`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L158).

> The colour factor of an isospin gauge transformation is trivial.

```lean
lemma toSU3_su2Elt (V : specialUnitaryGroup (Fin 2) ℂ) :
    GaugeGroupI.toSU3 ((1, V, 1) : GaugeGroupI) = 1
```

**`StandardModel.toSU2_su2Elt`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L162).

> The isospin factor of an isospin gauge transformation.

```lean
lemma toSU2_su2Elt (V : specialUnitaryGroup (Fin 2) ℂ) :
    GaugeGroupI.toSU2 ((1, V, 1) : GaugeGroupI) = V
```

**`StandardModel.toU1_su2Elt`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L166).

> The hypercharge factor of an isospin gauge transformation is trivial.

```lean
lemma toU1_su2Elt (V : specialUnitaryGroup (Fin 2) ℂ) :
    GaugeGroupI.toU1 ((1, V, 1) : GaugeGroupI) = 1
```

**`StandardModel.toSU3_u1Elt`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L170).

> The colour factor of a hypercharge gauge transformation is trivial.

```lean
lemma toSU3_u1Elt (t : unitary ℂ) :
    GaugeGroupI.toSU3 ((1, 1, t) : GaugeGroupI) = 1
```

**`StandardModel.toSU2_u1Elt`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L174).

> The isospin factor of a hypercharge gauge transformation is trivial.

```lean
lemma toSU2_u1Elt (t : unitary ℂ) :
    GaugeGroupI.toSU2 ((1, 1, t) : GaugeGroupI) = 1
```

**`StandardModel.toU1_u1Elt`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L178).

> The hypercharge factor of a hypercharge gauge transformation.

```lean
lemma toU1_u1Elt (t : unitary ℂ) :
    GaugeGroupI.toU1 ((1, 1, t) : GaugeGroupI) = t
```

**`StandardModel.forall_repGauge_eq_self`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L183).

> A gauge transformation is the product of its colour, isospin and hypercharge parts, so
> an element fixed by each of the three factors separately is gauge invariant.

```lean
lemma forall_repGauge_eq_self {B : Type*} [AddCommGroup B] [Module ℂ B]
    {rep : Representation ℂ GaugeGroupI B} {x : B}
    (h3 : ∀ U : specialUnitaryGroup (Fin 3) ℂ, rep (U, 1, 1) x = x)
    (h2 : ∀ V : specialUnitaryGroup (Fin 2) ℂ, rep (1, V, 1) x = x)
    (h1 : ∀ t : unitary ℂ, rep (1, 1, t) x = x) (g : GaugeGroupI) : rep g x = x
```

## Depends on

- [The Standard Model Gauge Group](../../../../physlib/particles/standardmodel/gaugegroup/basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean)
