---
declaration: section
origin: cited
lean: MetaMathlibExt.domino_tiling_sequence_factorization, MetaMathlibExt.boxProd_tiling_card_eq_fib_mul_pellNumber, MetaMathlibExt.boxProd_tiling_card_eq_fib_mul_pell
statement: formalized
proof: formalized
---

# Domino tilings and Fibonacci–Pell products

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/domino-tilings-and-fibonacci-pell-products/index.html).

## Factorization of the domino tiling sequence

Let $d$ and $g$ be sequences of natural
numbers with $d_1 = 1$, $d_2 = 8$, $d_3 = 95$, $d_4 = 1183$ and
$d_{n+4} + 32 d_{n+2} + d_n = 15 d_{n+3} + 15 d_{n+1}$ for all $n \ge 1$, and with $g_1 = 1$,
$g_2 = 4$ and $g_{n+2} + g_n = 5 g_{n+1}$ for all $n \ge 1$. Then $d_n = g_n F_{2n-1}$ for every
$n \ge 1$, where $F_m$ is the $m$-th Fibonacci number ($F_0 = 0$, $F_1 = 1$).

These recurrences determine $d_n$ and $g_n$ for $n \ge 1$: $d_n$ is the number of domino tilings
of $P_5 \times P_{2n-2}$ (OEIS A003775) and $g_n$ is OEIS A004253.

## Sources

- James A. Sellers, "Domino Tilings and Products of Fibonacci and Pell Numbers," Journal of Integer Sequences 5 (2002), Article 02.1.2, second Theorem (`d_n = g_n h_n`), lines 153–154, with `d` defined at lines 146–150 and `g` at line 164, https://cs.uwaterloo.ca/journals/JIS/VOL5/Sellers/sellers4.tex

Formalized by `MetaMathlibExt.domino_tiling_sequence_factorization`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/DominoTilingSequenceFactorization.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/DominoTilingSequenceFactorization.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/domino-tilings-and-fibonacci-pell-products/index.html#domino-tiling-sequence-factorization).

## Sellers' domino tiling theorem

Let $W_4$ be the complete graph $K_4$ with one edge
removed and $P_{n-1}$ the path graph on $n - 1$ vertices. For every natural number $n \ge 2$,
the number of perfect matchings (domino tilings) of the Cartesian product $W_4 \square P_{n-1}$
equals $f_n p_n$, where $f_n$ is the $n$-th Fibonacci number ($f_0 = 0$, $f_1 = 1$) and $p_n$ is
the $n$-th Pell number ($p_0 = 0$, $p_1 = 1$, $p_{k+2} = 2 p_{k+1} + p_k$).

Formalized by `MetaMathlibExt.boxProd_tiling_card_eq_fib_mul_pellNumber`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/W4PathDominoTilings.lean, line 1748](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/W4PathDominoTilings.lean#L1748). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/domino-tilings-and-fibonacci-pell-products/index.html#box-prod-tiling-card-eq-fib-mul-pell-num).

## Sellers' domino tiling theorem, recursive Pell form

Let $W_4$ be the complete graph
$K_4$ with one edge removed and $P_{n-1}$ the path graph on $n - 1$ vertices. For every natural
number $n \ge 2$, the number of perfect matchings (domino tilings) of the Cartesian product
$W_4 \square P_{n-1}$ equals $f_n p_n$, where $f_n$ is the $n$-th Fibonacci number
($f_0 = 0$, $f_1 = 1$) and $p_n$ is defined by $p_0 = 0$, $p_1 = 1$ and
$p_{k+2} = 2 p_{k+1} + p_k$.

The Cartesian product $\square$ is the paper's $\times$, following Faase. The paper writes
$c_n$ for this number of tilings; its values $c_2 = 2$, $c_3 = 10$, $c_4 = 36$ match $f_n p_n$.

## Sources

- James A. Sellers, "Domino Tilings and Products of Fibonacci and Pell Numbers," Journal of Integer Sequences 5 (2002), Article 02.1.2, Theorem, lines 105–108, https://cs.uwaterloo.ca/journals/JIS/VOL5/Sellers/sellers4.tex

Formalized by `MetaMathlibExt.boxProd_tiling_card_eq_fib_mul_pell`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/W4PathDominoTilings.lean, line 1798](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/W4PathDominoTilings.lean#L1798). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/domino-tilings-and-fibonacci-pell-products/index.html#box-prod-tiling-card-eq-fib-mul-pell).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Domino tilings and Fibonacci–Pell products](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/domino-tilings-and-fibonacci-pell-products/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/tilings-board-placements/domino-tilings-and-fibonacci-pell-products)
