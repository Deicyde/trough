---
declaration: theorem
origin: cited
lean: MIPRE.Repetition.commutingOperatorValue_repeat_le
statement: formalized
proof: formalized
---

# Direct parallel repetition for commuting-operator strategies

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] There is a universal constant $c > 0$ such that for every game $\mathfrak{G}$ with nonempty alphabets and every integer $n \geq 1$, writing $\varepsilon = 1 - {\omega^{\mathrm{co}}}(\mathfrak{G})$,

$$
{\omega^{\mathrm{co}}}\bigl( \mathfrak{G}^{n} \bigr) \;\leq\;
\exp\Bigl( - \frac{c\, \varepsilon^{7}\, n}{\varepsilon + \log\bigl(\left\vert {{\mathcal{A}}} \right\vert\,\left\vert {{\mathcal{B}}} \right\vert\bigr)} \Bigr)\;.
$$

## Depends on

- [Direct repetition](def-direct-repetition.md)
- [Commuting-operator value](def-co-value-bipartite.md)

## Proof

This is the main theorem of (Vid26) (Theorem 7.1 there), whose Lean proof is vendored at `MIPRE/Background/Repetition/CommutingRepetition/`. The bridge identifies a game of Definition [Nonlocal game](../foundations/part-01/def-game.md) with the game of the vendored development having the $\{0, 1\}$-valued payoff $D$, a commuting-operator strategy of Definition [Commuting-operator strategy](def-co-strategy-bipartite.md) with a strategy of the vendored development (field by field, so that the two suprema defining the value range over the same set of numbers), and the two direct repetitions with each other. When $\varepsilon = 0$ and $\left\vert {{\mathcal{A}}} \right\vert = \left\vert {{\mathcal{B}}} \right\vert = 1$ the formalization reads the quotient as $0$ and the bound is trivial.

## Lean

Formalized as [`MIPRE.Repetition.commutingOperatorValue_repeat_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.commutingOperatorValue_repeat_le).

## Sources

- [MIP* = RE blueprint: content/05_parallel_repetition.tex, line 147](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/05_parallel_repetition.tex#L147)
