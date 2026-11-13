---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.OnPropertyTWanted.OnPropertyT.Laplacian, MathlibExt.GroupTheory.OnPropertyTWanted.OnPropertyT.groupRingInvolution, MathlibExt.GroupTheory.OnPropertyTWanted.OnPropertyT.PropertyT, MathlibExt.GroupTheory.OnPropertyTWanted.OnPropertyT.theorem_1
statement: formalized
---

# Property (T) for automorphism groups of free groups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/property-t-for-automorphism-groups-of-free-group/index.html).

## Laplacian of a finite subset of a group

For a group $G$ and a finite subset
$S \subseteq G$, the Laplacian of $S$ is the element $\Delta_S = |S| - \sum_{s \in S} s$ of the
real group ring $\mathbb{R}G$, where $|S|$ is the number of elements of $S$, taken as $|S|$ times
the identity element of $\mathbb{R}G$. When $S$ is a symmetric generating set of $G$, this is the
Laplacian of Equation (1) in the paper of Kaluba, Kielak and Nowak on property (T) for
$\operatorname{Aut}(F_n)$ and $\operatorname{SL}_n(\mathbb{Z})$.

Formalized by `MathlibExt.GroupTheory.OnPropertyTWanted.OnPropertyT.Laplacian`, a definition declared in [WantedExt/GroupTheory/OnPropertyTWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OnPropertyTWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/property-t-for-automorphism-groups-of-free-group/index.html#laplacian).

## Involution of the real group ring

For a group $G$, the involution of the real group ring
$\mathbb{R}G$ is the $\mathbb{R}$-linear map $\mathbb{R}G \to \mathbb{R}G$ that sends
$\sum_{g \in G} a_g g$ to $\sum_{g \in G} a_g g^{-1}$, that is, the linear extension of inversion
on $G$.

Formalized by `MathlibExt.GroupTheory.OnPropertyTWanted.OnPropertyT.groupRingInvolution`, a definition declared in [WantedExt/GroupTheory/OnPropertyTWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OnPropertyTWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/property-t-for-automorphism-groups-of-free-group/index.html#group-ring-involution).

## Property (T)

Let $G$ be a group. For a finite subset $S \subseteq G$, write
$\Delta_S = |S| - \sum_{s \in S} s$ for the Laplacian of $S$ in the real group ring $\mathbb{R}G$,
and write $\xi \mapsto \xi^{\star}$ for the involution of $\mathbb{R}G$ that extends inversion on
$G$ linearly. The group $G$ has Kazhdan's property (T) when there exist a finite subset
$S \subseteq G$ with $S^{-1} = S$ that generates $G$, a real number $\lambda > 0$, and a finite set
$\Xi$ of elements of $\mathbb{R}G$ such that
$\Delta_S^2 - \lambda \Delta_S = \sum_{\xi \in \Xi} \xi^{\star} \xi$.

This is Ozawa's characterization of property (T) for finitely generated groups, used as the
definition in Equation (2) of Kaluba, Kielak and Nowak.

Formalized by `MathlibExt.GroupTheory.OnPropertyTWanted.OnPropertyT.PropertyT`, a definition declared in [WantedExt/GroupTheory/OnPropertyTWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OnPropertyTWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/property-t-for-automorphism-groups-of-free-group/index.html#property-t).

## Property (T) for automorphism groups of free groups of rank at least 6

For every natural
number $n \ge 6$, the automorphism group $\operatorname{Aut}(F_n)$ of the free group $F_n$ on $n$
generators has property (T).

## Sources

- M. Kaluba, D. Kielak, and P. W. Nowak, `On property (T) for Aut(F_n) and SL_n(Z)`, Annals of Math, 193 (2) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_on_property_t` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.OnPropertyTWanted.OnPropertyT.theorem_1` is written with `theorem_wanted` in [WantedExt/GroupTheory/OnPropertyTWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OnPropertyTWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/property-t-for-automorphism-groups-of-free-group/index.html#theorem-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Property (T) for automorphism groups of free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/property-t-for-automorphism-groups-of-free-group/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/geometric-group-theory/property-t-for-automorphism-groups-of-free-group)
