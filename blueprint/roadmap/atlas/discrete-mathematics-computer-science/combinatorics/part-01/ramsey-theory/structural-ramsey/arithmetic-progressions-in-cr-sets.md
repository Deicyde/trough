---
declaration: section
origin: cited
lean: MetaMathlibExt.IsAddThick, MetaMathlibExt.IsAddPiecewiseSyndetic, MetaMathlibExt.IsJSet, MetaMathlibExt.IsCRSet, MetaMathlibExt.IsEssentialCRSet, MetaMathlibExt.isAddThick_univ, MetaMathlibExt.not_isAddThick_empty, MetaMathlibExt.isAddPiecewiseSyndetic_univ
statement: formalized
---

# Arithmetic progressions in CR-sets

28 results, 15 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html).

## Thick set in a commutative semigroup

A subset $A$ of a commutative semigroup $(S, +)$ is
thick when for every finite set $E \subseteq S$ there is an $x \in S$ with $E + x \subseteq A$,
that is, $e + x \in A$ for every $e \in E$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Section 1 (definition of thick sets).

Formalized by `MetaMathlibExt.IsAddThick`, a definition declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#is-add-thick).

## Piecewise syndetic set in a commutative semigroup

A subset $A$ of a commutative semigroup
$(S, +)$ is piecewise syndetic when there is a finite set $F \subseteq S$ such that the union
$\bigcup_{t \in F} (-t + A)$ is thick, where $-t + A = \{s \in S : t + s \in A\}$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Section 1 (definition of piecewise syndetic sets).

Formalized by `MetaMathlibExt.IsAddPiecewiseSyndetic`, a definition declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#is-add-piecewise-syndetic).

## J-sets in commutative semigroups

Let $S$ be a commutative semigroup and let
$\mathbb{N} = \{0, 1, 2, \dots\}$. A set $A \subseteq S$ is a $J$-set when for every finite set
$F$ of sequences $f \colon \mathbb{N} \to S$ there are $a \in S$ and a nonempty finite set
$H \subseteq \mathbb{N}$ such that $a + \sum_{n \in H} f(n) \in A$ for every $f \in F$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Definition 1.

Formalized by `MetaMathlibExt.IsJSet`, a definition declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#is-jset).

## CR-set

A subset $A$ of a commutative semigroup $(S, +)$ is a CR-set (combinatorially rich)
when for every natural number $n$, including $n = 0$, there is a natural number $r$ such that for
every $r \times n$ matrix $(m_{ij})$ with entries in $S$ there are a nonempty set
$\alpha \subseteq \{1, \ldots, r\}$ and an element $s \in S$ such that
$s + \sum_{i \in \alpha} m_{ij} \in A$ for every column $j \in \{1, \ldots, n\}$.

The paper takes $n \ge 1$. Allowing $n = 0$ adds the requirement that $S$ be nonempty, the
paper's implicit convention: over an empty $S$ every case $n \ge 1$ holds vacuously (take
$r = 1$; there is no matrix), so without it $\emptyset$ would be a CR-set of the empty
semigroup. Over a nonempty $S$ the two definitions agree.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Definition 2.

Formalized by `MetaMathlibExt.IsCRSet`, a definition declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#is-crset).

## Essential CR-set

Let $(S, +)$ be a commutative semigroup, and add ultrafilters on $S$ by
the rule that $E \in p + q$ if and only if $\{x \in S : \{y \in S : x + y \in E\} \in q\} \in p$.
A subset $A$ of $S$ is an essential CR-set when there is an ultrafilter $p$ on $S$ with
$p + p = p$, all of whose members are CR-sets, such that $A \in p$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Section 2 (definition of essential CR-sets before Theorem 7).

Formalized by `MetaMathlibExt.IsEssentialCRSet`, a definition declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#is-essential-crset).

## The whole commutative semigroup is thick

If $S$ is a nonempty commutative semigroup,
then $S$ itself is a thick subset of $S$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Section 1 (definition of thick sets).

Formalized by `MetaMathlibExt.isAddThick_univ`, a theorem declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#is-add-thick-univ).

## The empty set is not thick

In a nonempty commutative semigroup, the empty set is not
thick.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Section 1 (definition of thick sets).

Formalized by `MetaMathlibExt.not_isAddThick_empty`, a theorem declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#not-is-add-thick-empty).

## The whole commutative semigroup is piecewise syndetic

If $S$ is a nonempty commutative
semigroup, then $S$ itself is a piecewise syndetic subset of $S$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Section 1 (definition of piecewise syndetic sets).

Formalized by `MetaMathlibExt.isAddPiecewiseSyndetic_univ`, a theorem declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#is-add-piecewise-syndetic-univ).

## The whole semigroup is a J-set

In every nonempty commutative semigroup $S$, the set $S$
itself is a $J$-set.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Definition 1.

Formalized by `MetaMathlibExt.isJSet_univ`, a theorem declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#is-jset-univ).

## The whole commutative semigroup is a CR-set

If $S$ is a nonempty commutative semigroup,
then $S$ itself is a CR-set in $S$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Definition 2.

Formalized by `MetaMathlibExt.isCRSet_univ`, a theorem declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#is-crset-univ).

## The empty set is not a CR-set

In every commutative semigroup, the empty set is not a
CR-set.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Definition 2.

Formalized by `MetaMathlibExt.not_isCRSet_empty`, a theorem declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#not-is-crset-empty).

## Families with the Ramsey property

Let $S$ be a set. A collection $F$ of subsets of $S$ is
a family with the Ramsey property when $F$ is nonempty, $\emptyset \notin F$, $F$ is closed under
supersets (if $A \in F$ and $A \subseteq B$, then $B \in F$), and whenever $A \cup B \in F$, then
$A \in F$ or $B \in F$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Section 2 (families and the Ramsey property).

Formalized by `MetaMathlibExt.IsRamseyFamily`, a definition declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#is-ramsey-family).

## The set β(F) of ultrafilters inside a family

For a family $\mathcal F$ of subsets of a
set $S$, $\beta(\mathcal F)$ is the set of ultrafilters $p$ on $S$ all of whose members lie in
$\mathcal F$, that is, $A \in \mathcal F$ for every $A \in p$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Section 2 (definition of `β(F)`).

Formalized by `MetaMathlibExt.betaFamily`, a definition declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#beta-family).

## Membership in β(F)

Let $F$ be a collection of subsets of a set $S$ and let $p$ be an
ultrafilter on $S$. Then $p \in \beta(F)$ if and only if every member of $p$ belongs to $F$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Section 2 (definition of `β(F)`).

Formalized by `MetaMathlibExt.mem_betaFamily`, a theorem declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#mem-beta-family).

## β of the nonempty sets is all of βS

For every set $S$, every ultrafilter on $S$ lies in
$\beta(\mathcal F)$, where $\mathcal F$ is the family of all nonempty subsets of $S$; that is,
$\beta(\mathcal F) = \beta S$, the set of all ultrafilters on $S$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Section 2 (definition of `β(F)`).

Formalized by `MetaMathlibExt.betaFamily_nonempty_sets`, a theorem declared in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#beta-family-nonempty-sets).

## Ultrafilters inside a Ramsey family form a closed set

Let $F$ be a family of subsets of a
set $S$ with the Ramsey property. Then the set $\beta(F)$ of ultrafilters on $S$ all of whose
members lie in $F$ is closed in the space $\beta S$ of all ultrafilters on $S$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Theorem 3.

Stated but not proved: `MetaMathlibExt.isClosed_betaFamily` is written with `theorem_wanted` in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#is-closed-beta-family).

## Theorem 3, part 2: a Ramsey family is the union of its ultrafilters

Let $F$ be a family
of subsets of a set $S$ with the Ramsey property, and let $\beta(F)$ be the set of ultrafilters on
$S$ all of whose members lie in $F$. Then a set $A \subseteq S$ lies in $F$ if and only if
$A \in p$ for some $p \in \beta(F)$; that is, $F = \bigcup \beta(F)$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Theorem 3.

Stated but not proved: `MetaMathlibExt.mem_iff_exists_mem_betaFamily` is written with `theorem_wanted` in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#mem-iff-exists-mem-beta-family).

## Nonempty closed sets of ultrafilters come from Ramsey families

Let $S$ be a set, let
$\beta S$ be the space of ultrafilters on $S$, and let $K$ be a nonempty closed subset of
$\beta S$. Let $\mathcal F_K$ be the collection of the sets $E \subseteq S$ with $E \in p$ for
some $p \in K$. Then $\mathcal F_K$ is a family with the Ramsey property, and
$\beta(\mathcal F_K) = K$, where $\beta(\mathcal F_K)$ is the set of ultrafilters on $S$ all of
whose members lie in $\mathcal F_K$.

The paper omits $K \ne \emptyset$; for $K = \emptyset$ the collection $\mathcal F_K$ is empty,
hence not a family.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Theorem 3.

Stated but not proved: `MetaMathlibExt.isRamseyFamily_and_betaFamily_eq_of_isClosed` is written with `theorem_wanted` in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#is-ramsey-family-and-beta-family-eq-of-i).

## β(F) contains an idempotent when it is a subsemigroup

Let $S$ be a semigroup and
$\mathcal F$ a family of subsets of $S$ with the Ramsey property, and multiply ultrafilters on
$S$ by $E \in pq$ iff $\{x \in S : \{y \in S : xy \in E\} \in q\} \in p$. If
$pq \in \beta(\mathcal F)$ for all $p, q \in \beta(\mathcal F)$, then there is
$p \in \beta(\mathcal F)$ with $pp = p$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Theorem 3.

Stated but not proved: `MetaMathlibExt.exists_idempotent_mem_betaFamily` is written with `theorem_wanted` in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#exists-idempotent-mem-beta-family).

## Left-ideal criterion for β(F)

Let $S$ be a semigroup and $\mathcal F$ a family of subsets
of $S$ with the Ramsey property. Multiply ultrafilters on $S$ by $E \in pq$ iff
$\{x \in S : \{y \in S : xy \in E\} \in q\} \in p$. Then $pq \in \beta(\mathcal F)$ for every
ultrafilter $p$ on $S$ and every $q \in \beta(\mathcal F)$ (that is, $\beta(\mathcal F)$ is a
left ideal of $\beta S$) if and only if $sE = \{se : e \in E\}$ lies in $\mathcal F$ for every
$s \in S$ and every $E \in \mathcal F$.

The paper's second sentence (right ideal iff right shift-invariant) is omitted: with this
convention it fails. Let $L$ be a minimal left ideal of $\beta\mathbb{N}$ and $\mathcal F_L$ the
family of sets belonging to some member of $L$. By the left half $\mathcal F_L$ is
shift-invariant ($\mathbb{N}$ is commutative), yet $L$ is not a right ideal, since a two-sided
ideal contains the smallest ideal $K(\beta\mathbb{N})$, a union of more than one minimal left
ideal.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Theorem 4.

Stated but not proved: `MetaMathlibExt.betaFamily_isLeftIdeal_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#beta-family-is-left-ideal-iff).

## Subsemigroup criterion for β(F)

Let $S$ be a semigroup and $\mathcal F$ a family of
subsets of $S$ with the Ramsey property. For $x \in S$ and $E \subseteq S$ write
$x^{-1}E = \{y \in S : xy \in E\}$, and multiply ultrafilters on $S$ by $E \in pq$ iff
$\{x \in S : x^{-1}E \in q\} \in p$. Then $pq \in \beta(\mathcal F)$ for all
$p, q \in \beta(\mathcal F)$ if and only if every $E \subseteq S$ has the following property: if
there is $A \in \mathcal F$ such that $\bigcap_{x \in H} x^{-1}E \in \mathcal F$ for every finite
$H \subseteq A$, then $E \in \mathcal F$.

The source's intersection $\bigcap_{q \in H} x^{-1}E$ is read as $\bigcap_{x \in H} x^{-1}E$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Theorem 5.

Stated but not proved: `MetaMathlibExt.betaFamily_isSubsemigroup_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#beta-family-is-subsemigroup-iff).

## Decreasing shift-closed sequences give essential sets

Let $S$ be a semigroup and let $F$
be a family of subsets of $S$ with the Ramsey property, and write $\beta(F)$ for the set of
ultrafilters on $S$ all of whose members lie in $F$. For $x \in S$ and $E \subseteq S$ write
$x^{-1}E = \{y \in S : xy \in E\}$, and multiply ultrafilters on $S$ by the rule that
$E \in p \cdot q$ if and only if $\{x \in S : x^{-1}E \in q\} \in p$. Suppose that
$p \cdot q \in \beta(F)$ whenever $p, q \in \beta(F)$. Let $A \subseteq S$, and let
$C_0 \supseteq C_1 \supseteq C_2 \supseteq \cdots$ be members of $F$ contained in $A$ such that
for every $n$ and every $x \in C_n$ there is an $m$ with $C_m \subseteq x^{-1}C_n$. Then some
$p \in \beta(F)$ satisfies $p \cdot p = p$ and $A \in p$; that is, $A$ is an essential $F$-set.

This is the implication (d) ⇒ (a) of the paper's Theorem 6; statements (b) (trees of functions)
and (c) (downward directed families) are omitted. The sequence is indexed from $0$ rather
than $1$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Theorem 6.

Stated but not proved: `MetaMathlibExt.exists_idempotent_mem_of_decreasing_sequence` is written with `theorem_wanted` in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#exists-idempotent-mem-of-decreasing-sequ).

## Essential F-sets contain shift-closed decreasing sequences (countable case)

Let $S$ be
a countable semigroup and $\mathcal F$ a family of subsets of $S$ with the Ramsey property. For
$x \in S$ and $E \subseteq S$ write $x^{-1}E = \{y \in S : xy \in E\}$, multiply ultrafilters on
$S$ by $E \in pq$ iff $\{x \in S : x^{-1}E \in q\} \in p$, and assume $pq \in \beta(\mathcal F)$
for all $p, q \in \beta(\mathcal F)$. If $A \subseteq S$ belongs to some $p \in \beta(\mathcal F)$
with $pp = p$ (an essential $\mathcal F$-set), then there are sets $C_0 \supseteq C_1 \supseteq
C_2 \supseteq \cdots$ in $\mathcal F$, all contained in $A$, such that for every $n$ and every
$x \in C_n$ there is $m$ with $C_m \subseteq x^{-1}C_n$.

Statements (b) (trees of functions) and (c) (downward directed families) of the paper are
omitted. The sequence is indexed from $0$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Theorem 6.

Stated but not proved: `MetaMathlibExt.exists_decreasing_sequence_of_idempotent_mem` is written with `theorem_wanted` in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#exists-decreasing-sequence-of-idempotent).

## Furstenberg–Glasner theorem on progressions in piecewise syndetic sets

If
$S \subseteq \mathbb{Z}$ is piecewise syndetic, then for every natural number $k$ the set of pairs
$(a, d) \in \mathbb{Z} \times \mathbb{Z}$ such that $a + i d \in S$ for all $i = 0, 1, \dots, k$
is piecewise syndetic in $\mathbb{Z} \times \mathbb{Z}$.

The paper takes $k \ge 1$; the case $k = 0$ is included.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Theorem 1.

Stated but not proved: `MetaMathlibExt.IsAddPiecewiseSyndetic.arithmeticProgressions_int` is written with `theorem_wanted` in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#arithmetic-progressions-int).

## Debnath–Goswami theorem on progressions in J-sets

Let $\mathbb{N}^+$ denote the
positive integers under addition. If $S \subseteq \mathbb{N}^+$ is a $J$-set, then for every
natural number $k$ the set of pairs $(a, d) \in \mathbb{N}^+ \times \mathbb{N}^+$ such that
$a + i d \in S$ for all $i = 0, 1, \dots, k$ is a $J$-set in $\mathbb{N}^+ \times \mathbb{N}^+$.

The paper writes $\mathbb{N}$ for the positive integers and takes $k \ge 1$; the case $k = 0$ is
included.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Theorem 2.

Stated but not proved: `MetaMathlibExt.IsJSet.arithmeticProgressions_pnat` is written with `theorem_wanted` in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#arithmetic-progressions-pnat).

## Essential CR-sets via decreasing sequences

Let $S$ be a countable commutative semigroup
and let $A \subseteq S$. Then $A$ is an essential CR-set if and only if there is a decreasing
sequence $C_0 \supseteq C_1 \supseteq C_2 \supseteq \cdots$ of CR-sets contained in $A$ such that
for every $n$ and every $x \in C_n$ there is an $m$ with $C_m \subseteq -x + C_n$, where
$-x + C_n = \{y \in S : x + y \in C_n\}$.

The sequence is indexed from $0$ rather than $1$.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Theorem 7.

Stated but not proved: `MetaMathlibExt.isEssentialCRSet_iff_exists_decreasing_sequence` is written with `theorem_wanted` in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#is-essential-crset-iff-exists-decreasing).

## Arithmetic progressions in CR-sets

If $A$ is a CR-set in a commutative semigroup
$(S, +)$ and $l$ is a natural number, then the set of pairs $(a, b) \in S \times S$ such that
$a, a + b, a + 2b, \dots, a + lb$ all lie in $A$ is a CR-set in $S \times S$. Here $a + ib$ is
$a$ followed by $i$ additions of $b$, since $S$ need not have a zero.

The paper takes $l \ge 1$; the case $l = 0$ is included.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Theorem 8.

Stated but not proved: `MetaMathlibExt.IsCRSet.arithmeticProgressions` is written with `theorem_wanted` in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#arithmetic-progressions).

## Arithmetic progressions in essential CR-sets of the positive integers

Let $\mathbb{N}^+$
denote the positive integers under addition. If $A \subseteq \mathbb{N}^+$ is an essential CR-set
and $l$ is a natural number, then the set of pairs $(a, b) \in \mathbb{N}^+ \times \mathbb{N}^+$
such that $a + i b \in A$ for all $i = 0, 1, \dots, l$ is an essential CR-set in
$\mathbb{N}^+ \times \mathbb{N}^+$.

The paper writes $\mathbb{N}$ for the positive integers and takes $l \ge 1$; the case $l = 0$ is
included.

## Sources

- De and Debnath, *Abundance of Arithmetic Progressions in CR-Sets*, INTEGERS 25 (2025), Article A4, Theorem 9.

Stated but not proved: `MetaMathlibExt.IsEssentialCRSet.arithmeticProgressions_pnat` is written with `theorem_wanted` in [WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CRSetArithmeticProgressionWanted.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html#arithmetic-progressions-pnat-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic progressions in CR-sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/ramsey-theory/structural-ramsey/arithmetic-progressions-in-cr-sets)
