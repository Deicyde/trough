---
declaration: lemma
origin: cited
lean: MIPRE.Tsirelson.stateSpace, MIPRE.Tsirelson.isCompact_stateSpace, MIPRE.Tsirelson.image_correlationOf_stateSpace, MIPRE.isCompact_Cqc, MIPRE.isClosed_Cqc, MIPRE.Cqa_subset_Cqc
statement: formalized
proof: formalized
---

# $C_{qc}$ is compact

For finite alphabets $C_{qc}$ is compact, hence closed, and $C_{qa} \subseteq C_{qc}$.

## Depends on

- [Cone states are the states of commuting-operator strategies](lem-cone-state-gns.md)
- [Basic properties of the correlation sets](lem-correlation-sets-basic.md)

## Proof

A cone state is determined by its values on words. The set of those value families that are cone states is closed in the product topology, since each condition involves finitely many words, and lies in the product of closed unit disks, since $2 \cdot 1 + \alpha w + (\alpha w)^* \in M$ for $\left\vert {\alpha} \right\vert = 1$ gives $\left\vert {L(w)} \right\vert \leq 1$. By Tychonoff it is compact, and by Lemma [Cone states are the states of commuting-operator strategies](lem-cone-state-gns.md) its continuous image under $L \mapsto \mathrm{Re}\, L(e_{xa} f_{yb})$ is $C_{qc}$.

## Lean

Formalized as [`MIPRE.Tsirelson.stateSpace`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.stateSpace), [`MIPRE.Tsirelson.isCompact_stateSpace`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.isCompact_stateSpace), [`MIPRE.Tsirelson.image_correlationOf_stateSpace`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.image_correlationOf_stateSpace), [`MIPRE.isCompact_Cqc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.isCompact_Cqc), [`MIPRE.isClosed_Cqc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.isClosed_Cqc), [`MIPRE.Cqa_subset_Cqc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cqa_subset_Cqc).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 223](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L223)
