---
declaration: section
origin: cited
lean: MetaMathlibExt.singer_cyclic_difference_set_exists
statement: formalized
proof: formalized
---

# Sidon sets and difference sets: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/index.html).

Sidon and B_h-sets (bounds, counts, greedy and thick constructions, isolated sums, the Sidon ideal), Golomb rulers, difference bases, cyclic and perfect difference sets including Singer's theorem, and difference sets of sparse sets.

## Singer's difference set theorem

For every prime power $q$, there is a subset $D$ of the
cyclic group $\mathbb{Z}/(q^2 + q + 1)\mathbb{Z}$ with $q + 1$ elements such that every nonzero
element $x$ of this group can be written as $x = a - b$ for exactly one ordered pair $(a, b)$ of
elements of $D$.

Formalized by `MetaMathlibExt.singer_cyclic_difference_set_exists`, a theorem declared in [MathlibExt/Combinatorics/Additive/SingerDifferenceSet.lean, line 751](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/SingerDifferenceSet.lean#L751). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/index.html#singer-cyclic-difference-set-exists).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sidon sets and difference sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets)
