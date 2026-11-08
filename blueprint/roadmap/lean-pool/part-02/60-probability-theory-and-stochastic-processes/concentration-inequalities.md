---
declaration: theorem
origin: cited
lean: Contrib.Freedman.subgamma_bernstein_tail
statement: formalized
proof: formalized
---

# Bennett--Bernstein, Freedman, and Hoeffding concentration inequalities

> Develops variance-sensitive sub-gamma moment-generating-function estimates, Bennett and Bernstein bounds, a Freedman--Bernstein upper tail for finite adapted sums, conditional and independent-variable Hoeffding inequalities.

*Quoted from the card [LeanPool/projects/concentration-inequalities.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/concentration-inequalities.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Contrib.Bennett.hasSubgammaMGF_of_bounded_above`](https://leanpool.github.io/lean-pool/LeanPool/ConcentrationInequalities/BennettBernstein.html#Contrib.Bennett.hasSubgammaMGF_of_bounded_above) (theorem), declared in [LeanPool/ConcentrationInequalities/BennettBernstein.lean, line 485](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ConcentrationInequalities/BennettBernstein.lean#L485): “A centered real random variable bounded above by a positive constant, with bounded second moment, satisfies a Bennett--Bernstein sub-gamma moment-generating-function estimate.”
- [`Contrib.Freedman.subgamma_bernstein_tail`](https://leanpool.github.io/lean-pool/LeanPool/ConcentrationInequalities/FreedmanBernstein.html#Contrib.Freedman.subgamma_bernstein_tail) (theorem; a main declaration), declared in [LeanPool/ConcentrationInequalities/FreedmanBernstein.lean, line 352](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ConcentrationInequalities/FreedmanBernstein.lean#L352): “A finite adapted sum of conditionally sub-gamma increments satisfies the corresponding variance-sensitive Freedman--Bernstein upper-tail bound.”
- [`Contrib.ConditionalHoeffding.hasCondSubgaussianMGF_of_mem_Icc`](https://leanpool.github.io/lean-pool/LeanPool/ConcentrationInequalities/ConditionalHoeffding.html#Contrib.ConditionalHoeffding.hasCondSubgaussianMGF_of_mem_Icc) (theorem), declared in [LeanPool/ConcentrationInequalities/ConditionalHoeffding.lean, line 41](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ConcentrationInequalities/ConditionalHoeffding.lean#L41): “A bounded random variable with zero conditional expectation satisfies a conditional Hoeffding sub-Gaussian moment-generating-function estimate.”
- [`Contrib.Hoeffding.hoeffding_upper`](https://leanpool.github.io/lean-pool/LeanPool/ConcentrationInequalities/HoeffdingUpper.html#Contrib.Hoeffding.hoeffding_upper) (theorem), declared in [LeanPool/ConcentrationInequalities/HoeffdingUpper.lean, line 63](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ConcentrationInequalities/HoeffdingUpper.lean#L63): “A sum of finitely many independent random variables valued in the unit interval exceeds its mean by t with probability at most exp(-2 t squared divided by the number of terms).”

## Project

- Authors: Juan Pablo Traverso Gianini, Aristotle.
- Source: *Reusable concentration-inequality components accompanying Linear-Error Clique Partitions of Split Graphs via Structured Triangle Packing* by Juan Pablo Traverso Gianini, [https://github.com/jtraverso/erdos-81-chordal-clique-partitions/blob/b3423f3e8c8db7c2d1b279673293ef3079faf903/preprints/PAPER_III/05_formalization/lean_v1.4_freeze/Contrib/FreedmanBernstein.lean](https://github.com/jtraverso/erdos-81-chordal-clique-partitions/blob/b3423f3e8c8db7c2d1b279673293ef3079faf903/preprints/PAPER_III/05_formalization/lean_v1.4_freeze/Contrib/FreedmanBernstein.lean).
- Project repository: [jtraverso/erdos-81-chordal-clique-partitions](https://github.com/jtraverso/erdos-81-chordal-clique-partitions).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 60E15, 60G42.
- In Lean Pool: [LeanPool/ConcentrationInequalities](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ConcentrationInequalities), from the card [LeanPool/projects/concentration-inequalities.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/concentration-inequalities.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/concentration-inequalities.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/concentration-inequalities.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ConcentrationInequalities](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ConcentrationInequalities)
