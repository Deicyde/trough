---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.ScottishBook15Point1Wanted.IsTypeF, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook15Point1Wanted.IsSphere, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook15Point1Wanted.IsBoundedSet, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook15Point1Wanted.AdmitsBanachNorm, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook15Point1Wanted.ScottishBookProblem15Point1Claim, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook15Point1Wanted.boundedSphereFImpliesB_refuted, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook26Wanted.IsTypeF, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook26Wanted.IsBoundedSet
statement: formalized
---

# F-spaces

11 results, 9 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/f-spaces/index.html).

## Spaces of type (F)

A real vector space $E$ with a topology is of type (F) when addition
$E \times E \to E$ and scalar multiplication $\mathbb{R} \times E \to E$ are continuous and there
is a metric $d$ on $E$ that is translation invariant, $d(x + z, y + z) = d(x, y)$ for all
$x, y, z \in E$, that induces the topology of $E$, and that is complete: every Cauchy sequence
for $d$ converges for $d$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook15Point1Wanted.IsTypeF`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook15Point1Wanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook15Point1Wanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/f-spaces/index.html#is-type-f).

## Spheres in the ray sense

Let $E$ be a real vector space. A set $K \subseteq E$ is a
sphere when $0 \notin K$ and for every $x \ne 0$ in $E$ there is exactly one real $t > 0$ with
$t x \in K$; that is, every open ray from the origin meets $K$ exactly once.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook15Point1Wanted.IsSphere`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook15Point1Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook15Point1Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/f-spaces/index.html#is-sphere).

## Sequentially bounded sets

Let $E$ be a real vector space with a topology. A set
$R \subseteq E$ is bounded when for every sequence $(x_n)$ of points of $R$ and every sequence
$(t_n)$ of real numbers with $t_n \to 0$, the sequence $(t_n x_n)$ tends to $0$ in $E$.

This is the definition of boundedness as printed in the statement of Scottish Book
Problem 15.1.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook15Point1Wanted.IsBoundedSet`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook15Point1Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook15Point1Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/f-spaces/index.html#is-bounded-set).

## Spaces of type (B)

A real vector space $E$ with a topology is of type (B) when there is
a function $\|\cdot\| : E \to \mathbb{R}$ with $\|x\| \ge 0$, with $\|x\| = 0$ exactly when
$x = 0$, with $\|x + y\| \le \|x\| + \|y\|$ and with $\|a x\| = |a| \, \|x\|$ for all
$x, y \in E$ and $a \in \mathbb{R}$, such that a set $U \subseteq E$ is open exactly when every
$x \in U$ has an $\varepsilon > 0$ with $y \in U$ whenever $\|y - x\| < \varepsilon$, and such
that every Cauchy sequence for $\|\cdot\|$ converges in $E$ for $\|\cdot\|$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook15Point1Wanted.AdmitsBanachNorm`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook15Point1Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook15Point1Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/f-spaces/index.html#admits-banach-norm).

## Scottish Book Problem 15.1

The claim of Mazur and Orlicz that every real vector space $E$
with a topology that is of type (F) and contains a bounded sphere is of type (B).

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook15Point1Wanted.ScottishBookProblem15Point1Claim`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook15Point1Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook15Point1Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/f-spaces/index.html#scottish-book-problem15-point1-claim).

## Negative answer to Scottish Book Problem 15.1

The Mazur–Orlicz claim of Problem 15.1 is
false: there is a real vector space $E$ with a topology that is of type (F) and contains a
bounded sphere, but is not of type (B).

## Sources

- S. Mazur and W. Orlicz, Problem 15.1 of the Scottish Book; the typescript itself records the negative answer (Ad 15.1, Mazur, May 1 1937) with the spaces `ℓ ^ p` and `L ^ p` for `0 < p < 1`, with quasi-norm given by the sum (respectively integral) of `|·| ^ p`, as counterexamples: they are of type (F), possess a bounded sphere, and are not normable, hence not of type (B).

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook15Point1Wanted.boundedSphereFImpliesB_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook15Point1Wanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook15Point1Wanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/f-spaces/index.html#bounded-sphere-fimplies-b-refuted).

## Spaces of type (F) in Scottish Book Problem 26

A real vector space $E$ with a topology
is of type (F) if there is a metric $d$ on $E$ that induces its topology, is translation
invariant, $d(x + z, y + z) = d(x, y)$ for all $x, y, z \in E$, and is complete, and if
addition $E \times E \to E$ and scalar multiplication $\mathbb{R} \times E \to E$ are
continuous.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook26Wanted.IsTypeF`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook26Wanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook26Wanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/f-spaces/index.html#is-type-f-2).

## Bounded sets in Scottish Book Problem 26

Let $E$ be a real vector space with a topology.
A set $R \subseteq E$ is bounded if for every sequence $(x_n)_{n \ge 0}$ of points of $R$ and
every real sequence $(t_n)_{n \ge 0}$ with $t_n \to 0$, we have $t_n x_n \to 0$ in $E$.

This sequential definition is the one printed in the problem statement.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook26Wanted.IsBoundedSet`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook26Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook26Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/f-spaces/index.html#is-bounded-set-2).

## Spaces of type $\{F_o\}$

A real vector space $E$ with a topology is of type $\{F_o\}$ if
it is of type (F) and, for every sequence $(x_n)_{n \ge 0}$ in $E$ with $x_n \to 0$ and every
real sequence $(t_n)_{n \ge 0}$ with $\sum_n |t_n| < \infty$, the series $\sum_n t_n x_n$
converges in $E$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook26Wanted.IsTypeFo`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook26Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook26Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/f-spaces/index.html#is-type-fo).

## Scottish Book Problem 26 (Mazur and Orlicz's claim)

The claim that for every real vector
space $E$ with a topology that is of type $\{F_o\}$ and every sequence $(F_n)_{n \ge 0}$ of
linear functionals $E \to \mathbb{R}$, if $F_n \to 0$ uniformly on every bounded set
$R \subseteq E$, then there is an open set $U \subseteq E$ containing $0$ on which
$F_n \to 0$ uniformly.

Here $F_n \to 0$ uniformly on a set $S$ means that for every $\varepsilon > 0$ there is $N$
with $|F_n(x)| < \varepsilon$ for all $n \ge N$ and all $x \in S$. The $F_n$ are only assumed
linear, not continuous.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook26Wanted.ScottishBookProblem26Claim`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook26Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook26Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/f-spaces/index.html#scottish-book-problem26-claim).

## Mazur and Orlicz's Problem 26 has a negative answer

The claim of Scottish Book Problem 26
is false: there are a real vector space $E$ with a topology, of type $\{F_o\}$, and a sequence
$(F_n)_{n \ge 0}$ of linear functionals $E \to \mathbb{R}$ that converges to $0$ uniformly on
every bounded subset of $E$ but does not converge to $0$ uniformly on any open set containing
$0$.

## Sources

- S. Mazur and W. Orlicz, Problem 26 of the Scottish Book (prize: one small beer); the typescript itself records the answer on the same page: "Ad 26, The answer is negative. M. Eidelheit, June 4, 1938."

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook26Wanted.foBoundedUniformNeighborhood_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook26Wanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook26Wanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/f-spaces/index.html#fo-bounded-uniform-neighborhood-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: F-spaces](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/f-spaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/f-spaces)
