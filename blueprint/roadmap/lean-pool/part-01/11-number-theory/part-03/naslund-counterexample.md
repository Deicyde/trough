---
declaration: theorem
origin: cited
lean: NaslundCounterexample.conjecture_fails, NaslundCounterexample.liminf_ge
statement: formalized
proof: formalized
---

# Square-difference-free polynomials beyond Naslund's conjectured bound

> Constructs square-difference-free subsets of polynomials over the field with three elements that refute Naslund's Conjecture 13 at every degree bound divisible by four and at least eight. An explicit degree-eight lift multiplies cardinality by 810 and yields a lower bound of 16/21 for the lower limiting normalized logarithmic growth rate.

*Quoted from the card [LeanPool/projects/naslund-counterexample.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/naslund-counterexample.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`NaslundCounterexample.exists_card_810`](https://leanpool.github.io/lean-pool/LeanPool/NaslundCounterexample/Main.html#NaslundCounterexample.exists_card_810) (theorem), declared in [LeanPool/NaslundCounterexample/Main.lean, line 40](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NaslundCounterexample/Main.lean#L40): “There is a square-difference-free set of 810 polynomials over F_3 with degree less than eight.”
- [`NaslundCounterexample.conjecture_fails_at_eight`](https://leanpool.github.io/lean-pool/LeanPool/NaslundCounterexample/Main.html#NaslundCounterexample.conjecture_fails_at_eight) (theorem), declared in [LeanPool/NaslundCounterexample/Main.lean, line 50](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NaslundCounterexample/Main.lean#L50): “The upper bound 3^6 = 729 in Naslund's Conjecture 13 fails for square differences over F_3 at degree bound eight.”
- [`NaslundCounterexample.exists_card_pow`](https://leanpool.github.io/lean-pool/LeanPool/NaslundCounterexample/Main.html#NaslundCounterexample.exists_card_pow) (theorem), declared in [LeanPool/NaslundCounterexample/Main.lean, line 61](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NaslundCounterexample/Main.lean#L61): “For every positive integer e, there is a square-difference-free set of 810^e polynomials over F_3 with degree less than 8e.”
- [`NaslundCounterexample.exists_card_twenty_seven_mul_pow`](https://leanpool.github.io/lean-pool/LeanPool/NaslundCounterexample/Main.html#NaslundCounterexample.exists_card_twenty_seven_mul_pow) (theorem), declared in [LeanPool/NaslundCounterexample/Main.lean, line 70](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NaslundCounterexample/Main.lean#L70): “For every natural number e, there is a square-difference-free set of 27 times 810^e polynomials over F_3 with degree less than 8e + 4.”
- [`NaslundCounterexample.conjecture_fails`](https://leanpool.github.io/lean-pool/LeanPool/NaslundCounterexample/Main.html#NaslundCounterexample.conjecture_fails) (theorem; a main declaration), declared in [LeanPool/NaslundCounterexample/Main.lean, line 80](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NaslundCounterexample/Main.lean#L80): “For every n divisible by four with n at least eight, there is a square-difference-free set of polynomials over F_3 of degree less than n whose cardinality exceeds 3^(3n/4).”
- [`NaslundCounterexample.liminf_ge`](https://leanpool.github.io/lean-pool/LeanPool/NaslundCounterexample/Asymptotics.html#NaslundCounterexample.liminf_ge) (theorem; a main declaration), declared in [LeanPool/NaslundCounterexample/Asymptotics.lean, line 196](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NaslundCounterexample/Asymptotics.lean#L196): “If D(n) is the largest cardinality of a square-difference-free set of polynomials over F_3 of degree less than n, then the lower limit of log D(n) divided by n log 3 is at least 16/21.”

## Project

- Authors: JD Jones.
- Source: *Square-difference-free sets in F_3[T] past the conjectured bound* by JD Jones.
- Project repository: [JD-Jones-ASES/ns-lean](https://github.com/JD-Jones-ASES/ns-lean), at commit [035e9b0c](https://github.com/JD-Jones-ASES/ns-lean/tree/035e9b0c147630e35631e4401433660f695d1fba).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 11B75, 05D05.
- In Lean Pool: [LeanPool/NaslundCounterexample](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NaslundCounterexample), from the card [LeanPool/projects/naslund-counterexample.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/naslund-counterexample.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/naslund-counterexample.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/naslund-counterexample.yaml)
- [Lean Pool at 2b205bf9: LeanPool/NaslundCounterexample](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NaslundCounterexample)
