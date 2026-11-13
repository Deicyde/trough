---
declaration: section
origin: cited
lean: MetaMathlibExt.newton_step_sub_root_abs_le, MetaMathlibExt.newton_method_local_quadratic_convergence
statement: formalized
proof: formalized
---

# Newton's method

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/newton-s-method/index.html).

## One-step error bound for Newton's method

Let $f : \mathbb{R} \to \mathbb{R}$ be
differentiable with $f(c) = 0$, let $x \in \mathbb{R}$, let $m > 0$ and let $K \ge 0$. If $f'$ is
Lipschitz with constant $K$ on the closed interval between $c$ and $x$ and $m \le |f'(x)|$,
then the Newton step from $x$ satisfies
$\left| x - f(x) / f'(x) - c \right| \le (K / m)\, |x - c|^2$.

Formalized by `MetaMathlibExt.newton_step_sub_root_abs_le`, a theorem declared in [MathlibExt/Analysis/Calculus/NewtonMethod.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/NewtonMethod.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/newton-s-method/index.html#newton-step-sub-root-abs-le).

## Local quadratic convergence of Newton's method

Let $f : \mathbb{R} \to \mathbb{R}$ be twice
continuously differentiable and let $c$ be a simple root of $f$: $f(c) = 0$ and $f'(c) \ne 0$.
Then there exist $\delta > 0$ and a real constant $C$ with the following property. For every
$x_0 \in (c - \delta, c + \delta)$ and every real sequence $(x_n)$ that starts at $x_0$ and
satisfies $x_{n+1} = x_n - f(x_n) / f'(x_n)$ for all $n$, every $x_n$ lies in
$(c - \delta, c + \delta)$, $|x_{n+1} - c| \le C\, |x_n - c|^2$ for all $n$, and $x_n \to c$.

Proof: Continuity keeps $f'$ away from zero near $c$, and $C^2$ regularity makes $f'$ Lipschitz
on a compact interval around $c$. The mean value theorem then bounds one Newton step by
$(K / m)\, |x - c|^2$, where $m > 0$ bounds $|f'|$ from below and $K$ is a Lipschitz constant
of $f'$; this replaces the Lagrange remainder in Wikipedia's "Proof of quadratic convergence
for Newton's iterative method". Shrinking the neighborhood gives an invariant half-contraction
and geometric convergence.

## Sources

- R. L. Burden and J. D. Faires, Numerical Analysis, 10th ed., Theorem 2.6; stable ref https://en.wikipedia.org/wiki/Newton%27s_method.

Formalized by `MetaMathlibExt.newton_method_local_quadratic_convergence`, a theorem declared in [MathlibExt/Analysis/Calculus/NewtonMethod.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/NewtonMethod.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/newton-s-method/index.html#newton-method-local-quadratic-convergenc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Newton's method](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/newton-s-method/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/numerical-analysis/newton-s-method)
