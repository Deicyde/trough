---
declaration: lemma
origin: cited
lean: MIPRE.TM.CookLevin.tableau_sat_iff
statement: formalized
proof: formalized
---

# Correctness of the Cook–Levin tableau

Let $M$ be a multi-input Turing machine (Definition [Multi-input Turing machine](../../computability/def-multiinput-tm.md)) with $i$ input tapes and $w$ work tapes over a finite alphabet, $\mathsf{acc}$, $s_0$, $s_1$ symbols and $S$ a step bound, and fix the strings on some of the input tapes. The *tableau formula* of $S$ steps of $M$ is the 3SAT formula on the variables “cell $p$ of tape $d$ at time $t$ holds $v$” (one for each of $2S + 7$ cells and each value: a symbol, the blank or the boundary marker), “the head of tape $d$ is on cell $p$ at time $t$”, “the state at time $t$ is $q$”, the emission flags of every step, and, for every step and every choice of a five-cell window on each tape, the gate variables of a circuit deciding local consistency of the window; its clauses are the start row, the boundary rows, the free-tape row (a string over $\{s_0, s_1\}$ followed by blanks), the emission bookkeeping, the acceptance row and the circuit-to-3SAT clauses of the local check at every window. The formula is satisfiable if and only if $M$, started on the fixed strings and on some strings over $\{s_0, s_1\}$ on the free input tapes, halts within $S$ steps having output exactly $\mathsf{acc}$.

## Depends on

- [Multi-input Turing machine](../../computability/def-multiinput-tm.md)

## Proof

Completeness: the encoding of the run satisfies every clause, the window clauses because the windows of a run pass the local check (`locallyConsistent_localCfgOf`) and the circuit computes it, which is its specification (`IsCheckCircuit`). Soundness: the time-$0$ rows of a satisfying assignment determine the free strings; by induction on time the rows encode the run, because a locally consistent window whose time-$t$ part is that of a configuration has the time-$(t + 1)$ part of its successor (`post_of_pre`); the acceptance row and the emission bookkeeping then give the output. Every head stays on an interior cell: a head moves at most one cell per step and a tape has $2S + 7$ cells.

## Lean

Formalized as [`MIPRE.TM.CookLevin.tableau_sat_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.tableau_sat_iff).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6219](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6219)
