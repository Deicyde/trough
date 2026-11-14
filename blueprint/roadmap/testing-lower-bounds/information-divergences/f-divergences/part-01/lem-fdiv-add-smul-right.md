---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_smul_add_smul_right
statement: formalized
proof: formalized
---

# fDiv_add_smul_right

For $a, b \ge 0$ with $a + b = 1$, $(\mu, \nu) \mapsto D_f(\mu, a \mu + b \nu)$ is an $f$-divergence for the function $x \mapsto (ax+b)f\left(\frac{x}{ax+b}\right)$ .

## Depends on

- [f-divergence](def-fdiv.md)

## Proof depends on

- [fDiv_symm](lem-fdiv-symm.md)
- [fDiv_add_smul_left](lem-fdiv-add-smul-left.md)

## Proof

We use Lemma [fDiv_symm](lem-fdiv-symm.md), then Lemma [fDiv_add_smul_left](lem-fdiv-add-smul-left.md) and finally Lemma [fDiv_symm](lem-fdiv-symm.md) again:

$$
\begin{aligned}
D_f(\mu, a \mu + b \nu)
&= D_{xf(1/x)}(a \mu + b \nu, \mu)
\\
&= D_{(bx+a)f(1/(bx+a))}(\nu, \mu)
\\
&= D_{(ax+b)f(x/(ax+b))}(\mu, \nu)
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.fDiv_smul_add_smul_right`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_smul_add_smul_right).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 173](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L173)
