---
declaration: section
origin: cited
lean: Cslib.IMP.Assertion, Cslib.IMP.Assertion.Entails, Cslib.IMP.Assertion.subst, Cslib.IMP.Valid, Cslib.IMP.Valid.whileLoop, Cslib.IMP.wlp, Cslib.IMP.wlp.whileLoop, Cslib.IMP.wlp.invariant_le_while
statement: formalized
proof: formalized
---

# Hoare logic

41 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html).

## Assertion

An assertion is a predicate on program states: it assigns a proposition to
each state. Assertions serve as the preconditions and postconditions of Hoare triples.

Formalized by `Cslib.IMP.Assertion`, an abbreviation declared in [CSLibExt/Languages/IMP/Hoare.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Hoare.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#assertion).

## Entailment of assertions

An assertion $P$ entails an assertion $Q$ when every state
that satisfies $P$ also satisfies $Q$.

Formalized by `Cslib.IMP.Assertion.Entails`, a definition declared in [CSLibExt/Languages/IMP/Hoare.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Hoare.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#entails).

## Substitution in an assertion

Let $P$ be an assertion, $x$ a variable and $e$ an
arithmetic expression. The assertion $P[e/x]$ holds in a state $s$ exactly when $P$ holds in
the state obtained from $s$ by setting the value of $x$ to the value of $e$ in $s$.

Formalized by `Cslib.IMP.Assertion.subst`, a definition declared in [CSLibExt/Languages/IMP/Hoare.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Hoare.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#subst).

## Validity of a Hoare triple

For assertions $P$ and $Q$ and a command $c$, the
partial-correctness Hoare triple $\lbrace P \rbrace\ c\ \lbrace Q \rbrace$ is valid when, for all
states $s$ and $t$, if $s$ satisfies $P$ and executing $c$ from $s$ terminates in $t$ under the
big-step semantics, then $t$ satisfies $Q$.

Formalized by `Cslib.IMP.Valid`, a definition declared in [CSLibExt/Languages/IMP/Hoare.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Hoare.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#valid).

## Invariant rule for while loops

Let $I$ be an assertion, $b$ a Boolean expression and
$c$ a command. Write $I \wedge b$ for the assertion that $I$ holds and $b$ evaluates to true,
and $I \wedge \neg b$ for the assertion that $I$ holds and $b$ evaluates to false. If the
partial-correctness Hoare triple $\lbrace I \wedge b \rbrace\ c\ \lbrace I \rbrace$ is valid,
then so is the triple
$\lbrace I \rbrace\ \mathtt{while}\ b\ \mathtt{do}\ c\ \lbrace I \wedge \neg b \rbrace$.

Formalized by `Cslib.IMP.Valid.whileLoop`, a theorem declared in [CSLibExt/Languages/IMP/Hoare.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Hoare.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#while-loop).

## Weakest liberal precondition

For a command $c$ and an assertion $Q$, the weakest
liberal precondition of $c$ with respect to $Q$ is the assertion that holds in a state $s$
exactly when every state $t$ in which an execution of $c$ from $s$ terminates, under the
big-step semantics, satisfies $Q$.

It is liberal because no termination claim is made: a state from which $c$ has no terminating
execution satisfies it for every $Q$.

Formalized by `Cslib.IMP.wlp`, a definition declared in [CSLibExt/Languages/IMP/Hoare.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Hoare.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#wlp).

## Weakest liberal precondition unfolding of a while loop

Let $b$ be a Boolean expression,
$c$ a command and $Q$ an assertion. Write $\mathrm{wlp}(d, R)$ for the weakest liberal
precondition of a command $d$ with respect to an assertion $R$, and let $W$ be the loop
$\mathbf{while}\ b\ \mathbf{do}\ c$. Then $\mathrm{wlp}(W, Q)$ is the assertion that holds in a
state $s$ exactly when both of the following hold: if $b$ evaluates to false in $s$, then $Q$
holds in $s$; and if $b$ evaluates to true in $s$, then $\mathrm{wlp}(c, \mathrm{wlp}(W, Q))$
holds in $s$.

Formalized by `Cslib.IMP.wlp.whileLoop`, a theorem declared in [CSLibExt/Languages/IMP/Hoare.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Hoare.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#while-loop-2).

## Loop invariants entail the weakest liberal precondition of the loop

Let $I$ and $Q$
be assertions, $b$ a Boolean expression and $c$ a command. Suppose that every state satisfying
$I$ in which $b$ evaluates to true satisfies the weakest liberal precondition of $c$ with
respect to $I$, and that every state satisfying $I$ in which $b$ evaluates to false satisfies
$Q$. Then $I$ entails the weakest liberal precondition of the loop
$\mathtt{while}\ b\ \mathtt{do}\ c$ with respect to $Q$.

Formalized by `Cslib.IMP.wlp.invariant_le_while`, a theorem declared in [CSLibExt/Languages/IMP/Hoare.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Hoare.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#invariant-le-while).

## Validity of total-correctness Hoare triples

For assertions $P$ and $Q$ on states and a
command $c$, the total-correctness Hoare triple with precondition $P$, command $c$ and
postcondition $Q$ is valid when every state $s$ satisfying $P$ has a terminating big-step
execution of $c$ from $s$ ending in a state $t$ that satisfies $Q$.

Formalized by `Cslib.IMP.TValid`, a definition declared in [CSLibExt/Languages/IMP/HoareTotal.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareTotal.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#tvalid).

## Variant rule for while loops

Let $I$ be an assertion (the invariant), $V$ a function
from states to natural numbers (the variant), $b$ a Boolean guard and $c$ a command. Suppose
that for every state $s$ satisfying $I$ in which $b$ evaluates to true, there is a terminating
big-step execution of $c$ from $s$ ending in a state $s'$ that satisfies $I$ with
$V(s') < V(s)$. Then the total-correctness Hoare triple with precondition $I$, command
$\mathtt{while}\ b\ \mathtt{do}\ c$ and postcondition "$I$ holds and $b$ evaluates to false"
is valid.

Formalized by `Cslib.IMP.TValid.whileVariant`, a theorem declared in [CSLibExt/Languages/IMP/HoareTotal.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareTotal.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#while-variant).

## Total correctness implies partial correctness

For assertions $P$, $Q$ and a command
$c$, if the total-correctness Hoare triple with precondition $P$, command $c$ and
postcondition $Q$ is valid, then the partial-correctness Hoare triple with the same
precondition, command and postcondition is valid.

Formalized by `Cslib.IMP.TValid.valid`, a theorem declared in [CSLibExt/Languages/IMP/HoareTotal.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareTotal.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#valid-2).

## Total correctness gives a terminating small-step run

If the total-correctness Hoare
triple with precondition $P$, command $c$ and postcondition $Q$ is valid and a state $s$
satisfies $P$, then there is a state $t$ such that $c$, started in $s$, reaches
$\mathtt{skip}$ with state $t$ in finitely many small steps, and $t$ satisfies $Q$.

Formalized by `Cslib.IMP.TValid.terminates`, a theorem declared in [CSLibExt/Languages/IMP/HoareTotal.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareTotal.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#terminates).

## Weakest precondition for total correctness

For a command $c$ and a postcondition $Q$,
the weakest precondition $\mathrm{wp}(c, Q)$ is the assertion that holds at a state $s$ exactly
when there is a terminating big-step execution of $c$ from $s$ ending in a state that satisfies
$Q$.

Formalized by `Cslib.IMP.wp`, a definition declared in [CSLibExt/Languages/IMP/HoareTotal.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareTotal.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#wp).

## Weakest-precondition unfolding of a while loop

For a Boolean guard $b$, a loop body
$c$, a postcondition $Q$ and a state $s$, the state $s$ satisfies the total-correctness weakest
precondition $\mathrm{wp}(\mathtt{while}\ b\ \mathtt{do}\ c, Q)$ if and only if either $b$
evaluates to false in $s$ and $s$ satisfies $Q$, or $b$ evaluates to true in $s$ and $s$
satisfies $\mathrm{wp}(c, \mathrm{wp}(\mathtt{while}\ b\ \mathtt{do}\ c, Q))$.

Formalized by `Cslib.IMP.wp.while_iff`, a theorem declared in [CSLibExt/Languages/IMP/HoareTotal.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareTotal.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#while-iff).

## Total-correctness weakest precondition implies the weakest liberal precondition

For
every command $c$, postcondition $Q$ and state $s$, if $s$ satisfies the total-correctness
weakest precondition $\mathrm{wp}(c, Q)$, then $s$ satisfies the weakest liberal precondition
$\mathrm{wlp}(c, Q)$.

Formalized by `Cslib.IMP.wp.le_wlp`, a theorem declared in [CSLibExt/Languages/IMP/HoareTotal.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareTotal.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#le-wlp).

## Derivability in Hoare logic for partial correctness

Here an assertion is a predicate on
states, and an assertion $P$ entails an assertion $P'$ when every state satisfying $P$ satisfies
$P'$. For an assertion $P$ and a Boolean expression $b$, the assertion $P \land b$ holds in a
state when $P$ holds there and $b$ evaluates to true in it, and the assertion $P \land \lnot b$
holds in a state when $P$ holds there and $b$ evaluates to false in it. Derivability of
partial-correctness Hoare triples $\{P\}\,c\,\{Q\}$ is the least relation closed under the
following rules, where $P$, $P'$, $Q$, $Q'$, $R$ and $I$ are assertions, $c$, $c_1$ and $c_2$ are
commands, $x$ is a variable, $a$ is an arithmetic expression and $b$ is a Boolean expression.

* Skip: $\{Q\}\,\mathtt{skip}\,\{Q\}$.
* Assignment: $\{Q[a/x]\}\,x := a\,\{Q\}$, where $Q[a/x]$ holds in a state $s$ when $Q$ holds in
  the state obtained from $s$ by setting $x$ to the value of $a$ in $s$.
* Sequencing: from $\{P\}\,c_1\,\{R\}$ and $\{R\}\,c_2\,\{Q\}$ derive $\{P\}\,c_1; c_2\,\{Q\}$.
* Conditional: from $\{P \land b\}\,c_1\,\{Q\}$ and $\{P \land \lnot b\}\,c_2\,\{Q\}$ derive
  $\{P\}\,\mathtt{if}\ b\ \mathtt{then}\ c_1\ \mathtt{else}\ c_2\,\{Q\}$.
* While: from $\{I \land b\}\,c\,\{I\}$ derive
  $\{I\}\,\mathtt{while}\ b\ \mathtt{do}\ c\,\{I \land \lnot b\}$.
* Consequence: if $P$ entails $P'$, $\{P'\}\,c\,\{Q'\}$ is derivable and $Q'$ entails $Q$, then
  $\{P\}\,c\,\{Q\}$ is derivable.

Formalized by `Cslib.IMP.Derivable`, an inductive type declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#derivable).

## Soundness of Hoare logic for partial correctness

Every partial-correctness Hoare triple
$\{P\}\,c\,\{Q\}$ that is derivable in the partial-correctness proof system is valid: for all
states $s$ and $s'$, if $s$ satisfies $P$ and $c$ has a terminating big-step execution from $s$ to
$s'$, then $s'$ satisfies $Q$.

Formalized by `Cslib.IMP.Derivable.sound`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#sound).

## Precondition strengthening for partial correctness

Let $P$, $P'$ and $Q$ be assertions
and $c$ a command. If $P$ entails $P'$ (every state satisfying $P$ satisfies $P'$) and the
partial-correctness triple $\{P'\}\,c\,\{Q\}$ is derivable in the partial-correctness proof
system, then so is $\{P\}\,c\,\{Q\}$.

Formalized by `Cslib.IMP.Derivable.strengthen`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#strengthen).

## The weakest liberal precondition gives a derivable triple

For every command $c$ and
every assertion $Q$, the triple whose precondition is the weakest liberal precondition of $c$
with respect to $Q$, whose command is $c$ and whose postcondition is $Q$ is derivable in
partial-correctness Hoare logic.

Formalized by `Cslib.IMP.derivable_wlp`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#derivable-wlp).

## Relative completeness of total-correctness Hoare logic

For all assertions $P$ and $Q$
and every command $c$, if the total-correctness triple with precondition $P$, command $c$ and
postcondition $Q$ is valid, then it is derivable in total-correctness Hoare logic.

Formalized by `Cslib.IMP.Derivable.complete`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#complete).

## Partial-correctness Hoare logic as an inference system

A Hoare triple, given by a
precondition $P$, a command $c$ and a postcondition $Q$, is derivable in the default inference
system on Hoare triples, which is partial-correctness Hoare logic, if and only if it is valid
for partial correctness.

Formalized by `Cslib.IMP.derivable_iff_valid`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#derivable-iff-valid).

## Partial-correctness Hoare logic matches the denotational semantics

For all assertions
$P$ and $Q$ and every command $c$, the partial-correctness triple with precondition $P$, command
$c$ and postcondition $Q$ is derivable if and only if, for all states $s$ and $t$ such that $P$
holds at $s$ and the pair $(s, t)$ lies in the relational denotation of $c$, $Q$ holds at $t$.

Formalized by `Cslib.IMP.derivable_iff_denote`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#derivable-iff-denote).

## Loop runs with a given number of iterations

Let $b$ be a Boolean expression and $c$ a
command. For a natural number $n$ and states $s$, $s'$, the loop $\mathtt{while}\ b\ \mathtt{do}\ c$
runs from $s$ to $s'$ in $n$ iterations when, started in $s$, it exits in $s'$ after exactly $n$
executions of the body $c$. This is the least relation such that the loop runs from $s$ to $s$ in
$0$ iterations whenever $b$ evaluates to false in $s$, and the loop runs from $s$ to $s'$ in
$n + 1$ iterations whenever $b$ evaluates to true in $s$, the body $c$ has a terminating big-step
execution from $s$ to some state $t$, and the loop runs from $t$ to $s'$ in $n$ iterations.

Formalized by `Cslib.IMP.Iterates`, an inductive type declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#iterates).

## Counted loop runs are big-step executions

Let $b$ be a boolean expression, $c$ a
command, $n$ a natural number and $s$, $t$ states. If the loop
$\mathtt{while}\ b\ \mathtt{do}\ c$, started in $s$, exits in $t$ after exactly $n$
executions of the body $c$, then the loop $\mathtt{while}\ b\ \mathtt{do}\ c$ runs from $s$
to $t$ in the big-step semantics.

Formalized by `Cslib.IMP.Iterates.bigStep`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#big-step).

## Every terminating loop run has an iteration count

Let $b$ be a Boolean expression, $c$ a
command and $s$, $s'$ states. If the loop $\mathtt{while}\ b\ \mathtt{do}\ c$ has a terminating
big-step execution from $s$ to $s'$, then there is a natural number $n$ such that the loop,
started in $s$, exits in $s'$ after exactly $n$ executions of the body $c$.

Formalized by `Cslib.IMP.Iterates.exists_of_bigStep`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#exists-of-big-step).

## Uniqueness of the loop iteration count

Let $b$ be a boolean expression, $c$ a command
and $s$ a state. If the loop $\mathtt{while}\ b\ \mathtt{do}\ c$, started in $s$, exits in
a state $t$ after exactly $n$ executions of the body and also exits in a state $t'$ after
exactly $m$ executions of the body, then $n = m$.

Formalized by `Cslib.IMP.Iterates.count_unique`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#count-unique).

## Loop iteration count

Let $b$ be a Boolean expression, $c$ a command and $s$ a state. If
there are a natural number $n$ and a state $s'$ such that the loop
$\mathtt{while}\ b\ \mathtt{do}\ c$, started in $s$, exits in $s'$ after exactly $n$ executions of
the body $c$, then the iteration count of the loop from $s$ is such an $n$; otherwise it is $0$.

Such an $n$ is unique because IMP is deterministic, so the iteration count is the number of body
executions the loop performs from $s$ before exiting.

Formalized by `Cslib.IMP.iterationCount`, a definition declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#iteration-count).

## The iteration count of a terminating loop run

Let $b$ be a Boolean expression, $c$ a
command, $n$ a natural number and $s$, $s'$ states. If the loop $\mathtt{while}\ b\ \mathtt{do}\ c$,
started in $s$, exits in $s'$ after exactly $n$ executions of the body $c$, then the iteration
count of the loop from $s$ is $n$.

Formalized by `Cslib.IMP.Iterates.iterationCount_eq`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#iteration-count-eq).

## The iteration count of a nonterminating loop is zero

Let $b$ be a Boolean expression, $c$ a
command and $s$ a state. If the loop $\mathtt{while}\ b\ \mathtt{do}\ c$ has no terminating
big-step execution from $s$ to any state, then the iteration count of the loop from $s$ is
$0$.

Formalized by `Cslib.IMP.iterationCount_eq_zero`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#iteration-count-eq-zero).

## Total-correctness Hoare logic

Derivability of total-correctness Hoare triples
$\{P\}\,c\,\{Q\}$, for assertions $P$, $Q$ (predicates on states) and IMP commands $c$, is the
least relation closed under the following rules. In an assertion, $b$ for a boolean expression
means that $b$ evaluates to true and $\neg b$ that it evaluates to false. Skip:
$\{Q\}\,\mathtt{skip}\,\{Q\}$. Assignment: for a variable $x$ and an arithmetic expression $a$,
$\{Q[a/x]\}\,x := a\,\{Q\}$, where $Q[a/x]$ holds in a state $s$ iff $Q$ holds in $s$ updated at
$x$ to the value of $a$ in $s$. Sequencing: from $\{P\}\,c_1\,\{R\}$ and $\{R\}\,c_2\,\{Q\}$
derive $\{P\}\,c_1; c_2\,\{Q\}$. Conditional: from $\{P \wedge b\}\,c_1\,\{Q\}$ and
$\{P \wedge \neg b\}\,c_2\,\{Q\}$ derive
$\{P\}\,\mathtt{if}\ b\ \mathtt{then}\ c_1\ \mathtt{else}\ c_2\,\{Q\}$. Loop (variant rule): for an
assertion $I$ and a map $V$ from states to natural numbers, if for every natural number $n$ the
triple $\{I \wedge b \wedge V = n\}\,c\,\{I \wedge V < n\}$ is derivable, derive
$\{I\}\,\mathtt{while}\ b\ \mathtt{do}\ c\,\{I \wedge \neg b\}$. Consequence: if $P$ entails $P'$,
$\{P'\}\,c\,\{Q'\}$ is derivable and $Q'$ entails $Q$, derive $\{P\}\,c\,\{Q\}$, where entailment
is pointwise implication.

Formalized by `Cslib.IMP.TDerivable`, an inductive type declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#tderivable).

## Soundness of total-correctness Hoare logic

For all assertions $P$ and $Q$ and every
command $c$, if the triple $\{P\}\,c\,\{Q\}$ is derivable in total-correctness Hoare logic, then
it is valid for total correctness: every state satisfying $P$ has a terminating big-step
execution of $c$ ending in a state that satisfies $Q$.

Formalized by `Cslib.IMP.TDerivable.sound`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#sound-2).

## Precondition strengthening for total correctness

Let $P$, $P'$ and $Q$ be assertions and
$c$ a command. If $P$ entails $P'$ (every state satisfying $P$ satisfies $P'$) and the triple
$\{P'\}\,c\,\{Q\}$ is derivable in total-correctness Hoare logic, then so is
$\{P\}\,c\,\{Q\}$.

Formalized by `Cslib.IMP.TDerivable.strengthen`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#strengthen-2).

## The weakest-precondition triple is derivable in total-correctness Hoare logic

For every
IMP command $c$ and every assertion $Q$ (a predicate on states), the triple
$\{\mathrm{wp}(c, Q)\}\,c\,\{Q\}$ is derivable in the total-correctness Hoare logic. Here
$\mathrm{wp}(c, Q)$ is the semantic weakest precondition: it holds in a state $s$ exactly when
there is a terminating execution of $c$ from $s$ ending in a state satisfying $Q$.

Formalized by `Cslib.IMP.tderivable_wp`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#tderivable-wp).

## Total-correctness Hoare logic is relatively complete

For all assertions $P$ and $Q$ and
every command $c$, if the total-correctness Hoare triple $\{P\}\,c\,\{Q\}$ is valid, then it is
derivable in total-correctness Hoare logic.

Formalized by `Cslib.IMP.TDerivable.complete`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#complete-2).

## Total-correctness derivations give partial-correctness derivations

For all assertions
$P$ and $Q$ and every command $c$, if the triple with precondition $P$, command $c$ and
postcondition $Q$ is derivable in total-correctness Hoare logic, then it is derivable in
partial-correctness Hoare logic.

Formalized by `Cslib.IMP.TDerivable.derivable`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#derivable-2).

## Soundness and relative completeness of total-correctness Hoare logic

For all assertions
$P$, $Q$ (predicates on states) and every IMP command $c$, the triple $\{P\}\,c\,\{Q\}$ is
derivable in the total-correctness Hoare logic if and only if it is totally valid.

Formalized by `Cslib.IMP.tderivable_iff_tvalid`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#tderivable-iff-tvalid).

## Total-correctness Hoare logic is sound and complete for the denotational semantics

For
all assertions $P$, $Q$ (predicates on states) and every IMP command $c$, the triple
$\{P\}\,c\,\{Q\}$ is derivable in the total-correctness Hoare logic if and only if for every
state $s$ satisfying $P$ there is a state $s'$ such that $(s, s')$ lies in the relational
denotation of $c$ and $s'$ satisfies $Q$.

Formalized by `Cslib.IMP.tderivable_iff_denote`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#tderivable-iff-denote).

## Hoare triples

A Hoare triple $\{P\}\,c\,\{Q\}$ consists of a precondition $P$ and a
postcondition $Q$, both assertions (predicates on states), and an IMP command $c$. It is the
judgement form of both the partial-correctness and the total-correctness Hoare logic.

Formalized by `Cslib.IMP.Triple`, a structure declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#triple).

## Total-correctness tag for Hoare triples

An empty type used only as a label: derivability
of Hoare triples in the total-correctness Hoare logic is registered as an inference system under
this tag, while partial-correctness derivability is the default inference system on Hoare
triples.

Formalized by `Cslib.IMP.TotalCorrectness`, an inductive type declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#total-correctness).

## Derivability in the default inference system on Hoare triples is validity

For every
Hoare triple $\{P\}\,c\,\{Q\}$, the triple is derivable in the default inference system on Hoare
triples, which is partial-correctness Hoare logic, if and only if it is valid for partial
correctness.

Formalized by `Cslib.IMP.Triple.derivable_iff_valid`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 439](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L439). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#derivable-iff-valid-2).

## Total-correctness Hoare logic as an inference system

A Hoare triple, given by a
precondition $P$, a command $c$ and a postcondition $Q$, is derivable in the inference system on
Hoare triples tagged total correctness, which is total-correctness Hoare logic, if and only if
it is valid for total correctness.

Formalized by `Cslib.IMP.Triple.derivableIn_totalCorrectness_iff_tvalid`, a theorem declared in [CSLibExt/Languages/IMP/HoareCompleteness.lean, line 445](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/HoareCompleteness.lean#L445). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html#derivable-in-total-correctness-iff-tvali).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hoare logic](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/hoare-logic/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/program-logics-and-verification/hoare-logic)
