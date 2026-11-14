---
declaration: proposition
origin: cited
lean: ConNF.BaseApprox.typical_permutative, ConNF.BaseApprox.atoms_permutative
statement: formalized
proof: formalized
---

# atomGraph_permutative

The graphs $\psi^{T{\mathcal A}}$ and $\psi^{\mathcal A}$ are permutative.

## Depends on

- [atom graph of an approximation](def-atomgraph.md)

## Proof depends on

- [atomGraph_inv](prop-atomgraph-inv.md)

## Proof

The typical atom graph is injective, because the equation $h_{L_\psi}(i)^\circ = L$ can be used to establish the the parameters of the relevant $h$ maps coincide. Furthermore, we can use the fact that $\psi^{\mathcal L}$ has equal image and coimage to produce images of any image element of this relation. We then appeal to symmetry using [Proposition atomGraph_inv](prop-atomgraph-inv.md) to conclude that $\psi^{T{\mathcal A}}$ is permutative.

The (co)image of $\psi^{T{\mathcal A}}$ is

$$
\bigcup_{L \in \operatorname{\mathsf{coim}} \psi^{\mathcal L}} L_\psi = \bigcup_{L \in \operatorname{\mathsf{coim}} \psi^{\mathcal L}} (\operatorname{\mathsf{LS}}(L) \setminus \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}})
$$

which is clearly disjoint from the coimage of $\psi^{E{\mathcal A}}$. (This result should of course be its own lemma.) So $\psi^{\mathcal A}$ is permutative by one of the results of [Proposition relation_results](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/auxiliary.tex#L33).

## Lean

Formalized as [`ConNF.BaseApprox.typical_permutative`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseApprox.typical_permutative), [`ConNF.BaseApprox.atoms_permutative`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseApprox.atoms_permutative).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 41](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L41)
