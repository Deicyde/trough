---
declaration: theorem
origin: cited
lean: VacuumBellSeparation.OQP12.theorem_1_1, VacuumBellSeparation.OQP12.corollary_1_2, VacuumBellSeparation.OQP12.no_chsh_violation_far_apart, VacuumBellSeparation.OQP12.no_chsh_violation_far_apart_uniform, VacuumBellSeparation.OQP12.freeFieldVacuum_exists, VacuumBellSeparation.OQP12.localAlgebra_open_nonabelian
statement: formalized
proof: formalized
---

# Vacuum Bell correlation at large spacelike separation

> For the massive real free scalar field in 3+1 dimensions, the vacuum Bell correlation of two fixed bounded regions equals the classical bound once one region is translated sufficiently far along a fixed spacelike vector. For equal-radius double cones separated along the first spatial axis at the same time, one separation-to-radius threshold works for every positive mass. The development includes Weyl systems, local von Neumann algebras, a construction of the free-field vacuum, and a proof that the algebra of a nonempty open region is noncommutative.

*Quoted from the card [LeanPool/projects/vacuum-bell-separation.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/vacuum-bell-separation.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`VacuumBellSeparation.OQP12.theorem_1_1`](https://leanpool.github.io/lean-pool/LeanPool/VacuumBellSeparation.html#VacuumBellSeparation.OQP12.theorem_1_1) (theorem; a main declaration), declared in [LeanPool/VacuumBellSeparation.lean, line 70](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/VacuumBellSeparation.lean#L70): “One constant greater than two suffices for every positive mass. For equal-radius double cones with simultaneous centers at the origin and on the first spatial axis, the normalized vacuum CHSH supremum is one once their spatial distance reaches that constant times their radius.”
- [`VacuumBellSeparation.OQP12.corollary_1_2`](https://leanpool.github.io/lean-pool/LeanPool/VacuumBellSeparation.html#VacuumBellSeparation.OQP12.corollary_1_2) (theorem; a main declaration), declared in [LeanPool/VacuumBellSeparation.lean, line 84](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/VacuumBellSeparation.lean#L84): “For two bounded regions and a fixed spacelike vector, the normalized supremum equals one beyond a translation threshold.”
- [`VacuumBellSeparation.OQP12.no_chsh_violation_far_apart`](https://leanpool.github.io/lean-pool/LeanPool/VacuumBellSeparation.html#VacuumBellSeparation.OQP12.no_chsh_violation_far_apart) (theorem; a main declaration), declared in [LeanPool/VacuumBellSeparation.lean, line 56](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/VacuumBellSeparation.lean#L56): “Beyond that threshold the unnormalized CHSH expression for any four local self-adjoint contractions has absolute value at most two.”
- [`VacuumBellSeparation.OQP12.no_chsh_violation_far_apart_uniform`](https://leanpool.github.io/lean-pool/LeanPool/VacuumBellSeparation.html#VacuumBellSeparation.OQP12.no_chsh_violation_far_apart_uniform) (theorem; a main declaration), declared in [LeanPool/VacuumBellSeparation.lean, line 105](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/VacuumBellSeparation.lean#L105): “A single threshold suffices uniformly over all spatial translation directions for a given pair of bounded regions and positive mass.”
- [`VacuumBellSeparation.OQP12.freeFieldVacuum_exists`](https://leanpool.github.io/lean-pool/LeanPool/VacuumBellSeparation.html#VacuumBellSeparation.OQP12.freeFieldVacuum_exists) (theorem; a main declaration), declared in [LeanPool/VacuumBellSeparation.lean, line 100](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/VacuumBellSeparation.lean#L100): “For every positive mass there exists a complex Hilbert space carrying a free-field vacuum Weyl system.”
- [`VacuumBellSeparation.OQP12.localAlgebra_open_nonabelian`](https://leanpool.github.io/lean-pool/LeanPool/VacuumBellSeparation.html#VacuumBellSeparation.OQP12.localAlgebra_open_nonabelian) (theorem; a main declaration), declared in [LeanPool/VacuumBellSeparation.lean, line 118](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/VacuumBellSeparation.lean#L118): “The local von Neumann algebra of every nonempty open spacetime region contains two noncommuting operators.”

## Project

- Authors: David Turturean.
- Source: *The vacuum Bell correlation of the massive free scalar field attains the classical bound for bounded regions beyond a finite separation*, [https://github.com/physical-superintelligence/oqp-batch-2026/tree/7049357c42a8fe85262da08fdc10d57b4d9e67a0/oqp12-vacuum-bell-correlations](https://github.com/physical-superintelligence/oqp-batch-2026/tree/7049357c42a8fe85262da08fdc10d57b4d9e67a0/oqp12-vacuum-bell-correlations).
- Project repository: [physical-superintelligence/oqp-batch-2026](https://github.com/physical-superintelligence/oqp-batch-2026), at commit [7049357c](https://github.com/physical-superintelligence/oqp-batch-2026/tree/7049357c42a8fe85262da08fdc10d57b4d9e67a0).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 81T05, 81P40, 46L60.
- In Lean Pool: [LeanPool/VacuumBellSeparation](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/VacuumBellSeparation), from the card [LeanPool/projects/vacuum-bell-separation.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/vacuum-bell-separation.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/vacuum-bell-separation.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/vacuum-bell-separation.yaml)
- [Lean Pool at bb99e52c: LeanPool/VacuumBellSeparation](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/VacuumBellSeparation)
