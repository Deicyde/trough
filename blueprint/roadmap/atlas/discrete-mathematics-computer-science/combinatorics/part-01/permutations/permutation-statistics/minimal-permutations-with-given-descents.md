---
declaration: section
origin: cited
lean: MetaMathlibExt.descent_minimal_iff, MetaMathlibExt.minimal_permutations_card
statement: formalized
proof: formalized
---

# Minimal permutations with given descents

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/minimal-permutations-with-given-descents/index.html).

## Characterization of minimal permutations with a given number of descents

Let $\sigma$ be a
permutation of $\{1, \dots, n\}$ and let $d$ be a natural number. A descent of a permutation
$\tau$ of $\{1, \dots, k\}$ is an index $1 \le i \le k - 1$ with $\tau(i+1) < \tau(i)$, and $\tau$
occurs in $\sigma$ if there are positions $\varphi(1) < \dots < \varphi(k)$ in $\{1, \dots, n\}$
with $\tau(a) < \tau(b)$ exactly when $\sigma(\varphi(a)) < \sigma(\varphi(b))$. Then $\sigma$ has
exactly $d$ descents and no permutation $\tau$ of $\{1, \dots, k\}$ with $0 < k < n$ occurring in
$\sigma$ has exactly $d$ descents if and only if $\sigma$ has exactly $d$ descents and every
ascent $i$ of $\sigma$ (an index $1 \le i \le n - 1$ with $\sigma(i) < \sigma(i+1)$) satisfies
$2 \le i \le n - 2$ and either $\sigma(i) < \sigma(i-1) < \sigma(i+2) < \sigma(i+1)$ or
$\sigma(i) < \sigma(i+2) < \sigma(i-1) < \sigma(i+1)$; that is, the entries at positions
$i-1, i, i+1, i+2$ form the pattern $2143$ or $3142$.

## Sources

- Stefano Bilotta, Elisabetta Grazzini, and Elisa Pergola, "Enumeration of Two Particular Sets of Minimal Permutations", Journal of Integer Sequences 18 (2015), Article 15.10.2, Theorem `thm:characterization`, lines 230-237, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Grazzini/graz3.tex>.

Formalized by `MetaMathlibExt.descent_minimal_iff`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MinimalDescentPermutations.lean, line 573](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MinimalDescentPermutations.lean#L573). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/minimal-permutations-with-given-descents/index.html#descent-minimal-iff).

## Minimal permutations of length two more than their number of descents

For every natural
number $d$, the number of permutations $\sigma$ of $\{0, 1, \dots, d + 1\}$ such that $\sigma$ has
exactly $d$ descents (positions $0 \le i \le d$ with $\sigma(i) > \sigma(i + 1)$) and, for every
position $j$, deleting the entry at position $j$ leaves a sequence of $d + 1$ entries with fewer
than $d$ descents, equals $2^{d+2} - (d + 1)(d + 2) - 2$.

## Sources

- Stefano Bilotta, Elisabetta Grazzini, and Elisa Pergola, "Enumeration of Two Particular Sets of Minimal Permutations", Journal of Integer Sequences 18 (2015), Article 15.10.2, Theorem `thm:enum`, lines 324-326, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Grazzini/graz3.tex>.

Formalized by `MetaMathlibExt.minimal_permutations_card`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MinimalPermutationsEnumeration.lean, line 2235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MinimalPermutationsEnumeration.lean#L2235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/minimal-permutations-with-given-descents/index.html#minimal-permutations-card).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minimal permutations with given descents](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/minimal-permutations-with-given-descents/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/permutations/permutation-statistics/minimal-permutations-with-given-descents)
