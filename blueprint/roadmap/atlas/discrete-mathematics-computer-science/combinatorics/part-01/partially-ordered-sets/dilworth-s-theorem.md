---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Order.DilworthWanted.IsChainCoverFin, MathlibExt.Combinatorics.Order.DilworthWanted.maxAntichainSize, MathlibExt.Combinatorics.Order.DilworthWanted.minChainCoverSize, MathlibExt.Combinatorics.Order.DilworthWanted.card_le_maxAntichainSize, MathlibExt.Combinatorics.Order.DilworthWanted.minChainCoverSize_le_card, MathlibExt.Combinatorics.Order.DilworthWanted.dilworth_decomposition, MathlibExt.Combinatorics.Order.DilworthWanted.exists_isAntichain_card_eq_maxAntichainSize, MathlibExt.Combinatorics.Order.DilworthWanted.exists_isChainCoverFin_card_eq_minChainCoverSize
statement: formalized
proof: formalized
---

# Dilworth's theorem

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/dilworth-s-theorem/index.html).

## Chain cover

Let $\alpha$ be a partially ordered set. A finite set $C$ of finite subsets of
$\alpha$ is a chain cover of $\alpha$ when every member of $C$ is a chain and every element of
$\alpha$ lies in some member of $C$.

Formalized by `MathlibExt.Combinatorics.Order.DilworthWanted.IsChainCoverFin`, a definition declared in [MathlibExt/Combinatorics/Order/Dilworth.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Order/Dilworth.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/dilworth-s-theorem/index.html#is-chain-cover-fin).

## Maximum antichain size

For a finite partially ordered set $\alpha$, the maximum antichain
size of $\alpha$ (its width) is the largest number of elements of an antichain in $\alpha$.

Formalized by `MathlibExt.Combinatorics.Order.DilworthWanted.maxAntichainSize`, a definition declared in [MathlibExt/Combinatorics/Order/Dilworth.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Order/Dilworth.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/dilworth-s-theorem/index.html#max-antichain-size).

## Minimum chain cover size

For a finite partially ordered set $\alpha$, the minimum chain
cover size of $\alpha$ is the smallest number of chains in a chain cover of $\alpha$, that is, in
a finite set of chains of $\alpha$ whose union is $\alpha$.

Formalized by `MathlibExt.Combinatorics.Order.DilworthWanted.minChainCoverSize`, a definition declared in [MathlibExt/Combinatorics/Order/Dilworth.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Order/Dilworth.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/dilworth-s-theorem/index.html#min-chain-cover-size).

## Antichains are no larger than the maximum antichain size

Let $\alpha$ be a finite
partially ordered set. Every antichain $A$ in $\alpha$ has at most as many elements as the
maximum antichain size of $\alpha$.

Formalized by `MathlibExt.Combinatorics.Order.DilworthWanted.card_le_maxAntichainSize`, a theorem declared in [MathlibExt/Combinatorics/Order/Dilworth.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Order/Dilworth.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/dilworth-s-theorem/index.html#card-le-max-antichain-size).

## Chain covers bound the minimum chain cover size

Let $\alpha$ be a finite partially
ordered set. If $C$ is a chain cover of $\alpha$, that is, a finite set of chains of $\alpha$ whose
union is $\alpha$, then the minimum chain cover size of $\alpha$ is at most the number of chains
in $C$.

Formalized by `MathlibExt.Combinatorics.Order.DilworthWanted.minChainCoverSize_le_card`, a theorem declared in [MathlibExt/Combinatorics/Order/Dilworth.lean, line 836](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Order/Dilworth.lean#L836). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/dilworth-s-theorem/index.html#min-chain-cover-size-le-card).

## Dilworth's theorem

Let $\alpha$ be a finite partially ordered set. The maximum antichain
size of $\alpha$ equals its minimum chain cover size: the largest number of elements of an
antichain in $\alpha$ equals the smallest number of chains whose union is $\alpha$.

## Sources

- R. P. Dilworth, A decomposition theorem for partially ordered sets, Annals of Mathematics 51 (1950), 161-166, DOI 10.2307/1969503.

Formalized by `MathlibExt.Combinatorics.Order.DilworthWanted.dilworth_decomposition`, a theorem declared in [MathlibExt/Combinatorics/Order/Dilworth.lean, line 880](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Order/Dilworth.lean#L880). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/dilworth-s-theorem/index.html#dilworth-decomposition).

## The maximum antichain size is attained

Let $\alpha$ be a finite partially ordered set.
Some antichain in $\alpha$ has exactly as many elements as the maximum antichain size of
$\alpha$.

Formalized by `MathlibExt.Combinatorics.Order.DilworthWanted.exists_isAntichain_card_eq_maxAntichainSize`, a theorem declared in [MathlibExt/Combinatorics/Order/Dilworth.lean, line 930](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Order/Dilworth.lean#L930). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/dilworth-s-theorem/index.html#exists-is-antichain-card-eq-max-antichai).

## The minimum chain cover size is attained

Let $\alpha$ be a finite partially ordered set.
Some chain cover $C$ of $\alpha$, a finite set of chains of $\alpha$ whose union is $\alpha$,
consists of exactly as many chains as the minimum chain cover size of $\alpha$.

Formalized by `MathlibExt.Combinatorics.Order.DilworthWanted.exists_isChainCoverFin_card_eq_minChainCoverSize`, a theorem declared in [MathlibExt/Combinatorics/Order/Dilworth.lean, line 937](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Order/Dilworth.lean#L937). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/dilworth-s-theorem/index.html#exists-is-chain-cover-fin-card-eq-min-ch).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dilworth's theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/dilworth-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/partially-ordered-sets/dilworth-s-theorem)
