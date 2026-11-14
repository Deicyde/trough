---
declaration: lemma
origin: cited
lean: MIPRE.oracleSampler, MIPRE.oracleSampler_cl, MIPRE.oracleSampler_dim, MIPRE.OracleSampler.core, MIPRE.OracleSampler.route_dimension, MIPRE.OracleSampler.route_alice, MIPRE.OracleSampler.route_bob, MIPRE.OracleSampler.route_oracle, MIPRE.OracleSampler.core_runs_within, MIPRE.OracleSampler.oracleSampler_timeBound, MIPRE.OracleSampler.samplerProgFun, MIPRE.OracleSampler.samplerProgFun_apply
statement: formalized
proof: formalized
---

# The typed oracularized sampler

For every sampler $\mathcal{S}$ with at least one level there is a typed sampler over ${\mathcal{T}}^\textsc{Orac}$, with the levels of $\mathcal{S}$, whose typed CL functions are those of Definition [The typed oracularized game](def-oracular-typed-game.md): the identity for $\textsc{O}$, and the CL functions $L^\textsc{A}$, $L^\textsc{B}$ of $\mathcal{S}$ for $\textsc{A}$, $\textsc{B}$, the same for both players. It depends on $\mathcal{S}$ alone, and its program is computed from the program of $\mathcal{S}$ in polynomial time. There are constants $c, m, e$ such that, whenever $\mathcal{S}$ runs within $B(\left\vert {d} \right\vert + 1)^k$ on inputs $(n, d)$ and $B$, $\left\vert {\mathcal{S}} \right\vert$ and $n$ are at most $W$, the typed sampler runs within $c(W + 1)^m(\left\vert {d} \right\vert + 1)^{e(k + 1)}$ on inputs $(n, d)$.

## Depends on

- [The typed oracularized game](def-oracular-typed-game.md)
- [Typed sampler and its distribution](../part-01/def-typed-sampler-interface.md)
- [Efficient s-m-n](../../computability/lem-smn.md)
- [Effective indexing and padding arithmetic](../part-07/lem-pcp-padding-programs.md)

## Proof depends on

- [Value transfers of the typed oracularized game](lem-oracular-typed-transfers.md)

## Proof

The program is a fixed core run on the program of $\mathcal{S}$ through the s-m-n construction of Lemma [Efficient s-m-n](../../computability/lem-smn.md), as the repeated sampler is. The core answers a typed query with at most one call to $\mathcal{S}$, through the universal machine of Lemma [Efficient universal Turing machine](../../computability/lem-universal-tm.md). The dimension query is forwarded unchanged. A query at an isolated type is forwarded as the query of the corresponding original player. A query at the type $\textsc{O}$ is answered from the query itself, with no call: the identity's marginals are the seed, its first stage map is the identity and its later ones are zero, its first factor space is everything and its later ones are empty. The zero vectors are written over the supplied vector rather than over the dimension, so the core never allocates by a dimension it has not been given. A forwarded query is at most twice the typed query plus a constant, and since $\left\vert {d} \right\vert + 1 \geq 2$ the resulting constant factor is absorbed into the degree, so no term exponential in $k$ enters the coefficient.

## Lean

Formalized as [`MIPRE.oracleSampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.oracleSampler), [`MIPRE.oracleSampler_cl`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.oracleSampler_cl), [`MIPRE.oracleSampler_dim`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.oracleSampler_dim), [`MIPRE.OracleSampler.core`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleSampler.core), [`MIPRE.OracleSampler.route_dimension`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleSampler.route_dimension), [`MIPRE.OracleSampler.route_alice`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleSampler.route_alice), [`MIPRE.OracleSampler.route_bob`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleSampler.route_bob), [`MIPRE.OracleSampler.route_oracle`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleSampler.route_oracle), [`MIPRE.OracleSampler.core_runs_within`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleSampler.core_runs_within), [`MIPRE.OracleSampler.oracleSampler_timeBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleSampler.oracleSampler_timeBound), [`MIPRE.OracleSampler.samplerProgFun`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleSampler.samplerProgFun), [`MIPRE.OracleSampler.samplerProgFun_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleSampler.samplerProgFun_apply).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4420](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4420)
