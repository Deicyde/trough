---
declaration: module
origin: cited
lean: QED.Electron.JetAlgebra.ofGenerator_mul_self, QED.Electron.JetAlgebra.ofGenerator_anticommute, QED.JetAlgebra.ψ_mul_ψ_anticomm, QED.JetAlgebra.ψ_mul_barψ_anticomm, QED.JetAlgebra.barψ_mul_barψ_anticomm, QED.JetAlgebra.ψ_mul_self, QED.JetAlgebra.barψ_mul_self, QED.JetAlgebra.A_mul_A_comm
statement: formalized
proof: formalized
---

# Spin-statistics of the QED fields

The module `PhyslibAlpha.Particles.QED.FermionStatistics`, [PhyslibAlpha/Particles/QED/FermionStatistics.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FermionStatistics.lean): 10 declarations, 9 with a docstring.

## i. Overview

> The statistics of the fields of QED, as encoded in the QED jet algebra: the
> electron jet coordinates anticommute among themselves and square to zero
> (fermionic statistics), while the photon jet coordinates commute with
> everything (bosonic statistics).
>
> This file contains no definitions, only theorems about the fields of
> `PhyslibAlpha.Particles.QED.Fields`.

## ii. Key results

> - `Electron.JetAlgebra.ofGenerator_mul_self`,
>   `Electron.JetAlgebra.ofGenerator_anticommute` : fermionic statistics of the
>   electron jet coordinates.
> - `JetAlgebra.ψ_mul_ψ_anticomm`, `JetAlgebra.ψ_mul_barψ_anticomm`,
>   `JetAlgebra.barψ_mul_barψ_anticomm` : the electron coordinates anticommute
>   in the QED jet algebra.
> - `JetAlgebra.ψ_mul_self`, `JetAlgebra.barψ_mul_self` : Pauli exclusion for
>   the jet coordinates.
> - `JetAlgebra.A_mul_A_comm`, `JetAlgebra.A_mul_ψ_comm`,
>   `JetAlgebra.A_mul_barψ_comm` : the photon coordinates are bosonic.

## iv. References

> The fields are defined in `PhyslibAlpha.Particles.QED.Fields`.

## A. Fermionic statistics of the electron jet coordinates

**`QED.Electron.JetAlgebra.ofGenerator_mul_self`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FermionStatistics.lean#L62).

```lean
lemma ofGenerator_mul_self (j : JetGenerators) :
    ofGenerator j * ofGenerator j = 0
```

**`QED.Electron.JetAlgebra.ofGenerator_anticommute`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FermionStatistics.lean#L68).

> The jet coordinates of the electron anticommute: the electron is a
> fermion.

```lean
lemma ofGenerator_anticommute (i j : JetGenerators) :
    ofGenerator i * ofGenerator j = -(ofGenerator j * ofGenerator i)
```

## B. Fermionic statistics in the QED jet algebra

**`QED.JetAlgebra.ψ_mul_ψ_anticomm`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FermionStatistics.lean#L89).

> The electron jet coordinates anticommute.

```lean
lemma ψ_mul_ψ_anticomm (s t : Multiset (Fin 1 ⊕ Fin 3)) (α β : Fin 2 ⊕ Fin 2) :
    ψ s α * ψ t β = -(ψ t β * ψ s α)
```

**`QED.JetAlgebra.ψ_mul_barψ_anticomm`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FermionStatistics.lean#L95).

> The electron and conjugate-electron jet coordinates anticommute.

```lean
lemma ψ_mul_barψ_anticomm (s t : Multiset (Fin 1 ⊕ Fin 3)) (α β : Fin 2 ⊕ Fin 2) :
    ψ s α * barψ t β = -(barψ t β * ψ s α)
```

**`QED.JetAlgebra.barψ_mul_barψ_anticomm`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FermionStatistics.lean#L101).

> The conjugate-electron jet coordinates anticommute.

```lean
lemma barψ_mul_barψ_anticomm (s t : Multiset (Fin 1 ⊕ Fin 3)) (α β : Fin 2 ⊕ Fin 2) :
    barψ s α * barψ t β = -(barψ t β * barψ s α)
```

**`QED.JetAlgebra.ψ_mul_self`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FermionStatistics.lean#L108).

> Pauli exclusion: an electron jet coordinate squares to zero.

```lean
lemma ψ_mul_self (s : Multiset (Fin 1 ⊕ Fin 3)) (α : Fin 2 ⊕ Fin 2) :
    ψ s α * ψ s α = 0
```

**`QED.JetAlgebra.barψ_mul_self`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FermionStatistics.lean#L114).

> Pauli exclusion: a conjugate electron jet coordinate squares to zero.

```lean
lemma barψ_mul_self (s : Multiset (Fin 1 ⊕ Fin 3)) (α : Fin 2 ⊕ Fin 2) :
    barψ s α * barψ s α = 0
```

## C. Bosonic statistics of the photon jet coordinates

**`QED.JetAlgebra.A_mul_A_comm`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FermionStatistics.lean#L126).

> The photon jet coordinates commute among themselves: the photon is a
> boson.

```lean
lemma A_mul_A_comm (s t : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    A s μ * A t ν = A t ν * A s μ
```

**`QED.JetAlgebra.A_mul_ψ_comm`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FermionStatistics.lean#L132).

> The photon jet coordinates commute with the electron jet coordinates.

```lean
lemma A_mul_ψ_comm (s t : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (α : Fin 2 ⊕ Fin 2) :
    A s μ * ψ t α = ψ t α * A s μ
```

**`QED.JetAlgebra.A_mul_barψ_comm`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FermionStatistics.lean#L139).

> The photon jet coordinates commute with the conjugate electron jet
> coordinates.

```lean
lemma A_mul_barψ_comm (s t : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (α : Fin 2 ⊕ Fin 2) :
    A s μ * barψ t α = barψ t α * A s μ
```

## Depends on

- [The fields of quantum electrodynamics](fields.md)

## Sources

- [PhyslibAlpha/Particles/QED/FermionStatistics.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/FermionStatistics.lean)
