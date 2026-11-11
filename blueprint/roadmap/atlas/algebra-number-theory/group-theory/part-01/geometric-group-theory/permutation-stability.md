---
declaration: section
origin: cited
lean: PermutationStability.normalizedHammingDistance, PermutationStability.IsAlmostHomomorphism, PermutationStability.IsCloseToHomomorphisms, PermutationStability.PermutationStable, PermutationStability.flexibleHammingDistance, PermutationStability.IsFlexiblyCloseToHomomorphisms, PermutationStability.FlexiblePermutationStable, PermutationStability.Metabelian
statement: formalized
proof: formalized
---

# Permutation stability

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/permutation-stability/index.html).

## Normalized Hamming distance

For a natural number $n$ and permutations $\sigma$, $\tau$ of
$\{0, \dots, n-1\}$, the normalized Hamming distance $d_n(\sigma, \tau)$ is the number of points
$i < n$ with $\sigma(i) \ne \tau(i)$, divided by $n$, as a real number. For $n = 0$ it is $0$;
this single value does not affect statements about limits as $n \to \infty$.

Formalized by `PermutationStability.normalizedHammingDistance`, a definition declared in [MathlibExt/GroupTheory/PermutationStability.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/PermutationStability.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/permutation-stability/index.html#normalized-hamming-distance).

## Almost-homomorphisms to symmetric groups

Let $G$ be a group and, for each natural number
$n$, let $f_n \colon G \to S_n$ be an arbitrary map, where $S_n$ is the group of permutations of
$\{0, \dots, n-1\}$. The sequence $(f_n)$ is an almost-homomorphism when for all $g, h \in G$ the
normalized Hamming distance $d_n(f_n(g) f_n(h), f_n(gh))$ tends to $0$ as $n \to \infty$.

Following the source, no condition such as $f_n(1) = 1$ is imposed.

Formalized by `PermutationStability.IsAlmostHomomorphism`, a definition declared in [MathlibExt/GroupTheory/PermutationStability.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/PermutationStability.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/permutation-stability/index.html#is-almost-homomorphism).

## Closeness to homomorphisms

Let $G$ be a group and let $f_n \colon G \to S_n$
($n \in \mathbb{N}$) be maps into the symmetric groups $S_n$ of permutations of $\{0, \dots, n-1\}$.
The sequence $(f_n)$ is close to homomorphisms when there are group homomorphisms
$\rho_n \colon G \to S_n$ such that for every $g \in G$ the normalized Hamming distance
$d_n(\rho_n(g), f_n(g))$ tends to $0$ as $n \to \infty$.

Formalized by `PermutationStability.IsCloseToHomomorphisms`, a definition declared in [MathlibExt/GroupTheory/PermutationStability.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/PermutationStability.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/permutation-stability/index.html#is-close-to-homomorphisms).

## Permutation stability

A group $G$ is permutation stable when every
almost-homomorphism $(f_n)$ from $G$ to the symmetric groups $S_n$ is close to
homomorphisms.

Formalized by `PermutationStability.PermutationStable`, a definition declared in [MathlibExt/GroupTheory/PermutationStability.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/PermutationStability.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/permutation-stability/index.html#permutation-stable).

## Flexible Hamming distance

Let $n \le m$ be natural numbers, $\sigma$ a permutation of
$\{0, \dots, n-1\}$ and $\tau$ a permutation of $\{0, \dots, m-1\}$. The flexible Hamming distance
of $\sigma$ and $\tau$ is the real number

$$
d^{\mathrm{flex}}_n(\sigma, \tau) = \frac{\#\{i < n : \sigma(i) \ne \tau(i)\} + (m - n)}{n}.
$$

For $n = 0$ this quotient is taken to be $0$; this single value does not affect statements about
limits as $n \to \infty$.

## Sources

- Kourovka Notebook 21.84. The source is internally inconsistent about the argument order: it first defines the distance with the small permutation first, `d_n^flex(σ, τ)` for `σ ∈ S_n`, `τ ∈ S_m`, but later writes the convergence expression with `ρ_n(g)` first. This formalization follows the definition site (small first), which is also the type-correct order for the embedding `Fin n → Fin m`.

Formalized by `PermutationStability.flexibleHammingDistance`, a definition declared in [MathlibExt/GroupTheory/PermutationStability.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/PermutationStability.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/permutation-stability/index.html#flexible-hamming-distance).

## Flexible closeness to homomorphisms

Let $G$ be a group and let $f_n \colon G \to S_n$
($n \in \mathbb{N}$) be maps into the symmetric groups $S_n$ of permutations of $\{0, \dots, n-1\}$.
The sequence $(f_n)$ is flexibly close to homomorphisms when there are natural numbers $m_n \ge n$
and group homomorphisms $\rho_n \colon G \to S_{m_n}$ such that for every $g \in G$ the flexible
Hamming distance $d^{\mathrm{flex}}_n(f_n(g), \rho_n(g))$ tends to $0$ as $n \to \infty$.

Formalized by `PermutationStability.IsFlexiblyCloseToHomomorphisms`, a definition declared in [MathlibExt/GroupTheory/PermutationStability.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/PermutationStability.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/permutation-stability/index.html#is-flexibly-close-to-homomorphisms).

## Flexible permutation stability

A group $G$ is flexibly permutation stable when every
almost-homomorphism $(f_n)$ from $G$ to the symmetric groups is flexibly close to homomorphisms.

Formalized by `PermutationStability.FlexiblePermutationStable`, a definition declared in [MathlibExt/GroupTheory/PermutationStability.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/PermutationStability.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/permutation-stability/index.html#flexible-permutation-stable).

## Metabelian groups

Let $G$ be a group and let $G' = [G, G]$ be its commutator subgroup.
Then $G$ is metabelian when its second derived subgroup $G'' = [G', G']$ is trivial.

Formalized by `PermutationStability.Metabelian`, a definition declared in [MathlibExt/GroupTheory/PermutationStability.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/PermutationStability.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/permutation-stability/index.html#metabelian).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Permutation stability](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/permutation-stability/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/geometric-group-theory/permutation-stability)
