---
declaration: section
origin: cited
lean: StochasticMatrix.toMatrix, StochasticMatrix.IsErgodic, StochasticMatrix.matPow_eq_pow, StochasticMatrix.isErgodic_iff_isPrimitive, StochasticMatrix.matPow_row_sum, StochasticMatrix.matPow_one, StochasticMatrix.matPow_add, StochasticMatrix.matPow_pos_of_le_of_pos_pow
statement: formalized
proof: formalized
---

# Convergence theorem for finite Markov chains

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html).

## Underlying matrix of a stochastic matrix

Underlying matrix of probabilities of a `StochasticMatrix`.

Formalized by `StochasticMatrix.toMatrix`, a definition declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#to-matrix).

## Ergodic finite Markov chain

A finite-state Markov chain (given by its stochastic transition matrix `P`) is
*ergodic* if some positive power `P^n` has all strictly positive entries.

Formalized by `StochasticMatrix.IsErgodic`, a definition declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#is-ergodic).

## Recursive matrix power agrees with the matrix power

The recursively defined power `matPow` agrees with the ordinary matrix power.

Formalized by `StochasticMatrix.matPow_eq_pow`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#mat-pow-eq-pow).

## Ergodicity is primitivity of the transition matrix

Ergodicity is exactly primitivity of the transition matrix. This is the
bridge to Mathlib: `Matrix.IsPrimitive` is the same condition for a bare
matrix, while `IsErgodic` is the stochastic-matrix form, with nonnegativity
supplied by the `StochasticMatrix` structure.

Formalized by `StochasticMatrix.isErgodic_iff_isPrimitive`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#is-ergodic-iff-is-primitive).

## Powers of a stochastic matrix are stochastic

Every row of every power of a stochastic matrix sums to `1`: powers of a
stochastic matrix are stochastic.

Formalized by `StochasticMatrix.matPow_row_sum`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#mat-pow-row-sum).

## First recursive power of a stochastic matrix

One step of the power recursion: `matPow 1` is the matrix itself.

Formalized by `StochasticMatrix.matPow_one`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#mat-pow-one).

## Additivity of recursive matrix powers

Powers add: `matPow (a + b)` is the matrix product of `matPow a` and `matPow b`.

Formalized by `StochasticMatrix.matPow_add`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#mat-pow-add).

## Later powers of a positive stochastic matrix power stay positive

If some power `w` of a stochastic matrix is all-positive, then every later
power `m ≥ w` is all-positive: write `m = (m - w) + w`, use `matPow_add`, and
note that row `i` of `matPow (m - w)` sums to `1`, so some entry of that row is
positive, and that entry times the positive `matPow w` entry gives a positive
summand.

Formalized by `StochasticMatrix.matPow_pos_of_le_of_pos_pow`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#mat-pow-pos-of-le-of-pos-pow).

## Pairwise positive powers of an ergodic chain

An ergodic chain has, for every pair of states, some positive power with
a positive `(i, j)`-entry. (This is the per-pair form; it is strictly weaker
than ergodicity, which asks for one power working for all pairs at once.)

Formalized by `StochasticMatrix.IsErgodic.exists_matPow_pos`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#exists-mat-pow-pos).

## Powers of an ergodic chain are eventually all positive

Once a power of an ergodic chain is all-positive, every later power is
all-positive: there is a threshold `w` past which every power is all-positive.

Formalized by `StochasticMatrix.IsErgodic.eventually_all_matPow_pos`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#eventually-all-mat-pow-pos).

## Power of a stochastic matrix

The `p`-th power of a stochastic matrix, as a stochastic matrix.

Formalized by `StochasticMatrix.pow`, a definition declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#pow).

## Underlying matrix of a stochastic matrix power

The underlying matrix of `P.pow p` is the `p`-th matrix power of `P`.

Formalized by `StochasticMatrix.toMatrix_pow`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#to-matrix-pow).

## Recursive powers of a stochastic matrix power

Powers of a power: `(P.pow p).matPow n = P.matPow (p * n)`.

Formalized by `StochasticMatrix.matPow_pow`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#mat-pow-pow).

## Powers of an ergodic Markov chain are ergodic

Every positive power of an ergodic chain is ergodic.

Formalized by `StochasticMatrix.IsErgodic.pow`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#pow-2).

## Uniform Markov chain on finitely many states

The uniform chain: every transition has probability `1 / (M + 1)`.

Formalized by `StochasticMatrix.uniform`, a definition declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#uniform).

## Transition probabilities of the uniform chain

The uniform chain has constant transition probabilities `1 / (M + 1)`.

Formalized by `StochasticMatrix.prob_uniform`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#prob-uniform).

## The uniform Markov chain is ergodic

The uniform chain is ergodic, with witness `n = 1`.

Formalized by `StochasticMatrix.isErgodic_uniform`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#is-ergodic-uniform).

## Identity Markov chain

The identity chain: `prob i j` is `1` on the diagonal and `0` elsewhere.

Formalized by `StochasticMatrix.identity`, a definition declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#identity).

## Transition probabilities of the identity chain

The identity chain has the displayed transition probabilities.

Formalized by `StochasticMatrix.prob_identity`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#prob-identity).

## Powers of the identity chain are the identity matrix

Every power of the identity chain is the identity matrix.

Formalized by `StochasticMatrix.matPow_identity`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#mat-pow-identity).

## The identity Markov chain is not ergodic

The identity chain is not ergodic (for `M ≥ 1`): every power has a zero
off-diagonal entry.

Formalized by `StochasticMatrix.not_isErgodic_identity`, a theorem declared in [MathlibExt/Probability/ErgodicMarkovChain.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ErgodicMarkovChain.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#not-is-ergodic-identity).

## Doeblin's argument

**Doeblin's argument** (Levin, Peres and Wilmer, proof of Theorem 4.9): if the `r`-step
transition probabilities dominate `δ π`, then the total variation distance of `Pⁿ(x, ·)` from the
stationary distribution `π` is at most `(1 - δ) ^ ⌊n / r⌋`. The bound is informative when
`r > 0` and `0 < δ`; for `r = 0` (`n / 0 = 0`) or `δ ≤ 0` it reads `d_TV ≤ 1` or weaker.

Formalized by `MathlibExt.Probability.FiniteMarkovChainConvergence.tvDist_pow_le_of_minorization`, a theorem declared in [MathlibExt/Probability/FiniteMarkovChainConvergence.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteMarkovChainConvergence.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#tv-dist-pow-le-of-minorization).

## The convergence theorem

**The convergence theorem** (Levin, Peres and Wilmer, Theorem 4.9): a primitive
(irreducible and aperiodic) stochastic matrix with stationary distribution `π` converges to `π`
geometrically fast in total variation, uniformly in the starting state.

Formalized by `MathlibExt.Probability.FiniteMarkovChainConvergence.exists_tvDist_pow_le`, a theorem declared in [MathlibExt/Probability/FiniteMarkovChainConvergence.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteMarkovChainConvergence.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#exists-tv-dist-pow-le).

## Convergence of matrix powers to the stationary distribution

For a primitive stochastic matrix with stationary distribution `π`, every row of `Pⁿ`
converges to `π`: `Pⁿ(x, y) → π(y)`.

Formalized by `MathlibExt.Probability.FiniteMarkovChainConvergence.tendsto_pow_apply`, a theorem declared in [MathlibExt/Probability/FiniteMarkovChainConvergence.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteMarkovChainConvergence.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#tendsto-pow-apply).

## Uniqueness of the stationary distribution of a primitive chain

A primitive stochastic matrix has at most one stationary distribution. In fact `π'` may be
any stationary vector of total mass `1`, not necessarily nonnegative.

Formalized by `MathlibExt.Probability.FiniteMarkovChainConvergence.stationary_unique`, a theorem declared in [MathlibExt/Probability/FiniteMarkovChainConvergence.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteMarkovChainConvergence.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#stationary-unique).

## Stationary distribution of a primitive chain has full support

The stationary distribution of a primitive stochastic matrix has full support.

Formalized by `MathlibExt.Probability.FiniteMarkovChainConvergence.stationary_pos`, a theorem declared in [MathlibExt/Probability/FiniteMarkovChainConvergence.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteMarkovChainConvergence.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html#stationary-pos).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convergence theorem for finite Markov chains](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/markov-chains/convergence-theorem-for-finite-markov-chains)
