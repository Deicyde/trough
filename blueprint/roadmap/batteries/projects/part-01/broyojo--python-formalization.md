---
declaration: module
origin: cited
lean: PyLean, PyLean.All
statement: formalized
---

# python-formalization

[Broyojo/python-formalization](https://github.com/Broyojo/python-formalization) at commit [6eaf6979](https://github.com/Broyojo/python-formalization/tree/6eaf6979bc96a9041346dcc8f6c982a5669c6ba0), 2026-11-17.

> A Lean 4 model of CPython 3.15.2, written by AI agents, tested against the real interpreter, and reviewed function by function. Along the way it found hundreds of bugs in CPython.

*Quoted from [README.md](https://github.com/Broyojo/python-formalization/blob/6eaf6979bc96a9041346dcc8f6c982a5669c6ba0/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [Rational number](../../../mathlib/overview/general-algebra/numbers/rational-number.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`PyLean`](https://github.com/Broyojo/python-formalization/blob/6eaf6979bc96a9041346dcc8f6c982a5669c6ba0/lean/PyLean.lean), [`PyLean.All`](https://github.com/Broyojo/python-formalization/blob/6eaf6979bc96a9041346dcc8f6c982a5669c6ba0/lean/PyLean/All.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `lean/PyLean/BytesObj/Bytes/HeapProps3.lean`, `lean/PyLean/CoreLibs/Coll/Counter.lean`, `lean/PyLean/CoreLibs/Misc/Contextlib/Model.lean`, `lean/PyLean/CoreLibs/Misc/Weakref/Model.lean`, `lean/PyLean/DictSet/Chain.lean`, `lean/PyLean/DictSet/Common.lean`, `lean/PyLean/Itertools/Islice.lean`, `lean/PyLean/Itertools/IsliceReentry.lean`, `lean/PyLean/RangeSlice/Model.lean`, `lean/PyLean/RangeSlice/SliceHash.lean`, `lean/PyLean/TextLibs/ReSem.lean`, `lean/PyLean/UnicodeObj/CodecCallback.lean`, `lean/PyLean/UnicodeObj/CodecsErr.lean`, `lean/PyLean/UnicodeObj/MethSlice.lean`, `lean/PyLean/UnicodeObj/TextTranslateX.lean` hold `sorry` or `admit`.

## Project

- Lean v4.35.0.
- 1,544 .lean files; its Lean libraries `PyLean` hold 1,541, declaring 46,334 names, with `sorry` in 15 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/Broyojo/python-formalization/blob/6eaf6979bc96a9041346dcc8f6c982a5669c6ba0/LICENSE)).

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core alone.

## Mathlib use

*Proof depends on* lists 5 of the 5 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import. It requires no Mathlib, so only the articles whose Lean names Lean core or Std declares are kept.

## Sources

- [Broyojo/python-formalization at 6eaf6979](https://github.com/Broyojo/python-formalization/tree/6eaf6979bc96a9041346dcc8f6c982a5669c6ba0)
