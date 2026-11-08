---
declaration: theorem
origin: cited
lean: Mathoverflow1973.mathoverflow_1973
statement: formalized
proof: formalized
---

# A complex structure on the six-sphere

> Formalizes Levent Alpöge's construction of a complex-analytic atlas on the standard six-sphere. The development builds a compact complex threefold from torus fibrations with cusp and elliptic fibres, computes its homology and fundamental group, proves that its underlying topological space is homeomorphic to the six-sphere, and transports the complex atlas across that homeomorphism. It adapts Lean developments by Yury G. Kudryashov and Sebastian Kumar, together with the statement from the Formal Conjectures Authors.

*Quoted from the card [LeanPool/projects/hopf-problem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/hopf-problem.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Mathoverflow1973.SixSphereComplexAtlas.exists_complex_analytic_atlas`](https://leanpool.github.io/lean-pool/LeanPool/HopfProblem/Threefold/SixSphereComplexAtlas.html#Mathoverflow1973.SixSphereComplexAtlas.exists_complex_analytic_atlas) (theorem), declared in [LeanPool/HopfProblem/Threefold/SixSphereComplexAtlas.lean, line 68](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HopfProblem/Threefold/SixSphereComplexAtlas.lean#L68): “The standard unit six-sphere admits a complex three-dimensional charted-space structure making it a complex-analytic manifold.”
- [`Mathoverflow1973.SixSphereComplexAtlas.exists_complex_atlas`](https://leanpool.github.io/lean-pool/LeanPool/HopfProblem/Threefold/SixSphereComplexAtlas.html#Mathoverflow1973.SixSphereComplexAtlas.exists_complex_atlas) (theorem), declared in [LeanPool/HopfProblem/Threefold/SixSphereComplexAtlas.lean, line 83](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HopfProblem/Threefold/SixSphereComplexAtlas.lean#L83): “The standard unit six-sphere admits a complex three-dimensional charted-space structure making it a continuously differentiable complex manifold.”
- [`Mathoverflow1973.mathoverflow_1973`](https://leanpool.github.io/lean-pool/LeanPool/HopfProblem/MainTheorem/Core3.html#Mathoverflow1973.mathoverflow_1973) (theorem; a main declaration), declared in [LeanPool/HopfProblem/MainTheorem/Core3.lean, line 37](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HopfProblem/MainTheorem/Core3.lean#L37): “The formalized statement of MathOverflow question 1973: the standard six-sphere carries a complex three-dimensional manifold atlas.”

## Project

- Authors: Boris Alexeev, Yury G. Kudryashov, Sebastian Kumar, The Formal Conjectures Authors.
- Source: *HopfProblem: formalization of Alpöge's six-sphere construction* by Boris Alexeev, [https://github.com/plby/HopfProblem/tree/9ac8a456b526527837d7082ff775213ca8bc9809](https://github.com/plby/HopfProblem/tree/9ac8a456b526527837d7082ff775213ca8bc9809).
- Project repository: [plby/HopfProblem](https://github.com/plby/HopfProblem), at commit [9ac8a456](https://github.com/plby/HopfProblem/tree/9ac8a456b526527837d7082ff775213ca8bc9809).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 32Q55, 57R15.
- In Lean Pool: [LeanPool/HopfProblem](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HopfProblem), from the card [LeanPool/projects/hopf-problem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/hopf-problem.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/hopf-problem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/hopf-problem.yaml)
- [Lean Pool at 2b205bf9: LeanPool/HopfProblem](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HopfProblem)
