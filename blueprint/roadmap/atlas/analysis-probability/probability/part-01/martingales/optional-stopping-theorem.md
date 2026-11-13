---
declaration: section
origin: cited
lean: MeasureTheory.Submartingale.stoppedValue_le_condExp_stoppedValue, MeasureTheory.Supermartingale.condExp_stoppedValue_le_stoppedValue, MeasureTheory.stoppedValueAtTop, MeasureTheory.Martingale.uniformIntegrable_stoppedProcess_of_uniformIntegrable, MeasureTheory.Martingale.integral_stoppedValueAtTop_eq_of_uniformIntegrable, MeasureTheory.IsStoppingTime.stoppedFiltration, MeasureTheory.IsStoppingTime.stoppedFiltration_apply, MeasureTheory.IsStoppingTime.measurableSet_eq_top_iSup_stoppedFiltration
statement: formalized
proof: formalized
---

# Optional stopping theorem

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html).

## Bounded optional stopping, conditional form

Let $\mu$ be a measure on a measurable
space $\Omega$, let $(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration such that $\mu$ is
σ-finite on every $\mathcal{F}_n$, and let $(f_n)_{n \in \mathbb{N}}$ be a real-valued
submartingale with respect to $(\mathcal{F}_n)$ and $\mu$. Let $L$ and $M$ be stopping times
with values in $\mathbb{N} \cup \{\infty\}$ such that $L(\omega) \le M(\omega) \le N$ for every
$\omega$, for some $N \in \mathbb{N}$, and suppose that $\mu$ is σ-finite on the σ-algebra
$\mathcal{F}_L$ of events $A$ with $A \cap \{L \le n\} \in \mathcal{F}_n$ for every $n$. Write
$f_L(\omega) = f_{L(\omega)}(\omega)$ and $f_M(\omega) = f_{M(\omega)}(\omega)$ for the stopped
values. Then $f_L \le \mathbb{E}_\mu[f_M \mid \mathcal{F}_L]$ holds $\mu$-almost everywhere.

Formalized by `MeasureTheory.Submartingale.stoppedValue_le_condExp_stoppedValue`, a theorem declared in [MathlibExt/Probability/BoundedOptionalStopping.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BoundedOptionalStopping.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#stopped-value-le-cond-exp-stopped-value).

## Bounded optional stopping, conditional form, supermartingale dual

Let $\mu$ be a
measure on a measurable space $\Omega$, let $(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration
such that $\mu$ is σ-finite on every $\mathcal{F}_n$, and let $(f_n)_{n \in \mathbb{N}}$ be a
real-valued supermartingale with respect to $(\mathcal{F}_n)$ and $\mu$. Let $L$ and $M$ be
stopping times with values in $\mathbb{N} \cup \{\infty\}$ such that
$L(\omega) \le M(\omega) \le N$ for every $\omega$, for some $N \in \mathbb{N}$, and suppose
that $\mu$ is σ-finite on the σ-algebra $\mathcal{F}_L$ of events $A$ with
$A \cap \{L \le n\} \in \mathcal{F}_n$ for every $n$. Write $f_L(\omega) = f_{L(\omega)}(\omega)$
and $f_M(\omega) = f_{M(\omega)}(\omega)$ for the stopped values. Then
$\mathbb{E}_\mu[f_M \mid \mathcal{F}_L] \le f_L$ holds $\mu$-almost everywhere.

This follows from the submartingale version applied to $-f$.

Formalized by `MeasureTheory.Supermartingale.condExp_stoppedValue_le_stoppedValue`, a theorem declared in [MathlibExt/Probability/BoundedOptionalStopping.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BoundedOptionalStopping.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#cond-exp-stopped-value-le-stopped-value).

## Value of a process at a possibly infinite time

For a real-valued process
$(f_n)_{n \in \mathbb{N}}$ on $\Omega$ and a map $\tau : \Omega \to \mathbb{N} \cup \{\infty\}$,
the value $f_\tau$ of $f$ at $\tau$ is the function on $\Omega$ given by
$f_\tau(\omega) = f_{\tau(\omega)}(\omega)$ when $\tau(\omega) < \infty$ and
$f_\tau(\omega) = \lim_{n \to \infty} f_n(\omega)$ when $\tau(\omega) = \infty$, where the limit
is an unspecified real number if $(f_n(\omega))_n$ does not converge.

Unlike the usual stopped value, which uses an arbitrary finite index where $\tau = \infty$,
this uses the limit there, as the general optional stopping theorem requires.

Formalized by `MeasureTheory.stoppedValueAtTop`, a definition declared in [MathlibExt/Probability/OptionalStoppingUniformIntegrable.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/OptionalStoppingUniformIntegrable.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#stopped-value-at-top).

## Optional stopping preserves uniform integrability of martingales

Let $\mu$ be a
probability measure and let $(f_n)_{n \in \mathbb{N}}$ be a real-valued martingale with respect
to a filtration $(\mathcal{F}_n)_{n \in \mathbb{N}}$ that is uniformly integrable. Then for every
stopping time $\tau$ with values in $\mathbb{N} \cup \{\infty\}$, the stopped process
$(f_{\tau \wedge n})_{n \in \mathbb{N}}$ is uniformly integrable.

The stopped process is a family of conditional expectations of the single integrable limit
process, hence uniformly integrable.

Formalized by `MeasureTheory.Martingale.uniformIntegrable_stoppedProcess_of_uniformIntegrable`, a theorem declared in [MathlibExt/Probability/OptionalStoppingUniformIntegrable.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/OptionalStoppingUniformIntegrable.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#uniform-integrable-stopped-process-of-un-2).

## General optional stopping for uniformly integrable martingales

Let $\mu$ be a
probability measure, let $(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration and let
$(f_n)_{n \in \mathbb{N}}$ be a real-valued martingale with respect to $(\mathcal{F}_n)$ that is
uniformly integrable. Let $f_\infty$ be the limit process of $f$ (its almost-everywhere limit, by
the martingale convergence theorem). Then for every stopping time $\tau$ with values in
$\mathbb{N} \cup \{\infty\}$, the value $f_\tau$ of $f$ at $\tau$ (at points where
$\tau = \infty$ it is $\lim_n f_n$) satisfies
$\int f_0 \, d\mu = \int f_\tau \, d\mu = \int f_\infty \, d\mu$.

Formalized by `MeasureTheory.Martingale.integral_stoppedValueAtTop_eq_of_uniformIntegrable`, a theorem declared in [MathlibExt/Probability/OptionalStoppingUniformIntegrable.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/OptionalStoppingUniformIntegrable.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#integral-stopped-value-at-top-eq-of-unif).

## Stopped filtration

Let $(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration on a
measurable space $\Omega$ and let $\tau$ be a stopping time for it with values in
$\mathbb{N} \cup \{\infty\}$. The stopped filtration is the filtration
$n \mapsto \mathcal{F}_{\tau \wedge n}$, where $\mathcal{F}_{\tau \wedge n}$ is the σ-algebra of
the stopping time $\tau \wedge n$.

Formalized by `MeasureTheory.IsStoppingTime.stoppedFiltration`, a definition declared in [MathlibExt/Probability/ConditionalOptionalStopping.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConditionalOptionalStopping.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#stopped-filtration).

## Levels of the stopped filtration

Let $(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration
on a measurable space $\Omega$ and let $\tau$ be a stopping time for it with values in
$\mathbb{N} \cup \{\infty\}$. For every $n \in \mathbb{N}$, the $n$-th σ-algebra of the stopped
filtration is $\mathcal{F}_{\tau \wedge n}$, the σ-algebra of the stopping time $\tau \wedge n$.

Formalized by `MeasureTheory.IsStoppingTime.stoppedFiltration_apply`, a theorem declared in [MathlibExt/Probability/ConditionalOptionalStopping.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConditionalOptionalStopping.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#stopped-filtration-apply).

## The event that the stopping time is infinite is measurable for the stopped filtration

Let
$(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration on a measurable space $\Omega$ and let $\tau$
be a stopping time for it with values in $\mathbb{N} \cup \{\infty\}$. For each $n$, let
$\mathcal{F}_{\tau \wedge n}$ be the σ-algebra of the stopping time $\tau \wedge n$. Then the set
$\{\omega : \tau(\omega) = \infty\}$ is measurable with respect to
$\bigvee_n \mathcal{F}_{\tau \wedge n}$.

Formalized by `MeasureTheory.IsStoppingTime.measurableSet_eq_top_iSup_stoppedFiltration`, a theorem declared in [MathlibExt/Probability/ConditionalOptionalStopping.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConditionalOptionalStopping.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#measurable-set-eq-top-i-sup-stopped-filt).

## Infinite-time parts of limit-σ-algebra sets are measurable for the stopped filtration

Let
$(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration on a measurable space $\Omega$ and let $\tau$
be a stopping time for it with values in $\mathbb{N} \cup \{\infty\}$. For each $n$, let
$\mathcal{F}_{\tau \wedge n}$ be the σ-algebra of the stopping time $\tau \wedge n$. If a set
$s \subseteq \Omega$ is measurable with respect to $\bigvee_n \mathcal{F}_n$, then
$s \cap \{\tau = \infty\}$ is measurable with respect to $\bigvee_n \mathcal{F}_{\tau \wedge n}$.

The proof is induction on the σ-algebra generated by the π-system of sets measurable at some
finite time. For $s \in \mathcal{F}_k$ and $m \ge k$, the sets
$(s \cap \{\tau > m\}) \cup \{\tau \le m\}$ lie in $\mathcal{F}_{\tau \wedge m}$, and their
intersection over $m \ge k$, intersected with $\{\tau = \infty\}$, is $s \cap \{\tau = \infty\}$.

Formalized by `MeasureTheory.IsStoppingTime.measurableSet_inter_eq_top_iSup_stoppedFiltration`, a theorem declared in [MathlibExt/Probability/ConditionalOptionalStopping.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConditionalOptionalStopping.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#measurable-set-inter-eq-top-i-sup-stoppe).

## The stopped filtration generates the stopping-time σ-algebra

Let
$(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration on a measurable space $\Omega$ and let $\tau$
be a stopping time for it with values in $\mathbb{N} \cup \{\infty\}$. For each $n$, let
$\mathcal{F}_{\tau \wedge n}$ be the σ-algebra of the stopping time $\tau \wedge n$, the $n$-th
σ-algebra of the stopped filtration, and let $\mathcal{F}_\tau$ be the σ-algebra of $\tau$. Then
$\bigvee_n \mathcal{F}_{\tau \wedge n} = \mathcal{F}_\tau$.

The inclusion $\le$ is monotonicity. For $\ge$, a set $s \in \mathcal{F}_\tau$ splits into its
finite-time part $s \cap \{\tau < \infty\} = \bigcup_n (s \cap \{\tau \le n\})$ and its
infinite-time part $s \cap \{\tau = \infty\}$, and both are measurable for the supremum.

Formalized by `MeasureTheory.IsStoppingTime.iSup_stoppedFiltration`, a theorem declared in [MathlibExt/Probability/ConditionalOptionalStopping.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConditionalOptionalStopping.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#i-sup-stopped-filtration).

## Stopped value as conditional expectation of the limit

Let $\mu$ be a probability measure
on $\Omega$, let $(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration, and let
$(f_n)_{n \in \mathbb{N}}$ be a real-valued martingale with respect to $(\mathcal{F}_n)$ and $\mu$
that is uniformly integrable in $L^1(\mu)$. Let $f_\infty$ be its limit process, a function
measurable with respect to $\bigvee_n \mathcal{F}_n$ to which $f_n$ converges $\mu$-almost
everywhere. Then for every stopping time $\tau$ with values in $\mathbb{N} \cup \{\infty\}$, the
value $f_\tau$ of $f$ at $\tau$ (with $f_\tau(\omega) = \lim_n f_n(\omega)$ where
$\tau(\omega) = \infty$) satisfies $f_\tau = \mu[f_\infty \mid \mathcal{F}_\tau]$ $\mu$-almost
everywhere, where $\mu[\,\cdot \mid \mathcal{F}_\tau]$ is conditional expectation given the
σ-algebra $\mathcal{F}_\tau$ of $\tau$.

For each $n$, bounded optional sampling gives
$f_{\tau \wedge n} = \mu[f_\infty \mid \mathcal{F}_{\tau \wedge n}]$ almost everywhere, and
Lévy's upward theorem for the filtration $n \mapsto \mathcal{F}_{\tau \wedge n}$ identifies the
almost-everywhere limit of these conditional expectations with
$\mu[f_\infty \mid \bigvee_n \mathcal{F}_{\tau \wedge n}] = \mu[f_\infty \mid \mathcal{F}_\tau]$.

Formalized by `MeasureTheory.Martingale.stoppedValueAtTop_ae_eq_condExp_limitProcess`, a theorem declared in [MathlibExt/Probability/ConditionalOptionalStopping.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConditionalOptionalStopping.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#stopped-value-at-top-ae-eq-cond-exp-limi).

## Stopping at a later time does not change the stopped value

Let $(f_n)_{n \in \mathbb{N}}$
be a sequence of real-valued functions on $\Omega$ and let
$L, M : \Omega \to \mathbb{N} \cup \{\infty\}$ satisfy $L(\omega) \le M(\omega)$ for every
$\omega$. Then the value at $L$ of the stopped process $n \mapsto f_{M \wedge n}$ equals the value
$f_L$ of $f$ at $L$ at every point of $\Omega$. Here the value of a sequence $(g_n)$ at a point
$\omega$ where the time is infinite is $\lim_n g_n(\omega)$ when this limit exists, and otherwise
a fixed default value that depends only on the sequence $(g_n(\omega))_{n \in \mathbb{N}}$.

On $\{L = \infty\}$ the inequality forces $M = \infty$, so there the stopped process is $f$
itself.

Formalized by `MeasureTheory.stoppedValueAtTop_stoppedProcess_of_le`, a theorem declared in [MathlibExt/Probability/ConditionalOptionalStopping.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConditionalOptionalStopping.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#stopped-value-at-top-stopped-process-of).

## Conditional optional stopping with UI of the stopped process

Let $\mu$ be a probability
measure on $\Omega$, let $(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration, and let
$(f_n)_{n \in \mathbb{N}}$ be a real-valued martingale with respect to $(\mathcal{F}_n)$ and $\mu$.
Let $L \le M$ be stopping times with values in $\mathbb{N} \cup \{\infty\}$, and suppose the
stopped process $(f_{M \wedge n})_{n \in \mathbb{N}}$ is uniformly integrable in $L^1(\mu)$. Then
$f_L = \mu[f_M \mid \mathcal{F}_L]$ $\mu$-almost everywhere. Here $f_L$ and $f_M$ are the values
of $f$ at the possibly infinite times $L$ and $M$, with $f_L(\omega) = \lim_n f_n(\omega)$ where
$L(\omega) = \infty$ and likewise for $M$, and $\mu[\,\cdot \mid \mathcal{F}_L]$ is conditional
expectation given the σ-algebra $\mathcal{F}_L$ of $L$.

If $f$ itself is uniformly integrable, then so is the stopped process $(f_{M \wedge n})$, so the
conclusion holds in that case as well.

Formalized by `MeasureTheory.Martingale.stoppedValueAtTop_ae_eq_condExp_stoppedValueAtTop`, a theorem declared in [MathlibExt/Probability/ConditionalOptionalStopping.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConditionalOptionalStopping.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#stopped-value-at-top-ae-eq-cond-exp-stop).

## Conditional optional stopping for uniformly integrable submartingales

**Conditional optional stopping for uniformly integrable
submartingales.** For stopping times `L ≤ M` (possibly infinite),
`f_L ≤ᵐ μ[f_M | ℱ_L]`.

Formalized by `MeasureTheory.Submartingale.stoppedValueAtTop_le_condExp_stoppedValueAtTop`, a theorem declared in [MathlibExt/Probability/ConditionalOptionalStoppingSubmartingale.lean, line 575](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConditionalOptionalStoppingSubmartingale.lean#L575). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#stopped-value-at-top-le-cond-exp-stopped).

## Expectation form of conditional optional stopping for uniformly integrable submartingales

**Expectation form of conditional optional stopping for uniformly
integrable submartingales.** For stopping times `L ≤ M` (possibly
infinite), `∫ f_L ≤ ∫ f_M`.

Formalized by `MeasureTheory.Submartingale.integral_stoppedValueAtTop_mono_of_uniformIntegrable`, a theorem declared in [MathlibExt/Probability/ConditionalOptionalStoppingSubmartingale.lean, line 600](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConditionalOptionalStoppingSubmartingale.lean#L600). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#integral-stopped-value-at-top-mono-of-un).

## General optional stopping, uniform integrability preservation

Let $\mu$ be a
probability measure and let $(f_n)_{n \in \mathbb{N}}$ be a real-valued submartingale with
respect to a filtration $(\mathcal{F}_n)_{n \in \mathbb{N}}$ that is uniformly integrable. Then
for every stopping time $\tau$ with values in $\mathbb{N} \cup \{\infty\}$, the stopped process
$(f_{\tau \wedge n})_{n \in \mathbb{N}}$ is uniformly integrable.

Formalized by `MeasureTheory.Submartingale.uniformIntegrable_stoppedProcess_of_uniformIntegrable`, a theorem declared in [MathlibExt/Probability/OptionalStoppingUISubmartingale.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/OptionalStoppingUISubmartingale.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#uniform-integrable-stopped-process-of-un).

## General optional stopping, expectation inequality

Let $\mu$ be a probability measure,
let $(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration and let $(f_n)_{n \in \mathbb{N}}$ be a
real-valued submartingale with respect to $(\mathcal{F}_n)$ that is uniformly integrable. Let
$f_\infty$ be the limit process of $f$ (its almost-everywhere limit, by the martingale
convergence theorem). Then for every stopping time $\tau$ with values in
$\mathbb{N} \cup \{\infty\}$, the value $f_\tau$ of $f$ at $\tau$ (at points where
$\tau = \infty$ it is $\lim_n f_n$) satisfies
$\int f_0 \, d\mu \le \int f_\tau \, d\mu \le \int f_\infty \, d\mu$.

Formalized by `MeasureTheory.Submartingale.integral_stoppedValueAtTop_of_uniformIntegrable`, a theorem declared in [MathlibExt/Probability/OptionalStoppingUISubmartingale.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/OptionalStoppingUISubmartingale.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#integral-stopped-value-at-top-of-uniform).

## Optional stopping for supermartingales at two bounded stopping times

Let $\mu$ be a
measure on $\Omega$ and $(\mathcal G_n)_{n \ge 0}$ a filtration such that the restriction of $\mu$
to each $\mathcal G_n$ is σ-finite, and let $(f_n)_{n \ge 0}$ be a real-valued supermartingale
with respect to $(\mathcal G_n)$ and $\mu$. Let $\tau$ and $\pi$ be stopping times for
$(\mathcal G_n)$ with values in $\mathbb N \cup \{\infty\}$, and let $N$ be a natural number such
that $\tau(\omega) \le \pi(\omega) \le N$ for every $\omega \in \Omega$. Then
$\int f_\pi \, d\mu \le \int f_\tau \, d\mu$, where $f_\tau(\omega) = f_{\tau(\omega)}(\omega)$.

This is the dual of the submartingale form of bounded optional stopping, obtained by applying
it to $-f$.

Formalized by `MeasureTheory.Supermartingale.expected_stoppedValue_anti_mono`, a theorem declared in [MathlibExt/Probability/SupermartingaleOptionalStopping.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/SupermartingaleOptionalStopping.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#expected-stopped-value-anti-mono).

## Optional stopping for supermartingales at a bounded stopping time

Let $\mu$ be a measure
on $\Omega$ and $(\mathcal G_n)_{n \ge 0}$ a filtration such that the restriction of $\mu$ to each
$\mathcal G_n$ is σ-finite, and let $(f_n)_{n \ge 0}$ be a real-valued supermartingale with
respect to $(\mathcal G_n)$ and $\mu$. Let $\tau$ be a stopping time for $(\mathcal G_n)$ with
values in $\mathbb N \cup \{\infty\}$, and let $N$ be a natural number such that
$\tau(\omega) \le N$ for every $\omega \in \Omega$. Then $\int f_\tau \, d\mu \le \int f_0 \, d\mu$,
where $f_\tau(\omega) = f_{\tau(\omega)}(\omega)$.

Formalized by `MeasureTheory.Supermartingale.expected_stoppedValue_le`, a theorem declared in [MathlibExt/Probability/SupermartingaleOptionalStopping.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/SupermartingaleOptionalStopping.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#expected-stopped-value-le).

## Optional stopping for martingales at two bounded stopping times

Let $\mu$ be a measure
on $\Omega$ and $(\mathcal G_n)_{n \ge 0}$ a filtration such that the restriction of $\mu$ to each
$\mathcal G_n$ is σ-finite, and let $(f_n)_{n \ge 0}$ be a real-valued martingale with respect to
$(\mathcal G_n)$ and $\mu$. Let $\tau$ and $\pi$ be stopping times for $(\mathcal G_n)$ with
values in $\mathbb N \cup \{\infty\}$, and let $N$ be a natural number such that
$\tau(\omega) \le \pi(\omega) \le N$ for every $\omega \in \Omega$. Then
$\int f_\tau \, d\mu = \int f_\pi \, d\mu$, where $f_\tau(\omega) = f_{\tau(\omega)}(\omega)$.

Formalized by `MeasureTheory.Martingale.expected_stoppedValue_eq`, a theorem declared in [MathlibExt/Probability/SupermartingaleOptionalStopping.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/SupermartingaleOptionalStopping.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#expected-stopped-value-eq).

## Optional stopping for martingales at a bounded stopping time

Let $\mu$ be a measure on
$\Omega$ and $(\mathcal G_n)_{n \ge 0}$ a filtration such that the restriction of $\mu$ to each
$\mathcal G_n$ is σ-finite, and let $(f_n)_{n \ge 0}$ be a real-valued martingale with respect to
$(\mathcal G_n)$ and $\mu$. Let $\tau$ be a stopping time for $(\mathcal G_n)$ with values in
$\mathbb N \cup \{\infty\}$, and let $N$ be a natural number such that $\tau(\omega) \le N$ for
every $\omega \in \Omega$. Then $\int f_\tau \, d\mu = \int f_0 \, d\mu$, where
$f_\tau(\omega) = f_{\tau(\omega)}(\omega)$.

Formalized by `MeasureTheory.Martingale.expected_stoppedValue_eq_zero`, a theorem declared in [MathlibExt/Probability/SupermartingaleOptionalStopping.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/SupermartingaleOptionalStopping.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html#expected-stopped-value-eq-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Optional stopping theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/optional-stopping-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/martingales/optional-stopping-theorem)
