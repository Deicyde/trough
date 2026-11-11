---
declaration: section
origin: cited
lean: Cslib.Databases.Tuple, Cslib.Databases.Tuple.IsOver, Cslib.Databases.Tuple.Compatible, Cslib.Databases.Tuple.merge, Cslib.Databases.Tuple.compatible_merge_left, Cslib.Databases.Tuple.compatible_merge_right, Cslib.Databases.Tuple.restrict, Cslib.Databases.Cond
statement: formalized
proof: formalized
---

# Relational algebra

39 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html).

## Tuple

For a type $A$ of attributes and a type $D$ of values, a tuple is a partial
assignment of values to attributes: a function that assigns to each attribute $a \in A$ either a
value in $D$ or no value, in which case the tuple is undefined at $a$.

Formalized by `Cslib.Databases.Tuple`, an abbreviation declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#tuple).

## Tuple over a schema

A tuple $t$ is over the schema $S$, a finite set of attributes, when
$t$ is defined exactly on the attributes of $S$: for every attribute $a$, the value $t(a)$ is
defined if and only if $a \in S$.

Formalized by `Cslib.Databases.Tuple.IsOver`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#is-over).

## Compatible tuples

Two tuples $t$ and $u$ are compatible (joinable) when they agree on
every attribute where both are defined: for every attribute $a$, either $t$ is undefined at $a$,
or $u$ is undefined at $a$, or $t(a) = u(a)$.

Formalized by `Cslib.Databases.Tuple.Compatible`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#compatible).

## Merge of two tuples

The merge of tuples $t$ and $u$ is the tuple whose value at each
attribute $a$ is $t(a)$ if $t$ is defined at $a$, and $u(a)$ otherwise; it is undefined at $a$
when neither $t$ nor $u$ is.

Formalized by `Cslib.Databases.Tuple.merge`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#merge).

## Compatibility with a merge, grouped from the left

For tuples $t$, $u$, $v$: $t$ and $u$
are compatible and the merge of $t$ and $u$ is compatible with $v$ if and only if $t$, $u$, $v$
are pairwise compatible, that is, $t$ and $u$, $t$ and $v$, and $u$ and $v$ are compatible.

Formalized by `Cslib.Databases.Tuple.compatible_merge_left`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#compatible-merge-left).

## Compatibility with a merge, grouped from the right

For tuples $t$, $u$, $v$: $u$ and $v$
are compatible and $t$ is compatible with the merge of $u$ and $v$ if and only if $t$, $u$, $v$
are pairwise compatible, that is, $t$ and $u$, $t$ and $v$, and $u$ and $v$ are compatible.

Formalized by `Cslib.Databases.Tuple.compatible_merge_right`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#compatible-merge-right).

## Restriction of a tuple

For a finite set $T$ of attributes and a tuple $t$, the
restriction $t|_T$ is the tuple that agrees with $t$ on every attribute in $T$ and is undefined
on every attribute outside $T$.

Formalized by `Cslib.Databases.Tuple.restrict`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#restrict).

## Selection conditions

The selection conditions over attributes $A$ and values $D$ are
generated by: the condition that always holds; the equality $a = c$ of an attribute $a$ with a
constant $c \in D$; the equality $a = b$ of two attributes $a$ and $b$; the negation of a
condition; and the conjunction of two conditions.

Formalized by `Cslib.Databases.Cond`, an inductive type declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#cond).

## Truth value of a selection condition

The truth value of a selection condition on a
tuple $t$ is defined by recursion: the always-true condition holds; $a = c$ holds when $t$ is
defined at $a$ with value $c$; $a = b$ holds when $t(a) = t(b)$ as possibly undefined values,
so it also holds when $t$ is undefined at both $a$ and $b$; a negation holds when the negated
condition fails; and a conjunction holds when both conditions hold.

Formalized by `Cslib.Databases.Cond.eval`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#eval).

## Attributes of a selection condition

The set of attributes mentioned by a selection
condition, defined by recursion: it is empty for the always-true condition; for the comparison
$a = d$ of an attribute $a$ with a constant $d$ it is $\{a\}$; for the comparison $a = b$ of
attributes $a$ and $b$ it is $\{a, b\}$; for the negation $\neg \varphi$ of a condition $\varphi$
it is the set of attributes of $\varphi$; and for the conjunction $\varphi \land \psi$ of
conditions $\varphi$ and $\psi$ it is the union of the attributes of $\varphi$ and of $\psi$.

Formalized by `Cslib.Databases.Cond.attrs`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#attrs).

## Selection conditions depend only on their attributes

Let $c$ be a selection condition,
$t$ a tuple and $T$ a finite set of attributes containing every attribute of $c$. Then $c$ has
the same truth value on the restriction of $t$ to $T$ as on $t$.

Formalized by `Cslib.Databases.Cond.eval_restrict`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#eval-restrict).

## Relation over a schema

A finite set $r$ of tuples is a relation over the schema $S$, a
finite set of attributes, when every tuple $t \in r$ is over $S$, that is, $t$ is defined exactly
on the attributes of $S$.

Formalized by `Cslib.Databases.IsOver`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#is-over-2).

## Selection

For a selection condition $c$ and a finite set $r$ of tuples, the selection
$\sigma_c(r)$ is the set of tuples $t \in r$ on which $c$ evaluates to true.

Formalized by `Cslib.Databases.select`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#select).

## Cascade of selections

Write $\sigma_c$ for selection by a selection condition $c$. For
selection conditions $c$ and $c'$ and a finite set $r$ of tuples,
$\sigma_c(\sigma_{c'}(r)) = \sigma_{c' \land c}(r)$: selecting by $c'$ and then by $c$ is the same
as selecting once by the conjunction $c' \land c$.

Formalized by `Cslib.Databases.select_select`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#select-select).

## Selections commute

For all selection conditions $c$ and $c'$ and every finite set $r$ of
tuples, selecting by $c'$ and then by $c$ gives the same result as selecting by $c$ and then by
$c'$: $\sigma_c(\sigma_{c'}(r)) = \sigma_{c'}(\sigma_c(r))$.

Formalized by `Cslib.Databases.select_comm`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#select-comm).

## Natural join

The natural join $r \bowtie s$ of finite sets of tuples $r$ and $s$ is the
set of merges of $t$ and $u$ over all pairs of tuples $t \in r$ and $u \in s$ that are
compatible, that is, agree on every attribute where both are defined. The merge of $t$ and $u$
takes the value of $t$ where $t$ is defined and the value of $u$ otherwise.

Formalized by `Cslib.Databases.join`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#join).

## Renaming of attributes

For a permutation $f$ of the attributes and a finite set $r$ of
tuples, the renaming $\rho_f(r)$ is the finite set of the tuples $t \circ f^{-1}$ for $t \in r$:
each tuple keeps its values, and its value at an attribute $a$ moves to the attribute $f(a)$.

Formalized by `Cslib.Databases.rename`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#rename).

## Commutativity of the natural join

For all finite sets $r$ and $s$ of tuples,
$r \bowtie s = s \bowtie r$, where $\bowtie$ is the natural join.

Formalized by `Cslib.Databases.join_comm`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#join-comm).

## Associativity of the natural join

For all finite sets $r$, $s$ and $w$ of tuples,
$(r \bowtie s) \bowtie w = r \bowtie (s \bowtie w)$, where $\bowtie$ is the natural join.

Formalized by `Cslib.Databases.join_assoc`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#join-assoc).

## The natural join on a common schema is the intersection

If $r$ and $s$ are relations
over the same schema $S$, that is, finite sets of tuples each over $S$, then their natural join
is their intersection: $r \bowtie s = r \cap s$.

Formalized by `Cslib.Databases.join_eq_inter`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#join-eq-inter).

## Selection distributes over union

Assume the set of attributes is finite. Let $c$ be a
selection condition and write $\sigma_c$ for selection by $c$. For finite sets $r$ and $s$ of
tuples, $\sigma_c(r \cup s) = \sigma_c(r) \cup \sigma_c(s)$.

Formalized by `Cslib.Databases.select_union`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#select-union).

## Selection distributes over difference

Assume the set of attributes is finite. Let $c$
be a selection condition and write $\sigma_c$ for selection by $c$. For finite sets $r$ and $s$
of tuples, $\sigma_c(r \setminus s) = \sigma_c(r) \setminus \sigma_c(s)$.

Formalized by `Cslib.Databases.select_sdiff`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#select-sdiff).

## Projection of a relation

For a finite set $T$ of attributes and a finite set $r$ of
tuples, the projection $\pi_T(r)$ is the finite set of the restrictions to $T$ of the tuples of
$r$: $\pi_T(r) = \{ t|_T : t \in r \}$.

Formalized by `Cslib.Databases.project`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#project).

## Membership in a join

Let $r$ be a relation over the schema $S$ and $s$ a relation over
the schema $S'$, that is, finite sets of tuples each over $S$, respectively each over $S'$. A
tuple $t$ belongs to the natural join $r \bowtie s$ if and only if $t$ is over $S \cup S'$, the
restriction of $t$ to $S$ belongs to $r$, and the restriction of $t$ to $S'$ belongs to $s$.

Formalized by `Cslib.Databases.mem_join_iff`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#mem-join-iff).

## Selection pushdown into the left operand of a join

Let $r$ be a relation over a schema
$S$, that is, a finite set of tuples each defined exactly on the attributes of $S$, and let $s$ be
any finite set of tuples. If every attribute of the selection condition $c$ lies in $S$, then
$\sigma_c(r \bowtie s) = \sigma_c(r) \bowtie s$, where $\sigma_c$ is selection by $c$ and
$\bowtie$ is the natural join.

Formalized by `Cslib.Databases.select_join_left`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#select-join-left).

## Selection pushdown into the right operand of a join

Let $s$ be a relation over a schema
$S'$, that is, a finite set of tuples each defined exactly on the attributes of $S'$, and let $r$
be any finite set of tuples. If every attribute of the selection condition $c$ lies in $S'$, then
$\sigma_c(r \bowtie s) = r \bowtie \sigma_c(s)$, where $\sigma_c$ is selection by $c$ and
$\bowtie$ is the natural join.

Formalized by `Cslib.Databases.select_join_right`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#select-join-right).

## Cascade of projections

Assume the set of attributes is finite. For all finite sets of
attributes $T$ and $T'$ and every finite set $r$ of tuples,
$\pi_T(\pi_{T'}(r)) = \pi_{T \cap T'}(r)$, where $\pi_T$ is projection onto $T$.

Formalized by `Cslib.Databases.project_project`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#project-project).

## Cascade of projections onto a subset

Assume the set of attributes is finite. For finite
sets of attributes $T \subseteq T'$ and every finite set $r$ of tuples,
$\pi_T(\pi_{T'}(r)) = \pi_T(r)$, where $\pi_T$ is projection onto $T$.

Formalized by `Cslib.Databases.project_project_of_subset`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#project-project-of-subset).

## Selection commutes with projection

Assume the set of attributes is finite. Let $c$ be a
selection condition, $T$ a finite set of attributes containing every attribute of $c$, and $r$ a
finite set of tuples. Then $\sigma_c(\pi_T(r)) = \pi_T(\sigma_c(r))$, where $\sigma_c$ is
selection by $c$ and $\pi_T$ is projection onto $T$.

Formalized by `Cslib.Databases.select_project`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#select-project).

## Projection distributes over union

For every finite set $T$ of attributes and all finite
sets $r$ and $s$ of tuples, the projection onto $T$ of $r \cup s$ is the union of the projections
onto $T$ of $r$ and of $s$: $\pi_T(r \cup s) = \pi_T(r) \cup \pi_T(s)$.

Formalized by `Cslib.Databases.project_union`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 449](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L449). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#project-union).

## Relational algebra queries

The relational algebra queries over base relations named
by $N$, with attributes $A$ and values $D$, are generated by: the base relation named $n$ for
each $n \in N$; the selection $\sigma_c(e)$ of a query $e$ by a selection condition $c$; the
projection $\pi_T(e)$ of a query $e$ on a finite set of attributes $T$; the natural join of two
queries; the union of two queries; the difference of two queries; and the renaming
$\rho_f(e)$ of a query $e$ along a permutation $f$ of $A$.

Formalized by `Cslib.Databases.Expr`, an inductive type declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#expr).

## Value of a query

Given a database $\mathrm{db}$, which assigns a finite set of tuples
$\mathrm{db}(n)$ to each relation name $n$, the value of a relational algebra query on
$\mathrm{db}$ is the finite set of tuples defined by recursion on the query: the base relation
$n$ has value $\mathrm{db}(n)$; for a query $e$ with value $v$, the selection $\sigma_c(e)$ by a
selection condition $c$, the projection $\pi_T(e)$ onto a finite set $T$ of attributes and the
renaming $\rho_f(e)$ along a permutation $f$ of the attributes have values $\sigma_c(v)$,
$\pi_T(v)$ and $\rho_f(v)$; and the natural join, the union and the difference of queries $e$
and $e'$ with values $v$ and $v'$ have values $v \bowtie v'$, $v \cup v'$ and
$v \setminus v'$.

Formalized by `Cslib.Databases.Expr.eval`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#eval-2).

## Schema of a query

Given a database schema assigning a finite set $\mathrm{sch}(n)$ of
attributes to each base relation name $n$, the schema of a relational algebra query is either a
finite set of attributes or undefined (the query is ill-formed), defined by recursion on the
query: the base relation $n$ has schema $\mathrm{sch}(n)$; if $e$ has schema $S$, then the
selection $\sigma_c(e)$ has schema $S$ when every attribute of the condition $c$ lies in $S$, the
projection $\pi_T(e)$ has schema $T$ when $T \subseteq S$, and the renaming $\rho_f(e)$ along a
permutation $f$ of the attributes has schema $f(S)$; if $e$ and $e'$ have schemas $S$ and $S'$,
then the natural join of $e$ and $e'$ has schema $S \cup S'$, and their union and their
difference have schema $S$ when $S = S'$. In every other case, including when an operand is
ill-formed, the schema is undefined.

Formalized by `Cslib.Databases.Expr.schema`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#schema).

## Databases conforming to a schema

Let $N$ be a set of relation names. A database
schema assigns to each name $n \in N$ a finite set of attributes $\mathrm{sch}(n)$, and a
database assigns to each name $n$ a finite set of tuples $\mathrm{db}(n)$. The database
$\mathrm{db}$ conforms to the database schema $\mathrm{sch}$ when, for every name $n$, the
set $\mathrm{db}(n)$ is a relation over $\mathrm{sch}(n)$.

Formalized by `Cslib.Databases.Expr.Conforms`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 501](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L501). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#conforms).

## Typing is sound

A well-formed query evaluates, on every conforming database, to a
relation over its inferred schema.

Formalized by `Cslib.Databases.Expr.eval_isOver`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 506](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L506). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#eval-is-over).

## Query equivalence

Let $\mathrm{sch}$ be a database schema, assigning a finite set of
attributes to each relation name. Two queries $e$ and $e'$ are equivalent with respect to
$\mathrm{sch}$ when there is a finite set of attributes $S$ such that the inferred schemas of
$e$ and of $e'$ with respect to $\mathrm{sch}$ are both $S$ (in particular both queries are
well-formed), and $e$ and $e'$ evaluate to the same relation on every database that conforms
to $\mathrm{sch}$.

Formalized by `Cslib.Databases.Expr.Equiv`, a definition declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 547](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L547). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#equiv).

## Selection pushdown as a query rewrite

Fix a database schema $\mathrm{sch}$ assigning a
finite set of attributes to each base relation name. Let $e$ and $e'$ be well-formed queries with
schemas $S$ and $S'$, and let $c$ be a selection condition all of whose attributes lie in $S$.
Then the query $\sigma_c(e \bowtie e')$, the selection by $c$ of the natural join of $e$ and $e'$,
is equivalent to the query $\sigma_c(e) \bowtie e'$: both are well-formed with the same schema,
and they have equal values on every database conforming to $\mathrm{sch}$.

Formalized by `Cslib.Databases.Expr.select_join`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 565](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L565). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#select-join).

## Cascade of selections as a query rewrite

Fix a database schema $\mathrm{sch}$
assigning a finite set of attributes to each base relation name. Let $e$ be a well-formed query
with schema $S$, and let $c$ and $c'$ be selection conditions all of whose attributes lie in
$S$. Then the query $\sigma_c(\sigma_{c'}(e))$, the selection by $c$ of the selection of $e$ by
$c'$, is equivalent to the query $\sigma_{c' \land c}(e)$, the selection of $e$ by the
conjunction $c' \land c$: both are well-formed with the same schema, and they have equal values
on every database conforming to $\mathrm{sch}$.

Formalized by `Cslib.Databases.Expr.select_select`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 573](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L573). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#select-select-2).

## Cascade of projections as a query rewrite

Fix a database schema $\mathrm{sch}$
assigning a finite set of attributes to each base relation name. Let $e$ be a well-formed query
with schema $S$, and let $T \subseteq T' \subseteq S$ be finite sets of attributes. Then the
query $\pi_T(\pi_{T'}(e))$, the projection onto $T$ of the projection of $e$ onto $T'$, is
equivalent to the query $\pi_T(e)$, the projection of $e$ onto $T$: both are well-formed with
the same schema, and they have equal values on every database conforming to $\mathrm{sch}$.

Formalized by `Cslib.Databases.Expr.project_project`, a theorem declared in [CSLibExt/Databases/RelationalAlgebra.lean, line 580](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/RelationalAlgebra.lean#L580). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html#project-project-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Relational algebra](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/relational-algebra/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/databases/relational-algebra)
