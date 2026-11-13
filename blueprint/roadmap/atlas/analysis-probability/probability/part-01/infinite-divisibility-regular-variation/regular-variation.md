---
declaration: section
origin: cited
lean: MathlibExt.Probability.RegularVariation.IsSlowlyVarying, MathlibExt.Probability.RegularVariation.IsSlowlyVarying.of_tendsto, MathlibExt.Probability.RegularVariation.isSlowlyVarying_one, MathlibExt.Probability.RegularVariation.isSlowlyVarying_const, MathlibExt.Probability.RegularVariation.IsSlowlyVarying.mul, MathlibExt.Probability.RegularVariation.IsSlowlyVarying.const_mul, MathlibExt.Probability.RegularVariation.isSlowlyVarying_one_add_inv, MathlibExt.Probability.RegularVariation.IsSlowlyVarying.of_eventuallyEq
statement: formalized
proof: formalized
---

# Regular variation

37 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html).

## Slowly varying function

A function $L : \mathbb{R} \to \mathbb{R}$ is slowly varying (at
infinity) if $L(x) > 0$ for all sufficiently large $x$ and, for every real $c > 0$,
$L(cx) / L(x) \to 1$ as $x \to \infty$.

Formalized by `MathlibExt.Probability.RegularVariation.IsSlowlyVarying`, a definition declared in [MathlibExt/Probability/RegularVariation.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#is-slowly-varying).

## Functions with a positive limit are slowly varying

Let $L : \mathbb{R} \to \mathbb{R}$ and
$a > 0$. If $L(x) > 0$ for all sufficiently large $x$ and $L(x) \to a$ as $x \to \infty$, then
$L$ is slowly varying.

Indeed, for every $c > 0$ the ratio $L(cx) / L(x)$ tends to $a / a = 1$.

Formalized by `MathlibExt.Probability.RegularVariation.IsSlowlyVarying.of_tendsto`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#of-tendsto).

## The constant function one is slowly varying

The constant function $x \mapsto 1$ on
$\mathbb{R}$ is slowly varying.

Formalized by `MathlibExt.Probability.RegularVariation.isSlowlyVarying_one`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#is-slowly-varying-one).

## Positive constants are slowly varying

For every real $c > 0$, the constant function
$x \mapsto c$ on $\mathbb{R}$ is slowly varying.

Formalized by `MathlibExt.Probability.RegularVariation.isSlowlyVarying_const`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#is-slowly-varying-const).

## Products of slowly varying functions

If $L_1, L_2 : \mathbb{R} \to \mathbb{R}$ are
slowly varying, then so is their pointwise product $x \mapsto L_1(x) L_2(x)$.

Formalized by `MathlibExt.Probability.RegularVariation.IsSlowlyVarying.mul`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#mul).

## Positive multiples of slowly varying functions

If $L : \mathbb{R} \to \mathbb{R}$ is slowly
varying and $c > 0$, then $x \mapsto c L(x)$ is slowly varying.

Formalized by `MathlibExt.Probability.RegularVariation.IsSlowlyVarying.const_mul`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#const-mul).

## The function $1 + (1 + x)^{-1}$ is slowly varying

The function
$x \mapsto 1 + (1 + x)^{-1}$ on $\mathbb{R}$ is slowly varying; it tends to the positive limit $1$
at infinity.

Formalized by `MathlibExt.Probability.RegularVariation.isSlowlyVarying_one_add_inv`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#is-slowly-varying-one-add-inv).

## Slow variation is preserved by eventual equality

Let $f, g : \mathbb{R} \to \mathbb{R}$.
If $f$ is slowly varying and $f(x) = g(x)$ for all sufficiently large $x$, then $g$ is slowly
varying.

Formalized by `MathlibExt.Probability.RegularVariation.IsSlowlyVarying.of_eventuallyEq`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#of-eventually-eq).

## Regularly varying function

A function $f : \mathbb{R} \to \mathbb{R}$ is regularly varying
with index $\rho \in \mathbb{R}$ if there is a slowly varying function
$L : \mathbb{R} \to \mathbb{R}$ such that $f(x) = x^{\rho} L(x)$ for all sufficiently large $x$.

Formalized by `MathlibExt.Probability.RegularVariation.IsRegularlyVarying`, a definition declared in [MathlibExt/Probability/RegularVariation.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#is-regularly-varying).

## Powers are regularly varying

For every real number $\rho$, the function $x \mapsto x^\rho$
on $\mathbb{R}$ is regularly varying with index $\rho$.

The slowly varying factor can be taken to be the constant function $1$.

Formalized by `MathlibExt.Probability.RegularVariation.isRegularlyVarying_rpow`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#is-regularly-varying-rpow).

## Products of regularly varying functions

If $f : \mathbb{R} \to \mathbb{R}$ is regularly
varying with index $\rho$ and $g : \mathbb{R} \to \mathbb{R}$ is regularly varying with index
$\sigma$, then the pointwise product $fg$ is regularly varying with index $\rho + \sigma$.

Formalized by `MathlibExt.Probability.RegularVariation.IsRegularlyVarying.mul`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#mul-2).

## Positive multiples of regularly varying functions

If $f : \mathbb{R} \to \mathbb{R}$ is
regularly varying with index $\rho$ and $c > 0$, then $x \mapsto c f(x)$ is regularly varying
with index $\rho$.

Formalized by `MathlibExt.Probability.RegularVariation.IsRegularlyVarying.const_mul`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#const-mul-2).

## Positive multiples of powers are regularly varying

For real numbers $c > 0$ and $\rho$, the
function $x \mapsto c x^\rho$ on $\mathbb{R}$ is regularly varying with index $\rho$.

Formalized by `MathlibExt.Probability.RegularVariation.isRegularlyVarying_const_mul_rpow`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#is-regularly-varying-const-mul-rpow).

## Regular variation is preserved by eventual equality

Let $f, g : \mathbb{R} \to \mathbb{R}$
and $\rho \in \mathbb{R}$. If $f$ is regularly varying with index $\rho$ and $f(x) = g(x)$ for
all sufficiently large $x$, then $g$ is regularly varying with index $\rho$.

Formalized by `MathlibExt.Probability.RegularVariation.IsRegularlyVarying.of_eventuallyEq`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#of-eventually-eq-2).

## Regularly varying functions are eventually positive

If $f : \mathbb{R} \to \mathbb{R}$ is
regularly varying with some index $\rho$, then $f(x) > 0$ for all sufficiently large $x$.

Formalized by `MathlibExt.Probability.RegularVariation.IsRegularlyVarying.eventually_pos`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#eventually-pos).

## Right tail of a measure

For a measure $\mu$ on $\mathbb{R}$ and $x \in \mathbb{R}$,
the right tail of $\mu$ at $x$ is the real number $\mu((x, \infty))$ when
$\mu((x, \infty)) < \infty$, and $0$ when $\mu((x, \infty)) = \infty$.

For a finite measure $\mu$ it is the mass of the open half-line $(x, \infty)$.

Formalized by `MathlibExt.Probability.RegularVariation.rightTail`, a definition declared in [MathlibExt/Probability/RegularVariation.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#right-tail).

## Left tail of a measure

For a measure $\mu$ on $\mathbb{R}$ and a real $x$, the left tail of
$\mu$ at $x$ is the real number $\mu((-\infty, -x))$, where an infinite value is sent to $0$.

For a finite measure it is the mass of the strict left tail $(-\infty, -x)$.

Formalized by `MathlibExt.Probability.RegularVariation.leftTail`, a definition declared in [MathlibExt/Probability/RegularVariation.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#left-tail).

## Combined tail of a measure

For a measure $\mu$ on $\mathbb{R}$ and a real number $x$,
the combined tail of $\mu$ at $x$ is the real number $\mu((x, \infty)) + \mu((-\infty, -x))$,
where each of the two measures is converted from $[0, \infty]$ to a real number, an infinite
value becoming $0$.

For a finite measure and $x \ge 0$ this equals $\mu(\{y : |y| > x\})$. At negative thresholds
the two intervals can overlap, so the combined tail is not the mass of the absolute tail.

Formalized by `MathlibExt.Probability.RegularVariation.combinedTail`, a definition declared in [MathlibExt/Probability/RegularVariation.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#combined-tail).

## The right tail of a probability measure is at most one

For every probability measure
$\mu$ on $\mathbb{R}$ and every $x \in \mathbb{R}$, the right tail of $\mu$ at $x$ is at most
$1$.

Formalized by `MathlibExt.Probability.RegularVariation.rightTail_le_one`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#right-tail-le-one).

## The left tail of a probability measure is at most one

For every probability measure $\mu$
on $\mathbb{R}$ and every real $x$, the left tail of $\mu$ at $x$ is at most $1$.

Formalized by `MathlibExt.Probability.RegularVariation.leftTail_le_one`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#left-tail-le-one).

## The combined tail of a probability measure is at most two

For every probability measure
$\mu$ on $\mathbb{R}$ and every real number $x$, the combined tail of $\mu$ at $x$ satisfies
$\mu((x, \infty)) + \mu((-\infty, -x)) \le 2$.

Formalized by `MathlibExt.Probability.RegularVariation.combinedTail_le_two`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#combined-tail-le-two).

## The right tail of a finite measure is antitone

Let $\mu$ be a finite measure on
$\mathbb{R}$. If $x \le y$, then the right tail of $\mu$ at $y$ is at most the right tail of
$\mu$ at $x$.

Formalized by `MathlibExt.Probability.RegularVariation.rightTail_antitone`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#right-tail-antitone).

## Monotonicity of the left tail

For every finite measure $\mu$ on $\mathbb{R}$, the left tail
of $\mu$ is antitone in the threshold: if $a \le b$, then
$\mu((-\infty, -b)) \le \mu((-\infty, -a))$.

Formalized by `MathlibExt.Probability.RegularVariation.leftTail_antitone`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#left-tail-antitone).

## The combined tail is antitone

Let $\mu$ be a finite measure on $\mathbb{R}$ and write
$T(x) = \mu((x, \infty)) + \mu((-\infty, -x))$ for its combined tail at a real number $x$. Then
$T$ is antitone: $T(b) \le T(a)$ whenever $a \le b$.

Formalized by `MathlibExt.Probability.RegularVariation.combinedTail_antitone`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#combined-tail-antitone).

## The right tail is at most the combined tail

For every measure $\mu$ on $\mathbb{R}$ and
every $x \in \mathbb{R}$, the right tail of $\mu$ at $x$ is at most the combined tail of $\mu$
at $x$.

Formalized by `MathlibExt.Probability.RegularVariation.rightTail_le_combinedTail`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#right-tail-le-combined-tail).

## The left tail is at most the combined tail

For every measure $\mu$ on $\mathbb{R}$ and
every real $x$, the left tail of $\mu$ at $x$ is at most the combined tail of $\mu$ at $x$.

Formalized by `MathlibExt.Probability.RegularVariation.leftTail_le_combinedTail`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#left-tail-le-combined-tail).

## The right tail of a finite measure vanishes at infinity

For every finite measure $\mu$
on $\mathbb{R}$, the right tail $\mu((x, \infty))$, taken as a real number, tends to $0$ as
$x \to \infty$.

Formalized by `MathlibExt.Probability.RegularVariation.tendsto_rightTail_atTop`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#tendsto-right-tail-at-top).

## The left tail of a finite measure vanishes at infinity

For every finite measure $\mu$
on $\mathbb{R}$, the left tail $\mu((-\infty, -x))$, taken as a real number, tends to $0$ as
$x \to \infty$.

Formalized by `MathlibExt.Probability.RegularVariation.tendsto_leftTail_atTop`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#tendsto-left-tail-at-top).

## The combined tail of a finite measure vanishes at infinity

For every finite measure
$\mu$ on $\mathbb{R}$, the combined tail $\mu((x, \infty)) + \mu((-\infty, -x))$, with both
masses taken as real numbers, tends to $0$ as $x \to \infty$.

Formalized by `MathlibExt.Probability.RegularVariation.tendsto_combinedTail_atTop`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#tendsto-combined-tail-at-top).

## Tail balance

Let $\mu$ be a finite measure on $\mathbb{R}$ and $p$ a real number. Write
$R(x) = \mu((x, \infty))$ for the right tail and $T(x) = \mu((x, \infty)) + \mu((-\infty, -x))$
for the combined tail of $\mu$. The measure $\mu$ has tail balance $p$ when $0 \le p \le 1$,
$T(x) > 0$ for all sufficiently large $x$, and $R(x) / T(x) \to p$ as $x \to \infty$.

For the law of a random variable $X$ this says $P(X > x) / P(|X| > x) \to p$. Eventual
positivity of $T$ rules out an eventual $0 / 0$.

Formalized by `MathlibExt.Probability.RegularVariation.HasTailBalance`, a definition declared in [MathlibExt/Probability/RegularVariation.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#has-tail-balance).

## Tail balance zero from a vanishing right tail

Let $\mu$ be a finite measure on
$\mathbb{R}$. If $\mu((x, \infty)) = 0$ for all sufficiently large $x$ and the combined tail
$\mu((x, \infty)) + \mu((-\infty, -x))$ is positive for all sufficiently large $x$, then $\mu$ has
tail balance $0$.

Formalized by `MathlibExt.Probability.RegularVariation.hasTailBalance_zero_of_eventually_rightTail_eq_zero`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#has-tail-balance-zero-of-eventually-righ).

## Eventually vanishing combined tail rules out tail balance

Let $\mu$ be a finite measure
on $\mathbb{R}$ and let $p \in \mathbb{R}$. If the combined tail of $\mu$ at $x$ equals $0$ for
all sufficiently large $x$, then $\mu$ does not have tail balance $p$.

Formalized by `MathlibExt.Probability.RegularVariation.not_hasTailBalance_of_eventually_combinedTail_eq_zero`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#not-has-tail-balance-of-eventually-combi).

## Dirac masses have no tail balance

For every $a \in \mathbb{R}$ and every
$p \in \mathbb{R}$, the Dirac measure $\delta_a$ at $a$ does not have tail balance $p$.

The combined tail of $\delta_a$ vanishes at every threshold $x \ge |a|$, so the eventual
positivity required by tail balance fails.

Formalized by `MathlibExt.Probability.RegularVariation.not_hasTailBalance_dirac`, a theorem declared in [MathlibExt/Probability/RegularVariation.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariation.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#not-has-tail-balance-dirac).

## Generalized inverse of a regularly varying function

For a regularly
varying function `f` of index `-α` with `α > 0` that is eventually
non-increasing, there exists a sequence `a : ℕ → ℝ` of positive reals such
that `n · f (a n) → 1` as `n → ∞`.

Formalized by `MathlibExt.Probability.RegularVariation.regularlyVarying_generalized_inverse`, a theorem declared in [MathlibExt/Probability/RegularVariationGeneralizedInverse.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariationGeneralizedInverse.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#regularly-varying-generalized-inverse).

## Ratio limit of a regularly varying function

A regularly varying function has the expected ratio limit.

Formalized by `MathlibExt.Probability.RegularVariation.IsRegularlyVarying.ratio_tendsto`, a theorem declared in [MathlibExt/Probability/RegularVariationKaramata.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariationKaramata.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#ratio-tendsto).

## Potter's bound

**Potter's bound** for antitone functions with a ratio limit. If `W` is
antitone, bounded, eventually positive and `W (c * x) / W x → c ^ ρ` for
every `c > 0`, then for every `δ > 0` there are `C > 0` and `Y` such that
`W (x * u) / W x ≤ C * u ^ (ρ - δ)` for all `x ≥ Y` and `u ∈ (0, 1]`.
The proof chains the ratio limit at the dyadic scales `1/2` and `2`.

Formalized by `MathlibExt.Probability.RegularVariation.potter_upper`, a theorem declared in [MathlibExt/Probability/RegularVariationKaramata.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariationKaramata.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#potter-upper).

## Karamata's integral theorem

**Karamata's integral theorem** for antitone functions with a ratio limit.
If `W` is antitone, nonnegative, bounded, eventually positive and
`W (c * x) / W x → c ^ ρ` for every `c > 0`, then for `β ≥ 0` and
`β + 1 + ρ > 0`,
`(∫ t in (0)..x, t ^ β * W t) / (x ^ (β + 1) * W x) → 1 / (β + 1 + ρ)`.
The proof substitutes `t = x * u` and applies dominated convergence with
Potter's bound as the dominator.

Formalized by `MathlibExt.Probability.RegularVariation.karamata_integral`, a theorem declared in [MathlibExt/Probability/RegularVariationKaramata.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/RegularVariationKaramata.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html#karamata-integral).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Regular variation](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/infinite-divisibility-regular-variation/regular-variation)
