---
declaration: module
origin: cited
lean: QED.Photon.JetAlgebra.massScale_fieldStrength_zero, QED.Photon.JetAlgebra.massScale_maxwellTerm, QED.JetAlgebra.massScale_A, QED.JetAlgebra.massScale_ψ, QED.JetAlgebra.massScale_barψ, QED.JetAlgebra.massScale_A_zero, QED.JetAlgebra.massScale_ψ_zero, QED.JetAlgebra.massScale_barψ_zero
statement: formalized
proof: formalized
---

# Mass dimensions in quantum electrodynamics

The module `PhyslibAlpha.Particles.QED.MassDimension`, [PhyslibAlpha/Particles/QED/MassDimension.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean): 18 declarations, 11 with a docstring.

## i. Overview

> The mass-dimension bookkeeping of QED, through the mass-weight scaling of
> `PhyslibAlpha.Particles.QED.Basic` (the algebra map multiplying each jet coordinate by `c`
> to twice its mass dimension): the photon has dimension one, the electron
> `3/2`, and each derivative adds one.  The theorems of this file identify the
> composite fields and the terms of the Lagrangian as eigenvectors of the
> scaling:
>
> * the covariant derivative `D_μ ψ` is homogeneous of weight five — this is
>   the statement that the electric coupling `e` is dimensionless, which is
>   what makes QED renormalizable;
> * the Maxwell term and the Dirac kinetic term have weight eight (mass
>   dimension four), and the mass term weight six (dimension three);
> * consequently `L(e, c² m)` scales to `c⁸ L(e, m)`: the Lagrangian has mass
>   dimension four with the electron mass a coefficient of dimension one.
>
> This file contains no definitions, only theorems.

## ii. Key results

> - `JetAlgebra.massScale_A_zero`, `JetAlgebra.massScale_ψ`, … : the scaling of
>   the jet coordinates.
> - `JetAlgebra.massScale_covDψ` : the covariant derivative is homogeneous of
>   weight five; the coupling is dimensionless.
> - `JetAlgebra.massScale_maxwellTerm`, `JetAlgebra.massScale_diracKineticTerm`,
>   `JetAlgebra.massScale_electronMassTerm` : the weights of the terms.
> - `JetAlgebra.massScale_lagrangian` : **the QED Lagrangian has mass dimension
>   four**.

## iv. References

> The scaling maps are defined in `PhyslibAlpha.Particles.QED.Basic`; the corresponding
> grading for the lepton–gauge sector is
> `Physlib.Particles.LeptonGaugeSector.JetAlgebra.MassDim`.

> …

## A. The scaling of the jet coordinates

> The photon-level scaling of the field strength and the Maxwell term, used to
> lift the weight of the Maxwell term to the QED jet algebra.

**`QED.Photon.JetAlgebra.massScale_fieldStrength_zero`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L82).

> The photon-level field strength has mass dimension two.

```lean
lemma massScale_fieldStrength_zero (c : ℝ) (μ ν : Fin 1 ⊕ Fin 3) :
    massScale c (fieldStrength 0 μ ν) = c ^ 4 • fieldStrength 0 μ ν
```

**`QED.Photon.JetAlgebra.massScale_maxwellTerm`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L89).

> The photon-level Maxwell term has mass dimension four.

```lean
lemma massScale_maxwellTerm (c : ℝ) :
    massScale c maxwellTerm = c ^ 8 • maxwellTerm
```

**`QED.JetAlgebra.massScale_A`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L104).

```lean
lemma massScale_A (c : ℝ) (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    massScale c (A s μ) = (c : ℂ) ^ (2 + 2 * Multiset.card s) • A s μ
```

**`QED.JetAlgebra.massScale_ψ`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L111).

```lean
lemma massScale_ψ (c : ℝ) (s : Multiset (Fin 1 ⊕ Fin 3)) (α : Fin 2 ⊕ Fin 2) :
    massScale c (ψ s α) = (c : ℂ) ^ (3 + 2 * Multiset.card s) • ψ s α
```

**`QED.JetAlgebra.massScale_barψ`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L117).

```lean
lemma massScale_barψ (c : ℝ) (s : Multiset (Fin 1 ⊕ Fin 3)) (α : Fin 2 ⊕ Fin 2) :
    massScale c (barψ s α) = (c : ℂ) ^ (3 + 2 * Multiset.card s) • barψ s α
```

**`QED.JetAlgebra.massScale_A_zero`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L124).

> The photon jet coordinate has mass dimension one.

```lean
lemma massScale_A_zero (c : ℝ) (μ : Fin 1 ⊕ Fin 3) :
    massScale c (A 0 μ) = (c : ℂ) ^ 2 • A 0 μ
```

**`QED.JetAlgebra.massScale_ψ_zero`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L130).

> The electron jet coordinate has mass dimension `3/2`.

```lean
lemma massScale_ψ_zero (c : ℝ) (α : Fin 2 ⊕ Fin 2) :
    massScale c (ψ 0 α) = (c : ℂ) ^ 3 • ψ 0 α
```

**`QED.JetAlgebra.massScale_barψ_zero`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L135).

```lean
lemma massScale_barψ_zero (c : ℝ) (α : Fin 2 ⊕ Fin 2) :
    massScale c (barψ 0 α) = (c : ℂ) ^ 3 • barψ 0 α
```

**`QED.JetAlgebra.massScale_ψ_singleton`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L140).

```lean
lemma massScale_ψ_singleton (c : ℝ) (μ : Fin 1 ⊕ Fin 3) (α : Fin 2 ⊕ Fin 2) :
    massScale c (ψ {μ} α) = (c : ℂ) ^ 5 • ψ {μ} α
```

**`QED.JetAlgebra.massScale_barψ_singleton`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L145).

```lean
lemma massScale_barψ_singleton (c : ℝ) (μ : Fin 1 ⊕ Fin 3) (α : Fin 2 ⊕ Fin 2) :
    massScale c (barψ {μ} α) = (c : ℂ) ^ 5 • barψ {μ} α
```

## B. Homogeneity of the field strength and the covariant derivative

**`QED.JetAlgebra.massScale_fieldStrength_zero`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L157).

> The field strength has mass dimension two.

```lean
lemma massScale_fieldStrength_zero (c : ℝ) (μ ν : Fin 1 ⊕ Fin 3) :
    massScale c (fieldStrength 0 μ ν) = (c : ℂ) ^ 4 • fieldStrength 0 μ ν
```

**`QED.JetAlgebra.massScale_covDψ`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L165).

> **The covariant derivative is homogeneous**, of the same weight as the
> plain derivative: the electric coupling `e` is dimensionless.  This is the
> power-counting statement behind the renormalizability of QED.

```lean
lemma massScale_covDψ (c : ℝ) (e : ℝ) (μ : Fin 1 ⊕ Fin 3) (α : Fin 2 ⊕ Fin 2) :
    massScale c (covDψ e μ α) = (c : ℂ) ^ 5 • covDψ e μ α
```

**`QED.JetAlgebra.massScale_covDbarψ`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L172).

```lean
lemma massScale_covDbarψ (c : ℝ) (e : ℝ) (μ : Fin 1 ⊕ Fin 3) (α : Fin 2 ⊕ Fin 2) :
    massScale c (covDbarψ e μ α) = (c : ℂ) ^ 5 • covDbarψ e μ α
```

## C. The weights of the terms of the Lagrangian

**`QED.JetAlgebra.massScale_maxwellTerm`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L186).

> The Maxwell term has mass dimension four.

```lean
lemma massScale_maxwellTerm (c : ℝ) :
    massScale c maxwellTerm = (c : ℂ) ^ 8 • maxwellTerm
```

**`QED.JetAlgebra.massScale_diracKineticTerm`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L194).

> The Dirac kinetic term has mass dimension four.

```lean
lemma massScale_diracKineticTerm (c : ℝ) (e : ℝ) :
    massScale c (diracKineticTerm e) = (c : ℂ) ^ 8 • diracKineticTerm e
```

**`QED.JetAlgebra.massScale_diracKineticTermBar`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L209).

> The conjugate Dirac kinetic term has mass dimension four.

```lean
lemma massScale_diracKineticTermBar (c : ℝ) (e : ℝ) :
    massScale c (diracKineticTermBar e) = (c : ℂ) ^ 8 • diracKineticTermBar e
```

**`QED.JetAlgebra.massScale_electronMassTerm`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L224).

> The Dirac mass term has mass dimension three.

```lean
lemma massScale_electronMassTerm (c : ℝ) :
    massScale c electronMassTerm = (c : ℂ) ^ 6 • electronMassTerm
```

## D. The mass dimension of the QED Lagrangian

**`QED.JetAlgebra.massScale_lagrangian`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean#L243).

> **The QED Lagrangian has mass dimension four.**  Rescaling all fields by
> their mass weights takes `L(e, c² m)` to `c⁸ L(e, m)`: the coupling `e` is
> dimensionless and the electron mass is a coefficient of dimension one, so
> every term of the Lagrangian is renormalizable.

```lean
lemma massScale_lagrangian (c : ℝ) (e m : ℝ) :
    massScale c (lagrangian e (c ^ 2 * m)) = (c : ℂ) ^ 8 • lagrangian e m
```

## Depends on

- [The QED Lagrangian](lagrangian.md)

## Proof depends on

- [Properties of the field strength](fieldstrength.md)

## Sources

- [PhyslibAlpha/Particles/QED/MassDimension.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/MassDimension.lean)
