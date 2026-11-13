---
declaration: section
origin: cited
lean: Cslib.Databases.FD, Cslib.Databases.FD.HoldsIn, Cslib.Databases.Satisfies, Cslib.Databases.Entails, Cslib.Databases.Derives, Cslib.Databases.Derives.sound, Cslib.Databases.Derives.decompose, Cslib.Databases.Derives.union
statement: formalized
proof: formalized
---

# Functional dependencies

30 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html).

## Functional dependency

A functional dependency $X \to Y$ over a type $A$ of attributes
consists of two finite sets of attributes $X, Y \subseteq A$: the determining attributes $X$
(its left side) and the determined attributes $Y$ (its right side).

Formalized by `Cslib.Databases.FD`, a structure declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#fd).

## A functional dependency holds in a relation

Let $A$ be a type of attributes and $V$ a
type of values. A functional dependency $X \to Y$ on $A$ holds in a relation $r$, a set of tuples
$A \to V$, when any two tuples $t, u \in r$ that agree on every attribute of $X$ also agree on
every attribute of $Y$.

Formalized by `Cslib.Databases.FD.HoldsIn`, a definition declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#holds-in).

## A relation satisfies a set of dependencies

Let $F$ be a finite set of functional
dependencies over attributes $A$, and let $r$ be a relation, given as a set of tuples $A \to V$
with values in a type $V$. Then $r$ satisfies $F$ when every dependency of $F$ holds in $r$.

Formalized by `Cslib.Databases.Satisfies`, a definition declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#satisfies).

## Entailment of functional dependencies

Let $A$ be a type of attributes. A finite set $F$
of functional dependencies on $A$ entails a functional dependency $f$ on $A$ when, for every
type $V$ and every relation $r$ with values in $V$ (a set of tuples $A \to V$) that satisfies
$F$, the dependency $f$ holds in $r$.

Formalized by `Cslib.Databases.Entails`, a definition declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#entails).

## Derivability with Armstrong's axioms

Let $F$ be a finite set of functional
dependencies over a set $A$ of attributes. Derivability from $F$ is the least property of
functional dependencies over $A$ such that, for all finite sets $X$, $Y$, $Z$ of attributes:
every dependency of $F$ is derivable; $X \to Y$ is derivable whenever $Y \subseteq X$
(reflexivity); if $X \to Y$ is derivable, then so is $X \cup Z \to Y \cup Z$ (augmentation);
and if $X \to Y$ and $Y \to Z$ are derivable, then so is $X \to Z$ (transitivity).

Formalized by `Cslib.Databases.Derives`, an inductive type declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#derives).

## Armstrong's axioms are sound

A derivable dependency holds in every relation satisfying
`F`.

Formalized by `Cslib.Databases.Derives.sound`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#sound).

## Decomposition rule

Let $F$ be a finite set of functional dependencies and $X$, $Y$, $Z$
finite sets of attributes with $Z \subseteq Y$. If $X \to Y$ is derivable from $F$ with
Armstrong's axioms, then so is $X \to Z$.

Formalized by `Cslib.Databases.Derives.decompose`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#decompose).

## Union rule

Let $F$ be a finite set of functional dependencies and $X, Y, Z$ finite sets
of attributes. If $X \to Y$ and $X \to Z$ are derivable from $F$ with Armstrong's axioms, then so
is $X \to Y \cup Z$.

Formalized by `Cslib.Databases.Derives.union`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#union).

## Pseudotransitivity rule

Let $F$ be a finite set of functional dependencies and
$X, Y, W, Z$ finite sets of attributes. If $X \to Y$ and $Y \cup W \to Z$ are derivable from $F$
with Armstrong's axioms, then so is $X \cup W \to Z$.

Formalized by `Cslib.Databases.Derives.pseudotrans`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#pseudotrans).

## Adding the left side to the right side

Let $F$ be a finite set of functional dependencies
and $X, Y$ finite sets of attributes. If $X \to Y$ is derivable from $F$ with Armstrong's axioms,
then so is $X \to X \cup Y$.

Formalized by `Cslib.Databases.Derives.union_left`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#union-left).

## One round of the attribute-closure algorithm

For a finite set $F$ of functional
dependencies and a finite set $Y$ of attributes, one closure round returns $Y$ together with the
right side of every dependency of $F$ whose left side is contained in $Y$, that is, the set
$Y \cup \bigcup \{R : (L \to R) \in F,\ L \subseteq Y\}$.

Formalized by `Cslib.Databases.closureStep`, a definition declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#closure-step).

## Iterated closure rounds

Let $F$ be a finite set of functional dependencies, $n$ a
natural number and $Y$ a finite set of attributes. The loop returns $Y$ if $n = 0$ or if one
closure round for $F$ leaves $Y$ unchanged; otherwise it returns the loop with $n - 1$ rounds
started from the result of one closure round applied to $Y$. Thus it repeats closure rounds from
$Y$ until nothing changes, for at most $n$ rounds.

Formalized by `Cslib.Databases.closureLoop`, a definition declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#closure-loop).

## Attribute closure

Let $A$ be a finite set of attributes, $F$ a finite set of functional
dependencies over $A$ and $X \subseteq A$. The attribute closure $X^+$ of $X$ under $F$ is
computed by the closure algorithm: starting from $X$, repeat closure rounds (each adds the right
side of every dependency of $F$ whose left side is already included) until nothing changes, for
at most $|A|$ rounds.

Formalized by `Cslib.Databases.attrClosure`, a definition declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#attr-closure).

## The attribute closure is a fixed point of a closure round

Let $A$ be a finite set of
attributes, $F$ a finite set of functional dependencies over $A$ and $X \subseteq A$. Applying
one closure round for $F$ to the attribute closure $X^+$ of $X$ under $F$ returns $X^+$.

Formalized by `Cslib.Databases.closureStep_attrClosure`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#closure-step-attr-closure).

## The attribute closure is closed under the dependencies

Let $F$ be a finite set of
functional dependencies over a finite set of attributes, $X$ a set of attributes and $X^+$ its
attribute closure under $F$. For every dependency $Y \to Z$ in $F$ with $Y \subseteq X^+$, also
$Z \subseteq X^+$.

Formalized by `Cslib.Databases.rhs_subset_attrClosure`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#rhs-subset-attr-closure).

## Closure witness relation

Let $A$ be a finite set of attributes, $F$ a finite set of
functional dependencies over $A$ and $X \subseteq A$. The closure witness relation for $X$ is the
relation with values in $\{\mathrm{true}, \mathrm{false}\}$ whose tuples are the tuple that is
$\mathrm{true}$ on every attribute and the tuple that is $\mathrm{true}$ exactly on the attribute
closure $X^+$ of $X$ under $F$. These two tuples agree exactly on $X^+$, and they coincide when
$X^+ = A$.

Formalized by `Cslib.Databases.closureWitnessRelation`, a definition declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#closure-witness-relation).

## The closure witness satisfies the dependencies

Let $F$ be a finite set of functional
dependencies on a finite set of attributes $A$. For every set $X \subseteq A$ of attributes, the
closure witness relation for $X$ under $F$ satisfies $F$.

Formalized by `Cslib.Databases.holdsIn_closureWitnessRelation`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#holds-in-closure-witness-relation).

## The closure algorithm decides derivability

Let $A$ be a finite set of attributes, $F$ a
finite set of functional dependencies over $A$ and $X, Y \subseteq A$. Then $X \to Y$ is
derivable from $F$ with Armstrong's axioms if and only if $Y \subseteq X^+$, where $X^+$ is the
attribute closure of $X$ under $F$ computed by the closure algorithm.

Formalized by `Cslib.Databases.derives_iff_subset_attrClosure`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#derives-iff-subset-attr-closure).

## The closure algorithm computes the attribute closure

Let $F$ be a finite set of
functional dependencies over a finite set of attributes and $X$ a set of attributes. An
attribute $a$ lies in the attribute closure $X^+$ of $X$ under $F$, as computed by the closure
algorithm, if and only if the dependency $X \to \{a\}$ is derivable from $F$ with Armstrong's
axioms.

Formalized by `Cslib.Databases.mem_attrClosure`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#mem-attr-closure).

## Completeness of Armstrong's axioms, two-tuple form

Let $A$ be a finite set of
attributes, $F$ a finite set of functional dependencies over $A$ and $f$ a functional
dependency over $A$. If $f$ holds in every relation with values in
$\{\mathrm{true}, \mathrm{false}\}$ that has at most two tuples and satisfies every dependency
of $F$, then $f$ is derivable from $F$ with Armstrong's axioms.

Formalized by `Cslib.Databases.derives_of_forall_two_tuple`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#derives-of-forall-two-tuple).

## Armstrong's theorem

Let $A$ be a finite set of attributes, $F$ a finite set of
functional dependencies over $A$ and $f$ a functional dependency over $A$. Then $f$ is
derivable from $F$ with Armstrong's axioms if and only if $F$ entails $f$, that is, $f$ holds
in every relation (with values in any type) that satisfies every dependency of $F$. In other
words, Armstrong's axioms are sound and complete for functional dependencies.

Formalized by `Cslib.Databases.derives_iff_entails`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#derives-iff-entails).

## Superkey

Let $F$ be a finite set of functional dependencies over a finite set of
attributes $A$. A set of attributes $K$ is a superkey for $F$ when the dependency $K \to A$ is
derivable from $F$ with Armstrong's axioms, that is, $K$ determines every attribute.

Formalized by `Cslib.Databases.IsSuperkey`, a definition declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#is-superkey).

## Candidate key

Let $F$ be a finite set of functional dependencies on a finite set of
attributes $A$. A set $K \subseteq A$ of attributes is a candidate key for $F$ when $K$ is a
superkey for $F$ and no proper subset of $K$ is a superkey for $F$.

Formalized by `Cslib.Databases.IsCandidateKey`, a definition declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#is-candidate-key).

## Supersets of superkeys are superkeys

Let $F$ be a finite set of functional dependencies
over a finite set of attributes. If $K$ is a superkey for $F$ and $K \subseteq K'$, then $K'$ is a
superkey for $F$.

Formalized by `Cslib.Databases.IsSuperkey.mono`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#mono).

## Tuples that agree on a superkey are equal

Let $F$ be a finite set of functional
dependencies on a finite set of attributes $A$, and let $K$ be a superkey for $F$. Let $V$ be a
type of values. If a relation $r$, a set of tuples $A \to V$, satisfies $F$, then any two tuples
$t, u \in r$ that agree on every attribute of $K$ are equal.

Formalized by `Cslib.Databases.IsSuperkey.eq_of_agree`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#eq-of-agree).

## Candidate keys are the superkeys minimal under single removals

Let $F$ be a finite set
of functional dependencies on a finite set of attributes $A$. A set $K \subseteq A$ of attributes
is a candidate key for $F$ if and only if $K$ is a superkey for $F$ and, for every $a \in K$, the
set $K \setminus \{a\}$ is not a superkey for $F$.

Formalized by `Cslib.Databases.isCandidateKey_iff`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#is-candidate-key-iff).

## Shrinking a key along a list

Let $F$ be a finite set of functional dependencies over a
finite set of attributes. Given a list $l$ of attributes and a set of attributes $K$, go through
$l$ in order and, for each attribute $a$, remove $a$ from the current set whenever the attribute
closure under $F$ of the current set without $a$ is the set of all attributes (that is, the set
without $a$ is still a superkey); the result is the set reached at the end of the list.

Formalized by `Cslib.Databases.shrinkKey`, a definition declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#shrink-key).

## Key-finding algorithm

Let $F$ be a finite set of functional dependencies on a finite set
of attributes $A$, and let $l$ be a list of attributes. The key-finding algorithm starts from the
set $K = A$ of all attributes and goes through $l$ in order: for each listed attribute $a$, it
replaces $K$ by $K \setminus \{a\}$ when the attribute closure of $K \setminus \{a\}$ under $F$ is
all of $A$, and keeps $K$ otherwise. It returns the final set $K$.

Formalized by `Cslib.Databases.findKey`, a definition declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#find-key).

## The key-finding algorithm returns a candidate key

Let $F$ be a finite set of functional
dependencies on a finite set of attributes $A$, and let $l$ be a list in which every attribute
of $A$ occurs. Then the output of the key-finding algorithm on $F$ and $l$, which starts from the
set of all attributes and goes through $l$ in order, removing each listed attribute whenever
what remains is still a superkey, is a candidate key for $F$.

Formalized by `Cslib.Databases.findKey_isCandidateKey`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#find-key-is-candidate-key).

## Every superkey contains a candidate key

Let $F$ be a finite set of functional
dependencies on a finite set of attributes $A$. Every superkey $K$ for $F$ has a subset
$K' \subseteq K$ that is a candidate key for $F$.

Formalized by `Cslib.Databases.exists_isCandidateKey_subset`, a theorem declared in [CSLibExt/Databases/FunctionalDependencies.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/FunctionalDependencies.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html#exists-is-candidate-key-subset).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Functional dependencies](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/functional-dependencies/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/databases/functional-dependencies)
