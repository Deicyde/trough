---
declaration: section
origin: cited
lean: Cslib.Algorithms.SAT.Tseitin.negLit, Cslib.Algorithms.SAT.Tseitin.andClauses, Cslib.Algorithms.SAT.Tseitin.orClauses, Cslib.Algorithms.SAT.Tseitin.impClauses, Cslib.Algorithms.SAT.Tseitin.tseitinStep, Cslib.Algorithms.SAT.Tseitin.accStep, Cslib.Logic.PL.Proposition.connectiveCount, Cslib.Logic.PL.Proposition.tseitinAux
statement: formalized
proof: formalized
---

# Tseitin transformation

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html).

## Complementary literal

The complement of a literal $(x, b)$ with variable $x$ and
polarity $b$ is the literal $(x, \lnot b)$: the same variable with the opposite polarity.

Formalized by `Cslib.Algorithms.SAT.Tseitin.negLit`, an abbreviation declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#neg-lit).

## Tseitin clauses for a conjunction

For literals $g$, $a$ and $b$, the defining clauses of
the gate literal $g$ for the conjunction of $a$ and $b$ are, in this order, the three clauses
$\lnot g \lor a$, $\lnot g \lor b$ and $g \lor \lnot a \lor \lnot b$, where $\lnot \ell$ denotes the
complementary literal of $\ell$ (same variable, opposite polarity).

Formalized by `Cslib.Algorithms.SAT.Tseitin.andClauses`, a definition declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#and-clauses).

## Tseitin clauses for a disjunction

For literals $g$, $a$ and $b$, the defining clauses
of the gate literal $g$ for the disjunction of $a$ and $b$ are the three clauses
$\lnot g \lor a \lor b$, $g \lor \lnot a$ and $g \lor \lnot b$, where $\lnot \ell$ denotes the
complementary literal of $\ell$.

Formalized by `Cslib.Algorithms.SAT.Tseitin.orClauses`, a definition declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#or-clauses).

## Tseitin clauses for an implication

For literals $g$, $a$ and $b$, the defining clauses of
the gate literal $g$ for the implication from $a$ to $b$ are, in this order, the three clauses
$\lnot g \lor \lnot a \lor b$, $g \lor a$ and $g \lor \lnot b$, where $\lnot \ell$ denotes the
complementary literal of $\ell$ (same variable, opposite polarity).

Formalized by `Cslib.Algorithms.SAT.Tseitin.impClauses`, a definition declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#imp-clauses).

## One step of the Tseitin encoding

Given a rule $\mathit{cl}$ assigning to literals $g$, $a$,
$b$ a list of defining clauses, and the results $(a, C_A, k_A)$ and $(b, C_B, k_B)$ of encoding
the two operands of a binary connective (each a literal, a clause list and a next unused gate
number), the step returns the positive literal $g$ of variable $2k_B+1$, the clause list $C_A$,
then $C_B$, then $\mathit{cl}(g, a, b)$, and the next gate number $k_B+1$.

Formalized by `Cslib.Algorithms.SAT.Tseitin.tseitinStep`, a definition declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#tseitin-step).

## One step of the linear-time Tseitin builder

Let $c$ map a gate literal and two operand
literals to a list of clauses, and let $(a, \varphi_A, k_A)$ and $(b, \varphi_B, k_B)$ be the
results for the two operands, each a literal, a clause list and a next free gate number. The step
returns the positive literal $g$ of the variable $2k_B + 1$, the clause list $c(g, a, b)$ followed
by $\varphi_B$, and the next free gate number $k_B + 1$. Neither $\varphi_A$ nor $k_A$ is used: in
the builder, $\varphi_B$ is the accumulator, which already holds both operands' clauses.

Formalized by `Cslib.Algorithms.SAT.Tseitin.accStep`, a definition declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#acc-step).

## Connective count of a propositional formula

For a propositional formula $A$, built from
atoms with the binary connectives $\wedge$, $\vee$ and $\to$, the connective count of $A$ is the
number of occurrences of these connectives in $A$. It is $0$ for an atom, and for $B \circ C$,
with $\circ$ one of $\wedge$, $\vee$ and $\to$, it is the count of $B$ plus the count of $C$
plus $1$.

Formalized by `Cslib.Logic.PL.Proposition.connectiveCount`, a definition declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#connective-count).

## Tseitin encoding with gates numbered from $k$

Fix a map $\iota$ from atoms to natural
numbers. Given a formula $A$ and a gate number $k$, the encoding returns a literal naming $A$, a
list of defining clauses and the next unused gate number. For an atom $a$ it returns the
positive literal of variable $2\iota(a)$, no clauses, and $k$. For $A \circ B$ with $\circ$ one of
$\wedge$, $\vee$, $\to$, it encodes $A$ from gate $k$, obtaining a literal $a$, clauses $C_A$ and a
gate number $k'$, then $B$ from gate $k'$, obtaining $b$, $C_B$ and $k''$; it returns the positive
literal $g$ of variable $2k''+1$, the clauses $C_A$, then $C_B$, then the three defining clauses
of $g$ for $a \circ b$, and $k''+1$.

Its list concatenations make it quadratic; the Tseitin CNF is computed by a linear-time builder
that produces the same clauses in another order.

Formalized by `Cslib.Logic.PL.Proposition.tseitinAux`, a definition declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#tseitin-aux).

## Linear-time Tseitin builder

Fix a map $\iota$ from atoms to natural numbers. Given a
formula $A$, a gate number $k$ and a clause list $\mathit{acc}$, the builder returns a literal
naming $A$, a clause list and the next unused gate number. For an atom $a$ it returns the
positive literal of variable $2\iota(a)$, the list $\mathit{acc}$ unchanged, and $k$. For
$A \circ B$ with $\circ$ one of $\wedge$, $\vee$, $\to$, it runs on $A$ from gate $k$ with
accumulator $\mathit{acc}$, obtaining a literal $a$, a list $L_A$ and a gate number $k'$, then on
$B$ from gate $k'$ with accumulator $L_A$, obtaining $b$, $L_B$ and $k''$; it returns the positive
literal $g$ of variable $2k''+1$, the three defining clauses of $g$ for $a \circ b$ followed by
$L_B$, and $k''+1$.

Unlike the reference Tseitin encoding, which concatenates the operands' clause lists, it
prepends each gate's clauses to the accumulator, so it runs in linear time and the clauses come
out in a different order.

Formalized by `Cslib.Logic.PL.Proposition.tseitinAcc`, a definition declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#tseitin-acc).

## The linear-time Tseitin builder agrees with the reference encoding

For every map $\iota$ from atoms to natural numbers, every formula $A$, every gate number $k$
and every clause list $\mathit{acc}$, the linear-time Tseitin builder run on $A$ from gate $k$
with accumulator $\mathit{acc}$ returns the same literal naming $A$ and the same next unused
gate number as the reference Tseitin encoding of $A$ with gates numbered from $k$, and its
clause list is $X$ followed by $\mathit{acc}$ for some list of clauses $X$ that is a
permutation of the defining clauses of the reference encoding.

Formalized by `Cslib.Logic.PL.Proposition.tseitinAcc_eq`, a theorem declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#tseitin-acc-eq).

## Tseitin CNF

For a map $\iota$ from atoms to natural numbers and a formula $A$, run the
linear-time Tseitin builder on $A$ with gates numbered from $0$ and the empty accumulator,
obtaining a literal $\ell$ naming $A$ and a clause list $C$. The Tseitin CNF of $A$ is the unit
clause $[\ell]$ followed by $C$.

Formalized by `Cslib.Logic.PL.Proposition.tseitin`, a definition declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#tseitin).

## The Tseitin CNF reorders the reference encoding

For every map $\iota$ from atoms to
natural numbers and every formula $A$, the Tseitin CNF of $A$ is the unit clause whose literal
is the literal naming $A$ in the reference Tseitin encoding of $A$ with gates numbered from $0$,
followed by a list of clauses that is a permutation of the defining clauses of that encoding.

Formalized by `Cslib.Logic.PL.Proposition.tseitin_eq`, a theorem declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#tseitin-eq).

## Tseitin CNF with $\bot$ false

For an atom type with a distinguished atom $\bot$, a map
$\iota$ from atoms to natural numbers and a formula $A$, this is the CNF consisting of the unit
clause whose literal is the negative literal of variable $2\iota(\bot)$, followed by the Tseitin
CNF of $A$ with respect to $\iota$.

Formalized by `Cslib.Logic.PL.Proposition.tseitinBot`, a definition declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#tseitin-bot).

## Number of defining clauses in the Tseitin encoding

For every map $\iota$ from atoms to
natural numbers, every formula $A$ and every gate number $k$, the list of defining clauses
produced by the Tseitin encoding of $A$ with gates numbered from $k$ has length $3c$, where $c$ is
the number of binary connectives of $A$.

Formalized by `Cslib.Logic.PL.Proposition.length_tseitinAux`, a theorem declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#length-tseitin-aux).

## Number of clauses of the Tseitin CNF

For every proposition $A$ and every map $\iota$
from atoms to natural numbers, the Tseitin CNF of $A$ with respect to $\iota$, as a list of
clauses counted with repetition, has length $3c + 1$, where $c$ is the number of binary
connectives of $A$: three defining clauses per connective plus the unit clause asserting $A$.

Formalized by `Cslib.Logic.PL.Proposition.length_tseitin`, a theorem declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#length-tseitin).

## Tseitin clauses have at most three literals

For every proposition $A$ and every map
$\iota$ from atoms to natural numbers, every clause of the Tseitin CNF of $A$ with respect to
$\iota$ has at most three literals.

Formalized by `Cslib.Logic.PL.Proposition.length_le_three_of_mem_tseitin`, a theorem declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#length-le-three-of-mem-tseitin).

## Truth value of a literal

Let $\sigma$ assign a Boolean value to every natural-number
variable, and let $\ell = (x, b)$ be a literal with variable $x$ and polarity $b$. The truth
value of $\ell$ under $\sigma$ is true exactly when $\sigma(x) = b$.

Formalized by `Cslib.Algorithms.SAT.Tseitin.litVal`, an abbreviation declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#lit-val).

## Satisfying a concatenation of CNF formulas

For every assignment $\sigma$ of Boolean
values to the natural-number variables and all CNF formulas $\varphi$ and $\psi$, $\sigma$
satisfies the formula consisting of the clauses of $\varphi$ followed by those of $\psi$ if
and only if $\sigma$ satisfies both $\varphi$ and $\psi$.

Formalized by `Cslib.Algorithms.SAT.Tseitin.satisfies_append`, a theorem declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#satisfies-append).

## Gate variables in a range

For natural numbers $k$ and $k'$, a variable $x \in \mathbb{N}$
is a gate in range $[k, k')$ if $x = 2j + 1$ for some $j \in \mathbb{N}$ with $k \le j < k'$.

Formalized by `Cslib.Algorithms.SAT.Tseitin.IsGate`, a definition declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#is-gate).

## Allowed variables for a gate range

For natural numbers $k$ and $k'$, a variable
$x \in \mathbb{N}$ is allowed for the gate range $[k, k')$ if $x$ is even (it names an atom) or
$x$ is a gate in range $[k, k')$, that is, $x = 2j + 1$ for some $j \in \mathbb{N}$ with
$k \le j < k'$.

Formalized by `Cslib.Algorithms.SAT.Tseitin.Allowed`, a definition declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#allowed).

## Functions of the atom variables

A function $f$ from assignments
$\sigma : \mathbb{N} \to \mathrm{Bool}$ to Booleans depends only on the atom variables if
$f(\sigma) = f(\tau)$ for all assignments $\sigma$ and $\tau$ with $\sigma(2n) = \tau(2n)$ for
every $n \in \mathbb{N}$.

Formalized by `Cslib.Algorithms.SAT.Tseitin.AtomDependent`, a definition declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#atom-dependent).

## Tseitin encoding invariant

Let $k$ be a natural number, let $r = (\ell, \Phi, k')$
consist of a literal $\ell$, a CNF formula $\Phi$ and a natural number $k'$, and let $v$ map
each assignment of Boolean values to the natural-number variables to a Boolean value. Call a
variable a gate in range if it equals $2j + 1$ for some $j$ with $k \le j < k'$. The invariant
holds for $k$, $r$ and $v$ when $k \le k'$; the variable of $\ell$ and every variable occurring
in a literal of $\Phi$ is even or a gate in range; every assignment $\sigma$ that satisfies
$\Phi$ gives $\ell$ the value $v(\sigma)$; and for every assignment $\sigma$ there is an
assignment $\tau$ that agrees with $\sigma$ on every variable that is not a gate in range,
satisfies $\Phi$ and gives $\ell$ the value $v(\sigma)$.

Here $r$ is meant to be the result (literal, clauses, next gate) of encoding a proposition with
gates numbered from $k$, and $v$ the value of that proposition.

Formalized by `Cslib.Algorithms.SAT.Tseitin.Spec`, a structure declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#spec).

## Satisfaction depends only on the occurring variables

Let $\varphi$ be a CNF formula and
let $\sigma$ and $\tau$ be assignments of Boolean values to the natural-number variables that
agree on every variable occurring in a literal of $\varphi$. If $\sigma$ satisfies $\varphi$,
then $\tau$ satisfies $\varphi$.

Formalized by `Cslib.Algorithms.SAT.Tseitin.satisfies_of_agree`, a theorem declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#satisfies-of-agree).

## Value of a proposition read off the atom variables

Given a map $\iota$ from atoms to
natural numbers, a proposition $A$ and an assignment $\sigma : \mathbb{N} \to \mathrm{Bool}$,
this is the truth value of $A$ under the valuation that gives each atom $a$ the value
$\sigma(2\iota(a))$.

Formalized by `Cslib.Algorithms.SAT.Tseitin.atomVal`, an abbreviation declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#atom-val).

## Correctness invariant of the Tseitin encoding

Let $\iota$ map atoms to natural numbers,
let $A$ be a proposition and $k$ a natural number, and let $(\ell, \Phi, k')$ be the reference
Tseitin encoding of $A$ with gates numbered from $k$: the literal naming $A$, its defining
clauses and the next unused gate number. For an assignment $\sigma$ of Boolean values to the
natural-number variables, let $A[\sigma]$ be the truth value of $A$ when each atom $a$ gets
the value $\sigma(2\iota(a))$, and call a variable a gate in range if it equals $2j + 1$ for
some $j$ with $k \le j < k'$. Then $k \le k'$; the variable of $\ell$ and every variable
occurring in a literal of $\Phi$ is even or a gate in range; every assignment $\sigma$ that
satisfies $\Phi$ gives $\ell$ the value $A[\sigma]$; and for every assignment $\sigma$ there is
an assignment $\tau$ that agrees with $\sigma$ on every variable that is not a gate in range,
satisfies $\Phi$ and gives $\ell$ the value $A[\sigma]$.

Formalized by `Cslib.Algorithms.SAT.Tseitin.spec_tseitinAux`, a theorem declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#spec-tseitin-aux).

## Tseitin correctness

Let $\iota$ be an injective map from atoms to natural numbers, let
$A$ be a proposition and let $v$ be a valuation of the atoms. Then $A$ is true under $v$ if and
only if some assignment $\sigma : \mathbb{N} \to \mathrm{Bool}$ with $\sigma(2\iota(a)) = v(a)$
for every atom $a$ satisfies the Tseitin CNF of $A$ with respect to $\iota$.

Formalized by `Cslib.Logic.PL.Proposition.evalBool_iff_exists_satisfies_tseitin`, a theorem declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 445](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L445). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#eval-bool-iff-exists-satisfies-tseitin).

## Equisatisfiability of the Tseitin transformation

Let the atoms have a distinguished atom
$\bot$, let $\iota$ be an injective map from atoms to natural numbers and let $A$ be a
proposition. The Tseitin CNF of $A$ with respect to $\iota$, together with the unit clause making
the variable $2\iota(\bot)$ false, is satisfiable if and only if $A$ is true under some valuation
$v$ of the atoms with $v(\bot)$ false.

Formalized by `Cslib.Logic.PL.Proposition.cnfSat_tseitinBot_iff`, a theorem declared in [CSLibExt/Algorithms/SAT/Tseitin/Basic.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/Tseitin/Basic.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html#cnf-sat-tseitin-bot-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tseitin transformation](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/tseitin-transformation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/propositional-logic/tseitin-transformation)
