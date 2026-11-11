---
declaration: section
origin: cited
lean: AdditiveCombinatorics.sumConv, AdditiveCombinatorics.orderedRepresentationCount, AdditiveCombinatorics.orderedRepresentationCount_pos_iff
statement: formalized
proof: formalized
---

# Additive representation functions

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/additive-representation-functions/index.html).

## Sum convolution

Let $R$ be a semiring. The sum convolution, or Cauchy product, of two
functions $f, g \colon \mathbb{N} \to R$ is the function $\mathbb{N} \to R$ whose value at
$n \in \mathbb{N}$ is

$$\sum_{a + b = n} f(a)\, g(b),$$

where the sum runs over all pairs $(a, b)$ of natural numbers with $a + b = n$.

Formalized by `AdditiveCombinatorics.sumConv`, a definition declared in [MathlibExt/Combinatorics/Additive/Convolution.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/Convolution.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/additive-representation-functions/index.html#sum-conv).

## Ordered representation count

For a set $A$ of natural numbers and a natural number $n$,
the ordered representation count of $n$ by $A$ is the number of ordered pairs
$(a, b) \in A \times A$ with $a + b = n$. Pairs are not identified under swapping: when $a \ne b$,
the pairs $(a, b)$ and $(b, a)$ are counted separately.

Formalized by `AdditiveCombinatorics.orderedRepresentationCount`, a definition declared in [MathlibExt/Combinatorics/Additive/RepresentationCount.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/RepresentationCount.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/additive-representation-functions/index.html#ordered-representation-count).

## Positivity of the ordered representation count

For a set $A$ of natural numbers and a
natural number $n$, the number of ordered pairs $(a, b) \in A \times A$ with $a + b = n$ is
positive if and only if $n = a + b$ for some $a \in A$ and $b \in A$.

Formalized by `AdditiveCombinatorics.orderedRepresentationCount_pos_iff`, a theorem declared in [MathlibExt/Combinatorics/Additive/RepresentationCount.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/RepresentationCount.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/additive-representation-functions/index.html#ordered-representation-count-pos-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Additive representation functions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/additive-representation-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/additive-bases/additive-representation-functions)
