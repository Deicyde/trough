---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.GroupClassesShared.IsGeneralizedQuaternion
statement: formalized
proof: formalized
---

# Finite p-groups: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/index.html).

Groups of prime-power order: composition series, Frattini subgroups and Φ-extensions, special, powerful, metacyclic and Camina p-groups, conjugacy class sizes of p-groups, generalized quaternion groups, coclass and rank analogues, derived length bounds, and orders of automorphism groups of p-groups only when the p-group structure is the point.

## Generalized quaternion group

A group $P$ is a generalized quaternion group if, for some
natural number $k \ge 1$, it is isomorphic to the quaternion group
$Q_{2^{k+2}} = \langle a, x \mid a^{2^{k+1}} = 1,\ x^2 = a^{2^k},\ x^{-1} a x = a^{-1} \rangle$
of order $2^{k+2}$. Thus $P$ has order $8$, $16$, $32$ or some larger power of $2$.

Formalized by `MathlibExt.GroupTheory.GroupClassesShared.IsGeneralizedQuaternion`, a definition declared in [WantedExt/GroupTheory/GroupClassesShared.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/GroupClassesShared.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/index.html#is-generalized-quaternion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite p-groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/finite-p-groups)
