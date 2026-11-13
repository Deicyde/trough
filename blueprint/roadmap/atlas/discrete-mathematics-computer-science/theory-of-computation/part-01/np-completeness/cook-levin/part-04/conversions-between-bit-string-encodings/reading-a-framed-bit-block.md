---
declaration: section
origin: cited
lean: Cslib.Complexity.FramedCNF.Block.read, Cslib.Complexity.FramedCNF.Block.run_delimit, Cslib.Complexity.FramedCNF.Block.run_none
statement: formalized
proof: formalized
---

# Reading a framed bit block

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reading-a-framed-bit-block/index.html).

## Machine step reading one framed payload pair

Consume one framed-payload pair or its terminator.

Formalized by `Cslib.Complexity.FramedCNF.Block.read`, a definition declared in [CSLibExt/Computability/Complexity/FramedCNF/Block.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/FramedCNF/Block.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reading-a-framed-bit-block/index.html#read).

## Reading a complete framed block

Read a complete block, preserving an arbitrary suffix and all stacks
other than the input and reversed-payload destination.

Formalized by `Cslib.Complexity.FramedCNF.Block.run_delimit`, a theorem declared in [CSLibExt/Computability/Complexity/FramedCNF/Block.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/FramedCNF/Block.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reading-a-framed-bit-block/index.html#run-delimit).

## Framed block reader fails on truncated framing

Truncated framing reaches the failure branch within input length
plus one, without assuming that the input is an encoder image. The
destination may contain a partial payload on failure; the caller must
discard or clear it before using that stack again.

Formalized by `Cslib.Complexity.FramedCNF.Block.run_none`, a theorem declared in [CSLibExt/Computability/Complexity/FramedCNF/Block.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/FramedCNF/Block.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reading-a-framed-bit-block/index.html#run-none).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reading a framed bit block](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reading-a-framed-bit-block/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reading-a-framed-bit-block)
