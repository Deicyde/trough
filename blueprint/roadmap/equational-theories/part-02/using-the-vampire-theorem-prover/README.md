# Using the Vampire theorem prover

[1,775 implications](https://github.com/teorth/equational_theories/tree/main/equational_theories/Generated/VampireProven/) were proven using the Vampire theorem prover.

The Vampire proofs were found by iteratively trying to prove some of the remaining unknown implications, then taking the transitive closure including the newly proven theorems. At the end only the transitive reduction of the implications was kept.

The Vampire proofs were converted to Lean proofs using [a term elaborator implementing the deduction step of superposition calculus](https://github.com/teorth/equational_theories/tree/main/equational_theories/Superposition.lean).
