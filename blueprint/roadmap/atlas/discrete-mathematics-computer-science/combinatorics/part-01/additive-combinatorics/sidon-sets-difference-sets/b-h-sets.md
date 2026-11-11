---
declaration: section
origin: cited
lean: AdditiveCombinatorics.sumNE, AdditiveCombinatorics.sumNE_proof_irrel, AdditiveCombinatorics.IsBhSet
statement: formalized
proof: formalized
---

# B_h-sets

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/b-h-sets/index.html).

## Sum of a nonempty list

For a nonempty list $(a_1, \dots, a_k)$ of elements of a type with
an addition, its sum is obtained by adding the entries from left to right starting from the head:
it is $a_1$ when $k = 1$, and $(\cdots((a_1 + a_2) + a_3) + \cdots) + a_k$ in general. No zero
element is needed, and the proof that the list is nonempty does not affect the value.

Formalized by `AdditiveCombinatorics.sumNE`, a definition declared in [MathlibExt/Combinatorics/Additive/BhSet.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/BhSet.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/b-h-sets/index.html#sum-ne).

## The sum of a nonempty list does not depend on the nonemptiness proof

For every list $l$
of elements of a type with an addition and any two proofs $e_1$ and $e_2$ that $l$ is nonempty,
the sum of $l$ computed with $e_1$ equals the sum of $l$ computed with $e_2$.

Formalized by `AdditiveCombinatorics.sumNE_proof_irrel`, a theorem declared in [MathlibExt/Combinatorics/Additive/BhSet.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/BhSet.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/b-h-sets/index.html#sum-ne-proof-irrel).

## $B_h$-set

Let $G$ be an additive commutative semigroup, $A \subseteq G$ and $h$ a natural
number. $A$ is a $B_h$-set if $A$ is nonempty, $h \ge 1$, and whenever two sequences
$(a_1, \dots, a_h)$ and $(b_1, \dots, b_h)$ of elements of $A$ satisfy
$a_1 + \dots + a_h = b_1 + \dots + b_h$, the sequence $(b_1, \dots, b_h)$ is a rearrangement of
$(a_1, \dots, a_h)$.

Repeated summands are allowed: the entries of each sequence need not be distinct. No zero element
is assumed.

Formalized by `AdditiveCombinatorics.IsBhSet`, a definition declared in [MathlibExt/Combinatorics/Additive/BhSet.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/BhSet.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/b-h-sets/index.html#is-bh-set).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: B_h-sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/b-h-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/b-h-sets)
