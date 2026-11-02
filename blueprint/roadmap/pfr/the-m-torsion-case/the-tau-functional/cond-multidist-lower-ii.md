---
declaration: corollary
origin: cited
lean: sub_condMultiDistance_le'
statement: formalized
proof: formalized
---

# Lower bound on conditional multidistance, II

With the notation of the previous lemma, we have

$$
k - D[ X'_{[m]} | Y_{[m]} ] \leq \eta \sum_{i=1}^m d[X_{\sigma(i)};X'_i|Y_i]\qquad\text{(3)}
$$

for any permutation $\sigma : \{1,\dots,m\} \rightarrow \{1,\dots,m\}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Lower bound on conditional multidistance](cond-multidist-lower.md)
- [Relabeling](../multidistance/multidist-perm.md)

## Proof

This follows from [Lower bound on conditional multidistance](cond-multidist-lower.md) and [Relabeling](../multidistance/multidist-perm.md).

## Lean

Formalized as [`sub_condMultiDistance_le'`](https://teorth.github.io/pfr/docs/find/#doc/sub_condMultiDistance_le').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 363](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L363)
