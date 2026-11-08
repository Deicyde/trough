---
declaration: theorem
origin: cited
lean: ChannelCapacity.exists_unique_capacity_achieving_prior_of_finite
statement: formalized
proof: formalized
---

# Uniqueness of Shannon Capacity-Achieving Priors

> Formalizes uniqueness of the capacity-achieving input distribution for a Markov-kernel channel in three aligned layers: a finite-alphabet theorem (compactness, continuity, and strict concavity of mutual information on Mathlib's weak topology for `ProbabilityMeasure`), a concrete discharged theorem for compact-Polish channels with a common strictly positive jointly continuous density, and a general measure-theoretic packaging that isolates the abstract well-conditioning hypotheses, plus a counterexample showing pairwise-distinct rows do not give an injective prior pushforward (the non-degeneracy required for uniqueness).

*Quoted from the card [LeanPool/projects/channel-capacity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/channel-capacity.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`ChannelCapacity.exists_unique_capacity_achieving_prior_of_finite`](https://leanpool.github.io/lean-pool/LeanPool/ChannelCapacity/Finite.html#ChannelCapacity.exists_unique_capacity_achieving_prior_of_finite) (theorem; a main declaration), declared in [LeanPool/ChannelCapacity/Finite.lean, line 632](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ChannelCapacity/Finite.lean#L632): “For a Markov kernel between finite alphabets (nonempty input) whose rows are linearly independent (`Kernel.RowMatrixFullRank`), a capacity-achieving input prior exists and is unique.” Its source, as the card gives it: “R. G. Gallager, Information Theory and Reliable Communication, Wiley, 1968, Section 4.5.”
- [`ChannelCapacity.exists_unique_capacity_achieving_prior_discharged`](https://leanpool.github.io/lean-pool/LeanPool/ChannelCapacity/Discharged.html#ChannelCapacity.exists_unique_capacity_achieving_prior_discharged) (theorem), declared in [LeanPool/ChannelCapacity/Discharged.lean, line 419](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ChannelCapacity/Discharged.lean#L419): “For compact-Polish channels with a common strictly positive jointly continuous density, given injectivity of the prior-pushforward map and upper semicontinuity of mutual information (the latter carried as a field of `Kernel.ContinuousPositiveDensity`, not derived), the capacity-achieving prior is unique.”
- [`ChannelCapacity.exists_unique_capacity_achieving_prior`](https://leanpool.github.io/lean-pool/LeanPool/ChannelCapacity/Capacity.html#ChannelCapacity.exists_unique_capacity_achieving_prior) (theorem), declared in [LeanPool/ChannelCapacity/Capacity.lean, line 78](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ChannelCapacity/Capacity.lean#L78): “General measure-theoretic packaging: under abstract well-conditioning hypotheses, the capacity-achieving prior is unique.”

## Project

- Authors: Adam Benenson.
- Source: *Elements of Information Theory* by Thomas M. Cover, Joy A. Thomas, [doi:10.1002/047174882X](https://doi.org/10.1002/047174882X).
- Project repository: [abenenson/channel-capacity](https://github.com/abenenson/channel-capacity).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 94A17, 94A15, 60A10.
- In Lean Pool: [LeanPool/ChannelCapacity](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ChannelCapacity), from the card [LeanPool/projects/channel-capacity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/channel-capacity.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/channel-capacity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/channel-capacity.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ChannelCapacity](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ChannelCapacity)
