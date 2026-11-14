---
declaration: module
origin: cited
lean: MicroHamiltonian, microHamiltonianFintype, NVEHamiltonian, NVEHamiltonian.N, NVEHamiltonian.V
statement: formalized
proof: formalized
---

# The Microcanonical Ensemble

The module `Physlib.StatisticalMechanics.MicroCanonicalEnsemble.Basic`, [Physlib/StatisticalMechanics/MicroCanonicalEnsemble/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/Basic.lean): 5 declarations, 5 with a docstring.

**`MicroHamiltonian`**, a structure, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/Basic.lean#L27).

> The Hamiltonian for a microcanonical ensemble, parameterized by any extrinsic parameters of data
> D. Since it's an arbitrary type, 'T' would be nice, but we use 'D' for data to avoid confusion
> with temperature. We define Hamiltonians as an energy function on a real manifold, whose
> dimension n possibly depends on the data D. Energy is a WithTop ℝ, ⊤ is used to mean "excluded
> as a possibility in phase space". This formalization does exclude the possibility of discrete
> degrees of freedom; it is not \_completely\_ general. A better formalization could have an
> arbitrary measurable space.

```lean
structure MicroHamiltonian (D : Type) where
  /-- For extrinsic parameters D (e.g. the number of particles of different chemical species,
    the shape of the box), how many continuous degrees of freedom are there? -/
  dim : D → Type
  /-- The number of degrees of freedom is finite. -/
  [dimFin : ∀ d, Fintype (dim d)]
  /-- Given the configuration, what is its energy? -/
  H : {d : D} → (dim d → ℝ) → WithTop ℝ
  --The energy function must be measurable (else the partition function integral is meaningless).
  measurable_H : ∀ d, Measurable (@H d)
```

**`microHamiltonianFintype`**, an instance, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/Basic.lean#L39).

> The dimFin to the instance cache is added so that things like the measure can be synthesized

```lean
instance microHamiltonianFintype {D} (H : MicroHamiltonian D) (d : D) : Fintype (H.dim d)
```

**`NVEHamiltonian`**, an abbrev, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/Basic.lean#L44).

> The standard microcanonical ensemble Hamiltonian, where the data is the particle number N and
> the volume V.

```lean
abbrev NVEHamiltonian
```

**`NVEHamiltonian.N`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/Basic.lean#L47).

> Helper to get the number in an N-V Hamiltonian

```lean
def NVEHamiltonian.N : (ℕ × ℝ) → ℕ
```

**`NVEHamiltonian.V`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/Basic.lean#L50).

> Helper to get the volume in an N-V Hamiltonian

```lean
def NVEHamiltonian.V : (ℕ × ℝ) → ℝ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/StatisticalMechanics/MicroCanonicalEnsemble/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/Basic.lean)
