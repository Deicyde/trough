---
declaration: section
origin: cited
lean: ProbabilityTheory.IsRateMatrix, ProbabilityTheory.IsRateMatrix.diag_eq, ProbabilityTheory.IsRateMatrix.diag_nonpos, ProbabilityTheory.IsRateMatrix.mulVec_one, ProbabilityTheory.IsRateMatrix.add_smul_one_nonneg, ProbabilityTheory.IsRateMatrix.exists_add_smul_one_nonneg
statement: formalized
proof: formalized
---

# Rate matrices of finite continuous-time Markov chains

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/rate-matrices-of-finite-continuous-time-markov-c/index.html).

## Probability Theory

## Rate matrix

A real square matrix `Q` is a **rate matrix** (a `Q`-matrix in Norris's terminology) if its
off-diagonal entries are nonnegative and each of its rows sums to `0` (Norris 1997, §2.1).

Formalized by `ProbabilityTheory.IsRateMatrix`, a structure declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/RateMatrix.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/RateMatrix.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/rate-matrices-of-finite-continuous-time-markov-c/index.html#is-rate-matrix).

## Diagonal of a rate matrix is minus the total jump rate

The diagonal entry of a rate matrix is minus the total jump rate out of the state.

Formalized by `ProbabilityTheory.IsRateMatrix.diag_eq`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/RateMatrix.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/RateMatrix.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/rate-matrices-of-finite-continuous-time-markov-c/index.html#diag-eq).

## Diagonal entries of a rate matrix are nonpositive

The diagonal entries of a rate matrix are nonpositive.

Formalized by `ProbabilityTheory.IsRateMatrix.diag_nonpos`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/RateMatrix.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/RateMatrix.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/rate-matrices-of-finite-continuous-time-markov-c/index.html#diag-nonpos).

## Rate matrix annihilates the constant vector

A rate matrix annihilates the constant vector `1`.

Formalized by `ProbabilityTheory.IsRateMatrix.mulVec_one`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/RateMatrix.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/RateMatrix.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/rate-matrices-of-finite-continuous-time-markov-c/index.html#mul-vec-one).

## Uniformization

If `c` bounds every exit rate `-Q i i`, then `Q + c • 1` has
nonnegative entries (Jensen 1953).

Formalized by `ProbabilityTheory.IsRateMatrix.add_smul_one_nonneg`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/RateMatrix.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/RateMatrix.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/rate-matrices-of-finite-continuous-time-markov-c/index.html#add-smul-one-nonneg).

## Existence of a uniformization constant for a rate matrix

Every rate matrix admits a uniformization constant `c ≥ 0`.

Formalized by `ProbabilityTheory.IsRateMatrix.exists_add_smul_one_nonneg`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/RateMatrix.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/RateMatrix.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/rate-matrices-of-finite-continuous-time-markov-c/index.html#exists-add-smul-one-nonneg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rate matrices of finite continuous-time Markov chains](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/rate-matrices-of-finite-continuous-time-markov-c/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/rate-matrices-of-finite-continuous-time-markov-c)
