---
declaration: lemma
origin: cited
lean: MIPRE.OracleDecider.oracleDecider, MIPRE.OracleDecider.oracleDecider_total, MIPRE.OracleDecider.oracleDecider_accepts_iff, MIPRE.OracleDecider.gameProg_accepts_iff, MIPRE.OracleDecider.core_accepts_iff, MIPRE.OracleDecider.accepts_sound, MIPRE.OracleDecider.accepts_complete, MIPRE.OracleDecider.deciderProgFun, MIPRE.OracleDecider.deciderProgFun_apply, MIPRE.OracleDecider.typedPredicate_sound, MIPRE.OracleDecider.typedPredicate_complete, MIPRE.OracleDecider.valStar_ge_of_typedPredicate, MIPRE.OracleDecider.exists_typedPredicate_perfectPCC
statement: formalized
proof: formalized
---

# The typed oracularized decider

Let $\mathsf{V}$ be a normal form verifier whose sampler has $\ell + 1$ levels, and let an index routine supply at each index $n$ a parse cut $B(n)$ and a simulation budget $K(n)$. There is a typed decider over ${\mathcal{T}}^\textsc{Orac}$ that halts on every input, whatever the programs of $\mathsf{V}$ do, whose program is computed from those of $\mathsf{V}$ and the routine in polynomial time, and which accepts $(n, t, x, u, y, a, b)$ exactly when a fixed core accepts it within $K(n)$ steps. For $x, y$ of length $s(n)$ the core accepts exactly the answers that the bit-string predicate of Definition [The typed oracularized game](../part-06/def-oracular-typed-game.md) accepts at the cut $B(n)$: both answers parse by role against $B(n)$, the checks of `fig:oracle-decider` hold, and for each oracle the decider of $\mathsf{V}$ accepts $(n, L^\textsc{A} z, L^\textsc{B} z, a_1, a_2)$. Consequently, for the typed predicate the detyping compiler reads off this decider, at an inner cut of at least $8B(n) + 3$: if its typed game has value above $1 - \varepsilon$ then $\mathrm{val}^*(\mathsf{V}_n) \geq 1 - 24\sqrt{\varepsilon}$ at the cut $B(n)$, whatever the budget; and a value-$1$ PCC strategy of $\mathsf{V}_n$ at the cut $B(n)$ gives one of the doubled typed game, when the core's accepting runs on answers within the inner cut take at most $K(n)$ steps.

## Depends on

- [The typed oracularized game](../part-06/def-oracular-typed-game.md)
- [Value transfers of the typed oracularized game](../part-06/lem-oracular-typed-transfers.md)
- [The typed oracularized sampler](../part-06/lem-oracle-typed-sampler.md)
- [Efficient s-m-n](../../computability/lem-smn.md)

## Proof depends on

- [Total clocking of arbitrary typed decision programs](../part-01/lem-detype-total-clock.md)

## Proof

The decider is a fixed shell run on the three programs through the s-m-n construction of Lemma [Efficient s-m-n](../../computability/lem-smn.md). The shell asks the index routine for $(K(n), B(n))$ and runs the core under the clocked universal machine of Lemma [Efficient universal Turing machine](../../computability/lem-universal-tm.md) for $K(n)$ steps. This replaces the paper's timeout-counter form, which the ambient model does not have, and it makes the decider total, which the detyping compiler of Lemma [Effective detyping compiler](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L882) requires. The core parses each answer by role and runs the checks that need no call. For each oracle it runs the game check: two marginal queries to the sampler and one call to the decider of $\mathsf{V}$, all through the universal machine. The decider of $\mathsf{V}$ need not halt on the inputs it rejects, so both directions of the core's acceptance law go through inversion lemmas of the programs rather than through determinism. The two value statements are those of Lemma [Value transfers of the typed oracularized game](../part-06/lem-oracular-typed-transfers.md), read through the acceptance law.

## Lean

Formalized as [`MIPRE.OracleDecider.oracleDecider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.oracleDecider), [`MIPRE.OracleDecider.oracleDecider_total`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.oracleDecider_total), [`MIPRE.OracleDecider.oracleDecider_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.oracleDecider_accepts_iff), [`MIPRE.OracleDecider.gameProg_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.gameProg_accepts_iff), [`MIPRE.OracleDecider.core_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.core_accepts_iff), [`MIPRE.OracleDecider.accepts_sound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.accepts_sound), [`MIPRE.OracleDecider.accepts_complete`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.accepts_complete), [`MIPRE.OracleDecider.deciderProgFun`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.deciderProgFun), [`MIPRE.OracleDecider.deciderProgFun_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.deciderProgFun_apply), [`MIPRE.OracleDecider.typedPredicate_sound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.typedPredicate_sound), [`MIPRE.OracleDecider.typedPredicate_complete`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.typedPredicate_complete), [`MIPRE.OracleDecider.valStar_ge_of_typedPredicate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.valStar_ge_of_typedPredicate), [`MIPRE.OracleDecider.exists_typedPredicate_perfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.exists_typedPredicate_perfectPCC).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4455](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4455)
