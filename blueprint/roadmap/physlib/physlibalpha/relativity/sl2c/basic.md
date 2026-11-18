---
declaration: module
origin: cited
lean: Lorentz.SL2C.conjHom, Lorentz.SL2C.conjHom_coe, Lorentz.SL2C.conjHom_involutive, Lorentz.SL2C.conjHom_inv_conjTranspose, Lorentz.SL2C.toLorentzGroup_neg_one, Lorentz.SL2C.sum_pauliLower_mul_sl2c, Lorentz.SL2C.toLorentzGroup_conjTranspose
statement: formalized
proof: formalized
---

# Conjugation and the kernel of the covering map

The module `PhyslibAlpha.Relativity.SL2C.Basic`, [PhyslibAlpha/Relativity/SL2C/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/Basic.lean): 7 declarations, 6 with a docstring.

> Entrywise conjugation on `SL(2, ℂ)`, and the covering map on `-1`, on entries and on adjoints.

## i. Overview

> Three things about the covering map `SL(2, ℂ) →* LorentzGroup 3` are collected here, all
> needed to carry a Lorentz index through a spinor computation.
>
> Entrywise complex conjugation is a monoid endomorphism `conjHom` of `SL(2, ℂ)`, an involution,
> and conjugating the group argument undoes the conjugation of the entries: the inverse
> conjugate transpose at `conjHom g` is the inverse transpose at `g`. This is what lets a
> right-handed slot be treated as a conjugated left-handed one.
>
> The covering map sandwiches, `A ↦ M A Mᴴ`, so the two signs of `-1` cancel and
> `toLorentzGroup (-1) = 1`: the map is two-to-one. It also intertwines conjugate transposition
> with matrix transposition, `L(M†) = L(M)ᵀ`.
>
> Finally `sum_pauliLower_mul_sl2c` is the defining intertwining identity read entrywise:
> sandwiching `σ_μ` between `g` and `gᴴ` mixes the covariant Pauli matrices by the column `μ` of
> the Lorentz matrix of `g`.

## ii. Key results

> - `Lorentz.SL2C.conjHom` : entrywise conjugation as a monoid endomorphism.
> - `Lorentz.SL2C.conjHom_involutive`, `Lorentz.SL2C.conjHom_inv_conjTranspose` : its
>   involutivity, and its effect on the inverse conjugate transpose.
> - `Lorentz.SL2C.toLorentzGroup_neg_one` : the centre covers the identity.
> - `Lorentz.SL2C.sum_pauliLower_mul_sl2c` : the intertwining identity on entries.
> - `Lorentz.SL2C.toLorentzGroup_conjTranspose` : `L(M†) = L(M)ᵀ`.

## iv. References

> The covering map and its properties are in `Physlib.Relativity.SL2C.Basic`.

## A. Entrywise conjugation

**`Lorentz.SL2C.conjHom`**, an abbrev, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/Basic.lean#L73).

> Entrywise complex conjugation as a monoid endomorphism of `SL(2,ℂ)`: Mathlib's
> `SpecialLinearGroup.map` along `starRingEnd ℂ`.

```lean
abbrev conjHom : SL(2,ℂ) →* SL(2,ℂ)
```

**`Lorentz.SL2C.conjHom_coe`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/Basic.lean#L75).

```lean
lemma conjHom_coe (g : SL(2,ℂ)) : (conjHom g).1 = g.1.map star
```

**`Lorentz.SL2C.conjHom_involutive`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/Basic.lean#L78).

> Conjugation is an involution, hence surjective.

```lean
lemma conjHom_involutive : Function.Involutive conjHom
```

**`Lorentz.SL2C.conjHom_inv_conjTranspose`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/Basic.lean#L86).

> Conjugating the group argument undoes the conjugation of the entries: the inverse
> conjugate transpose at `conjHom g` is the inverse transpose at `g`.

```lean
lemma conjHom_inv_conjTranspose (g : SL(2,ℂ)) : (((conjHom g).1)⁻¹)ᴴ = (g.1⁻¹)ᵀ
```

## B. The kernel of the covering map

**`Lorentz.SL2C.toLorentzGroup_neg_one`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/Basic.lean#L103).

> **The centre of `SL(2, ℂ)` covers the identity Lorentz transformation.** The covering
> map sandwiches, `A ↦ M A Mᴴ`, so the two signs of `-1` cancel. Together with
> `_root_.map_one` this says that the covering map is two-to-one.

```lean
lemma toLorentzGroup_neg_one : toLorentzGroup (-1) = 1
```

## C. The intertwining identity on entries

**`Lorentz.SL2C.sum_pauliLower_mul_sl2c`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/Basic.lean#L121).

> The intertwining identity `toSelfAdjointMap_basis` read entrywise: sandwiching the
> covariant Pauli matrix `σ_μ` between `g` and `gᴴ` mixes the covariant Pauli matrices by the
> column `μ` of the Lorentz matrix of `g`, the summed Lorentz index first.

```lean
lemma sum_pauliLower_mul_sl2c (g : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (β β' : Fin 2) :
    ∑ p : Fin 2 × Fin 2, PauliMatrix.pauliLower μ p.1 p.2 * (g.1 β p.1 * star (g.1 β' p.2))
      = ∑ ν : Fin 1 ⊕ Fin 3, (((toLorentzGroup g).1 ν μ : ℝ) : ℂ)
        * PauliMatrix.pauliLower ν β β'
```

## D. The covering map and adjoints

**`Lorentz.SL2C.toLorentzGroup_conjTranspose`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/Basic.lean#L145).

> The covering map intertwines conjugate transposition with matrix
> transposition: `L(M†) = L(M)ᵀ`.

```lean
lemma toLorentzGroup_conjTranspose {M N : SL(2,ℂ)} (hN : N.1 = M.1ᴴ) :
    (toLorentzGroup N).1 = (toLorentzGroup M).1ᵀ
```

## Depends on

- [The group SL(2, ℂ) and it's relation to the Lorentz group](../../../physlib/relativity/sl2c/basic.md)
- [The covariant Pauli matrices as plain matrices](../paulimatrices/selfadjoint.md)

## Sources

- [PhyslibAlpha/Relativity/SL2C/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/Basic.lean)
