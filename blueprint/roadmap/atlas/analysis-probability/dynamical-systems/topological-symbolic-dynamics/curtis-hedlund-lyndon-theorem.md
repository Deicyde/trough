---
declaration: section
origin: cited
lean: MetaMathlibExt.curtis_hedlund_lyndon_general, MetaMathlibExt.curtis_hedlund_lyndon
statement: formalized
proof: formalized
---

# Curtis–Hedlund–Lyndon theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/curtis-hedlund-lyndon-theorem/index.html).

## Curtis–Hedlund–Lyndon theorem with an arbitrary discrete output alphabet

Let $A$ be a
finite set and $B$ any set, both with the discrete topology, and give $A^{\mathbb{Z}}$ and
$B^{\mathbb{Z}}$ the product topology. For $k \in \mathbb{Z}$ let $\sigma^k$ be the shift on
either space given by $(\sigma^k x)_n = x_{n+k}$ for all $n \in \mathbb{Z}$. A map
$F : A^{\mathbb{Z}} \to B^{\mathbb{Z}}$ is a sliding block code, that is, there are a radius
$r \in \mathbb{N}$ and a local rule $\varphi : A^{2r+1} \to B$ with
$F(x)_n = \varphi(x_{n-r}, \dots, x_{n+r})$ for all $x \in A^{\mathbb{Z}}$ and $n \in \mathbb{Z}$,
if and only if $F$ is continuous and commutes with every shift: $F(\sigma^k x) = \sigma^k F(x)$
for all $x \in A^{\mathbb{Z}}$ and $k \in \mathbb{Z}$.

Formalized by `MetaMathlibExt.curtis_hedlund_lyndon_general`, a theorem declared in [MathlibExt/Dynamics/CurtisHedlundLyndon.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/CurtisHedlundLyndon.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/curtis-hedlund-lyndon-theorem/index.html#curtis-hedlund-lyndon-general).

## Curtis–Hedlund–Lyndon theorem

Let $A$ and $B$ be finite sets with the discrete
topology, and give $A^{\mathbb{Z}}$ and $B^{\mathbb{Z}}$ the product topology. For
$k \in \mathbb{Z}$ let $\sigma^k$ be the shift on either space given by
$(\sigma^k x)_n = x_{n+k}$ for all $n \in \mathbb{Z}$. A map
$F : A^{\mathbb{Z}} \to B^{\mathbb{Z}}$ is a sliding block code, that is, there are a radius
$r \in \mathbb{N}$ and a local rule $\varphi : A^{2r+1} \to B$ with
$F(x)_n = \varphi(x_{n-r}, \dots, x_{n+r})$ for all $x \in A^{\mathbb{Z}}$ and $n \in \mathbb{Z}$,
if and only if $F$ is continuous and commutes with every shift: $F(\sigma^k x) = \sigma^k F(x)$
for all $x \in A^{\mathbb{Z}}$ and $k \in \mathbb{Z}$.

## Sources

- https://en.wikipedia.org/wiki/Curtis%E2%80%93Hedlund%E2%80%93Lyndon_theorem (statement id `curtis-hedlund-s1`).

Formalized by `MetaMathlibExt.curtis_hedlund_lyndon`, a theorem declared in [MathlibExt/Dynamics/CurtisHedlundLyndon.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/CurtisHedlundLyndon.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/curtis-hedlund-lyndon-theorem/index.html#curtis-hedlund-lyndon).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Curtis–Hedlund–Lyndon theorem](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/curtis-hedlund-lyndon-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/topological-symbolic-dynamics/curtis-hedlund-lyndon-theorem)
