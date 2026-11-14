---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.TailoredGame.Extends, MIPRE.Tailored.TailoredGame.Extends.valStar_eq, MIPRE.Tailored.TailoredGame.Extends.hasPerfectZPC, MIPRE.Tailored.TailoredGame.Extends.doubled
statement: formalized
proof: formalized
---

# Extending a tailored game along its questions

Let $\mathfrak{G}'$ and $\mathfrak{G}$ be tailored games on question sets $X'$ and $X$, and $e : X \to X'$ injective, such that $\mathfrak{G}'$ has the weights, the lengths and the constraints of $\mathfrak{G}$ on the image of $e$, and no weight off it. Then $\mathrm{val}^*(\mathfrak{G}') = \mathrm{val}^*(\mathfrak{G})$, a perfect ZPC strategy of $\mathfrak{G}$ gives one of $\mathfrak{G}'$, and the doubled game of $\mathfrak{G}'$ extends that of $\mathfrak{G}$ in the same way, along $\mathrm{id} \times e$.

## Depends on

- [Tailored game; II:1243](../part-01/def-tailored-game.md)
- [Z-aligned permutation strategies commuting along edges; II:1043–1057, II:1279–1283](../part-01/def-zpc-strategy.md)
- [Tensor powers of permutation strategies; II:3043](../part-03/lem-tensor-power-zpc.md)

## Proof

Restricting $\mathfrak{G}'$ to the image of $e$ does not change its value, its distribution being supported there. The answers of length at most the largest length of $\mathfrak{G}$ then sit inside those of $\mathfrak{G}'$, and the canonical decider rejects the longer ones, so the value is $\mathfrak{G}$'s. For a ZPC strategy of $\mathfrak{G}$, pull it back along the inverse of $e$: its observables on the image of $e$, and identities elsewhere, where no question is asked. An edge of positive weight has both ends in the image, with the lengths of their preimages and an edge of $\mathfrak{G}$ between these, on which the two canonical deciders agree; so the pulled-back strategy is a perfect ZPC strategy, by the pull-back of permutation strategies of the repetition phase.

## Lean

Formalized as [`MIPRE.Tailored.TailoredGame.Extends`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.Extends), [`MIPRE.Tailored.TailoredGame.Extends.valStar_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.Extends.valStar_eq), [`MIPRE.Tailored.TailoredGame.Extends.hasPerfectZPC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.Extends.hasPerfectZPC), [`MIPRE.Tailored.TailoredGame.Extends.doubled`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.Extends.doubled).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1000](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1000)
