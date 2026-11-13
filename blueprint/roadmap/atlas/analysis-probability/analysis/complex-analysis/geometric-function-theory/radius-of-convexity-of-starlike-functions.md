---
declaration: section
origin: cited
lean: MathlibExt.Analysis.HaymanProblem622Wanted.conjecture, MathlibExt.Analysis.HaymanProblem622Wanted.conjecture_holds
statement: formalized
---

# Radius of convexity of starlike functions

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/radius-of-convexity-of-starlike-functions/index.html).

## Conjecture: a sharp radius of convexity for starlike functions of order 1/2

Let
$\mathbb{D}$ be the open unit disc in $\mathbb{C}$. Call $f : \mathbb{C} \to \mathbb{C}$ a
normalized starlike function of order $1/2$ if $f$ is holomorphic and injective on $\mathbb{D}$,
$f(0) = 0$, $f'(0) = 1$, and $\operatorname{Re}(z f'(z)/f(z)) \ge 1/2$ for every $z \in \mathbb{D}$
with $z \ne 0$ and $f(z) \ne 0$. Call $P : \mathbb{C} \to \mathbb{C}$ a Carathéodory function if
$P$ is holomorphic on $\mathbb{D}$, $P(0) = 1$, and $\operatorname{Re} P(z) > 0$ for every
$z \in \mathbb{D}$. Call a real number $\rho$ a good radius if
$\operatorname{Re}(1 + z f''(z)/f'(z)) > 0$ for every normalized starlike function $f$ of order
$1/2$ and every $z$ with $0 < |z| < \rho$ and $f'(z) \ne 0$, and
$\operatorname{Re}\big((P(z) + 1)/2 + z P'(z)/(P(z) + 1)\big) > 0$ for every Carathéodory
function $P$ and every $z$ with $|z| < \rho$. The conjecture is the proposition that there is a
good radius $r$ with $0 < r \le 1$ such that no real number $r'$ with $r < r' \le 1$ is a good
radius.

This is Problem 6.22 of Hayman, Research Problems in Function Theory (2018), source record
AMR-022-6022.

## Sources

- https://arxiv.org/abs/1809.07200

Formalized by `MathlibExt.Analysis.HaymanProblem622Wanted.conjecture`, a definition declared in [WantedExt/Analysis/HaymanProblem622Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HaymanProblem622Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/radius-of-convexity-of-starlike-functions/index.html#conjecture).

## A sharp radius of convexity for starlike functions of order 1/2 exists

Let $\mathbb{D}$ be
the open unit disc in $\mathbb{C}$. Call $f : \mathbb{C} \to \mathbb{C}$ a normalized starlike
function of order $1/2$ if $f$ is holomorphic and injective on $\mathbb{D}$, $f(0) = 0$,
$f'(0) = 1$, and $\operatorname{Re}(z f'(z)/f(z)) \ge 1/2$ for every $z \in \mathbb{D}$ with
$z \ne 0$ and $f(z) \ne 0$. Call $P : \mathbb{C} \to \mathbb{C}$ a Carathéodory function if $P$
is holomorphic on $\mathbb{D}$, $P(0) = 1$, and $\operatorname{Re} P(z) > 0$ for every
$z \in \mathbb{D}$. Call a real number $\rho$ a good radius if
$\operatorname{Re}(1 + z f''(z)/f'(z)) > 0$ for every normalized starlike function $f$ of order
$1/2$ and every $z$ with $0 < |z| < \rho$ and $f'(z) \ne 0$, and
$\operatorname{Re}\big((P(z) + 1)/2 + z P'(z)/(P(z) + 1)\big) > 0$ for every Carathéodory
function $P$ and every $z$ with $|z| < \rho$. Then there is a good radius $r$ with
$0 < r \le 1$ such that no real $r'$ with $r < r' \le 1$ is a good radius.

MacGregor (Proc. AMS 14 (1963) 71-76, Theorem 1) proved that the sharp radius of convexity of
normalized starlike functions of order $1/2$ is $\sqrt{2\sqrt{3}-3} \approx 0.681$; this value is
such a radius $r$. The statement above does not assert the value of $r$.

## Sources

- B. Bhowmik and S. Biswas, Radius of convexity of certain classes of functions defined by convolution, preprint (2026), arXiv:2606.20872, https://arxiv.org/abs/2606.20872.

Stated but not proved: `MathlibExt.Analysis.HaymanProblem622Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/HaymanProblem622Wanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HaymanProblem622Wanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/radius-of-convexity-of-starlike-functions/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Radius of convexity of starlike functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/radius-of-convexity-of-starlike-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory/radius-of-convexity-of-starlike-functions)
