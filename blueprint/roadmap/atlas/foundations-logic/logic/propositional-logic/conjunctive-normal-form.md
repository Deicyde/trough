---
declaration: section
origin: cited
lean: Cslib.Logic.PL.CNFClause, Cslib.Logic.PL.CNF, Cslib.Logic.PL.CNFSat, Cslib.Logic.PL.CNFLiteral.Satisfies, Cslib.Logic.PL.CNFClause.Satisfies, Cslib.Logic.PL.CNF.Satisfies, Cslib.Logic.PL.cnfSat_iff_exists_satisfies, Cslib.Logic.PL.CNF.disj
statement: formalized
proof: formalized
---

# Conjunctive normal form

29 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html).

## CNF clause

A CNF clause is a finite list of literals, each a pair $(x, b)$ of a variable
index $x \in \mathbb{N}$ and a polarity $b \in \{\mathrm{true}, \mathrm{false}\}$.

Formalized by `Cslib.Logic.PL.CNFClause`, an abbreviation declared in [CSLibExt/Logics/Propositional/CNF/Basic.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Basic.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#cnfclause).

## CNF formula

A CNF formula is a finite list of CNF clauses, read as the conjunction of its
clauses.

Formalized by `Cslib.Logic.PL.CNF`, an abbreviation declared in [CSLibExt/Logics/Propositional/CNF/Basic.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Basic.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#cnf).

## Satisfiability of a CNF formula

A CNF formula $\varphi$ is satisfiable when there is an
assignment $v : \mathbb{N} \to \{\mathrm{true}, \mathrm{false}\}$ such that every clause $C$ of
$\varphi$ contains a literal $(x, b)$ with $v(x) = b$.

Formalized by `Cslib.Logic.PL.CNFSat`, a definition declared in [CSLibExt/Logics/Propositional/CNF/Basic.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Basic.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#cnfsat).

## Satisfaction of a literal

An assignment $v : \mathbb{N} \to \{\mathrm{true},
\mathrm{false}\}$ satisfies a literal $(x, b)$, with variable $x \in \mathbb{N}$ and polarity
$b \in \{\mathrm{true}, \mathrm{false}\}$, when $v(x) = b$.

Formalized by `Cslib.Logic.PL.CNFLiteral.Satisfies`, a definition declared in [CSLibExt/Logics/Propositional/CNF/Semantics.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Semantics.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#satisfies).

## Satisfaction of a clause

An assignment $v : \mathbb{N} \to \{\mathrm{true},
\mathrm{false}\}$ satisfies a CNF clause $C$ when at least one literal of $C$ is satisfied by $v$,
that is, $C$ contains a literal $(x, b)$ with $v(x) = b$.

Formalized by `Cslib.Logic.PL.CNFClause.Satisfies`, a definition declared in [CSLibExt/Logics/Propositional/CNF/Semantics.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Semantics.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#satisfies-2).

## Satisfaction of a CNF formula

An assignment $v : \mathbb{N} \to \{\mathrm{true},
\mathrm{false}\}$ satisfies a CNF formula $\varphi$ when $v$ satisfies every clause of $\varphi$.

Formalized by `Cslib.Logic.PL.CNF.Satisfies`, a definition declared in [CSLibExt/Logics/Propositional/CNF/Semantics.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Semantics.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#satisfies-3).

## Satisfiability means having a satisfying assignment

A CNF formula $\varphi$ is
satisfiable if and only if there is an assignment $v : \mathbb{N} \to \{\mathrm{true},
\mathrm{false}\}$ that satisfies $\varphi$.

Formalized by `Cslib.Logic.PL.cnfSat_iff_exists_satisfies`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Semantics.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Semantics.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#cnf-sat-iff-exists-satisfies).

## Disjunction of two CNFs

For CNFs $\varphi = C_1 \land \dots \land C_m$ and
$\psi = D_1 \land \dots \land D_n$, their disjunction is the CNF with one clause $C_i \lor D_j$
(the literals of $C_i$ followed by those of $D_j$) for each pair $(i, j)$, listed with $i$ as the
outer and $j$ as the inner index. It expresses $(\bigwedge_i C_i) \lor (\bigwedge_j D_j)$ as
$\bigwedge_{i,j} (C_i \lor D_j)$.

Formalized by `Cslib.Logic.PL.CNF.disj`, a definition declared in [CSLibExt/Logics/Propositional/CNF/NormalForm.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/NormalForm.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#disj).

## Accumulating CNF builder

Let $\iota$ number the atoms by natural numbers, read a literal
$(n, p)$ as variable $n$ with polarity $p$, and write $1$ and $0$ for the polarities true and
false. For a polarity $p$, a proposition $\varphi$ and a CNF $S$, the CNF
$\mathcal{A}_p(\varphi, S)$ is defined by recursion on $\varphi$, together with the disjoining
builder $\mathcal{O}_p$. For an atom $a$, $\mathcal{A}_p(a, S)$ is the unit clause
$[(\iota(a), p)]$ followed by the clauses of $S$. Conjunction-like nodes thread the accumulator:
$\mathcal{A}_1(A \land B, S) = \mathcal{A}_1(A, \mathcal{A}_1(B, S))$,
$\mathcal{A}_0(A \lor B, S) = \mathcal{A}_0(A, \mathcal{A}_0(B, S))$ and
$\mathcal{A}_0(A \to B, S) = \mathcal{A}_1(A, \mathcal{A}_0(B, S))$. Disjunction-like nodes go
through $\mathcal{O}$: writing $X \mathbin{+\!\!+} S$ for the clauses of $X$ followed by those of
$S$ and $[\,]$ for the empty CNF,
$\mathcal{A}_1(A \lor B, S) = \mathcal{O}_1(A, \mathcal{A}_1(B, [\,])) \mathbin{+\!\!+} S$,
$\mathcal{A}_1(A \to B, S) = \mathcal{O}_0(A, \mathcal{A}_1(B, [\,])) \mathbin{+\!\!+} S$ and
$\mathcal{A}_0(A \land B, S) = \mathcal{O}_0(A, \mathcal{A}_0(B, [\,])) \mathbin{+\!\!+} S$.

An assignment $\sigma$ satisfies $\mathcal{A}_p(\varphi, S)$ exactly when $\varphi$ has truth
value $p$ under $\sigma \circ \iota$ and $\sigma$ satisfies $S$.

Formalized by `Cslib.Logic.PL.Proposition.cnfAcc`, a definition declared in [CSLibExt/Logics/Propositional/CNF/NormalForm.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/NormalForm.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#cnf-acc).

## Disjoining CNF builder

Let $\iota$ number the atoms by natural numbers, read a literal
$(n, p)$ as variable $n$ with polarity $p$, and write $1$ and $0$ for the polarities true and
false. For a polarity $p$, a proposition $\varphi$ and a CNF $S$, the CNF
$\mathcal{O}_p(\varphi, S)$ is defined by recursion on $\varphi$, together with the accumulating
CNF builder $\mathcal{A}_p$. Write $X \otimes S$ for the disjunction of two CNFs $X$ and $S$ and
$[\,]$ for the empty CNF. For an atom $a$, $\mathcal{O}_p(a, S) = U \otimes S$, where $U$ is the
CNF whose only clause is the unit clause $[(\iota(a), p)]$. Disjunction-like nodes are consumed
from the left: $\mathcal{O}_1(A \lor B, S) = \mathcal{O}_1(A, \mathcal{O}_1(B, S))$,
$\mathcal{O}_1(A \to B, S) = \mathcal{O}_0(A, \mathcal{O}_1(B, S))$ and
$\mathcal{O}_0(A \land B, S) = \mathcal{O}_0(A, \mathcal{O}_0(B, S))$. Conjunction-like nodes go
through $\mathcal{A}$:
$\mathcal{O}_1(A \land B, S) = \mathcal{A}_1(A, \mathcal{A}_1(B, [\,])) \otimes S$,
$\mathcal{O}_0(A \lor B, S) = \mathcal{A}_0(A, \mathcal{A}_0(B, [\,])) \otimes S$ and
$\mathcal{O}_0(A \to B, S) = \mathcal{A}_1(A, \mathcal{A}_0(B, [\,])) \otimes S$.

An assignment $\sigma$ satisfies $\mathcal{O}_p(\varphi, S)$ exactly when $\varphi$ has truth
value $p$ under $\sigma \circ \iota$ or $\sigma$ satisfies $S$.

Formalized by `Cslib.Logic.PL.Proposition.cnfOr`, a definition declared in [CSLibExt/Logics/Propositional/CNF/NormalForm.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/NormalForm.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#cnf-or).

## CNF of a proposition at a polarity

Let $\iota$ number the atoms by natural numbers. For a
polarity $p$ and a proposition $\varphi$, the CNF of $\varphi$ at polarity $p$ is the result of the
accumulating CNF builder at polarity $p$ on $\varphi$ with the empty CNF as accumulator; the atom
$a$ becomes the variable $\iota(a)$.

An assignment $\sigma$ satisfies it exactly when $\varphi$ has truth value $p$ under
$\sigma \circ \iota$, so it is a CNF of $\varphi$ when $p$ is true and of the Boolean complement of
$\varphi$ when $p$ is false. Only the requested polarity is built: a proposition already in
conjunctive normal form gets a CNF of linear size at polarity true, although the CNF of its
complement can be exponentially larger.

Formalized by `Cslib.Logic.PL.Proposition.cnfOf`, a definition declared in [CSLibExt/Logics/Propositional/CNF/NormalForm.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/NormalForm.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#cnf-of).

## CNF of a proposition

Let $\iota$ number the atoms by natural numbers. The CNF of a
proposition $A$ is its CNF at polarity true, with the atom $a$ as the variable $\iota(a)$.

An assignment $\sigma$ satisfies it exactly when $A$ is true under $\sigma \circ \iota$.

Formalized by `Cslib.Logic.PL.Proposition.toCNF`, a definition declared in [CSLibExt/Logics/Propositional/CNF/NormalForm.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/NormalForm.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#to-cnf).

## CNF of the complement of a proposition

Let $\iota$ number the atoms by natural numbers.
The complement CNF of a proposition $A$ is its CNF at polarity false, with the atom $a$ as the
variable $\iota(a)$.

An assignment $\sigma$ satisfies it exactly when $A$ is false under $\sigma \circ \iota$. This is
not the negation $\lnot A$, which is $A \to \bot$ with $\bot$ an atom: that proposition can be
true together with $A$ when the atom $\bot$ is true.

Formalized by `Cslib.Logic.PL.Proposition.toNegCNF`, a definition declared in [CSLibExt/Logics/Propositional/CNF/NormalForm.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/NormalForm.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#to-neg-cnf).

## Equivalent CNF

Let $\iota$ number the atoms by natural numbers. For every proposition $A$
and every assignment $\sigma$ of Boolean values to the natural-number variables, the CNF of $A$
built with atom $a$ as variable $\iota(a)$ is satisfied by $\sigma$ if and only if $A$ evaluates
to true under the valuation $\sigma \circ \iota$ of the atoms.

Formalized by `Cslib.Logic.PL.Proposition.satisfies_toCNF_iff`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/NormalForm.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/NormalForm.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#satisfies-to-cnf-iff).

## Satisfiability of a CNF with falsum false

Let the atoms have a distinguished atom $\bot$
and let $\iota$ be an injective numbering of the atoms by natural numbers. For every proposition
$A$, the CNF consisting of the unit clause with the single negative literal on variable
$\iota(\bot)$ followed by the clauses of the CNF of $A$ (atom $a$ read as variable $\iota(a)$) is
satisfiable if and only if some valuation $v$ of the atoms with $v(\bot)$ false makes $A$ true.

Formalized by `Cslib.Logic.PL.Proposition.cnfSat_toCNF_bot_iff`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/NormalForm.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/NormalForm.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#cnf-sat-to-cnf-bot-iff).

## Variables of a clause

The variables of a CNF clause $C$ form the finite set of natural
numbers $x$ such that $C$ contains a literal $(x, b)$ for some polarity $b$.

Formalized by `Cslib.Logic.PL.CNFClause.vars`, a definition declared in [CSLibExt/Logics/Propositional/CNF/Restriction.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Restriction.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#vars).

## Restriction of a clause by a literal

Given a literal $\ell = (x, b)$, the restriction
of a clause by $\ell$ is the clause obtained by deleting every literal whose variable is $x$, of
either polarity, keeping the other literals in order.

Formalized by `Cslib.Logic.PL.CNFClause.restrict`, a definition declared in [CSLibExt/Logics/Propositional/CNF/Restriction.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Restriction.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#restrict).

## Satisfaction of a restricted clause

Let $C$ be a clause, $\ell = (x, b)$ a literal that
does not occur in $C$, and $v$ an assignment of Booleans to variables with $v(x) = b$. Then $v$
satisfies the restriction of $C$ by $\ell$ if and only if $v$ satisfies $C$.

Formalized by `Cslib.Logic.PL.CNFClause.satisfies_restrict_iff`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Restriction.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Restriction.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#satisfies-restrict-iff).

## Variables of a CNF formula

The variables of a CNF formula $\varphi$ form the union of the
sets of variables of its clauses, that is, the finite set of natural numbers $x$ such that some
clause of $\varphi$ contains a literal $(x, b)$ for some polarity $b$.

Formalized by `Cslib.Logic.PL.CNF.vars`, a definition declared in [CSLibExt/Logics/Propositional/CNF/Restriction.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Restriction.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#vars-2).

## Restriction of a CNF formula by a literal

Given a literal $\ell = (x, b)$, the
restriction of a CNF formula $\varphi$ by $\ell$ is obtained by deleting every clause of $\varphi$
that contains $\ell$ and replacing every other clause by its restriction by $\ell$, the clause
obtained by deleting every literal whose variable is $x$, of either polarity; the remaining
clauses keep their order.

The deleted clauses are true under every assignment that gives $x$ the value $b$.

Formalized by `Cslib.Logic.PL.CNF.restrict`, a definition declared in [CSLibExt/Logics/Propositional/CNF/Restriction.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Restriction.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#restrict-2).

## Restriction does not add variables

For every CNF formula $\varphi$ and every literal
$\ell$, every variable of the restriction of $\varphi$ by $\ell$ is a variable of $\varphi$.

Formalized by `Cslib.Logic.PL.CNF.vars_restrict_subset`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Restriction.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Restriction.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#vars-restrict-subset).

## The restricted variable no longer occurs

For every CNF formula $F$ and every literal
$\ell = (x, b)$, the variable $x$ does not occur in the restriction of $F$ by $\ell$.

Formalized by `Cslib.Logic.PL.CNF.not_mem_vars_restrict`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Restriction.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Restriction.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#not-mem-vars-restrict).

## Restricting by an occurring variable shrinks the variable set

Let $\varphi$ be a CNF
formula and $(x, b)$ a literal. If $x$ is a variable of $\varphi$, then the set of variables of
the restriction of $\varphi$ by $(x, b)$ is a proper subset of the set of variables of
$\varphi$.

Formalized by `Cslib.Logic.PL.CNF.vars_restrict_ssubset`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Restriction.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Restriction.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#vars-restrict-ssubset).

## Restriction reduces the number of variables

Let $F$ be a CNF formula and let
$\ell = (x, b)$ be a literal whose variable $x$ occurs in $F$. Then the restriction of $F$
by $\ell$ has strictly fewer distinct variables than $F$.

Formalized by `Cslib.Logic.PL.CNF.card_vars_restrict_lt`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Restriction.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Restriction.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#card-vars-restrict-lt).

## Satisfaction of a restricted CNF formula

Let $\varphi$ be a CNF formula, $\ell = (x, b)$
a literal, and $v$ an assignment of Booleans to variables with $v(x) = b$. Then $v$ satisfies the
restriction of $\varphi$ by $\ell$ if and only if $v$ satisfies $\varphi$.

Formalized by `Cslib.Logic.PL.CNF.satisfies_restrict_iff`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Restriction.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Restriction.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#satisfies-restrict-iff-2).

## Satisfaction depends only on the occurring variables

Let $F$ be a CNF formula and let
$v_1, v_2$ be assignments of Booleans to variables with $v_1(x) = v_2(x)$ for every variable $x$
occurring in $F$. If $v_1$ satisfies $F$, then $v_2$ satisfies $F$.

Formalized by `Cslib.Logic.PL.CNF.satisfies_congr`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Restriction.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Restriction.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#satisfies-congr).

## Lifting a satisfying assignment from a restriction

Let $F$ be a CNF formula,
$\ell = (x, b)$ a literal and $v$ an assignment of Booleans to variables. If $v$ satisfies the
restriction of $F$ by $\ell$, then the assignment that agrees with $v$ except that it sends $x$
to $b$ satisfies $F$.

Formalized by `Cslib.Logic.PL.CNF.satisfies_of_satisfies_restrict`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Restriction.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Restriction.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#satisfies-of-satisfies-restrict).

## Splitting on a variable

For every CNF formula $F$ and every variable $x$, the formula
$F$ is satisfiable if and only if the restriction of $F$ by the literal $(x, \mathrm{true})$ is
satisfiable or the restriction of $F$ by the literal $(x, \mathrm{false})$ is satisfiable.

Formalized by `Cslib.Logic.PL.CNF.sat_iff_restrict_true_or_false`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Restriction.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Restriction.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#sat-iff-restrict-true-or-false).

## Unit propagation preserves satisfiability

Let $F$ be a CNF formula that contains the
unit clause whose only literal is $\ell$. Then $F$ is satisfiable if and only if the restriction
of $F$ by $\ell$ is satisfiable.

Formalized by `Cslib.Logic.PL.CNF.sat_iff_restrict_of_unit`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Restriction.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Restriction.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html#sat-iff-restrict-of-unit).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conjunctive normal form](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/conjunctive-normal-form/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/propositional-logic/conjunctive-normal-form)
