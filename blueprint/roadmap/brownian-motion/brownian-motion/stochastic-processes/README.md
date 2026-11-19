# Stochastic processes

Let $T$ be an index set and $\Omega$ a measurable space, with measure $\mathbb{P}$. A stochastic process is a function $X : T \to \Omega \to E$, where $E$ is another measurable space, such that for all $t \in T$, $X_t : \Omega \to E$ is $\mathbb{P}$-a.e. measurable.

**Lean remark**: we don't use a Lean definition for the law, but write the map in full.

**Lean remark**: we don't use a Lean definition for being a modification, but write explicitly the condition $\forall t \in T,\ Y_t =_{\mathbb{P}\text{-a.e.}} X_t$ .

A summary of the next few lemmas is this:

- indistinguishable $\implies$ modification $\implies$ same law,
- modification and continuous with $T$ separable $\implies$ indistinguishable.

- [Indistinguishable.Modification](lem-indistinguishable-modification.md)
- [map_eq_of_modification](lem-map-eq-of-modification.md)
- [map_eq_iff](lem-map-eq-iff.md)
- [indistinguishable_of_modification_of_continuous](lem-indistinguishable-of-modification-of-continu.md)
