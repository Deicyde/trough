---
declaration: section
origin: cited
lean: MathlibExt.Probability.MarkovChainConstruction.markovLiftKernel, MathlibExt.Probability.MarkovChainConstruction.markovChainMeasure, MathlibExt.Probability.MarkovChainConstruction.markovChainMeasure_initial_distribution, MathlibExt.Probability.MarkovChainConstruction.markovChainMeasure_condDistrib, MathlibExt.Probability.MarkovChainConstruction.markov_chain_construction, MathlibExt.Probability.FiniteMarkovChain.ae_eval_zero_markovChainMeasure, MathlibExt.Probability.FiniteMarkovChain.isFiniteMarkovChain_markovChainMeasure, MathlibExt.Probability.MarkovChainPath.markovLiftKernel
statement: formalized
proof: formalized
---

# Construction of Markov chains

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html).

## Lifting a kernel to histories

For a kernel $\kappa$ from a measurable space $S$ to itself
and $n \in \mathbb{N}$, the lifted kernel from $S^{\{0, \dots, n\}}$ to $S$ sends a history
$(x_0, \dots, x_n)$ to $\kappa(x_n, \cdot)$: it reads off the last coordinate and applies $\kappa$.

This is the form of kernel used by the Ionescu–Tulcea trajectory construction.

Formalized by `MathlibExt.Probability.MarkovChainConstruction.markovLiftKernel`, a definition declared in [MathlibExt/Probability/MarkovChainConstruction.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainConstruction.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#markov-lift-kernel).

## Canonical Markov chain measure

Let $\kappa$ be a Markov kernel from a measurable space
$S$ to itself and let $\mu$ be a measure on $S$. The canonical Markov chain measure $P_\mu$ is the
measure on the path space $S^{\mathbb{N}}$ given by the Ionescu–Tulcea theorem for the initial
measure $\mu$ and, at each time $n$, the kernel sending a history $(x_0, \dots, x_n)$ to
$\kappa(x_n, \cdot)$. When $\mu$ is a probability measure, $P_\mu$ is the law of the Markov chain
with initial distribution $\mu$ and transition kernel $\kappa$.

Formalized by `MathlibExt.Probability.MarkovChainConstruction.markovChainMeasure`, a definition declared in [MathlibExt/Probability/MarkovChainConstruction.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainConstruction.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#markov-chain-measure).

## Initial distribution of the canonical Markov chain measure

Let $\kappa$ be a Markov
kernel from a measurable space $S$ to itself and let $\mu$ be a measure on $S$. Under the
canonical Markov chain measure $P_\mu$ on $S^{\mathbb{N}}$ with initial measure $\mu$ and
transition kernel $\kappa$, the law of the initial coordinate is $\mu$: the pushforward of $P_\mu$
along $\omega \mapsto \omega_0$ equals $\mu$.

Formalized by `MathlibExt.Probability.MarkovChainConstruction.markovChainMeasure_initial_distribution`, a theorem declared in [MathlibExt/Probability/MarkovChainConstruction.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainConstruction.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#markov-chain-measure-initial-distributio).

## Markov property of the canonical Markov chain measure

Let $S$ be a nonempty standard
Borel space, let $\kappa$ be a Markov kernel from $S$ to $S$, let $\mu$ be a probability measure
on $S$, and let $P_\mu$ be the canonical Markov chain measure on $S^{\mathbb{N}}$ with initial
distribution $\mu$ and transition kernel $\kappa$. Write $X_n(\omega) = \omega_n$. For every
$n \in \mathbb{N}$, the regular conditional distribution of $X_{n+1}$ given $(X_0, \dots, X_n)$
under $P_\mu$ agrees with the lifted kernel $(x_0, \dots, x_n) \mapsto \kappa(x_n, \cdot)$ for
almost every $(x_0, \dots, x_n)$ with respect to the law of $(X_0, \dots, X_n)$ under $P_\mu$.

Formalized by `MathlibExt.Probability.MarkovChainConstruction.markovChainMeasure_condDistrib`, a theorem declared in [MathlibExt/Probability/MarkovChainConstruction.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainConstruction.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#markov-chain-measure-cond-distrib).

## Markov chain construction theorem

Let $S$ be a nonempty standard Borel space, let
$\kappa$ be a Markov kernel from $S$ to $S$ and let $\mu$ be a probability measure on $S$. Then
there is a probability measure $P$ on the path space $S^{\mathbb{N}}$ such that, writing
$X_n(\omega) = \omega_n$ for the coordinates, the law of $X_0$ under $P$ is $\mu$, and for every
$n \in \mathbb{N}$ the regular conditional distribution of $X_{n+1}$ given $(X_0, \dots, X_n)$
under $P$ agrees with the kernel $(x_0, \dots, x_n) \mapsto \kappa(x_n, \cdot)$ for almost every
$(x_0, \dots, x_n)$ with respect to the law of $(X_0, \dots, X_n)$ under $P$.

That is, the coordinate process $(X_0, X_1, \dots)$ under $P$ is a Markov chain with initial
distribution $\mu$ and transition kernel $\kappa$.

Formalized by `MathlibExt.Probability.MarkovChainConstruction.markov_chain_construction`, a theorem declared in [MathlibExt/Probability/MarkovChainConstruction.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainConstruction.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#markov-chain-construction).

## Canonical Markov law started from a point starts there almost surely

The canonical Markov law with initial distribution `dirac i` starts at `i`
almost surely. Its initial marginal is supplied by the existing construction.

Formalized by `MathlibExt.Probability.FiniteMarkovChain.ae_eval_zero_markovChainMeasure`, a theorem declared in [MathlibExt/Probability/FiniteMarkovChainConstruction.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/FiniteMarkovChainConstruction.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#ae-eval-zero-markov-chain-measure).

## Canonical Markov law satisfies the finite Markov chain specification

The coordinate process under the existing canonical matrix-derived Markov law
satisfies the original finite-state Markov-chain specification on `Filtration.piLE`.

Formalized by `MathlibExt.Probability.FiniteMarkovChain.isFiniteMarkovChain_markovChainMeasure`, a theorem declared in [MathlibExt/Probability/FiniteMarkovChainConstruction.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/FiniteMarkovChainConstruction.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#is-finite-markov-chain-markov-chain-meas).

## Lifted transition kernel on histories

For a kernel $\kappa$ on $S$ and $n \in \mathbb{N}$,
this is the kernel from histories $(x_0, \dots, x_n)$ of states in $S$, indexed by
$\{0, \dots, n\}$, to $S$ that sends $(x_0, \dots, x_n)$ to $\kappa(x_n, \cdot)$. It is the
Markov lift kernel of $\kappa$ at $n$.

Formalized by `MathlibExt.Probability.MarkovChainPath.markovLiftKernel`, an abbreviation declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#markov-lift-kernel-2).

## One-step shift of a Markov partial trajectory

Let $\kappa$ be a Markov kernel on a
measurable space $S$, let $a, b \in \mathbb{N}$ and let $z = (z_0, \dots, z_{a+b})$ be a history
in $S^{\{0, \dots, a+b\}}$. Let $\mu_z$ be the one-step partial trajectory of the lifted kernel
of $\kappa$ from time $a + b$ to time $a + b + 1$ started at $z$, that is, the law of
$(z_0, \dots, z_{a+b}, X)$ where $X$ has law $\kappa(z_{a+b})$. Then the image of $\mu_z$ under
the map $(y_0, \dots, y_{a+b+1}) \mapsto (y_a, \dots, y_{a+b+1})$ that drops the first $a$
coordinates equals the one-step partial trajectory of the lifted kernel from time $b$ to time
$b + 1$ started at $(z_a, \dots, z_{a+b})$, that is, the law of $(z_a, \dots, z_{a+b}, X')$ where
$X'$ has law $\kappa(z_{a+b})$.

Formalized by `MathlibExt.Probability.MarkovChainPath.partialTraj_succ_map_drop`, a theorem declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#partial-traj-succ-map-drop).

## Last-coordinate history

For $a \in \mathbb{N}$ and a history $x = (x_0, \dots, x_a)$ of
states in $S$, indexed by $\{0, \dots, a\}$, the last-coordinate history of $x$ is the history
indexed by $\{0\}$ whose only entry is $x_a$.

Formalized by `MathlibExt.Probability.MarkovChainPath.lastHist`, a definition declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#last-hist).

## One-step shift of the partial trajectory kernel

Let $\kappa$ be a Markov kernel on $S$
and $a, b \in \mathbb{N}$. For a history $z = (z_0, \dots, z_{a+b})$ of states in $S$, extend
$z$ by one step, drawing $z_{a+b+1}$ from $\kappa(z_{a+b}, \cdot)$, and then keep the entries
at times $a, \dots, a + b + 1$, reindexed as $0, \dots, b + 1$. The law of the result equals
the law obtained by first keeping the entries of $z$ at times $a, \dots, a + b$, reindexed as
$0, \dots, b$, and then extending that history by one step in the same way. This holds as an
identity of kernels in $z$.

Formalized by `MathlibExt.Probability.MarkovChainPath.partialTraj_succ_map_drop_kernel`, a theorem declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#partial-traj-succ-map-drop-kernel).

## Shifted finite-dimensional distributions

Let $\kappa$ be a Markov kernel on $S$ and
$a, b \in \mathbb{N}$. For a history $x = (x_0, \dots, x_a)$ of states in $S$, let $Q_x$ be the
law of the history $(X_0, \dots, X_{a+b})$ that equals $x$ at times $0, \dots, a$ and then draws
each next state from $\kappa$ applied to the current state (the Ionescu–Tulcea partial
trajectory from time $a$ to time $a + b$). Then the image of $Q_x$ under
$(X_0, \dots, X_{a+b}) \mapsto (X_a, \dots, X_{a+b})$, with the times reindexed as
$0, \dots, b$, equals the law of $(X_0, \dots, X_b)$ under the partial trajectory from time $0$
to time $b$ started from the one-entry history $(x_a)$. This holds as an identity of kernels
in $x$.

Formalized by `MathlibExt.Probability.MarkovChainPath.partialTraj_map_drop`, a theorem declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#partial-traj-map-drop).

## Time shift on path space

Let $S$ be a set and $n \in \mathbb{N}$. The time-$n$ shift on
the path space $S^{\mathbb{N}}$ sends a path $\omega$ to the path $k \mapsto \omega_{n+k}$.

Formalized by `MathlibExt.Probability.MarkovChainPath.shiftPath`, a definition declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#shift-path).

## Finite restrictions of the shifted path

For all $n, b \in \mathbb{N}$ and every path
$\omega : \mathbb{N} \to S$, let $\theta_n \omega$ be the shifted path, $(\theta_n \omega)_k =
\omega_{n+k}$. The restriction of $\theta_n \omega$ to the times $0, \dots, b$ equals the
restriction of $\omega$ to the times $0, \dots, n + b$ with its entries at times $n, \dots, n + b$
kept and reindexed as $0, \dots, b$; that is, it is the tuple
$(\omega_n, \omega_{n+1}, \dots, \omega_{n+b})$.

Formalized by `MathlibExt.Probability.MarkovChainPath.frestrictLe_comp_shiftPath`, a lemma declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#frestrict-le-comp-shift-path).

## The shifted trajectory of a Markov chain restarts from its last state

Let $\kappa$ be a
Markov kernel on a measurable space $S$, let $n \in \mathbb{N}$ and let
$x = (x_0, \dots, x_n) \in S^{\{0, \dots, n\}}$. Let $P_x$ be the trajectory measure on
$S^{\mathbb{N}}$ of the lifted kernel of $\kappa$ started at time $n$ from the history $x$, and
let $P_{x_n}$ be the trajectory measure of the lifted kernel started at time $0$ from the
one-point history $x_n$. Then the image of $P_x$ under the time-$n$ shift
$\omega \mapsto (k \mapsto \omega_{n+k})$ equals $P_{x_n}$.

Formalized by `MathlibExt.Probability.MarkovChainPath.traj_map_shiftPath_eq`, a theorem declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#traj-map-shift-path-eq).

## Path filtration

Let $S$ be a measurable space. The path filtration on the path space
$S^{\mathbb{N}}$ is the filtration indexed by $\mathbb{N}$, relative to the product σ-algebra,
whose σ-algebra at time $n$ is the one generated by the coordinate maps $\omega \mapsto \omega_i$
for $i \le n$.

Formalized by `MathlibExt.Probability.MarkovChainPath.pathFiltration`, a definition declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#path-filtration).

## The path filtration is contained in the product σ-algebra

Let $S$ be a measurable space.
For every $n \in \mathbb{N}$, the $n$-th σ-algebra of the path filtration on $S^{\mathbb{N}}$,
generated by the coordinate maps $\omega \mapsto \omega_i$ for $i \le n$, is contained in the
product σ-algebra on $S^{\mathbb{N}}$.

Formalized by `MathlibExt.Probability.MarkovChainPath.pathFiltration_le_pi`, a lemma declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#path-filtration-le-pi).

## Markov chain path measure

For a measure $\mu$ on $S$ and a Markov kernel $\kappa$ on
$S$, the path measure $P_\mu$ is the measure on $S^{\mathbb{N}}$, with the product
$\sigma$-algebra, obtained by integrating against $\mu(dx)$ the Ionescu–Tulcea trajectory
measure that starts at $x$ at time $0$ and draws each next state from $\kappa$ applied to the
current state. It is the Markov chain measure of $\kappa$ and $\mu$; when $\mu$ is a
probability measure it is the law on path space of the Markov chain with initial distribution
$\mu$ and transition kernel $\kappa$.

Formalized by `MathlibExt.Probability.MarkovChainPath.MarkovChainPathMeasure`, an abbreviation declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#markov-chain-path-measure).

## Expectation under the chain started from a point

For a Markov kernel $\kappa$ on $S$,
a function $Y : S^{\mathbb{N}} \to \mathbb{R}$ of paths and a state $x \in S$, the expectation
$E_x Y$ is the integral of $Y$ against the Markov chain path measure with transition kernel
$\kappa$ and initial distribution the Dirac measure at $x$.

Formalized by `MathlibExt.Probability.MarkovChainPath.markovExpectation`, a definition declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#markov-expectation).

## Measurability of the Markov expectation

Let $S$ be a nonempty standard Borel space,
$\kappa$ a Markov kernel on $S$, and $Y : S^{\mathbb{N}} \to \mathbb{R}$ a bounded function,
measurable for the product $\sigma$-algebra. Then the map $x \mapsto E_x Y$, sending a state
$x$ to the expectation of $Y$ under the Markov chain with transition kernel $\kappa$ started
from $x$, is measurable.

Formalized by `MathlibExt.Probability.MarkovChainPath.measurable_markovExpectation`, a theorem declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#measurable-markov-expectation).

## Path measure from a point as a trajectory measure

Let $\kappa$ be a Markov kernel on
$S$, $n \in \mathbb{N}$, and $x = (x_0, \dots, x_n)$ a history of states in $S$. The law on path
space of the Markov chain with transition kernel $\kappa$ and initial distribution the Dirac
measure at $x_n$ equals the Ionescu–Tulcea trajectory measure on $S^{\mathbb{N}}$ started at
time $0$ from the one-entry history $(x_n)$ (the last-coordinate history of $x$), in which each
next state is drawn from $\kappa$ applied to the current state.

Formalized by `MathlibExt.Probability.MarkovChainPath.MarkovChainPathMeasure_dirac_eq_traj`, a theorem declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#markov-chain-path-measure-dirac-eq-traj).

## Integral of a shifted path functional

Let $S$ be a nonempty standard Borel space,
$\kappa$ a Markov kernel on $S$, and $Y : S^{\mathbb{N}} \to \mathbb{R}$ a bounded function,
measurable for the product $\sigma$-algebra. Fix $n \in \mathbb{N}$ and a history
$x = (x_0, \dots, x_n)$ of states in $S$, and let $P_{n,x}$ be the Ionescu–Tulcea trajectory
measure on $S^{\mathbb{N}}$ that equals $x$ at times $0, \dots, n$ and afterwards draws each
next state from $\kappa$ applied to the current state. Then

$$\int Y(\theta_n \omega) \, dP_{n,x}(\omega) = \int Y \, dP_{\delta_{x_n}},$$

where $(\theta_n \omega)_k = \omega_{n+k}$ is the time-$n$ shift and $P_{\delta_{x_n}}$ is the
law on path space of the Markov chain with transition kernel $\kappa$ and initial distribution
the Dirac measure at $x_n$.

The statement also takes a finite measure $\mu$ on $S$, which does not appear in it.

Formalized by `MathlibExt.Probability.MarkovChainPath.integral_shiftPath_traj_eq_markovExpectation`, a theorem declared in [MathlibExt/Probability/MarkovChainPathMeasure.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovChainPathMeasure.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html#integral-shift-path-traj-eq-markov-expec).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Construction of Markov chains](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/construction-of-markov-chains/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/markov-chains/construction-of-markov-chains)
