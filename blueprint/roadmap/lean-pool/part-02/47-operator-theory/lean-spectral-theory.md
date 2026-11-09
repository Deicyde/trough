---
declaration: theorem
origin: cited
lean: PalomarSpectralStone.spectral_theorem_intrinsic
statement: formalized
proof: formalized
---

# lean-spectral-theory

> The spectral theorem for possibly unbounded self-adjoint operators on complex Hilbert spaces, formalized through the Cayley transform and real projection-valued measures. The selected spectral theorem constructs a PVM whose scalar measures give the exact finite-second-moment domain and first-moment quadratic form, with measurable-set uniqueness, and is proved equivalent to equality with the unbounded coordinate spectral integral. The selected Stone theorem proves both that strongly continuous one-parameter unitary groups have self-adjoint generators and that every self-adjoint operator generates such a group.

*Quoted from the card [LeanPool/projects/lean-spectral-theory.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-spectral-theory.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`PalomarSpectralStone.spectral_theorem_intrinsic`](https://leanpool.github.io/lean-pool/LeanPool/SpectralTheory/SpectralStoneSolution.html#PalomarSpectralStone.spectral_theorem_intrinsic) (theorem; a main declaration), declared in [LeanPool/SpectralTheory/SpectralStoneSolution.lean, line 85](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpectralTheory/SpectralStoneSolution.lean#L85): “Every self-adjoint partial linear operator on a complex Hilbert space has a real projection-valued measure representing its domain and scalar moments, unique on Borel sets.”
- [`PalomarSpectralStone.stone_theorem_intrinsic`](https://leanpool.github.io/lean-pool/LeanPool/SpectralTheory/SpectralStoneSolution.html#PalomarSpectralStone.stone_theorem_intrinsic) (theorem), declared in [LeanPool/SpectralTheory/SpectralStoneSolution.lean, line 137](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpectralTheory/SpectralStoneSolution.lean#L137): “Every strongly continuous one-parameter unitary group has a self-adjoint generator, and every self-adjoint operator generates such a group.”

## Project

- Authors: Ezzeri Esa.
- Project repository: [savarin/lean-spectral-theory](https://github.com/savarin/lean-spectral-theory), at commit [d19e279f](https://github.com/savarin/lean-spectral-theory/tree/d19e279f0ab244657f02ce678e8d67fa69e2f407).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 47A10, 47B15.
- In Lean Pool: [LeanPool/SpectralTheory](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpectralTheory), from the card [LeanPool/projects/lean-spectral-theory.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-spectral-theory.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/lean-spectral-theory.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-spectral-theory.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SpectralTheory](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpectralTheory)
