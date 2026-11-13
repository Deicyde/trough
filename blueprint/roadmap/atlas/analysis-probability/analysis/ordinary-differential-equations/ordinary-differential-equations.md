---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ODE.CauchyPeanoWanted.cauchy_peano_exists, MathlibExt.Analysis.BVPComparisonWanted.Analysis.ODE.bvp_comparison, MathlibExt.Analysis.CubicDecayWanted.Analysis.ODE.cubic_decay_asymptotic, MathlibExt.Analysis.DirichletEigenvaluesWanted.Analysis.ODE.dirichlet_eigenvalues_eq_nat_sq, MathlibExt.Analysis.ODE.DuhamelWanted.duhamel_variation_of_constants, MathlibExt.Analysis.Calculus.NonresonantForcedOscillatorPeriodicWanted.existsUnique_periodic_solution_and_isBounded_of_ne_natCast, MathlibExt.Analysis.Calculus.BesselTypeOdeInfinitelyManyZerosWanted.setInfinite_zero_of_mul_iteratedDeriv_two_add_two_deriv_add_eq_zero, MathlibExt.Analysis.SturmSeparationWanted.Analysis.ODE.sturm_separation
statement: formalized
---

# Ordinary differential equations: its own results

8 results, 2 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/index.html).

Existence and uniqueness (Cauchy–Peano, Picard, maximal solutions), linear systems and fundamental matrices, stability and Lyapunov's indirect method, Sturm–Liouville and boundary value problems with their Green's operators and eigenfunctions, oscillation and comparison theorems.

## Cauchy–Peano existence theorem

Let $E$ be a finite-dimensional real normed space and let
$f : \mathbb{R} \times E \to E$ be continuous. Then for every $t_0 \in \mathbb{R}$ and
$x_0 \in E$ there are $\varepsilon > 0$ and a function $x : \mathbb{R} \to E$ with
$x(t_0) = x_0$ such that, for every $t \in (t_0 - \varepsilon, t_0 + \varepsilon)$, $x$ is
differentiable at $t$ with $x'(t) = f(t, x(t))$.

## Sources

- G. Peano, Math. Ann. 37 (1890), 182-228, DOI 10.1007/BF01200235.

Formalized by `MathlibExt.Analysis.ODE.CauchyPeanoWanted.cauchy_peano_exists`, a theorem declared in [MathlibExt/Analysis/ODE/CauchyPeano.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/CauchyPeano.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/index.html#cauchy-peano-exists).

## Comparison principle for the Dirichlet problem on $(0, 1)$

Let $J \subseteq \mathbb{R}$
be an open set containing $[0, 1]$, and let $u, v : \mathbb{R} \to \mathbb{R}$ be functions
that are differentiable at every point of $J$ and whose derivatives $u'$ and $v'$ are
differentiable at every point of $J$. If $-u''(x) \le -v''(x)$ for every $x \in (0, 1)$,
$u(0) \le v(0)$ and $u(1) \le v(1)$, then $u(x) \le v(x)$ for every $x \in [0, 1]$.

## Sources

- Standard maximum-principle argument; Protter-Weinberger. Problem `bvp_comparison` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.BVPComparisonWanted.Analysis.ODE.bvp_comparison` is written with `theorem_wanted` in [WantedExt/Analysis/BVPComparisonWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/BVPComparisonWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/index.html#bvp-comparison).

## Decay rate of solutions of $y' = -y^3$

Let $y : \mathbb{R} \to \mathbb{R}$ be
differentiable at every $t > 0$ with $y'(t) = -y(t)^3$, continuous at $0$ within $[0, \infty)$,
and such that $y(0) = 1$. Then $y(t) \sqrt{t} \to 1/\sqrt{2}$ as $t \to \infty$.

## Sources

- Standard ODE textbook exercise. Problem `cubic_decay_asymptotic` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.CubicDecayWanted.Analysis.ODE.cubic_decay_asymptotic` is written with `theorem_wanted` in [WantedExt/Analysis/CubicDecayWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/CubicDecayWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/index.html#cubic-decay-asymptotic).

## Dirichlet eigenvalues of $-y'' = \lambda y$ on $(0, \pi)$

For every real number
$\lambda$, the following are equivalent:
(i) there are a function $y : \mathbb{R} \to \mathbb{R}$ and an open set $J \subseteq \mathbb{R}$
containing $[0, \pi]$ such that $y$ is differentiable at every point of $J$, its derivative $y'$
is differentiable at every $x \in J$ with $y''(x) = -\lambda y(x)$, $y(0) = y(\pi) = 0$, and
$y(x) \ne 0$ for some $x \in (0, \pi)$;
(ii) $\lambda = n^2$ for some positive integer $n$.

## Sources

- Classical Sturm-Liouville theory. Problem `dirichlet_eigenvalues_eq_nat_sq` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.DirichletEigenvaluesWanted.Analysis.ODE.dirichlet_eigenvalues_eq_nat_sq` is written with `theorem_wanted` in [WantedExt/Analysis/DirichletEigenvaluesWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/DirichletEigenvaluesWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/index.html#dirichlet-eigenvalues-eq-nat-sq).

## Duhamel's formula (variation of constants)

Let $E$ be a real Banach space, let
$A : E \to E$ be a bounded linear operator, let $b : \mathbb{R} \to E$ be continuous, and let
$t_0 \in \mathbb{R}$ and $x_0 \in E$. Write $e^{sA}$ for the operator exponential and define
$x : \mathbb{R} \to E$ by
$x(t) = e^{(t - t_0)A} x_0 + \int_{t_0}^{t} e^{(t - s)A} b(s)\, ds$.
Then $x(t_0) = x_0$ and $x$ is differentiable with $x'(t) = A x(t) + b(t)$ for every
$t \in \mathbb{R}$. Moreover $x$ is the only such solution: every $y : \mathbb{R} \to E$ with
$y(t_0) = x_0$ and $y'(t) = A y(t) + b(t)$ for every $t \in \mathbb{R}$ equals $x$.

Proof: Factor the propagator by the commuting exponential group law, differentiate the
integrating-factor primitive, and apply global Lipschitz uniqueness. This follows Teschl,
Sections 3.2 and 3.4, formula (3.48) and Theorem 3.12 / (3.97).

## Sources

- G. Teschl, Ordinary Differential Equations and Dynamical Systems, Section 3.2; stable ref https://en.wikipedia.org/wiki/Duhamel%27s_principle.

Formalized by `MathlibExt.Analysis.ODE.DuhamelWanted.duhamel_variation_of_constants`, a theorem declared in [MathlibExt/Analysis/ODE/Duhamel.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/Duhamel.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/index.html#duhamel-variation-of-constants).

## Nonresonant forced oscillator

Let $\omega > 0$ be a real number that is not an integer,
and let $g : \mathbb{R} \to \mathbb{R}$ be continuous and $2\pi$-periodic. Then the equation
$u'' + \omega^2 u = g$ has exactly one twice continuously differentiable solution
$u : \mathbb{R} \to \mathbb{R}$ that is $2\pi$-periodic, and every twice continuously
differentiable solution $u : \mathbb{R} \to \mathbb{R}$ of this equation is bounded.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; Ordinary differential operators), problem `ma_proofbench_l2_39`.

Stated but not proved: `MathlibExt.Analysis.Calculus.NonresonantForcedOscillatorPeriodicWanted.existsUnique_periodic_solution_and_isBounded_of_ne_natCast` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/NonresonantForcedOscillatorPeriodicWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/NonresonantForcedOscillatorPeriodicWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/index.html#exists-unique-periodic-solution-and-is-b).

## Solutions of $xu''+2u'+u=0$ have infinitely many zeros

Let $u : \mathbb{R} \to \mathbb{R}$
be twice continuously differentiable on $(0,\infty)$ and satisfy

$$
x\,u''(x)+2u'(x)+u(x)=0 \quad \text{for all } x>0.
$$

If $u(x) \ne 0$ for some $x>0$, then $u$ has infinitely many zeros in $(1,\infty)$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; Ordinary differential operators), problem `ma_proofbench_l2_83`.

Stated but not proved: `MathlibExt.Analysis.Calculus.BesselTypeOdeInfinitelyManyZerosWanted.setInfinite_zero_of_mul_iteratedDeriv_two_add_two_deriv_add_eq_zero` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/BesselTypeOdeInfinitelyManyZerosWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/BesselTypeOdeInfinitelyManyZerosWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/index.html#set-infinite-zero-of-mul-iterated-deriv).

## Sturm separation theorem

Let $p, q, y_1, y_2 : \mathbb{R} \to \mathbb{R}$ and $a < b$,
and let $J \subseteq \mathbb{R}$ be an open connected set (an open interval, possibly unbounded)
containing $[a, b]$. Suppose that $p$ and $q$ are continuous on $J$, and that $y_1$ and $y_2$
are twice differentiable at every point of $J$ and solve $y'' + p(x)\, y' + q(x)\, y = 0$ at
every $x \in J$. Suppose further that the Wronskian $y_1 y_2' - y_2 y_1'$ is nonzero at some
point of $J$. If $y_1(a) = y_1(b) = 0$ and $y_1(x) \ne 0$ for every $x \in (a, b)$, then $y_2$
has exactly one zero in the open interval $(a, b)$.

## Sources

- C. Sturm, Mémoire sur les équations différentielles linéaires du second ordre, 1836. Problem `sturm_separation` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.SturmSeparationWanted.Analysis.ODE.sturm_separation` is written with `theorem_wanted` in [WantedExt/Analysis/SturmSeparationWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/SturmSeparationWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/index.html#sturm-separation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ordinary differential equations](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/ordinary-differential-equations)
