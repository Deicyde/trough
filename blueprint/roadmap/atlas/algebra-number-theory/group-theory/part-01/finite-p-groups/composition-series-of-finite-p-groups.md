---
declaration: section
origin: cited
lean: IsPGroup.exists_chain_zmod_p_quotients, IsPGroup.isSolvable
statement: formalized
proof: formalized
---

# Composition series of finite p-groups

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/composition-series-of-finite-p-groups/index.html).

## Composition series of finite p-groups

Let $p$ be a prime and let $G$ be a finite
$p$-group of order $p^n$. Then there are subgroups
$G = H_0 \supseteq H_1 \supseteq \cdots \supseteq H_n = \{1\}$ such that for each $i < n$,
$H_{i+1}$ is a normal subgroup of $H_i$ and there is a surjective homomorphism
$H_i \to \mathbb{Z}/p\mathbb{Z}$ with kernel $H_{i+1}$. By the first isomorphism theorem,
$H_i / H_{i+1} \cong \mathbb{Z}/p\mathbb{Z}$ for each $i < n$.

Formalized by `IsPGroup.exists_chain_zmod_p_quotients`, a theorem declared in [MathlibExt/GroupTheory/PGroupChain.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/PGroupChain.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/composition-series-of-finite-p-groups/index.html#exists-chain-zmod-p-quotients).

## Finite p-groups are solvable

For every prime $p$, every finite $p$-group is
solvable.

Formalized by `IsPGroup.isSolvable`, a theorem declared in [MathlibExt/GroupTheory/PGroupChain.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/PGroupChain.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/composition-series-of-finite-p-groups/index.html#is-solvable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Composition series of finite p-groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/composition-series-of-finite-p-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/finite-p-groups/composition-series-of-finite-p-groups)
