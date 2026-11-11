---
declaration: section
origin: cited
lean: MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.rootCount, MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.n, MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.sphericalDensity, MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.A, MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.IsNonconstant, MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.HasBoundedRootCounts, MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.conjecture, MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.conjecture_refuted
statement: formalized
---

# Spherical area and valence of meromorphic functions

8 results, 7 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/spherical-area-and-valence-of-meromorphic-functi/index.html).

## Root count

For $f\colon \mathbb{C} \to \mathbb{C}$, $a \in \mathbb{C}$ and real $r$, the
root count of $f$ at $a$ in radius $r$ is the number of roots of $f(z) = a$ in the open disk
$|z| < r$, counted with multiplicity: the sum over $z \in \mathbb{C}$ of the positive part of
the divisor of $f - a$ on that disk at $z$ (the sum is taken to be $0$ if infinitely many terms
are nonzero).

Formalized by `MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.rootCount`, a definition declared in [WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/spherical-area-and-valence-of-meromorphic-functi/index.html#root-count).

## Maximum valence

For $f\colon \mathbb{C} \to \mathbb{C}$ and real $r$, $n(f, r)$ is the
supremum in $\mathbb{R}$, over all $a \in \mathbb{C}$, of the root count of $f$ at $a$ in radius
$r$, that is, of the number of roots of $f(z) = a$ in $|z| < r$ counted with multiplicity.

This is a conditional supremum of real numbers, so it is meaningful only when these root counts
are bounded above as $a$ varies; see bounded root counts.

Formalized by `MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.n`, a definition declared in [WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/spherical-area-and-valence-of-meromorphic-functi/index.html#n).

## Spherical density

For $f\colon \mathbb{C} \to \mathbb{C}$ and $z \in \mathbb{C}$, the
spherical density of $f$ at $z$ is $|f'(z)|^2 / (1 + |f(z)|^2)^2$, where $f'(z)$ is the complex
derivative of $f$ at $z$, taken to be $0$ where $f$ is not differentiable.

Formalized by `MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.sphericalDensity`, a definition declared in [WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/spherical-area-and-valence-of-meromorphic-functi/index.html#spherical-density).

## Normalized spherical area

For $f\colon \mathbb{C} \to \mathbb{C}$ and real $r$, the
normalized spherical area $A(f, r)$ of $f$ on the disk $|z| < r$ is $\frac{1}{\pi}$ times the
Lebesgue integral of the spherical density of $f$ over the open disk
$\{z \in \mathbb{C} : |z| < r\}$ (the integral is taken to be $0$ if the density is not
integrable there).

Formalized by `MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.A`, a definition declared in [WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/spherical-area-and-valence-of-meromorphic-functi/index.html#a).

## Germ-wise nonconstant function

A function $f\colon \mathbb{C} \to \mathbb{C}$ is
nonconstant if there are points $u, v \in \mathbb{C}$ at which $f$ is complex differentiable and
$f(u) \ne f(v)$.

This excludes pointwise-modified constant functions (for example $f(0) = 1$ and $f(z) = 0$ for
$z \ne 0$), which are meromorphic with zero derivative density but represent the constant zero
germ.

Formalized by `MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.IsNonconstant`, a definition declared in [WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/spherical-area-and-valence-of-meromorphic-functi/index.html#is-nonconstant).

## Bounded root counts

A function $f\colon \mathbb{C} \to \mathbb{C}$ has bounded root
counts if for every real $r$ the root counts of $f$ in radius $r$, that is, the numbers of roots
of $f(z) = a$ in $|z| < r$ counted with multiplicity, are bounded above as $a$ ranges over
$\mathbb{C}$.

This guarantees that the supremum over $a$ defining the maximum valence of $f$ in radius $r$ is
taken over a bounded set.

Formalized by `MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.HasBoundedRootCounts`, a definition declared in [WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/spherical-area-and-valence-of-meromorphic-functi/index.html#has-bounded-root-counts).

## Hayman's spherical-area ratio conjecture

The statement that every function
$f\colon \mathbb{C} \to \mathbb{C}$ that is meromorphic on all of $\mathbb{C}$ and nonconstant
(complex differentiable at two points where it takes different values) has bounded root counts
(for every real $r$, the numbers of roots of $f(z) = a$ in $|z| < r$, counted with
multiplicity, are bounded above as $a$ ranges over $\mathbb{C}$) and satisfies

$$\liminf_{r \to \infty} \frac{n(f, r)}{A(f, r)} = 1,$$

where $n(f, r)$ is the supremum over $a \in \mathbb{C}$ of the number of roots of $f(z) = a$ in
$|z| < r$ counted with multiplicity, and $A(f, r)$ is the normalized spherical area of $f$ on
$|z| < r$.

For such $f$ it is known that $1 \le \liminf_{r \to \infty} n(f, r)/A(f, r) \le e$; Hayman asked
whether $e$ can be replaced by $1$. The statement is recorded as a proposition and is not
asserted.

## Sources

- problem record AMR-022-1016 (W. K. Hayman).

Formalized by `MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.conjecture`, a definition declared in [WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/spherical-area-and-valence-of-meromorphic-functi/index.html#conjecture).

## Hayman's spherical-area ratio conjecture is false

Not every function
$f\colon \mathbb{C} \to \mathbb{C}$ that is meromorphic on all of $\mathbb{C}$ and nonconstant
(complex differentiable at two points where it takes different values) has bounded root counts
and satisfies $\liminf_{r \to \infty} n(f, r)/A(f, r) = 1$, where $n(f, r)$ is the maximum
valence and $A(f, r)$ the normalized spherical area of $f$ on the disk $|z| < r$.

Toppila constructed a nonconstant meromorphic function $f$ with
$\liminf_{r \to \infty} n(f, r)/A(f, r) \ge 80/79$, and Hinkkanen and Miles (arXiv:2401.13808,
2024, Theorem 1.1) give one with $\liminf_{r \to \infty} n(f, r)/A(f, r) \ge 1.07328$.

## Sources

- A. Hinkkanen and J. Miles, Maximum and Average Valence of Meromorphic Functions, arXiv preprint (2024), arXiv:2401.13808, https://arxiv.org/abs/2401.13808.

Stated but not proved: `MathlibExt.Analysis.HaymanSphericalAreaRatioWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanSphericalAreaRatioWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/spherical-area-and-valence-of-meromorphic-functi/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spherical area and valence of meromorphic functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/spherical-area-and-valence-of-meromorphic-functi/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/entire-functions/spherical-area-and-valence-of-meromorphic-functi)
