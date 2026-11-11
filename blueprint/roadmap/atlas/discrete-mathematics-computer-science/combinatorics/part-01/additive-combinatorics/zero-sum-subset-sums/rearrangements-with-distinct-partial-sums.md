---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ValidOrderingWanted.exists_distinct_partial_sums_ordering, MathlibExt.Combinatorics.ValidOrderingWanted.exists_freimanIso_to_int
statement: formalized
---

# Rearrangements with distinct partial sums

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/rearrangements-with-distinct-partial-sums/index.html).

## Valid orderings of finite sets of nonzero integers

Every finite set $A$ of nonzero
integers has a valid ordering: its elements can be listed as $a_1, \dots, a_m$, each exactly
once, so that the partial sums $a_1, a_1 + a_2, \dots, a_1 + \cdots + a_m$ are pairwise
distinct. The empty sum $0$ is not counted among the partial sums.

## Sources

- Noah Kravitz, "Rearranging Small Sets for Distinct Partial Sums", Theorem 2.

Stated but not proved: `MathlibExt.Combinatorics.ValidOrderingWanted.exists_distinct_partial_sums_ordering` is written with `theorem_wanted` in [WantedExt/Combinatorics/ValidOrderingWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ValidOrderingWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/rearrangements-with-distinct-partial-sums/index.html#exists-distinct-partial-sums-ordering).

## Lev's rectification principle

Let $\ell \ge 2$ be a natural number, $p$ a prime and
$A$ a subset of $\mathbb{Z}/p\mathbb{Z}$ with $|A| \le \lceil \log p / \log \ell \rceil$. Then
there are a finite set $B$ of integers and a map $f \colon \mathbb{Z}/p\mathbb{Z} \to \mathbb{Z}$
that is a Freiman isomorphism of order $\ell$ from $A$ to $B$: $f$ maps $A$ bijectively onto
$B$, and for all $a_1, \dots, a_\ell, b_1, \dots, b_\ell \in A$ we have
$f(a_1) + \cdots + f(a_\ell) = f(b_1) + \cdots + f(b_\ell)$ if and only if
$a_1 + \cdots + a_\ell = b_1 + \cdots + b_\ell$.

## Sources

- Noah Kravitz, "Rearranging Small Sets for Distinct Partial Sums", Theorem 3.

Stated but not proved: `MathlibExt.Combinatorics.ValidOrderingWanted.exists_freimanIso_to_int` is written with `theorem_wanted` in [WantedExt/Combinatorics/ValidOrderingWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ValidOrderingWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/rearrangements-with-distinct-partial-sums/index.html#exists-freiman-iso-to-int).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rearrangements with distinct partial sums](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/rearrangements-with-distinct-partial-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/rearrangements-with-distinct-partial-sums)
