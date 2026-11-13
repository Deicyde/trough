---
declaration: section
origin: cited
lean: Cslib.Databases.join_project_eq_of_holdsIn, Cslib.Databases.SatisfiesOn, Cslib.Databases.LosslessJoin, Cslib.Databases.losslessJoin_of_derives, Cslib.Databases.derives_of_losslessJoin, Cslib.Databases.losslessJoin_iff, Cslib.Databases.joinUnit, Cslib.Databases.joinProjections
statement: formalized
proof: formalized
---

# Lossless decomposition and normal forms

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html).

## Heath's theorem

## Heath's theorem

If the dependency `R₁ ∩ R₂ → R₁` holds in a relation `r` over
`R₁ ∪ R₂`, then `r` is the natural join of its projections onto `R₁` and `R₂`.

Formalized by `Cslib.Databases.join_project_eq_of_holdsIn`, a theorem declared in [CSLibExt/Databases/NormalForms.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#join-project-eq-of-holds-in).

## Satisfying a set of dependencies on a scheme

A relation $r$ satisfies a finite set $F$ of
functional dependencies on a set $S$ of attributes when every dependency $X \to Y$ with
$X, Y \subseteq S$ that is derivable from $F$ by Armstrong's axioms holds in $r$.

Formalized by `Cslib.Databases.SatisfiesOn`, a definition declared in [CSLibExt/Databases/NormalForms.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#satisfies-on).

## Lossless decomposition into two schemes

Let $F$ be a finite set of functional
dependencies, let $R_1$ and $R_2$ be finite sets of attributes, and let $D$ be a type of values.
The decomposition of $R_1 \cup R_2$ into $R_1$ and $R_2$ is lossless for $F$ with values in $D$
when every relation $r$ over $R_1 \cup R_2$ with values in $D$ that satisfies $F$ on
$R_1 \cup R_2$ (every dependency $X \to Y$ with $X, Y \subseteq R_1 \cup R_2$ that is derivable
from $F$ by Armstrong's axioms holds in $r$) is the natural join of its projections:
$\pi_{R_1}(r) \bowtie \pi_{R_2}(r) = r$.

Formalized by `Cslib.Databases.LosslessJoin`, a definition declared in [CSLibExt/Databases/NormalForms.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#lossless-join).

## Lossless binary decompositions from derivable dependencies

Let $F$ be a finite set of
functional dependencies and let $R_1$, $R_2$ be sets of attributes. If $R_1 \cap R_2 \to R_1$ or
$R_1 \cap R_2 \to R_2$ is derivable from $F$ by Armstrong's axioms, then for every value type $D$
the decomposition of $R_1 \cup R_2$ into $R_1$ and $R_2$ is lossless for $F$ with values in $D$.

Formalized by `Cslib.Databases.losslessJoin_of_derives`, a theorem declared in [CSLibExt/Databases/NormalForms.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#lossless-join-of-derives).

## Converse of the lossless-join test for two schemes

Let $F$ be a set of functional
dependencies, let $R_1$ and $R_2$ be schemes whose union is the set of all attributes, and let
$D$ be a value type containing at least two distinct elements. If the decomposition of
$R_1 \cup R_2$ into $R_1$ and $R_2$ is lossless for $F$ with values in $D$, then $F$ derives
$R_1 \cap R_2 \to R_1$ or $R_1 \cap R_2 \to R_2$.

Formalized by `Cslib.Databases.derives_of_losslessJoin`, a theorem declared in [CSLibExt/Databases/NormalForms.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#derives-of-lossless-join).

## Lossless binary decompositions

Let $F$ be a finite set of functional dependencies, let
$R_1$ and $R_2$ be sets of attributes whose union is the set of all attributes, and suppose that
the value type $D$ has two distinct elements. Then the decomposition into $R_1$ and $R_2$ is
lossless for $F$ with values in $D$ if and only if $R_1 \cap R_2 \to R_1$ or
$R_1 \cap R_2 \to R_2$ is derivable from $F$ by Armstrong's axioms.

Formalized by `Cslib.Databases.losslessJoin_iff`, a theorem declared in [CSLibExt/Databases/NormalForms.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#lossless-join-iff).

## Unit relation of the natural join

The relation containing only the empty tuple, the unit of the natural join.

Formalized by `Cslib.Databases.joinUnit`, a definition declared in [CSLibExt/Databases/NormalForms.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#join-unit).

## Join of the projections of a relation

For a relation $r$ (a finite set of tuples) and a
list of schemes $S_1, \dots, S_n$, this is the natural join of the projections
$\pi_{S_1} r, \dots, \pi_{S_n} r$, computed as
$\pi_{S_1} r \bowtie (\pi_{S_2} r \bowtie (\cdots \bowtie (\pi_{S_n} r \bowtie U)))$, where $U$ is
the relation containing only the empty tuple; for the empty list it is $U$.

Formalized by `Cslib.Databases.joinProjections`, a definition declared in [CSLibExt/Databases/NormalForms.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#join-projections).

## Union of a list of schemes

For a list $S_1, \dots, S_n$ of schemes (finite sets of
attributes), this is the union $S_1 \cup \dots \cup S_n$; for the empty list it is the empty set.

Formalized by `Cslib.Databases.schemaUnion`, a definition declared in [CSLibExt/Databases/NormalForms.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#schema-union).

## Membership in a join of projections

Let $r$ be a relation over a schema $R$ and let
$S_1, \dots, S_n$ be a list of schemes, each contained in $R$. A tuple $t$ belongs to the natural
join of the projections $\pi_{S_1} r, \dots, \pi_{S_n} r$ if and only if $t$ is a tuple over
$S_1 \cup \dots \cup S_n$ and, for every $i$, the restriction of $t$ to $S_i$ belongs to
$\pi_{S_i} r$.

Formalized by `Cslib.Databases.mem_joinProjections`, a theorem declared in [CSLibExt/Databases/NormalForms.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#mem-join-projections).

## Boyce–Codd normal form

A scheme $S$ is in Boyce–Codd normal form for a set $F$ of
functional dependencies when, for every dependency $X \to Y$ derivable from $F$ with
$X, Y \subseteq S$, either $Y \subseteq X$ or $F$ derives $X \to S$ (that is, $X$ is a superkey of
$S$).

Formalized by `Cslib.Databases.IsBCNF`, a definition declared in [CSLibExt/Databases/NormalForms.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#is-bcnf).

## BCNF violations

Let $F$ be a set of functional dependencies and $S$ a scheme, and write
$X^+$ for the attribute closure of a set $X$ of attributes under $F$. A set $X \subseteq S$
violates BCNF in $S$ when $S \not\subseteq X^+$ and $X^+ \cap S \not\subseteq X$, that is, when
the closure $X^+ \cap S$ of $X$ within $S$ is neither $X$ nor $S$.

Formalized by `Cslib.Databases.IsBCNFViolation`, a definition declared in [CSLibExt/Databases/NormalForms.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#is-bcnfviolation).

## Candidate BCNF violations

Given a list $l$ of attributes and a set $S$ of attributes, the
candidate violations of BCNF in $S$ are all subsets of the set of attributes that occur in $l$ and
lie in $S$, listed once each. Duplicates in $l$ are removed first, so there are $2^k$ candidates
when $k$ distinct attributes of $l$ lie in $S$.

Formalized by `Cslib.Databases.bcnfCandidates`, a definition declared in [CSLibExt/Databases/NormalForms.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#bcnf-candidates).

## BCNF decomposition with bounded depth

Let $F$ be a set of functional dependencies, $l$ a
list of attributes, $n$ a natural number and $S$ a scheme. For $n = 0$ the result is the list $[S]$.
For $n > 0$, the candidate violations of BCNF in $S$ built from $l$ are searched in order for the
first $X$ that violates BCNF in $S$ for $F$. If there is none, the result is $[S]$. Otherwise, with
$X^+$ the attribute closure of $X$ under $F$, the result is the decomposition of $X^+ \cap S$
followed by the decomposition of $S \setminus (X^+ \setminus X)$, both computed with depth bound
$n - 1$.

Formalized by `Cslib.Databases.bcnfDecompose`, a definition declared in [CSLibExt/Databases/NormalForms.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#bcnf-decompose).

## BCNF decomposition

Let $F$ be a set of functional dependencies, $l$ a list of attributes
and $S$ a scheme. The BCNF decomposition of $S$ for $F$ and $l$ is the BCNF decomposition with
bounded depth run on $S$ with depth bound $|S|$. At each step, if some candidate violation of BCNF
in the current scheme $T$ built from $l$ violates BCNF in $T$ for $F$, the first such $X$ is used:
with $X^+$ the attribute closure of $X$ under $F$, $T$ is replaced by the decomposition of
$X^+ \cap T$ followed by the decomposition of $T \setminus (X^+ \setminus X)$. Otherwise, or once
the depth bound is reached, $T$ is kept as it is.

Formalized by `Cslib.Databases.bcnfDecomposition`, a definition declared in [CSLibExt/Databases/NormalForms.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#bcnf-decomposition).

## The BCNF decomposition is lossless

Let $F$ be a set of functional dependencies, $l$ a list
of attributes and $S$ a set of attributes, and let $r$ be a relation over $S$ that satisfies every
dependency $X \to Y$ derivable from $F$ with $X, Y \subseteq S$. Then $r$ is the natural join of
its projections onto the schemes of the BCNF decomposition of $S$ for $F$ and $l$.

Formalized by `Cslib.Databases.bcnfDecomposition_lossless`, a theorem declared in [CSLibExt/Databases/NormalForms.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#bcnf-decomposition-lossless).

## The BCNF decomposition produces BCNF schemes

Let $F$ be a set of functional dependencies
and $l$ a list containing every attribute. Then for every scheme $S$, every scheme in the BCNF
decomposition of $S$ for $F$ and $l$ is in Boyce–Codd normal form for $F$.

Formalized by `Cslib.Databases.isBCNF_of_mem_bcnfDecomposition`, a theorem declared in [CSLibExt/Databases/NormalForms.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#is-bcnf-of-mem-bcnf-decomposition).

## Equivalent sets of functional dependencies

Two sets $F$ and $G$ of functional dependencies
are equivalent when $F$ derives every dependency of $G$ and $G$ derives every dependency of $F$.

Formalized by `Cslib.Databases.Equivalent`, a definition declared in [CSLibExt/Databases/NormalForms.lean, line 529](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L529). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#equivalent).

## Projection of the dependency closure onto a scheme

For a finite set $F$ of functional
dependencies and a set $S$ of attributes, this is the finite set of all dependencies $X \to Y$
with $X, Y \subseteq S$ that are derivable from $F$ by Armstrong's axioms, that is, the projection
onto $S$ of the closure $F^+$ of $F$.

Formalized by `Cslib.Databases.projectFDs`, a definition declared in [CSLibExt/Databases/NormalForms.lean, line 537](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L537). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#project-fds).

## Dependency-preserving decompositions

A list $l$ of schemes is dependency-preserving for a
set $F$ of functional dependencies when every dependency of $F$ is derivable from the union, over
the schemes $S$ of $l$, of the sets of dependencies $X \to Y$ derivable from $F$ with
$X, Y \subseteq S$.

Formalized by `Cslib.Databases.DependencyPreserving`, a definition declared in [CSLibExt/Databases/NormalForms.lean, line 542](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L542). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#dependency-preserving).

## Synthesis

Given a list $G$ of functional dependencies and a set of attributes $K$, the
synthesized decomposition is the list of schemes consisting of $K$ followed by, for each
dependency $X \to Y$ of $G$ in order, the scheme $X \cup Y$.

Formalized by `Cslib.Databases.synthesize`, a definition declared in [CSLibExt/Databases/NormalForms.lean, line 550](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L550). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#synthesize).

## Synthesis is dependency-preserving

Let $F$ be a finite set of functional dependencies and
$G$ a list of functional dependencies equivalent to $F$ (each derives every dependency of the
other). Then for every set of attributes $K$, the decomposition synthesized from $G$ and $K$,
with one scheme $X \cup Y$ for each dependency $X \to Y$ of $G$ together with the scheme $K$, is
dependency-preserving for $F$.

Formalized by `Cslib.Databases.synthesize_dependencyPreserving`, a theorem declared in [CSLibExt/Databases/NormalForms.lean, line 584](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L584). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#synthesize-dependency-preserving).

## Synthesis is lossless

For a cover `G` of `F` and a superkey `K` of all attributes, every
relation over all attributes satisfying `F` is the join of its projections onto the synthesized
schemes.

Formalized by `Cslib.Databases.synthesize_lossless`, a theorem declared in [CSLibExt/Databases/NormalForms.lean, line 608](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/NormalForms.lean#L608). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html#synthesize-lossless).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lossless decomposition and normal forms](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/databases/lossless-decomposition-and-normal-forms)
