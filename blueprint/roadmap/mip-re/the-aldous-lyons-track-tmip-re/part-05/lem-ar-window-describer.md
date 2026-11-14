---
declaration: lemma
origin: cited
lean: MIPRE.SAT.Circuit.formula6, MIPRE.SAT.Circuit.DescribesWindows, MIPRE.SAT.WindowDescriber, MIPRE.SAT.windowDescriber
statement: formalized
proof: formalized
---

# Decoupled 6SAT through three windows; prop:explicit-padded-succinct-deciders

There is a polynomial-time algorithm that, on window lengths $\ell_a, \ell_b, \ell_c$ in unary and the inputs $(\mathcal{D}, n, T, Q, \sigma, x, y)$ of Theorem [Explicit succinct Cook–Levin](../../background-results/part-04/thm-succinct-sat.md), outputs a circuit with inputs of lengths $\ell_a$, $\ell_b$, $\ell_c$, three of length $r_0 = O(\log T + \log \sigma)$, with $2^{r_0} \geq 4T$, and six single bits, describing a decoupled 6SAT formula on blocks of $2^{\ell_a}$, $2^{\ell_b}$, $2^{\ell_c}$ and three times $2^{r_0}$ variables. On valid inputs with $\ell_a, \ell_b, \ell_c \le r_0$ the circuit has at most $s_0 = \mathrm{poly}(\log n, \log T, Q, \sigma)$ gates, and if moreover $2^{\ell_a} + 2^{\ell_c} \le 2T$ and $2^{\ell_b} \le 2T$, then three tables $A, B, C$ complete to a satisfying assignment exactly when the decider accepts, within cost $T$, strings $a, b$ of length at most $T$ such that $A$ and $C$ are the consecutive windows of lengths $2^{\ell_a}$ and $2^{\ell_c}$ at the start of the tape encoding of $a$, and $B$ is the first $2^{\ell_b}$ bits of that of $b$. The parameters $r_0, s_0$ are computable in time polynomial in the bit lengths of $n, T, Q, \sigma$.

## Depends on

- [Multi-input Turing machine](../../computability/def-multiinput-tm.md)

## Proof depends on

- [Succinctly described 3SAT and decoupled 5SAT](../../background-results/part-03/def-succinct-3sat.md)

## Proof

As for Lemma [Succinct decoupled 5SAT](../../structure-of-the-proof/part-07/lem-decoupled-5sat.md). The circuit accepts $(i_1, \dots, i_6, o_1, \dots, o_6)$ when the circuit of Theorem [Explicit succinct Cook–Levin](../../background-results/part-04/thm-succinct-sat.md) accepts the last three indices and signs, or when one of five link conditions holds: $i_4 = i_1 \land o_1 \neq o_4$; $i_4 = i_2 + 2T \land o_2 \neq o_4$; $i_4 = i_3 + 2^{\ell_a} \land o_3 \neq o_4$; $i_4 = i_5 \land o_4 \neq o_5$; $i_5 = i_6 \land o_5 \neq o_6$. For fixed indices the signs of the blocks a condition does not constrain range over all values, so the last two conditions say $w_1 = w_2 = w_3$ and the first three that the windows are read off the common assignment at the offsets $0$, $2T$ and $2^{\ell_a}$. The windows lie inside the two input regions of the tableau, so no padding condition is needed, and item 1 of Theorem [Explicit succinct Cook–Levin](../../background-results/part-04/thm-succinct-sat.md) relates a satisfying assignment to acceptance. The offset of the third window is a power of two, which the algorithm computes from $\ell_a$ without binary addition; the link conditions cost $O(r_0)$ gates.

## Lean

Formalized as [`MIPRE.SAT.Circuit.formula6`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.formula6), [`MIPRE.SAT.Circuit.DescribesWindows`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.DescribesWindows), [`MIPRE.SAT.WindowDescriber`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.WindowDescriber), [`MIPRE.SAT.windowDescriber`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.windowDescriber).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2429](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2429)
