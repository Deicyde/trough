---
declaration: section
origin: cited
lean: MathlibExt.Probability.FiniteMarkovChain.IsFiniteMarkovChain, MathlibExt.Probability.FiniteMarkovChain.finiteChainKernel, MathlibExt.Probability.FiniteMarkovChain.finiteChainKernel_apply, MathlibExt.Probability.FiniteMarkovChain.IsFiniteMarkovChain.condExp_indicator, MathlibExt.Probability.FiniteMarkovChain.IsFiniteMarkovChain.toIsMarkovChain, MathlibExt.Probability.FiniteMarkovChain.IsFiniteMarkovChain.map_succ_eq_bind
statement: formalized
proof: formalized
---

# Finite Markov chains

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-markov-chains/index.html).

## Finite-state Markov chain with a given transition matrix

`IsFiniteMarkovChain X P ℱ μ` asserts that the sequence `X : ℕ → Ω → Fin (M+1)`
is a Markov chain with transition matrix `P`, adapted to the filtration `ℱ`,
under the measure `μ`. Concretely: each `X n` is `ℱ n`-measurable, and the conditional
probability that `X (n+1) = j` given `ℱ n` equals `P.prob (X n) j`, matching the
Markov property `P(X_{n+1} = j | X_n = i, ...) = P_{ij}`.
Ported verbatim from `v1/Atlas/TheoryOfProbability/code/FiniteMarkovChain.lean`;
`v1` writes the filtration as `DiscreteFiltration Ω m`, which is `Filtration ℕ m`.

Formalized by `MathlibExt.Probability.FiniteMarkovChain.IsFiniteMarkovChain`, a structure declared in [MathlibExt/Probability/FiniteMarkovChain.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteMarkovChain.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-markov-chains/index.html#is-finite-markov-chain).

## Transition kernel of a stochastic matrix

The transition kernel of a stochastic matrix: `finiteChainKernel P x` is the
probability measure on `Fin (M + 1)` putting mass `P.prob x j` on each state `j`.
This is the kernel form of the transition matrix.

Formalized by `MathlibExt.Probability.FiniteMarkovChain.finiteChainKernel`, a definition declared in [MathlibExt/Probability/FiniteMarkovChain.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteMarkovChain.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-markov-chains/index.html#finite-chain-kernel).

## Transition kernel of a stochastic matrix evaluated on a set

The kernel of a stochastic matrix evaluated at a finite set is the sum of the
transition probabilities into that set.

Formalized by `MathlibExt.Probability.FiniteMarkovChain.finiteChainKernel_apply`, a theorem declared in [MathlibExt/Probability/FiniteMarkovChain.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteMarkovChain.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-markov-chains/index.html#finite-chain-kernel-apply).

## Bridge: finite-state Markov chains satisfy the general one-step Markov property

**Bridge: finite-state Markov chains satisfy the general one-step Markov
property.** For a finite Markov chain, the conditional expectation of the
indicator of `X (n+1) ∈ B` given `ℱ n` is the kernel of `P` evaluated at
`X n`, almost surely. This is the one-step form of `v1`'s general
`IsMarkovChain.markov_prop` specialized to the matrix kernel. No measurability
hypothesis on `B` is needed: the indicator is defined for every set, and the
proof only sums over the finite state space.

Formalized by `MathlibExt.Probability.FiniteMarkovChain.IsFiniteMarkovChain.condExp_indicator`, a theorem declared in [MathlibExt/Probability/FiniteMarkovChain.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteMarkovChain.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-markov-chains/index.html#cond-exp-indicator).

## Finite Markov chains satisfy the general Markov property

Convert the finite singleton-probability specification to the canonical general
Markov-chain predicate under the probability-space hypotheses of `condExp_indicator`.

Formalized by `MathlibExt.Probability.FiniteMarkovChain.IsFiniteMarkovChain.toIsMarkovChain`, a theorem declared in [MathlibExt/Probability/FiniteMarkovChain.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteMarkovChain.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-markov-chains/index.html#to-is-markov-chain).

## One-step forward equation

The law of `X (n+1)` is the law of `X n`
transported by the transition kernel of `P`.

Formalized by `MathlibExt.Probability.FiniteMarkovChain.IsFiniteMarkovChain.map_succ_eq_bind`, a theorem declared in [MathlibExt/Probability/FiniteMarkovChain.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteMarkovChain.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-markov-chains/index.html#map-succ-eq-bind).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite Markov chains](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-markov-chains/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/markov-chains/finite-markov-chains)
