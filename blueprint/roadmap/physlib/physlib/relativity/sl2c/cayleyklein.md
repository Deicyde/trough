---
declaration: module
origin: cited
lean: Lorentz.SL2C.cayleyKlein, Lorentz.SL2C.cayleyKlein_mem_unitaryGroup, Lorentz.SL2C.toLorentzGroup_cayleyKlein_mem_rotations, Lorentz.SL2C.cayleyKleinRotation, Lorentz.SL2C.cayleyKleinRotation_inr_inr, Lorentz.SL2C.exists_cayleyKleinRotation_apply_two
statement: formalized
proof: formalized
---

# Cayley–Klein parameters

The module `Physlib.Relativity.SL2C.CayleyKlein`, [Physlib/Relativity/SL2C/CayleyKlein.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/CayleyKlein.lean): 6 declarations, 6 with a docstring.

## i. Overview

> Two complex numbers `a b` with `‖a‖² + ‖b‖² = 1`, the Cayley–Klein parameters, give the unitary
> element `!![a, -conj b; b, conj a]` of `SL(2, ℂ)`. Its image in the Lorentz group is a rotation,
> whose matrix is written explicitly in terms of `a` and `b`.

## ii. Key results

> - `cayleyKlein` : the element of `SL(2, ℂ)` with Cayley–Klein parameters `a b`.
> - `cayleyKlein_mem_unitaryGroup` : a Cayley–Klein element is unitary.
> - `toLorentzGroup_cayleyKlein_mem_rotations` : the image of a Cayley–Klein element is a
>   rotation.
> - `cayleyKleinRotation` : the Lorentz-group rotation of the Cayley–Klein parameters `a b`.
> - `cayleyKleinRotation_inr_inr` : the spatial block of `cayleyKleinRotation a b h` is the
>   matrix written explicitly in terms of `a` and `b`.
> - `exists_cayleyKleinRotation_apply_two` : every unit vector is the image of the third axis
>   under some Cayley–Klein rotation.

## iv. References

> * https://mathworld.wolfram.com/Cayley-KleinParameters.html

## A. The Cayley–Klein element

**`Lorentz.SL2C.cayleyKlein`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/CayleyKlein.lean#L61).

> The element `!![a, -conj b; b, conj a]` of `SL(2, ℂ)`, given by its Cayley–Klein
> parameters `a b` with `‖a‖² + ‖b‖² = 1`.

```lean
def cayleyKlein (a b : ℂ) (h : normSq a + normSq b = 1) : SL(2, ℂ)
```

**`Lorentz.SL2C.cayleyKlein_mem_unitaryGroup`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/CayleyKlein.lean#L67).

> A Cayley–Klein element is unitary.

```lean
lemma cayleyKlein_mem_unitaryGroup (a b : ℂ) (h : normSq a + normSq b = 1) :
    (cayleyKlein a b h).1 ∈ unitaryGroup (Fin 2) ℂ
```

**`Lorentz.SL2C.toLorentzGroup_cayleyKlein_mem_rotations`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/CayleyKlein.lean#L77).

> The image of a Cayley–Klein element is a rotation.

```lean
lemma toLorentzGroup_cayleyKlein_mem_rotations (a b : ℂ) (h : normSq a + normSq b = 1) :
    toLorentzGroup (cayleyKlein a b h) ∈ LorentzGroup.Rotations 3
```

## B. The Cayley–Klein rotation

**`Lorentz.SL2C.cayleyKleinRotation`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/CayleyKlein.lean#L92).

> The rotation of the Cayley–Klein parameters `a b`, as an element of the Lorentz rotation
> subgroup.

```lean
def cayleyKleinRotation (a b : ℂ) (h : normSq a + normSq b = 1) : LorentzGroup.Rotations 3
```

**`Lorentz.SL2C.cayleyKleinRotation_inr_inr`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/CayleyKlein.lean#L96).

> The spatial block of the rotation of the Cayley–Klein parameters `a b`.

```lean
lemma cayleyKleinRotation_inr_inr (a b : ℂ) (h : normSq a + normSq b = 1) (i j : Fin 3) :
    (cayleyKleinRotation a b h).1.1 (Sum.inr i) (Sum.inr j) =
      !![(a ^ 2 - b ^ 2).re, (a ^ 2 - b ^ 2).im, 2 * (a * starRingEnd ℂ b).re;
        -(a ^ 2 + b ^ 2).im, (a ^ 2 + b ^ 2).re, -2 * (a * starRingEnd ℂ b).im;
        -2 * (a * b).re, -2 * (a * b).im, normSq a - normSq b] i j
```

**`Lorentz.SL2C.exists_cayleyKleinRotation_apply_two`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/CayleyKlein.lean#L108).

> Every unit vector is the image of the third axis under some Cayley–Klein rotation.

```lean
lemma exists_cayleyKleinRotation_apply_two (n : Fin 3 → ℝ)
    (hn : n 0 ^ 2 + n 1 ^ 2 + n 2 ^ 2 = 1) :
    ∃ a b, ∃ h : normSq a + normSq b = 1,
      ∀ i, (cayleyKleinRotation a b h).1.1 (Sum.inr i) (Sum.inr 2) = n i
```

## Depends on

- [Rotations](../lorentzgroup/rotations.md)
- [The group SL(2, ℂ) and it's relation to the Lorentz group](basic.md)

## Sources

- [Physlib/Relativity/SL2C/CayleyKlein.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/CayleyKlein.lean)
