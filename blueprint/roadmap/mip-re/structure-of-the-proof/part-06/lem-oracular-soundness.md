---
declaration: lemma
origin: cited
lean: MIPRE.SeededGame.soundStrategy, MIPRE.SeededGame.soundStrategy_value_ge
statement: formalized
proof: formalized
---

# Soundness of oracularization, at the level of games

Let $S$ be a seeded game with nonempty seed space and nonempty answer alphabet, let $0 \leq \varepsilon \leq 1$, and let $N$ be a synchronous strategy for the oracularization of $S$ with value at least $1 - \varepsilon$. Let $\Sigma(N)$ be the strategy for the doubled game of $S$ in which Alice measures $\{N^{(\textsc{A},\, x)}_a\}$ and Bob measures $\{N^{(\textsc{B},\, y)}_b\}$, each relabelled so that the oracle-shaped answers are grouped into one fixed answer. Then $\Sigma(N)$ has value at least $1 - 24\sqrt{\varepsilon}$.

## Depends on

- [The oracularized game](def-oracular-game.md)
- [Synchronous strategy](../../foundations/part-01/def-sync-strategy.md)
- [Synchronous value](../../foundations/part-01/def-sync-value.md)
- [Closeness from two disagreements](../../foundations/part-02/lem-hs-closeness.md)
- [Close measurements have close values](../../foundations/part-02/lem-close-measurements-close-values.md)

## Proof depends on

- [A perfect strategy rejects nothing on the support](../../foundations/part-01/lem-perfect-rejects-nothing.md)

## Proof

Fix a seed $z$ and write $O_{(a,b)}$ for the oracle's measurement at $(\textsc{O}, z)$ relabelled onto answer pairs, and $C_a$, $D_b$ for Alice's and Bob's at $(\textsc{A}, L^\textsc{A}(z))$ and $(\textsc{B}, L^\textsc{B}(z))$; the relabellings group the shape failures into one distinguished outcome, so all three are measurements and not sub-measurements. Each of the nine ordered role pairs carries a ninth of the question weight, so at any one of them a set of outcome pairs the decider rejects carries mass at most $9\varepsilon$ on average over the seed. Applying this at $(\textsc{O}, \textsc{O})$, $(\textsc{O}, \textsc{A})$ and $(\textsc{O}, \textsc{B})$ gives, on average over $z$,

$$
\gamma = \sum_{(a,b) \text{ rejected}} \tau(O_{(a,b)}) \leq 9\varepsilon, \quad
\beta = \sum_{(a,b)} \tau\bigl(O_{(a,b)}(1 - C_a)\bigr) \leq 9\varepsilon, \quad
\alpha = \sum_{(a,b)} \tau\bigl(O_{(a,b)}(1 - D_b)\bigr) \leq 9\varepsilon.
$$

By Lemma [Closeness from two disagreements](../../foundations/part-02/lem-hs-closeness.md), $\sum_{(a,b)} \left\| {C_aD_b - O_{(a,b)}} \right\|_{hs}^2 \leq 3(\alpha + \beta)$ at each seed, so on average at most $54\varepsilon$. By Lemma [Close measurements have close values](../../foundations/part-02/lem-close-measurements-close-values.md) applied at each seed with $\mathrm{acc}$ the accepted pairs, the value of $\Sigma(N)$ at that seed is at least $1 - \gamma$ minus twice the square root of that closeness; averaging and using Cauchy–Schwarz once more to take the average inside the square root gives $\mathrm{val}^* \geq 1 - 9\varepsilon - 2\sqrt{54\varepsilon} \geq 1 - 24\sqrt{\varepsilon}$, the last step because $\varepsilon \leq \sqrt\varepsilon$ for $\varepsilon \leq 1$ and $2\sqrt{54} < 15$.

## Lean

Formalized as [`MIPRE.SeededGame.soundStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.soundStrategy), [`MIPRE.SeededGame.soundStrategy_value_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.soundStrategy_value_ge).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4258](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4258)
