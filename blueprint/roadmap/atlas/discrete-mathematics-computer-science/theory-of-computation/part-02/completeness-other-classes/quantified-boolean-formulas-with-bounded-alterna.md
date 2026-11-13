---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.QBFMatrixGate, MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.qbfGateEval, MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.qbfCircuitEval, MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.qbfCircuitVars, MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.qbfCircuitWellFormed, MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.EvalQBFK, MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.blockCountAux, MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.blockCount
statement: formalized
---

# Quantified Boolean formulas with bounded alternation

10 results, 9 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/quantified-boolean-formulas-with-bounded-alterna/index.html).

## Gates of a quantified Boolean formula matrix

A gate of a matrix circuit is a pair $(t, r)$
of a natural number $t$, its kind, and a list $r$ of natural numbers, its references. The kinds
are read as follows: kind $0$ with $r = [v]$ is the variable $v$, kind $1$ with $r = [b]$ is the
constant true if $b = 1$ and false otherwise, kind $2$ is a negation, kind $3$ a conjunction and
kind $4$ a disjunction, where for kinds $2$, $3$ and $4$ the references are indices of gates.

A circuit matrix is thus an unrestricted Boolean formula with sharing, not a formula in
conjunctive normal form.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.QBFMatrixGate`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/quantified-boolean-formulas-with-bounded-alterna/index.html#qbfmatrix-gate).

## Evaluation of a QBF matrix gate

Given a list $s$ of truth values (the values of the earlier
gates) and an assignment $\alpha$ of a truth value to every natural number, the value of a gate
$(t, r)$ is computed as follows, where $s_a$ is the $a$-th entry of $s$ if $a$ is less than the
length of $s$ and false otherwise: if $t = 0$ and $r = [v]$, it is $\alpha(v)$; if $t = 1$ and
$r = [b]$, it is true exactly when $b = 1$; if $t = 2$ and $r = [a]$, it is the negation of $s_a$;
if $t = 3$, it is true exactly when $s_a$ is true for every $a$ in $r$; if $t = 4$, it is true
exactly when $s_a$ is true for some $a$ in $r$; for every other gate it is false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.qbfGateEval`, a definition declared in [WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/quantified-boolean-formulas-with-bounded-alterna/index.html#qbf-gate-eval).

## Evaluation of a QBF matrix circuit

Given a matrix circuit $C = (g_0, \dots, g_{m-1})$, a
list of gates, and an assignment $\alpha$ of a truth value to every natural number, the list
$(s_0, \dots, s_{m-1})$ of the values of the gates of $C$, where $s_i$ is the value of the gate
$g_i$ given the values $(s_0, \dots, s_{i-1})$ of the earlier gates and the assignment $\alpha$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.qbfCircuitEval`, a definition declared in [WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/quantified-boolean-formulas-with-bounded-alterna/index.html#qbf-circuit-eval).

## Variables of a QBF matrix circuit

For a matrix circuit $C$, a list of gates, the list of
the variables $v$ of the gates of $C$ of the form $(0, [v])$, in the order of the gates of $C$ and
with repetitions.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.qbfCircuitVars`, a definition declared in [WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/quantified-boolean-formulas-with-bounded-alterna/index.html#qbf-circuit-vars).

## Well-formed QBF matrix circuits

A matrix circuit $C = (g_0, \dots, g_{m-1})$, a list of
gates, is well formed when for every $j < m$ whose gate $g_j = (t, r)$ has kind $t \in \{2, 3, 4\}$
(negation, conjunction or disjunction), every reference $a$ in $r$ satisfies $a < j$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.qbfCircuitWellFormed`, a definition declared in [WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/quantified-boolean-formulas-with-bounded-alterna/index.html#qbf-circuit-well-formed).

## Truth of a quantified Boolean formula with circuit matrix

Let $P$ be a quantifier prefix,
a list of pairs $(q, v)$ of a quantifier $q$, $\exists$ (true) or $\forall$ (false), and a
variable $v \in \mathbb{N}$; let $\varphi$ be a matrix circuit and $\alpha$ an assignment of a
truth value to every natural number. Truth of $(P, \varphi)$ under $\alpha$ is defined by
recursion on $P$. If $P$ is empty, it means that $\varphi$ is nonempty and the value of its last
gate under $\alpha$ is true. If $P$ starts with $(q, v)$ followed by the prefix $P'$, it means that
$(P', \varphi)$ is true under $\alpha[v \mapsto \mathrm{true}]$ or under
$\alpha[v \mapsto \mathrm{false}]$ when $q$ is $\exists$, and under both when $q$ is $\forall$,
where $\alpha[v \mapsto b]$ agrees with $\alpha$ except that it sends $v$ to $b$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.EvalQBFK`, a definition declared in [WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/quantified-boolean-formulas-with-bounded-alterna/index.html#eval-qbfk).

## Quantifier alternations after a given quantifier

For a quantifier $p$ and a quantifier
prefix $(q_1, v_1), \dots, (q_n, v_n)$, the number of indices $1 \le i \le n$ with
$q_i \ne q_{i-1}$, where $q_0 = p$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.blockCountAux`, a definition declared in [WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/quantified-boolean-formulas-with-bounded-alterna/index.html#block-count-aux).

## Number of quantifier blocks

The number of maximal blocks of consecutive equal quantifiers
in a quantifier prefix $(q_1, v_1), \dots, (q_n, v_n)$: it is $0$ if $n = 0$, and otherwise $1$
plus the number of indices $2 \le i \le n$ with $q_i \ne q_{i-1}$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.blockCount`, a definition declared in [WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/quantified-boolean-formulas-with-bounded-alterna/index.html#block-count).

## The decision problem $\mathrm{QSAT}_k$

For a natural number $k$, $\mathrm{QSAT}_k$ accepts
a bitstring $x$ exactly when $x$ decodes, under the standard bitstring encoding, to a pair
$(P, \varphi)$ of a quantifier prefix $P = (q_1, v_1), \dots, (q_n, v_n)$, where each $q_i$ is
$\exists$ (true) or $\forall$ (false) and each $v_i$ is a natural number, and a matrix circuit
$\varphi$, such that: $P$ is nonempty and $q_1$ is $\exists$; $(v_1, \dots, v_n)$ is a
permutation of $(0, \dots, n - 1)$; every variable of $\varphi$ is less than $n$; $\varphi$ is
well formed; $P$ has exactly $k$ quantifier blocks; and $(P, \varphi)$ is true under the
assignment that sends every variable to false. A bitstring that does not decode is rejected.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.qsatKDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/quantified-boolean-formulas-with-bounded-alterna/index.html#qsat-kdec).

## $\mathrm{QSAT}_k$ is $\Sigma_k^p$-complete, uniformly in $k$

For every natural number
$k \ge 1$, the decision problem $\mathrm{QSAT}_k$ lies in $\Sigma_k^p$, and every decision problem
$L$ in $\Sigma_k^p$ reduces to $\mathrm{QSAT}_k$ by a polynomial-time many-one reduction.

## Sources

- L. J. Stockmeyer, "The polynomial-time hierarchy", Theoretical Computer Science 3 (1977), 1-22; A. R. Meyer, "A polynomial hierarchy" (see also S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Chapter 5).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.QSATKComplete.qsat_k_sigma_k_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/QSATKCompleteWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/quantified-boolean-formulas-with-bounded-alterna/index.html#qsat-k-sigma-k-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quantified Boolean formulas with bounded alternation](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/quantified-boolean-formulas-with-bounded-alterna/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/completeness-other-classes/quantified-boolean-formulas-with-bounded-alterna)
