---
declaration: module
origin: cited
lean: Lorentz.SL2C.boostAxis, Lorentz.SL2C.boostAxis_zero_apply, Lorentz.SL2C.boostAxis_one_apply, Lorentz.SL2C.boostAxis_two_apply, Lorentz.SL2C.boostAxis_inv, Lorentz.SL2C.boostAxis_conjTranspose, Lorentz.SL2C.boostAxis_eq_conj, Lorentz.SL2C.exists_conj_boostAxis
statement: formalized
proof: formalized
---

# Coordinate-axis boosts in `SL(2,ℂ)` and the Lorentz group

The module `Physlib.Relativity.LorentzGroup.Boosts.Axis`, [Physlib/Relativity/LorentzGroup/Boosts/Axis.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Axis.lean): 10 declarations, 10 with a docstring.

## i. Overview

> We define the axis-indexed lift `Lorentz.SL2C.boostAxis` in `SL(2,ℂ)` and its image
> `LorentzGroup.boostAxis` in the Lorentz group.
>
> The parameter `t ≠ 0` is multiplicative; replacing `t` by `t⁻¹` reverses the boost. For
> `t > 0`, its rapidity is `2 * log t`; negative values retain the action of the central
> element `-1 : SL(2,ℂ)`.
>
> For the `z`-axis, `LorentzGroup.boostAxis 2 t ht` agrees with the velocity-parameterized boost
> `LorentzGroup.boost 2 β` at `β = (t² - t⁻²) / (t² + t⁻²)`.
>
> The lift is Hermitian along every axis, and the `x`- and `y`-axis lifts are conjugates of
> the diagonal `z`-axis lift.
>
> The index `Sum.inl 0` is the time coordinate, while `Sum.inr 0`, `Sum.inr 1`, and
> `Sum.inr 2` are the `x`, `y`, and `z` coordinates. Accordingly, axis indices `0`, `1`, and
> `2` select the `x`-, `y`-, and `z`-axis boosts. The covering map uses the action
> `X ↦ M X Mᴴ` on self-adjoint matrices.

## ii. Key results

> - `Lorentz.SL2C.boostAxis` defines the axis-boost lifts.
> - `Lorentz.SL2C.boostAxis_inv` and `Lorentz.SL2C.boostAxis_conjTranspose` give their
>   inverses and Hermiticity.
> - `LorentzGroup.boostAxis` defines the induced Lorentz transformations, with entries given by
>   `LorentzGroup.boostAxis_apply`.
> - `Lorentz.SL2C.exists_conj_boostAxis` proves that every lift is conjugate to the `z`-boost.

## A. The axis-boost lift

**`Lorentz.SL2C.boostAxis`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Axis.lean#L65).

> The `SL(2,ℂ)` lift of the boost along spatial axis `i`, with `0 = x`, `1 = y`, and
> `2 = z`. The parameter `t` is multiplicative, and for `t > 0` the rapidity is `2 * log t`.

```lean
noncomputable def boostAxis : Fin 3 → (t : ℝ) → t ≠ 0 → SL(2,ℂ)
```

**`Lorentz.SL2C.boostAxis_zero_apply`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Axis.lean#L99).

> The matrix entries of the `SL(2,ℂ)` boost lift along the `x`-axis.

```lean
lemma boostAxis_zero_apply (t : ℝ) (ht : t ≠ 0) (j k : Fin 2) :
    (boostAxis 0 t ht).1 j k =
      (!![((t : ℂ) + (t : ℂ)⁻¹) / 2, ((t : ℂ) - (t : ℂ)⁻¹) / 2;
        ((t : ℂ) - (t : ℂ)⁻¹) / 2, ((t : ℂ) + (t : ℂ)⁻¹) / 2]) j k
```

**`Lorentz.SL2C.boostAxis_one_apply`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Axis.lean#L105).

> The matrix entries of the `SL(2,ℂ)` boost lift along the `y`-axis.

```lean
lemma boostAxis_one_apply (t : ℝ) (ht : t ≠ 0) (j k : Fin 2) :
    (boostAxis 1 t ht).1 j k =
      (!![((t : ℂ) + (t : ℂ)⁻¹) / 2,
        -Complex.I * ((t : ℂ) - (t : ℂ)⁻¹) / 2;
        Complex.I * ((t : ℂ) - (t : ℂ)⁻¹) / 2,
        ((t : ℂ) + (t : ℂ)⁻¹) / 2]) j k
```

**`Lorentz.SL2C.boostAxis_two_apply`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Axis.lean#L113).

> The matrix entries of the diagonal `SL(2,ℂ)` boost lift along the `z`-axis.

```lean
lemma boostAxis_two_apply (t : ℝ) (ht : t ≠ 0) (j k : Fin 2) :
    (boostAxis 2 t ht).1 j k = (!![(t : ℂ), 0; 0, (t : ℂ)⁻¹]) j k
```

**`Lorentz.SL2C.boostAxis_inv`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Axis.lean#L117).

> Inverting an axis boost replaces its multiplicative parameter `t` by `t⁻¹`.

```lean
lemma boostAxis_inv (i : Fin 3) (t : ℝ) (ht : t ≠ 0) :
    (boostAxis i t ht)⁻¹ = boostAxis i t⁻¹ (inv_ne_zero ht)
```

**`Lorentz.SL2C.boostAxis_conjTranspose`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Axis.lean#L136).

> The matrix underlying an axis-boost lift is Hermitian.

```lean
lemma boostAxis_conjTranspose (i : Fin 3) (t : ℝ) (ht : t ≠ 0) :
    (boostAxis i t ht).1ᴴ = (boostAxis i t ht).1
```

## B. Axis conjugation

**`Lorentz.SL2C.boostAxis_eq_conj`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Axis.lean#L147).

> Every axis boost is obtained by conjugating the `z`-axis boost by `rotationZToAxis`.

```lean
lemma boostAxis_eq_conj (i : Fin 3) (t : ℝ) (ht : t ≠ 0) :
    boostAxis i t ht =
      rotationZToAxis i * boostAxis 2 t ht * (rotationZToAxis i)⁻¹
```

**`Lorentz.SL2C.exists_conj_boostAxis`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Axis.lean#L172).

> Every coordinate-axis boost is conjugate to the `z`-axis boost.

```lean
lemma exists_conj_boostAxis (i : Fin 3) :
    ∃ R : SL(2,ℂ), ∀ (t : ℝ) (ht : t ≠ 0),
      boostAxis i t ht = R * boostAxis 2 t ht * R⁻¹
```

## C. The induced Lorentz transformation

**`LorentzGroup.boostAxis`**, a def, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Axis.lean#L189).

> The Lorentz transformation induced by the multiplicatively parameterized `SL(2,ℂ)` boost
> along spatial axis `i`.

```lean
noncomputable def boostAxis (i : Fin 3) (t : ℝ) (ht : t ≠ 0) : LorentzGroup 3
```

**`LorentzGroup.boostAxis_apply`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Axis.lean#L193).

> The entries of an axis boost in the Lorentz group.

```lean
lemma boostAxis_apply (i : Fin 3) (t : ℝ) (ht : t ≠ 0) (a b : Fin 1 ⊕ Fin 3) :
    (boostAxis i t ht).1 a b =
      if a = Sum.inl 0 ∧ b = Sum.inl 0 then (t ^ 2 + (t⁻¹) ^ 2) / 2
      else if a = Sum.inl 0 ∧ b = Sum.inr i then -((t ^ 2 - (t⁻¹) ^ 2) / 2)
      else if a = Sum.inr i ∧ b = Sum.inl 0 then -((t ^ 2 - (t⁻¹) ^ 2) / 2)
      else if a = Sum.inr i ∧ b = Sum.inr i then (t ^ 2 + (t⁻¹) ^ 2) / 2
      else if a = b then 1 else 0
```

## Depends on

- [Coordinate-axis rotations in `SL(2,ℂ)`](../sl2c/axisrotations.md)
- [The group SL(2, ℂ) and it's relation to the Lorentz group](../sl2c/basic.md)

## Sources

- [Physlib/Relativity/LorentzGroup/Boosts/Axis.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Axis.lean)
