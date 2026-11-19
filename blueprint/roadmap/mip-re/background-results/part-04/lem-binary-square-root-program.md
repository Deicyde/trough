---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.rootBitsProg, MIPRE.LowDegree.rootBitsProg_time_le, MIPRE.LowDegree.groupOfBits_rootBits, MIPRE.LowDegree.rootBitsProg_square
statement: formalized
proof: formalized
---

# The binary square-root program

For odd $k$, the square-root permutation on the coefficient vector of $\mathbb{F}_2[\mathbb{Z}/k\mathbb{Z}]$ is computed by one uniform ambient program in time polynomial in $k$. The output vector has length $k$ and represents a square root of the input group-algebra element.

## Depends on

- [Self-dualization in the group algebra](lem-group-algebra-selfdualization.md)
- [The low-degree code](../../structure-of-the-proof/part-07/def-ld-encoding.md)

## Proof

Split the list into coefficients in even positions and coefficients in odd positions, then append those lists. At position $i$ this reads the coefficient at $2i$ modulo $k$. A size-bounded fold implements the split. The input encoding has size at most $4k+1$, giving the stated polynomial bound. The preceding lemma supplies the algebraic identity.

## Lean

Formalized as [`MIPRE.LowDegree.rootBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.rootBitsProg), [`MIPRE.LowDegree.rootBitsProg_time_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.rootBitsProg_time_le), [`MIPRE.LowDegree.groupOfBits_rootBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.groupOfBits_rootBits), [`MIPRE.LowDegree.rootBitsProg_square`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.rootBitsProg_square).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6439](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6439)
