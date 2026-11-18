---
declaration: theorem
origin: cited
lean: Blanc.ContractSpec.sound_of_dispatch, Blanc.Prog.runCompiled_iff_exec, Blanc.correct, Blanc.correct_core, Blanc.Prog.exec_of_runCompiled, Blanc.Devm.withRefundCounter_getStor, Blanc.Devm.addLog_getStor, Blanc.Lift.Witness.AccKeep.setMach
statement: formalized
proof: formalized
---

# Blanc: A Verification Stack for EVM Smart Contracts in Lean 4

[skbaek/blanc](https://github.com/skbaek/blanc) at commit [251128de](https://github.com/skbaek/blanc/tree/251128de090c5b14c655d9be5dfbc7dd35076a92), 2026-11-14.

> **[skbaek.github.io/blanc](https://skbaek.github.io/blanc/)** — the guided tour: what Blanc proves about bytecode already deployed on mainnet, how, and on which premises; the Blanc language and its contracts; and what none of it claims. **[Jaune](https://github.com/skbaek/jaune)** ([site](https://skbaek.github.io/jaune/)) — the EVM semantics every theorem here is stated against.

*Quoted from [README.md](https://github.com/skbaek/blanc/blob/251128de090c5b14c655d9be5dfbc7dd35076a92/README.md), MIT, Copyright (c) 2024 skbaek.*

## Depends on

- [List](../../../data-structures/list-like-structures/list.md)
- [Natural number](../../numbers/natural-number.md)
- [Integer](../../numbers/integer.md)
- [Jaune](../../../data-structures/projects/skbaek--jaune.md)

## Proof depends on

- [Array](../../../data-structures/list-like-structures/array.md)
- [Finite set](../../../data-structures/sets/finite-set.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Blanc.ContractSpec.sound_of_dispatch`](https://github.com/skbaek/blanc/blob/251128de090c5b14c655d9be5dfbc7dd35076a92/Blanc/Ladder.lean#L704) (theorem)
- [`Blanc.Prog.runCompiled_iff_exec`](https://github.com/skbaek/blanc/blob/251128de090c5b14c655d9be5dfbc7dd35076a92/Blanc/Compiled.lean#L1658) (theorem)
- [`Blanc.correct`](https://github.com/skbaek/blanc/blob/251128de090c5b14c655d9be5dfbc7dd35076a92/Blanc/CommonCore.lean#L2119) (theorem)
- [`Blanc.correct_core`](https://github.com/skbaek/blanc/blob/251128de090c5b14c655d9be5dfbc7dd35076a92/Blanc/CommonCore.lean#L1986) (theorem)
- [`Blanc.Prog.exec_of_runCompiled`](https://github.com/skbaek/blanc/blob/251128de090c5b14c655d9be5dfbc7dd35076a92/Blanc/Compiled.lean#L1620) (theorem)
- [`Blanc.Devm.withRefundCounter_getStor`](https://github.com/skbaek/blanc/blob/251128de090c5b14c655d9be5dfbc7dd35076a92/Blanc/CommonProofs/Base.lean#L662) (lemma)
- [`Blanc.Devm.addLog_getStor`](https://github.com/skbaek/blanc/blob/251128de090c5b14c655d9be5dfbc7dd35076a92/Blanc/CommonProofs/Base.lean#L666) (lemma)
- [`Blanc.Lift.Witness.AccKeep.setMach`](https://github.com/skbaek/blanc/blob/251128de090c5b14c655d9be5dfbc7dd35076a92/Blanc/Lift/WitnessArms.lean#L32) (theorem)

No file its headlines import, directly or not (41 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 1,001 .lean files; its Lean libraries `Blanc` hold 982, declaring 15,615 names, with `sorry` in 15 files and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- License: MIT ([LICENSE](https://github.com/skbaek/blanc/blob/251128de090c5b14c655d9be5dfbc7dd35076a92/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- [jaune](../../../data-structures/projects/skbaek--jaune.md) at `730aae65`.

## Placement

2 of the 3 Mathlib concepts its headline statements name are in General algebra.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (6 of 8 imports, 2.1×), Data structures (2 of 8 imports, 1.8×). *Proof depends on* names 2 of the 5 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [skbaek/blanc at 251128de](https://github.com/skbaek/blanc/tree/251128de090c5b14c655d9be5dfbc7dd35076a92)
