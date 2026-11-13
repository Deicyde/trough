---
declaration: section
origin: cited
lean: OAI.TruffetV4Counterexample.finite_execution_not_optimal, OAI.randomized_quasipolynomial_mean_payoff
statement: formalized
proof: formalized
---

# 104. Quasipolynomial algorithms for mean-payoff, stochastic and parity games

4 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Gives deterministic algorithms using $2^{O((\log(L+2))^2)}$ bit operations, for complete binary input length *L*, for ordinary mean-payoff games and two separate extensions. They compute exact values and optimal positional strategies in ordinary games, the nonnegative expectation-of-liminf value set in turn-based stochastic games, and the winning set for nonnegative liminf mean payoff conjoined with parity. Signed rewards, rational chance probabilities, and parity priorities are unrestricted and binary-encoded.

## Turn-Based Stochastic Mean-Payoff Games in Deterministic Quasipolynomial Time

We give a uniform deterministic quasipolynomial-time algorithm for finite turn-based stochastic mean-payoff games with signed integer rewards and rational chance-transition probabilities encoded in binary. It computes exactly the vertices of nonnegative value, including value zero, for the expectation of the pathwise liminf mean payoff. The algorithm uses exact rational arithmetic and $2^{O((\log(L+2))^2)}$ bit operations, where *L* is the complete binary input length.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/stochastic-mean-payoff-games.pdf).

## Mean-payoff parity games in quasipolynomial time

We give a uniform deterministic quasipolynomial-time algorithm for mean-payoff parity games. It computes all vertices from which a player can enforce both nonnegative liminf mean payoff and the parity condition, with arbitrary signed binary rewards and unrestricted binary priorities. The running time is $2^{O((\log(L+2))^2)}$ bit operations, where *L* is the complete input length.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/mean-payoff-parity.pdf).

## Deterministic quasipolynomial-time mean-payoff games

We give a deterministic algorithm that computes the complete zero-threshold winning set of a finite mean-payoff game with arbitrary signed integer edge weights encoded in binary. For total explicit input length *L*, it uses $2^{O((\log(L+2))^2)}$ bit operations. A reduction also computes the exact rational value at every vertex and globally optimal positional strategies for both players within the same quasipolynomial bound.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## Randomized quasipolynomial-time mean-payoff games

We give a randomized algorithm that computes the complete zero-threshold winning set of a finite mean-payoff game with arbitrary signed integer edge weights encoded in binary. For total explicit input length *L*, it uses $2^{O((\log(L+2))^2)}$ bit operations on every random tape and is correct with probability at least 7/8. A polynomial-time check certifies the winning regions and positional strategies for both players or reports failure. Independent repetition therefore gives an always-correct algorithm with the same expected quasipolynomial bit bound.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization checks that a specified two-step execution of Truffet's elimination procedure terminates with a feasible but nonoptimal output. It is a finite counterexample to that proposed optimization step.

The formalized result gives one randomized algorithm for the complete zero-threshold winning set of every finite mean-payoff game with signed binary weights. It succeeds with probability at least $7/8$ and runs in quasipolynomial bit time on every random tape. Self-loops, parallel edges, and history-dependent strategies are allowed, and winning means a nonnegative liminf average payoff.

## Lean: Finite counterexample to Truffet's optimization procedure

```lean
theorem finite_execution_not_optimal :
    crossRowRestriction initial ∧
    ForcedSingletonStep initial middle 0 1 ∧
    ForcedSingletonStep middle finalState 1 0 ∧
    (¬ ∃ j, finalState.remaining j) ∧ stop finalState ∧
    feasible initial output ∧ feasible initial better ∧
    output 2 = 0 ∧ better 2 = 0 ∧
    (output 1 : Coeff) = eval (lowerForm initial 0 1) output ∧
    (output 0 : Coeff) = eval (lowerForm middle 1 0) output ∧
    eval initial.cost output = eval finalState.cost output ∧
    eval initial.cost better < eval finalState.cost output
```

Stated in [TruffetCounterexample.lean, line 118](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TruffetCounterexample.lean#L118). Proved in [lean/OAI/Optimization/Tropical/TruffetCounterexample.lean, line 126](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Optimization/Tropical/TruffetCounterexample.lean#L126).

## Lean: Randomized quasipolynomial mean-payoff algorithm

```lean
theorem randomized_quasipolynomial_mean_payoff : MeanPayoff.MainClaim
```

Stated in [RandomizedMeanPayoff.lean, line 123](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/RandomizedMeanPayoff.lean#L123). Proved in [lean/OAI/Computability/RandomMean/Main.lean, line 65](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/RandomMean/Main.lean#L65). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/104.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/104.md)
