---
declaration: section
origin: cited
lean: CSLibExt.Combinatorics.RandomThreeSat.Clause, CSLibExt.Combinatorics.RandomThreeSat.Formula, CSLibExt.Combinatorics.RandomThreeSat.clauseSat, CSLibExt.Combinatorics.RandomThreeSat.Satisfiable, CSLibExt.Combinatorics.RandomThreeSat.satProb, CSLibExt.Combinatorics.RandomThreeSat.clause_nonempty, CSLibExt.Combinatorics.RandomThreeSat.satProb_zero, CSLibExt.Combinatorics.RandomThreeSat.IsUpperCutoff
statement: formalized
---

# Random 3-SAT threshold

20 results, 18 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html).

## 3-clause

A 3-clause on $n$ variables is a pair $(S, p)$ of a three-element set $S$ of
variables among the $n$ and a polarity $p$ assigning a Boolean value to every variable, with
$p$ equal to false at every variable outside $S$. This normalization gives each clause in the
usual sense (a three-element variable set with one of $2^3$ polarity patterns) exactly one
representative.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.Clause`, a definition declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#clause).

## Formulas of the random 3-SAT model

A formula with $m$ clauses on $n$ variables is an
ordered $m$-tuple of 3-clauses on $n$ variables, that is, a function from $\{0, \dots, m - 1\}$
to the set of 3-clauses on $n$ variables.

With the uniform counting measure, this finite set of formulas is the sample space of $m$
clauses chosen uniformly and independently, with replacement.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.Formula`, an abbreviation declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#formula).

## Satisfaction of a 3-clause

An assignment $a$ of Boolean values to $n$ variables
satisfies a 3-clause $c$ on these variables when $a$ gives at least one of the three variables
of $c$ the polarity that $c$ prescribes for it.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.clauseSat`, a definition declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#clause-sat).

## Satisfiable 3-SAT formulas

A formula $F$ with $m$ clauses on $n$ variables is
satisfiable when there is an assignment $a$ of Boolean values to the $n$ variables that
satisfies every clause of $F$, that is, $a$ satisfies the 3-clause $F(j)$ for every
$j \in \{0, \dots, m - 1\}$.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.Satisfiable`, a definition declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#satisfiable).

## Satisfiability probability of random 3-SAT

For natural numbers $n$ and $m$, the
satisfiability probability $p(n, m)$ is the number of satisfiable formulas with $m$ clauses on
$n$ variables divided by the number of all such formulas, that is, the probability that a
uniformly random formula with $m$ clauses on $n$ variables is satisfiable. When there are no such
formulas, which happens exactly when $n < 3$ and $m > 0$, the quotient is taken to be $0$; this
affects only finitely many $n$ in any asymptotic statement.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.satProb`, a definition declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#sat-prob).

## 3-clauses exist on at least three variables

If $n \ge 3$, then there is a 3-clause on
$n$ variables: take the first three variables, with polarity true on them and the normalized
polarity false elsewhere.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.clause_nonempty`, a theorem declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#clause-nonempty).

## Satisfiability probability with no clauses

For every number $n$ of variables, the
probability that a uniformly random formula with $0$ clauses on $n$ variables is satisfiable is
$1$: the only such formula is the empty one, and every assignment satisfies it.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.satProb_zero`, a theorem declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#sat-prob-zero).

## Upper threshold cutoff

A real number $\rho$ is an upper threshold cutoff for random
3-SAT when, for every real $r > \rho$, the probability that a uniformly random formula with
$\lfloor r n \rfloor$ clauses on $n$ variables is satisfiable tends to $0$ as $n \to \infty$
(when $r n < 0$ the formula has no clauses); equivalently, such a formula is unsatisfiable
with probability tending to $1$.

Literature upper bounds on the threshold are exactly cutoffs in this sense.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.IsUpperCutoff`, a definition declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#is-upper-cutoff).

## Lower threshold cutoff

A real number $\rho$ is a lower threshold cutoff for random
3-SAT when, for every real $r < \rho$, the probability that a uniformly random formula with
$\lfloor r n \rfloor$ clauses on $n$ variables is satisfiable tends to $1$ as $n \to \infty$
(when $r n < 0$ the formula has no clauses).

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.IsLowerCutoff`, a definition declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#is-lower-cutoff).

## Upper threshold of random 3-SAT

The upper threshold is the infimum, in the real numbers,
of the set of upper threshold cutoffs: the reals $\rho$ such that, for every real $r > \rho$, the
probability that a uniformly random formula with $\lfloor rn \rfloor$ clauses on $n$ variables
(no clauses when $rn < 0$) is satisfiable tends to $0$ as $n \to \infty$. The infimum is taken
to be $0$ when this set is empty or unbounded below.

Under the cutoff characterization of the source's Friedgut sequence $r_{3,n}$, this is the limsup
of that sequence.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.upperThreshold`, a definition declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#upper-threshold).

## Lower threshold of random 3-SAT

The lower threshold is the supremum, in the real numbers,
of the set of lower threshold cutoffs: the reals $\rho$ such that, for every real $r < \rho$, the
probability that a uniformly random formula with $\lfloor rn \rfloor$ clauses on $n$ variables
(no clauses when $rn < 0$) is satisfiable tends to $1$ as $n \to \infty$. The supremum is taken
to be $0$ when this set is empty or unbounded above.

It is the liminf counterpart of the upper threshold.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.lowerThreshold`, a definition declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#lower-threshold).

## Random 3-SAT threshold conjecture

There is a real number $c$ that is both a lower and
an upper threshold cutoff: for every real $r < c$, the probability that a uniformly random
formula with $\lfloor r n \rfloor$ clauses on $n$ variables is satisfiable tends to $1$ as
$n \to \infty$, and for every real $r > c$ this probability tends to $0$ (when $r n < 0$ the
formula has no clauses).

This is stated as a proposition, not asserted: the existence of such a constant is open,
whereas Friedgut's sharp-threshold theorem is proved.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.HasConstantThreshold`, a definition declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#has-constant-threshold).

## Clauses as variable sets with polarity patterns

For every $n$, the 3-clauses on $n$
variables correspond bijectively to the pairs $(S, q)$ of a three-element set $S$ of variables
among the $n$ and a Boolean polarity $q$ on the variables of $S$: a clause is sent to its
variable set together with its polarity restricted to that set.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.clauseEquiv`, a definition declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#clause-equiv).

## CNF clause of a random 3-SAT clause

The CNF clause of a clause $c$ on $n$ variables is the
list of literals $(i, b_i)$, one for each of the three variables $i$ of $c$ taken as a
natural-number index, where $b_i$ is the polarity that $c$ prescribes for $i$; the literals are
listed in some fixed order.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.toCNFClause`, a definition declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#to-cnfclause).

## Extension of an assignment by false

An assignment $a$ of Boolean values to the variables
$0, \dots, n - 1$ extends to all natural-number variables by giving variable $i$ the value $a(i)$
when $i < n$ and the value false otherwise.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.extendAssign`, a definition declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#extend-assign).

## Satisfying a clause through a restricted assignment

Let $A$ assign a Boolean value to
every natural-number variable, and let $c$ be a 3-clause on the $n$ variables $0, \dots, n - 1$.
Then the restriction of $A$ to these $n$ variables satisfies $c$ if and only if $A$ satisfies
the CNF clause of $c$: the list with one literal $(i, p_i)$ for each of the three variables $i$
of $c$, where $p_i$ is the polarity that $c$ prescribes at $i$. A CNF clause is satisfied when
$A$ gives the variable of at least one of its literals that literal's polarity.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.clauseSat_restrict_iff`, a theorem declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#clause-sat-restrict-iff).

## CNF formula of a random 3-SAT formula

The CNF formula of a formula $F$ with $m$ clauses
$F_0, \dots, F_{m-1}$ on $n$ variables is the list of the CNF clauses of $F_0, \dots, F_{m-1}$,
in this order.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.toCNF`, a definition declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#to-cnf).

## Random 3-SAT satisfiability agrees with CNF satisfiability

A formula $F$ with $m$ clauses
on $n$ variables is satisfiable if and only if its CNF formula, which lists each clause of $F$ as
its three literals (variable index, polarity), is satisfiable as a CNF formula: some assignment
of truth values to all natural-number variable indices makes at least one literal of every
clause true.

Formalized by `CSLibExt.Combinatorics.RandomThreeSat.satisfiable_iff`, a theorem declared in [CSLibExt/Combinatorics/RandomThreeSat.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Combinatorics/RandomThreeSat.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#satisfiable-iff).

## Díaz–Kirousis–Mitsche–Pérez-Giménez upper bound for random 3-SAT

The number $4.49$ is an
upper threshold cutoff for random 3-SAT: for every real $r > 4.49$, the probability that a
uniformly random formula with $\lfloor r n \rfloor$ clauses on $n$ variables is satisfiable tends
to $0$ as $n \to \infty$.

## Sources

- Díaz, Kirousis, Mitsche, and Pérez-Giménez, *On the satisfiability threshold of formulas with three literals per clause* (2009), catalogue upper bound `4.490`.

Stated but not proved: `MathlibExt.Combinatorics.RandomThreeSatWanted.diazKirousisMitschePerezUpperBound_wanted` is written with `theorem_wanted` in [WantedExt/Combinatorics/RandomThreeSatWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RandomThreeSatWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#diaz-kirousis-mitsche-perez-upper-bound).

## Hajiaghayi–Sorkin lower bound for random 3-SAT

The number $3.52$ is a lower threshold
cutoff for random 3-SAT: for every real $r < 3.52$, the probability that a uniformly random
formula with $\lfloor r n \rfloor$ clauses on $n$ variables (no clauses when $r < 0$) is
satisfiable tends to $1$ as $n \to \infty$.

## Sources

- Hajiaghayi and Sorkin, *The satisfiability threshold of random 3-SAT is at least 3.52* (2003), and Kaporis, Kirousis, and Lalas (2003), catalogue lower bound `3.52`.

Stated but not proved: `MathlibExt.Combinatorics.RandomThreeSatWanted.hajiaghayiSorkinLowerBound_wanted` is written with `theorem_wanted` in [WantedExt/Combinatorics/RandomThreeSatWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RandomThreeSatWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html#hajiaghayi-sorkin-lower-bound-wanted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Random 3-SAT threshold](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/probabilistic-combinatorics/random-3-sat-threshold)
