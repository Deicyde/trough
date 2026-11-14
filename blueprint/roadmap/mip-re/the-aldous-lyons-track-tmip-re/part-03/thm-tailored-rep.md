---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.tailoredRepetition
statement: formalized
proof: formalized
---

# Parallel repetition of tailored verifiers; II:11103, direct form

The contract `TailoredRepetition` is inhabited, at every level.

## Depends on

- [The three stage contracts](def-tailored-stages.md)
- [Completeness and soundness of repeated tailored verifiers](thm-tailored-rep-from-spec.md)
- [The repeated programs meet the specification](lem-tailored-rep-programs.md)
- [Running times of the repeated programs](lem-tailored-rep-programs-time.md)

## Proof

The repeated sampler, and the repeated programs of Definition [The repeated programs](def-tailored-rep-programs.md), their descriptions computed by the s-m-n map. The complexity clause is Lemma [Running times of the repeated programs](lem-tailored-rep-programs-time.md) with the repeated sampler's time bound, and completeness and soundness are Theorem [Completeness and soundness of repeated tailored verifiers](thm-tailored-rep-from-spec.md) applied to Lemma [The repeated programs meet the specification](lem-tailored-rep-programs.md).

## Lean

Formalized as [`MIPRE.Tailored.tailoredRepetition`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.tailoredRepetition).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1313](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1313)
