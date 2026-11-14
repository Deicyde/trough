---
declaration: definition
origin: cited
lean: MIPRE.SAT.Circuit.formula3, MIPRE.SAT.Circuit.formula5, MIPRE.SAT.Circuit.DescribesDecider
statement: formalized
---

# Succinctly described 3SAT and decoupled 5SAT

A Boolean circuit $C$ with three inputs of length $m$ and three single-bit inputs *succinctly describes* the 3SAT formula on the $2^m$ variables $x_0, \ldots, x_{2^m - 1}$ whose clauses are the $x_{i_1}^{o_1} \vee x_{i_2}^{o_2} \vee x_{i_3}^{o_3}$ with $C(i_1, i_2, i_3, o_1, o_2, o_3) = 1$, integers presented to the circuit in binary ((JNVWY20, Definition of succinct descriptions of 3SAT formulas, Section 10)). A *decoupled 5SAT* formula has five blocks of variables and clauses with one literal from each block, evaluated on five separate assignments; a circuit with two inputs of length $\ell$, three of length $r$ and five single-bit inputs succinctly describes one in the same way. Such a circuit *describes the decider $\mathcal{D}$ on $(n, x, y)$ at time $T$* if, for all $a, b \in \{0,1\}^{2^\ell}$, some three assignments complete $(a, b)$ to a satisfying tuple exactly when $a$ and $b$ are the two-bit tape encodings ($0 \mapsto 00$, $1 \mapsto 01$, blank $\mapsto 10$) of strings of length at most $T$ on which $\mathcal{D}$ accepts $(n, x, y, \cdot, \cdot)$ within $T$ steps. Circuits have fan-in and fan-out at most two and a terminal output gate, and their size is the number of gates.

## Depends on

- [Decider](../../foundations/part-03/def-decider.md)

## Lean

Formalized as [`MIPRE.SAT.Circuit.formula3`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.formula3), [`MIPRE.SAT.Circuit.formula5`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.formula5), [`MIPRE.SAT.Circuit.DescribesDecider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.DescribesDecider).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6080](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6080)
