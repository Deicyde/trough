---
declaration: theorem
origin: cited
lean: RotationOfEigenvectors.sinTheta_mem_and_bound
statement: formalized
proof: formalized
---

# Davis–Kahan rotation of eigenvectors

> Formalizes the sin-Theta, tan-Theta, sin-two-Theta, and tan-two-Theta theorem families from Section 2 of Davis and Kahan (1970), for real or complex separable Hilbert spaces, including common-domain unbounded operators and symmetric-norm estimates. The tan-Theta endpoint requires Rayleigh–Ritz trial data with residual orthogonal to the trial subspace.

*Quoted from the card [LeanPool/projects/aiq-davis-kahan-1970-rotation-eigenvectgors-perturbation-formalization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/aiq-davis-kahan-1970-rotation-eigenvectgors-perturbation-formalization.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`RotationOfEigenvectors.sinTheta_mem_and_bound`](https://leanpool.github.io/lean-pool/LeanPool/DavisKahan/Solution.html#RotationOfEigenvectors.sinTheta_mem_and_bound) (theorem; a main declaration), declared in [LeanPool/DavisKahan/Solution.lean, line 383](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DavisKahan/Solution.lean#L383): “With finite symmetric residual norm, a spectral gap gives sine-angle ideal membership and controls its symmetric norm by the corresponding residual norm.”
- [`RotationOfEigenvectors.tanTheta`](https://leanpool.github.io/lean-pool/LeanPool/DavisKahan/Solution.html#RotationOfEigenvectors.tanTheta) (theorem), declared in [LeanPool/DavisKahan/Solution.lean, line 416](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DavisKahan/Solution.lean#L416): “For Rayleigh–Ritz trial data with residual orthogonal to the trial subspace, a positive directed spectral gap between the trial compression and the unwanted reducing block gives the symmetric-norm tangent-angle residual estimate and tangent pole exclusion, assuming the residual has finite symmetric norm.”
- [`RotationOfEigenvectors.sinTwoTheta_directed_mem_and_bound`](https://leanpool.github.io/lean-pool/LeanPool/DavisKahan/Solution.html#RotationOfEigenvectors.sinTwoTheta_directed_mem_and_bound) (theorem), declared in [LeanPool/DavisKahan/Solution.lean, line 461](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DavisKahan/Solution.lean#L461): “Under the printed oriented gap and common-domain self-adjointness hypotheses, finite symmetric residual norm gives directed sine-double-angle ideal membership, and twice the residual norm bounds the gap times its norm.”
- [`RotationOfEigenvectors.sinTwoTheta_ambient_mem_and_bound`](https://leanpool.github.io/lean-pool/LeanPool/DavisKahan/Solution.html#RotationOfEigenvectors.sinTwoTheta_ambient_mem_and_bound) (theorem), declared in [LeanPool/DavisKahan/Solution.lean, line 536](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DavisKahan/Solution.lean#L536): “Finite symmetric perturbation norm gives ambient sine-double-angle ideal membership and the whole-space gap bound under the theorem's reducing and perturbed-gap hypotheses.”
- [`RotationOfEigenvectors.tanTwoTheta`](https://leanpool.github.io/lean-pool/LeanPool/DavisKahan/Solution.html#RotationOfEigenvectors.tanTwoTheta) (theorem), declared in [LeanPool/DavisKahan/Solution.lean, line 603](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DavisKahan/Solution.lean#L603): “The residual tangent-double-angle estimate holds with the theorem’s source-facing block hypotheses.”

## Project

- Authors: Jon Crall, Edward Wang.
- Project repository: [aiq-kitware/aiq-davis-kahan-1970-rotation-eigenvectgors-perturbation-formalization](https://github.com/aiq-kitware/aiq-davis-kahan-1970-rotation-eigenvectgors-perturbation-formalization), at commit [38e37da6](https://github.com/aiq-kitware/aiq-davis-kahan-1970-rotation-eigenvectgors-perturbation-formalization/tree/38e37da6e147cd0016da1eb05987c3edf7d95b39).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 47A55, 47A15, 15A42.
- In Lean Pool: [LeanPool/DavisKahan](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DavisKahan), from the card [LeanPool/projects/aiq-davis-kahan-1970-rotation-eigenvectgors-perturbation-formalization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/aiq-davis-kahan-1970-rotation-eigenvectgors-perturbation-formalization.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/aiq-davis-kahan-1970-rotation-eigenvectgors-perturbation-formalization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/aiq-davis-kahan-1970-rotation-eigenvectgors-perturbation-formalization.yaml)
- [Lean Pool at 2b205bf9: LeanPool/DavisKahan](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DavisKahan)
