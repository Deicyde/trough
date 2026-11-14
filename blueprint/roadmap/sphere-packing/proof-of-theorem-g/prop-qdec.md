---
declaration: proposition
origin: cited
lean: FmodG_strictAntiOn
statement: formalized
proof: formalized
---

# Qdec

The function $t \mapsto Q(t)$ is strictly decreasing.

## Depends on

- [ramanujan-formula](../modular-forms/part-02/thm-ramanujan-formula.md)
- [serre-der-prod-rule](../modular-forms/part-02/thm-serre-der-prod-rule.md)
- [MLDE-pos](cor-mlde-pos.md)
- [log-der-inf](lemma-log-der-inf.md)

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

The vanishing order of $F$ and $G$ at the infinity are $2$ and $\frac{3}{2}$ respectively, so by Lemma [log-der-inf](lemma-log-der-inf.md), we have

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

Hence $\mathcal{L}_{1, 0}(it) > 0$ by Theorem [anti-serre-der-pos](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L733), and the monotonicity follows.

## Lean

Formalized as [`FmodG_strictAntiOn`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/FmodG_strictAntiOn).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modform-ineq.tex, line 194](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modform-ineq.tex#L194)
