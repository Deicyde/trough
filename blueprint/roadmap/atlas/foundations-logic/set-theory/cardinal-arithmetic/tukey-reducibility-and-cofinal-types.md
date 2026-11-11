---
declaration: section
origin: cited
lean: MetaMathlibExt.TukeyLE, MetaMathlibExt.TukeyEquiv, MetaMathlibExt.CofinalType
statement: formalized
proof: formalized
---

# Tukey reducibility and cofinal types

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/cardinal-arithmetic/tukey-reducibility-and-cofinal-types/index.html).

## Tukey reducibility

For preordered sets $D$ and $E$, $D$ is Tukey reducible to $E$,
written $D \le_T E$, if there is a map $f \colon D \to E$ that carries unbounded sets to
unbounded sets: for every $A \subseteq D$ with no upper bound in $D$, the image $f[A]$ has no
upper bound in $E$.

Formalized by `MetaMathlibExt.TukeyLE`, a definition declared in [MathlibExt/SetTheory/Dichotomies/CofinalTypes.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Dichotomies/CofinalTypes.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/cardinal-arithmetic/tukey-reducibility-and-cofinal-types/index.html#tukey-le).

## Tukey equivalence

Preordered sets $D$ and $E$ are Tukey equivalent (cofinally
equivalent), written $D \equiv_T E$, if $D \le_T E$ and $E \le_T D$, where $\le_T$ is Tukey
reducibility.

Formalized by `MetaMathlibExt.TukeyEquiv`, a definition declared in [MathlibExt/SetTheory/Dichotomies/CofinalTypes.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Dichotomies/CofinalTypes.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/cardinal-arithmetic/tukey-reducibility-and-cofinal-types/index.html#tukey-equiv).

## Cofinal type

A cofinal type is an equivalence class of preordered sets under Tukey
equivalence $\equiv_T$, where $D \equiv_T E$ means $D \le_T E$ and $E \le_T D$ (Tukey
reducibility in both directions).

Formalized by `MetaMathlibExt.CofinalType`, a definition declared in [MathlibExt/SetTheory/Dichotomies/CofinalTypes.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Dichotomies/CofinalTypes.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/cardinal-arithmetic/tukey-reducibility-and-cofinal-types/index.html#cofinal-type).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tukey reducibility and cofinal types](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/cardinal-arithmetic/tukey-reducibility-and-cofinal-types/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/SetTheory/cardinal-arithmetic/tukey-reducibility-and-cofinal-types)
