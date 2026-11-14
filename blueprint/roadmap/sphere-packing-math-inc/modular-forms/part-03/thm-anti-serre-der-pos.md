---
declaration: theorem
origin: cited
lean: antiSerreDerPos
statement: formalized
proof: formalized
---

# anti-serre-der-pos

Let $F$ be a holomorphic quasimodular cusp form with real Fourier coefficients. Assume that there exists $k$ such that $(\partial_{k}F)(it) > 0$ for all $t > 0$. If the first Fourier coefficient of $F$ is positive, then $F(it) > 0$ for all $t > 0$.

## Depends on

- [serre-der](def-serre-der.md)
- [logder-disc-E2](cor-logder-disc-e2.md)

## Proof

By [(44)](cor-logder-disc-e2.md), we have

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d} t} \left( \frac{F(it)}{\Delta(it)^{\frac{k}{12}}}\right)
&= (-2 \pi) \frac{F'(it) \Delta(it)^{\frac{k}{12}} - F(it) \frac{k}{12} E_{2}(it) \Delta(it)^{\frac{k}{12}}}{\Delta(it)^{\frac{k}{6}}} \\
&= (-2 \pi) \frac{(\partial_{k} F)(it)}{\Delta(it)^{\frac{k}{12}}}  < 0,
\end{aligned}
$$

hence

$$
t \mapsto \frac{F(it)}{\Delta(it)^{\frac{k}{12}}}
$$

is monotone decreasing. Because of the assumption on the positivity of the first nonzero Fourier coefficient of $F$, $F(it) > 0$ for sufficiently large $t$ since

$$
F = \sum_{n \geq n_{0}} a_{n} q^{n} \Rightarrow e^{2 \pi n_{0} t} F(it) = a_{n_{0}} + e^{-2 \pi t}\sum_{n\geq n_{0} + 1} a_{n} e^{-2 \pi (n - n_{0} - 1)t}
$$

and $\lim_{t \to \infty} e^{2 \pi n_{0}t} F(it) = a_{n_0} > 0$, hence the result follows.

## Lean

Formalized as [`antiSerreDerPos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/antiSerreDerPos).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 708](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L708)
