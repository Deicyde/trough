---
declaration: lemma
origin: cited
lean: MIPRE.OracleDecider.gameProg_runs_within, MIPRE.OracleDecider.core_runs_within, MIPRE.OracleDecider.core_timeBound, MIPRE.OracleDecider.core_accepting_le, MIPRE.OracleDecider.budget_sufficient, MIPRE.OracleDecider.exists_typedPredicate_perfectPCC_within, MIPRE.OracleDecider.oracleDecider_runs_within, MIPRE.OracleDecider.oracleDecider_timeBound
statement: formalized
proof: formalized
---

# Running times of the typed oracularized decider

In the setting of Lemma [The typed oracularized decider](lem-oracle-typed-decider.md), let the sampler and the decider of $\mathsf{V}$ run within $T_S(\left\vert {d} \right\vert + 1)^k$ and $T_D(\left\vert {d} \right\vert + 1)^k$ on inputs $(n, d)$, with $T_S, T_D \leq W$. There are constants depending only on $\ell$ such that:

1. the core runs on every well-formed input $c$ within $c_0(W + 1)^m(\left\vert {c} \right\vert + 1)^{e(k + 1)}$;
2. hence, if the budget $K(n)$ is at least that bound at the largest core input whose answers lie within the inner cut, the completeness statement of Lemma [The typed oracularized decider](lem-oracle-typed-decider.md) holds with no further hypothesis;
3. the decider runs on every input $(n, d)$ within $c_1(W + 1)^{m_1}(\left\vert {d} \right\vert + 1)^{e_1}$ whenever $K(n)$, $B(n)$, the index routine's running time at $n$, the description lengths of the three programs and $n$ are at most $W$, and the degree $e_1$ does not depend on $k$.

## Depends on

- [The typed oracularized decider](lem-oracle-typed-decider.md)

## Proof

The core's cost is the sum of the costs of its stages, each bounded through the cost lemmas of the routing combinators and the overhead of the universal machine. The answers of the sampler of $\mathsf{V}$ to the marginal queries are sized by its correctness clause, as vectors of length $s(n)$, and not by its running time; otherwise the time of the decider of $\mathsf{V}$, of degree $k$ in its input, would compound to degree $k^2$. Affine size bounds are absorbed into powers of $\left\vert {c} \right\vert + 1 \geq 2$, so that no constant depends on $k$. The decider's own cost is that of the index routine and of the clocked universal machine on the budget and the input, so the running time of $\mathsf{V}$ enters only through the budget.

## Lean

Formalized as [`MIPRE.OracleDecider.gameProg_runs_within`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.gameProg_runs_within), [`MIPRE.OracleDecider.core_runs_within`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.core_runs_within), [`MIPRE.OracleDecider.core_timeBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.core_timeBound), [`MIPRE.OracleDecider.core_accepting_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.core_accepting_le), [`MIPRE.OracleDecider.budget_sufficient`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.budget_sufficient), [`MIPRE.OracleDecider.exists_typedPredicate_perfectPCC_within`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.exists_typedPredicate_perfectPCC_within), [`MIPRE.OracleDecider.oracleDecider_runs_within`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.oracleDecider_runs_within), [`MIPRE.OracleDecider.oracleDecider_timeBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OracleDecider.oracleDecider_timeBound).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4498](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4498)
