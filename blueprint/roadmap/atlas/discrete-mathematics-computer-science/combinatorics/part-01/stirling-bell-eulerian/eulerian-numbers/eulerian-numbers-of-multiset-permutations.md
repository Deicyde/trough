---
declaration: section
origin: cited
lean: MetaMathlibExt.multisetDescentNumber, MetaMathlibExt.IsMultisetPermutation, MetaMathlibExt.multisetEulerianNumber
statement: formalized
proof: formalized
---

# Eulerian numbers of multiset permutations

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/eulerian-numbers-of-multiset-permutations/index.html).

## Descent number of a word

For a word $w = w_1 \cdots w_K$ of length $K$ over the alphabet
$\{0, 1, \dots, m-1\}$, the descent number of $w$ is one more than its number of descents:
$1 + \#\{j : 1 \le j < K,\ w_j > w_{j+1}\}$.

The extra $1$ follows the source convention, which also counts a descent at the end of the
word; in particular the empty word has descent number $1$.

Formalized by `MetaMathlibExt.multisetDescentNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MultisetEulerianNumber.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MultisetEulerianNumber.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/eulerian-numbers-of-multiset-permutations/index.html#multiset-descent-number).

## Multiset permutation

Let $k_0, \dots, k_{m-1}$ be natural numbers. A word
$w = w_1 \cdots w_K$ of length $K$ over the alphabet $\{0, 1, \dots, m-1\}$ is a permutation of
the multiset with $k_i$ copies of each letter $i$ when, for every letter $i$, exactly $k_i$
positions $j$ have $w_j = i$.

Formalized by `MetaMathlibExt.IsMultisetPermutation`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MultisetEulerianNumber.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MultisetEulerianNumber.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/eulerian-numbers-of-multiset-permutations/index.html#is-multiset-permutation).

## Eulerian numbers of multiset permutations

Let $k_0, \dots, k_{m-1}$ be natural numbers
with sum $K$, and let $p$ be a natural number. The multiset Eulerian number is the number of
words of length $K$ over the alphabet $\{0, 1, \dots, m-1\}$ that are permutations of the
multiset with $k_i$ copies of each letter $i$ and whose descent number, one more than the
number of descents, equals $p$.

For multiplicities $2, 2$, its nonzero values are $1, 4, 1$ at $p = 1, 2, 3$.

Formalized by `MetaMathlibExt.multisetEulerianNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MultisetEulerianNumber.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MultisetEulerianNumber.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/eulerian-numbers-of-multiset-permutations/index.html#multiset-eulerian-number).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Eulerian numbers of multiset permutations](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/eulerian-numbers-of-multiset-permutations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/eulerian-numbers-of-multiset-permutations)
