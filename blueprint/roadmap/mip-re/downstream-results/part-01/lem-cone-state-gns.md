---
declaration: lemma
origin: cited
lean: MIPRE.Tsirelson.isConeState_stateOf, MIPRE.GNS.GenData.strategy, MIPRE.GNS.GenData.strategy_correlation, MIPRE.Tsirelson.stateStrategy, MIPRE.Tsirelson.stateStrategy_correlation, MIPRE.Tsirelson.stateStrategy_value, MIPRE.Tsirelson.mem_Cqc_iff
statement: formalized
proof: formalized
---

# Cone states are the states of commuting-operator strategies

For finite alphabets, the functional $z \mapsto \langle \psi, z(E, F) \psi \rangle$ of a commuting-operator strategy is a cone state; conversely every cone state $L$ is that of a commuting-operator strategy whose correlation is $\mathrm{Re}\, L(e_{xa} f_{yb})$. So $C_{qc}$ is the set of the correlations $\mathrm{Re}\, L(e_{xa} f_{yb})$ over cone states $L$.

## Depends on

- [The cone is Archimedean and positive on strategies](lem-cone-archimedean.md)
- [Correlation sets](def-correlation-sets.md)

## Proof

A cone state is hermitian (since $z - z^*$ and $i(z + z^*)$ are anti-hermitian), vanishes on $I$ (since $\pm j, \pm i j \in I \subseteq M$) and is positive on $s^* s$ and $s^* g s$. The GNS construction completes $P$ for the seminorm $\mathrm{Re}\, L(a^* a)^{1/2}$; left multiplication by a variable $g$ is a contraction because $a^*(1 - g^2) a \in M$, and extends to a positive operator on the completion. The normalizations and the cross-commutation hold because the corresponding vectors are null, and the class of $1$ is a unit vector.

## Lean

Formalized as [`MIPRE.Tsirelson.isConeState_stateOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.isConeState_stateOf), [`MIPRE.GNS.GenData.strategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.GNS.GenData.strategy), [`MIPRE.GNS.GenData.strategy_correlation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.GNS.GenData.strategy_correlation), [`MIPRE.Tsirelson.stateStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.stateStrategy), [`MIPRE.Tsirelson.stateStrategy_correlation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.stateStrategy_correlation), [`MIPRE.Tsirelson.stateStrategy_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.stateStrategy_value), [`MIPRE.Tsirelson.mem_Cqc_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.mem_Cqc_iff).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 199](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L199)
