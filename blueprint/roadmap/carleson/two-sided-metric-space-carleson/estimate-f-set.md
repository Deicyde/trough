---
declaration: lemma
origin: cited
lean: distribution_czOperatorBound
statement: formalized
proof: formalized
---

# Estimate F set

For $F$ as defined in [Estimate bad partial](estimate-bad-partial.md), we have

$$
\mu(\{x\in X\setminus\Omega: F(x)>\alpha/8\}) \le \frac{2^{a^3+9a+4}}{\alpha} \int |f(y)|\,d\mu(y)\,.\qquad\text{(77)}
$$

## Depends on

- [Calderon Zygmund decomposition](calderon-zygmund-decomposition.md)
- [geometric series estimate](geometric-series-estimate.md)

## Proof

We estimate

$$
\begin{aligned}
\mu(\{x\in X\setminus\Omega&: F(x)> \alpha/8\})
\le \frac{8}{\alpha} \int_{X\setminus \Omega} F(x)\,d\mu(x) \\
&\le \frac{8}{\alpha} \int_{X\setminus \Omega} 2^{a^3+2a+1} c\alpha \sum_{j} \left(\frac{3r_j}{\rho(x,x_j)}\right)^{\frac{1}{a}}\frac{\mu(B_{3,j})}{V(x,x_j)}\,d\mu(x) \\
&\le 2^{a^3+2a+4} c \sum_{j} \mu(B_{3,j}) \int_{X\setminus B_{6,j}} \left(\frac{3r_j}{\rho(x,x_j)}\right)^{\frac{1}{a}}\frac{1}{V(x,x_j)}\,d\mu(x)\qquad\text{(78)}\end{aligned}
$$

Using

$$
V(x,x_j) = \mu(B(x,\rho(x,x_j))) \ge 2^{-a}\mu(B(x,2\rho(x,x_j))) \ge 2^{-a} \mu(B(x_j,\rho(x_j,x))),
$$

we have for all $j\in J$,

$$
\begin{aligned}
&\int_{X\setminus B_{6,j}} \left(\frac{3r_j}{\rho(x,x_j)}\right)^{\frac{1}{a}}\frac{1}{V(x,x_j)}\,d\mu(x) \\
\le& 2^a \int_{X\setminus B_{6,j}} \left(\frac{3r_j}{\rho(x,x_j)}\right)^{\frac{1}{a}}\frac{1}{\mu(B(x_j,\rho(x_j,x)))}\,d\mu(x) \\
\le&2^a \sum_{n=1}^\infty \int_{B(x_j,2^{n+1}\cdot3r_j)\setminus B(x_j,2^n\cdot3r_j)} \left(\frac{3r_j}{2^n \cdot3r_j}\right)^{\frac{1}{a}}\frac{1}{\mu(B(x_j,2^n \cdot3r_j))}\,d\mu(x) \\
\le&2^a \sum_{n=1}^\infty 2^{-\frac{n}{a}} \frac{\mu(B(x_j,2^{n+1}\cdot3r_j))}{\mu(B(x_j,2^n \cdot3r_j))} \\
\le&2^{3a},
\end{aligned}
$$

where we used [geometric series estimate](geometric-series-estimate.md) in the last step. Plugging this into (78) and using [(56)](calderon-zygmund-decomposition.md), we conclude that

$$
\mu(\{x\in X\setminus\Omega: F(x)> \alpha/8\}) \le \frac{2^{a^3+9a+4}}{\alpha} \int |f(y)|\,d\mu(y)\,.
$$

## Lean

Formalized as [`distribution_czOperatorBound`](https://fpvandoorn.github.io/carleson/docs/find/#doc/distribution_czOperatorBound).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8029](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8029)
