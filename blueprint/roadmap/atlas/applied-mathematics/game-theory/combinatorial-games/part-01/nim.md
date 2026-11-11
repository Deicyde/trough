---
declaration: section
origin: cited
lean: MetaMathlibExt.BoutonNim.bouton_nim_p_positions, MetaMathlibExt.nim_sum_eq_zero_iff_last_eq_xor_fold
statement: formalized
proof: formalized
---

# Nim

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim/index.html).

## Bouton's move properties in Nim

Let a Nim position be a finite list of heap sizes
$a_1, \dots, a_n \in \mathbb{N}$, with nim-sum $a_1 \oplus \cdots \oplus a_n$, where $\oplus$
is bitwise exclusive or and the empty list has nim-sum $0$. A move chooses an index $i$ and
replaces $a_i$ by a natural number $y < a_i$. Then: (i) if the position has nim-sum $0$, every
move leads to a position with nonzero nim-sum; (ii) if the position has nonzero nim-sum, some
move leads to a position with nim-sum $0$.

Positions with no move (the empty list and the all-zero lists) have nim-sum $0$, so the two
properties determine the normal-play labelling by induction on the game: the positions with
nim-sum $0$ are exactly the P-positions (previous player wins) and the others are the
N-positions.

## Sources

- Tanya Khovanova and Joshua Xiong, "Nim Fractals", Journal of Integer Sequences 17 (2014), theorem lines 155–159, https://cs.uwaterloo.ca/journals/JIS/VOL17/Khovanova/khova6.tex.

Formalized by `MetaMathlibExt.BoutonNim.bouton_nim_p_positions`, a theorem declared in [MathlibExt/GameTheory/BoutonNim.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/BoutonNim.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim/index.html#bouton-nim-p-positions).

## Nim-sum zero via the last pile

For natural numbers $a_1, \dots, a_n$ (the preceding piles)
and $b$ (the last pile), the nim-sum $a_1 \oplus \cdots \oplus a_n \oplus b$ is $0$ if and only if
$b = a_1 \oplus \cdots \oplus a_n$, where $\oplus$ is bitwise exclusive or and the nim-sum of no
piles is $0$.

This is only the nim-sum identity behind the source's corollary. The corollary itself
characterizes P-positions; its game-theoretic content, that the nim-sum-zero positions are
exactly the P-positions, is Bouton's theorem.

## Sources

- Tanya Khovanova and Joshua Xiong, "Nim Fractals," Journal of Integer Sequences 17 (2014), Article 14.7.8, Corollary, lines 163–165, https://cs.uwaterloo.ca/journals/JIS/VOL17/Khovanova/khova6.tex

Formalized by `MetaMathlibExt.nim_sum_eq_zero_iff_last_eq_xor_fold`, a theorem declared in [MathlibExt/GameTheory/NimSumLastPile.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/NimSumLastPile.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim/index.html#nim-sum-eq-zero-iff-last-eq-xor-fold).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nim](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GameTheory/combinatorial-games/nim)
