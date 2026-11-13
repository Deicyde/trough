---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FractalUncertaintyWanted.FractalUncertainty.PorousOnBalls, MathlibExt.Analysis.FractalUncertaintyWanted.FractalUncertainty.PorousOnLines, MathlibExt.Analysis.FractalUncertaintyWanted.FractalUncertainty.cube, MathlibExt.Analysis.FractalUncertaintyWanted.FractalUncertainty.theorem_1_1
statement: formalized
---

# Fractal uncertainty principle

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fractal-uncertainty-principle/index.html).

## Porosity on balls

Let $d$ be a natural number and let $\nu$, $\alpha_0$ and $\alpha_1$ be
real numbers. A set $X$ in the Euclidean space $\mathbb{R}^d$ is $\nu$-porous on balls from scales
$\alpha_0$ to $\alpha_1$ if for every $y \in \mathbb{R}^d$ and every $R$ with
$\alpha_0 < R < \alpha_1$, the closed ball of radius $R/2$ about $y$ contains a point $x$ such that
the closed ball of radius $\nu R$ about $x$ is disjoint from $X$.

Formalized by `MathlibExt.Analysis.FractalUncertaintyWanted.FractalUncertainty.PorousOnBalls`, a definition declared in [WantedExt/Analysis/FractalUncertaintyWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FractalUncertaintyWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fractal-uncertainty-principle/index.html#porous-on-balls).

## Porosity on lines

Let $d$ be a natural number and let $\nu$, $\alpha_0$ and $\alpha_1$ be
real numbers. A set $X$ in the Euclidean space $\mathbb{R}^d$ is $\nu$-porous on lines from scales
$\alpha_0$ to $\alpha_1$ if for every $R$ with $\alpha_0 < R < \alpha_1$ and all points
$y_1, y_2 \in \mathbb{R}^d$ at distance $R$, the closed segment from $y_1$ to $y_2$ contains a point
$x$ such that the closed ball of radius $\nu R$ about $x$ is disjoint from $X$.

Formalized by `MathlibExt.Analysis.FractalUncertaintyWanted.FractalUncertainty.PorousOnLines`, a definition declared in [WantedExt/Analysis/FractalUncertaintyWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FractalUncertaintyWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fractal-uncertainty-principle/index.html#porous-on-lines).

## Closed cubes in Euclidean space

Let $d$ be a natural number. For real numbers $a$ and $b$,
the cube $[a,b]^d$ is the set of points $x$ of the Euclidean space $\mathbb{R}^d$ with
$a \le x_i \le b$ for every coordinate $i$.

Formalized by `MathlibExt.Analysis.FractalUncertaintyWanted.FractalUncertainty.cube`, an abbreviation declared in [WantedExt/Analysis/FractalUncertaintyWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FractalUncertaintyWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fractal-uncertainty-principle/index.html#cube).

## Cohen's fractal uncertainty principle for line-porous sets

Let $d$ be a natural number and
$\nu > 0$. Then there are real numbers $\beta > 0$ and $C > 0$ such that for every $h$ with
$0 < h < 1/100$ and all measurable sets $X, Y$ in the Euclidean space $\mathbb{R}^d$ the following
holds: if $X \subseteq [-1,1]^d$ is $\nu$-porous on balls from scales $h$ to $1$ and
$Y \subseteq [-h^{-1},h^{-1}]^d$ is $\nu$-porous on lines from scales $1$ to $h^{-1}$, then every
$f \in L^2(\mathbb{R}^d)$ whose Fourier transform $\mathcal{F}f$ vanishes almost everywhere outside
$Y$ satisfies $\|\mathbf{1}_X f\|_2 \le C h^{\beta} \|f\|_2$. Thus $\beta$ and $C$ depend only on
$\nu$ and $d$.

Here $\mathcal{F}$ is the Fourier transform on $L^2(\mathbb{R}^d)$, extended by continuity from
$\mathcal{F}f(\xi) = \int_{\mathbb{R}^d} e^{-2\pi i \langle x, \xi \rangle} f(x)\,dx$ on Schwartz
functions.

We require $X$ and $Y$ to be measurable to make the statement more natural.

## Sources

- A. Cohen, `Fractal uncertainty in higher dimensions`, Annals of Math, 202 (1) 2025. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_fractal_uncertainty` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.FractalUncertaintyWanted.FractalUncertainty.theorem_1_1` is written with `theorem_wanted` in [WantedExt/Analysis/FractalUncertaintyWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FractalUncertaintyWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fractal-uncertainty-principle/index.html#theorem-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fractal uncertainty principle](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fractal-uncertainty-principle/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/fourier-transform/fractal-uncertainty-principle)
