---
declaration: lemma
origin: cited
lean: nontangential_operator_boundary
statement: formalized
proof: formalized
---

# nontangential operator boundary

Let $f:X\to{\mathbb{C}}$ be a bounded measurable function supported on a set of finite measure. For all $x\in X$,

$$
T_*f(x) = \sup_{R_1 < R_2} \sup_{x'\in B(x,R_1)} \left|\int_{B(x',R_2)\setminus B(x',R_1)} K(x',y) f(y) \, \mathrm{d}\mu(y) \right|\qquad\text{(35)}
$$

## Depends on

- [small annulus](small-annulus.md)

## Proof

We show two inequalities. Let $\epsilon>0$. Let $R_1\lt R_2$ and $x'\in B(x,R_1)$. Then for small enough $\delta>0$,

$$
\begin{alignedat}{3}
&&&\left|\int_{R_1\lt \rho(x',y)\lt R_2} K(x',y) f(y) \, \mathrm{d}\mu(y) \right|\qquad\text{(36)}\\
\le &&&\left|\int_{R_1\lt \rho(x',y)\lt R_1+\delta} K(x',y) f(y) \, \mathrm{d}\mu(y) \right|\qquad\text{(37)}\\
&+&&\left|\int_{R_1+\delta\le\rho(x',y)\lt R_2} K(x',y) f(y) \, \mathrm{d}\mu(y) \right| .\qquad\text{(38)}\end{alignedat}
$$

By [small annulus](small-annulus.md), we can choose $\delta$ such that (37) is bounded by $\epsilon$. Without loss of generality, we can assume $R_1+\delta\lt R_2$. Then (38) is bounded by the right hand side of (35) and we obtain

$$
\le \epsilon + \sup_{R_1 < R_2} \sup_{x'\in B(x,R_1)} \left|\int_{B(x',R_2)\setminus B(x',R_1)} K(x',y) f(y) \, \mathrm{d}\mu(y) \right| .
$$

The inequality still holds when taking the suprema over $R_1\lt R_2$ and $\rho(x,x')\lt R_1$ in (36). Since $\epsilon>0$ was arbitrary, this proves the first inequality.

The other direction is similar. Let $\epsilon>0$. Let $R_1\lt R_2$ and $x'\in B(x,R_1)$. Then for $\delta>0$,

$$
\begin{alignedat}{3}
&&&\left|\int_{B(x',R_2)\setminus B(x',R_1)} K(x',y) f(y) \, \mathrm{d}\mu(y) \right|\qquad\text{(39)}\\
\le &&&\left|\int_{R_1-\delta\lt \rho(x',y)< R_1} K(x',y) f(y) \, \mathrm{d}\mu(y) \right|\qquad\text{(40)}\\
&+&&\left|\int_{R_1-\delta\lt \rho(x',y)\lt R_2} K(x',y) f(y) \, \mathrm{d}\mu(y) \right| .\qquad\text{(41)}\end{alignedat}
$$

By [small annulus](small-annulus.md), we can choose $\delta$ such that (40) is bounded by $\epsilon$. Without loss of generality, we can assume $\rho(x,x')\lt R_1-\delta$. Then (41) is bounded by the left hand side of (35) and we obtain

$$
\le \epsilon + \sup_{R_1 < R_2} \sup_{x'\in B(x,R_1)} \left|\int_{R_1\lt \rho(x',y)\lt R_2} K(x',y) f(y) \, \mathrm{d}\mu(y) \right| .
$$

The inequality still holds when taking the suprema over $R_1\lt R_2$ and $\rho(x,x')\lt R_1$ in (36). Since $\epsilon>0$ was arbitrary, this proves the second inequality.

## Lean

Formalized as [`nontangential_operator_boundary`](https://fpvandoorn.github.io/carleson/docs/find/#doc/nontangential_operator_boundary).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7450](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7450)
