---
declaration: lemma
origin: cited
lean: MIPRE.BipartiteModel.bornProb_expand_smulKron, MIPRE.BipartiteModel.stateSqNorm_expand_smulKron_one, MIPRE.BipartiteModel.swap_stateSqNorm_expand_smulKron_one, MIPRE.BipartiteModel.norm_expand_state, MIPRE.IsPVMIn.smulKron
statement: formalized
proof: formalized
---

# The ancilla extension

In the ancilla extension by $e$ of a bipartite model:

1. for $X \in {\mathscr{A}}_A$, $Y \in {\mathscr{A}}_B$ and positive semidefinite $P \in M_\alpha(\mathbb{C})$ and $Q \in M_\beta(\mathbb{C})$, the Born probability of $(X \otimes P, Y \otimes Q)$ is the model's Born probability of $(X, Y)$ times $\mathrm{Re}\langle e, (P \otimes Q) e\rangle$;
2. an operator with an *inert* ancilla keeps its norm up to the norm of $e$: $\|\pi(X \otimes {I})(\psi \otimes e)\| = \|e\|\,\|\pi(X)\psi\|$, for either player;
3. $\|\psi \otimes e\| = \|\psi\|\,\|e\|$;
4. if $(P_i)_i$ is a projective measurement in ${\mathscr{A}}_A$ and $(Q_k)_k$ one in $M_\alpha(\mathbb{C})$, then $(P_i \otimes Q_k)_{(i,k)}$ is a projective measurement in $M_\alpha({\mathscr{A}}_A)$.

## Depends on

- [Ancilla extension of a bipartite model](def-ancilla-extension.md)

## Proof

The operator of $(X \otimes P)(Y \otimes Q)$ acts on $\psi \otimes e$ entrywise, as $\pi(XY)$ on $\psi$ and as $P \otimes Q$ on $e$, so its quadratic form is $\langle e, (P \otimes Q) e\rangle \langle \psi, \pi(XY) \psi\rangle$. The first factor is real when $P$ and $Q$ are positive semidefinite, and the real part of the product then splits: item 1. Items 2 and 3 are item 1 with $P = Q = {I}$, and item 4 is a computation in the entries.

## Lean

Formalized as [`MIPRE.BipartiteModel.bornProb_expand_smulKron`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.bornProb_expand_smulKron), [`MIPRE.BipartiteModel.stateSqNorm_expand_smulKron_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.stateSqNorm_expand_smulKron_one), [`MIPRE.BipartiteModel.swap_stateSqNorm_expand_smulKron_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.swap_stateSqNorm_expand_smulKron_one), [`MIPRE.BipartiteModel.norm_expand_state`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.norm_expand_state), [`MIPRE.IsPVMIn.smulKron`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVMIn.smulKron).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1268](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1268)
