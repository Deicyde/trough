---
declaration: section
origin: cited
lean: abelPartialSum, abelSummatory, abelContinuation, abelSummatory_eq_zero_of_lt_one, locallyIntegrableOn_abelSummatory, isBigO_abelSummatory_atTop, isBigO_abelSummatory_nhdsGT_zero, abelContinuation_eq_mul_mellin
statement: formalized
proof: formalized
---

# Analytic continuation of Dirichlet series

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html).

## Partial sums of a coefficient sequence

For $f : \mathbb{N} \to \mathbb{C}$ and
$n \in \mathbb{N}$, the one-based partial sum is $A(n) = \sum_{k=1}^{n} f(k)$; in particular
$A(0) = 0$ and the value $f(0)$ is never used.

Formalized by `abelPartialSum`, a definition declared in [MathlibExt/NumberTheory/LSeries/AbelContinuation.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AbelContinuation.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#abel-partial-sum).

## Summatory step function

For $f : \mathbb{N} \to \mathbb{C}$ with partial sums
$A(n) = \sum_{k=1}^{n} f(k)$, the summatory step function of $f$ is the function
$S : \mathbb{R} \to \mathbb{C}$ with $S(t) = A(\lfloor t \rfloor)$ for $t \ge 0$ and $S(t) = 0$
for $t < 0$. Equivalently, $S(t) = \sum_{1 \le k \le t} f(k)$ for every real $t$.

Formalized by `abelSummatory`, a definition declared in [MathlibExt/NumberTheory/LSeries/AbelContinuation.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AbelContinuation.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#abel-summatory).

## Abel continuation of a Dirichlet series

For $f : \mathbb{N} \to \mathbb{C}$ with partial
sums $A(n) = \sum_{k=1}^{n} f(k)$, the Abel continuation of $f$ is the function
$F_f : \mathbb{C} \to \mathbb{C}$ given by

$$F_f(s) = s \int_1^\infty A(\lfloor t \rfloor)\, t^{-s-1}\, dt,$$

where the integral is taken to be $0$ when the integrand is not integrable on $(1, \infty)$.

Formalized by `abelContinuation`, a definition declared in [MathlibExt/NumberTheory/LSeries/AbelContinuation.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AbelContinuation.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#abel-continuation).

## The summatory step function vanishes below one

For $f : \mathbb{N} \to \mathbb{C}$, the
summatory step function $S(t) = \sum_{1 \le k \le t} f(k)$ satisfies $S(t) = 0$ for every real
$t < 1$.

Formalized by `abelSummatory_eq_zero_of_lt_one`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AbelContinuation.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AbelContinuation.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#abel-summatory-eq-zero-of-lt-one).

## Local integrability of the summatory function

For every $f : \mathbb{N} \to \mathbb{C}$,
the summatory step function $t \mapsto \sum_{k=1}^{\lfloor t \rfloor} f(k)$ on $\mathbb{R}$ is
locally integrable on the open half-line $(0, \infty)$: every $t > 0$ has a neighbourhood
within $(0, \infty)$ on which this function is Lebesgue integrable.

Formalized by `locallyIntegrableOn_abelSummatory`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AbelContinuation.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AbelContinuation.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#locally-integrable-on-abel-summatory).

## Growth of the summatory step function

Let $f : \mathbb{N} \to \mathbb{C}$ have partial
sums $A(n) = \sum_{k=1}^{n} f(k)$ and summatory step function
$S(t) = \sum_{1 \le k \le t} f(k)$, and let $\sigma$ be any real number with
$A(n) = O(n^\sigma)$ as $n \to \infty$. Then $S(t) = O(t^\sigma)$ as $t \to \infty$ through the
reals.

No sign condition on $\sigma$ is needed.

Formalized by `isBigO_abelSummatory_atTop`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AbelContinuation.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AbelContinuation.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#is-big-o-abel-summatory-at-top).

## The summatory step function is negligible near zero

Let $f : \mathbb{N} \to \mathbb{C}$
have summatory step function $S(t) = \sum_{1 \le k \le t} f(k)$. For every real $b$,
$S(t) = O(t^{-b})$ as $t \to 0^+$.

This holds because $S$ vanishes on $(0, 1)$.

Formalized by `isBigO_abelSummatory_nhdsGT_zero`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AbelContinuation.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AbelContinuation.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#is-big-o-abel-summatory-nhds-gt-zero).

## The Abel continuation as a Mellin transform

Let $f : \mathbb{N} \to \mathbb{C}$ have
partial sums $A(n) = \sum_{k=1}^{n} f(k)$ and summatory step function
$S(t) = \sum_{1 \le k \le t} f(k)$ for real $t$, and let $\sigma$ be a real number with
$A(n) = O(n^\sigma)$ as $n \to \infty$. Then for every $s \in \mathbb{C}$ with
$\operatorname{Re} s > \sigma$, the Abel continuation satisfies $F_f(s) = s\,\mathcal{M}S(-s)$,
where $\mathcal{M}S(z) = \int_0^\infty t^{z-1} S(t)\,dt$ is the Mellin transform of $S$.

This identity transfers holomorphy of the Mellin transform to the continuation.

Formalized by `abelContinuation_eq_mul_mellin`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AbelContinuation.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AbelContinuation.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#abel-continuation-eq-mul-mellin).

## Complex differentiability of the Abel continuation

Let $f : \mathbb{N} \to \mathbb{C}$
have partial sums $A(n) = \sum_{k=1}^{n} f(k)$, and let $\sigma$ be a real number with
$A(n) = O(n^\sigma)$ as $n \to \infty$. Then the Abel continuation $F_f$ of $f$ is complex
differentiable at every $s \in \mathbb{C}$ with $\operatorname{Re} s > \sigma$.

The proof uses holomorphy of the Mellin transform of the summatory step function at $-s$.

Formalized by `differentiableAt_abelContinuation`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AbelContinuation.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AbelContinuation.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#differentiable-at-abel-continuation).

## Analyticity of the Abel continuation

Let $f : \mathbb{N} \to \mathbb{C}$ have partial sums
$A(n) = \sum_{k=1}^{n} f(k)$, and let $\sigma$ be a real number with $A(n) = O(n^\sigma)$ as
$n \to \infty$. Then the Abel continuation $F_f$ of $f$ is analytic on the half-plane
$\{s \in \mathbb{C} : \operatorname{Re} s > \sigma\}$.

Formalized by `analyticOn_abelContinuation`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AbelContinuation.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AbelContinuation.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#analytic-on-abel-continuation).

## Abel continuation agrees with the Dirichlet series

Let $f : \mathbb{N} \to \mathbb{C}$
have partial sums $A(n) = \sum_{k=1}^{n} f(k)$, let $\sigma \ge 0$ be a real number with
$A(n) = O(n^\sigma)$ as $n \to \infty$, and let $s$ be a complex number with
$\operatorname{Re} s > \sigma$ at which the Dirichlet series $\sum_{n \ge 1} f(n) n^{-s}$
converges absolutely. Then the Abel continuation $F_f$ of $f$ satisfies
$F_f(s) = \sum_{n=1}^{\infty} f(n) n^{-s}$.

The hypothesis $\sigma \ge 0$ is inherited from the integral representation of the Dirichlet
series used in the proof.

Formalized by `abelContinuation_eq_LSeries`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AbelContinuation.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AbelContinuation.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#abel-continuation-eq-lseries).

## Abel continuation as the limit of Dirichlet partial sums

Let
$f : \mathbb{N} \to \mathbb{C}$ with partial sums $A(n) = \sum_{k=1}^{n} f(k)$, let $\sigma$ be a
real number and let $s$ be a complex number with $\sigma < \operatorname{Re} s$. If
$A(n) = O(n^\sigma)$ as $n \to \infty$, then the partial sums $\sum_{n=1}^{N} f(n) n^{-s}$ converge,
as $N \to \infty$, to the Abel continuation $F_f(s)$ of $f$ at $s$.

No summability of the Dirichlet series is assumed: the convergence may be conditional.

Formalized by `tendsto_abelContinuation_Icc`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AbelContinuation.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AbelContinuation.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#tendsto-abel-continuation-icc).

## Linear asymptotic Dirichlet continuation

For $a : \mathbb{N} \to \mathbb{C}$ and
$\rho \in \mathbb{C}$, the linear asymptotic Dirichlet continuation of $a$ with constant $\rho$ is
the function $L_{a,\rho} : \mathbb{C} \to \mathbb{C}$ given by
$L_{a,\rho}(s) = \rho\,\zeta(s) + F_{a-\rho}(s)$, where $\zeta$ is the Riemann zeta function and
$F_{a-\rho}$ is the Abel continuation of the sequence $n \mapsto a(n) - \rho$.

For $\rho \neq 0$ the term $\rho\,\zeta(s)$ carries the pole at $s = 1$, and $F_{a-\rho}$
continues the remainder. At $s = 1$ the formula uses the finite value that Mathlib assigns to
$\zeta(1)$.

Formalized by `linearAsymptoticDirichletContinuation`, a definition declared in [MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#linear-asymptotic-dirichlet-continuation).

## Partial sums after subtracting a constant

For $a : \mathbb{N} \to \mathbb{C}$,
$\rho \in \mathbb{C}$ and $n \in \mathbb{N}$, the one-based partial sum
$\sum_{k=1}^{n} (a(k) - \rho)$ equals $\sum_{k=1}^{n} a(k) - n\rho$.

Formalized by `abelPartialSum_sub_const`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#abel-partial-sum-sub-const).

## Growth bound for the partial sums of a shifted sequence

Let
$a : \mathbb{N} \to \mathbb{C}$, $\rho \in \mathbb{C}$ and $\sigma \in \mathbb{R}$. If the one-based
partial sums $A(n) = \sum_{k=1}^{n} a(k)$ satisfy $A(n) - n\rho = O(n^{\sigma})$ as
$n \to \infty$, then $\sum_{k=1}^{n} (a(k) - \rho) = O(n^{\sigma})$ as $n \to \infty$.

Formalized by `isBigO_abelPartialSum_sub_const`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#is-big-o-abel-partial-sum-sub-const).

## Analyticity of the linear asymptotic continuation away from $1$

Let
$a : \mathbb{N} \to \mathbb{C}$, $\rho \in \mathbb{C}$ and $\sigma \in \mathbb{R}$, and suppose
that the one-based partial sums $A(n) = \sum_{k=1}^{n} a(k)$ satisfy
$A(n) - n\rho = O(n^{\sigma})$ as $n \to \infty$. Then the linear asymptotic Dirichlet
continuation $L_{a,\rho}$ of $a$ with constant $\rho$ is complex analytic at every
$s \in \mathbb{C}$ with $\operatorname{Re} s > \sigma$ and $s \neq 1$.

Formalized by `analyticAt_linearAsymptoticDirichletContinuation_of_ne_one`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#analytic-at-linear-asymptotic-dirichlet).

## Cleared-denominator form of the linear asymptotic continuation

Let
$a : \mathbb{N} \to \mathbb{C}$ and $\rho \in \mathbb{C}$, let $L_{a,\rho}$ be the linear
asymptotic Dirichlet continuation of $a$ with constant $\rho$, and let $F_{a-\rho}$ be the Abel
continuation of the sequence $n \mapsto a(n) - \rho$. Let $\zeta_1 : \mathbb{C} \to \mathbb{C}$ be
the function with $\zeta_1(s) = (s - 1)\,\zeta(s)$ for $s \neq 1$ and $\zeta_1(1) = 1$, where
$\zeta$ is the Riemann zeta function. Then for every $s \in \mathbb{C}$ with $s \neq 1$,

$$
L_{a,\rho}(s) = (s - 1)^{-1} \bigl(\rho\,\zeta_1(s) + (s - 1)\,F_{a-\rho}(s)\bigr).
$$

Formalized by `linearAsymptoticDirichletContinuation_eq_inv_sub_mul`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#linear-asymptotic-dirichlet-continuation-2).

## Meromorphy of the linear asymptotic continuation at $1$

Let
$a : \mathbb{N} \to \mathbb{C}$, $\rho \in \mathbb{C}$ and $\sigma \in \mathbb{R}$ with
$\sigma < 1$, and suppose that the one-based partial sums $A(n) = \sum_{k=1}^{n} a(k)$ satisfy
$A(n) - n\rho = O(n^{\sigma})$ as $n \to \infty$. Then the linear asymptotic Dirichlet
continuation $L_{a,\rho}$ of $a$ with constant $\rho$ is meromorphic at $s = 1$.

Formalized by `meromorphicAt_linearAsymptoticDirichletContinuation_one`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#meromorphic-at-linear-asymptotic-dirichl).

## The linear asymptotic continuation has a simple pole at $1$

Let
$a : \mathbb{N} \to \mathbb{C}$, $\rho \in \mathbb{C}$ with $\rho \neq 0$ and
$\sigma \in \mathbb{R}$ with $\sigma < 1$, and suppose that the one-based partial sums
$A(n) = \sum_{k=1}^{n} a(k)$ satisfy $A(n) - n\rho = O(n^{\sigma})$ as $n \to \infty$. Then the
meromorphic order at $s = 1$ of the linear asymptotic Dirichlet continuation $L_{a,\rho}$ of $a$
with constant $\rho$ is $-1$.

Formalized by `meromorphicOrderAt_linearAsymptoticDirichletContinuation_one`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#meromorphic-order-at-linear-asymptotic-d).

## Limit of the linear asymptotic continuation times $s - 1$ at $1$

Let
$a : \mathbb{N} \to \mathbb{C}$, $\rho \in \mathbb{C}$ and $\sigma \in \mathbb{R}$ with
$\sigma < 1$, and suppose that the one-based partial sums $A(n) = \sum_{k=1}^{n} a(k)$ satisfy
$A(n) - n\rho = O(n^{\sigma})$ as $n \to \infty$. Let $L_{a,\rho}$ be the linear asymptotic
Dirichlet continuation of $a$ with constant $\rho$. Then $(s - 1)\,L_{a,\rho}(s) \to \rho$ as
$s \to 1$ with $s \neq 1$.

Formalized by `tendsto_sub_one_mul_linearAsymptoticDirichletContinuation`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#tendsto-sub-one-mul-linear-asymptotic-di).

## Meromorphy of the linear asymptotic continuation on a half-plane

Let
$a : \mathbb{N} \to \mathbb{C}$, $\rho \in \mathbb{C}$ and $\sigma \in \mathbb{R}$ with
$\sigma < 1$, and suppose that the one-based partial sums $A(n) = \sum_{k=1}^{n} a(k)$ satisfy
$A(n) - n\rho = O(n^{\sigma})$ as $n \to \infty$. Then the linear asymptotic Dirichlet
continuation $L_{a,\rho}$ of $a$ with constant $\rho$ is meromorphic at every point of the
half-plane $\{s \in \mathbb{C} : \operatorname{Re} s > \sigma\}$.

Formalized by `meromorphicOn_linearAsymptoticDirichletContinuation`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#meromorphic-on-linear-asymptotic-dirichl).

## Convergence of the Dirichlet series to the linear asymptotic continuation

Let
$a : \mathbb{N} \to \mathbb{C}$, $\rho \in \mathbb{C}$ and $\sigma \in \mathbb{R}$ with
$\sigma < 1$, and suppose that the one-based partial sums $A(n) = \sum_{k=1}^{n} a(k)$ satisfy
$A(n) - n\rho = O(n^{\sigma})$ as $n \to \infty$. Then for every $s \in \mathbb{C}$ with
$\operatorname{Re} s > 1$, the partial sums $\sum_{n=1}^{N} a(n)\, n^{-s}$ converge, as
$N \to \infty$, to $L_{a,\rho}(s)$, where $L_{a,\rho}$ is the linear asymptotic Dirichlet
continuation of $a$ with constant $\rho$.

Formalized by `tendsto_linearAsymptoticDirichletContinuation_Icc`, a theorem declared in [MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/AsymptoticContinuation.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html#tendsto-linear-asymptotic-dirichlet-cont).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Analytic continuation of Dirichlet series](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/analytic-continuation-of-dirichlet-series)
