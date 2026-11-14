---
declaration: theorem
origin: cited
lean: MIPRE.SAT.SuccinctCookLevin, MIPRE.SAT.succinctCookLevin
statement: formalized
proof: formalized
---

# Explicit succinct Cook–Levin

There is a polynomial-time algorithm that, given a decider $\mathcal{D}$, an index $n$, a time bound $T$ (in binary), a question length $Q$, a bound $\sigma$ and strings $x, y$, with $\max\{Q, 2\lceil \log n \rceil\} \leq T$, $\left\vert {\mathcal{D}} \right\vert \leq \sigma$ and $\left\vert {x} \right\vert, \left\vert {y} \right\vert \leq Q$, outputs a circuit $C$ on $3m + 3$ inputs which succinctly describes (Definition [Succinctly described 3SAT and decoupled 5SAT](../part-03/def-succinct-3sat.md)) a 3SAT formula $\varphi$ on $2^m$ variables such that

1. for all $a, b \in \{0,1\}^{2T}$, the formula $\varphi$ has a satisfying assignment whose first $4T$ variables are $(a, b)$ if and only if $a$ and $b$ are the two-bit tape encodings of strings $a', b'$ of length at most $T$ such that $\mathcal{D}$ accepts $(n, x, y, a', b')$ within $T$ steps;
2. $m = O(\log T + \log \sigma)$ and $2^m \geq 4T$;
3. $C$ has at most $s(n, T, Q, \sigma) = \mathrm{poly}(\log n, \log T, Q, \sigma)$ gates;
4. the algorithm runs in time $\mathrm{poly}(\log n, \log T, Q, \sigma)$;
5. $m$ and $s$ are computable from the parameters in time polynomial in their bit lengths.

## Depends on

- [Succinctly described 3SAT and decoupled 5SAT](../part-03/def-succinct-3sat.md)
- [Decider](../../foundations/part-03/def-decider.md)
- [Multi-input Turing machine](../../computability/def-multiinput-tm.md)

## Proof

Fix one interpreter machine $U$, a multi-input Turing machine that runs the small-step semantics of the ambient model on a serialized configuration, and put the five parameters $n, x, y$ and the two answers on its input tapes, the answers on the two tapes left free. Then the decider is \*data\* on an input tape and never becomes a machine, so the local check circuit of $U$ is a constant; and the answer blocks are the contents of two tapes at time $0$, which is item 1's block structure for free. The time bound $T$ in the cost of the ambient model becomes a tableau length $S = 2^e$ with $e = 5\lceil \log T \rceil + 5 \lceil \log \sigma \rceil + 24$, because a run of the decider of cost $T$ is a run of $U$ of at most $400000 (T + \sigma + 1)^5$ steps.

Apply Lemma [Correctness of the Cook–Levin tableau](lem-correct-tableau.md) to $U$ at that length. Index its variables by bit strings of width $m = 11 + 15 W + Q_b + G_b$, where $W = e + 4$ is the width of a time, a position or a window offset: the top bit says whether the index is structured or is one of the first $4T$ answer indices, and the remaining fields are a kind tag, a time, a tape, a position, a value, a state, the thirteen window offsets and a gate number. Each clause family of the tableau is then a predicate on those decoded fields, and each such predicate is computed by a formula over the $3m + 3$ input bits of the describer, built from equality and comparison with a constant, equality of two fields, and a ripple-carry increment. The describer is the flattening of the disjunction of those formulas to a circuit, together with two clauses forcing the cell at position $T + 3$ of each free tape to hold the blank, which is what bounds the answers read off a satisfying assignment by $T$ rather than by $2S$.

Item 1 is the correctness of the tableau in both directions, transported along the indexing: an assignment of the tableau gives one of the formula by decoding, and an assignment of the formula gives one of the tableau by the canonical index, where an answer cell of a free tape inside the answer block is sent to its answer index, so that the extension hypothesis on the first $4T$ variables is exactly the time-$0$ row of that tape. Item 2 is arithmetic on $m$ and $e$. For items 3 and 4, every builder of the formula is a polynomial-time function of the parameters, since the encoding of a formula is the encoding of its post-order list and each builder is therefore a concatenation, a map or a fold over lists, with the widths and offsets carried in unary; and then item 3 needs no separate argument, because the output of a polynomial-time function is no larger than its running time and a circuit has at most as many gates as its encoding has nodes. Item 5 follows by rounding $s$ up to a power of two whose exponent is a multiple of the bit lengths of the parameters.

## Lean

Formalized as [`MIPRE.SAT.SuccinctCookLevin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.SuccinctCookLevin), [`MIPRE.SAT.succinctCookLevin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.succinctCookLevin).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6101](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6101)
