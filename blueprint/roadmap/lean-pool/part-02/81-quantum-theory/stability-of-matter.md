---
declaration: theorem
origin: cited
lean: LiebThirring.stability_of_matter
statement: formalized
proof: formalized
---

# Stability of matter and the kinetic Lieb–Thirring inequality

> Formalizes stability of non-relativistic fermionic Coulomb matter in three dimensions, the kinetic Lieb–Thirring inequality with Rumin's explicit coefficient, Baxter's electrostatic inequality with its positive nuclear correction, and real quadratic-form stability with Coulomb finiteness. Preserves the Fourier, Pauli-occupation, Hardy and Voronoi infrastructure in the 184-module dependency closure of these results. The separate ionization, thermodynamic-limit and Thomas–Fermi developments are outside the imported scope.

*Quoted from the card [LeanPool/projects/stability-of-matter.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/stability-of-matter.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`LiebThirring.stability_of_matter`](https://leanpool.github.io/lean-pool/LeanPool/LiebThirring/Theorems/StabilityOfMatter.html#LiebThirring.stability_of_matter) (theorem; a main declaration), declared in [LeanPool/LiebThirring/Theorems/StabilityOfMatter.lean, line 32](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LiebThirring/Theorems/StabilityOfMatter.lean#L32): “For each positive spin multiplicity and nonnegative maximum nuclear charge, one positive constant bounds electron–nucleus attraction by kinetic energy, electron and nuclear repulsion, and the total particle count, uniformly over normalized antisymmetric L² states, charges and nuclear positions, in nonnegative extended-energy form.”
- [`LiebThirring.stability_of_matter_real`](https://leanpool.github.io/lean-pool/LeanPool/LiebThirring/Theorems/StabilityOfMatterReal.html#LiebThirring.stability_of_matter_real) (theorem), declared in [LeanPool/LiebThirring/Theorems/StabilityOfMatterReal.lean, line 31](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LiebThirring/Theorems/StabilityOfMatterReal.lean#L31): “With distinct nuclear positions and finite kinetic energy, Coulomb expectations and nuclear repulsion are finite and the real quadratic energy is bounded below by a negative constant times the total particle count, with the constant depending only on spin and maximum charge.”
- [`LiebThirring.kinetic_lieb_thirring`](https://leanpool.github.io/lean-pool/LeanPool/LiebThirring/Theorems/KineticLiebThirring.html#LiebThirring.kinetic_lieb_thirring) (theorem), declared in [LeanPool/LiebThirring/Theorems/KineticLiebThirring.lean, line 31](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LiebThirring/Theorems/KineticLiebThirring.lean#L31): “Every normalized antisymmetric L² state with positive spin multiplicity q has kinetic energy at least Rumin's coefficient times q to the power minus two thirds times the integral of the density to the power five thirds, including states of infinite kinetic energy.”
- [`LiebThirring.baxter`](https://leanpool.github.io/lean-pool/LeanPool/LiebThirring/Theorems/Baxter.html#LiebThirring.baxter) (theorem), declared in [LeanPool/LiebThirring/Theorems/Baxter.lean, line 29](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LiebThirring/Theorems/Baxter.lean#L29): “For equal nonnegative nuclear charges, attraction plus the positive nearest-other-nucleus correction is bounded by electron and nuclear repulsion plus nearest-nucleus control, including collisions and empty configurations in nonnegative extended arithmetic.”
- [`LiebThirring.kineticEnergy_schwartz`](https://leanpool.github.io/lean-pool/LeanPool/LiebThirring/Theorems/KineticEnergySchwartz.html#LiebThirring.kineticEnergy_schwartz) (theorem), declared in [LeanPool/LiebThirring/Theorems/KineticEnergySchwartz.lean, line 30](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LiebThirring/Theorems/KineticEnergySchwartz.lean#L30): “The Fourier kinetic energy of a spin-valued Schwartz state equals the sum of the squared classical spatial derivative integrals, with the physical minus-Laplacian normalization.”

## Project

- Authors: Scott Armstrong, Amélie Loher.
- Source: [arXiv:2007.09326](https://arxiv.org/abs/2007.09326), [https://github.com/scottnarmstrong/LiebThirring/tree/8bf4656f07f5aaa227b0b850d77b16976915bbd4](https://github.com/scottnarmstrong/LiebThirring/tree/8bf4656f07f5aaa227b0b850d77b16976915bbd4).
- Project repository: [scottnarmstrong/LiebThirring](https://github.com/scottnarmstrong/LiebThirring), at commit [8bf4656f](https://github.com/scottnarmstrong/LiebThirring/tree/8bf4656f07f5aaa227b0b850d77b16976915bbd4).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 81Q10, 35P15, 46N50.
- In Lean Pool: [LeanPool/LiebThirring](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LiebThirring), from the card [LeanPool/projects/stability-of-matter.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/stability-of-matter.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/stability-of-matter.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/stability-of-matter.yaml)
- [Lean Pool at 2b205bf9: LeanPool/LiebThirring](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LiebThirring)
