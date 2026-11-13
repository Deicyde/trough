---
declaration: module
origin: cited
lean: QED.sum_eta_inv_inv, QED.pauliSelfAdjoint'_coe, QED.kineticGamma_eq_fromBlocks_pauliSelfAdjoint', QED.sl2c_conj_pauliSelfAdjoint', QED.sum_fromBlocks, QED.sum_lorentz_inv_conjTranspose_pauli_conj, QED.sum_lorentz_inv_eta_pauli_conj, QED.sum_lorentz_inv_spinorRep_kineticGamma
statement: formalized
proof: formalized
---

# Lorentz invariance of quantum electrodynamics

The module `PhyslibAlpha.Particles.QED.LorentzInvariance`, [PhyslibAlpha/Particles/QED/LorentzInvariance.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean): 24 declarations, 22 with a docstring.

## i. Overview

> The Lorentz-theoretic theorems of QED, culminating in the Lorentz invariance
> of the QED Lagrangian, `lorentzAction_lagrangian`.  The chain of results:
>
> * the covering map `Lorentz.SL2C.toLorentzGroup` intertwines the conjugation
>   of the covariant Pauli matrices with the Lorentz transformation of their
>   index; combined with the defining property `Λ η Λᵀ = η` of the Lorentz
>   group this yields the two contraction identities of the spinor
>   representation (`sum_lorentz_inv_conjTranspose_pauli_conj` and
>   `sum_lorentz_inv_eta_pauli_conj`), which assemble block-diagonally into
>   the contraction identity of the kinetic matrices `γ⁰ γ^μ`
>   (`sum_kineticGamma_contraction`);
> * the jet coordinates of QED transform as tensors and spinors
>   (`lorentzAction_A_zero`, `lorentzAction_ψ_singleton`, …), and the covariant
>   derivative transforms exactly like the first-order jet
>   (`lorentzAction_covDψ`);
> * the Maxwell term is invariant because `Λ⁻¹ η (Λ⁻¹)ᵀ = η`
>   (`Photon.JetAlgebra.lorentzAction_maxwellTerm`), the mass term because the
>   spinor representation preserves `γ⁰`
>   (`spinorRep_conjTranspose_gammaZero_spinorRep`), and the kinetic term by
>   the contraction identity;
> * the Lagrangian, being built from invariant pieces, is invariant
>   (`lorentzAction_lagrangian`).
>
> This file contains no definitions, only theorems about the jet algebras of
> `PhyslibAlpha.Particles.QED.Basic`, the fields of `PhyslibAlpha.Particles.QED.Fields`
> and the Lagrangian of
> `PhyslibAlpha.Particles.QED.Lagrangian`.

## ii. Key results

> - `sum_kineticGamma_contraction` : the Lorentz contraction identity of the
>   matrices `γ⁰ γ^μ` under the spinor representation.
> - `spinorRep_conjTranspose_gammaZero_spinorRep` : the spinor representation
>   preserves `γ⁰`.
> - `JetAlgebra.lorentzAction_A_zero`, `JetAlgebra.lorentzAction_ψ_zero`,
>   `JetAlgebra.lorentzAction_ψ_singleton`, … : the transformation laws of the
>   jet coordinates.
> - `JetAlgebra.lorentzAction_covDψ` : Lorentz covariance of the covariant
>   derivative.
> - `Photon.JetAlgebra.lorentzAction_maxwellTerm`,
>   `JetAlgebra.lorentzAction_maxwellTerm` : Lorentz invariance of the Maxwell
>   term.
> - `JetAlgebra.lorentzAction_electronMassTerm`,
>   `JetAlgebra.lorentzAction_diracKineticTerm` : Lorentz invariance of the
>   fermionic terms.
> - `JetAlgebra.lorentzAction_lagrangian` : **Lorentz invariance of the QED
>   Lagrangian**.

## iv. References

> The Lorentz actions are defined in `PhyslibAlpha.Particles.QED.Basic`; the corresponding
> machinery for the lepton–gauge sector is
> `Physlib.Particles.LeptonGaugeSector.JetAlgebra.LorentzAction`.

## A. Contractions of the Minkowski metric with a Lorentz transformation

**`QED.sum_eta_inv_inv`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L102).

> The defining property of the Lorentz group in index form: contracting two
> rows of `Λ⁻¹` with the Minkowski metric reproduces the metric.

```lean
lemma sum_eta_inv_inv (Λ : LorentzGroup 3) (τ τ' : Fin 1 ⊕ Fin 3) :
    ∑ μ, η μ μ * ((Λ⁻¹).1 τ μ * (Λ⁻¹).1 τ' μ) = η τ τ'
```

## B. The intertwining identities of the spinor representation

### B.1. Conjugation of the covariant Pauli matrices

**`QED.pauliSelfAdjoint'_coe`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L122).

> The covariant Pauli matrices are `σ̄^μ = η_{μμ} σ^μ` (no sum).

```lean
lemma pauliSelfAdjoint'_coe (μ : Fin 1 ⊕ Fin 3) :
    (PauliMatrix.pauliSelfAdjoint' μ).1 = η μ μ • σ μ
```

**`QED.kineticGamma_eq_fromBlocks_pauliSelfAdjoint'`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L128).

> The kinetic matrices through the covariant Pauli matrices:
> `γ⁰ γ^μ = ((σ̄^μ, 0), (0, η_{μμ} σ̄^μ))`.

```lean
lemma kineticGamma_eq_fromBlocks_pauliSelfAdjoint' (μ : Fin 1 ⊕ Fin 3) :
    JetAlgebra.kineticGamma μ =
      Matrix.fromBlocks (PauliMatrix.pauliSelfAdjoint' μ).1 0 0
        (η μ μ • (PauliMatrix.pauliSelfAdjoint' μ).1)
```

**`QED.sl2c_conj_pauliSelfAdjoint'`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L138).

> Conjugating a covariant Pauli matrix by `N : SL(2,ℂ)` transforms its
> index by the image of `N` in the Lorentz group; this is the defining
> property of the covering map.

```lean
lemma sl2c_conj_pauliSelfAdjoint' (N : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) :
    N.1 * (PauliMatrix.pauliSelfAdjoint' μ).1 * N.1ᴴ =
      ∑ ν, (Lorentz.SL2C.toLorentzGroup N).1 ν μ •
        (PauliMatrix.pauliSelfAdjoint' ν).1
```

**`QED.sum_fromBlocks`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L147).

> A block matrix summed over the diagonal blocks.

```lean
lemma sum_fromBlocks {ι : Type*} (s : Finset ι)
    (A : ι → Matrix (Fin 2) (Fin 2) ℂ) (D : ι → Matrix (Fin 2) (Fin 2) ℂ) :
    ∑ i ∈ s, Matrix.fromBlocks (A i) 0 0 (D i) =
      Matrix.fromBlocks (∑ i ∈ s, A i) 0 0 (∑ i ∈ s, D i)
```

### B.2. The two block identities

> The left Weyl block: transporting the index of `σ̄^μ` with `Λ(M)⁻¹` cancels
> the conjugation by `M`, through `Λ(M†) = Λ(M)ᵀ`.

**`QED.sum_lorentz_inv_conjTranspose_pauli_conj`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L166).

```lean
lemma sum_lorentz_inv_conjTranspose_pauli_conj (M : SL(2,ℂ)) (τ : Fin 1 ⊕ Fin 3) :
    ∑ μ, ((Lorentz.SL2C.toLorentzGroup M)⁻¹).1 τ μ •
        (M.1ᴴ * (PauliMatrix.pauliSelfAdjoint' μ).1 * M.1) =
      (PauliMatrix.pauliSelfAdjoint' τ).1
```

**`QED.sum_lorentz_inv_eta_pauli_conj`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L201).

> The right Weyl block: transporting the index of `η_{μμ} σ̄^μ` with
> `Λ(M)⁻¹` cancels the conjugation by `(M⁻¹)†`, through `Λ⁻¹ η (Λ⁻¹)ᵀ = η`.

```lean
lemma sum_lorentz_inv_eta_pauli_conj (M : SL(2,ℂ)) (τ : Fin 1 ⊕ Fin 3) :
    ∑ μ, (((Lorentz.SL2C.toLorentzGroup M)⁻¹).1 τ μ * η μ μ) •
        ((M⁻¹).1 * (PauliMatrix.pauliSelfAdjoint' μ).1 * ((M⁻¹).1)ᴴ) =
      η τ τ • (PauliMatrix.pauliSelfAdjoint' τ).1
```

### B.3. The contraction identity of the kinetic matrices

**`QED.sum_lorentz_inv_spinorRep_kineticGamma`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L238).

> The matrix form of the contraction identity: transporting the vector index
> of `γ⁰ γ^μ` with `Λ(M)⁻¹` cancels the conjugation by the spinor
> representation.

```lean
lemma sum_lorentz_inv_spinorRep_kineticGamma (M : SL(2,ℂ)) (τ : Fin 1 ⊕ Fin 3) :
    ∑ μ, ((Lorentz.SL2C.toLorentzGroup M)⁻¹).1 τ μ •
        ((Electron.JetAlgebra.spinorRep M)ᴴ * JetAlgebra.kineticGamma μ *
          Electron.JetAlgebra.spinorRep M) =
      JetAlgebra.kineticGamma τ
```

**`QED.sum_kineticGamma_contraction`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L263).

> **The contraction identity of the Dirac kinetic term**: the index form of
> `∑_μ (Λ⁻¹)_{τμ} S(M)† (γ⁰ γ^μ) S(M) = γ⁰ γ^τ`.  This is the identity that
> makes `i ψ̄ γ^μ D_μ ψ` a Lorentz scalar.

```lean
lemma sum_kineticGamma_contraction (M : SL(2,ℂ)) (τ : Fin 1 ⊕ Fin 3)
    (α' β' : Fin 2 ⊕ Fin 2) :
    ∑ μ, ∑ α, ∑ β, JetAlgebra.kineticGamma μ α β *
        (star (Electron.JetAlgebra.spinorRep M α α') *
          (((((Lorentz.SL2C.toLorentzGroup M)⁻¹).1 τ μ : ℝ) : ℂ) *
            Electron.JetAlgebra.spinorRep M β β')) =
      JetAlgebra.kineticGamma τ α' β'
```

### B.4. The spinor representation preserves `γ⁰`

**`QED.spinorRep_conjTranspose_gammaZero_spinorRep`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L290).

> The spinor representation preserves `γ⁰`: `S(M)† γ⁰ S(M) = γ⁰`.  This is
> the identity that makes the Dirac mass term `m ψ̄ ψ` a Lorentz scalar.

```lean
lemma spinorRep_conjTranspose_gammaZero_spinorRep (M : SL(2,ℂ)) :
    (Electron.JetAlgebra.spinorRep M)ᴴ * JetAlgebra.gammaMatrix (Sum.inl 0) *
      Electron.JetAlgebra.spinorRep M = JetAlgebra.gammaMatrix (Sum.inl 0)
```

**`QED.sum_gammaZero_contraction`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L308).

> The index form of `S(M)† γ⁰ S(M) = γ⁰`.

```lean
lemma sum_gammaZero_contraction (M : SL(2,ℂ)) (α' β' : Fin 2 ⊕ Fin 2) :
    ∑ α, ∑ β, JetAlgebra.gammaMatrix (Sum.inl 0) α β *
        (star (Electron.JetAlgebra.spinorRep M α α') *
          Electron.JetAlgebra.spinorRep M β β') =
      JetAlgebra.gammaMatrix (Sum.inl 0) α' β'
```

## C. The transformation laws of the jet coordinates

**`QED.JetAlgebra.lorentzAction_A_zero`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L331).

> The photon jet coordinate transforms as a covector.

```lean
lemma lorentzAction_A_zero (M : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) :
    lorentzAction M (A 0 μ) =
      ∑ ν, ((((Lorentz.SL2C.toLorentzGroup M)⁻¹).1 ν μ : ℝ) : ℂ) • A 0 ν
```

**`QED.JetAlgebra.lorentzAction_A_singleton`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L341).

> The first-order photon jet coordinate transforms as a two-tensor.

```lean
lemma lorentzAction_A_singleton (M : SL(2,ℂ)) (ρ μ : Fin 1 ⊕ Fin 3) :
    lorentzAction M (A {ρ} μ) =
      ∑ τ, ∑ ν, ((((Lorentz.SL2C.toLorentzGroup M)⁻¹).1 τ ρ *
          ((Lorentz.SL2C.toLorentzGroup M)⁻¹).1 ν μ : ℝ) : ℂ) • A {τ} ν
```

**`QED.JetAlgebra.lorentzAction_ψ_zero`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L355).

> The electron jet coordinate transforms in the spinor representation.

```lean
lemma lorentzAction_ψ_zero (M : SL(2,ℂ)) (α : Fin 2 ⊕ Fin 2) :
    lorentzAction M (ψ 0 α) =
      ∑ β, Electron.JetAlgebra.spinorRep M α β • ψ 0 β
```

**`QED.JetAlgebra.lorentzAction_barψ_zero`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L366).

> The conjugate electron jet coordinate transforms in the conjugate spinor
> representation.

```lean
lemma lorentzAction_barψ_zero (M : SL(2,ℂ)) (α : Fin 2 ⊕ Fin 2) :
    lorentzAction M (barψ 0 α) =
      ∑ β, star (Electron.JetAlgebra.spinorRep M α β) • barψ 0 β
```

**`QED.JetAlgebra.lorentzAction_ψ_singleton`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L377).

> The first-order electron jet coordinate transforms as a spinor with a
> covector derivative index.

```lean
lemma lorentzAction_ψ_singleton (M : SL(2,ℂ)) (ρ : Fin 1 ⊕ Fin 3)
    (α : Fin 2 ⊕ Fin 2) :
    lorentzAction M (ψ {ρ} α) =
      ∑ τ, ∑ β, (((((Lorentz.SL2C.toLorentzGroup M)⁻¹).1 τ ρ : ℝ) : ℂ) *
          Electron.JetAlgebra.spinorRep M α β) • ψ {τ} β
```

**`QED.JetAlgebra.lorentzAction_barψ_singleton`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L390).

```lean
lemma lorentzAction_barψ_singleton (M : SL(2,ℂ)) (ρ : Fin 1 ⊕ Fin 3)
    (α : Fin 2 ⊕ Fin 2) :
    lorentzAction M (barψ {ρ} α) =
      ∑ τ, ∑ β, (((((Lorentz.SL2C.toLorentzGroup M)⁻¹).1 τ ρ : ℝ) : ℂ) *
          star (Electron.JetAlgebra.spinorRep M α β)) • barψ {τ} β
```

## D. Lorentz invariance of the Maxwell term

**`QED.Photon.JetAlgebra.lorentzAction_fieldStrength_zero`**, a lemma, [line 416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L416).

> The formal field strength transforms as an antisymmetric two-tensor.

```lean
lemma lorentzAction_fieldStrength_zero (Λ : LorentzGroup 3) (μ ν : Fin 1 ⊕ Fin 3) :
    lorentzAction Λ (fieldStrength 0 μ ν) =
      ∑ a, ∑ b, ((Λ⁻¹).1 a μ * (Λ⁻¹).1 b ν) • fieldStrength 0 a b
```

**`QED.Photon.JetAlgebra.lorentzAction_maxwellTerm`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L434).

> **Lorentz invariance of the Maxwell term** in the photon jet algebra:
> the two metric contractions absorb the four transformation matrices through
> `Λ⁻¹ η (Λ⁻¹)ᵀ = η`.

```lean
lemma lorentzAction_maxwellTerm (Λ : LorentzGroup 3) :
    lorentzAction Λ maxwellTerm = maxwellTerm
```

**`QED.JetAlgebra.lorentzAction_maxwellTerm`**, a lemma, [line 498](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L498).

> **Lorentz invariance of the Maxwell term** in the QED jet algebra,
> inherited from the photon jet algebra.

```lean
lemma lorentzAction_maxwellTerm (M : SL(2,ℂ)) :
    lorentzAction M maxwellTerm = maxwellTerm
```

## E. Lorentz covariance of the covariant derivative

**`QED.JetAlgebra.lorentzAction_covDψ`**, a lemma, [line 512](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L512).

> The covariant derivative transforms exactly like the first-order jet
> coordinate: as a spinor with a covector derivative index.

```lean
lemma lorentzAction_covDψ (M : SL(2,ℂ)) (e : ℝ) (μ : Fin 1 ⊕ Fin 3)
    (β : Fin 2 ⊕ Fin 2) :
    lorentzAction M (covDψ e μ β) =
      ∑ τ, ∑ β', (((((Lorentz.SL2C.toLorentzGroup M)⁻¹).1 τ μ : ℝ) : ℂ) *
        Electron.JetAlgebra.spinorRep M β β') • covDψ e τ β'
```

## F. Lorentz invariance of the fermionic terms

**`QED.JetAlgebra.lorentzAction_electronMassTerm`**, a lemma, [line 535](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L535).

> **Lorentz invariance of the Dirac mass term**: the spinor phases of the
> electron and its conjugate cancel through `S(M)† γ⁰ S(M) = γ⁰`.

```lean
lemma lorentzAction_electronMassTerm (M : SL(2,ℂ)) :
    lorentzAction M electronMassTerm = electronMassTerm
```

**`QED.JetAlgebra.lorentzAction_diracKineticTerm`**, a lemma, [line 559](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L559).

> **Lorentz invariance of the Dirac kinetic term**: the transformation of
> the two spinor slots and the derivative slot cancels through the contraction
> identity of the matrices `γ⁰ γ^μ`.

```lean
lemma lorentzAction_diracKineticTerm (M : SL(2,ℂ)) (e : ℝ) :
    lorentzAction M (diracKineticTerm e) = diracKineticTerm e
```

## G. Lorentz invariance of the QED Lagrangian

**`QED.JetAlgebra.lorentzAction_lagrangian`**, a lemma, [line 599](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean#L599).

> **Lorentz invariance of the QED Lagrangian.**  The Maxwell term is
> invariant through `Λ⁻¹ η (Λ⁻¹)ᵀ = η`, the kinetic term through the
> contraction identity of `γ⁰ γ^μ` under the spinor representation, and the
> mass term through `S(M)† γ⁰ S(M) = γ⁰`.

```lean
lemma lorentzAction_lagrangian (M : SL(2,ℂ)) (e m : ℝ) :
    lorentzAction M (lagrangian e m) = lagrangian e m
```

## Depends on

- [The QED Lagrangian](lagrangian.md)

## Proof depends on

- [Properties of the γ matrices](gammamatrices.md)
- [Gauge invariance of quantum electrodynamics](gaugeinvariance.md)
- [Conjugation and the kernel of the covering map](../../relativity/sl2c/basic.md)

## Sources

- [PhyslibAlpha/Particles/QED/LorentzInvariance.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/LorentzInvariance.lean)
