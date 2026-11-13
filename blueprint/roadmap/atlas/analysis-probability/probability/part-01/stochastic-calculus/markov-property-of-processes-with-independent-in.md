---
declaration: section
origin: cited
lean: MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmPrev, MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmInc, MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmShifted, MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmCenteredShift, MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmCenteredLaw, MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmPathExpectation, MathlibExt.Probability.IndependentIncrementsMarkovProperty.BmAdapted, MathlibExt.Probability.IndependentIncrementsMarkovProperty.BmIndepIncrements
statement: formalized
proof: formalized
---

# Markov property of processes with independent increments

48 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html).

## Predecessor of a time in a finite set

For a finite set $S \subseteq \mathbb{R}_{\ge 0}$ and
$t \in \mathbb{R}_{\ge 0}$, the predecessor of $t$ in $S$ is the largest element of $S$ strictly
below $t$, or $0$ if there is no such element.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmPrev`, a definition declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-prev).

## Increment over the predecessor interval

Let $(B_t)_{t \ge 0}$ be a real-valued process
on $\Omega$, let $s \ge 0$, and let $S \subset \mathbb{R}_{\ge 0}$ be a finite set. For $t \ge 0$
let $t^-$ be the largest element of $S$ strictly below $t$, or $0$ if there is none. The
increment at $t$ is the random variable $\omega \mapsto B_{s+t}(\omega) - B_{s+t^-}(\omega)$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmInc`, a definition declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-inc).

## Shifted path of a process

For a real-valued process $(B_t)_{t \ge 0}$ on $\Omega$
indexed by $t \in \mathbb{R}_{\ge 0}$ and a time $s \ge 0$, the shifted path is the map sending
$\omega \in \Omega$ to the path $t \mapsto B_{s+t}(\omega)$ in $\mathbb{R}^{\mathbb{R}_{\ge 0}}$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmShifted`, a definition declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-shifted).

## Centered shifted path

Let $(B_t)_{t \ge 0}$ be a real-valued process on $\Omega$ and
let $s \ge 0$. The centered shifted path at time $s$ sends $\omega \in \Omega$ to the function
$t \mapsto B_{s+t}(\omega) - B_s(\omega)$ on $\mathbb{R}_{\ge 0}$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmCenteredShift`, a definition declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-centered-shift).

## Law of the centered shifted path

Let $(B_t)_{t \ge 0}$ be a real-valued process on a
measure space $(\Omega, \mu)$ and let $s \ge 0$. This is the pushforward of $\mu$ under the map
sending $\omega \in \Omega$ to the path $t \mapsto B_{s+t}(\omega) - B_s(\omega)$, a measure on
the space of functions $\mathbb{R}_{\ge 0} \to \mathbb{R}$ with its product σ-algebra.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmCenteredLaw`, a definition declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-centered-law).

## Time-dependent path expectation

Let $\mu$ be a measure on $\Omega$, let
$(B_t)_{t \ge 0}$ be a real process on $\Omega$ indexed by $t \in \mathbb{R}_{\ge 0}$, let
$s \ge 0$, and let $\nu_s$ be the law under $\mu$ (the pushforward of $\mu$) of the centered
shifted path $\omega \mapsto (t \mapsto B_{s+t}(\omega) - B_s(\omega))$. For a real function $Y$
on paths $\mathbb{R}_{\ge 0} \to \mathbb{R}$ and $x \in \mathbb{R}$, the path expectation is the
Bochner integral $\int Y(t \mapsto x + f(t))\, d\nu_s(f)$, which is $0$ when the integrand is
not integrable.

This value can depend on $s$; it is the generic time-dependent expectation.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmPathExpectation`, a definition declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-path-expectation).

## Adapted real process

A real-valued process $(B_t)_{t \ge 0}$ on $\Omega$, indexed by
$t \in \mathbb{R}_{\ge 0}$, is adapted to a filtration $(\mathcal{F}_t)_{t \ge 0}$ when $B_t$ is
$\mathcal{F}_t$-measurable for every $t \ge 0$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.BmAdapted`, an abbreviation declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-adapted).

## Independent increments with respect to a filtration

A real-valued process
$(B_t)_{t \ge 0}$ on $\Omega$ has independent increments with respect to a filtration
$(\mathcal{F}_t)_{t \ge 0}$ and a measure $\mu$ when, for all $0 \le s \le t$, the σ-algebra
generated by $B_t - B_s$ is independent of $\mathcal{F}_s$ under $\mu$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.BmIndepIncrements`, an abbreviation declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-indep-increments).

## Measurability of the shifted path

Let $B = (B_t)_{t \ge 0}$ be a real process on a
measurable space $\Omega$, adapted to a filtration $(\mathcal{F}_t)_{t \ge 0}$ of its σ-algebra,
and give the space $\mathbb{R}^{[0, \infty)}$ of real paths indexed by $t \ge 0$ the product
σ-algebra. For every $s \ge 0$, the map from $\Omega$ to $\mathbb{R}^{[0, \infty)}$ sending
$\omega$ to the path $t \mapsto B_{s+t}(\omega)$ is measurable.

Each coordinate $B_{s+t}$ is $\mathcal{F}_{s+t}$-measurable, hence measurable.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.measurable_bmShifted`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#measurable-bm-shifted).

## Measurability of the centered shifted path

Let $(\mathcal{F}_t)_{t \ge 0}$ be a
filtration on a measurable space $\Omega$ indexed by $\mathbb{R}_{\ge 0}$, and let
$(B_t)_{t \ge 0}$ be a real-valued process adapted to it (each $B_t$ is
$\mathcal{F}_t$-measurable). Then for every $s \ge 0$ the map
$\omega \mapsto (t \mapsto B_{s+t}(\omega) - B_s(\omega))$ from $\Omega$ to
$\mathbb{R}^{\mathbb{R}_{\ge 0}}$, with the product σ-algebra, is measurable.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.measurable_bmCenteredShift`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#measurable-bm-centered-shift).

## Measurability of an increment before a given time

Let $B = (B_t)_{t \ge 0}$ be a real
process on a measurable space $\Omega$, adapted to a filtration $(\mathcal{F}_t)_{t \ge 0}$ of its
σ-algebra, let $S$ be a finite set of nonnegative reals and let $s, t, u \ge 0$. Write $p_S(t)$
for the largest element of $S$ strictly below $t$, or $0$ if there is none. If $s + t \le s + u$
and $s + p_S(t) \le s + u$, then the increment $B_{s+t} - B_{s+p_S(t)}$ is
$\mathcal{F}_{s+u}$-measurable.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.measurable_bmInc_of_le`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#measurable-bm-inc-of-le).

## Inserting a larger element does not change the predecessor

For a finite set
$T \subseteq \mathbb{R}_{\ge 0}$ and $t \in \mathbb{R}_{\ge 0}$, call the largest element of $T$
strictly below $t$ (or $0$ if there is none) the predecessor of $t$ in $T$. Let
$S \subseteq \mathbb{R}_{\ge 0}$ be finite and let $t, a \in \mathbb{R}_{\ge 0}$ with $t < a$.
Then the predecessor of $t$ in $S \cup \{a\}$ equals the predecessor of $t$ in $S$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmPrev_insert_of_lt`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-prev-insert-of-lt).

## Predecessor of a new maximum

For a finite set $T \subseteq \mathbb{R}_{\ge 0}$ and
$t \in \mathbb{R}_{\ge 0}$, call the largest element of $T$ strictly below $t$ (or $0$ if there
is none) the predecessor of $t$ in $T$. Let $S \subseteq \mathbb{R}_{\ge 0}$ be finite and let
$a \in \mathbb{R}_{\ge 0}$ with $x < a$ for every $x \in S$. Then the predecessor of $a$ in
$S \cup \{a\}$ is the supremum of $S$ in $\mathbb{R}_{\ge 0}$, that is, its largest element, or $0$
if $S$ is empty.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmPrev_insert_self`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-prev-insert-self).

## Past events factor against grid increments

Let $\mu$ be a probability measure and let
$(B_t)_{t \ge 0}$ be a real process adapted to a filtration $(\mathcal{F}_t)_{t \ge 0}$ such that
$B_t - B_s$ is independent of $\mathcal{F}_s$ under $\mu$ whenever $s \le t$. Let
$s \in \mathbb{R}_{\ge 0}$ and let $S \subseteq \mathbb{R}_{\ge 0}$ be finite. For $t \in S$ let
$\Delta_t = B_{s+t} - B_{s+t^-}$, where $t^-$ is the largest element of $S$ strictly below $t$, or
$0$ if there is none. Then for every family $(C_t)_{t \ge 0}$ of Borel subsets of $\mathbb{R}$ and
every $A \in \mathcal{F}_s$,

$$\mu\Big(A \cap \bigcap_{t \in S} \{\Delta_t \in C_t\}\Big)
= \mu(A)\,\mu\Big(\bigcap_{t \in S} \{\Delta_t \in C_t\}\Big).$$

The proof is induction on $S$ by its maximum element $a$: the increment $\Delta_a$ is independent
of $\mathcal{F}_{s + a^-}$, which contains both $A$ and the earlier increments.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.measure_inter_biInter_bmInc`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#measure-inter-bi-inter-bm-inc).

## Telescoping sum of grid increments

Let $(B_t)_{t \ge 0}$ be a family of real functions
on $\Omega$, let $s \in \mathbb{R}_{\ge 0}$ and let $S \subseteq \mathbb{R}_{\ge 0}$ be a nonempty
finite set. For $u \in S$ let $\Delta_u = B_{s+u} - B_{s+u^-}$, where $u^-$ is the largest element
of $S$ strictly below $u$, or $0$ if there is none. Then for every $\omega \in \Omega$,
$\sum_{u \in S} \Delta_u(\omega) = B_{s + \max S}(\omega) - B_s(\omega)$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.sum_bmInc_eq`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#sum-bm-inc-eq).

## Telescoping the centered shifted path over a finite set

Let $(B_t)_{t \ge 0}$ be a
real-valued process on $\Omega$, let $s \ge 0$, and let $S \subset \mathbb{R}_{\ge 0}$ be a
finite set. For $u \ge 0$ let $u^-$ be the largest element of $S$ strictly below $u$, or $0$
if there is none. Then for every $t \in S$ and every $\omega \in \Omega$,
$B_{s+t}(\omega) - B_s(\omega) =
\sum_{u \in S : u \le t} (B_{s+u}(\omega) - B_{s+u^-}(\omega))$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmCentered_eq_sum_bmInc`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-centered-eq-sum-bm-inc).

## Measurability of the increments

Let $B = (B_t)_{t \ge 0}$ be a real process on a
measurable space $\Omega$, adapted to a filtration $(\mathcal{F}_t)_{t \ge 0}$ of its σ-algebra.
For every finite set $S$ of nonnegative reals and all $s, t \ge 0$, the increment
$B_{s+t} - B_{s+p_S(t)}$ is measurable, where $p_S(t)$ is the largest element of $S$ strictly
below $t$, or $0$ if there is none.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.measurable_bmInc`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#measurable-bm-inc).

## Increment rectangles

Let $(B_t)_{t \ge 0}$ be a real-valued process on $\Omega$, let
$s \ge 0$, and let $S \subset \mathbb{R}_{\ge 0}$ be a finite set. For $t \ge 0$ let $t^-$ be the
largest element of $S$ strictly below $t$, or $0$ if there is none. The increment rectangles
are the events
$\bigcap_{t \in S} \{\omega \in \Omega : B_{s+t}(\omega) - B_{s+t^-}(\omega) \in C_t\}$, where each
$C_t \subseteq \mathbb{R}$ is a Borel set.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmIncRectangles`, a definition declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-inc-rectangles).

## σ-algebra of the increments over a finite set

Let $(B_t)_{t \ge 0}$ be a real-valued
process on $\Omega$, let $s \ge 0$, and let $S \subset \mathbb{R}_{\ge 0}$ be a finite set. For
$t \ge 0$ let $t^-$ be the largest element of $S$ strictly below $t$, or $0$ if there is none.
This is the σ-algebra on $\Omega$ generated by the increment rectangles, the events
$\bigcap_{t \in S} \{\omega \in \Omega : B_{s+t}(\omega) - B_{s+t^-}(\omega) \in C_t\}$ with each
$C_t \subseteq \mathbb{R}$ a Borel set.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmIncSigma`, a definition declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-inc-sigma).

## Events of a single increment lie in the increment σ-algebra

Let $B = (B_t)_{t \ge 0}$
be a real process on a measurable space $\Omega$, let $s \ge 0$ and let $S$ be a finite set of
nonnegative reals. For $u \ge 0$ let $p_S(u)$ be the largest element of $S$ strictly below $u$,
or $0$ if there is none, and let $\Delta_u = B_{s+u} - B_{s+p_S(u)}$. Let $\mathcal{G}_S$ be the
σ-algebra on $\Omega$ generated by the sets
$\bigcap_{u \in S} \{\omega : \Delta_u(\omega) \in E_u\}$ for families $(E_u)_{u \ge 0}$ of
measurable subsets of $\mathbb{R}$. Then for every $t \in S$ and every measurable
$D \subseteq \mathbb{R}$, the event $\{\omega : \Delta_t(\omega) \in D\}$ belongs to
$\mathcal{G}_S$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.measurableSet_bmInc_preimage`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#measurable-set-bm-inc-preimage).

## Measurability of an increment in the increment σ-algebra

Let $(B_t)_{t \ge 0}$ be a
real-valued process on $\Omega$, let $s \ge 0$, and let $S \subseteq \mathbb{R}_{\ge 0}$ be
finite; for $t \in S$ let $t^-$ be the largest element of $S$ strictly below $t$, or $0$ if there
is none. Then for every $t \in S$, the increment $\omega \mapsto B_{s+t}(\omega) -
B_{s+t^-}(\omega)$ is measurable with respect to the σ-algebra generated by the events
$\bigcap_{u \in S} \{B_{s+u} - B_{s+u^-} \in C_u\}$, where every $C_u \subseteq \mathbb{R}$ is
Borel.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.measurable_bmInc_incSigma`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#measurable-bm-inc-inc-sigma).

## Independence of future increments from the present

Let $\mu$ be a probability measure
on $\Omega$, let $(\mathcal{F}_t)_{t \ge 0}$ be a filtration indexed by $\mathbb{R}_{\ge 0}$, and
let $(B_t)_{t \ge 0}$ be a real-valued process that is adapted (each $B_t$ is
$\mathcal{F}_t$-measurable) and has independent increments (for $u \le t$, the increment
$B_t - B_u$ is independent of $\mathcal{F}_u$ under $\mu$). For a finite set
$S \subseteq \mathbb{R}_{\ge 0}$ and $t \in S$, let $t^-$ be the largest element of $S$ strictly
below $t$, or $0$ if there is none. Then for every $s \ge 0$ and every finite
$S \subseteq \mathbb{R}_{\ge 0}$, $\mathcal{F}_s$ is independent under $\mu$ of the σ-algebra
generated by the events $\bigcap_{t \in S} \{B_{s+t} - B_{s+t^-} \in C_t\}$, where every
$C_t \subseteq \mathbb{R}$ is Borel.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.indep_bmIncSigma`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#indep-bm-inc-sigma).

## Cylinder events of the centered shifted path

Let $(B_t)_{t \ge 0}$ be a real-valued
process on $\Omega$ and let $s \ge 0$. The centered cylinders at time $s$ are the events
$\bigcap_{t \in S} \{\omega \in \Omega : B_{s+t}(\omega) - B_s(\omega) \in C_t\}$, where
$S \subset \mathbb{R}_{\ge 0}$ is a finite set and each $C_t \subseteq \mathbb{R}$ is a
Borel set.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmCenteredCylinders`, a definition declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-centered-cylinders).

## Centered cylinders lie in the increment σ-algebra

Let $B = (B_t)_{t \ge 0}$ be a real
process on a measurable space $\Omega$, let $s \ge 0$ and let $S$ be a finite set of nonnegative
reals. For $u \ge 0$ let $p_S(u)$ be the largest element of $S$ strictly below $u$, or $0$ if
there is none, and let $\Delta_u = B_{s+u} - B_{s+p_S(u)}$. Let $\mathcal{G}_S$ be the σ-algebra
on $\Omega$ generated by the sets $\bigcap_{u \in S} \{\omega : \Delta_u(\omega) \in E_u\}$ for
families $(E_u)_{u \ge 0}$ of measurable subsets of $\mathbb{R}$. Then for every family
$(C_t)_{t \ge 0}$ of measurable subsets of $\mathbb{R}$, the set
$\bigcap_{t \in S} \{\omega : B_{s+t}(\omega) - B_s(\omega) \in C_t\}$ belongs to
$\mathcal{G}_S$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.measurableSet_bmCentered_cylinder`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#measurable-set-bm-centered-cylinder).

## Evaluation events are measurable

For every $t \in \mathbb{R}_{\ge 0}$ and every Borel set
$D \subseteq \mathbb{R}$, the set of paths $f : \mathbb{R}_{\ge 0} \to \mathbb{R}$ with $f(t) \in D$
is measurable for the product σ-algebra on the space of all such paths.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.measurableSet_pi_eval_preimage`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#measurable-set-pi-eval-preimage).

## Independence of the centered future path from the present

Let $\mu$ be a probability
measure on $\Omega$, let $(\mathcal{F}_t)_{t \ge 0}$ be a filtration indexed by
$\mathbb{R}_{\ge 0}$, and let $(B_t)_{t \ge 0}$ be a real-valued process that is adapted (each
$B_t$ is $\mathcal{F}_t$-measurable) and has independent increments (for $u \le t$, the
increment $B_t - B_u$ is independent of $\mathcal{F}_u$ under $\mu$). Then for every $s \ge 0$,
$\mathcal{F}_s$ is independent under $\mu$ of the σ-algebra generated by the centered shifted
path $\omega \mapsto (t \mapsto B_{s+t}(\omega) - B_s(\omega))$, where the path space
$\mathbb{R}^{\mathbb{R}_{\ge 0}}$ carries the product σ-algebra.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.indep_bmCenteredShift`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#indep-bm-centered-shift).

## Cylinder sets of path space

The collection of sets of paths
$f : \mathbb{R}_{\ge 0} \to \mathbb{R}$ of the form $\bigcap_{t \in S} \{f : f(t) \in C_t\}$,
where $S \subseteq \mathbb{R}_{\ge 0}$ is a finite set and each $C_t$ is a measurable subset of
$\mathbb{R}$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmPathCylinders`, a definition declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-path-cylinders).

## Path cylinders form a π-system

Consider the subsets of $\mathbb{R}^{\mathbb{R}_{\ge 0}}$
of the form $\bigcap_{t \in S} \{f : f(t) \in C_t\}$, where $S \subseteq \mathbb{R}_{\ge 0}$ is
finite and every $C_t \subseteq \mathbb{R}$ is Borel. They form a π-system: whenever two of them
have nonempty intersection, the intersection is again of this form.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.isPiSystem_bmPathCylinders`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#is-pi-system-bm-path-cylinders).

## Cylinders generate the product σ-algebra on path space

The product σ-algebra on the space
of paths $f : \mathbb{R}_{\ge 0} \to \mathbb{R}$ equals the σ-algebra generated by the cylinders,
the sets $\{f : f(t) \in C_t \text{ for all } t \in S\}$ with $S$ a finite subset of
$\mathbb{R}_{\ge 0}$ and $(C_t)_{t \ge 0}$ a family of Borel subsets of $\mathbb{R}$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.pi_eq_generateFrom_bmPathCylinders`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 540](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L540). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#pi-eq-generate-from-bm-path-cylinders).

## Rectangles of a Borel set and a path cylinder

Write $\mathbb{R}^{\mathbb{R}_{\ge 0}}$
for the space of functions $\mathbb{R}_{\ge 0} \to \mathbb{R}$. These are the subsets of
$\mathbb{R} \times \mathbb{R}^{\mathbb{R}_{\ge 0}}$ of the form
$U \times \{f : f(t) \in V_t \text{ for all } t \in S\}$, where $U \subseteq \mathbb{R}$ is a
Borel set, $S \subset \mathbb{R}_{\ge 0}$ is a finite set, and each $V_t \subseteq \mathbb{R}$
is a Borel set.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmCylRectangles`, a definition declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 571](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L571). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-cyl-rectangles).

## Rectangles of a Borel set and a path cylinder form a π-system

Consider the subsets of
$\mathbb{R} \times \mathbb{R}^{\mathbb{R}_{\ge 0}}$ of the form
$U \times \bigcap_{t \in S} \{f \in \mathbb{R}^{\mathbb{R}_{\ge 0}} : f(t) \in V_t\}$, where
$U \subseteq \mathbb{R}$ is Borel, $S \subseteq \mathbb{R}_{\ge 0}$ is finite and every
$V_t \subseteq \mathbb{R}$ is Borel. They form a π-system: whenever two of them have nonempty
intersection, the intersection is again of this form.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.isPiSystem_bmCylRectangles`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 576](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L576). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#is-pi-system-bm-cyl-rectangles).

## Measurable rectangles lie in the σ-algebra of cylinder rectangles

Let
$U \subseteq \mathbb{R}$ be a Borel set and let $V$ be a set of paths
$f : \mathbb{R}_{\ge 0} \to \mathbb{R}$ that is measurable for the product σ-algebra. Then
$U \times V$ belongs to the σ-algebra on $\mathbb{R} \times (\mathbb{R}_{\ge 0} \to \mathbb{R})$
generated by the cylinder rectangles, the sets $U' \times \{f : f(t) \in C_t \text{ for all }
t \in S\}$ with $U'$ Borel, $S$ a finite subset of $\mathbb{R}_{\ge 0}$ and $(C_t)_{t \ge 0}$ a
family of Borel sets.

This is Dynkin's theorem applied to the cylinder π-system on path space.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.mem_generateFrom_bmCylRectangles`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 608](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L608). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#mem-generate-from-bm-cyl-rectangles).

## Cylinder rectangles generate the product σ-algebra

The product σ-algebra on
$\mathbb{R} \times (\mathbb{R}_{\ge 0} \to \mathbb{R})$, where the path space carries its product
σ-algebra, equals the σ-algebra generated by the cylinder rectangles, the sets
$U \times \{f : f(t) \in V_t \text{ for all } t \in S\}$ with $U$ Borel, $S$ a finite subset of
$\mathbb{R}_{\ge 0}$ and $(V_t)_{t \ge 0}$ a family of Borel subsets of $\mathbb{R}$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.prod_eq_generateFrom_bmCylRectangles`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 634](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L634). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#prod-eq-generate-from-bm-cyl-rectangles).

## The process value paired with its centered future path

For a real process
$(B_t)_{t \ge 0}$ on $\Omega$ indexed by $t \in \mathbb{R}_{\ge 0}$ and a time $s \ge 0$, this is
the map $\Omega \to \mathbb{R} \times \mathbb{R}^{\mathbb{R}_{\ge 0}}$ sending $\omega$ to the pair
consisting of $B_s(\omega)$ and the path $t \mapsto B_{s+t}(\omega) - B_s(\omega)$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmPair`, a definition declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 654](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L654). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-pair).

## Translating a path by a constant

The map sending a pair $(x, f)$, with
$x \in \mathbb{R}$ and $f : \mathbb{R}_{\ge 0} \to \mathbb{R}$, to the path $t \mapsto x + f(t)$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmPhi`, a definition declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 658](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L658). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-phi).

## Measurability of the pair map

Let $B = (B_t)_{t \ge 0}$ be a real process on a
measurable space $\Omega$, adapted to a filtration $(\mathcal{F}_t)_{t \ge 0}$ of its σ-algebra,
and give the space $\mathbb{R}^{[0, \infty)}$ of real paths indexed by $t \ge 0$ the product
σ-algebra. For every $s \ge 0$, the map from $\Omega$ to
$\mathbb{R} \times \mathbb{R}^{[0, \infty)}$ sending $\omega$ to the pair of $B_s(\omega)$ and the
centered shifted path $t \mapsto B_{s+t}(\omega) - B_s(\omega)$ is measurable.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.measurable_bmPair`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 662](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L662). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#measurable-bm-pair).

## Translation of paths is measurable

Give the space $\mathbb{R}^{[0, \infty)}$ of real paths
indexed by $t \ge 0$ the product σ-algebra. The map from
$\mathbb{R} \times \mathbb{R}^{[0, \infty)}$ to $\mathbb{R}^{[0, \infty)}$ sending $(x, f)$ to the
path $t \mapsto x + f(t)$ is measurable.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.measurable_bmPhi`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 668](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L668). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#measurable-bm-phi).

## Translating the centered future path recovers the shifted path

For a real process
$(B_t)_{t \ge 0}$ on $\Omega$ indexed by $t \in \mathbb{R}_{\ge 0}$, a time $s \ge 0$ and
$\omega \in \Omega$, translating the centered shifted path
$t \mapsto B_{s+t}(\omega) - B_s(\omega)$ by the constant $B_s(\omega)$ gives the shifted path
$t \mapsto B_{s+t}(\omega)$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmPhi_bmPair`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 675](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L675). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-phi-bm-pair).

## Section measures of the centered law are measurable

Let $B = (B_t)_{t \ge 0}$ be a real
process on a probability space $(\Omega, \mu)$, let $s \ge 0$, and let $\nu_s$ be the law of the
centered shifted path $t \mapsto B_{s+t} - B_s$ on the space $\mathbb{R}^{[0, \infty)}$ of real
paths indexed by $t \ge 0$, with its product σ-algebra. For every measurable set
$T \subseteq \mathbb{R} \times \mathbb{R}^{[0, \infty)}$, the function
$x \mapsto \nu_s(\{f : (x, f) \in T\})$ from $\mathbb{R}$ to $[0, \infty]$ is measurable.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.measurable_section_bmCenteredLaw`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 682](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L682). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#measurable-section-bm-centered-law).

## The pair identity on cylinder rectangles

Let $\mu$ be a probability measure and let
$(B_t)_{t \ge 0}$ be a real process adapted to a filtration $(\mathcal{F}_t)_{t \ge 0}$ such that
$B_t - B_s$ is independent of $\mathcal{F}_s$ under $\mu$ whenever $s \le t$. Fix
$s \in \mathbb{R}_{\ge 0}$, let $W^s$ be the centered shifted path $t \mapsto B_{s+t} - B_s$ and
let $\nu_s$ be its law under $\mu$. Let $U \subseteq \mathbb{R}$ be Borel, let
$S \subseteq \mathbb{R}_{\ge 0}$ be finite, let $(V_t)_{t \ge 0}$ be Borel subsets of $\mathbb{R}$,
and let $R = U \times \{f : f(t) \in V_t \text{ for all } t \in S\}$. Then for every
$A \in \mathcal{F}_s$,

$$\mu\big(A \cap \{(B_s, W^s) \in R\}\big)
= \int_A \nu_s\big(\{f : (B_s(\omega), f) \in R\}\big)\,d\mu(\omega).$$

The left side factors by the independence of $W^s$ from $\mathcal{F}_s$, and the section on the
right is empty unless $B_s(\omega) \in U$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.pair_section_rectangle`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 703](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L703). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#pair-section-rectangle).

## The pair-section identity for measurable sets

Let $\mu$ be a probability measure and
let $(B_t)_{t \ge 0}$ be a real process adapted to a filtration $(\mathcal{F}_t)_{t \ge 0}$ such
that $B_t - B_s$ is independent of $\mathcal{F}_s$ under $\mu$ whenever $s \le t$. Fix
$s \in \mathbb{R}_{\ge 0}$, let $W^s$ be the centered shifted path $t \mapsto B_{s+t} - B_s$ and
let $\nu_s$ be its law under $\mu$. Then for every set
$T \subseteq \mathbb{R} \times (\mathbb{R}_{\ge 0} \to \mathbb{R})$ that is measurable for the
product σ-algebra and every $A \in \mathcal{F}_s$,

$$\mu\big(A \cap \{(B_s, W^s) \in T\}\big)
= \int_A \nu_s\big(\{f : (B_s(\omega), f) \in T\}\big)\,d\mu(\omega).$$

The proof is Dynkin's theorem over cylinder rectangles.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.pair_section_lintegral`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 761](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L761). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#pair-section-lintegral).

## Nonnegative translated integrals against the centered law are measurable

Let
$B = (B_t)_{t \ge 0}$ be a real process on a probability space $(\Omega, \mu)$, let $s \ge 0$,
and let $\nu_s$ be the law of the centered shifted path $t \mapsto B_{s+t} - B_s$ on the space
$\mathbb{R}^{[0, \infty)}$ of real paths indexed by $t \ge 0$, with its product σ-algebra. For
every measurable $Y : \mathbb{R}^{[0, \infty)} \to [0, \infty]$, the function
$x \mapsto \int Y(x + g) \, d\nu_s(g)$ on $\mathbb{R}$ is measurable, where $x + g$ is the path
$t \mapsto x + g(t)$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.measurable_lintegral_bmPhi`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 901](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L901). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#measurable-lintegral-bm-phi).

## Nonnegative integrals of future path functionals over present events

Let $\mu$ be a
probability measure on $\Omega$, let $(\mathcal{F}_t)_{t \ge 0}$ be a filtration indexed by
$\mathbb{R}_{\ge 0}$, and let $(B_t)_{t \ge 0}$ be a real-valued process that is adapted (each
$B_t$ is $\mathcal{F}_t$-measurable) and has independent increments (for $u \le t$, the
increment $B_t - B_u$ is independent of $\mathcal{F}_u$ under $\mu$). Fix $s \ge 0$ and let
$\nu_s$ be the law under $\mu$ of the centered shifted path
$\omega \mapsto (t \mapsto B_{s+t}(\omega) - B_s(\omega))$ on $\mathbb{R}^{\mathbb{R}_{\ge 0}}$
with the product σ-algebra. Then for every measurable
$Y : \mathbb{R}^{\mathbb{R}_{\ge 0}} \to [0, \infty]$ and every $A \in \mathcal{F}_s$,

$$\int_A Y\big((B_{s+t}(\omega))_{t \ge 0}\big) \, d\mu(\omega)
= \int_A \int Y\big(t \mapsto B_s(\omega) + g(t)\big) \, d\nu_s(g) \, d\mu(\omega),$$

where all integrals are Lebesgue integrals of $[0, \infty]$-valued functions.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.independent_increments_lintegral_shift`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 913](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L913). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#independent-increments-lintegral-shift).

## The path expectation is measurable in the starting point

Let $B = (B_t)_{t \ge 0}$ be a
real process on a probability space $(\Omega, \mu)$, let $s \ge 0$, and let $\nu_s$ be the law of
the centered shifted path $t \mapsto B_{s+t} - B_s$ on the space $\mathbb{R}^{[0, \infty)}$ of
real paths indexed by $t \ge 0$, with its product σ-algebra. For every measurable
$Y : \mathbb{R}^{[0, \infty)} \to \mathbb{R}$, the function $x \mapsto \int Y(x + f) \, d\nu_s(f)$
on $\mathbb{R}$ is measurable, where $x + f$ is the path $t \mapsto x + f(t)$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.measurable_bmPathExpectation`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 1123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L1123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#measurable-bm-path-expectation).

## Bound on the path expectation

Let $\mu$ be a probability measure on $\Omega$, let
$(B_t)_{t \ge 0}$ be a real process on $\Omega$ indexed by $t \in \mathbb{R}_{\ge 0}$, let
$s \ge 0$, and let $\nu_s$ be the law under $\mu$ of the path
$\omega \mapsto (t \mapsto B_{s+t}(\omega) - B_s(\omega))$. If $Y$ is a measurable real function
on paths $\mathbb{R}_{\ge 0} \to \mathbb{R}$ with $|Y(p)| \le C$ for every path $p$, then for
every $x \in \mathbb{R}$ the path expectation $E_s Y(x) = \int Y(t \mapsto x + f(t))\, d\nu_s(f)$
satisfies $|E_s Y(x)| \le C$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmPathExpectation_bound`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 1136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L1136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-path-expectation-bound).

## Set integrals of the path expectation

Let $\mu$ be a probability measure on $\Omega$, let
$(\mathcal{F}_t)_{t \ge 0}$ be a filtration of the σ-algebra of $\Omega$ indexed by
$\mathbb{R}_{\ge 0}$, and let $(B_t)_{t \ge 0}$ be a real process such that each $B_t$ is
$\mathcal{F}_t$-measurable and, for all $u \le t$, the increment $B_t - B_u$ is independent of
$\mathcal{F}_u$ under $\mu$. Let $s \ge 0$, let $Y$ be a measurable real function on paths
$\mathbb{R}_{\ge 0} \to \mathbb{R}$ with $|Y(p)| \le C$ for every path $p$, and let
$A \in \mathcal{F}_s$. Write $\nu_s$ for the law under $\mu$ of
$\omega \mapsto (t \mapsto B_{s+t}(\omega) - B_s(\omega))$,
$E_s Y(x) = \int Y(t \mapsto x + f(t))\, d\nu_s(f)$ for $x \in \mathbb{R}$, and
$\theta_s \omega$ for the shifted path $t \mapsto B_{s+t}(\omega)$. Then

$$
\int_A E_s Y(B_s(\omega))\, d\mu(\omega)
  = \int_A Y^+(\theta_s \omega)\, d\mu(\omega) - \int_A Y^-(\theta_s \omega)\, d\mu(\omega),
$$

where $Y^+ = \max(Y, 0)$, $Y^- = \max(-Y, 0)$, and each integral on the right is the integral of
a nonnegative function, taken in $[0, \infty]$ and then converted to a real number.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.bmPathExpectation_setIntegral`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 1167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L1167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#bm-path-expectation-set-integral).

## Bounded integrals of future path functionals over present events

Let $\mu$ be a
probability measure on $\Omega$, let $(\mathcal{F}_t)_{t \ge 0}$ be a filtration indexed by
$\mathbb{R}_{\ge 0}$, and let $(B_t)_{t \ge 0}$ be a real-valued process that is adapted (each
$B_t$ is $\mathcal{F}_t$-measurable) and has independent increments (for $u \le t$, the
increment $B_t - B_u$ is independent of $\mathcal{F}_u$ under $\mu$). Fix $s \ge 0$ and let
$\nu_s$ be the law under $\mu$ of the centered shifted path
$\omega \mapsto (t \mapsto B_{s+t}(\omega) - B_s(\omega))$ on $\mathbb{R}^{\mathbb{R}_{\ge 0}}$
with the product σ-algebra. Let $Y : \mathbb{R}^{\mathbb{R}_{\ge 0}} \to \mathbb{R}$ be
measurable with $|Y(p)| \le C$ for every path $p$, for some real $C$, and for $x \in \mathbb{R}$
put $\Phi_s(x) = \int Y(t \mapsto x + f(t)) \, d\nu_s(f)$. Then for every $A \in \mathcal{F}_s$,

$$\int_A Y\big((B_{s+t}(\omega))_{t \ge 0}\big) \, d\mu(\omega)
= \int_A \Phi_s(B_s(\omega)) \, d\mu(\omega).$$

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.independent_increments_setIntegral`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 1336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L1336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#independent-increments-set-integral).

## Conditional expectation of a future path functional

Let $\mu$ be a probability measure
on $\Omega$, let $(\mathcal{F}_t)_{t \ge 0}$ be a filtration indexed by $\mathbb{R}_{\ge 0}$, and
let $(B_t)_{t \ge 0}$ be a real-valued process that is adapted (each $B_t$ is
$\mathcal{F}_t$-measurable) and has independent increments (for $u \le t$, the increment
$B_t - B_u$ is independent of $\mathcal{F}_u$ under $\mu$). Fix $s \ge 0$ and let $\nu_s$ be the
law under $\mu$ of the centered shifted path $\omega \mapsto (t \mapsto B_{s+t}(\omega) -
B_s(\omega))$ on $\mathbb{R}^{\mathbb{R}_{\ge 0}}$ with the product σ-algebra. Let
$Y : \mathbb{R}^{\mathbb{R}_{\ge 0}} \to \mathbb{R}$ be measurable with $|Y(p)| \le C$ for every
path $p$, for some real $C$, and for $x \in \mathbb{R}$ put
$\Phi_s(x) = \int Y(t \mapsto x + f(t)) \, d\nu_s(f)$. Then, $\mu$-almost everywhere,

$$\mathbb{E}_\mu\big[\, Y\big((B_{s+t})_{t \ge 0}\big) \bigm| \mathcal{F}_s \big] = \Phi_s(B_s).$$

The function $\Phi_s$ is computed from the law of the increments after time $s$, so it may
depend on $s$.

Formalized by `MathlibExt.Probability.IndependentIncrementsMarkovProperty.independent_increments_condExp`, a lemma declared in [MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean, line 1361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/IndependentIncrementsMarkovProperty.lean#L1361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html#independent-increments-cond-exp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Markov property of processes with independent increments](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/stochastic-calculus/markov-property-of-processes-with-independent-in)
