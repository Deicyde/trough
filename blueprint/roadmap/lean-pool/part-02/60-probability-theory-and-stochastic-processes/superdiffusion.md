---
declaration: theorem
origin: cited
lean: Algsuperdiff.superdiffusivity_with_finite_moments
statement: formalized
proof: formalized
---

# Superdiffusion and anomalous regularization in self-similar random flows

> Proves quenched displacement-moment estimates, quantitative generator renormalization and anomalous large-scale elliptic regularity for random incompressible flows satisfying the ABK shell-law assumptions. The shell carrier has continuous second derivatives, a stronger qualitative regularity assumption than the paper's local C^{1,1} assumption. The model hypotheses are explicit; the Gaussian example is not constructed. Preserves the production dependency closure, including sensitivity, diffusivity recursion, concentration and divergence-form process theory. Reuses the pooled homogenization and Markov-process libraries. A public companion theorem proves finiteness of the first and second displacement observables used in the superdiffusivity statement. Additional proofs establish measurable dependence of the transition law and quenched displacement expectations on the environment.

*Quoted from the card [LeanPool/projects/superdiffusion.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/superdiffusion.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Algsuperdiff.superdiffusivity_with_finite_moments`](https://leanpool.github.io/lean-pool/LeanPool/Superdiffusion/Algsuperdiff/SuperdiffusivityFiniteMoments.html#Algsuperdiff.superdiffusivity_with_finite_moments) (theorem; a main declaration), declared in [LeanPool/Superdiffusion/Algsuperdiff/SuperdiffusivityFiniteMoments.lean, line 30](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Superdiffusion/Algsuperdiff/SuperdiffusivityFiniteMoments.lean#L30): “For dimensions at least two, one positive small-coupling threshold simultaneously gives the full quantitative superdiffusivity bounds and almost-sure integrability of both displacement observables at every positive time.”
- [`Algsuperdiff.superdiffusivity`](https://leanpool.github.io/lean-pool/LeanPool/Superdiffusion/Algsuperdiff/MainTheorems.html#Algsuperdiff.superdiffusivity) (theorem), declared in [LeanPool/Superdiffusion/Algsuperdiff/MainTheorems.lean, line 104](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Superdiffusion/Algsuperdiff/MainTheorems.lean#L104): “For each dimension and positive nondegeneracy constant, sufficiently small coupling gives annealed moment bounds for the quenched second displacement moment about the intrinsic superdiffusive scale and for the squared quenched mean displacement, uniformly at all positive times and throughout the stated coupling-dependent moment range.”
- [`Algsuperdiff.generator_renormalization`](https://leanpool.github.io/lean-pool/LeanPool/Superdiffusion/Algsuperdiff/MainTheorems.html#Algsuperdiff.generator_renormalization) (theorem), declared in [LeanPool/Superdiffusion/Algsuperdiff/MainTheorems.lean, line 156](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Superdiffusion/Algsuperdiff/MainTheorems.lean#L156): “At every triadic scale, the effective diffusivity tracks the predicted superdiffusive profile. One measurable random error with quantitative moment bounds controls both the essential uniform difference and the energy difference between random and homogenized Dirichlet solutions for all admissible forcing and boundary data.”
- [`Algsuperdiff.anomalous_regularity`](https://leanpool.github.io/lean-pool/LeanPool/Superdiffusion/Algsuperdiff/MainTheorems.html#Algsuperdiff.anomalous_regularity) (theorem), declared in [LeanPool/Superdiffusion/Algsuperdiff/MainTheorems.lean, line 235](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Superdiffusion/Algsuperdiff/MainTheorems.lean#L235): “At every scale and admissible Hölder exponent, a random minimal scale with an exponential tail yields large-scale excess-decay estimates for Dirichlet solutions, uniformly in molecular diffusivity, with the boundary-data term absent in the interior subcube.”
- [`Algsuperdiff.Section5.Provider.exists_ae_integrable_streamProcess_displacement`](https://leanpool.github.io/lean-pool/LeanPool/Superdiffusion/Algsuperdiff/Section5/Provider/DisplacementIntegrability.html#Algsuperdiff.Section5.Provider.exists_ae_integrable_streamProcess_displacement) (theorem), declared in [LeanPool/Superdiffusion/Algsuperdiff/Section5/Provider/DisplacementIntegrability.lean, line 64](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Superdiffusion/Algsuperdiff/Section5/Provider/DisplacementIntegrability.lean#L64): “For dimensions at least two and sufficiently small coupling, at every positive time the first and second displacement observables of the constructed process are integrable for almost every environment.”
- [`Algsuperdiff.Section5.Measurability.measurable_streamProcess_displacement_expectations`](https://leanpool.github.io/lean-pool/LeanPool/Superdiffusion/Algsuperdiff/Section5/Measurability/DisplacementExpectations.html#Algsuperdiff.Section5.Measurability.measurable_streamProcess_displacement_expectations) (theorem), declared in [LeanPool/Superdiffusion/Algsuperdiff/Section5/Measurability/DisplacementExpectations.lean, line 115](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Superdiffusion/Algsuperdiff/Section5/Measurability/DisplacementExpectations.lean#L115): “The first and second quenched displacement expectations of the constructed process are measurable functions of the environment.”

## Project

- Authors: Scott Armstrong, Tuomo Kuusi.
- Source: [arXiv:2601.22142](https://arxiv.org/abs/2601.22142).
- Project repository: [scottnarmstrong/Superdiffusion](https://github.com/scottnarmstrong/Superdiffusion), at commit [7f204763](https://github.com/scottnarmstrong/Superdiffusion/tree/7f20476385d4af418f110303085ad0740c9eba46).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 60K37, 35B27, 60J60.
- In Lean Pool: [LeanPool/Superdiffusion](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Superdiffusion), from the card [LeanPool/projects/superdiffusion.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/superdiffusion.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/superdiffusion.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/superdiffusion.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Superdiffusion](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Superdiffusion)
