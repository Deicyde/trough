---
declaration: theorem
origin: cited
lean: VeriDNS.Proof.NameTree.resolveWithIO_sound, VeriDNS.Spec.Net.scrubAnswer_no_foreign, VeriDNS.Impl.Resolver.scrubAnswerB_excludes_foreign, ioResumeLoop_sound
statement: formalized
proof: formalized
---

# VeriDNS

[BasisResearch/VeriDNS](https://github.com/BasisResearch/VeriDNS) at commit [74bb5f3f](https://github.com/BasisResearch/VeriDNS/tree/74bb5f3f1454a8de2744e69f8af18fe48e0e9f2e), 2026-07-17.

## Depends on

- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)

## Proof depends on

- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)
- [Set](../../../mathlib/overview/data-structures/sets/set.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`VeriDNS.Proof.NameTree.resolveWithIO_sound`](https://github.com/BasisResearch/VeriDNS/blob/74bb5f3f1454a8de2744e69f8af18fe48e0e9f2e/VeriDNS/Proof/NameTree.lean#L2018) (theorem)
- [`VeriDNS.Spec.Net.scrubAnswer_no_foreign`](https://github.com/BasisResearch/VeriDNS/blob/74bb5f3f1454a8de2744e69f8af18fe48e0e9f2e/VeriDNS/Spec/AnswerAuthenticity.lean#L158) (theorem)
- [`VeriDNS.Impl.Resolver.scrubAnswerB_excludes_foreign`](https://github.com/BasisResearch/VeriDNS/blob/74bb5f3f1454a8de2744e69f8af18fe48e0e9f2e/VeriDNS/Proof/AnswerScrub.lean#L99) (theorem)
- [`ioResumeLoop_sound`](https://github.com/BasisResearch/VeriDNS/blob/74bb5f3f1454a8de2744e69f8af18fe48e0e9f2e/VeriDNS/Proof/IoResumeSound.lean#L3571) (theorem)

No file its headlines import, directly or not (65 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.31.0-rc2.
- 127 .lean files; its Lean libraries `VeriDNS` hold 126, declaring 4,076 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- No license file; facts only.

## Placement

It requires neither Mathlib nor another library mapped here; 36 files of the project import Batteries modules.

## Mathlib use

*Proof depends on* names 2 of the 5 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [BasisResearch/VeriDNS at 74bb5f3f](https://github.com/BasisResearch/VeriDNS/tree/74bb5f3f1454a8de2744e69f8af18fe48e0e9f2e)
