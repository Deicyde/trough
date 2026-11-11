---
declaration: section
origin: cited
lean: MetaMathlibExt.bell_perm_second_kind_weakExcedance_eq_stirlingSecond, MetaMathlibExt.bell_count_perm_increasing_weakExcedance_letters
statement: formalized
proof: formalized
---

# Bell permutations and weak excedances

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/bell-permutations-and-weak-excedances/index.html).

## Weak excedances of Bell permutations of the second kind

Let $n \ge 1$ and $k$ be natural
numbers, and write $[n] = \{0, \dots, n-1\}$. A function $f : [n] \to [n]$ is a restricted
growth function if for every $i$, every $j < f(i)$ equals $f(i_0)$ for some $i_0 < i$. Its Bell
permutation is the product of transpositions $(0\ f(0))(1\ f(1)) \cdots (n-1\ f(n-1))$, composed
so that the rightmost factor acts first, where $(i\ i)$ denotes the identity. A weak excedance
of a permutation $\sigma$ of $[n]$ is an index $i$ with $i \le \sigma(i)$. Then the number of
permutations of $[n]$ that are the Bell permutation of some restricted growth function and have
exactly $k$ weak excedances is the Stirling number of the second kind $S(n, k)$.

## Sources

- Fufa Beyene, Jörgen Backelin, Roberto Mantaci, and Samuel A. Fufa, "Set Partitions and Other Bell Number Enumerated Objects," Journal of Integer Sequences 26 (2023), Article 23.1.8, Corollary, item 1, lines 283–290, https://cs.uwaterloo.ca/journals/JIS/VOL26/Beyene/beyene13.tex

Formalized by `MetaMathlibExt.bell_perm_second_kind_weakExcedance_eq_stirlingSecond`, a theorem declared in [MathlibExt/Combinatorics/BellPermutationsSecondKind.lean, line 662](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/BellPermutationsSecondKind.lean#L662). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/bell-permutations-and-weak-excedances/index.html#bell-perm-second-kind-weak-excedance-eq).

## Bell numbers count permutations with increasing weak excedance letters

A position $i$ is a
weak excedance of a permutation $\sigma$ when $i \le \sigma(i)$. For every $n$, the number of
permutations $\sigma$ of $\{0, 1, \dots, n-1\}$ such that $\sigma(i) < \sigma(j)$ whenever
$i < j$ are both weak excedances of $\sigma$ is the Bell number $B_n$.

## Sources

- Fufa Beyene, Jörgen Backelin, Roberto Mantaci, and Samuel A. Fufa, "Set Partitions and Other Bell Number Enumerated Objects," Journal of Integer Sequences 26 (2023), Article 23.1.8, Theorem, lines 434–436, https://cs.uwaterloo.ca/journals/JIS/VOL26/Beyene/beyene13.tex

Formalized by `MetaMathlibExt.bell_count_perm_increasing_weakExcedance_letters`, a theorem declared in [MathlibExt/Combinatorics/BellWeakExcedance.lean, line 1485](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/BellWeakExcedance.lean#L1485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/bell-permutations-and-weak-excedances/index.html#bell-count-perm-increasing-weak-excedanc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bell permutations and weak excedances](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/bell-permutations-and-weak-excedances/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/bell-permutations-and-weak-excedances)
