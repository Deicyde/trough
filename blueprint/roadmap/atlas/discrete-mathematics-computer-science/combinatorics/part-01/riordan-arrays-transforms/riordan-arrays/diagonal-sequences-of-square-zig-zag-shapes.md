---
declaration: section
origin: cited
lean: MetaMathlibExt.rightDownDiagonalCoefficient, MetaMathlibExt.IsRightDownDiagonalFamily
statement: formalized
proof: formalized
---

# Diagonal sequences of square zig-zag shapes

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/diagonal-sequences-of-square-zig-zag-shapes/index.html).

## Right-down diagonal coefficient

For natural numbers $k$ and $i$, the coefficient
$c_k(i)$ of the right-down diagonal recurrence is the integer $(-1)^i \binom{k+1-i}{i+1}$ when
$i \le k+1$, and $0$ when $i > k+1$.

Formalized by `MetaMathlibExt.rightDownDiagonalCoefficient`, a definition declared in [MathlibExt/Combinatorics/Enumerative/RightDownDiagonalSequences.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/RightDownDiagonalSequences.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/diagonal-sequences-of-square-zig-zag-shapes/index.html#right-down-diagonal-coefficient).

## Right-down diagonal families of order $k$

For a natural number $k$, a family
$(A_j)_{0 \le j \le k+1}$ of integer sequences $A_j : \mathbb{N} \to \mathbb{Z}$ is a family of
right-down diagonal sequences of order $k$ when $k \ge 1$ and, for every $j$ and every natural
number $n \ge \lfloor k/2 \rfloor + 1$,

$$A_j(n) = \sum_{i=0}^{\lfloor k/2 \rfloor} c_k(i)\, A_j(n-1-i),$$

where $c_k(i) = (-1)^i \binom{k+1-i}{i+1}$ is the right-down diagonal coefficient.

## Sources

- László Németh and László Szalay, *Sequences Involving Square Zig-Zag Shapes*, Journal of Integer Sequences 24 (2021), Article 21.5.2.

Formalized by `MetaMathlibExt.IsRightDownDiagonalFamily`, a definition declared in [MathlibExt/Combinatorics/Enumerative/RightDownDiagonalSequences.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/RightDownDiagonalSequences.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/diagonal-sequences-of-square-zig-zag-shapes/index.html#is-right-down-diagonal-family).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Diagonal sequences of square zig-zag shapes](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/diagonal-sequences-of-square-zig-zag-shapes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/diagonal-sequences-of-square-zig-zag-shapes)
