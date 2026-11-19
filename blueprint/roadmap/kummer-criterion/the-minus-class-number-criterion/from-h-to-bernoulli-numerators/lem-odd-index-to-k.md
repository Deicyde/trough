---
declaration: lemma
origin: cited
lean: KummerCriterion.exists_odd_index_iff_exists_k
statement: formalized
proof: formalized
---

# odd-index-to-k

For any predicate $Q$ on natural numbers,

$$
\bigl(\exists j,\ j\lt p-2,\ j\ \mathrm{odd},\ Q(j+1)\bigr)
\quad\Longleftrightarrow\quad
\bigl(\exists k,\ 1\le k,\ 2k\le p-3,\ Q(2k)\bigr).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

If $j$ is odd, write $j=2k-1$ with $k \ge 1$, so $j+1=2k$, and $j < p-2$ becomes $2k \le p-3$ after parity bookkeeping. Conversely, an even index $2k$ in Kummer's range corresponds to the odd index $j=2k-1 < p-2$.

## Lean

Formalized as [`KummerCriterion.exists_odd_index_iff_exists_k`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.exists_odd_index_iff_exists_k).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 280](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L280)
