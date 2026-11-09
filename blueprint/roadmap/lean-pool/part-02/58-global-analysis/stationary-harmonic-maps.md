---
declaration: structure
origin: cited
lean: LeanStationaryHarmonicMaps.StationaryHarmonicMap.StationaryW12LocMap
statement: formalized
---

# Monotonicity Formula for Stationary Harmonic Maps

> Formalizes the monotonicity formula for stationary `W^{1,2}_{loc}` maps with Euclidean target. The proof is target independent: it uses only the displayed weak gradient and a vanishing domain first variation, so no target-manifold structure enters the argument. From a bundled stationary Sobolev witness `StationaryW12LocMap u Omega` it proves, for `0 < s <= r < R0`, that the normalized energy `Theta(Du, a, rho) = rho^(2-n) * integral over B(a, rho) of |Du|^2` is monotone: `weakTheta Du a s <= weakTheta Du a r`, together with the exact increment formula `weakTheta Du a r - weakTheta Du a s = weakMonotonicityRhs Du a s r`. The Sobolev layer is project-defined from Mathlib's `MemLp`, weak-derivative identities, Bochner integration, and Euclidean measure theory, following the De Giorgi-Nash-Moser engineering choice; the internal proof routes through a radial vector-field first variation, a coarea/Radon-Nikodym radius representation, smooth radial cutoffs, and an absolute-continuity boundary step.

*Quoted from the card [LeanPool/projects/stationary-harmonic-maps.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/stationary-harmonic-maps.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanStationaryHarmonicMaps.StationaryHarmonicMap.StationaryW12LocMap`](https://leanpool.github.io/lean-pool/LeanPool/LeanStationaryHarmonicMaps/StationaryHarmonicMap/StationaryMap.html#LeanStationaryHarmonicMaps.StationaryHarmonicMap.StationaryW12LocMap) (structure; a main declaration), declared in [LeanPool/LeanStationaryHarmonicMaps/StationaryHarmonicMap/StationaryMap.lean, line 37](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanStationaryHarmonicMaps/StationaryHarmonicMap/StationaryMap.lean#L37): “The public input package: a domain-variation stationary `W^{1,2}_{loc}` Sobolev map bundling a chosen weak gradient (`W12LocMapWitness`) with the vanishing domain first-variation identity. This is the object users construct to invoke the monotonicity theorem.”
- [`LeanStationaryHarmonicMaps.StationaryHarmonicMap.stationaryW12LocMonotonicity_euclidean`](https://leanpool.github.io/lean-pool/LeanPool/LeanStationaryHarmonicMaps/StationaryHarmonicMap/MainTheorem.html#LeanStationaryHarmonicMaps.StationaryHarmonicMap.stationaryW12LocMonotonicity_euclidean) (theorem), declared in [LeanPool/LeanStationaryHarmonicMaps/StationaryHarmonicMap/MainTheorem.lean, line 56](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanStationaryHarmonicMaps/StationaryHarmonicMap/MainTheorem.lean#L56): “Witness-style monotonicity: from a stationary `W^{1,2}_{loc}` map package, the normalized weak energy `weakTheta` is monotone in the radius, `weakTheta Du a s <= weakTheta Du a r` for `0 < s <= r < R0`.”
- [`LeanStationaryHarmonicMaps.StationaryHarmonicMap.stationaryW12LocMonotonicityFormula_euclidean`](https://leanpool.github.io/lean-pool/LeanPool/LeanStationaryHarmonicMaps/StationaryHarmonicMap/MainTheorem.html#LeanStationaryHarmonicMaps.StationaryHarmonicMap.stationaryW12LocMonotonicityFormula_euclidean) (theorem), declared in [LeanPool/LeanStationaryHarmonicMaps/StationaryHarmonicMap/MainTheorem.lean, line 34](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanStationaryHarmonicMaps/StationaryHarmonicMap/MainTheorem.lean#L34): “Witness-style monotonicity formula: the increment of `weakTheta` equals the nonnegative annular radial-energy term, `weakTheta Du a r - weakTheta Du a s = weakMonotonicityRhs Du a s r` for `0 < s < r < R0`.”
- [`LeanStationaryHarmonicMaps.StationaryHarmonicMap.stationarySobolevMonotonicity_euclidean`](https://leanpool.github.io/lean-pool/LeanPool/LeanStationaryHarmonicMaps/StationaryHarmonicMap/API.html#LeanStationaryHarmonicMaps.StationaryHarmonicMap.stationarySobolevMonotonicity_euclidean) (theorem), declared in [LeanPool/LeanStationaryHarmonicMaps/StationaryHarmonicMap/API.lean, line 87](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanStationaryHarmonicMaps/StationaryHarmonicMap/API.lean#L87): “Componentwise convenience wrapper: the same monotonicity inequality stated directly from the local `L^2`, measurability, weak-gradient, and first-variation hypotheses, without first constructing the witness package.”

## Project

- Authors: Wei Wang.
- Source: *Theorems on Regularity and Singularity of Energy Minimizing Maps* by Leon Simon, [doi:10.1007/978-3-0348-9193-6](https://doi.org/10.1007/978-3-0348-9193-6).
- Project repository: [BrookWW/LeanStationaryHarmonicMaps](https://github.com/BrookWW/LeanStationaryHarmonicMaps).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 58E20, 35J50.
- In Lean Pool: [LeanPool/LeanStationaryHarmonicMaps](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanStationaryHarmonicMaps), from the card [LeanPool/projects/stationary-harmonic-maps.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/stationary-harmonic-maps.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/stationary-harmonic-maps.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/stationary-harmonic-maps.yaml)
- [Lean Pool at 2b205bf9: LeanPool/LeanStationaryHarmonicMaps](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanStationaryHarmonicMaps)
