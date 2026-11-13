---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.BlockCompatibleSequenceCountWanted.IsPBD, MathlibExt.Combinatorics.BlockCompatibleSequenceCountWanted.BlockCompatible, MathlibExt.Combinatorics.BlockCompatibleSequenceCountWanted.conjecture, MathlibExt.Combinatorics.BlockCompatibleSequenceCountWanted.conjecture_holds
statement: formalized
---

# Block-compatible sequences of pairwise balanced designs

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/block-compatible-sequences-of-pairwise-balanced/index.html).

## Pairwise balanced design

For a natural number $n$, a finite list of blocks
$B_1, \ldots, B_m \subseteq \{0, \ldots, n - 1\}$ is a pairwise balanced design on these $n$ points
when the blocks are pairwise distinct, every block has at least two points, and every two distinct
points lie in exactly one common block.

Formalized by `MathlibExt.Combinatorics.BlockCompatibleSequenceCountWanted.IsPBD`, a definition declared in [WantedExt/Combinatorics/BlockCompatibleSequenceCountWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BlockCompatibleSequenceCountWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/block-compatible-sequences-of-pairwise-balanced/index.html#is-pbd).

## Block-compatible sequences

For a natural number $n$, a finite sequence
$(x_1, \ldots, x_m)$ of natural numbers is block-compatible for $n$ when
$x_1 \ge x_2 \ge \cdots \ge x_m$, every $x_k$ satisfies $2 \le x_k \le n$, and there is a pairwise
balanced design on the point set $\{0, \ldots, n - 1\}$ whose blocks, listed in order as
$B_1, \ldots, B_m$, have sizes $|B_k| = x_k$ for every $k$.

Formalized by `MathlibExt.Combinatorics.BlockCompatibleSequenceCountWanted.BlockCompatible`, a definition declared in [WantedExt/Combinatorics/BlockCompatibleSequenceCountWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BlockCompatibleSequenceCountWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/block-compatible-sequences-of-pairwise-balanced/index.html#block-compatible).

## Many block-compatible sequences

The statement that there are a real number $c > 0$ and a
natural number $N$ such that for every $n \ge N$ there is a finite set of at least
$\exp(c \sqrt{n} \log n)$ distinct finite sequences of natural numbers, each of which is
block-compatible for $n$. Here $\log$ is the natural logarithm.

## Sources

- OWR-14299518-002, question (2).

Formalized by `MathlibExt.Combinatorics.BlockCompatibleSequenceCountWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/BlockCompatibleSequenceCountWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BlockCompatibleSequenceCountWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/block-compatible-sequences-of-pairwise-balanced/index.html#conjecture).

## Many block-compatible sequences (Erdős Problem 732)

There are a real number $c > 0$ and a
natural number $N$ such that for every $n \ge N$ there is a finite set of at least
$\exp(c \sqrt{n} \log n)$ distinct finite sequences of natural numbers, each of which is
block-compatible for $n$. Here $\log$ is the natural logarithm.

Alon proved the stronger bound that at least $2^{(1/2 + o(1)) \sqrt{n} \log n}$ sequences are
block-compatible for $n$ (Oberwolfach Report 42/2025, Theorem 4; also Theorem 2.3 of his note
'Blocking partial designs and block-compatible sequences').

## Sources

- N. Alon, On designs and partial designs, extended abstract in Oberwolfach Report 42/2025 (Combinatorics, Probability and Computing), pp. 2249-2250, Theorem 4, https://doi.org/10.4171/owr/2025/42; N. Alon, Blocking partial designs and block-compatible sequences, note, Theorem 2.3, https://web.math.princeton.edu/~nalon/PDFS/remark191.pdf; T. F. Bloom, Erdős Problem #732, erdosproblems.com (status PROVED), https://www.erdosproblems.com/732.

Stated but not proved: `MathlibExt.Combinatorics.BlockCompatibleSequenceCountWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/BlockCompatibleSequenceCountWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BlockCompatibleSequenceCountWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/block-compatible-sequences-of-pairwise-balanced/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Block-compatible sequences of pairwise balanced designs](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/block-compatible-sequences-of-pairwise-balanced/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/designs-latin-squares/block-compatible-sequences-of-pairwise-balanced)
