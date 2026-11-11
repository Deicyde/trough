---
declaration: section
origin: cited
lean: MathlibExt.Analysis.HausdorffAbsoluteContinuityWanted.Analysis.HausdorffAbsoluteContinuity.cube, MathlibExt.Analysis.HausdorffAbsoluteContinuityWanted.Analysis.HausdorffAbsoluteContinuity.monomial, MathlibExt.Analysis.HausdorffAbsoluteContinuityWanted.Analysis.HausdorffAbsoluteContinuity.momentOf, MathlibExt.Analysis.HausdorffAbsoluteContinuityWanted.Analysis.HausdorffAbsoluteContinuity.multiChoose, MathlibExt.Analysis.HausdorffAbsoluteContinuityWanted.Analysis.HausdorffAbsoluteContinuity.diff, MathlibExt.Analysis.HausdorffAbsoluteContinuityWanted.Analysis.HausdorffAbsoluteContinuity.UniformlyAbsolutelyContinuous, MathlibExt.Analysis.HausdorffAbsoluteContinuityWanted.Analysis.HausdorffAbsoluteContinuity.hausdorff_absolute_continuity, MathlibExt.Analysis.HausdorffMomentsWanted.Analysis.cube
statement: formalized
---

# Hausdorff moment problem

17 results, 14 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html).

## Closed unit cube

For $d \in \mathbb{N}$, the closed unit cube $I^d = [0,1]^d$ is the
set of points $x \in \mathbb{R}^d$ with $0 \le x_i \le 1$ for every coordinate $i$.

Formalized by `MathlibExt.Analysis.HausdorffAbsoluteContinuityWanted.Analysis.HausdorffAbsoluteContinuity.cube`, a definition declared in [WantedExt/Analysis/HausdorffAbsoluteContinuityWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffAbsoluteContinuityWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#cube).

## Multivariate monomial

For a multi-index $n = (n_1, \dots, n_d) \in \mathbb{N}^d$ and a
point $x \in \mathbb{R}^d$, the monomial $x^n$ is the real number $\prod_{i=1}^{d} x_i^{n_i}$.

Formalized by `MathlibExt.Analysis.HausdorffAbsoluteContinuityWanted.Analysis.HausdorffAbsoluteContinuity.monomial`, a definition declared in [WantedExt/Analysis/HausdorffAbsoluteContinuityWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffAbsoluteContinuityWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#monomial).

## Moments of a measure on the unit cube

For a measure $\mu$ on $\mathbb{R}^d$ and a
multi-index $n \in \mathbb{N}^d$, the $n$-th moment of $\mu$ is the real number
$\int_{I^d} x^n \, d\mu(x)$, the integral over the closed unit cube $I^d = [0,1]^d$ of the
monomial $x^n = \prod_{i=1}^{d} x_i^{n_i}$, taken to be $0$ when the monomial is not
$\mu$-integrable on $I^d$.

Formalized by `MathlibExt.Analysis.HausdorffAbsoluteContinuityWanted.Analysis.HausdorffAbsoluteContinuity.momentOf`, a definition declared in [WantedExt/Analysis/HausdorffAbsoluteContinuityWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffAbsoluteContinuityWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#moment-of).

## Multi-index binomial coefficient

For multi-indices $n, k \in \mathbb{N}^d$, the
binomial coefficient $\binom{n}{k}$ is the natural number $\prod_{i=1}^{d} \binom{n_i}{k_i}$.

Formalized by `MathlibExt.Analysis.HausdorffAbsoluteContinuityWanted.Analysis.HausdorffAbsoluteContinuity.multiChoose`, a definition declared in [WantedExt/Analysis/HausdorffAbsoluteContinuityWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffAbsoluteContinuityWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#multi-choose).

## Iterated backward difference of a multi-sequence

For a function
$a : \mathbb{N}^d \to \mathbb{R}$ and multi-indices $k, n \in \mathbb{N}^d$,

$$(\Delta^k a)_n = \sum_{j \le k} (-1)^{|k| - |j|} \binom{k}{j} \, a_{n - j},$$

where $j$ runs over the multi-indices with $j_i \le k_i$ for every $i$, $|k| = \sum_i k_i$,
$\binom{k}{j} = \prod_i \binom{k_i}{j_i}$ is the multi-index binomial coefficient, and $n - j$
is taken coordinatewise, with $n_i - j_i$ replaced by $0$ when $j_i > n_i$.

When $k \le n$ coordinatewise, $\Delta^k$ is the composite of $k_i$ applications of
$(\Delta_i a)_n = a_{n - e_i} - a_n$ in each coordinate $i$, where $e_i$ is the $i$-th unit
multi-index.

Formalized by `MathlibExt.Analysis.HausdorffAbsoluteContinuityWanted.Analysis.HausdorffAbsoluteContinuity.diff`, a definition declared in [WantedExt/Analysis/HausdorffAbsoluteContinuityWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffAbsoluteContinuityWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#diff).

## Uniformly absolutely continuous measures

A measure $\mu$ on $\mathbb{R}^d$ is uniformly
absolutely continuous with respect to a measure $\nu$ on $\mathbb{R}^d$ if there is a real
constant $C \ge 0$ with $\mu(S) \le C \, \nu(S)$ for every measurable set $S$.

When $\nu$ is $\sigma$-finite, this says that $\mu$ has an essentially bounded Radon–Nikodym
density with respect to $\nu$.

Formalized by `MathlibExt.Analysis.HausdorffAbsoluteContinuityWanted.Analysis.HausdorffAbsoluteContinuity.UniformlyAbsolutelyContinuous`, a definition declared in [WantedExt/Analysis/HausdorffAbsoluteContinuityWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffAbsoluteContinuityWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#uniformly-absolutely-continuous).

## Hausdorff's absolute continuity criterion

Let $\mu$ be a probability measure on
$\mathbb{R}^d$ with $\mu(\mathbb{R}^d \setminus I^d) = 0$, where $I^d = [0,1]^d$ is the closed
unit cube, and let $\lambda$ be Lebesgue measure restricted to $I^d$. For a measure $\rho$ write
$m_\rho(n) = \int_{I^d} x^n \, d\rho(x)$ for its moments, indexed by multi-indices
$n \in \mathbb{N}^d$. Then $\mu$ is uniformly absolutely continuous with respect to $\lambda$ if
and only if there is a real constant $C$ such that
$(\Delta^k m_\mu)_n \le C \, (\Delta^k m_\lambda)_n$ for all multi-indices $k \le n$
(coordinatewise), where $\Delta^k$ is the iterated backward difference.

## Sources

- F. Hausdorff (1921–1923); see Shohat–Tamarkin, *The Problem of Moments*. Knill, *Some fundamental theorems in mathematics*, §115. Problem `hausdorff_absolute_continuity` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.HausdorffAbsoluteContinuityWanted.Analysis.HausdorffAbsoluteContinuity.hausdorff_absolute_continuity` is written with `theorem_wanted` in [WantedExt/Analysis/HausdorffAbsoluteContinuityWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffAbsoluteContinuityWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#hausdorff-absolute-continuity).

## Unit cube of the Hausdorff moment problem

For $d \in \mathbb{N}$, the closed unit cube
$I^d = [0,1]^d$ is the set of points $x \in \mathbb{R}^d$ with $0 \le x_i \le 1$ for every
coordinate $i$.

Formalized by `MathlibExt.Analysis.HausdorffMomentsWanted.Analysis.cube`, a definition declared in [WantedExt/Analysis/HausdorffMomentsWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffMomentsWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#cube-2).

## Multi-index monomial

For a multi-index $n \in \mathbb{N}^d$, the monomial $x^n$ is the
real function on $\mathbb{R}^d$ given by $x^n = \prod_i x_i^{n_i}$.

Formalized by `MathlibExt.Analysis.HausdorffMomentsWanted.Analysis.monomial`, a definition declared in [WantedExt/Analysis/HausdorffMomentsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffMomentsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#monomial-2).

## Moments on the unit cube

For a measure $\mu$ on $\mathbb{R}^d$ and a multi-index
$n \in \mathbb{N}^d$, the $n$-th moment of $\mu$ on the unit cube is the real number
$\int_{[0,1]^d} x^n \, d\mu(x)$, where $x^n = \prod_i x_i^{n_i}$.

When $x^n$ is not $\mu$-integrable on $[0,1]^d$, this integral is taken to be $0$.

Formalized by `MathlibExt.Analysis.HausdorffMomentsWanted.Analysis.momentOf`, a definition declared in [WantedExt/Analysis/HausdorffMomentsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffMomentsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#moment-of-2).

## Moment sequences of signed measures on the cube

A real sequence $a$ indexed by
$\mathbb{N}^d$ is a moment configuration if there are finite measures $\mu$ and $\nu$ on
$\mathbb{R}^d$ such that for every multi-index $n \in \mathbb{N}^d$,

$$a_n = \int_{[0,1]^d} x^n \, d\mu(x) - \int_{[0,1]^d} x^n \, d\nu(x),$$

where $x^n = \prod_i x_i^{n_i}$.

This encodes a signed measure of bounded variation on the cube by its Jordan decomposition
$\mu - \nu$.

Formalized by `MathlibExt.Analysis.HausdorffMomentsWanted.Analysis.IsMomentConfiguration`, a definition declared in [WantedExt/Analysis/HausdorffMomentsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffMomentsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#is-moment-configuration).

## Multi-index binomial coefficient

For multi-indices $n, k \in \mathbb{N}^d$, the binomial
coefficient $\binom{n}{k}$ is the natural number $\prod_i \binom{n_i}{k_i}$.

Formalized by `MathlibExt.Analysis.HausdorffMomentsWanted.Analysis.multiChoose`, a definition declared in [WantedExt/Analysis/HausdorffMomentsWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffMomentsWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#multi-choose-2).

## Iterated backward difference

For a real sequence $a$ indexed by $\mathbb{N}^d$ and
multi-indices $k, n \in \mathbb{N}^d$, the iterated backward difference of $a$ is the real number

$$(\Delta^k a)_n = \sum_{j \le k} (-1)^{|k| - |j|} \binom{k}{j} a_{n - j},$$

where $j$ ranges over the multi-indices with $j \le k$ coordinatewise, $|j| = \sum_i j_i$,
$\binom{k}{j} = \prod_i \binom{k_i}{j_i}$, and $n - j$ is computed coordinatewise in $\mathbb{N}$,
with $n_i - j_i = 0$ when $j_i > n_i$.

For $k \le n$ no truncation occurs, and $\Delta^k a$ is the iterate of the backward partial
differences $(\Delta_i a)_n = a_{n - e_i} - a_n$, applied $k_i$ times in each coordinate $i$,
where $e_i \in \mathbb{N}^d$ is the $i$-th unit multi-index.

Formalized by `MathlibExt.Analysis.HausdorffMomentsWanted.Analysis.diff`, a definition declared in [WantedExt/Analysis/HausdorffMomentsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffMomentsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#diff-2).

## Hausdorff-bounded sequences

A real sequence $a$ indexed by $\mathbb{N}^d$ is Hausdorff
bounded if there is a real constant $M$ such that for every multi-index $n \in \mathbb{N}^d$,

$$\sum_{k \le n} \left| \binom{n}{k} (\Delta^k a)_n \right| \le M,$$

where $k$ ranges over the multi-indices with $k \le n$ coordinatewise,
$\binom{n}{k} = \prod_i \binom{n_i}{k_i}$ is the multi-index binomial coefficient, and
$\Delta^k a$ is the iterated backward difference of $a$.

Formalized by `MathlibExt.Analysis.HausdorffMomentsWanted.Analysis.HausdorffBounded`, a definition declared in [WantedExt/Analysis/HausdorffMomentsWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffMomentsWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#hausdorff-bounded).

## Moment sequences of positive measures on the cube

A real sequence $a$ indexed by
$\mathbb{N}^d$ is a positive moment configuration if there is a finite measure $\mu$ on
$\mathbb{R}^d$ such that $a_n = \int_{[0,1]^d} x^n \, d\mu(x)$ for every multi-index
$n \in \mathbb{N}^d$, where $x^n = \prod_i x_i^{n_i}$.

Formalized by `MathlibExt.Analysis.HausdorffMomentsWanted.Analysis.IsPositiveMomentConfiguration`, a definition declared in [WantedExt/Analysis/HausdorffMomentsWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffMomentsWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#is-positive-moment-configuration).

## Hausdorff–Hildebrandt–Schoenberg moment theorem

A real sequence $a$ indexed by
$\mathbb{N}^d$ is a moment configuration, that is, there are finite measures $\mu$ and $\nu$ on
$\mathbb{R}^d$ with $a_n = \int_{[0,1]^d} x^n \, d\mu(x) - \int_{[0,1]^d} x^n \, d\nu(x)$ for every
multi-index $n \in \mathbb{N}^d$, where $x^n = \prod_i x_i^{n_i}$, if and only if $a$ is Hausdorff
bounded.

## Sources

- F. Hausdorff (1921, 1923); T. H. Hildebrandt and I. J. Schoenberg, *On linear functional operations and the moment problem for a finite interval in one or several dimensions*, Ann. of Math. 34 (1933). Knill, *Some fundamental theorems in mathematics*, §115. Problem `hausdorff_hildebrandt_schoenberg` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.HausdorffMomentsWanted.Analysis.hausdorff_hildebrandt_schoenberg` is written with `theorem_wanted` in [WantedExt/Analysis/HausdorffMomentsWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffMomentsWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#hausdorff-hildebrandt-schoenberg).

## Hausdorff positivity criterion

A real sequence $a$ indexed by $\mathbb{N}^d$ is a positive
moment configuration, that is, there is a finite measure $\mu$ on $\mathbb{R}^d$ with
$a_n = \int_{[0,1]^d} x^n \, d\mu(x)$ for every multi-index $n \in \mathbb{N}^d$, where
$x^n = \prod_i x_i^{n_i}$, if and only if $(\Delta^k a)_n \ge 0$ for all multi-indices $k, n$ with
$k \le n$ coordinatewise, where $\Delta^k a$ is the iterated backward difference of $a$.

## Sources

- F. Hausdorff, *Summationsmethoden und Momentfolgen I, II*, Math. Z. 9 (1921). Knill, *Some fundamental theorems in mathematics*, §115. Problem `hausdorff_positivity_criterion` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.HausdorffMomentsWanted.Analysis.hausdorff_positivity` is written with `theorem_wanted` in [WantedExt/Analysis/HausdorffMomentsWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HausdorffMomentsWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html#hausdorff-positivity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hausdorff moment problem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/integral-transforms/hausdorff-moment-problem)
