---
declaration: theorem
origin: cited
lean: Derivative.serreDerivative_slash_equivariant
statement: formalized
---

# serre-der-equiv-action

Serre derivative $\partial_{k}$ is equivariant with the slash action of $\mathrm{SL}_{2}(\mathbb{Z})$ in the following sense:

$$
\partial_{k} (F|_{k}\gamma) = (\partial_{k} F)|_{k+2}\gamma, \quad \forall \gamma \in \mathrm{SL}_{2}(\mathbb{Z}).
$$

## Depends on

- [serre-der](def-serre-der.md)
- [E2](../part-01/def-e2.md)
- [E2-transform-general](../part-01/lemma-e2-transform-general.md)

## Proof

Let $G = \partial_{k}F = F' - \frac{k}{12}E_2 F$. From $F \in M_k(\Gamma)$, we have

$$
(F|_{k}\gamma)(z) := (cz + d)^{-k} F\left(\frac{az + b}{cz + d}\right), \quad \gamma = \begin{pmatrix}a & b \\ c & d\end{pmatrix} \in \Gamma.
$$

By taking the derivative of the above equation, we get

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d} z}(F|_{k} \gamma)(z) &= -kc (cz + d)^{-k - 1} F\left(\frac{az + b}{cz + d}\right) + (cz + d)^{-k} (cz + d)^{-2} \frac{\mathrm{d} F}{\mathrm{d} z}\left(\frac{az + b}{cz + d}\right) \\
&= -kc (cz + d)^{-k - 1} F\left(\frac{az + b}{cz + d}\right) + (cz + d)^{-k - 2} \frac{\mathrm{d} F}{\mathrm{d} z}\left(\frac{az + b}{cz + d}\right) \\
&= -kc (cz + d)^{-k - 1} F\left(\frac{az + b}{cz + d}\right) + 2 \pi i (cz + d)^{-k - 2} F'\left(\frac{az + b}{cz + d}\right) \\
\Leftrightarrow (F|_{k} \gamma)'(z) &= -\frac{kc}{2 \pi i} (cz + d)^{-k - 1} F\left(\frac{az + b}{cz + d}\right) + (cz + d)^{-k - 2} F'\left(\frac{az + b}{cz + d}\right).
\end{aligned}
$$

Combined with [(7)](../part-01/lemma-e2-transform-general.md), we get

$$
\begin{aligned}
((\partial_k F)|_{k+2}\gamma)(z) &= (cz + d)^{-k-2} \left(F'\left(\frac{az + b}{cz + d}\right) - \frac{k}{12}E_2\left(\frac{az + b}{cz + d}\right)F\left(\frac{az + b}{cz + d}\right)\right) \\
&= (cz + d)^{-k-2} F'\left(\frac{az + b}{cz + d}\right) - \frac{k}{12} \left(E_2(z) - \frac{6ic}{\pi(cz + d)}\right) \cdot (cz + d)^{-k} F\left(\frac{az + b}{cz + d}\right) \\
&= (F|_{k}\gamma)'(z) - \frac{k}{12} E_2(z) (F|_{k}\gamma)(z) \\
&= \partial_{k} (F|_{k}\gamma)(z).
\end{aligned}
$$

## Lean

Stated as [`Derivative.serreDerivative_slash_equivariant`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Derivative.serreDerivative_slash_equivariant); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 588](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L588)
