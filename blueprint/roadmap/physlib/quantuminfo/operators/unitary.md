---
declaration: module
origin: cited
lean: MState.uConj_spectrum_eq, MState.no_cloning, MState.uConj, MState.inner_uConj
statement: formalized
proof: formalized
---

# Unitary operators on quantum state

The module `QuantumInfo.Operators.Unitary`, [QuantumInfo/Operators/Unitary.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Operators/Unitary.lean): 4 declarations, 3 with a docstring, 2 listed as significant.

> This file is intended for lemmas about unitary matrices (`Matrix.unitaryGroup`) and how they
> apply to `Bra`s, `Ket`s, and `MState` mixed states.
>
> This is imported by `CPTPMap` to define things like unitary channels, Kraus operators, and
> complementary channels, so this file itself does not discuss channels yet.

**`MState.uConj`**, a def, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Operators/Unitary.lean#L33).

> Conjugate a state by a unitary matrix (applying the unitary as an evolution).

```lean
def uConj (ρ : MState d) (U : 𝐔[d]) : MState d
```

**`MState.uConj_spectrum_eq`**, a theorem, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Operators/Unitary.lean#L49). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> You might think this should only be true up to permutation, so that it would read like
> `∃ σ : Equiv.Perm d, (ρ.uConj U).spectrum = ρ.spectrum.relabel σ`. But since eigenvalues
> of a matrix are always canonically sorted, this is actually an equality.

```lean
theorem uConj_spectrum_eq (ρ : MState d) (U : 𝐔[d]) :
    (ρ.uConj U).spectrum = ρ.spectrum
```

**`MState.inner_uConj`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Operators/Unitary.lean#L54).

```lean
lemma inner_uConj (ρ σ : MState d) (U : 𝐔[d]) : ⟪U ◃ ρ, U ◃ σ⟫_Prob = ⟪ρ, σ⟫_Prob
```

**`MState.no_cloning`**, a theorem, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Operators/Unitary.lean#L61). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The **No-cloning theorem**, saying that if states `ψ` and `φ` can both be perfectly cloned
> using a unitary `U` and a fiducial state `f`, and they aren't identical (their inner product is
> less than 1), then the two states must be orthogonal to begin with. In short: only orthogonal
> states can be simultaneously cloned.

```lean
theorem no_cloning {U : 𝐔[d × d]}
    (hψ : U ◃ pure (ψ ⊗ᵠ f) = pure (ψ ⊗ᵠ ψ))
    (hφ : U ◃ pure (φ ⊗ᵠ f) = pure (φ ⊗ᵠ φ))
    (H : ⟪pure ψ, pure φ⟫_Prob < (1 : ℝ)) :
    ⟪pure ψ, pure φ⟫_Prob = (0 : ℝ)
```

## Depends on

- [QuantumInfo.States.Mixed.MState](../states/mixed/mstate.md)

## Sources

- [QuantumInfo/Operators/Unitary.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Operators/Unitary.lean)
