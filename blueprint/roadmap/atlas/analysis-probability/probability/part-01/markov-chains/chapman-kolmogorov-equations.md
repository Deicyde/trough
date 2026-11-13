---
declaration: section
origin: cited
lean: MathlibExt.Probability.MarkovChainChapmanKolmogorov.IsMarkovChain, MathlibExt.Probability.MarkovChainChapmanKolmogorov.IsMarkovChain.condExp_indicator_eq, MathlibExt.Probability.MarkovChainChapmanKolmogorov.IsMarkovChain.map_eq_bind_pow, MathlibExt.Probability.MarkovChainFunctionCK.IsMarkovChain.condExp_comp_eq_integral_pow, MathlibExt.Probability.MarkovChainFunctionCK.IsMarkovChain.condExp_one_step_eq_integral, MathlibExt.Probability.MarkovChainFunctionCK.IsMarkovChain.integral_comp_eq
statement: formalized
proof: formalized
---

# Chapman–Kolmogorov equations

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/chapman-kolmogorov-equations/index.html).

## Markov chain with respect to a filtration

Let $\mu$ be a measure on $\Omega$, let
$(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration on $\Omega$, and let $\kappa$ be a Markov
kernel from a measurable space $S$ to itself. A sequence of random variables
$X_n : \Omega \to S$ is a Markov chain with respect to $(\mathcal{F}_n)$ with transition kernel
$\kappa$ under $\mu$ if it is adapted to $(\mathcal{F}_n)$ and, for every $n \in \mathbb{N}$ and
every measurable $B \subseteq S$,

$$\mathbb{E}_\mu[\mathbf{1}_B(X_{n+1}) \mid \mathcal{F}_n] = \kappa(X_n, B)$$

$\mu$-almost everywhere. This is the standard form
$P(X_{n+1} \in B \mid \mathcal{F}_n) = \kappa(X_n, B)$ of the Markov property.

Formalized by `MathlibExt.Probability.MarkovChainChapmanKolmogorov.IsMarkovChain`, a structure declared in [MathlibExt/Probability/MarkovChainChapmanKolmogorov.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovChainChapmanKolmogorov.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/chapman-kolmogorov-equations/index.html#is-markov-chain).

## Chapman–Kolmogorov equations, conditional form

Let $X = (X_n)_{n \in \mathbb{N}}$ be a
Markov chain with state space $S$, with respect to a filtration $(\mathcal{F}_n)$, with Markov
transition kernel $\kappa$, under a probability measure $\mu$. Then for all $m, n \in \mathbb{N}$
and every measurable $B \subseteq S$,

$$\mathbb{E}_\mu[\mathbf{1}_B(X_{m+n}) \mid \mathcal{F}_m] = \kappa^n(X_m, B)$$

$\mu$-almost everywhere, where $\kappa^n$ is the $n$-fold composition of $\kappa$ (the identity
kernel for $n = 0$). For $n = 1$ this is the defining one-step Markov property.

Formalized by `MathlibExt.Probability.MarkovChainChapmanKolmogorov.IsMarkovChain.condExp_indicator_eq`, a theorem declared in [MathlibExt/Probability/MarkovChainChapmanKolmogorov.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovChainChapmanKolmogorov.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/chapman-kolmogorov-equations/index.html#cond-exp-indicator-eq).

## Chapman–Kolmogorov equations, forward (law) form

Let $X = (X_n)_{n \in \mathbb{N}}$ be
a Markov chain with state space $S$, with respect to a filtration, with Markov transition kernel
$\kappa$, under a probability measure $\mu$, and let $\kappa^n$ be the $n$-fold composition of
$\kappa$ (the identity kernel for $n = 0$). Then for all $m, n \in \mathbb{N}$ the law of
$X_{m+n}$ is the law $\nu_m$ of $X_m$ pushed forward through $\kappa^n$: for every measurable
$B \subseteq S$, $\mu(X_{m+n} \in B) = \int_S \kappa^n(x, B) \, d\nu_m(x)$.

Formalized by `MathlibExt.Probability.MarkovChainChapmanKolmogorov.IsMarkovChain.map_eq_bind_pow`, a theorem declared in [MathlibExt/Probability/MarkovChainChapmanKolmogorov.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovChainChapmanKolmogorov.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/chapman-kolmogorov-equations/index.html#map-eq-bind-pow).

## Chapman–Kolmogorov equations for bounded measurable functions

For a Markov chain `X` with transition kernel `κ`, the conditional
expectation of `f (X (m + n))` given the past up to time `m` is the
`κ ^ n`-integral of `f` evaluated at `X m`. For `n = 1` this is the
one-step function form; the general case follows by integrating the
canonical conditional-indicator formula over each past-measurable set.

Formalized by `MathlibExt.Probability.MarkovChainFunctionCK.IsMarkovChain.condExp_comp_eq_integral_pow`, a theorem declared in [MathlibExt/Probability/MarkovChainFunctionCK.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovChainFunctionCK.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/chapman-kolmogorov-equations/index.html#cond-exp-comp-eq-integral-pow).

## One-step Chapman–Kolmogorov equation for functions

For a
bounded measurable `f`, the conditional expectation of `f (X (k+1))`
given `ℱ k` is the `κ`-integral of `f` evaluated at `X k`.

Formalized by `MathlibExt.Probability.MarkovChainFunctionCK.IsMarkovChain.condExp_one_step_eq_integral`, a theorem declared in [MathlibExt/Probability/MarkovChainFunctionCK.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovChainFunctionCK.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/chapman-kolmogorov-equations/index.html#cond-exp-one-step-eq-integral).

## Integrated Chapman–Kolmogorov equation for functions

The
unconditional expectation of `f (X (m + n))` is the expectation of the
`κ ^ n`-integral of `f` evaluated at `X m`.

Formalized by `MathlibExt.Probability.MarkovChainFunctionCK.IsMarkovChain.integral_comp_eq`, a theorem declared in [MathlibExt/Probability/MarkovChainFunctionCK.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovChainFunctionCK.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/chapman-kolmogorov-equations/index.html#integral-comp-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chapman–Kolmogorov equations](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/chapman-kolmogorov-equations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/markov-chains/chapman-kolmogorov-equations)
