---
declaration: lemma
origin: cited
lean: MIPRE.SAT.DecoupledDescriber, MIPRE.SAT.decoupledDescriber
statement: formalized
proof: formalized
---

# Succinct decoupled 5SAT

There is a polynomial-time algorithm that, on the inputs of Theorem [Explicit succinct Cook–Levin](../../background-results/part-04/thm-succinct-sat.md) under the same hypotheses, outputs a circuit with two inputs of length $\ell_0 = \lceil \log 2T \rceil$, three of length $r_0 = O(\log T + \log \sigma)$ and five single-bit inputs, with at most $s_0 = \mathrm{poly}(\log T, \log n, Q, \sigma)$ gates, which describes the decider $\mathcal{D}$ on $(n, x, y)$ at time $T$ in the sense of Definition [Succinctly described 3SAT and decoupled 5SAT](../../background-results/part-03/def-succinct-3sat.md): the variables of the decoupled 5SAT formula fall into five blocks, the first two being the players' answer strings, and every clause touches each block once. The parameters $\ell_0, r_0, s_0$ are computable in time polynomial in the bit lengths of $n, T, Q, \sigma$. (The padded description, with the outer variable count a power of two, is the padding step of the PCP, Remark [Why $m$ is a power of two](../README.md).)

## Depends on

- [Succinctly described 3SAT and decoupled 5SAT](../../background-results/part-03/def-succinct-3sat.md)
- [Decider](../../foundations/part-03/def-decider.md)
- [Multi-input Turing machine](../../computability/def-multiinput-tm.md)

## Proof

Run the describer of Theorem [Explicit succinct Cook–Levin](../../background-results/part-04/thm-succinct-sat.md) to get a circuit $C_3$ on $3 r_0 + 3$ inputs, $r_0$ being that theorem's index width, and set $\ell_0 = \lceil \log 2T \rceil$. Since $2^{r_0} \geq 4T$ and $2^{\ell_0} < 4T$ we have $\ell_0 \leq r_0$, so an $\ell_0$-bit index compared with an $r_0$-bit one is zero-padded and $i_2 + 2T < 4T \leq 2^{r_0}$ does not overflow. The output circuit accepts $(i_1, \ldots, i_5, o_1, \ldots, o_5)$ when any of nine conditions holds: the first is $C_3(i_3, i_4, i_5, o_3, o_4, o_5) = 1$, and the other eight are $i_1 < 2T \land i_1 = i_3 \land o_1 \neq o_3$; $i_2 < 2T \land i_3 = i_2 + 2T \land o_2 \neq o_3$; $i_1 \geq 2T$ with $i_1$ even and $o_1 = 1$, or $i_1$ odd and $o_1 = 0$; the same two for $i_2, o_2$; $i_3 = i_4 \land o_3 \neq o_4$; and $i_4 = i_5 \land o_4 \neq o_5$.

For a fixed triple of indices the signs of the blocks a condition does not constrain range over all of $\{0,1\}^3$, so a decoupled clause is satisfied exactly when the literals of the blocks it does constrain are. The last two conditions therefore say $w_1 = w_2 = w_3$, the first two that the common assignment agrees with $a$ below $2T$ and with $b$ on $[2T, 4T)$, and the middle four that $a$ and $b$ carry the blank padding above $2T$. So a satisfying five-tuple is exactly a satisfying assignment of $\varphi_{3}$ extending the answer blocks, and item 1 of Theorem [Explicit succinct Cook–Levin](../../background-results/part-04/thm-succinct-sat.md) finishes it. Sizes and running times are those of $C_3$ plus $O(r_0)$ gates for the eight conditions.

## Lean

Formalized as [`MIPRE.SAT.DecoupledDescriber`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.DecoupledDescriber), [`MIPRE.SAT.decoupledDescriber`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.decoupledDescriber).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4624](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4624)
