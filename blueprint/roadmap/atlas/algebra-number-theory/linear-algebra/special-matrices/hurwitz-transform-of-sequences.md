---
declaration: section
origin: cited
lean: MetaMathlibExt.hurwitzEntry, MetaMathlibExt.hurwitzMatrix, MetaMathlibExt.hurwitzTransform, MetaMathlibExt.hurwitzSingle
statement: formalized
proof: formalized
---

# Hurwitz transform of sequences

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/hurwitz-transform-of-sequences/index.html).

## Entries of the Hurwitz matrix

For sequences $a, b \colon \mathbb{N} \to R$ in a commutative
ring $R$ and indices $i, j \in \mathbb{N}$ (counted from zero), the Hurwitz entry $h_{ij}$ is $0$ if
$i \ge 2j + 2$; otherwise it is $a_{j - i/2}$ if $i$ is even and $b_{j - (i-1)/2}$ if $i$ is odd.

## Sources

- Barry's definition in the Journal of Integer Sequences, vol. 15.

Formalized by `MetaMathlibExt.hurwitzEntry`, a definition declared in [MathlibExt/LinearAlgebra/HurwitzTransform.lean, line 20](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/HurwitzTransform.lean#L20). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/hurwitz-transform-of-sequences/index.html#hurwitz-entry).

## Hurwitz matrix

For sequences $a, b \colon \mathbb{N} \to R$ in a commutative ring $R$ and
$n \in \mathbb{N}$, the Hurwitz matrix of order $n$ is the $(n+1) \times (n+1)$ matrix whose entry
in row $i$ and column $j$, for $0 \le i, j \le n$, is the Hurwitz entry $h_{ij}$ of $a$ and $b$.

Formalized by `MetaMathlibExt.hurwitzMatrix`, a definition declared in [MathlibExt/LinearAlgebra/HurwitzTransform.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/HurwitzTransform.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/hurwitz-transform-of-sequences/index.html#hurwitz-matrix).

## Hurwitz transform

For sequences $a, b \colon \mathbb{N} \to R$ in a commutative ring $R$,
the Hurwitz transform of $a$ and $b$ is the sequence whose $n$-th term, for $n \in \mathbb{N}$, is
the determinant of the Hurwitz matrix of $a$ and $b$ of order $n$.

Formalized by `MetaMathlibExt.hurwitzTransform`, a definition declared in [MathlibExt/LinearAlgebra/HurwitzTransform.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/HurwitzTransform.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/hurwitz-transform-of-sequences/index.html#hurwitz-transform).

## Hurwitz transform of a single sequence

For a sequence $a \colon \mathbb{N} \to R$ in a
commutative ring $R$, its Hurwitz transform is the Hurwitz transform of $a$ and the sequence
$(0^k)_{k \in \mathbb{N}}$, which is $1$ at $k = 0$ and $0$ for $k \ge 1$.

Formalized by `MetaMathlibExt.hurwitzSingle`, a definition declared in [MathlibExt/LinearAlgebra/HurwitzTransform.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/HurwitzTransform.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/hurwitz-transform-of-sequences/index.html#hurwitz-single).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hurwitz transform of sequences](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/hurwitz-transform-of-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/special-matrices/hurwitz-transform-of-sequences)
