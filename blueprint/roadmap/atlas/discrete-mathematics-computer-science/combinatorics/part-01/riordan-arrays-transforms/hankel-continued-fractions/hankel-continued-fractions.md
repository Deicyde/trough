---
declaration: section
origin: cited
lean: MetaMathlibExt.layman_binomial_transform_hankel_invariant
statement: formalized
proof: formalized
---

# Hankel determinants and continued fractions: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/index.html).

Hankel transforms of sequences and their invariance under binomial transforms, Heilermann's formula linking Jacobi continued fractions to weighted Motzkin paths, Catalan-sum Hankel determinants, and Toeplitz–Hessenberg determinants.

## Layman's theorem: the binomial transform preserves the Hankel transform

For every
sequence of integers $(a_n)_{n \ge 0}$, the Hankel transform of the binomial transform of $a$
equals the Hankel transform of $a$. Here the binomial transform of $a$ is the sequence
$b_n = \sum_{i=0}^{n} \binom{n}{i} a_i$, and the Hankel transform of a sequence $c$ is the
sequence whose $n$-th term, for $n \ge 0$, is the determinant of the $(n+1) \times (n+1)$
matrix $(c_{i+j})_{0 \le i, j \le n}$.

## Sources

- John W. Layman, *The Hankel Transform and Some of its Properties*, Journal of Integer Sequences 4 (2001), Theorem 1, <https://cs.uwaterloo.ca/journals/JIS/VOL4/LAYMAN/hankel.pdf>. Campaign source passage: Mahid M. Mangontarum, <https://cs.uwaterloo.ca/journals/JIS/VOL20/Mangontarum/mango4.tex>, lines 535-557.

Formalized by `MetaMathlibExt.layman_binomial_transform_hankel_invariant`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/LaymanBinomialTransformHankel.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/LaymanBinomialTransformHankel.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/index.html#layman-binomial-transform-hankel-invaria).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hankel determinants and continued fractions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions)
