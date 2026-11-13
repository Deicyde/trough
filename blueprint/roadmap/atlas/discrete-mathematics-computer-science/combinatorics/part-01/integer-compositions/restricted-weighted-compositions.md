---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Enumerative.sRestrictedWeightedCompositionCount, MathlibExt.Combinatorics.Enumerative.vandermondeTypeConvolutionForSRestrictedWeightedCompositions
statement: formalized
proof: formalized
---

# Restricted weighted compositions

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-weighted-compositions/index.html).

## Restricted weighted composition count

Let $R$ be a commutative ring, $S$ a finite set
of natural numbers and $f \colon \mathbb{N} \to R$ a weight function. For natural numbers $n$
and $k$, $d_{S,f}(n, k)$ is the sum, over all $k$-tuples $(\pi_1, \dots, \pi_k)$ of natural
numbers with every $\pi_i \in S$ and $\pi_1 + \dots + \pi_k = n$, of the weight
$f(\pi_1) \cdots f(\pi_k)$.

Since every part of a composition of $n$ is at most $n$, the tuples range over the finite set
of maps from $\{0, \dots, k-1\}$ to $\{0, \dots, n\}$.

Formalized by `MathlibExt.Combinatorics.Enumerative.sRestrictedWeightedCompositionCount`, a definition declared in [MathlibExt/Combinatorics/Enumerative/VandermondeTypeConvolutionForSRestrictedWeightedCompositions.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/VandermondeTypeConvolutionForSRestrictedWeightedCompositions.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-weighted-compositions/index.html#s-restricted-weighted-composition-count).

## Vandermonde convolution for restricted weighted compositions

Let $R$ be a commutative
ring, $S$ a finite set of natural numbers and $f \colon \mathbb{N} \to R$ a weight function, and
write $d_{S,f}(n, k)$ for the weighted count of $S$-restricted $f$-weighted compositions of $n$
with $k$ parts. Then for all natural numbers $n$, $k$ and $j$ with $j \le k$,

$$d_{S,f}(n, k) = \sum_{m=0}^{n} d_{S,f}(m, j) \, d_{S,f}(n - m, k - j).$$

Formalized by `MathlibExt.Combinatorics.Enumerative.vandermondeTypeConvolutionForSRestrictedWeightedCompositions`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/VandermondeTypeConvolutionForSRestrictedWeightedCompositions.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/VandermondeTypeConvolutionForSRestrictedWeightedCompositions.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-weighted-compositions/index.html#vandermonde-type-convolution-for-srestri).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Restricted weighted compositions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-weighted-compositions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/integer-compositions/restricted-weighted-compositions)
