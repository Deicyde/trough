---
declaration: section
origin: cited
lean: MathlibExt.GameTheory.ShapleyValue.CoopGame, MathlibExt.GameTheory.ShapleyValue.IsNullPlayer, MathlibExt.GameTheory.ShapleyValue.IsEfficient, MathlibExt.GameTheory.ShapleyValue.IsSymmetric, MathlibExt.GameTheory.ShapleyValue.SatisfiesNullPlayerAxiom
statement: formalized
proof: formalized
---

# Shapley value

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/cooperative-games/shapley-value/index.html).

## Cooperative game with transferable utility

Given a set $N$ of players, a cooperative
game on $N$ is a function $v$ that assigns to every coalition $S \subseteq N$ a real number
$v(S)$, the worth of $S$, such that $v(\emptyset) = 0$.

Formalized by `MathlibExt.GameTheory.ShapleyValue.CoopGame`, a structure declared in [MathlibExt/GameTheory/ShapleyValue.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/ShapleyValue.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/cooperative-games/shapley-value/index.html#coop-game).

## Null player

Let $v$ be a cooperative game on a finite set $N$ of players. A player
$i \in N$ is a null player of $v$ if $v(S \cup \{i\}) = v(S)$ for every coalition
$S \subseteq N$ with $i \notin S$.

Formalized by `MathlibExt.GameTheory.ShapleyValue.IsNullPlayer`, a definition declared in [MathlibExt/GameTheory/ShapleyValue.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/ShapleyValue.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/cooperative-games/shapley-value/index.html#is-null-player).

## Efficient value

Let $N$ be a finite set of players and $\varphi$ an $\mathbb{R}$-linear
map from cooperative games on $N$ (added and scaled pointwise) to payoff vectors in
$\mathbb{R}^N$. Then $\varphi$ is efficient if for every game $v$ the payoffs add up to the worth
of the grand coalition: $\sum_{i \in N} \varphi(v)_i = v(N)$.

Formalized by `MathlibExt.GameTheory.ShapleyValue.IsEfficient`, a definition declared in [MathlibExt/GameTheory/ShapleyValue.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/ShapleyValue.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/cooperative-games/shapley-value/index.html#is-efficient).

## Symmetric value

Let $N$ be a finite set of players and $\varphi$ an $\mathbb{R}$-linear
map from cooperative games on $N$ (added and scaled pointwise) to payoff vectors in
$\mathbb{R}^N$. Then $\varphi$ is symmetric if for every game $v$ and every permutation $\sigma$
of $N$ with $v(\sigma(S)) = v(S)$ for all coalitions $S \subseteq N$, every player $i$ satisfies
$\varphi(v)_{\sigma(i)} = \varphi(v)_i$.

Formalized by `MathlibExt.GameTheory.ShapleyValue.IsSymmetric`, a definition declared in [MathlibExt/GameTheory/ShapleyValue.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/ShapleyValue.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/cooperative-games/shapley-value/index.html#is-symmetric).

## Null player axiom

Let $N$ be a finite set of players and $\varphi$ an $\mathbb{R}$-linear
map from cooperative games on $N$ (added and scaled pointwise) to payoff vectors in
$\mathbb{R}^N$. Then $\varphi$ satisfies the null player axiom if $\varphi(v)_i = 0$ for every
game $v$ and every null player $i$ of $v$.

Formalized by `MathlibExt.GameTheory.ShapleyValue.SatisfiesNullPlayerAxiom`, a definition declared in [MathlibExt/GameTheory/ShapleyValue.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/ShapleyValue.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/cooperative-games/shapley-value/index.html#satisfies-null-player-axiom).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shapley value](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/cooperative-games/shapley-value/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GameTheory/cooperative-games/shapley-value)
