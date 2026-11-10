---
declaration: theorem
origin: cited
lean: EllipticPdes.Regularity.higher_interior_regularity
statement: formalized
proof: formalized
---

# Linear elliptic PDE: solvability, regularity and spectral theory

> A reusable analytic development of linear uniformly elliptic divergence-form PDE on Euclidean domains: Hilbert graph models of H¹ and H₀¹, bounded coefficient operators, Poincaré inequalities, zero-drift/nonnegative-potential Dirichlet existence and uniqueness, Gårding and Fredholm theory for general drift, interior H² and higher Sobolev regularity, smooth classical representatives, Sobolev and Hölder embeddings, C¹-domain extension and compactness, variational eigenvalues, and maximum principles. AI-generated proofs with human mathematical design and transcription; announced in arXiv:2609.32561 on 2026-09-26. The unfinished boundary-H² program is outside this completed dependency closure.

*Quoted from the card [LeanPool/projects/elliptic-pde.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/elliptic-pde.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`EllipticPdes.Sobolev.FullEllipticOp.weak_solution_L2_of_nonneg_zeroth_of_bounded`](https://leanpool.github.io/lean-pool/LeanPool/EllipticPDE/Existence/Garding.html#EllipticPdes.Sobolev.FullEllipticOp.weak_solution_L2_of_nonneg_zeroth_of_bounded) (theorem), declared in [LeanPool/EllipticPDE/Existence/Garding.lean, line 565](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EllipticPDE/Existence/Garding.lean#L565): “On a bounded domain in positive dimension, a bounded measurable uniformly elliptic operator with zero drift and nonnegative zeroth-order coefficient has a unique H₀¹ weak solution for every L² datum, with a datum-independent norm bound.”
- [`EllipticPdes.Regularity.interior_H2_estimate`](https://leanpool.github.io/lean-pool/LeanPool/EllipticPDE/Regularity/Interior.html#EllipticPdes.Regularity.interior_H2_estimate) (theorem), declared in [LeanPool/EllipticPDE/Regularity/Interior.lean, line 118](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EllipticPDE/Regularity/Interior.lean#L118): “In positive dimension, on an open measurable domain, an H₀¹ weak solution of a bounded measurable uniformly elliptic divergence-form operator with globally Lipschitz principal coefficients and an L² datum has interior L² second weak derivatives, with an estimate whose constant is chosen before the solution and datum.”
- [`EllipticPdes.Regularity.higher_interior_regularity`](https://leanpool.github.io/lean-pool/LeanPool/EllipticPDE/Regularity/HigherInterior.html#EllipticPdes.Regularity.higher_interior_regularity) (theorem; a main declaration), declared in [LeanPool/EllipticPDE/Regularity/HigherInterior.lean, line 549](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EllipticPDE/Regularity/HigherInterior.lean#L549): “In positive dimension, for a uniformly elliptic divergence-form operator with bounded measurable coefficients, globally Lipschitz principal-coefficient representatives in W^{k+1,∞}(ℝ^d), and lower-order coefficients in W^{k,∞}(ℝ^d), every H₀¹ weak solution on an open measurable domain with an H^k datum has interior H^{k+2} regularity. On each compact subset the iterated L² derivative bounds have a constant chosen before the solution, datum and its H^k bound. The pointwise Lipschitz hypothesis is separate from the weak-derivative bundles.”
- [`EllipticPdes.Sobolev.embL2_isCompact`](https://leanpool.github.io/lean-pool/LeanPool/EllipticPDE/Spectrum/RellichDischarge.html#EllipticPdes.Sobolev.embL2_isCompact) (theorem), declared in [LeanPool/EllipticPDE/Spectrum/RellichDischarge.lean, line 203](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EllipticPDE/Spectrum/RellichDischarge.lean#L203): “The inclusion H₀¹(Ω) → L²(Ω) is compact for bounded measurable Euclidean domains, discharging the compactness input to the Fredholm and spectral results.”
- [`EllipticPdes.Extension.exists_extW12`](https://leanpool.github.io/lean-pool/LeanPool/EllipticPDE/Extension/GraphOperator.html#EllipticPdes.Extension.exists_extW12) (theorem), declared in [LeanPool/EllipticPDE/Extension/GraphOperator.lean, line 188](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EllipticPDE/Extension/GraphOperator.lean#L188): “In positive dimension, bounded open Euclidean domains with C¹ boundary admit a bounded linear H¹ extension operator with compact support control.”

## Project

- Authors: Alejandro José Soto Franco, Kobe Marshall-Stevens.
- Source: [arXiv:2609.32561](https://arxiv.org/abs/2609.32561).
- Project repository: [alejandro-soto-franco/EllipticPDE](https://github.com/alejandro-soto-franco/EllipticPDE), at commit [eaf821d3](https://github.com/alejandro-soto-franco/EllipticPDE/tree/eaf821d31b200bb6ea235f19eecc50cf0f38c294).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 35J15, 35J25, 35B65, 46E35.
- In Lean Pool: [LeanPool/EllipticPDE](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EllipticPDE), from the card [LeanPool/projects/elliptic-pde.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/elliptic-pde.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/elliptic-pde.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/elliptic-pde.yaml)
- [Lean Pool at 2b205bf9: LeanPool/EllipticPDE](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EllipticPDE)
