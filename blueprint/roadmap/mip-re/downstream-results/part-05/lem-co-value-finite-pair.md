---
declaration: lemma
origin: cited
lean: MIPRE.Repetition.nonempty_of_lt_commutingOperatorValue, MIPRE.Repetition.exists_projStrat_expand_stdModel, MIPRE.Repetition.commutingFinitePairApprox
statement: formalized
proof: formalized
---

# ${\omega^{\mathrm{co}}}$ is approached in dyadic pairs

For every game $\mathfrak{G}$ and every $0 \leq t < {\omega^{\mathrm{co}}}(\mathfrak{G})$ there is a projective strategy for $\mathfrak{G}$ of value greater than $t$ in a dyadic pair (Definition [Dyadic pairs](def-dyadic-pair.md)).

## Depends on

- [Dyadic pairs](def-dyadic-pair.md)
- [Dyadic pairs are closed under ancilla extensions](lem-dyadic-pair-closure.md)
- [Amplification by an algebra with dyadic matrix units](lem-amplification-dyadic.md)
- [The twisted Pauli algebra](lem-pauli-algebra.md)
- [Projective dilation against a fixed state, in a star-ordered ring](../part-03/lem-kraus-dilation.md)
- [A global padded polynomial PVM](../../background-results/part-03/lem-qld-global-pvm.md)

## Proof

If an alphabet is empty, ${\omega^{\mathrm{co}}}(\mathfrak{G}) = 0$ and there is nothing to prove. Otherwise the vendored development's strict form of Lin's tracial density for game values gives a tracially embeddable strategy (Theorem [Lin's tracial density theorem](../../parallel-repetition/thm-tracial-density.md)) of winning probability greater than $t$: a tracial algebra ${\mathscr{A}}$ in standard form on $L^2({\mathscr{A}}, \tau)$, a density $\sigma$, and the two players' POVMs acting on the left and on the right, in the state $\iota\sigma$. Amplified by the twisted Pauli algebra (Lemma [The twisted Pauli algebra](lem-pauli-algebra.md)), it keeps its winning probability, and its standard-form model — the commutant $\mathcal{N}$ of the right action and its commutant $\mathcal{N}'$, as the players' algebras — is a dyadic pair in every state (Lemma [Amplification by an algebra with dyadic matrix units](lem-amplification-dyadic.md)). The left action lies in $\mathcal{N}$ and the right action in $\mathcal{N}'$, so the strategy is a POVM strategy in this model, of the same value. Each player's POVMs dilate to projective measurements in the matrices over the player's algebra, compressed to one basis vector (Lemma [Projective dilation against a fixed state, in a star-ordered ring](../part-03/lem-kraus-dilation.md)); in the ancilla extension at that basis vector they form a projective strategy of the same value (Lemma [A global padded polynomial PVM](../../background-results/part-03/lem-qld-global-pvm.md)), and the extension is a dyadic pair (Lemma [Dyadic pairs are closed under ancilla extensions](lem-dyadic-pair-closure.md)). Before the amplification the model is only a finite pair, whose algebras may have abelian projections; that is the reason for it (`reports/c6b-paper-proofs.md`, Section 3.7).

## Lean

Formalized as [`MIPRE.Repetition.nonempty_of_lt_commutingOperatorValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.nonempty_of_lt_commutingOperatorValue), [`MIPRE.Repetition.exists_projStrat_expand_stdModel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.exists_projStrat_expand_stdModel), [`MIPRE.Repetition.commutingFinitePairApprox`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.commutingFinitePairApprox).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3075](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3075)
