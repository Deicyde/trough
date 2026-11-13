---
declaration: section
origin: cited
lean: ProbabilityTheory.IsDetailedBalance, ProbabilityTheory.vecMul_eq_zero_iff_forall_vecMul_ctmcTransition, ProbabilityTheory.IsDetailedBalance.vecMul_eq_zero, ProbabilityTheory.IsDetailedBalance.ctmcTransition, ProbabilityTheory.IsDetailedBalance.vecMul_ctmcTransition
statement: formalized
proof: formalized
---

# Stationarity and detailed balance for finite continuous-time Markov chains

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/stationarity-and-detailed-balance-for-finite-con/index.html).

## Probability Theory

## Detailed balance

The row vector `π` is in **detailed balance** with the matrix `Q`:
`π i * Q i j = π j * Q j i` for all `i j` (Norris 1997, §3.7). This is only the algebraic
equation: it holds for `π = 0` and every `Q`. For a probability vector `π` and a stochastic
matrix it is the reversibility of the chain started from `π`.

Formalized by `ProbabilityTheory.IsDetailedBalance`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Stationary.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Stationary.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/stationarity-and-detailed-balance-for-finite-con/index.html#is-detailed-balance).

## Invariance under the semigroup

`π Q = 0` if and only if `π P t = π` for every real
`t` (Norris 1997, §3.5, finite state space).

Formalized by `ProbabilityTheory.vecMul_eq_zero_iff_forall_vecMul_ctmcTransition`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Stationary.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Stationary.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/stationarity-and-detailed-balance-for-finite-con/index.html#vec-mul-eq-zero-iff-forall-vec-mul-ctmc).

## Detailed balance implies invariance for the generator

Detailed balance with a matrix whose rows sum to `0` implies invariance `π Q = 0`
(Norris 1997, §3.7).

Formalized by `ProbabilityTheory.IsDetailedBalance.vecMul_eq_zero`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Stationary.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Stationary.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/stationarity-and-detailed-balance-for-finite-con/index.html#vec-mul-eq-zero).

## Detailed balance propagates to the transition function

Detailed balance for `Q`
implies `π i P t i j = π j P t j i` for every `t` (Norris 1997, §3.7). For a probability
vector `π` and a rate matrix `Q` this is the reversibility of the chain started from `π`.

Formalized by `ProbabilityTheory.IsDetailedBalance.ctmcTransition`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Stationary.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Stationary.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/stationarity-and-detailed-balance-for-finite-con/index.html#ctmc-transition).

## Detailed balance implies invariance for the transition semigroup

Detailed balance with a matrix whose rows sum to `0` (for instance a rate matrix) makes `π`
invariant for every `P t`.

Formalized by `ProbabilityTheory.IsDetailedBalance.vecMul_ctmcTransition`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Stationary.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Stationary.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/stationarity-and-detailed-balance-for-finite-con/index.html#vec-mul-ctmc-transition).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stationarity and detailed balance for finite continuous-time Markov chains](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/stationarity-and-detailed-balance-for-finite-con/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/stationarity-and-detailed-balance-for-finite-con)
