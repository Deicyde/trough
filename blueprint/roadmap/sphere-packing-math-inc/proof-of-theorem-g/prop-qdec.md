---
declaration: proposition
origin: cited
lean: FmodG_antitone
statement: formalized
proof: formalized
---

# Qdec

The function $t \mapsto Q(t)$ is monotone decreasing.

## Depends on

- [ramanujan-formula](../modular-forms/part-03/thm-ramanujan-formula.md)
- [serre-der-prod-rule](../modular-forms/part-03/thm-serre-der-prod-rule.md)
- [MLDE-pos](cor-mlde-pos.md)
- [anti-serre-der-pos](../modular-forms/part-03/thm-anti-serre-der-pos.md)

## Proof

It is enough to show that

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d} t} \left(\frac{F(it)}{G(it)}\right) < 0 &\Leftrightarrow (- 2\pi) \frac{F'(it)G(it) - F(it) G'(it)}{G(it)^{2}} < 0 \\
&\Leftrightarrow F'(it) G(it) - F(it) G'(it) > 0 \\
&\Leftrightarrow (\partial_{10}F)(it) G(it) - F(it) (\partial_{10}G)(it) > 0.
\end{aligned}
$$

Let $\mathcal{L}_{1, 0} := (\partial_{10}F) G - F (\partial_{10} G) = F'G - FG'$. Then

$$
\begin{aligned}
\frac{\mathcal{L}_{1, 0}}{FG} = \frac{F'G - FG'}{FG} = \frac{F'}{F} - \frac{G'}{G}
\end{aligned}
$$

The vanishing order of $F$ and $G$ at the infinity are $2$ and $\frac{3}{2}$ respectively, so we have

$$
\begin{aligned}
\lim_{t \to \infty} \frac{\mathcal{L}_{1, 0}(it)}{F(it) G(it)} = \lim_{t \to \infty} \left(\frac{F'(it)}{F(it)} - \frac{G'(it)}{G(it)}\right) = 2 - \frac{3}{2} = \frac{1}{2} > 0
\end{aligned}
$$

so $\mathcal{L}_{1, 0}(it) > 0$ for sufficiently large $t$. Its Serre derivative $\partial_{22} \mathcal{L}_{1, 0}$ is positive by Corollary [MLDE-pos](cor-mlde-pos.md):

$$
\begin{aligned}
\partial_{22} \mathcal{L}_{1, 0} = (\partial_{12} \partial_{10} F) G - F (\partial_{12}\partial_{10} G)
= \Delta (7200 (-E_{2}') G + 640 H_2 F) > 0.
\end{aligned}
$$

Hence $\mathcal{L}_{1, 0}(it) > 0$ by Theorem [anti-serre-der-pos](../modular-forms/part-03/thm-anti-serre-der-pos.md), and the monotonicity follows.

## Lean

Formalized as [`FmodG_antitone`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/FmodG_antitone).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modform-ineq.tex, line 187](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modform-ineq.tex#L187)
