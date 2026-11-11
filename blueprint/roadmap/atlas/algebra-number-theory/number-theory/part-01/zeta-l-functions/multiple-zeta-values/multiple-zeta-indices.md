---
declaration: section
origin: cited
lean: MetaMathlibExt.MultipleZeta.Index, MetaMathlibExt.MultipleZeta.Index.entries, MetaMathlibExt.MultipleZeta.Index.weight, MetaMathlibExt.MultipleZeta.Index.depth, MetaMathlibExt.MultipleZeta.Index.height, MetaMathlibExt.MultipleZeta.Index.IsAdmissible, MetaMathlibExt.MultipleZeta.IsAdmissible, MetaMathlibExt.MultipleZeta.Index.isAdmissible_iff
statement: formalized
proof: formalized
---

# Multiple-zeta indices

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-indices/index.html).

## Multiple-zeta index

An index is a finite sequence $(k_1, \ldots, k_r)$ of positive
integers with $r \ge 0$, so the empty sequence is allowed. It is represented as a natural
number $n$ together with a composition of $n$, that is, a sequence of positive integers with
sum $n$.

## Sources

- clause D1 (`2608.10675:D01`, `2307.09867:D01`).

Formalized by `MetaMathlibExt.MultipleZeta.Index`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Index.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Index.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-indices/index.html#index-2).

## Entries of an index

The entries of an index $(k_1, \ldots, k_r)$ form the list
$[k_1, \ldots, k_r]$ of its terms, in order.

## Sources

- clause D2 (`2608.10675:D01`, `2307.09867:D01`).

Formalized by `MetaMathlibExt.MultipleZeta.Index.entries`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Index.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Index.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-indices/index.html#entries).

## Weight of an index

The weight of an index $(k_1, \ldots, k_r)$ is the sum
$k_1 + \cdots + k_r$ of its entries.

## Sources

- clause D3 (`2307.09867:D01`).

Formalized by `MetaMathlibExt.MultipleZeta.Index.weight`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Index.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Index.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-indices/index.html#weight).

## Depth of an index

The depth of an index $(k_1, \ldots, k_r)$ is its number of
entries $r$.

## Sources

- clause D4 (`2608.10675:D01`, `2307.09867:D01`).

Formalized by `MetaMathlibExt.MultipleZeta.Index.depth`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Index.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Index.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-indices/index.html#depth).

## Height of an index

The height of an index $(k_1, \ldots, k_r)$ is the number of
positions $i$ with $1 \le i \le r$ and $k_i \ge 2$.

## Sources

- clause D5 (`2307.09867:D01`).

Formalized by `MetaMathlibExt.MultipleZeta.Index.height`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Index.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Index.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-indices/index.html#height).

## Admissible index

An index $(k_1, \ldots, k_r)$ is admissible when it is nonempty
($r \ge 1$) and its first entry satisfies $k_1 \ge 2$.

## Sources

- clause D6 (`2307.09867:D01`).

Formalized by `MetaMathlibExt.MultipleZeta.Index.IsAdmissible`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Index.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Index.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-indices/index.html#is-admissible).

## Admissible list

A list $[k_1, \ldots, k_r]$ of natural numbers is admissible when it
is nonempty ($r \ge 1$), $k_1 \ge 2$, and $k_i > 0$ for every $i$ with $2 \le i \le r$.

This is the admissibility condition for multiple-zeta indices in decreasing summation order.

## Sources

- `2307.09867:D01`.

Formalized by `MetaMathlibExt.MultipleZeta.IsAdmissible`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Index.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Index.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-indices/index.html#is-admissible-2).

## Admissibility of an index via its entries

An index is admissible if and only if the
list of its entries is an admissible list.

Formalized by `MetaMathlibExt.MultipleZeta.Index.isAdmissible_iff`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/Index.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Index.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-indices/index.html#is-admissible-iff).

## Hoffman block

For a positive integer $k$, the Hoffman block $z_k = x^{k-1} y$ is the
word in the free monoid on two letters $x$ and $y$ consisting of $k - 1$ copies of $x$ followed
by one $y$.

The free monoid is taken on the booleans, with false standing for $x$ and true for $y$.

## Sources

- `2307.09867:D05`.

Formalized by `MetaMathlibExt.MultipleZeta.hoffmanBlock`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Index.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Index.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-indices/index.html#hoffman-block).

## Hoffman block as a list

For every positive integer $k$, the list of letters of the
Hoffman block $z_k$ consists of $k - 1$ copies of $x$ (false) followed by one $y$ (true).

Formalized by `MetaMathlibExt.MultipleZeta.toList_hoffmanBlock`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/Index.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Index.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-indices/index.html#to-list-hoffman-block).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiple-zeta indices](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-indices/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-indices)
