---
declaration: section
origin: cited
lean: MetaMathlibExt.worpitzky_identity_multiset
statement: formalized
proof: formalized
---

# Eulerian numbers and polynomials: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/index.html).

Counting permutations by descents or excedances: Eulerian numbers and polynomials, refined, multiset and generalized Eulerian polynomials, associated Stirling–Eulerian numbers, Worpitzky's identity, gamma-positivity and Hankel determinants of Eulerian polynomials, Bell permutations by weak excedances.

## Worpitzky identity for multiset permutations

Let $m$ and $x$ be natural numbers, let
$k_1, \dots, k_m$ be natural numbers with sum $K = k_1 + \dots + k_m$, and for $p \ge 1$ let
$a_p$ be the number of words $w_1 w_2 \cdots w_K$ over the alphabet $\{1, \dots, m\}$ in which
each letter $i$ occurs exactly $k_i$ times and which have exactly $p - 1$ descents, that is,
indices $j$ with $1 \le j < K$ and $w_j > w_{j+1}$. Then

$$\prod_{i=1}^{m} \binom{x + k_i - 1}{k_i} = \sum_{p=1}^{\max(1, K)} \binom{x + K - p}{K} a_p.$$

Here subtraction of natural numbers is truncated at $0$.

## Sources

- A. Dzhumadil'daev and D. Yeliussizov, *Power Sums of Binomial Coefficients*, Journal of Integer Sequences 16 (2013), Article 13.1.4, Theorem Worpitzky, lines 212-217, <https://cs.uwaterloo.ca/journals/JIS/VOL16/Yeliussizov/dzhuma6.tex>, quoting A. S. Dzhumadil'daev, *Worpitzky identity for multipermutations*, Mat. Zametki 90 (2011), 464-466.

Formalized by `MetaMathlibExt.worpitzky_identity_multiset`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/WorpitzkyMultisetIdentity.lean, line 910](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/WorpitzkyMultisetIdentity.lean#L910). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/index.html#worpitzky-identity-multiset).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Eulerian numbers and polynomials](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers)
