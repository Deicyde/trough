---
declaration: module
origin: cited
lean: QED.Photon.JetAlgebra.fieldStrength_antisymm, QED.Photon.JetAlgebra.fieldStrength_self, QED.Photon.JetAlgebra.fieldStrength_bianchi, QED.JetAlgebra.fieldStrength_eq_sub, QED.JetAlgebra.fieldStrength_antisymm, QED.JetAlgebra.fieldStrength_self, QED.JetAlgebra.fieldStrength_bianchi, QED.Photon.JetAlgebra.fieldStrength_singleton_eq_jetDeriv
statement: formalized
proof: formalized
---

# Properties of the field strength

The module `PhyslibAlpha.Particles.QED.FieldStrength`, [PhyslibAlpha/Particles/QED/FieldStrength.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FieldStrength.lean): 11 declarations, 6 with a docstring.

## i. Overview

> The structural theorems about the electromagnetic field strength in the jet
> algebras of QED: antisymmetry, the expression of the field strength through
> the potential coordinates, and the **Bianchi identity**
>
> `∂_λ F_{μν} + ∂_μ F_{νλ} + ∂_ν F_{λμ} = 0`,
>
> the homogeneous half of Maxwell's equations.  In the jet algebra the Bianchi
> identity is exact and purely combinatorial: each term is a difference of
> second-derivative coordinates, and the six coordinates cancel in pairs because
> multiset addition is commutative — Clairaut's theorem is built into the
> indexing.
>
> This file contains no definitions, only theorems about the fields of
> `PhyslibAlpha.Particles.QED.Fields`.

## ii. Key results

> - `Photon.JetAlgebra.fieldStrength_antisymm`,
>   `JetAlgebra.fieldStrength_antisymm` : antisymmetry of the field strength.
> - `JetAlgebra.fieldStrength_eq_sub` : the field strength through the
>   potential coordinates, `F_{μν} = ∂_μ A_ν - ∂_ν A_μ`.
> - `Photon.JetAlgebra.fieldStrength_bianchi`,
>   `JetAlgebra.fieldStrength_bianchi` : **the Bianchi identity**.

## iv. References

> The fields are defined in `PhyslibAlpha.Particles.QED.Fields`.  The inhomogeneous half of
> Maxwell's equations is dynamical (it needs the variation of the Lagrangian)
> and is not part of the jet-algebra kinematics.

## A. The field strength in the photon jet algebra

### A.1. Antisymmetry

**`QED.Photon.JetAlgebra.fieldStrength_antisymm`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FieldStrength.lean#L72).

```lean
lemma fieldStrength_antisymm (s : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    fieldStrength s μ ν = -fieldStrength s ν μ
```

**`QED.Photon.JetAlgebra.fieldStrength_self`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FieldStrength.lean#L77).

```lean
lemma fieldStrength_self (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    fieldStrength s μ μ = 0
```

### A.2. The Bianchi identity

> Each field strength is a difference of two second-derivative coordinates; the
> cyclic sum produces six coordinates which cancel in pairs, because the
> multisets `s + {μ} + {ν}` and `s + {ν} + {μ}` are equal.

**`QED.Photon.JetAlgebra.fieldStrength_bianchi`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FieldStrength.lean#L94).

> **The Bianchi identity** `∂_lam F_{μν} + ∂_μ F_{ν lam} + ∂_ν F_{lam μ} = 0`
> in the photon jet algebra: the homogeneous Maxwell equations hold exactly,
> for every derivative order `s`.

```lean
lemma fieldStrength_bianchi (s : Multiset (Fin 1 ⊕ Fin 3))
    (lam μ ν : Fin 1 ⊕ Fin 3) :
    fieldStrength (s + {lam}) μ ν + fieldStrength (s + {μ}) ν lam +
      fieldStrength (s + {ν}) lam μ = 0
```

## B. The field strength in the QED jet algebra

> The theorems of section A, transported through the inclusion of the photon
> factor into the QED jet algebra.

**`QED.JetAlgebra.fieldStrength_eq_sub`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FieldStrength.lean#L121).

> The field strength is the antisymmetrised derivative of the potential,
> `∂_s F_{μν} = ∂_s ∂_μ A_ν - ∂_s ∂_ν A_μ`.

```lean
lemma fieldStrength_eq_sub (s : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    fieldStrength s μ ν = A (s + {μ}) ν - A (s + {ν}) μ
```

**`QED.JetAlgebra.fieldStrength_antisymm`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FieldStrength.lean#L127).

```lean
lemma fieldStrength_antisymm (s : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    fieldStrength s μ ν = -fieldStrength s ν μ
```

**`QED.JetAlgebra.fieldStrength_self`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FieldStrength.lean#L133).

```lean
lemma fieldStrength_self (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    fieldStrength s μ μ = 0
```

**`QED.JetAlgebra.fieldStrength_bianchi`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FieldStrength.lean#L139).

> **The Bianchi identity** in the QED jet algebra.

```lean
lemma fieldStrength_bianchi (s : Multiset (Fin 1 ⊕ Fin 3))
    (lam μ ν : Fin 1 ⊕ Fin 3) :
    fieldStrength (s + {lam}) μ ν + fieldStrength (s + {μ}) ν lam +
      fieldStrength (s + {ν}) lam μ = 0
```

## C. The total derivative on the fields

**`QED.Photon.JetAlgebra.fieldStrength_singleton_eq_jetDeriv`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FieldStrength.lean#L155).

> The first-order field-strength jet is the total derivative of the
> zeroth-order one, in the photon jet algebra.

```lean
lemma _root_.QED.Photon.JetAlgebra.fieldStrength_singleton_eq_jetDeriv
    (ρ μ ν : Fin 1 ⊕ Fin 3) :
    Photon.JetAlgebra.fieldStrength {ρ} μ ν =
      Photon.JetAlgebra.jetDeriv ρ (Photon.JetAlgebra.fieldStrength 0 μ ν)
```

**`QED.JetAlgebra.jetDeriv_A`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FieldStrength.lean#L170).

> The total derivative appends the derivative index to the photon jet
> coordinate.

```lean
lemma jetDeriv_A (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (μ : Fin 1 ⊕ Fin 3) :
    jetDeriv ρ (A s μ) = A (s + {ρ}) μ
```

**`QED.JetAlgebra.jetDeriv_ψ`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FieldStrength.lean#L180).

> The total derivative appends the derivative index to the electron jet
> coordinate.

```lean
lemma jetDeriv_ψ (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (α : Fin 2 ⊕ Fin 2) :
    jetDeriv ρ (ψ s α) = ψ (s + {ρ}) α
```

**`QED.JetAlgebra.jetDeriv_barψ`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FieldStrength.lean#L191).

```lean
lemma jetDeriv_barψ (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (α : Fin 2 ⊕ Fin 2) :
    jetDeriv ρ (barψ s α) = barψ (s + {ρ}) α
```

## Depends on

- [The fields of quantum electrodynamics](fields.md)

## Proof depends on

- [Gauge invariance of quantum electrodynamics](gaugeinvariance.md)

## Sources

- [PhyslibAlpha/Particles/QED/FieldStrength.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FieldStrength.lean)
