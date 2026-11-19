---
declaration: theorem
origin: cited
lean: YulEvmCompiler.SsaCfg.CseAgree.jump, YulEvmCompiler.Optimizer.MemorySpillControlSound.CodeOrigin.call, YulEvmCompiler.compileObject_correct, YulEvmCompiler.compileObject_consistent, YulParser.parse_canon_block, YulParser.parse_canon_obj, YulEvmCompiler.Optimizer.LocalPass.optimize_then_compile_correct, YulEvmCompiler.Optimizer.optimizerPipelineObject_correct
statement: formalized
proof: formalized
---

# yul-evm-compiler

[powdr-labs/yul-compiler](https://github.com/powdr-labs/yul-compiler) at commit [330923e0](https://github.com/powdr-labs/yul-compiler/tree/330923e0be35fc02c6cdb325e737003bb79230a8), 2026-09-04.

> A **verified non-optimizing compiler for a fragment of Yul to EVM bytecode**, written in Lean 4. "Non-optimizing" describes the *core*: code generation is direct and its correctness never depends on any optimization. Two separately verified optimizers do run in front of and below it — a Yul→Yul pipeline (`Optimizer/`) and an Asm→Asm peephole (`AsmPeephole.lean`), each with its own soundness contract composed into the end-to-end theorem. See **Optimization** below.

*Quoted from [README.md](https://github.com/powdr-labs/yul-compiler/blob/330923e0be35fc02c6cdb325e737003bb79230a8/README.md), Apache-2.0.*

## Depends on

- [List](../../list-like-structures/list.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Proof depends on

- [Hash map](../../maps/hash-map.md)
- [Array](../../list-like-structures/array.md)
- [Closure](../../../topology/general-topology/part-01/closure.md)
- [Integer](../../../general-algebra/numbers/integer.md)

## Main results

Its Lean names are 8 of the 21 theorems its README names in code:

- [`YulEvmCompiler.SsaCfg.CseAgree.jump`](https://github.com/powdr-labs/yul-compiler/blob/330923e0be35fc02c6cdb325e737003bb79230a8/YulEvmCompiler/SsaCfg/Implementation/PassesSound/CseRuntime.lean#L1124) (theorem)
- [`YulEvmCompiler.Optimizer.MemorySpillControlSound.CodeOrigin.call`](https://github.com/powdr-labs/yul-compiler/blob/330923e0be35fc02c6cdb325e737003bb79230a8/YulEvmCompiler/Optimizer/Implementation/MemorySpillControlSound.lean#L770) (theorem)
- [`YulEvmCompiler.compileObject_correct`](https://github.com/powdr-labs/yul-compiler/blob/330923e0be35fc02c6cdb325e737003bb79230a8/YulEvmCompiler/ObjectCompile.lean#L1059) (theorem)
- [`YulEvmCompiler.compileObject_consistent`](https://github.com/powdr-labs/yul-compiler/blob/330923e0be35fc02c6cdb325e737003bb79230a8/YulEvmCompiler/ObjectCompile.lean#L1031) (theorem)
- [`YulParser.parse_canon_block`](https://github.com/powdr-labs/yul-compiler/blob/330923e0be35fc02c6cdb325e737003bb79230a8/YulParser/Stmt.lean#L314) (theorem)
- [`YulParser.parse_canon_obj`](https://github.com/powdr-labs/yul-compiler/blob/330923e0be35fc02c6cdb325e737003bb79230a8/YulParser/Obj.lean#L142) (theorem)
- [`YulEvmCompiler.Optimizer.LocalPass.optimize_then_compile_correct`](https://github.com/powdr-labs/yul-compiler/blob/330923e0be35fc02c6cdb325e737003bb79230a8/YulEvmCompiler/Optimizer/Spec/Backend.lean#L40) (theorem)
- [`YulEvmCompiler.Optimizer.optimizerPipelineObject_correct`](https://github.com/powdr-labs/yul-compiler/blob/330923e0be35fc02c6cdb325e737003bb79230a8/YulEvmCompiler/Optimizer/Implementation/Pipeline.lean#L435) (theorem)

No file its headlines import, directly or not (130 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.33.0, Mathlib at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).
- 248 .lean files; its Lean libraries `YulEvmCompiler`, `YulParser`, `YulCApi`, `YulEvmCompilerTests`, `YulIR`, `YulIRBench` hold 236, declaring 7,342 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- License: Apache-2.0 ([LICENSE](https://github.com/powdr-labs/yul-compiler/blob/330923e0be35fc02c6cdb325e737003bb79230a8/LICENSE)).

## Builds on

- Mathlib, at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).
- `evm_semantics` (https://github.com/powdr-labs/evm-semantics) at `2f8714d6`.
- `«yul-semantics»` (https://github.com/powdr-labs/yul-semantics) at `c9914c13`.

## Placement

Of its imports of Mathlib modules in an overview area, 11 of 17 are in Data structures, 4.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (11 of 17 imports, 4.5×), General algebra (6 of 17 imports, 1.0×). *Proof depends on* lists 4 of the 6 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [powdr-labs/yul-compiler at 330923e0](https://github.com/powdr-labs/yul-compiler/tree/330923e0be35fc02c6cdb325e737003bb79230a8)
