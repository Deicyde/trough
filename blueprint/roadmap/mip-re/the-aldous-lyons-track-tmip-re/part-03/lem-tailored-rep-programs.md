---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.RepProg.repSpec, MIPRE.Tailored.RepProg.repLen_lenIs, MIPRE.Tailored.RepProg.good_of_repLen, MIPRE.Tailored.RepProg.repLp_lpIs_iff, MIPRE.Tailored.Calls.mapCall_runs, MIPRE.Tailored.Calls.mapCall_inv
statement: formalized
proof: formalized
---

# The repeated programs meet the specification

At every index, the repeated programs meet the specification of Definition [Repeated tailored verifiers and the specification of their programs](def-tailored-rep-spec.md).

## Depends on

- [The repeated programs](def-tailored-rep-programs.md)
- [Repeated tailored verifiers and the specification of their programs](def-tailored-rep-spec.md)

## Proof

The loop of calls halts with the results of the calls when every call halts, and only then. At a question all of whose coordinates have their lengths, the calculator's calls all halt and its output has the sum of the lengths; conversely a halting run of the calculator ran the input calculator at both kinds of every coordinate. For the processor, the lengths read off the calculator's outputs are the coordinates', so its cuts of $a^R$ and $b^R$ are the coordinates' readable answers, its queries are the coordinates' and its padding is the product's.

## Lean

Formalized as [`MIPRE.Tailored.RepProg.repSpec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.RepProg.repSpec), [`MIPRE.Tailored.RepProg.repLen_lenIs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.RepProg.repLen_lenIs), [`MIPRE.Tailored.RepProg.good_of_repLen`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.RepProg.good_of_repLen), [`MIPRE.Tailored.RepProg.repLp_lpIs_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.RepProg.repLp_lpIs_iff), [`MIPRE.Tailored.Calls.mapCall_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Calls.mapCall_runs), [`MIPRE.Tailored.Calls.mapCall_inv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Calls.mapCall_inv).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1270](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1270)
