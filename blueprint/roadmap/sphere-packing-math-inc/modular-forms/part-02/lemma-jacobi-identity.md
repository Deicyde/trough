---
declaration: lemma
origin: cited
lean: jacobi_identity
statement: formalized
proof: formalized
---

# jacobi-identity

These three theta functions satisfy the *Jacobi identity*

$$
H_{2} + H_{4} = H_{3} \Leftrightarrow \Theta_{2}^4 + \Theta_{4}^4 = \Theta_{3}^4.\qquad\text{(29)}
$$

## Depends on

- [theta-modular](lemma-theta-modular.md)
- [dim-mf](cor-dim-mf.md)

## Proof

Let $f = (H_2 + H_4 - H_3)^{2}$. Obviously, $f$ is a modular form of weight $4$ and level $\Gamma(2)$. However, by using the transformation rules of $H_2, H_3, H_4$, one have

$$
\begin{aligned}
f|_{S} &= (-H_4 - H_2 + H_3)^{2} = f\\
f|_{T} &= (-H_2 + H_3 - H_4)^{2} = f
\end{aligned}
$$

so $f$ is actually a modular form of level $1$. By considering the limit as $z \to i\infty$, $f$ is a cusp form, so we get $f = 0$ from [(13)](cor-dim-mf.md).

## Lean

Formalized as [`jacobi_identity`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/jacobi_identity).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 477](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L477)
