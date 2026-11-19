---
declaration: module
origin: cited
lean: PrimeAndTwoPowersCovering10, Statement
statement: formalized
---

# Math proofs

[linrock/math-proofs](https://github.com/linrock/math-proofs) at commit [994b4c04](https://github.com/linrock/math-proofs/tree/994b4c04dc4cf77c4b27364e27f179622104c681), 2026-10-25.

> Standalone [Lean 4](https://lean-lang.org/) proofs of [Erdős problems](https://www.erdosproblems.com/), packaged as pinned [Lake](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/) projects for [Palomar](https://palomar-registry.org/) submission. Each project has a statement-only `Challenge.lean`, a proved `Solution.lean`, an `AxiomAudit.lean`, and build instructions.

*Quoted from [README.md](https://github.com/linrock/math-proofs/blob/994b4c04dc4cf77c4b27364e27f179622104c681/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Multiset](../../sets/multiset.md)
- [Set](../../sets/set.md)
- [Filter](../../../topology/general-topology/part-01/filter.md)
- [Finite set](../../sets/finite-set.md)
- [List](../../list-like-structures/list.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`PrimeAndTwoPowersCovering10`](https://github.com/linrock/math-proofs/blob/994b4c04dc4cf77c4b27364e27f179622104c681/erdos-10/Proofs/PrimeAndTwoPowersCovering10.lean), [`Statement`](https://github.com/linrock/math-proofs/blob/994b4c04dc4cf77c4b27364e27f179622104c681/erdos-10/Statement.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `erdos-10/Challenge.lean` holds `sorry` or `admit`.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 863 .lean files; its Lean libraries `Proofs10`, `Challenge`, `Solution`, `AxiomAudit`, `Statement` hold 5, declaring 243 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/linrock/math-proofs/blob/994b4c04dc4cf77c4b27364e27f179622104c681/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).

## Placement

4 of the 5 Mathlib concepts its files name are in Data structures.

## Mathlib use

*Proof depends on* lists 5 of the 5 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [linrock/math-proofs at 994b4c04](https://github.com/linrock/math-proofs/tree/994b4c04dc4cf77c4b27364e27f179622104c681)
