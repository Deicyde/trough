---
declaration: section
origin: cited
lean: MetaMathlibExt.SubsetModFinite, MetaMathlibExt.IsPIdeal, MetaMathlibExt.IsOrthogonalTo, MetaMathlibExt.PIdealDichotomy
statement: formalized
proof: formalized
---

# P-ideal dichotomy

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/p-ideal-dichotomy/index.html).

## Inclusion modulo finite

For subsets $a$ and $b$ of a set $\alpha$, $a \subseteq^* b$
($a$ is almost contained in $b$) if the difference $a \setminus b$ is finite.

Formalized by `MetaMathlibExt.SubsetModFinite`, a definition declared in [MathlibExt/SetTheory/Dichotomies/PIdeal.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Dichotomies/PIdeal.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/p-ideal-dichotomy/index.html#subset-mod-finite).

## P-ideal of countable sets

A family $I$ of subsets of a set $\alpha$ is a P-ideal of
countable sets if every member of $I$ is countable, every subset of a member of $I$ is in $I$,
every finite subset of $\alpha$ is in $I$, $I$ is closed under binary unions, and for every
sequence $(a_n)_{n \in \mathbb{N}}$ of members of $I$ there is $b \in I$ with $a_n \subseteq^* b$
(that is, $a_n \setminus b$ is finite) for every $n$.

Formalized by `MetaMathlibExt.IsPIdeal`, a structure declared in [MathlibExt/SetTheory/Dichotomies/PIdeal.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Dichotomies/PIdeal.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/p-ideal-dichotomy/index.html#is-pideal).

## Orthogonality to a family of sets

Let $I$ be a family of subsets of a set $\alpha$. A
set $X \subseteq \alpha$ is orthogonal to $I$ if $X \cap a$ is finite for every $a \in I$.

Formalized by `MetaMathlibExt.IsOrthogonalTo`, a definition declared in [MathlibExt/SetTheory/Dichotomies/PIdeal.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Dichotomies/PIdeal.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/p-ideal-dichotomy/index.html#is-orthogonal-to).

## P-ideal dichotomy

The P-ideal dichotomy (PID): for every P-ideal I of countable subsets of an uncountable
set, either some uncountable set has all its countable subsets in I, or the whole set is a
countable union of sets orthogonal to I.

Formalized by `MetaMathlibExt.PIdealDichotomy`, a definition declared in [MathlibExt/SetTheory/Dichotomies/PIdeal.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Dichotomies/PIdeal.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/p-ideal-dichotomy/index.html#p-ideal-dichotomy).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: P-ideal dichotomy](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/p-ideal-dichotomy/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/SetTheory/forcing/p-ideal-dichotomy)
