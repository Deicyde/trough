---
declaration: section
origin: cited
lean: MetaMathlibExt.IsMulPiecewiseSyndetic, MetaMathlibExt.IsMulJSet, MetaMathlibExt.IsCentralSet, MetaMathlibExt.IsCSet, MetaMathlibExt.isMulPiecewiseSyndetic_univ, MetaMathlibExt.not_isMulPiecewiseSyndetic_empty, MetaMathlibExt.isMulJSet_univ, MetaMathlibExt.not_isMulJSet_empty
statement: formalized
proof: formalized
---

# Large sets in semigroups

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/large-sets-in-semigroups/index.html).

## Piecewise syndetic subsets of a semigroup

A set $D$ in a semigroup $S$ is piecewise
syndetic when there is a finite set $G \subseteq S$ such that for every finite set
$F \subseteq S$ there is $x \in S$ with $Fx \subseteq \bigcup_{t \in G} t^{-1} D$, where
$Fx = \{fx : f \in F\}$ and $t^{-1} D = \{s \in S : ts \in D\}$.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Section 2 (piecewise syndetic sets, after Hindman--Strauss).

Formalized by `MetaMathlibExt.IsMulPiecewiseSyndetic`, a definition declared in [MathlibExt/Combinatorics/SemigroupLargeness.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SemigroupLargeness.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/large-sets-in-semigroups/index.html#is-mul-piecewise-syndetic).

## J-sets in a semigroup

A set $D$ in a semigroup $S$ is a $J$-set when for every nonempty
finite set $F$ of sequences $f : \mathbb{N} \to S$, where $\mathbb{N} = \{0, 1, 2, \dots\}$,
there are an integer $m \ge 1$, elements $a_1, \dots, a_{m+1} \in S$ and indices
$t_1 < \dots < t_m$ in $\mathbb{N}$ such that
$a_1 f(t_1) a_2 f(t_2) \cdots a_m f(t_m) a_{m+1} \in D$ for every $f \in F$.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Definition 2.4(3).

Formalized by `MetaMathlibExt.IsMulJSet`, a definition declared in [MathlibExt/Combinatorics/SemigroupLargeness.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SemigroupLargeness.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/large-sets-in-semigroups/index.html#is-mul-jset).

## Central sets in a semigroup

Let $S$ be a semigroup and let $\beta S$ be the set of
ultrafilters on $S$, with the product for which $D \in pq$ exactly when
$\{x \in S : \{y \in S : xy \in D\} \in q\} \in p$. A two-sided ideal of $\beta S$ is a set
$I \subseteq \beta S$ with $rq \in I$ and $qr \in I$ for all $q \in I$ and $r \in \beta S$. A set
$D \subseteq S$ is central when some $p \in \beta S$ with $pp = p$ lies in every nonempty
two-sided ideal of $\beta S$ and has $D \in p$.

Equivalently, $D \in p$ for a minimal idempotent $p$, that is, an idempotent of the smallest
two-sided ideal $K(\beta S)$, which is itself a nonempty two-sided ideal lying in all of them.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Section 2.1 (central sets).

Formalized by `MetaMathlibExt.IsCentralSet`, a definition declared in [MathlibExt/Combinatorics/SemigroupLargeness.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SemigroupLargeness.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/large-sets-in-semigroups/index.html#is-central-set).

## C-sets in a semigroup

Let $S$ be a semigroup and let $\beta S$ be the set of ultrafilters
on $S$, with the product for which $D \in pq$ exactly when
$\{x \in S : \{y \in S : xy \in D\} \in q\} \in p$. Let $J(S)$ be the set of ultrafilters on $S$
all of whose members are $J$-sets. A set $D \subseteq S$ is a $C$-set when $D \in p$ for some
$p \in J(S)$ with $pp = p$.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Definition 2.4(3) (C-sets).

Formalized by `MetaMathlibExt.IsCSet`, a definition declared in [MathlibExt/Combinatorics/SemigroupLargeness.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SemigroupLargeness.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/large-sets-in-semigroups/index.html#is-cset).

## A nonempty semigroup is piecewise syndetic in itself

If $S$ is a nonempty semigroup,
then $S$ is a piecewise syndetic subset of $S$.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Section 2 (piecewise syndetic sets).

Formalized by `MetaMathlibExt.isMulPiecewiseSyndetic_univ`, a theorem declared in [MathlibExt/Combinatorics/SemigroupLargeness.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SemigroupLargeness.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/large-sets-in-semigroups/index.html#is-mul-piecewise-syndetic-univ).

## The empty set is not piecewise syndetic in a semigroup

In every semigroup $S$, the empty
subset of $S$ is not piecewise syndetic.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Section 2 (piecewise syndetic sets).

Formalized by `MetaMathlibExt.not_isMulPiecewiseSyndetic_empty`, a theorem declared in [MathlibExt/Combinatorics/SemigroupLargeness.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SemigroupLargeness.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/large-sets-in-semigroups/index.html#not-is-mul-piecewise-syndetic-empty).

## A nonempty semigroup is a J-set in itself

If $S$ is a nonempty semigroup, then $S$ is a
$J$-set in $S$.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Definition 2.4(3).

Formalized by `MetaMathlibExt.isMulJSet_univ`, a theorem declared in [MathlibExt/Combinatorics/SemigroupLargeness.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SemigroupLargeness.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/large-sets-in-semigroups/index.html#is-mul-jset-univ).

## The empty set is not a J-set in a nonempty semigroup

If $S$ is a nonempty semigroup, then
the empty subset of $S$ is not a $J$-set.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Definition 2.4(3).

Formalized by `MetaMathlibExt.not_isMulJSet_empty`, a theorem declared in [MathlibExt/Combinatorics/SemigroupLargeness.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SemigroupLargeness.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/large-sets-in-semigroups/index.html#not-is-mul-jset-empty).

## The empty set is not central in a semigroup

In every semigroup $S$, the empty subset of
$S$ is not central.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Section 2.1 (central sets).

Formalized by `MetaMathlibExt.not_isCentralSet_empty`, a theorem declared in [MathlibExt/Combinatorics/SemigroupLargeness.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SemigroupLargeness.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/large-sets-in-semigroups/index.html#not-is-central-set-empty).

## The empty set is not a C-set in a semigroup

In every semigroup $S$, the empty subset of
$S$ is not a $C$-set.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Definition 2.4(3) (C-sets).

Formalized by `MetaMathlibExt.not_isCSet_empty`, a theorem declared in [MathlibExt/Combinatorics/SemigroupLargeness.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SemigroupLargeness.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/large-sets-in-semigroups/index.html#not-is-cset-empty).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Large sets in semigroups](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/large-sets-in-semigroups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/ramsey-theory/structural-ramsey/large-sets-in-semigroups)
