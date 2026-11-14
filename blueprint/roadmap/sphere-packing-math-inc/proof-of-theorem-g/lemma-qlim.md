---
declaration: lemma
origin: cited
lean: FmodG_rightLimitAt_zero
statement: formalized
proof: formalized
---

# Qlim

We have

$$
\lim_{t \to 0^+} Q(t) = \frac{18}{\pi^2}.
$$

## Depends on

- [E2-transform-S](../modular-forms/part-01/lemma-e2-transform-s.md)
- [Ek-is-modular-form](../modular-forms/part-01/lemma-ek-is-modular-form.md)
- [theta-transform-S-T](../modular-forms/part-02/lemma-theta-transform-s-t.md)

## Proof

We have

$$
\lim_{t \to 0^+} Q(t) = \lim_{t \to 0^+} \frac{F(it)}{G(it)} = \lim_{t \to \infty} \frac{F(i/t)}{G(i/t)}.
$$

By using the transformation laws of Eisenstein series [(6)](../modular-forms/part-01/lemma-e2-transform-s.md), [(2)](../modular-forms/part-01/lemma-ek-is-modular-form.md) (for $k = 4, 6$) and the thetanull functions, [(17)](../modular-forms/part-02/lemma-theta-transform-s-t.md), [(19)](../modular-forms/part-02/lemma-theta-transform-s-t.md), we get

$$
\begin{aligned}
F\left(\frac{i}{t}\right) &= t^{12} F(it) - \frac{12t^{11}}{\pi} (E_2(it)E_4(it) - E_6(it))E_4(it) + \frac{36t^{10}}{\pi^2}E_4(it)^2, \\
G\left(\frac{i}{t}\right) &= t^{10} H_{4}(it)^{3}(2H_{4}(it)^{2} + 5 H_{4}(it)H_{2}(it) + 5 H_{2}(it)^{2}).
\end{aligned}
$$

Since $F$, $E_2 E_4 - E_6$ and $H_2$ are cusp forms, we have $\lim_{t \to \infty}t^k A(it) = 0$ when $A(z)$ is one of these forms and $k \geq 0$. From $\lim_{t \to \infty} E_4(it) = 1 = \lim_{t \to \infty}H_{4}(it)$, we get

$$
\begin{aligned}
\lim_{t \to \infty} \frac{F(i/t)}{G(i/t)}
&= \lim_{t \to \infty} \frac{t^{12} F(it) - \frac{12t^{11}}{\pi} (E_2(it)E_4(it) - E_6(it))E_4(it) + \frac{36t^{10}}{\pi^2}E_4(it)^2}{t^{10} H_{4}(it)^{3}(2H_{4}(it)^{2} + 5 H_{4}(it)H_{2}(it) + 5 H_{2}(it)^{2})} \\
&= \lim_{t \to \infty} \frac{t^{2} F(it) - \frac{12t}{\pi} (E_2(it)E_4(it) - E_6(it))E_4(it) + \frac{36}{\pi^2}E_4(it)^2}{H_{4}(it)^{3}(2H_{4}(it)^{2} + 5 H_{4}(it)H_{2}(it) + 5 H_{2}(it)^{2})} \\
&= \frac{18}{\pi^2}.
\end{aligned}
$$

## Lean

Formalized as [`FmodG_rightLimitAt_zero`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/FmodG_rightLimitAt_zero).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modform-ineq.tex, line 161](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modform-ineq.tex#L161)
