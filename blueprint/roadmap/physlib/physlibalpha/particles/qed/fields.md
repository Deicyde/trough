---
declaration: module
origin: cited
lean: QED.Photon.JetAlgebra.fieldStrength, QED.Photon.JetAlgebra.maxwellTerm, QED.Photon.JetAlgebra.maxwellOperator, QED.JetAlgebra.A, QED.JetAlgebra.ψ, QED.JetAlgebra.barψ, QED.JetAlgebra.fieldStrength, QED.JetAlgebra.maxwellTerm
statement: formalized
proof: formalized
---

# The fields of quantum electrodynamics

The module `PhyslibAlpha.Particles.QED.Fields`, [PhyslibAlpha/Particles/QED/Fields.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Fields.lean): 12 declarations, 12 with a docstring.

## i. Overview

> The fields of QED, defined on top of the jet algebras of `PhyslibAlpha.Particles.QED.Basic`:
> the photon and electron jet coordinates as elements of the QED jet algebra,
> the field strength, the Maxwell term, the Dirac γ matrices in the chiral
> representation, and the covariant derivatives of the electron and its
> conjugate.
>
> This file contains only definitions; the theorems about these fields are
> proved in `PhyslibAlpha.Particles.QED.FermionStatistics`,
> `PhyslibAlpha.Particles.QED.FieldStrength`,
> `PhyslibAlpha.Particles.QED.GammaMatrices`, `PhyslibAlpha.Particles.QED.GaugeInvariance` and
> `PhyslibAlpha.Particles.QED.Evaluation`, and the Lagrangian built from them is defined in
> `PhyslibAlpha.Particles.QED.Lagrangian`.

## ii. Key results

> - `Photon.JetAlgebra.fieldStrength`, `Photon.JetAlgebra.maxwellTerm` : the
>   field strength and the Maxwell term in the photon jet algebra.
> - `JetAlgebra.A`, `JetAlgebra.ψ`, `JetAlgebra.barψ` : the jet coordinates of
>   QED.
> - `JetAlgebra.fieldStrength`, `JetAlgebra.maxwellTerm` : the field strength
>   and the Maxwell term in the QED jet algebra.
> - `JetAlgebra.gammaMatrix`, `JetAlgebra.kineticGamma` : the γ matrices in the
>   chiral representation and the contraction matrices `γ⁰ γ^μ`.
> - `JetAlgebra.covDψ`, `JetAlgebra.covDbarψ` : the covariant derivatives.

## iv. References

> The jet algebras are defined in `PhyslibAlpha.Particles.QED.Basic`; the Lagrangian is
> defined in `PhyslibAlpha.Particles.QED.Lagrangian`.

## A. The field strength and Maxwell term of the photon

**`QED.Photon.JetAlgebra.fieldStrength`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Fields.lean#L71).

> The formal field strength `∂_s F_{μν} = ∂_s ∂_μ A_ν - ∂_s ∂_ν A_μ`.

```lean
noncomputable def fieldStrength (s : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    JetAlgebra
```

**`QED.Photon.JetAlgebra.maxwellTerm`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Fields.lean#L77).

> The formal Maxwell term `F_{μν} F^{μν}`, both indices raised with the
> (diagonal) Minkowski metric.

```lean
noncomputable def maxwellTerm : JetAlgebra
```

**`QED.Photon.JetAlgebra.maxwellOperator`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Fields.lean#L84).

> The Maxwell operator `∂_μ F^{μν}`: the divergence of the field strength
> with raised indices.  Its vanishing is the vacuum Maxwell equation; its
> evaluation on an honest potential is the Euler–Lagrange gradient of the
> Maxwell action — see `PhyslibAlpha.Particles.QED.Evaluation`.

```lean
noncomputable def maxwellOperator (ν : Fin 1 ⊕ Fin 3) : JetAlgebra
```

## B. The jet coordinates of QED

> The photon jet coordinate `∂_s A_μ` and the electron jet coordinates
> `∂_s ψ_α`, `∂_s ψ̄_α`, as elements of the QED jet algebra, together with the
> field strength and the Maxwell term.

**`QED.JetAlgebra.A`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Fields.lean#L104).

> The photon jet coordinate `∂_s A_μ` in the QED jet algebra.

```lean
noncomputable def A (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    JetAlgebra
```

**`QED.JetAlgebra.ψ`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Fields.lean#L109).

> The electron jet coordinate `∂_s ψ_α` in the QED jet algebra.

```lean
noncomputable def ψ (s : Multiset (Fin 1 ⊕ Fin 3)) (α : Fin 2 ⊕ Fin 2) :
    JetAlgebra
```

**`QED.JetAlgebra.barψ`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Fields.lean#L114).

> The conjugate electron jet coordinate `∂_s ψ̄_α` in the QED jet algebra.

```lean
noncomputable def barψ (s : Multiset (Fin 1 ⊕ Fin 3)) (α : Fin 2 ⊕ Fin 2) :
    JetAlgebra
```

**`QED.JetAlgebra.fieldStrength`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Fields.lean#L119).

> The formal field strength `∂_s F_{μν}` in the QED jet algebra.

```lean
noncomputable def fieldStrength (s : Multiset (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) : JetAlgebra
```

**`QED.JetAlgebra.maxwellTerm`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Fields.lean#L126).

> The formal Maxwell term `F_{μν} F^{μν}` in the QED jet algebra.  Its
> evaluation on an honest electromagnetic potential is the Maxwell Lagrangian;
> see `PhyslibAlpha.Particles.QED.Evaluation`.

```lean
noncomputable def maxwellTerm : JetAlgebra
```

## C. The γ matrices in the chiral representation

> In the chiral representation `γ^μ = ((0, σ^μ), (σ̄^μ, 0))` with
> `σ^μ = (1, σ^i)` and `σ̄^μ = (1, -σ^i)`; since the Minkowski matrix is
> diagonal, `σ̄^μ = η_{μμ} σ^μ` with no sum over `μ`.

**`QED.JetAlgebra.gammaMatrix`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Fields.lean#L142).

> The Dirac γ matrices in the chiral (Weyl) representation:
> `γ^μ = ((0, σ^μ), (σ̄^μ, 0))`, acting on the Dirac index `Fin 2 ⊕ Fin 2`
> whose summands are the left- and right-handed Weyl components.

```lean
noncomputable def gammaMatrix (μ : Fin 1 ⊕ Fin 3) :
    Matrix (Fin 2 ⊕ Fin 2) (Fin 2 ⊕ Fin 2) ℂ
```

**`QED.JetAlgebra.kineticGamma`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Fields.lean#L149).

> The contraction matrices `γ⁰ γ^μ = ((σ̄^μ, 0), (0, σ^μ))` of the Dirac
> kinetic term `i ψ† (γ⁰ γ^μ) D_μ ψ`; see
> `Physlib.Particles.QED.GammaMatrices.kineticGamma_eq_gammaMatrix_mul`.

```lean
noncomputable def kineticGamma (μ : Fin 1 ⊕ Fin 3) :
    Matrix (Fin 2 ⊕ Fin 2) (Fin 2 ⊕ Fin 2) ℂ
```

## D. The covariant derivatives

> The electron has electric charge `-1`, so `D_μ ψ = ∂_μ ψ + i e A_μ ψ` and
> `D_μ ψ̄ = ∂_μ ψ̄ - i e A_μ ψ̄`, with `e` the electric coupling.

**`QED.JetAlgebra.covDψ`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Fields.lean#L164).

> The covariant derivative jet `(D_μ ψ)_α = ∂_μ ψ_α + i e A_μ ψ_α` of the
> electron.

```lean
noncomputable def covDψ (e : ℝ) (μ : Fin 1 ⊕ Fin 3) (α : Fin 2 ⊕ Fin 2) :
    JetAlgebra
```

**`QED.JetAlgebra.covDbarψ`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Fields.lean#L170).

> The covariant derivative jet `(D_μ ψ̄)_α = ∂_μ ψ̄_α - i e A_μ ψ̄_α` of the
> conjugate electron.

```lean
noncomputable def covDbarψ (e : ℝ) (μ : Fin 1 ⊕ Fin 3) (α : Fin 2 ⊕ Fin 2) :
    JetAlgebra
```

## Depends on

- [The jet algebras of quantum electrodynamics](basic.md)

## Sources

- [PhyslibAlpha/Particles/QED/Fields.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Fields.lean)
