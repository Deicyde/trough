---
declaration: theorem
origin: cited
lean: allpos_has_pos_eigenvec, perron_frobenius, ground_state_strictly_positive
statement: formalized
proof: formalized
---

# Spectral positivity

> Perron-Frobenius theory, Jentzsch's theorem, and matrix/operator positivity in Lean 4. At the matrix level it proves that nonnegative matrices have nonnegative powers, the Metzler decomposition and positivity of the matrix exponential of a Metzler matrix, M-matrix inverse positivity, and the Perron-Frobenius theorem for irreducible nonnegative matrices (a positive dominant eigenvalue with a strictly positive eigenvector). At the operator level it proves Jentzsch's theorem for compact self-adjoint positivity-improving operators on L2 — a simple, strictly positive ground state with a spectral gap — together with a kernel positivity criterion.

*Quoted from the card [LeanPool/projects/spectral-positivity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/spectral-positivity.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`allpos_has_pos_eigenvec`](https://leanpool.github.io/lean-pool/LeanPool/SpectralPositivity/Matrix/PerronFrobenius.html#allpos_has_pos_eigenvec) (theorem; a main declaration), declared in [LeanPool/SpectralPositivity/Matrix/PerronFrobenius.lean, line 266](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpectralPositivity/Matrix/PerronFrobenius.lean#L266): “A matrix with all strictly positive entries has a positive eigenvalue with a strictly positive eigenvector (Perron-Frobenius for positive matrices, via the Collatz-Wielandt characterization).”
- [`perron_frobenius`](https://leanpool.github.io/lean-pool/LeanPool/SpectralPositivity/Matrix/PerronFrobenius.html#perron_frobenius) (theorem; a main declaration), declared in [LeanPool/SpectralPositivity/Matrix/PerronFrobenius.lean, line 481](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpectralPositivity/Matrix/PerronFrobenius.lean#L481): “An irreducible (primitive) nonnegative matrix has a positive eigenvalue with a strictly positive eigenvector.”
- [`ground_state_strictly_positive`](https://leanpool.github.io/lean-pool/LeanPool/SpectralPositivity/Operator/JentzschProof.html#ground_state_strictly_positive) (theorem; a main declaration), declared in [LeanPool/SpectralPositivity/Operator/JentzschProof.lean, line 294](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpectralPositivity/Operator/JentzschProof.lean#L294): “The ground eigenfunction of a compact self-adjoint positivity-improving operator on L2 is strictly positive almost everywhere (Jentzsch).”
- [`SpectralPositivity.Matrix.MMatrix.inverse_pos`](https://leanpool.github.io/lean-pool/LeanPool/SpectralPositivity/Matrix/MMatrixInverse.html#SpectralPositivity.Matrix.MMatrix.inverse_pos) (theorem), declared in [LeanPool/SpectralPositivity/Matrix/MMatrixInverse.lean, line 309](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpectralPositivity/Matrix/MMatrixInverse.lean#L309): “The inverse of a nonsingular irreducible M-matrix is entrywise strictly positive.”

## Project

- Authors: Michael R. Douglas.
- Source: *spectral-positivity: Perron-Frobenius, Jentzsch, and matrix positivity in Lean 4* by Michael R. Douglas.
- Project repository: [mrdouglasny/spectral-positivity](https://github.com/mrdouglasny/spectral-positivity).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 15B48, 15A18.
- In Lean Pool: [LeanPool/SpectralPositivity](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpectralPositivity), from the card [LeanPool/projects/spectral-positivity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/spectral-positivity.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/spectral-positivity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/spectral-positivity.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SpectralPositivity](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpectralPositivity)
