# Foundations

This chapter fixes the objects that everything else refers to: games, strategies and values (in the synchronous framework, see Section [Departures from the paper](../introduction/README.md)), the computability conventions, and normal form verifiers. Definitions here are meant to be final; they are the first formalization targets of the project.

Statements marked [[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] are general-purpose quantum information content: they are intended to be developed in, or contributed to, the [QuantumLib (Lean-QuantumInfo)](https://github.com/Timeroot/Lean-QuantumInfo) library rather than to remain specific to this project. The badge marks the general-purpose layer — games, strategies, values, and the rigidity theorems of Section [Background results](../background-results/README.md) — as opposed to project-specific machinery such as normal form verifiers and the game transformations.

## Games, strategies, and values

### Games

## [Nonlocal game to The Magic Square](part-01/README.md)

- [Nonlocal game](part-01/def-game.md)
- [Synchronous game](part-01/def-sync-game.md)
- [Tensor-product strategy](part-01/def-tensor-strategy.md)
- [Synchronous strategy](part-01/def-sync-strategy.md)
- [Commuting strategy](part-01/def-commuting-strategy.md)
- [PCC strategy](part-01/def-pcc.md)
- [Quantum value](part-01/def-q-value.md)
- [Synchronous value](part-01/def-sync-value.md)
- [Commuting value](part-01/def-commuting-value.md)
- [A perfect strategy rejects nothing on the support](part-01/lem-perfect-rejects-nothing.md)
- [Entanglement requirement](part-01/def-ent.md)
- [Synchronous value lower-bounds the quantum value](part-01/lem-sync-le-valstar.md)
- [Synchronous value lower-bounds the commuting value](part-01/lem-sync-le-valco.md)
- [LCS instance](part-01/def-lcs-instance.md)
- [LCS game](part-01/def-lcs-game.md)
- [Solution group](part-01/def-solution-group.md)
- [Binary observables](part-01/def-observable.md)
- [Observables and projective measurements correspond](part-01/lem-observable-projector.md)
- [From an observable strategy to a projective strategy](part-01/lem-observable-strategy.md)
- [The Magic Square](part-01/def-magic-square.md)

## [The Mermin–Peres strategy is… to Game description](part-02/README.md)

- [The Mermin–Peres strategy is perfect](part-02/lem-mermin-peres.md)
- [Perfect strategies from operator solutions](part-02/thm-lcs-perfect.md)
- [Normalized Hilbert–Schmidt norm](part-02/def-hs-norm.md)
- [POVM distance](part-02/def-distance.md)
- [State-dependent POVM distance](part-02/def-state-distance.md)
- [Cross-party state-dependent distance](part-02/def-cross-distance.md)
- [The expanded state, and an inert ancilla](part-02/def-expanded-state.md)
- [Naimark dilation of a question-indexed family](part-02/lem-naimark-dilation.md)
- [Commutation analysis](part-02/lem-commutation-analysis.md)
- [Cool closeness fact, and the marginal step](part-02/lem-cool-closeness-fact.md)
- [Pasting, the two-measurement case](part-02/lem-pasting-updated.md)
- [Generalized Pauli observables in characteristic two](part-02/def-generalized-pauli.md)
- [The maximally entangled state of the Weyl system](part-02/def-weyl-epr.md)
- [Qudits are qubits, in characteristic two](part-02/lem-pauli-binary.md)
- [Inconsistency](part-02/def-inconsistency.md)
- [Closeness from two disagreements](part-02/lem-hs-closeness.md)
- [Close measurements have close values](part-02/lem-close-measurements-close-values.md)
- [Recursively enumerable](part-02/def-re.md)
- [Succinct description](part-02/def-succinct.md)
- [Game description](part-02/def-game-description.md)

## [Sampler to The class is contained in the…](part-03/README.md)

- [Sampler](part-03/def-sampler.md)
- [Decider](part-03/def-decider.md)
- [Normal form verifier in the ambient model](part-03/def-normal-verifier.md)
- [$\lambda$-bounded verifier in the ambient model](part-03/def-lambda-bounded.md)
- [The class $\mathrm{MIP}^*_{1,1/2}(2,1)$](part-03/def-mipstar.md)
- [The computable class](part-03/def-mipstar-computable.md)
- [The class is contained in the computable one](part-03/lem-mipstar-poly-sub.md)
