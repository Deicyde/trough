---
declaration: theorem
origin: cited
lean: exceptional_set_carleson
statement: formalized
proof: formalized
---

# classical Carleson with exceptional sets

Let $f$ be a $2\pi$-periodic complex-valued continuous function on $\mathbb{R}$. For all $\epsilon>0$, there exists a Borel set $E\subset [0,2\pi]$ with Lebesgue measure $|E|\le \epsilon$ and a positive integer $N_0$ such that for all $x\in [0,2\pi]\setminus E$ and all integers $N>N_0$, we have

$$
|f(x)-S_N f(x)|\le \epsilon.\qquad\text{(5)}
$$

## Depends on

- [smooth approximation](smooth-approximation.md)
- [convergence for smooth](convergence-for-smooth.md)
- [control approximation effect](control-approximation-effect.md)

## Proof

Let $N_0$ be as in [convergence for smooth](convergence-for-smooth.md). For every

$$
x\in [0, 2\pi) \setminus E\, ,
$$

and every $N>N_0$ we have by the triangle inequality

$$
|f(x)-S_Nf(x)|
$$

$$
\le |f(x)-f_0(x)|+ |f_0(x)-S_Nf_0(x)|+|S_Nf_0(x)-S_N f(x)|\, .\qquad\text{(6)}
$$

Using [smooth approximation](smooth-approximation.md), [convergence for smooth](convergence-for-smooth.md) and [control approximation effect](control-approximation-effect.md), we estimate (6) by

$$
\le \epsilon' +\frac \epsilon 4 +\frac \epsilon 4\le \epsilon\, .
$$

This shows (5) for the given $E$ and $N_0$.

## Lean

Formalized as [`exceptional_set_carleson`](https://fpvandoorn.github.io/carleson/docs/find/#doc/exceptional_set_carleson).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8224](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8224)
