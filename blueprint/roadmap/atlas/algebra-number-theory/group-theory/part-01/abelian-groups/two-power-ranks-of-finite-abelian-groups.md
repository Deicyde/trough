---
declaration: section
origin: cited
lean: AbelianGroup.twoPowerImage, AbelianGroup.higherTwoPowerLayer, AbelianGroup.higherTwoPowerRank, AbelianGroup.fourRank
statement: formalized
proof: formalized
---

# Two-power ranks of finite abelian groups

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/two-power-ranks-of-finite-abelian-groups/index.html).

## The subgroup $2^kA$

For an abelian group $A$, written additively, and a natural number
$k$, $2^kA$ is the subgroup $\{2^k a : a \in A\}$ of $A$, the image of multiplication by $2^k$.

Formalized by `AbelianGroup.twoPowerImage`, a definition declared in [MathlibExt/GroupTheory/TwoPowerRank.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/TwoPowerRank.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/two-power-ranks-of-finite-abelian-groups/index.html#two-power-image).

## The two-power layer $2^{j-1}A / 2^jA$

For an abelian group $A$, written additively, and a
natural number $j$, this is the quotient group $2^{j-1}A / 2^jA$, where $2^kA$ denotes the
subgroup $\{2^k a : a \in A\}$ and $2^jA \subseteq 2^{j-1}A$. For $j = 0$, where $j - 1$ is
read as $0$, it is the trivial quotient $A / A$.

Formalized by `AbelianGroup.higherTwoPowerLayer`, an abbreviation declared in [MathlibExt/GroupTheory/TwoPowerRank.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/TwoPowerRank.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/two-power-ranks-of-finite-abelian-groups/index.html#higher-two-power-layer).

## The $2^j$-rank of a finite abelian group

Let $A$ be a finite abelian group, written
additively, and let $j \ge 1$ be an integer. Writing $2^kA$ for the subgroup
$\{2^k a : a \in A\}$, the $2^j$-rank of $A$ is the dimension over $\mathbb{F}_2$ of the
quotient $2^{j-1}A / 2^jA$, which is an $\mathbb{F}_2$-vector space because $2$ kills it.

Formalized by `AbelianGroup.higherTwoPowerRank`, a definition declared in [MathlibExt/GroupTheory/TwoPowerRank.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/TwoPowerRank.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/two-power-ranks-of-finite-abelian-groups/index.html#higher-two-power-rank).

## The $4$-rank of a finite abelian group

For a finite abelian group $A$, written
additively, the $4$-rank of $A$ is the dimension over $\mathbb{F}_2$ of the quotient $2A / 4A$,
where $2A = \{2a : a \in A\}$ and $4A = \{4a : a \in A\}$; it is the $2^j$-rank of $A$ for
$j = 2$.

Formalized by `AbelianGroup.fourRank`, an abbreviation declared in [MathlibExt/GroupTheory/TwoPowerRank.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/TwoPowerRank.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/two-power-ranks-of-finite-abelian-groups/index.html#four-rank).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Two-power ranks of finite abelian groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/two-power-ranks-of-finite-abelian-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/abelian-groups/two-power-ranks-of-finite-abelian-groups)
