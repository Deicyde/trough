---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.TriangleRule, PhyslibAlpha.Sl2.exists_eq_iff_triangleRule, PhyslibAlpha.Sl2.IsTensorOperator.triangleRule, PhyslibAlpha.Sl2.parity_eq_of_ne_zero, PhyslibAlpha.Sl2.MultipoleType, PhyslibAlpha.Sl2.MultipoleType.parity, PhyslibAlpha.Sl2.IsAllowedMultipole, PhyslibAlpha.Sl2.hf178_primary_branches_allowed
statement: formalized
proof: formalized
---

# Selection rules for multipole transitions

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.SelectionRules`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean): 14 declarations (2 instances with no name), 12 with a docstring.

> The triangle rule for tensor operators in the usual inequality form, and the angular momentum
> and parity selection rules for electromagnetic multipole transitions.

## i. Overview

> By the Wigner–Eckart theorem a nonzero tensor operator of rank `k` from `V(m)` to `V(p)` requires
> `p = k + m - 2j` for some `j ≤ min k m`. In doubled units (`k = 2λ`, `m = 2Iᵢ`, `p = 2I_f`) this is
> the triangle rule `|Iᵢ - I_f| ≤ λ ≤ Iᵢ + I_f` together with `Iᵢ + I_f + λ ∈ ℕ`, written here as
> `TriangleRule k m p`.
>
> For an electromagnetic multipole transition of order `λ` the photon carries angular momentum
> `λ ≥ 1`, and the transition operator has parity `(-1)^λ` (electric, `Eλ`) or `(-1)^(λ+1)`
> (magnetic, `Mλ`). These two facts are standard input and are not derived here; the parity
> condition is the elementary statement `parity_eq_of_ne_zero`. `IsAllowedMultipole` collects the
> three conditions. As an example, the file checks the three branches that depopulate the
> `16⁺` isomer of `¹⁷⁸Hf` (`E3` to `13⁻`, `M4` to `12⁻`, `E5` to `11⁻`) and the `E1` decay of the
> `8⁻` isomer, and shows that each is the lowest allowed multipole. The hindrance of these
> transitions by the `K` quantum number is a separate effect and not a selection rule.

## ii. Key results

> - `TriangleRule` and `exists_eq_iff_triangleRule` translate the Clebsch–Gordan condition.
> - `IsTensorOperator.triangleRule` is the triangle rule for nonzero tensor operators.
> - `parity_eq_of_ne_zero` is the parity rule.
> - `IsAllowedMultipole` combines the rules; `hf178_primary_branches_allowed` and the lemmas after
>   it are worked examples.

## iv. References

> - J. M. Blatt and V. F. Weisskopf, *Theoretical Nuclear Physics*, Wiley (1952), chapter XII.
> - ENSDF, ¹⁷⁸Hf adopted levels and gammas, E. Achterberg, O. A. Capurro, G. V. Marti,
>   Nucl. Data Sheets 110, 1473 (2009).

## A. The triangle rule

**`PhyslibAlpha.Sl2.TriangleRule`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean#L68).

> The triangle rule in doubled units: `p ≤ k + m`, `k ≤ m + p`, `m ≤ k + p` and `k + m + p`
> even. For `k = 2λ`, `m = 2Iᵢ`, `p = 2I_f` this is `|Iᵢ - I_f| ≤ λ ≤ Iᵢ + I_f` with
> `Iᵢ + I_f + λ` an integer.

```lean
def TriangleRule (k m p : ℕ) : Prop
```

**An instance with no name**, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean#L71).

```lean
instance (k m p : ℕ) : Decidable (TriangleRule k m p)
```

**`PhyslibAlpha.Sl2.exists_eq_iff_triangleRule`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean#L77).

> `p` occurs in the Clebsch–Gordan decomposition of `V(k) ⊗ V(m)` exactly when the triangle
> rule holds.

```lean
lemma exists_eq_iff_triangleRule {k m p : ℕ} :
    (∃ j : Fin (min k m + 1), k + m - 2 * (j : ℕ) = p) ↔ TriangleRule k m p
```

**`PhyslibAlpha.Sl2.IsTensorOperator.triangleRule`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean#L89).

> **Triangle rule.** A nonzero tensor operator of rank `k` from `V(m)` to `V(p)` satisfies
> `TriangleRule k m p`.

```lean
lemma IsTensorOperator.triangleRule {K : Type*} [Field K] [CharZero K] {k m p : ℕ}
    (hkm : 0 < k + m)
    {T : StandardSl2Module K k →ₗ[K] StandardSl2Module K m →ₗ[K] StandardSl2Module K p}
    (hT : IsTensorOperator T) (hT0 : T ≠ 0) : TriangleRule k m p
```

## B. Parity and multipole transitions

**`PhyslibAlpha.Sl2.parity_eq_of_ne_zero`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean#L104).

> **Parity rule.** If a linear map between states of definite parities `πᵢ` and `π_f` has
> parity `π_T`, in the sense `π_f • T = π_T • πᵢ • T`, and is nonzero, then `π_f = π_T * πᵢ`.

```lean
lemma parity_eq_of_ne_zero {K V W : Type*} [Field K] [AddCommGroup V] [Module K V]
    [AddCommGroup W] [Module K W] {T : V →ₗ[K] W} {πi πf πT : K}
    (h : πf • T = πT • πi • T) (hT : T ≠ 0) : πf = πT * πi
```

**`PhyslibAlpha.Sl2.MultipoleType`**, an inductive, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean#L111).

> Electric and magnetic multipoles.

```lean
inductive MultipoleType
  /-- Electric multipole `Eλ`. -/
  | electric
  /-- Magnetic multipole `Mλ`. -/
  | magnetic
  deriving DecidableEq
```

**`PhyslibAlpha.Sl2.MultipoleType.parity`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean#L119).

> The parity of a multipole operator of order `λ`: `(-1)^λ` for `Eλ`, `(-1)^(λ+1)` for `Mλ`.

```lean
def MultipoleType.parity : MultipoleType → ℕ → ℤ
```

**`PhyslibAlpha.Sl2.IsAllowedMultipole`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean#L126).

> A multipole transition of type `t` and order `l` between a state of spin `Iᵢ` and parity
> `πᵢ` and a state of spin `I_f` and parity `π_f` (spins in doubled units `twoIi = 2Iᵢ`,
> `twoIf = 2I_f`) is allowed if `l ≥ 1`, the triangle rule holds and the parities match.

```lean
def IsAllowedMultipole (twoIi twoIf : ℕ) (πi πf : ℤ) (t : MultipoleType) (l : ℕ) : Prop
```

**An instance with no name**, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean#L129).

```lean
instance (twoIi twoIf : ℕ) (πi πf : ℤ) (t : MultipoleType) (l : ℕ) :
    Decidable (IsAllowedMultipole twoIi twoIf πi πf t l)
```

## C. Example: the decay of the ¹⁷⁸ᵐ²Hf isomer

> Spins in doubled units: `16⁺` is `(32, 1)`, `13⁻` is `(26, -1)`, `12⁻` is `(24, -1)`, `11⁻` is
> `(22, -1)`, and the `8⁻` and `8⁺` levels of the `4 s` isomer decay are `(16, -1)` and `(16, 1)`.

**`PhyslibAlpha.Sl2.hf178_primary_branches_allowed`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean#L145).

> The three branches depopulating the `16⁺` isomer are allowed: `E3` to `13⁻`, `M4` to `12⁻`,
> `E5` to `11⁻`.

```lean
lemma hf178_primary_branches_allowed :
    IsAllowedMultipole 32 26 1 (-1) .electric 3 ∧ IsAllowedMultipole 32 24 1 (-1) .magnetic 4 ∧
      IsAllowedMultipole 32 22 1 (-1) .electric 5
```

**`PhyslibAlpha.Sl2.hf178_E3_lowest`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean#L151).

> `E3` is the lowest allowed multipole for `16⁺ → 13⁻`.

```lean
lemma hf178_E3_lowest : ∀ l < 3, ¬ IsAllowedMultipole 32 26 1 (-1) .electric l ∧
    ¬ IsAllowedMultipole 32 26 1 (-1) .magnetic l
```

**`PhyslibAlpha.Sl2.hf178_M4_lowest`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean#L156).

> `M4` is the lowest allowed multipole for `16⁺ → 12⁻`; `E4` is forbidden by parity.

```lean
lemma hf178_M4_lowest : (∀ l < 4, ¬ IsAllowedMultipole 32 24 1 (-1) .electric l ∧
    ¬ IsAllowedMultipole 32 24 1 (-1) .magnetic l) ∧
    ¬ IsAllowedMultipole 32 24 1 (-1) .electric 4
```

**`PhyslibAlpha.Sl2.hf178_E5_lowest`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean#L162).

> `E5` is the lowest allowed multipole for `16⁺ → 11⁻`.

```lean
lemma hf178_E5_lowest : (∀ l < 5, ¬ IsAllowedMultipole 32 22 1 (-1) .electric l ∧
    ¬ IsAllowedMultipole 32 22 1 (-1) .magnetic l) ∧
    ¬ IsAllowedMultipole 32 22 1 (-1) .magnetic 5
```

**`PhyslibAlpha.Sl2.hf178_E1_8minus`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean#L168).

> The `8⁻ → 8⁺` decay of the `4 s` isomer is `E1`, and `M1` is forbidden by parity.

```lean
lemma hf178_E1_8minus : IsAllowedMultipole 16 16 (-1) 1 .electric 1 ∧
    ¬ IsAllowedMultipole 16 16 (-1) 1 .magnetic 1
```

## Depends on

- [The Wigner–Eckart theorem for sl₂](wignereckart.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SelectionRules.lean)
