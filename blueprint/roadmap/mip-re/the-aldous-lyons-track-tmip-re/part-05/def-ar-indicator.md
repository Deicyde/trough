---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.tableSize, MIPRE.Tailored.AnsRed.indTable, MIPRE.Tailored.AnsRed.TableSat, MIPRE.Tailored.AnsRed.LstarOK, MIPRE.Tailored.AnsRed.lstarProg, MIPRE.Tailored.AnsRed.lstar
statement: formalized
---

# The table and the output indicator

The index space of the table is $[N] \times [N] \times [D]^3 \times [64]$, the first coordinate fastest, so that for $N = 2^\ell$ and $D = 2^{\delta}$ the binary digits of an index are those of its coordinates in turn (II:8453); the last coordinate holds the six signs, one per digit. The *table* of a triangulated system is the indicator of its decoupled system (Definition [Purified, triangulated and decoupled systems](def-ar-linear.md)) over the index space, a string of $64 N^2 D^3$ bits, and five assignments *satisfy* a table when every equation whose index it contains holds. The *check* at $(N, D)$ reads the four lengths at the two questions, the constraints that the processor outputs on the readable answers, and the inputs $a = a^R O$ and $b = b^R$: the lengths are at most $N$, $b$ has $N$ bits and $O$ has $64 N^2 D^3$, the number of constraints times $2N$, plus $2N$, is at most $D$, and $O$ is the table of the triangulated purified equations, the readable answers cut at the readable lengths. The *output indicator* of a tailored verifier, at a parameter program giving $(\ell, \delta)$ in unary, is the decider that runs the answer-length calculator four times and the processor once, as the canonical decider does, and then makes the check at $(2^\ell, 2^{\delta})$.

## Depends on

- [Purified, triangulated and decoupled systems](def-ar-linear.md)
- [The canonical decider, as a program; II:1757–1787](../part-01/def-canonical-decider.md)
- [Effective unary prime-power decomposition](../../background-results/part-04/lem-binary-degree-decomposition.md)
- [Effective self-dualization of a supplied normal basis](../../background-results/part-05/lem-effective-normal-selfdualization.md)

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.tableSize`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.tableSize), [`MIPRE.Tailored.AnsRed.indTable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.indTable), [`MIPRE.Tailored.AnsRed.TableSat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.TableSat), [`MIPRE.Tailored.AnsRed.LstarOK`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.LstarOK), [`MIPRE.Tailored.AnsRed.lstarProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.lstarProg), [`MIPRE.Tailored.AnsRed.lstar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.lstar).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2477](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2477)
