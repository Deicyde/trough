---
declaration: lemma
origin: cited
lean: dist_mem_Icc_of_Ks_ne_zero, enorm_Ks_le, enorm_Ks_sub_Ks_le
statement: formalized
proof: formalized
---

# kernel summand

Let $-S\le s\le S$ and $x,y,y'\in X$. If $K_s(x,y)\neq 0$, then we have

$$
\frac{1}{4} D^{s-1} \leq \rho(x,y) \leq \frac{1}{2} D^s\, .\qquad\text{(65)}
$$

We have

$$
|K_s(x,y)|\le \frac{2^{102 a^3}}{\mu(B(x, D^{s}))}\,\qquad\text{(66)}
$$

and

$$
|K_s(x,y)-K_s(x, y')|\le \frac{2^{127a^3}}{\mu(B(x, D^{s}))}
\left(\frac{ \rho(y,y')}{D^s}\right)^{\frac 1a}\,.\qquad\text{(67)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By Definition [(5)](README.md), the function $K_s$ is the product of $K$ with a function which is supported in the set of all $x,y$ satisfying (65). This proves (65).

Using [(14)](../introduction/README.md) and the lower bound in (65) we obtain

$$
|K_s(x,y)|\le |K(x,y)|\le \frac{2^{a^3}}{\mu(B(x,\frac 14 D^{s-1}))}\qquad\text{(68)}
$$

Using $D=2^{100a^2}$ and the doubling property [(5)](../introduction/README.md) $2 +100a^2$ times estimates the last display by

$$
\le \frac{2^{2a+101a^3}}{\mu(B(x, D^{s}))}\, .\qquad\text{(69)}
$$

Using $a\ge 4$ proves (66).

To prove (67) when $2\rho(y,y') > \rho(x,y)$, use the lower bound in (65) and the inequality $2\rho(y,y') > \frac{1}{4}D^{s-1}$. Then (67) follows from the triangle inequality, (66) and $a \ge 4$.

If $2\rho(y,y') \le \rho(x,y)$, we rewrite $|K_s(x,y)-K_s(x, y')|$ as

$$
|(K(x,y)-K(x,y')) \psi(D^{-s}\rho(x,y)) +
K(x,y)(\psi(D^{-s}\rho(x,y))-\psi(D^{-s}\rho(x,y')))|\,.
$$

An upper bound for $|K(x,y)-K(x, y')|$ is obtained similarly to the proof of (66), using [(15)](../introduction/README.md) and the lower bound in (65)

$$
|K(x,y)-K(x, y')|\le \frac{2^{a^3}}{\mu(B(x, \frac 14 D^{s-1}))}
\left(\frac{ \rho(y,y')}{\frac 14 D^{s-1}}\right)^{\frac 1a}\,.
$$

As above, this is estimated by

$$
\le \frac{4D 2^{2a+101a^3}}{\mu(B(x, D^{s}))}
\left(\frac{ \rho(y,y')}{D^{s}}\right)^{\frac 1a}
= \frac{2^{2+2a+100a^2+101a^3}}{\mu(B(x, D^{s}))}
\left(\frac{ \rho(y,y')}{D^{s}}\right)^{\frac 1a}\,.
$$

We have the trivial bound $|\psi(D^{-s}\rho(x,y))| \leq 1$, and (69) provides a bound for $|K(x,y)|$. Finally, we show that

$$
|\psi(D^{-s}\rho(x,y))-\psi(D^{-s}\rho(x,y'))|\le
4D \left(\frac{\rho(y, y')}{D ^ s}\right)^{\frac 1a}
$$

by considering separately the cases $\rho(y,y')/D^s \ge 1$ and $\rho(y,y')/D^s < 1$. In the former case, the inequality is trivial; in the latter case, it follows from the fact that $\psi$ is Lipschitz with constant $4D$.

Combining the above bounds and using $a\ge 4$ proves (67) when $2\rho(y,y') \le \rho(x,y)$.

## Lean

Formalized as [`dist_mem_Icc_of_Ks_ne_zero`](https://fpvandoorn.github.io/carleson/docs/find/#doc/dist_mem_Icc_of_Ks_ne_zero), [`enorm_Ks_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/enorm_Ks_le), [`enorm_Ks_sub_Ks_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/enorm_Ks_sub_Ks_le).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 872](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L872)
