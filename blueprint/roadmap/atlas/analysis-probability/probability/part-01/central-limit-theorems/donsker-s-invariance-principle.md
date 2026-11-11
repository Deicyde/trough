---
declaration: section
origin: cited
lean: MathlibExt.Probability.DonskerWanted.donskerClamp, MathlibExt.Probability.DonskerWanted.donskerWeight, MathlibExt.Probability.DonskerWanted.donskerWeightCM, MathlibExt.Probability.DonskerWanted.donskerProcess, MathlibExt.Probability.DonskerWanted.donskerProcess_apply_eq, MathlibExt.Probability.DonskerWanted.iccToNNReal, MathlibExt.Probability.DonskerWanted.continuousMap_measure_ext_of_finset_eval, MathlibExt.Probability.DonskerWanted.etemadi_maximal_inequality
statement: formalized
proof: formalized
---

# Donsker's invariance principle

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/donsker-s-invariance-principle/index.html).

## Clamping to the unit interval

For a real number $x$, its clamp to $[0,1]$ is
$\min(\max(x, 0), 1)$.

Formalized by `MathlibExt.Probability.DonskerWanted.donskerClamp`, a definition declared in [MathlibExt/Probability/Donsker.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Donsker.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/donsker-s-invariance-principle/index.html#donsker-clamp).

## Polygonal interpolation weight

For natural numbers $n$ and $i$ and $t \in [0,1]$, the
weight is $w_{n,i}(t) = \min(\max(nt - i, 0), 1)$, the clamp of $nt - i$ to $[0,1]$.

Formalized by `MathlibExt.Probability.DonskerWanted.donskerWeight`, a definition declared in [MathlibExt/Probability/Donsker.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Donsker.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/donsker-s-invariance-principle/index.html#donsker-weight).

## Polygonal interpolation weight as a continuous function

For natural numbers $n$ and $i$,
this is the function $t \mapsto \min(\max(nt - i, 0), 1)$ on $[0,1]$, regarded as an element of
the space $C([0,1], \mathbb{R})$ of continuous real functions on $[0,1]$.

Formalized by `MathlibExt.Probability.DonskerWanted.donskerWeightCM`, a definition declared in [MathlibExt/Probability/Donsker.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Donsker.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/donsker-s-invariance-principle/index.html#donsker-weight-cm).

## Polygonal partial-sum process

Let $X_0, X_1, \dots$ be real-valued functions on a set
$\Omega$. For $n \in \mathbb{N}$ and $\omega \in \Omega$, $S_n(\omega)$ is the element of the space
$C([0,1], \mathbb{R})$ of continuous real functions on $[0,1]$ defined by $S_0(\omega) = 0$ and,
for $n \ge 1$ and $t \in [0,1]$,

$$S_n(\omega)(t) = \frac{1}{\sqrt{n}} \sum_{i=0}^{n-1} X_i(\omega) \min(\max(nt - i, 0), 1).$$

Thus for $n \ge 1$, $S_n(\omega)$ linearly interpolates the values
$(X_0(\omega) + \dots + X_{k-1}(\omega))/\sqrt{n}$ at the times $k/n$ for $0 \le k \le n$.

Formalized by `MathlibExt.Probability.DonskerWanted.donskerProcess`, a definition declared in [MathlibExt/Probability/Donsker.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Donsker.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/donsker-s-invariance-principle/index.html#donsker-process).

## Explicit formula for the polygonal partial-sum process

Let $X_0, X_1, \dots$ be
real-valued functions on a set $\Omega$ and let $S_n$ be their polygonal partial-sum process. For
$n \ge 1$, $\omega \in \Omega$ and $t \in [0,1]$, write $m = \lfloor nt \rfloor$. Then

$$S_n(\omega)(t) = \frac{1}{\sqrt{n}} \Big( \sum_{i=0}^{m-1} X_i(\omega) + c \Big),$$

where $c = (nt - m) X_m(\omega)$ if $m < n$ and $c = 0$ otherwise.

Formalized by `MathlibExt.Probability.DonskerWanted.donskerProcess_apply_eq`, a theorem declared in [MathlibExt/Probability/Donsker.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Donsker.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/donsker-s-invariance-principle/index.html#donsker-process-apply-eq).

## Inclusion of the unit interval into the nonnegative reals

This map sends $t \in [0,1]$
to $t$ regarded as a nonnegative real number.

Formalized by `MathlibExt.Probability.DonskerWanted.iccToNNReal`, a definition declared in [MathlibExt/Probability/Donsker.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Donsker.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/donsker-s-invariance-principle/index.html#icc-to-nnreal).

## Finite-dimensional distributions determine laws on $C((0,1))$

Probability measures on `C([0,1], ℝ)` are determined by their finite-dimensional
distributions. Compatibility wrapper around
`MathlibExt.Probability.ContinuousPathConvergence.continuousPath_measure_ext_of_finset_eval`
at `T = 1`; the projective-limit argument lives there, not here.

Formalized by `MathlibExt.Probability.DonskerWanted.continuousMap_measure_ext_of_finset_eval`, a theorem declared in [MathlibExt/Probability/Donsker.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Donsker.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/donsker-s-invariance-principle/index.html#continuous-map-measure-ext-of-finset-eva).

## Etemadi's maximal inequality

Let $X_0, X_1, \dots$ be independent real random variables
on a probability space $(\Omega, P)$ and write $S_k = X_0 + \dots + X_{k-1}$, so that $S_0 = 0$.
Then for every natural number $n$ and every real number $a$,

$$P\Big(\max_{0 \le k \le n} |S_k| \ge 3a\Big) \le 3 \max_{0 \le k \le n} P(|S_k| \ge a).$$

Formalized by `MathlibExt.Probability.DonskerWanted.etemadi_maximal_inequality`, a theorem declared in [MathlibExt/Probability/Donsker.lean, line 1334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Donsker.lean#L1334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/donsker-s-invariance-principle/index.html#etemadi-maximal-inequality).

## Donsker's invariance principle

Let $X_0, X_1, \dots$ be independent, identically
distributed, measurable real random variables on a probability space $(\Omega, P)$ such that
$X_0$ is integrable, $\mathbb{E}[X_0^2] < \infty$, $\mathbb{E}[X_0] = 0$ and
$\operatorname{Var}(X_0) = 1$. Let $(B_t)_{t \ge 0}$ be a real Brownian motion on a probability
space $(\Omega', P')$: its finite-dimensional laws are those of Brownian motion and its paths are
$P'$-almost surely continuous. For $n \ge 1$ let $S_n$ be the polygonal partial-sum process of
the $X_i$, the random element of $C([0,1], \mathbb{R})$ that linearly interpolates the values
$(X_0 + \dots + X_{k-1})/\sqrt{n}$ at the times $k/n$ for $0 \le k \le n$. Then there is a random
element $Y$ of $C([0,1], \mathbb{R})$ defined on $\Omega'$ such that $P'$-almost surely
$Y(t) = B_t$ for all $t \in [0,1]$, and $S_n$ converges in distribution to $Y$ as $n \to \infty$.
Here $C([0,1], \mathbb{R})$ carries the topology of uniform convergence and its Borel
$\sigma$-algebra.

Proof: The route combines finite-dimensional convergence from the central limit theorem,
tightness from a maximal inequality and a modulus-of-continuity criterion, Prokhorov's theorem,
and uniqueness of laws on $C([0,1], \mathbb{R})$ from finite-dimensional distributions.

## Sources

- M. D. Donsker, An invariance principle for certain probability limit theorems, Mem. Amer. Math. Soc. 6 (1951); extension Prohorov 1956 to Polish; textbook in Billingsley, Convergence of Probability Measures, 2nd ed., Kallenberg, Foundations of Modern Probability; Lean is `C(Icc 0 1, ℝ)` polygonal process with `MemLp 2`, mean-zero variance-one standardization.

Formalized by `MathlibExt.Probability.DonskerWanted.donsker_invariance_principle`, a theorem declared in [MathlibExt/Probability/Donsker.lean, line 2618](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Donsker.lean#L2618). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/donsker-s-invariance-principle/index.html#donsker-invariance-principle).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Donsker's invariance principle](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/donsker-s-invariance-principle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/central-limit-theorems/donsker-s-invariance-principle)
