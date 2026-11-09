---
declaration: theorem
origin: cited
lean: Chvatal.chvatal, Chvatal.sharp_correlation
statement: formalized
proof: formalized
---

# Chvátal's conjecture and sharp Boolean correlation

> Formalizes Chang, Liu, and Liu's proof that a hereditary family on a finite nonempty ground set has a largest intersecting subfamily that is a star. Develops the sharp Boolean Fourier correlation inequality, its antipodal and quadratic forms, sharpness examples, and the weighted star theorem for nonnegative decreasing weights.

*Quoted from the card [LeanPool/projects/chvatal-conjecture.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/chvatal-conjecture.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Chvatal.chvatal`](https://leanpool.github.io/lean-pool/LeanPool/Chvatal/Main.html#Chvatal.chvatal) (theorem; a main declaration), declared in [LeanPool/Chvatal/Main.lean, line 131](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Chvatal/Main.lean#L131): “Every intersecting subfamily A of a hereditary finite family D on a finite nonempty ground type has cardinality at most that of some star of D.”
- [`Chvatal.exists_largest_intersecting_star`](https://leanpool.github.io/lean-pool/LeanPool/Chvatal/Main.html#Chvatal.exists_largest_intersecting_star) (theorem), declared in [LeanPool/Chvatal/Main.lean, line 140](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Chvatal/Main.lean#L140): “One star of D is itself intersecting and simultaneously dominates all intersecting subfamilies of the hereditary family D in size, on a finite nonempty ground type.”
- [`Chvatal.sharp_correlation`](https://leanpool.github.io/lean-pool/LeanPool/Chvatal/Main.html#Chvatal.sharp_correlation) (theorem; a main declaration), declared in [LeanPool/Chvatal/Main.lean, line 82](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Chvatal/Main.lean#L82): “For increasing Boolean functions f and g on any finite cube, the sum of squared Fourier coefficients of g weighted by the largest influence of f on each nonempty index is at most the harmonic mean of Cov(f,g) and Cov(f,g\*), with zero-denominator value zero.”
- [`Chvatal.two_spectral_le_quadratic_covariance`](https://leanpool.github.io/lean-pool/LeanPool/Chvatal/Correlation.html#Chvatal.two_spectral_le_quadratic_covariance) (theorem), declared in [LeanPool/Chvatal/Correlation.lean, line 214](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Chvatal/Correlation.lean#L214): “For increasing Boolean f and g and every real t, twice their squared Fourier energy over index pairs with odd intersection is bounded by t^2 Cov(f,g) + (1-t)^2 Cov(f,g\*).”
- [`Chvatal.antipodal_correlation`](https://leanpool.github.io/lean-pool/LeanPool/Chvatal/Main.html#Chvatal.antipodal_correlation) (theorem), declared in [LeanPool/Chvatal/Main.lean, line 114](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Chvatal/Main.lean#L114): “If g is also self-dual and the finite coordinate type is nonempty, Cov(f,g) is at least one quarter of f's minimum coordinate influence.”
- [`Chvatal.andFunction_sharp`](https://leanpool.github.io/lean-pool/LeanPool/Chvatal/Sharpness.html#Chvatal.andFunction_sharp) (theorem), declared in [LeanPool/Chvatal/Sharpness.lean, line 192](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Chvatal/Sharpness.lean#L192): “The AND function attains equality in the sharp correlation bound for every increasing Boolean second function, including constants.”
- [`Chvatal.exists_largest_weighted_intersecting_star`](https://leanpool.github.io/lean-pool/LeanPool/Chvatal/Weighted.html#Chvatal.exists_largest_weighted_intersecting_star) (theorem), declared in [LeanPool/Chvatal/Weighted.lean, line 347](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Chvatal/Weighted.lean#L347): “For any nonnegative antitone real weight on subsets of a finite nonempty ground type, one full-cube star is intersecting and its total weight dominates every intersecting family.”

## Project

- Authors: Boon Suan Ho, Chvatal formalization contributors.
- Source: *A proof of Chvátal's conjecture via a sharp correlation inequality* by Fan Chang, Hong Liu, Miao Liu, [arXiv:2609.19123v1](https://arxiv.org/abs/2609.19123v1).
- Project repository: [boonsuan/chvatal](https://github.com/boonsuan/chvatal), at commit [c19ed3aa](https://github.com/boonsuan/chvatal/tree/c19ed3aaac9e42d446f963a862d39d8a09eddbf9).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 05D05, 60E15.
- In Lean Pool: [LeanPool/Chvatal](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Chvatal), from the card [LeanPool/projects/chvatal-conjecture.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/chvatal-conjecture.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/chvatal-conjecture.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/chvatal-conjecture.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Chvatal](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Chvatal)
