---
declaration: theorem
origin: cited
lean: CompactSelfAdjoint.exists_hasEigenvector_iSup_or_iInf_of_isCompactOperator
statement: formalized
proof: formalized
---

# Spectral theorem for compact self-adjoint operators

> Formalizes the spectral theorem for compact self-adjoint operators on a Hilbert space: such an operator admits a Hilbert basis of eigenvectors. The development passes from weak compactness of Hilbert closed balls and Rayleigh-quotient extrema to an eigenvector at the operator norm, finiteness of the point spectrum outside any neighbourhood of zero, finite-rank cutoff approximation, and finally the orthogonal decomposition into eigenspaces.

*Quoted from the card [LeanPool/projects/compact-spectral.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/compact-spectral.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`CompactSelfAdjoint.exists_hilbertBasis_hasEigenvector_of_isCompactOperator_of_isSelfAdjoint`](https://leanpool.github.io/lean-pool/LeanPool/CompactSpectral/Analysis/InnerProductSpace/CompactSelfAdjoint/SpectralTheorem.html#CompactSelfAdjoint.exists_hilbertBasis_hasEigenvector_of_isCompactOperator_of_isSelfAdjoint) (theorem), declared in [LeanPool/CompactSpectral/Analysis/InnerProductSpace/CompactSelfAdjoint/SpectralTheorem.lean, line 139](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompactSpectral/Analysis/InnerProductSpace/CompactSelfAdjoint/SpectralTheorem.lean#L139): “A compact self-adjoint operator on a Hilbert space admits a Hilbert basis of eigenvectors.” Its source, as the card gives it: “A. W. Knapp, Advanced Real Analysis, Chapter II, Section 2, Theorem 2.3, doi:10.3792/euclid/9781429799911-2.”
- [`CompactSelfAdjoint.iSup_eigenspace_orthogonal_eq_bot_of_isCompactOperator_of_isSelfAdjoint`](https://leanpool.github.io/lean-pool/LeanPool/CompactSpectral/Analysis/InnerProductSpace/CompactSelfAdjoint/SpectralTheorem.html#CompactSelfAdjoint.iSup_eigenspace_orthogonal_eq_bot_of_isCompactOperator_of_isSelfAdjoint) (theorem), declared in [LeanPool/CompactSpectral/Analysis/InnerProductSpace/CompactSelfAdjoint/SpectralTheorem.lean, line 45](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompactSpectral/Analysis/InnerProductSpace/CompactSelfAdjoint/SpectralTheorem.lean#L45): “The eigenspaces of a compact self-adjoint operator span a dense subspace: the orthogonal complement of the supremum of all eigenspaces is trivial.” Its source, as the card gives it: “A. W. Knapp, Advanced Real Analysis, Chapter II, Section 2, Theorem 2.3, doi:10.3792/euclid/9781429799911-2.”
- [`CompactSelfAdjoint.exists_hasEigenvector_iSup_or_iInf_of_isCompactOperator`](https://leanpool.github.io/lean-pool/LeanPool/CompactSpectral/Analysis/InnerProductSpace/RayleighCompact.html#CompactSelfAdjoint.exists_hasEigenvector_iSup_or_iInf_of_isCompactOperator) (theorem; a main declaration), declared in [LeanPool/CompactSpectral/Analysis/InnerProductSpace/RayleighCompact.lean, line 335](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompactSpectral/Analysis/InnerProductSpace/RayleighCompact.lean#L335): “A compact self-adjoint operator has an eigenvector whose eigenvalue realizes either the supremum or the infimum of its Rayleigh quotient.” Its source, as the card gives it: “A. W. Knapp, Advanced Real Analysis, Chapter II, Section 2, Theorem 2.2, doi:10.3792/euclid/9781429799911-2.”
- [`CompactSelfAdjoint.exists_unit_norm_eq_opNorm_of_isCompactOperator`](https://leanpool.github.io/lean-pool/LeanPool/CompactSpectral/Analysis/InnerProductSpace/CompactSelfAdjoint/OpNormEigenvalue.html#CompactSelfAdjoint.exists_unit_norm_eq_opNorm_of_isCompactOperator) (theorem), declared in [LeanPool/CompactSpectral/Analysis/InnerProductSpace/CompactSelfAdjoint/OpNormEigenvalue.lean, line 63](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompactSpectral/Analysis/InnerProductSpace/CompactSelfAdjoint/OpNormEigenvalue.lean#L63): “A compact operator attains its operator norm on the unit sphere of the Hilbert space.” Its source, as the card gives it: “A. W. Knapp, Advanced Real Analysis, Chapter II, Section 1, compactness preliminaries for compact operators, doi:10.3792/euclid/9781429799911-2.”
- [`CompactSelfAdjoint.countable_set_hasEigenvalue_ne_zero_of_isCompactOperator_of_isSelfAdjoint`](https://leanpool.github.io/lean-pool/LeanPool/CompactSpectral/Analysis/InnerProductSpace/CompactSelfAdjoint/SpectralFiniteness.html#CompactSelfAdjoint.countable_set_hasEigenvalue_ne_zero_of_isCompactOperator_of_isSelfAdjoint) (theorem), declared in [LeanPool/CompactSpectral/Analysis/InnerProductSpace/CompactSelfAdjoint/SpectralFiniteness.lean, line 212](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompactSpectral/Analysis/InnerProductSpace/CompactSelfAdjoint/SpectralFiniteness.lean#L212): “The set of nonzero eigenvalues of a compact self-adjoint operator is countable.” Its source, as the card gives it: “A. W. Knapp, Advanced Real Analysis, Chapter II, Section 2, spectral theorem consequences, doi:10.3792/euclid/9781429799911-2.”

## Project

- Authors: Adam Benenson.
- Source: *Advanced Real Analysis* by Anthony W. Knapp, [doi:10.3792/euclid/9781429799911-2](https://doi.org/10.3792/euclid/9781429799911-2).
- Project repository: [abenenson/compact-spectral](https://github.com/abenenson/compact-spectral).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 47A75, 47B07.
- In Lean Pool: [LeanPool/CompactSpectral](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompactSpectral), from the card [LeanPool/projects/compact-spectral.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/compact-spectral.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/compact-spectral.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/compact-spectral.yaml)
- [Lean Pool at 2b205bf9: LeanPool/CompactSpectral](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompactSpectral)
