---
navigation: transparent
---

# NumberField.InfinitePlace.Comple… to NumberField.AdeleRing.baseChange…

- [NumberField.InfinitePlace.Completion.baseChangeEquiv](numberfield-infiniteplace-completion-basechangee.md)
- [NumberField.InfinitePlace.Completion.piEquiv](numberfield-infiniteplace-completion-piequiv.md)

### Base change for the infinite adele ring

First, we induce a $K_{\infty}$-algebra on $L_{\infty}$ from the action of each $K_v$ on $\prod_{w\mid v}L_w$. Specifically, this means that for $x \in K_{\infty}$ and $y \in L_{\infty}$, we have $(x \cdot y)_w = x_{v_w} \cdot y_w$, where $v_w$ is the restriction of $w$ to $K$. We show that $L_{\infty}$ has the $K_{\infty}$-module topology.

- [NumberField.InfiniteAdeleRing.piEquiv](numberfield-infiniteadelering-piequiv.md)
- [NumberField.InfiniteAdeleRing.instIsModuleTopology\_fLT](numberfield-infiniteadelering-instismoduletopolo.md)
- [NumberField.InfiniteAdeleRing.baseChangeAlgEquiv](numberfield-infiniteadelering-basechangealgequiv.md)

It remains to show that the map in [NumberField.InfiniteAdeleRing.baseChangeAlgEquiv](numberfield-infiniteadelering-basechangealgequiv.md) is a homeomorphism. Since both sides have the $K_{\infty}$-module topology, and since the $L$-algebra isomorphism of [NumberField.InfiniteAdeleRing.baseChangeAlgEquiv](numberfield-infiniteadelering-basechangealgequiv.md) can equivalently be viewed as a $K_{\infty}$-linear isomorphism, it is also a homeomorphism.

- [NumberField.InfiniteAdeleRing.baseChangeEquiv](numberfield-infiniteadelering-basechangeequiv.md)

## Base change for adeles

From the previous results we deduce immediately that if $L/K$ is a finite extension of number fields then there's a natural (topological and algebraic) isomorphism $L\otimes_K\mathbb{A}_K\to \mathbb{A}_L$.

- [NumberField.AdeleRing.baseChangeEquiv](numberfield-adelering-basechangeequiv.md)

Something else we shall need:

- [NumberField.AdeleRing.baseChange\_moduleTopology](numberfield-adelering-basechange-moduletopology.md)
