---
declaration: definition
origin: cited
lean: Groups.tSdhCondition, Groups.tSdhExperiment, Groups.tSdhAssumption
statement: formalized
---

# $t$-SDH

A $t$-SDH adversary receives the reference string for $t=n$ and a uniform nonzero $\tau$, and outputs $(c,h)\in\mathbb{Z}_p\times G_1$. It wins when $\tau+c\neq 0$ and $h=g_1^{1/(\tau+c)}$. For a set $\mathcal{A}$ of adversaries and $\varepsilon\geq 0$, the $t$-SDH assumption over $\mathcal{A}$ with error $\varepsilon$ states that every adversary in $\mathcal{A}$ wins with probability at most $\varepsilon$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Groups.tSdhCondition`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Groups.tSdhCondition), [`Groups.tSdhExperiment`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Groups.tSdhExperiment), [`Groups.tSdhAssumption`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Groups.tSdhAssumption).

## Sources

- [ArkLib blueprint: commitments/kzg.tex, line 35](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/commitments/kzg.tex#L35)
