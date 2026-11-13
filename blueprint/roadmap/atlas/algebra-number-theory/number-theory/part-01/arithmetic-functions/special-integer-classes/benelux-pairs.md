---
declaration: section
origin: cited
lean: MetaMathlibExt.benelux_pair_first_kind_iff, MetaMathlibExt.benelux_pair_second_kind_iff
statement: formalized
---

# Benelux pairs

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/benelux-pairs/index.html).

## Benelux pairs of the first kind below $1.4 \cdot 10^{12}$

Let $m < n$ be
non-negative integers with $n < 1.4 \cdot 10^{12}$. Then $m$ and $n$ have the same prime
factors and $m + 1$ and $n + 1$ have the same prime factors (that is, $(m, n)$ is a Benelux
pair of the first kind) if and only if $(m, n) = (75, 1215)$ or
$(m, n) = (2^k - 2, 2^{2k} - 2^{k+1})$ for some integer $k$ with $2 \le k \le 20$.

Here $0$ is taken to have no prime factors; for $m = 0$ both sides are false.

## Sources

- Christian Hercher, *On One of Erdős' Problems—An Efficient Search for Benelux Pairs*, Journal of Integer Sequences 28 (2025), Article 25.8.5, Theorem 1 a) (`jis-2025-25.8.5-thm-1`).

Stated but not proved: `MetaMathlibExt.benelux_pair_first_kind_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeneluxPairsWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BeneluxPairsWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/benelux-pairs/index.html#benelux-pair-first-kind-iff).

## Benelux pairs of the second kind below $1.4 \cdot 10^{12}$

Let $m < n$ be
non-negative integers with $n < 1.4 \cdot 10^{12}$. Then $m$ and $n + 1$ have the same prime
factors and $m + 1$ and $n$ have the same prime factors (that is, $(m, n)$ is a Benelux pair
of the second kind) if and only if $(m, n) = (35, 4374)$ or
$(m, n) = (2^k + 1, 2^{2k} + 2^{k+1})$ for some integer $k$ with $0 \le k \le 20$.

Here $0$ is taken to have no prime factors; for $m = 0$ both sides are false.

## Sources

- Christian Hercher, *On One of Erdős' Problems—An Efficient Search for Benelux Pairs*, Journal of Integer Sequences 28 (2025), Article 25.8.5, Theorem 1 b) (`jis-2025-25.8.5-thm-1`).

Stated but not proved: `MetaMathlibExt.benelux_pair_second_kind_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/BeneluxPairsWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BeneluxPairsWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/benelux-pairs/index.html#benelux-pair-second-kind-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Benelux pairs](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/benelux-pairs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/benelux-pairs)
