---
declaration: module
origin: cited
lean: QED.JetAlgebra.pauliMatrix_mul_smul_add_swap, QED.JetAlgebra.smul_pauliMatrix_mul_add_swap, QED.JetAlgebra.gammaMatrix_mul_add_swap, QED.JetAlgebra.gammaMatrix_sq, QED.JetAlgebra.gammaMatrix_anticommute, QED.JetAlgebra.gammaMatrix_inl_zero, QED.JetAlgebra.kineticGamma_eq_gammaMatrix_mul, QED.JetAlgebra.kineticGamma_conjTranspose
statement: formalized
proof: formalized
---

# Properties of the γ matrices

The module `PhyslibAlpha.Particles.QED.GammaMatrices`, [PhyslibAlpha/Particles/QED/GammaMatrices.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GammaMatrices.lean): 10 declarations, 8 with a docstring.

## i. Overview

> The defining properties of the Dirac γ matrices of `PhyslibAlpha.Particles.QED.Fields`, in
> the chiral representation:
>
> * the **Clifford algebra relation** `γ^μ γ^ν + γ^ν γ^μ = 2 η^{μν} 1`, which
>   makes the Dirac operator a square root of the wave operator;
> * the hermiticity properties `(γ⁰ γ^μ)† = γ⁰ γ^μ` and
>   `(γ^μ)† = γ⁰ γ^μ γ⁰`, which make the Dirac Lagrangian hermitian;
> * the factorisation `γ⁰ γ^μ` of the contraction matrices of the kinetic term.
>
> This file contains no definitions, only theorems about the fields of
> `PhyslibAlpha.Particles.QED.Fields`.

## ii. Key results

> - `JetAlgebra.gammaMatrix_mul_add_swap` : **the Clifford algebra relation**.
> - `JetAlgebra.kineticGamma_eq_gammaMatrix_mul` : the contraction matrices of
>   the kinetic term are `γ⁰ γ^μ`.
> - `JetAlgebra.kineticGamma_conjTranspose` : the contraction matrices are
>   self-adjoint.
> - `JetAlgebra.gammaMatrix_conjTranspose` : `(γ^μ)† = γ⁰ γ^μ γ⁰`.

## iv. References

> The γ matrices are defined in `PhyslibAlpha.Particles.QED.Fields`; the Pauli matrices are
> those of `Physlib.Relativity.PauliMatrices`.

## A. The Pauli anticommutators

> The two block identities behind the Clifford relation:
> `σ^μ σ̄^ν + σ^ν σ̄^μ = 2 η^{μν} 1` and `σ̄^μ σ^ν + σ̄^ν σ^μ = 2 η^{μν} 1`,
> with `σ̄^μ = η_{μμ} σ^μ` (no sum).  Both reduce to the anticommutation
> relations of the Pauli matrices.

**`QED.JetAlgebra.pauliMatrix_mul_smul_add_swap`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GammaMatrices.lean#L68).

```lean
lemma pauliMatrix_mul_smul_add_swap (μ ν : Fin 1 ⊕ Fin 3) :
    σ μ * (η ν ν • σ ν) + σ ν * (η μ μ • σ μ) =
      (2 * η μ ν) • (1 : Matrix (Fin 2) (Fin 2) ℂ)
```

**`QED.JetAlgebra.smul_pauliMatrix_mul_add_swap`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GammaMatrices.lean#L75).

```lean
lemma smul_pauliMatrix_mul_add_swap (μ ν : Fin 1 ⊕ Fin 3) :
    (η μ μ • σ μ) * σ ν + (η ν ν • σ ν) * σ μ =
      (2 * η μ ν) • (1 : Matrix (Fin 2) (Fin 2) ℂ)
```

## B. The Clifford algebra relation

**`QED.JetAlgebra.gammaMatrix_mul_add_swap`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GammaMatrices.lean#L92).

> **The Clifford algebra relation** of the Dirac γ matrices:
> `γ^μ γ^ν + γ^ν γ^μ = 2 η^{μν} 1`.  This is the algebraic identity that
> makes the Dirac operator a square root of the wave operator, and hence the
> Dirac equation relativistic.

```lean
lemma gammaMatrix_mul_add_swap (μ ν : Fin 1 ⊕ Fin 3) :
    gammaMatrix μ * gammaMatrix ν + gammaMatrix ν * gammaMatrix μ =
      (2 * η μ ν) • (1 : Matrix (Fin 2 ⊕ Fin 2) (Fin 2 ⊕ Fin 2) ℂ)
```

**`QED.JetAlgebra.gammaMatrix_sq`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GammaMatrices.lean#L107).

> The square of a γ matrix: `(γ^μ)² = η^{μμ} 1` (no sum).

```lean
lemma gammaMatrix_sq (μ : Fin 1 ⊕ Fin 3) :
    gammaMatrix μ * gammaMatrix μ =
      (η μ μ) • (1 : Matrix (Fin 2 ⊕ Fin 2) (Fin 2 ⊕ Fin 2) ℂ)
```

**`QED.JetAlgebra.gammaMatrix_anticommute`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GammaMatrices.lean#L117).

> The γ matrices of distinct indices anticommute.

```lean
lemma gammaMatrix_anticommute {μ ν : Fin 1 ⊕ Fin 3} (h : μ ≠ ν) :
    gammaMatrix μ * gammaMatrix ν = -(gammaMatrix ν * gammaMatrix μ)
```

## C. Hermiticity

**`QED.JetAlgebra.gammaMatrix_inl_zero`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GammaMatrices.lean#L131).

> `γ⁰` in the chiral representation is the block off-diagonal identity.

```lean
lemma gammaMatrix_inl_zero :
    gammaMatrix (Sum.inl 0) = Matrix.fromBlocks 0 1 1 0
```

**`QED.JetAlgebra.kineticGamma_eq_gammaMatrix_mul`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GammaMatrices.lean#L137).

> The contraction matrices of the kinetic term are `γ⁰ γ^μ`.

```lean
lemma kineticGamma_eq_gammaMatrix_mul (μ : Fin 1 ⊕ Fin 3) :
    kineticGamma μ = gammaMatrix (Sum.inl 0) * gammaMatrix μ
```

**`QED.JetAlgebra.kineticGamma_conjTranspose`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GammaMatrices.lean#L145).

> The contraction matrices `γ⁰ γ^μ` of the kinetic term are self-adjoint;
> this is what makes the Dirac kinetic term hermitian up to a total
> derivative.

```lean
lemma kineticGamma_conjTranspose (μ : Fin 1 ⊕ Fin 3) :
    (kineticGamma μ)ᴴ = kineticGamma μ
```

**`QED.JetAlgebra.gammaMatrix_zero_conjTranspose`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GammaMatrices.lean#L152).

> `γ⁰` is self-adjoint.

```lean
lemma gammaMatrix_zero_conjTranspose :
    (gammaMatrix (Sum.inl 0))ᴴ = gammaMatrix (Sum.inl 0)
```

**`QED.JetAlgebra.gammaMatrix_conjTranspose`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GammaMatrices.lean#L158).

> The hermiticity relation of the γ matrices, `(γ^μ)† = γ⁰ γ^μ γ⁰`.

```lean
lemma gammaMatrix_conjTranspose (μ : Fin 1 ⊕ Fin 3) :
    (gammaMatrix μ)ᴴ =
      gammaMatrix (Sum.inl 0) * gammaMatrix μ * gammaMatrix (Sum.inl 0)
```

## Depends on

- [The fields of quantum electrodynamics](fields.md)

## Sources

- [PhyslibAlpha/Particles/QED/GammaMatrices.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GammaMatrices.lean)
