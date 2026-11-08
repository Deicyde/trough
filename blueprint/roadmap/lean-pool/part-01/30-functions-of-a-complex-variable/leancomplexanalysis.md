---
declaration: theorem
origin: cited
lean: LeanPool.LeanComplexAnalysis.harnack_ineq
statement: formalized
proof: formalized
---

# Formalized Complex Analysis in Lean

> Formalizes Poisson integral formulas on the unit disc and arbitrary centered discs, Herglotz–Riesz representation, and Harnack's inequality on the unit disc, plus infrastructure for univalent function classes S and Σ.

*Quoted from the card [LeanPool/projects/leancomplexanalysis.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/leancomplexanalysis.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`LeanPool.LeanComplexAnalysis.poisson_integral_of_harmonicOn_unitDisc_continuousOn_closedUnitDisc`](https://leanpool.github.io/lean-pool/LeanPool/LeanComplexAnalysis/Harmonic/PoissonIntegral.html#LeanPool.LeanComplexAnalysis.poisson_integral_of_harmonicOn_unitDisc_continuousOn_closedUnitDisc) (theorem), declared in [LeanPool/LeanComplexAnalysis/Harmonic/PoissonIntegral.lean, line 401](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanComplexAnalysis/Harmonic/PoissonIntegral.lean#L401): “Proves the Poisson integral formula for harmonic functions on the unit disc.”
- [`LeanPool.LeanComplexAnalysis.poisson_integral_of_harmonicOn_disc_continuousOn_closedDisc`](https://leanpool.github.io/lean-pool/LeanPool/LeanComplexAnalysis/Harmonic/PoissonIntegral2.html#LeanPool.LeanComplexAnalysis.poisson_integral_of_harmonicOn_disc_continuousOn_closedDisc) (theorem), declared in [LeanPool/LeanComplexAnalysis/Harmonic/PoissonIntegral2.lean, line 418](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanComplexAnalysis/Harmonic/PoissonIntegral2.lean#L418): “Proves the Poisson integral formula for harmonic functions on arbitrary centered discs.”
- [`LeanPool.LeanComplexAnalysis.HerglotzRiesz_representation_harmonic`](https://leanpool.github.io/lean-pool/LeanPool/LeanComplexAnalysis/Harmonic/Positive/HerglotzRieszRepresentations.html#LeanPool.LeanComplexAnalysis.HerglotzRiesz_representation_harmonic) (theorem), declared in [LeanPool/LeanComplexAnalysis/Harmonic/Positive/HerglotzRieszRepresentations.lean, line 993](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanComplexAnalysis/Harmonic/Positive/HerglotzRieszRepresentations.lean#L993): “Proves that every positive harmonic function on the unit disc with value 1 at 0 has a unique Herglotz–Riesz representation by a probability measure on the unit circle.”
- [`LeanPool.LeanComplexAnalysis.harnack_ineq`](https://leanpool.github.io/lean-pool/LeanPool/LeanComplexAnalysis/Harmonic/Positive/HarnackIneq.html#LeanPool.LeanComplexAnalysis.harnack_ineq) (theorem; a main declaration), declared in [LeanPool/LeanComplexAnalysis/Harmonic/Positive/HarnackIneq.lean, line 276](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanComplexAnalysis/Harmonic/Positive/HarnackIneq.lean#L276): “Proves Harnack's inequality for positive harmonic functions on the unit disc.”

## Project

- Authors: seb488, Aristotle.
- Project repository: [seb488/LeanComplexAnalysis](https://github.com/seb488/LeanComplexAnalysis).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 30A99, 31A05, 30C55.
- In Lean Pool: [LeanPool/LeanComplexAnalysis](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanComplexAnalysis), from the card [LeanPool/projects/leancomplexanalysis.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/leancomplexanalysis.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/leancomplexanalysis.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/leancomplexanalysis.yaml)
- [Lean Pool at 2b205bf9: LeanPool/LeanComplexAnalysis](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanComplexAnalysis)
