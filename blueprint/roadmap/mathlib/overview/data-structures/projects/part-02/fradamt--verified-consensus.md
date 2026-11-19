---
declaration: theorem
origin: cited
lean: DecoupledConsensusModel.Proofs.concreteConsensus
statement: formalized
proof: formalized
---

# verified-consensus

[fradamt/verified-consensus](https://github.com/fradamt/verified-consensus) at commit [d3797547](https://github.com/fradamt/verified-consensus/tree/d379754762ccd69cec2fcaf94d18481a0600ef78), 2026-10-12.

> A Lean 4 model of the decoupled consensus protocol (Section 7 of the paper) and a machine-checked proof of its consensus guarantees.

*Quoted from [README.md](https://github.com/fradamt/verified-consensus/blob/d379754762ccd69cec2fcaf94d18481a0600ef78/README.md), CC0-1.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Integer](../../../general-algebra/numbers/integer.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [Finite set](../../sets/finite-set.md)
- [List](../../list-like-structures/list.md)
- [Set](../../sets/set.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`DecoupledConsensusModel.Proofs.concreteConsensus`](https://github.com/fradamt/verified-consensus/blob/d379754762ccd69cec2fcaf94d18481a0600ef78/DecoupledConsensusProofs/ReviewTheorem.lean#L288) (theorem)

No file its headlines import, directly or not (1031 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.1, Mathlib at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).
- 1,047 .lean files; its Lean libraries `DecoupledConsensusModel`, `DecoupledConsensusStatements`, `DecoupledConsensusInternal`, `DecoupledConsensusProofs`, `DecoupledConsensusWitnesses` hold 1,044, declaring 6,404 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: CC0-1.0 ([LICENSE](https://github.com/fradamt/verified-consensus/blob/d379754762ccd69cec2fcaf94d18481a0600ef78/LICENSE)).

## Builds on

- Mathlib, at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).

## Placement

Of its imports of Mathlib modules in an overview area, 24 of 50 are in Data structures, 3.4 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (24 of 50 imports, 3.4×), General algebra (21 of 50 imports, 1.2×). *Proof depends on* names 5 of the 5 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [fradamt/verified-consensus at d3797547](https://github.com/fradamt/verified-consensus/tree/d379754762ccd69cec2fcaf94d18481a0600ef78)
