---
declaration: section
origin: cited
lean: MathlibExt.GameTheory.BondarevaShapleyWanted.IsCoreAllocation, MathlibExt.GameTheory.BondarevaShapleyWanted.IsBalanced, MathlibExt.GameTheory.BondarevaShapleyWanted.bondareva_shapley
statement: formalized
proof: formalized
---

# Bondareva–Shapley theorem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/cooperative-games/bondareva-shapley-theorem/index.html).

## Core allocation

A payoff vector $x \colon N \to \mathbb{R}$ is a core allocation of a
cooperative game $v$ on a finite set $N$ of players if it is efficient,
$\sum_{i \in N} x_i = v(N)$, and coalitionally rational, $v(S) \le \sum_{i \in S} x_i$ for every
coalition $S \subseteq N$.

Formalized by `MathlibExt.GameTheory.BondarevaShapleyWanted.IsCoreAllocation`, a definition declared in [MathlibExt/GameTheory/BondarevaShapley.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/BondarevaShapley.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/cooperative-games/bondareva-shapley-theorem/index.html#is-core-allocation).

## Balanced cooperative game

A cooperative game $v$ on a finite set $N$ of players is
balanced if for every family of real weights $(\lambda_S)_{S \subseteq N}$ with $\lambda_S \ge 0$
for every coalition $S \subseteq N$ and $\sum_{S \subseteq N,\, i \in S} \lambda_S = 1$ for every
player $i \in N$, one has $\sum_{S \subseteq N} \lambda_S \, v(S) \le v(N)$.

Formalized by `MathlibExt.GameTheory.BondarevaShapleyWanted.IsBalanced`, a definition declared in [MathlibExt/GameTheory/BondarevaShapley.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/BondarevaShapley.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/cooperative-games/bondareva-shapley-theorem/index.html#is-balanced).

## Bondareva–Shapley theorem

Let $v$ be a cooperative game with transferable utility on a
finite set $N$ of players. Then $v$ has a core allocation $x \colon N \to \mathbb{R}$, that is,
the core of $v$ is nonempty, if and only if $v$ is balanced.

## Sources

- O. N. Bondareva, Probl. Kibernet. 10 (1963), 119-139; L. S. Shapley, Naval Res. Log. Quart. 14 (1967), 453-460, DOI 10.1002/nav.3800140404.

Formalized by `MathlibExt.GameTheory.BondarevaShapleyWanted.bondareva_shapley`, a theorem declared in [MathlibExt/GameTheory/BondarevaShapley.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/BondarevaShapley.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/cooperative-games/bondareva-shapley-theorem/index.html#bondareva-shapley).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bondareva–Shapley theorem](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/cooperative-games/bondareva-shapley-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GameTheory/cooperative-games/bondareva-shapley-theorem)
