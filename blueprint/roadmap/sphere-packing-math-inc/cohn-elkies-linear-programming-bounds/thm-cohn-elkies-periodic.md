---
declaration: theorem
origin: cited
lean: LinearProgrammingBound'
statement: formalized
proof: formalized
---

# Cohn–Elkies (ElkiesCohn)

Let $X\subset\mathbb{R}^d$ be a discrete subset such that $\|x-y\|\geq 1$ for any distinct $x,y\in X$. Suppose that $X$ is $\Lambda$-periodic with respect to some lattice $\Lambda\subset\mathbb{R}^d$. Let $f:\mathbb{R}^d\to\mathbb{R}$ be a Schwartz function that is not identically zero and satisfies the following conditions:

$$
f(x)\leq 0\mbox{ for } \|x\|\geq 1\qquad\text{(1)}
$$

and

$$
\widehat{f}(x)\geq0\mbox{ for all } x\in\mathbb{R}^d.\qquad\text{(2)}
$$

Then the density of any $\Lambda$-periodic sphere packing is bounded above by

$$
\frac{f(0)}{\widehat{f}(0)}\cdot \mathrm{vol}(B_d(0,1/2)).
$$

## Depends on

- [Fourier-Transform](../facts-from-fourier-analysis/def-fourier-transform.md)
- [SpherePacking.density](../sphere-packings/def-spherepacking-density.md)

## Proof depends on

- [Poisson summation formula](../facts-from-fourier-analysis/thm-poisson-summation-formula.md)

## Proof

Here we reproduce the proof given in (ElkiesCohn).

The inequality

$$
\sharp (X/\Lambda)\cdot f(0)\geq \sum_{x\in X}\sum_{y\in X/\Lambda}f(x-y)=\sum_{x\in X/\Lambda}\sum_{y\in X/\Lambda}\sum_{\ell\in  \Lambda}f(x-y+l)\qquad\text{(3)}
$$

follows from the condition (1) of the theorem and the assumption on the distances between points in $X$. The equality

$$
\sum_{x\in X/\Lambda}\sum_{y\in X/\Lambda}\sum_{\ell\in  \Lambda}f(x-y+l)=\sum_{x\in X/\Lambda}\sum_{y\in X/\Lambda}\frac{1}{\mathrm{vol}(\mathbb{R}^d/\Lambda)}\,\sum_{m\in \Lambda^*} \widehat{f}(m)\,e^{2\pi i m(x-y)}.
$$

follows from the Poisson summation formula. The right hand side of the above equation can be written as

$$
\sum_{x\in X/\Lambda}\sum_{y\in X/\Lambda}\frac{1}{\mathrm{vol}(\mathbb{R}^d/\Lambda)}\,\sum_{m\in \Lambda^*} \widehat{f}(m)\,e^{2\pi i m(x-y)}=\frac{1}{\mathrm{vol}(\mathbb{R}^d/\Lambda)}\,\sum_{m\in \Lambda^*} \widehat{f}(m)\cdot\big|\sum_{x\in X/\Lambda}e^{2\pi i m x}\big|^2.
$$

Note that $\big|\sum_{x\in X/\Lambda}e^{2\pi i m x}\big|^2\geq0$ for all $m\in\Lambda^*$. Moreover, the term corresponding to $m=0$ satisfies $\big|\sum_{x\in X/\Lambda}e^{2\pi i 0 x}\big|^2=\sharp (X/\Lambda)^2$. Now we use the condition (2) and estimate

$$
\frac{1}{\mathrm{vol}(\mathbb{R}^d/\Lambda)}\,\sum_{m\in \Lambda^*} \widehat{f}(m)\cdot\big|\sum_{x\in X/\Lambda}e^{2\pi i m(x-y)}\big|^2
\geq \frac{\sharp (X/\Lambda)^2}{\mathrm{vol}(\mathbb{R}^d/\Lambda)}\cdot \widehat{f}(0).\qquad\text{(4)}
$$

Comparing inequalities (3) and (4) we arrive at

$$
\frac{\sharp (X/\Lambda)}{\mathrm{vol}(\mathbb{R}^d/\Lambda)}\leq \frac{f(0)}{\widehat{f}(0)}.
$$

Now we see that the density of the periodic packing $\mathcal{P}_X$ with balls of radius $1/2$ is bounded by

$$
\Delta(\mathcal{P}_X)=\frac{\sharp (X/\Lambda)}{\mathrm{vol}(\mathbb{R}^d/\Lambda)}\cdot{\mathrm{vol}(B_d(0,1/2))}\leq
\frac{f(0)}{\widehat{f}(0)}\cdot \mathrm{vol}(B_d(0,1/2)).
$$

This finishes the proof of the theorem for periodic packings.

## Lean

Formalized as [`LinearProgrammingBound'`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/LinearProgrammingBound').

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/cohn-elkies.tex, line 4](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/cohn-elkies.tex#L4)
