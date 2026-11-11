---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Order.FinitePosets.IsAntichainCoverFin, MathlibExt.Combinatorics.Order.FinitePosets.maxChainSize, MathlibExt.Combinatorics.Order.FinitePosets.minAntichainCoverSize, MathlibExt.Combinatorics.Order.FinitePosets.mirsky_dual_general, MathlibExt.Combinatorics.Order.FinitePosets.mirsky_dual
statement: formalized
proof: formalized
---

# Mirsky's theorem

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/mirsky-s-theorem/index.html).

## Finite antichain covers

Let $\alpha$ be a partially ordered set. A finite family $C$ of
finite subsets of $\alpha$ is a finite antichain cover of $\alpha$ when every member of $C$ is an
antichain and every element of $\alpha$ belongs to some member of $C$.

Formalized by `MathlibExt.Combinatorics.Order.FinitePosets.IsAntichainCoverFin`, a definition declared in [MathlibExt/Combinatorics/Order/FinitePosets.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Order/FinitePosets.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/mirsky-s-theorem/index.html#is-antichain-cover-fin).

## Maximum chain size

For a finite partially ordered set $\alpha$, the maximum chain size of
$\alpha$ is the largest cardinality of a chain in $\alpha$, that is, of a set of pairwise
comparable elements.

Formalized by `MathlibExt.Combinatorics.Order.FinitePosets.maxChainSize`, a definition declared in [MathlibExt/Combinatorics/Order/FinitePosets.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Order/FinitePosets.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/mirsky-s-theorem/index.html#max-chain-size).

## Minimum antichain cover size

For a finite partially ordered set $\alpha$, the minimum
antichain cover size of $\alpha$ is the smallest number of antichains in $\alpha$ whose union is
all of $\alpha$.

Formalized by `MathlibExt.Combinatorics.Order.FinitePosets.minAntichainCoverSize`, a definition declared in [MathlibExt/Combinatorics/Order/FinitePosets.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Order/FinitePosets.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/mirsky-s-theorem/index.html#min-antichain-cover-size).

## Dual of Dilworth's theorem

For every finite partially ordered set $\alpha$, the maximum
chain size of $\alpha$ equals its minimum antichain cover size: the largest cardinality of a chain
in $\alpha$ equals the smallest number of antichains whose union is $\alpha$.

Formalized by `MathlibExt.Combinatorics.Order.FinitePosets.mirsky_dual_general`, a theorem declared in [MathlibExt/Combinatorics/Order/FinitePosets.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Order/FinitePosets.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/mirsky-s-theorem/index.html#mirsky-dual-general).

## Mirsky's theorem

For every finite partially ordered set $\alpha$, the maximum chain size of
$\alpha$ equals its minimum antichain cover size: the largest cardinality of a chain in $\alpha$
equals the smallest number of antichains whose union is $\alpha$.

## Sources

- L. Mirsky, Amer. Math. Monthly 78 (1971), 876-877, DOI 10.2307/2316481. It follows from `mirsky_dual_general`; the instance `[DecidableEq α]` is unused and keeps the Wanted entry's shape.

Formalized by `MathlibExt.Combinatorics.Order.FinitePosets.mirsky_dual`, a theorem declared in [MathlibExt/Combinatorics/Order/FinitePosets.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Order/FinitePosets.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/mirsky-s-theorem/index.html#mirsky-dual).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mirsky's theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/mirsky-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/partially-ordered-sets/mirsky-s-theorem)
