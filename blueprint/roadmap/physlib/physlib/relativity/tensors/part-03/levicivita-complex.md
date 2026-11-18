---
declaration: module
origin: cited
lean: complexLorentzTensor.leviCivita_isReindexing, complexLorentzTensor.leviCivita, complexLorentzTensor.leviCivita_eq_ofGaussianInt, complexLorentzTensor.leviCivita_eq_ofGaussianInt_prod
statement: formalized
proof: formalized
---

# The Levi-Civita tensor as a complex Lorentz tensor

The module `Physlib.Relativity.Tensors.LeviCivita.Complex`, [Physlib/Relativity/Tensors/LeviCivita/Complex.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Complex.lean): 4 declarations, 4 with a docstring.

> This file complexifies the real Lorentz Levi-Civita tensor and records its components in the
> Gaussian integer tensor basis.

## A. Definition and components

**`complexLorentzTensor.leviCivita_isReindexing`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Complex.lean#L39).

> The index colors of the complexified real Levi-Civita tensor agree with four complex
> contravariant Lorentz indices.

```lean
lemma leviCivita_isReindexing : IsReindexing
    (realLorentzTensor.colorToComplex ∘
      ![realLorentzTensor.Color.up, realLorentzTensor.Color.up,
        realLorentzTensor.Color.up, realLorentzTensor.Color.up])
    ![Color.up, Color.up, Color.up, Color.up] id
```

**`complexLorentzTensor.leviCivita`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Complex.lean#L47).

> The Levi-Civita tensor `εᵘᵛᵖᵟ` as a complex Lorentz tensor, with `ε⁰¹²³ = 1`.

```lean
noncomputable def leviCivita : ℂT[.up, .up, .up, .up]
```

**`complexLorentzTensor.leviCivita_eq_ofGaussianInt`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Complex.lean#L56).

> The complex Levi-Civita tensor has the Levi-Civita symbol as its real component and zero
> imaginary component in the standard basis.

```lean
lemma leviCivita_eq_ofGaussianInt : ε4ℂ = ofGaussianInt (fun
    b : ComponentIdx (S := complexLorentzTensor) ![Color.up, Color.up, Color.up, Color.up] =>
    (generalizedKroneckerDelta
      (fun i => finSumFinEquiv (basisIdxCongr (c1 := Color.up) (by fin_cases i <;> rfl) (b i)))
      (id : Fin 4 → Fin 4) : GaussianInt))
```

**`complexLorentzTensor.leviCivita_eq_ofGaussianInt_prod`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Complex.lean#L100).

> The components of the complex Levi-Civita tensor as the product over pairs `i < j` of the
> sign of `b j - b i`, from `leviCivitaSymbol_eq_prod_prod_Ioi`. Unlike the determinant appearing
> in `leviCivita_eq_ofGaussianInt`, these components are cheap to evaluate, e.g. by `decide`.

```lean
lemma leviCivita_eq_ofGaussianInt_prod : ε4ℂ = ofGaussianInt (fun
    b : ComponentIdx (S := complexLorentzTensor) ![Color.up, Color.up, Color.up, Color.up] =>
    (((∏ i : Fin 4, ∏ j ∈ Finset.Ioi i,
      (if finSumFinEquiv (basisIdxCongr (c1 := Color.up) (by fin_cases i <;> rfl) (b i)) <
          finSumFinEquiv (basisIdxCongr (c1 := Color.up) (by fin_cases j <;> rfl) (b j)) then 1
        else if finSumFinEquiv (basisIdxCongr (c1 := Color.up) (by fin_cases i <;> rfl) (b i)) =
          finSumFinEquiv (basisIdxCongr (c1 := Color.up) (by fin_cases j <;> rfl) (b j))
        then 0 else -1) : ℤ) :
      GaussianInt)))
```

## Depends on

- [Complex Lorentz tensors with Gaussian integer components](../part-01/complextensor-ofgaussianint.md)
- [The Levi-Civita tensor as a real Lorentz tensor](levicivita-basic.md)
- [Complex Lorentz tensors from real Lorentz tensors](realtensor-tocomplex.md)

## Sources

- [Physlib/Relativity/Tensors/LeviCivita/Complex.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Complex.lean)
