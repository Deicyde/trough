---
declaration: corollary
origin: cited
lean: MIPRE.tsirelson, MIPRE.tsirelson_of_haltingReduction, MIPRE.tsirelson_of_upperRE
statement: formalized
proof: formalized
---

# Tsirelson's problem, negative answer

There exist finite question and answer sets for which the closure $C_{qa}$ of the set of finite-dimensional quantum correlations is strictly contained in the set $C_{qc}$ of commuting-operator correlations.

## Depends on

- [Correlation sets](def-correlation-sets.md)
- [Conditional separation](lem-tsirelson-conditional.md)
- [Halting reduces to the quantum value](../../the-main-theorem/cor-main-quantum.md)
- [Upper semidecision of the commuting-operator value](lem-valco-upper-re.md)
- [$C_{qc}$ is compact](lem-cqc-compact.md)

## Proof

Lemma [Conditional separation](lem-tsirelson-conditional.md), with the halting reduction of Corollary [Halting reduces to the quantum value](../../the-main-theorem/cor-main-quantum.md), the upper semidecider of Lemma [Upper semidecision of the commuting-operator value](lem-valco-upper-re.md), and the closedness of $C_{qc}$ in every finite scenario (Lemma [$C_{qc}$ is compact](lem-cqc-compact.md)).

## Lean

Formalized as [`MIPRE.tsirelson`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.tsirelson), [`MIPRE.tsirelson_of_haltingReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.tsirelson_of_haltingReduction), [`MIPRE.tsirelson_of_upperRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.tsirelson_of_upperRE).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 446](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L446)
