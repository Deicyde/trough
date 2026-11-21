---
declaration: theorem
origin: cited
lean: Xv6.xv6FsAdequacy_closed, Xv6.unionAdequacyClosed, Xv6.unionSyncCutNeg
statement: formalized
---

# xv6iris

*xv6iris (Lean) — verifying xv6-riscv in Lean 4 / Iris over the Sail RISC-V semantics*

[mit-pdos/xv6iris](https://github.com/mit-pdos/xv6iris) at commit [5cb9df99](https://github.com/mit-pdos/xv6iris/tree/5cb9df992c45829f6210b3e4176962d7b7a4c408), 2026-11-06.

> This project proves, in [Lean 4](https://lean-lang.org/) with the [iris-lean](https://github.com/leanprover-community/iris-lean) separation logic, that the [xv6-riscv](https://github.com/mit-pdos/xv6-riscv) kernel and its user programs are correct — reasoning about the *actual binaries*, instruction by instruction, against the official [Sail RISC-V](https://github.com/riscv/sail-riscv) ISA semantics compiled to Lean by Sail's own Lean backend (from the [zeldovich/sail-riscv](https://github.com/zeldovich/sail-riscv) fork; see "Regenerating the Sail model").

*Quoted from [README.md](https://github.com/mit-pdos/xv6iris/blob/5cb9df992c45829f6210b3e4176962d7b7a4c408/README.md), MIT, Copyright (c) 2026 Massachusetts Institute of Technology.*

## Depends on

- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)

## Proof depends on

- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [Rational number](../../../mathlib/overview/general-algebra/numbers/rational-number.md)
- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Xv6.xv6FsAdequacy_closed`](https://github.com/mit-pdos/xv6iris/blob/5cb9df992c45829f6210b3e4176962d7b7a4c408/Xv6/LinkSystemAdequacyClosed.lean#L20) (theorem)
- [`Xv6.unionAdequacyClosed`](https://github.com/mit-pdos/xv6iris/blob/5cb9df992c45829f6210b3e4176962d7b7a4c408/Xv6/LinkUInitUnion.lean#L162) (theorem)
- [`Xv6.unionSyncCutNeg`](https://github.com/mit-pdos/xv6iris/blob/5cb9df992c45829f6210b3e4176962d7b7a4c408/Xv6/LinkUInitUnion.lean#L176) (theorem)

Of the files its headlines import, directly or not, `Xv6/UShLexRedir.lean`, `Xv6/UserHeap.lean` hold `sorry` or `admit`.

## Project

- Lean v4.32.2.
- 3,035 .lean files; its Lean libraries `MachCSL`, `Xv6`, `Vtest` hold 2,883, declaring 41,891 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- License: MIT ([LICENSE](https://github.com/mit-pdos/xv6iris/blob/5cb9df992c45829f6210b3e4176962d7b7a4c408/LICENSE)).

## Builds on

- `iris` (https://github.com/leanprover-community/iris-lean) at `728a1714`.
- `Lean_RV64D`.
- `Sail`.

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core and packages not mapped here.

## Mathlib use

*Proof depends on* lists 4 of the 6 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import. It requires no Mathlib, so only the articles whose Lean names Lean core or Std declares are kept.

## Sources

- [mit-pdos/xv6iris at 5cb9df99](https://github.com/mit-pdos/xv6iris/tree/5cb9df992c45829f6210b3e4176962d7b7a4c408)
