---
declaration: theorem
origin: cited
lean: rado_riemannSurface
statement: formalized
proof: formalized
---

# Radó's theorem for Riemann surfaces

> Proves that every connected Hausdorff one-dimensional complex manifold is second countable. The development constructs a nonconstant harmonic function by Perron's method, builds the étale space of its harmonic-conjugate germs, and applies a formalized Poincaré-Volterra lemma to its discrete-fiber evaluation map.

*Quoted from the card [LeanPool/projects/rado-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/rado-theorem.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`rado_riemannSurface`](https://leanpool.github.io/lean-pool/LeanPool/Rado/Main.html#rado_riemannSurface) (theorem; a main declaration), declared in [LeanPool/Rado/Main.lean, line 30](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Rado/Main.lean#L30): “Every connected Hausdorff topological space carrying the structure of a one-dimensional complex manifold has a second-countable topology.”
- [`Rado.poincare_volterra`](https://leanpool.github.io/lean-pool/LeanPool/Rado/Topology/PoincareVolterra.html#Rado.poincare_volterra) (theorem), declared in [LeanPool/Rado/Topology/PoincareVolterra.lean, line 104](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Rado/Topology/PoincareVolterra.lean#L104): “A connected Hausdorff, locally compact, locally connected and locally second-countable space is second countable whenever it admits a continuous, locally injective map into a second-countable Hausdorff space.”
- [`Rado.exists_harmonic_extension`](https://leanpool.github.io/lean-pool/LeanPool/Rado/Complex/Poisson.html#Rado.exists_harmonic_extension) (theorem), declared in [LeanPool/Rado/Complex/Poisson.lean, line 391](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Rado/Complex/Poisson.lean#L391): “Every continuous real-valued function on a Euclidean circle extends continuously to its closed disk and harmonically to the open disk; unlike the existing LeanComplexAnalysis Poisson theorems, this constructs the harmonic function rather than assuming one.”
- [`Rado.IsPerronFamily.surfaceHarmonicOn_perronSup`](https://leanpool.github.io/lean-pool/LeanPool/Rado/Surface/Perron.html#Rado.IsPerronFamily.surfaceHarmonicOn_perronSup) (theorem), declared in [LeanPool/Rado/Surface/Perron.lean, line 554](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Rado/Surface/Perron.lean#L554): “The pointwise upper envelope of a Perron family of surface subharmonic functions is harmonic on its open domain.”

## Project

- Authors: Rado Kirov.
- Source: *Radó's theorem for Riemann surfaces* by Rado Kirov.
- Project repository: [rkirov/jordan_pick](https://github.com/rkirov/jordan_pick), at commit [b3c9b7cf](https://github.com/rkirov/jordan_pick/tree/b3c9b7cf7358bf81a077d78ad67e6e8247869ddd).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 30F15, 30F20, 54D65.
- In Lean Pool: [LeanPool/Rado](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Rado), from the card [LeanPool/projects/rado-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/rado-theorem.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/rado-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/rado-theorem.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Rado](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Rado)
