---
declaration: definition
origin: cited
lean: MIPRE.MIPStarComputable
statement: formalized
---

# The computable class

A language $L\subseteq\{0,1\}^*$ is in the *computable class* if there exists a computable map $g$ from bit strings to `HaltingGameValue.GameData` (Definition [Game description](../part-02/def-game-description.md)) such that for every string $z$,

$$
z\in L\ \Longrightarrow\ \mathrm{val}^*(\mathfrak{G}_{g(z)})=1,
\qquad
z\notin L\ \Longrightarrow\ \mathrm{val}^*(\mathfrak{G}_{g(z)})\leq\tfrac12.
$$

The game $\mathfrak{G}_{g(z)}$ is the explicit game `(g z).game`. Computability is the Mathlib `Computable` predicate; there is no polynomial-time bound on $g$ in this definition. This is `MIPRE.MIPStarComputable`, the class used by the checked inclusion in $\mathrm{RE}$ and by the main theorem in its current form (Theorem [$\mathrm{MIP}^* = \mathrm{RE}$](../../the-main-theorem/thm-mipstar-eq-re.md)); in Lean it is the class `MIPRE.MIPClass` of Definition [Value models](../../downstream-results/part-01/def-value-model.md) at the tensor-product value model.

## Depends on

- [Quantum value](../part-01/def-q-value.md)
- [Game description](../part-02/def-game-description.md)
- [Value models](../../downstream-results/part-01/def-value-model.md)

## Lean

Formalized as [`MIPRE.MIPStarComputable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MIPStarComputable).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1635](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1635)
