---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.GroupLawsShared.LawConsequence, MathlibExt.GroupTheory.GroupLawsShared.HasIndependentLawBasis, MathlibExt.GroupTheory.GroupLawsShared.QuasiIdentityConsequence, MathlibExt.GroupTheory.GroupLawsShared.HasIndependentQuasiIdentityBasis
statement: formalized
proof: formalized
---

# Independent bases of laws

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/independent-bases-of-laws/index.html).

## Consequence of a set of laws

Let $F$ be the free group on countably many generators
$x_0, x_1, x_2, \dots$, let $W \subseteq F$ be a set of laws and let $w \in F$. Then $w$ is a
consequence of $W$ if $w$ holds in every group $G$ satisfying all laws in $W$: whenever every
homomorphism $F \to G$ sends each element of $W$ to $1$, every homomorphism $F \to G$ sends $w$
to $1$.

Formalized by `MathlibExt.GroupTheory.GroupLawsShared.LawConsequence`, a definition declared in [WantedExt/GroupTheory/GroupLawsShared.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/GroupLawsShared.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/independent-bases-of-laws/index.html#law-consequence).

## Independent basis of laws

Let $F$ be the free group on countably many generators
$x_0, x_1, x_2, \dots$ and let $W \subseteq F$ be a set of laws. The variety defined by $W$ has an
independent basis of identities if there is a set $B \subseteq F$ of laws such that a law is a
consequence of $B$ exactly when it is a consequence of $W$, and no $b \in B$ is a consequence of
$B \setminus \{b\}$.

Formalized by `MathlibExt.GroupTheory.GroupLawsShared.HasIndependentLawBasis`, a definition declared in [WantedExt/GroupTheory/GroupLawsShared.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/GroupLawsShared.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/independent-bases-of-laws/index.html#has-independent-law-basis).

## Consequence of a set of quasi-identities

Let $Q$ be a set of quasi-identities and $q$ a
quasi-identity. Then $q$ is a consequence of $Q$ if $q$ holds in every group in which all members
of $Q$ hold.

Formalized by `MathlibExt.GroupTheory.GroupLawsShared.QuasiIdentityConsequence`, a definition declared in [WantedExt/GroupTheory/GroupLawsShared.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/GroupLawsShared.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/independent-bases-of-laws/index.html#quasi-identity-consequence).

## Independent basis of quasi-identities

The quasi-identities of a group $G$ have an
independent basis if there is a set $B$ of quasi-identities such that a quasi-identity is a
consequence of $B$ exactly when it holds in $G$, and no $b \in B$ is a consequence of
$B \setminus \{b\}$.

Formalized by `MathlibExt.GroupTheory.GroupLawsShared.HasIndependentQuasiIdentityBasis`, a definition declared in [WantedExt/GroupTheory/GroupLawsShared.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/GroupLawsShared.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/independent-bases-of-laws/index.html#has-independent-quasi-identity-basis).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Independent bases of laws](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/independent-bases-of-laws/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/varieties-and-equations/independent-bases-of-laws)
