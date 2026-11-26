---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.toMatrix'_standard_one_Jx, PhyslibAlpha.Sl2.toMatrix'_standard_one_Jy, PhyslibAlpha.Sl2.toMatrix'_standard_one_Jz, PhyslibAlpha.Sl2.toMatrix'_standard_one_Jp, PhyslibAlpha.Sl2.toMatrix'_standard_one_Jm, PhyslibAlpha.Sl2.normVec_one_zero, PhyslibAlpha.Sl2.normVec_one_one
statement: formalized
proof: formalized
---

# Spin ½ and the Pauli matrices

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.SpinHalf`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinHalf.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinHalf.lean): 7 declarations, 7 with a docstring.

> The spin-½ representation `standard 1` is given by half the Pauli matrices.

## i. Overview

> The spin-`n/2` representation `AngularMomentumRepresentation.standard n` acts on
> `StandardSl2Module ℂ n = Fin (n + 1) → ℂ`, whose standard basis `v k = Pi.single k 1` is the
> basis of `LinearMap.toMatrix'`. For `n = 1` the matrices of `Jx, Jy, Jz` in this basis are
> `σ₁ / 2, σ₂ / 2, σ₃ / 2`, with `σ_i = pauliMatrix (Sum.inr i)`, and those of the ladder operators
> `J₊, J₋` are `σ₊ = |↑⟩⟨↓|` and `σ₋ = |↓⟩⟨↑|`, written as matrix literals; they equal
> `(1 / 2) (σ₁ + i σ₂)` and `(1 / 2) (σ₁ - i σ₂)` (A). No new operators are defined: spin ½ is
> `standard 1`, and the lemmas identify its matrices.
>
> Conventions. `ℏ = 1`. The spatial indices `0, 1, 2` label `x, y, z`. The basis is
> `|↑⟩ = |0⟩ = v 0` (`m = +½`) and `|↓⟩ = |1⟩ = v 1` (`m = -½`), so `σ₃ |↑⟩ = |↑⟩`. Over `ℝ` the
> normalised states `|½, m⟩ = normVec 1 a` with `m = ½ - a` are exactly these basis vectors (B).
> The Condon–Shortley phase convention of `normVec` holds with no extra signs:
> `J₊ |↓⟩ = |↑⟩` and `J₋ |↑⟩ = |↓⟩`.
>
> The commutation relations `[Jᵢ, Jⱼ] = i εᵢⱼₖ Jₖ` are not restated here: for `standard 1` they are
> the fields `comm_xy`, `comm_yz`, `comm_zx` of `AngularMomentumRepresentation`, and for the Pauli
> matrices they are `PauliMatrix.pauliMatrix_commutator`, `[σᵢ, σⱼ] = 2i ∑ₖ εᵢⱼₖ σₖ`, with its
> vector form `PauliMatrix.vectorMatrix_commutator` (`Physlib.Relativity.PauliMatrices.Basic`).

## ii. Key results

> - `toMatrix'_standard_one_Jx`, `toMatrix'_standard_one_Jy`, `toMatrix'_standard_one_Jz` :
>   `J = σ / 2` for spin ½.
> - `toMatrix'_standard_one_Jp`, `toMatrix'_standard_one_Jm` : the ladder operators are `σ₊, σ₋`.
> - `normVec_one_zero`, `normVec_one_one` : the normalised basis of spin ½ is the standard basis.

## iv. References

## A. The spin-½ operators as Pauli matrices

**`PhyslibAlpha.Sl2.toMatrix'_standard_one_Jx`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinHalf.lean#L63).

> In the basis `v 0 = |↑⟩`, `v 1 = |↓⟩`, the spin-½ operator `Jx` is `σ₁ / 2`.

```lean
lemma toMatrix'_standard_one_Jx :
    LinearMap.toMatrix' (standard 1).Jx = (1 / 2 : ℂ) • pauliMatrix (Sum.inr 0)
```

**`PhyslibAlpha.Sl2.toMatrix'_standard_one_Jy`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinHalf.lean#L70).

> In the basis `v 0 = |↑⟩`, `v 1 = |↓⟩`, the spin-½ operator `Jy` is `σ₂ / 2`.

```lean
lemma toMatrix'_standard_one_Jy :
    LinearMap.toMatrix' (standard 1).Jy = (1 / 2 : ℂ) • pauliMatrix (Sum.inr 1)
```

**`PhyslibAlpha.Sl2.toMatrix'_standard_one_Jz`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinHalf.lean#L78).

> In the basis `v 0 = |↑⟩`, `v 1 = |↓⟩`, the spin-½ operator `Jz` is `σ₃ / 2`.

```lean
lemma toMatrix'_standard_one_Jz :
    LinearMap.toMatrix' (standard 1).Jz = (1 / 2 : ℂ) • pauliMatrix (Sum.inr 2)
```

**`PhyslibAlpha.Sl2.toMatrix'_standard_one_Jp`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinHalf.lean#L85).

> The raising operator `J₊ = Jx + i Jy` of spin ½ is `σ₊ = (σ₁ + i σ₂) / 2 = |↑⟩⟨↓|`.

```lean
lemma toMatrix'_standard_one_Jp : LinearMap.toMatrix' (standard 1).Jp = !![0, 1; 0, 0]
```

**`PhyslibAlpha.Sl2.toMatrix'_standard_one_Jm`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinHalf.lean#L91).

> The lowering operator `J₋ = Jx - i Jy` of spin ½ is `σ₋ = (σ₁ - i σ₂) / 2 = |↓⟩⟨↑|`.

```lean
lemma toMatrix'_standard_one_Jm : LinearMap.toMatrix' (standard 1).Jm = !![0, 0; 1, 0]
```

## B. The normalised basis

**`PhyslibAlpha.Sl2.normVec_one_zero`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinHalf.lean#L103).

> The normalised state `|½, ½⟩ = normVec 1 0` is the basis vector `v 0`.

```lean
lemma normVec_one_zero : normVec 1 0 = v 0
```

**`PhyslibAlpha.Sl2.normVec_one_one`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinHalf.lean#L107).

> The normalised state `|½, -½⟩ = normVec 1 1` is the basis vector `v 1`.

```lean
lemma normVec_one_one : normVec 1 1 = v 1
```

## Depends on

- [Physlib.Relativity.PauliMatrices.Basic](../../../../physlib/relativity/paulimatrices/basic.md)
- [Addition of angular momenta](addition.md)
- [The invariant form and the normalised basis of the standard modules](normalizedbasis.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinHalf.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinHalf.lean)
