---
declaration: section
origin: cited
lean: Real.exists_cos_sub_cos_ge_one, Real.exists_cos_oscillation, Real.weierstrassFun, Real.norm_weierstrassFun_term_le, Real.summable_weierstrassFun_terms, Real.summable_abs_weierstrassFun_terms, Real.continuous_weierstrassFun, Real.weierstrassFun_abs_le
statement: formalized
proof: formalized
---

# Weierstrass function

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/weierstrass-function/index.html).

## Cosine oscillation (phase-shift form)

For every real number $\theta$ there is a real
number $\varphi$ with $\pi < \varphi < 3\pi$ such that
$|\cos\theta - \cos(\theta + \varphi)| \ge 1$.

The two candidate shifts are $3\pi/2$ and $5\pi/2$, where $\cos(\theta + \varphi)$ equals
$\sin\theta$ and $-\sin\theta$ respectively; at least one of $|\cos\theta - \sin\theta|$ and
$|\cos\theta + \sin\theta|$ is at least $1$, since their squares sum to $2$.

Formalized by `Real.exists_cos_sub_cos_ge_one`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/CosineOscillation.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/CosineOscillation.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/weierstrass-function/index.html#exists-cos-sub-cos-ge-one).

## Cosine oscillation (scaled form)

For every real number $c$ and every positive integer
$K$, there is a real number $y$ with $c + \pi / K < y < c + 3\pi / K$ such that
$|\cos(Kc) - \cos(Ky)| \ge 1$.

This is the estimate that drives the slope blow-up in the proof that the Weierstrass function is
nowhere differentiable.

Formalized by `Real.exists_cos_oscillation`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/CosineOscillation.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/CosineOscillation.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/weierstrass-function/index.html#exists-cos-oscillation).

## The Weierstrass function

The Weierstrass function is the function
$W : \mathbb{R} \to \mathbb{R}$ given by $W(x) = \sum_{k \ge 0} \cos(160^k x) / 4^k$, the sum
running over all natural numbers $k$.

Formalized by `Real.weierstrassFun`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/WeierstrassFunction.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/WeierstrassFunction.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/weierstrass-function/index.html#weierstrass-fun).

## Termwise bound for the Weierstrass series

For every natural number $k$ and every real
number $x$, $|\cos(160^k x) / 4^k| \le (1/4)^k$.

The right-hand side is the $k$-th term of a convergent geometric series.

Formalized by `Real.norm_weierstrassFun_term_le`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/WeierstrassFunction.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/WeierstrassFunction.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/weierstrass-function/index.html#norm-weierstrass-fun-term-le).

## Summability of the Weierstrass series

For every real number $x$, the series
$\sum_{k \ge 0} \cos(160^k x) / 4^k$ defining the Weierstrass function is summable, by
comparison with the geometric series $\sum_{k \ge 0} (1/4)^k$.

Formalized by `Real.summable_weierstrassFun_terms`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/WeierstrassFunction.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/WeierstrassFunction.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/weierstrass-function/index.html#summable-weierstrass-fun-terms).

## Absolute convergence of the Weierstrass series

For every real number $x$, the series
$\sum_{k \ge 0} \cos(160^k x) / 4^k$ defining the Weierstrass function converges absolutely,
that is, $\sum_{k \ge 0} |\cos(160^k x) / 4^k|$ is summable.

Formalized by `Real.summable_abs_weierstrassFun_terms`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/WeierstrassFunction.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/WeierstrassFunction.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/weierstrass-function/index.html#summable-abs-weierstrass-fun-terms).

## Continuity of the Weierstrass function

The Weierstrass function
$W(x) = \sum_{k \ge 0} \cos(160^k x) / 4^k$ is continuous on $\mathbb{R}$.

It is a uniform limit of continuous partial sums.

Formalized by `Real.continuous_weierstrassFun`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/WeierstrassFunction.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/WeierstrassFunction.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/weierstrass-function/index.html#continuous-weierstrass-fun).

## Bound on the Weierstrass function

The Weierstrass function
$W(x) = \sum_{k \ge 0} \cos(160^k x) / 4^k$ satisfies $|W(x)| \le 4/3$ for every real number $x$.

Formalized by `Real.weierstrassFun_abs_le`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/WeierstrassFunction.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/WeierstrassFunction.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/weierstrass-function/index.html#weierstrass-fun-abs-le).

## Reverse triangle inequality, three terms

For all real numbers
`a`, `b`, `c`, the absolute value of their sum is at least
`|a| - |b| - |c|`.

Formalized by `Real.reverse_triangle_three`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/WeierstrassNowhereDifferentiable.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/WeierstrassNowhereDifferentiable.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/weierstrass-function/index.html#reverse-triangle-three).

## Slope blow-up lemma

For every real `c` and every natural number
`n`, there exists a point `y ≠ c` with `|y - c| < 3π / 160ⁿ` such that
the difference quotient of the Weierstrass function between `y` and `c`
has absolute value at least `40ⁿ / (117 π)`. Since
`40ⁿ / (117 π) → ∞`, this witnesses that the function cannot have a
finite derivative at `c`.

Formalized by `Real.weierstrassFun_slope_lower_bound`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/WeierstrassNowhereDifferentiable.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/WeierstrassNowhereDifferentiable.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/weierstrass-function/index.html#weierstrass-fun-slope-lower-bound).

## The Weierstrass function is nowhere differentiable

The Weierstrass function
$W(x) = \sum_{k=0}^{\infty} \cos(160^k x) / 4^k$ is differentiable at no point of $\mathbb{R}$:
for every real number $c$, $W$ is not differentiable at $c$.

The proof uses the slope blow-up lemma to exhibit a sequence of points approaching $c$ along
which the absolute values of the difference quotients of $W$ tend to infinity, contradicting
the convergence of the slope to a finite derivative.

Formalized by `Real.weierstrassFun_nowhere_differentiable`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/WeierstrassNowhereDifferentiable.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/WeierstrassNowhereDifferentiable.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/weierstrass-function/index.html#weierstrass-fun-nowhere-differentiable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weierstrass function](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/weierstrass-function/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/real-functions/continuity-and-functional-equations/weierstrass-function)
