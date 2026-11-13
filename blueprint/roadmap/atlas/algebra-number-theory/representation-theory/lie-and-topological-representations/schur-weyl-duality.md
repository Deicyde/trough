---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SchurWeylWanted.RepresentationTheory.symAction, MathlibExt.GroupTheory.SchurWeylWanted.RepresentationTheory.glAction, MathlibExt.GroupTheory.SchurWeylWanted.RepresentationTheory.symAction_range_eq_centralizer_glAction, MathlibExt.GroupTheory.SchurWeylWanted.RepresentationTheory.glAction_range_eq_centralizer_symAction
statement: formalized
---

# Schur–Weyl duality

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/schur-weyl-duality/index.html).

## Permutation action of the symmetric group on tensor powers

Let $R$ be a commutative
semiring, $M$ an $R$-module and $k$ a natural number. The symmetric group $S_k$ of permutations of
$\{1, \dots, k\}$ acts on the $k$-th tensor power $M^{\otimes k}$ by permuting tensor factors: this
is the monoid homomorphism from $S_k$ to the $R$-linear endomorphisms of $M^{\otimes k}$ that sends
$\sigma$ to the map $v_1 \otimes \cdots \otimes v_k \mapsto
v_{\sigma^{-1}(1)} \otimes \cdots \otimes v_{\sigma^{-1}(k)}$.

Formalized by `MathlibExt.GroupTheory.SchurWeylWanted.RepresentationTheory.symAction`, a definition declared in [WantedExt/GroupTheory/SchurWeylWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SchurWeylWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/schur-weyl-duality/index.html#sym-action).

## Diagonal action of the general linear group on tensor powers

Let $R$ be a commutative
semiring, $M$ an $R$-module and $k$ a natural number. Write $\mathrm{GL}(M)$ for the group of
invertible $R$-linear endomorphisms of $M$. The diagonal action of $\mathrm{GL}(M)$ on the $k$-th
tensor power $M^{\otimes k}$ is the monoid homomorphism from $\mathrm{GL}(M)$ to the
$R$-linear endomorphisms of $M^{\otimes k}$ that sends $g$ to $g^{\otimes k}$, so that
$g \cdot (v_1 \otimes \cdots \otimes v_k) = g v_1 \otimes \cdots \otimes g v_k$.

Formalized by `MathlibExt.GroupTheory.SchurWeylWanted.RepresentationTheory.glAction`, a definition declared in [WantedExt/GroupTheory/SchurWeylWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SchurWeylWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/schur-weyl-duality/index.html#gl-action).

## Schur–Weyl duality: the symmetric group side

Let $R$ be a field, $M$ a finite-dimensional
vector space over $R$, and $k$ a natural number such that $k!$ is invertible in $R$. In the
algebra of $R$-linear endomorphisms of the tensor power $M^{\otimes k}$, the subalgebra generated
by the image of the action of the symmetric group $S_k$ by permuting tensor factors equals the
centralizer of the image of the diagonal action $g \mapsto g^{\otimes k}$ of $\mathrm{GL}(M)$.

## Sources

- H. Weyl, The Classical Groups, 1939; I. Schur, Über die rationalen Darstellungen der allgemeinen linearen Gruppe, 1927. Problem `symAction_range_eq_centralizer_glAction` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.SchurWeylWanted.RepresentationTheory.symAction_range_eq_centralizer_glAction` is written with `theorem_wanted` in [WantedExt/GroupTheory/SchurWeylWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SchurWeylWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/schur-weyl-duality/index.html#sym-action-range-eq-centralizer-gl-actio).

## Schur–Weyl duality: the general linear side

Let $R$ be a field, $M$ a finite-dimensional
vector space over $R$, and $k$ a natural number such that $k!$ is invertible in $R$. In the
algebra of $R$-linear endomorphisms of the tensor power $M^{\otimes k}$, the subalgebra generated
by the image of the diagonal action $g \mapsto g^{\otimes k}$ of $\mathrm{GL}(M)$ equals the
centralizer of the image of the action of the symmetric group $S_k$ by permuting tensor factors.

## Sources

- H. Weyl, The Classical Groups, 1939; I. Schur, Über die rationalen Darstellungen der allgemeinen linearen Gruppe, 1927. Problem `glAction_range_eq_centralizer_symAction` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.SchurWeylWanted.RepresentationTheory.glAction_range_eq_centralizer_symAction` is written with `theorem_wanted` in [WantedExt/GroupTheory/SchurWeylWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SchurWeylWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/schur-weyl-duality/index.html#gl-action-range-eq-centralizer-sym-actio).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schur–Weyl duality](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/schur-weyl-duality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RepresentationTheory/lie-and-topological-representations/schur-weyl-duality)
