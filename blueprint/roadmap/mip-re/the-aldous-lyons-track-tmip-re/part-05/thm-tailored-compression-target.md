---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.tailoredGapCompression
statement: formalized
proof: formalized
---

# Tailored compression; II:5643, value form

There is a tailored gap compression at level $7$.

## Depends on

- [Tailored compression from its stages; II:5643, value form](thm-tailored-compression-from-stages.md)
- [Question reduction for tailored verifiers; II:5712](../part-03/thm-tailored-qr.md)
- [Answer reduction for tailored verifiers; II:6883](../part-03/thm-tailored-ar.md)
- [Parallel repetition of tailored verifiers; II:11103, direct form](../part-03/thm-tailored-rep.md)
- [$\mathrm{TMIP}^* = \mathrm{RE}$ from tailored answer reduction](cor-tmip-re-from-ar.md)

## Proof

Theorem [Tailored compression from its stages; II:5643, value form](thm-tailored-compression-from-stages.md) applied to the three stages: question reduction (Theorem [Question reduction for tailored verifiers; II:5712](../part-03/thm-tailored-qr.md)), answer reduction (Theorem [Answer reduction for tailored verifiers; II:6883](../part-03/thm-tailored-ar.md)) and parallel repetition (Theorem [Parallel repetition of tailored verifiers; II:11103, direct form](../part-03/thm-tailored-rep.md)).

## Lean

Formalized as [`MIPRE.Tailored.tailoredGapCompression`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.tailoredGapCompression).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2297](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2297)
