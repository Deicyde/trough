---
declaration: theorem
origin: cited
lean: IsTranscendentalPi, IsTranscendentalPiReal
statement: formalized
proof: formalized
---

# The transcendence of π

> Formalizes a self-contained proof, following Niven's 1939 argument, that the real and complex number π is transcendental over the rationals.

*Quoted from the card [LeanPool/projects/istranscendentalpi.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/istranscendentalpi.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`IsTranscendentalPi`](https://leanpool.github.io/lean-pool/LeanPool/IsTranscendentalPi/Main.html#IsTranscendentalPi) (theorem; a main declaration), declared in [LeanPool/IsTranscendentalPi/Main.lean, line 50](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/IsTranscendentalPi/Main.lean#L50): “Proves that the complex number π is transcendental over ℚ.”
- [`IsTranscendentalPiReal`](https://leanpool.github.io/lean-pool/LeanPool/IsTranscendentalPi/Main.html#IsTranscendentalPiReal) (theorem; a main declaration), declared in [LeanPool/IsTranscendentalPi/Main.lean, line 117](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/IsTranscendentalPi/Main.lean#L117): “Proves that the real number π is transcendental over ℚ.”
- [`isAlgebraic_I_mul_pi_of_isAlgebraic_pi`](https://leanpool.github.io/lean-pool/LeanPool/IsTranscendentalPi/Main.html#isAlgebraic_I_mul_pi_of_isAlgebraic_pi) (lemma), declared in [LeanPool/IsTranscendentalPi/Main.lean, line 38](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/IsTranscendentalPi/Main.lean#L38): “Shows that if π is algebraic over ℚ then so is iπ.”
- [`exists_monic_rat_poly_aeval_Ipi_eq_zero`](https://leanpool.github.io/lean-pool/LeanPool/IsTranscendentalPi/Main.html#exists_monic_rat_poly_aeval_Ipi_eq_zero) (lemma), declared in [LeanPool/IsTranscendentalPi/Main.lean, line 43](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/IsTranscendentalPi/Main.lean#L43): “Produces a monic rational polynomial vanishing at iπ when iπ is algebraic.”

## Project

- Authors: James Huang, Samuël Borza.
- Project repository: [samuelborza/IsTranscendentalPi](https://github.com/samuelborza/IsTranscendentalPi).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 11A41.
- In Lean Pool: [LeanPool/IsTranscendentalPi](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/IsTranscendentalPi), from the card [LeanPool/projects/istranscendentalpi.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/istranscendentalpi.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/istranscendentalpi.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/istranscendentalpi.yaml)
- [Lean Pool at 701389c0: LeanPool/IsTranscendentalPi](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/IsTranscendentalPi)
