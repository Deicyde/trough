---
declaration: section
origin: cited
lean: Cslib.IMP.State, Cslib.IMP.AExp, Cslib.IMP.BExp, Cslib.IMP.Cmd, Cslib.IMP.AExp.eval, Cslib.IMP.BExp.eval, Cslib.IMP.BigStep, Cslib.IMP.BigStep.deterministic
statement: formalized
proof: formalized
---

# Operational semantics of IMP

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html).

## IMP program states

A state of an IMP program is a function
$\sigma : \mathbb{N} \to \mathbb{N}$ assigning a natural-number value $\sigma(i)$ to each variable,
where variables are identified by natural numbers $i$.

Formalized by `Cslib.IMP.State`, an abbreviation declared in [CSLibExt/Languages/IMP/Syntax.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Syntax.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#state).

## Arithmetic expressions of IMP

The arithmetic expressions of IMP are built inductively
from the constants $n$, one for each natural number $n$, and the variables $x_i$, one for each
natural number $i$: if $a_1$ and $a_2$ are arithmetic expressions, then so are $a_1 + a_2$,
$a_1 - a_2$ and $a_1 \cdot a_2$.

Formalized by `Cslib.IMP.AExp`, an inductive type declared in [CSLibExt/Languages/IMP/Syntax.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Syntax.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#aexp).

## Boolean expressions of IMP

The Boolean expressions of IMP are built inductively from the
constants true and false and the comparisons $a_1 = a_2$ and $a_1 \le a_2$ of arithmetic
expressions $a_1, a_2$: if $b$, $b_1$ and $b_2$ are Boolean expressions, then so are the negation
$\neg b$ and the conjunction $b_1 \wedge b_2$.

Formalized by `Cslib.IMP.BExp`, an inductive type declared in [CSLibExt/Languages/IMP/Syntax.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Syntax.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#bexp).

## Commands of IMP

The commands of the while-language IMP are built inductively from skip
and the assignments $x_i := a$ of an arithmetic expression $a$ to the variable $x_i$ with index
$i \in \mathbb{N}$: if $c$, $c_1$ and $c_2$ are commands and $b$ is a Boolean expression, then so
are the sequential composition $c_1 ; c_2$, the conditional if $b$ then $c_1$ else $c_2$, and the
loop while $b$ do $c$.

Formalized by `Cslib.IMP.Cmd`, an inductive type declared in [CSLibExt/Languages/IMP/Syntax.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Syntax.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#cmd).

## Evaluation of IMP arithmetic expressions

The value of an arithmetic expression in a state
$\sigma : \mathbb{N} \to \mathbb{N}$ is the natural number defined by recursion on the expression:
a constant $n$ has value $n$, the variable $x_i$ with index $i$ has value $\sigma(i)$, and for
arithmetic expressions $a_1$ and $a_2$, the expressions $a_1 + a_2$, $a_1 - a_2$ and
$a_1 \cdot a_2$ have as value the sum, the truncated difference and the product of the values of
$a_1$ and $a_2$. The truncated difference of natural numbers $m$ and $n$ is $\max(m - n, 0)$.

Formalized by `Cslib.IMP.AExp.eval`, a definition declared in [CSLibExt/Languages/IMP/Syntax.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Syntax.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#eval).

## Evaluation of IMP Boolean expressions

The truth value of a Boolean expression in a
state $\sigma : \mathbb{N} \to \mathbb{N}$ is defined by recursion on the expression: the
constants true and false have values true and false; for arithmetic expressions $a_1$ and $a_2$,
the comparison $a_1 = a_2$ is true exactly when the values of $a_1$ and $a_2$ in $\sigma$ are
equal, and $a_1 \le a_2$ is true exactly when the value of $a_1$ is at most the value of $a_2$;
for Boolean expressions $b$, $b_1$ and $b_2$, the negation $\neg b$ is true exactly when $b$ is
false, and the conjunction $b_1 \wedge b_2$ is true exactly when both $b_1$ and $b_2$ are true.

Formalized by `Cslib.IMP.BExp.eval`, a definition declared in [CSLibExt/Languages/IMP/Syntax.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Syntax.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#eval-2).

## Big-step semantics of IMP

The big-step relation says when running a command $c$ from a
state $s$ terminates in a state $t$; we then say that $c$ takes $s$ to $t$. It is the least
relation satisfying the following rules. The command $\mathtt{skip}$ takes $s$ to $s$. The
assignment $x := a$ takes $s$ to the state $s[x \mapsto a(s)]$, which agrees with $s$ except that
$x$ has the value $a(s)$ of the arithmetic expression $a$ in $s$. If $c_1$ takes $s$ to $u$ and
$c_2$ takes $u$ to $t$, then the sequence $c_1 ; c_2$ takes $s$ to $t$. If the Boolean expression
$b$ is true in $s$ and $c_1$ takes $s$ to $t$, then
$\mathtt{if}\ b\ \mathtt{then}\ c_1\ \mathtt{else}\ c_2$ takes $s$ to $t$; if $b$ is false in $s$
and $c_2$ takes $s$ to $t$, then it also takes $s$ to $t$. If $b$ is false in $s$, then the loop
$\mathtt{while}\ b\ \mathtt{do}\ c$ takes $s$ to $s$; if $b$ is true in $s$, $c$ takes $s$ to $u$
and the loop takes $u$ to $t$, then the loop takes $s$ to $t$.

Formalized by `Cslib.IMP.BigStep`, an inductive type declared in [CSLibExt/Languages/IMP/BigStep.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/BigStep.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#big-step).

## Determinism of IMP big-step semantics

For every command $c$ and every state $s$, if $c$
run from $s$ terminates in a state $t_1$ and also in a state $t_2$ under the big-step semantics,
then $t_1 = t_2$.

Formalized by `Cslib.IMP.BigStep.deterministic`, a theorem declared in [CSLibExt/Languages/IMP/BigStep.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/BigStep.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#deterministic).

## IMP configuration

A configuration of IMP is a pair $(c, \sigma)$ of a command $c$ and a
state $\sigma$.

Formalized by `Cslib.IMP.Config`, an abbreviation declared in [CSLibExt/Languages/IMP/SmallStep.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/SmallStep.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#config).

## IMP small-step relation

The single-step relation $\to$ on IMP configurations is the
smallest relation satisfying the following rules, for all variables $x$, arithmetic expressions
$a$, Boolean expressions $b$, commands $c, c_1, c_1', c_2$ and states $\sigma, \sigma'$.
Assignment: $(x := a, \sigma) \to (\mathtt{skip}, \sigma[x \mapsto v])$, where $v$ is the value
of $a$ in $\sigma$. Sequencing: $(\mathtt{skip}; c_2, \sigma) \to (c_2, \sigma)$, and if
$(c_1, \sigma) \to (c_1', \sigma')$ then $(c_1; c_2, \sigma) \to (c_1'; c_2, \sigma')$.
Conditional: $(\mathtt{if}\ b\ \mathtt{then}\ c_1\ \mathtt{else}\ c_2, \sigma)$ steps to
$(c_1, \sigma)$ if $b$ evaluates to true in $\sigma$ and to $(c_2, \sigma)$ if it evaluates to
false. Loop: $(\mathtt{while}\ b\ \mathtt{do}\ c, \sigma)$ steps to $(W, \sigma)$, where $W$ is
the command $\mathtt{if}\ b\ \mathtt{then}\ (c; \mathtt{while}\ b\ \mathtt{do}\ c)$
$\mathtt{else}\ \mathtt{skip}$.

Formalized by `Cslib.IMP.Step`, an inductive type declared in [CSLibExt/Languages/IMP/SmallStep.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/SmallStep.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#step).

## IMP multi-step relation

The relation $\to^*$ on IMP configurations is the reflexive,
transitive closure of the small-step relation: $x \to^* y$ when $y$ is reached from $x$ by a
finite sequence of zero or more small steps.

Formalized by `Cslib.IMP.Steps`, an abbreviation declared in [CSLibExt/Languages/IMP/SmallStep.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/SmallStep.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#steps).

## Termination of an IMP command

A command $c$ terminates from an initial state $\sigma$
in a final state $\tau$ when the configuration $(c, \sigma)$ reaches $(\mathtt{skip}, \tau)$ in
finitely many small steps.

Formalized by `Cslib.IMP.Terminates`, a definition declared in [CSLibExt/Languages/IMP/SmallStep.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/SmallStep.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#terminates).

## Determinism of IMP small-step semantics

For all IMP configurations $x$, $y$, $z$, if
$x$ steps to $y$ and $x$ steps to $z$ in one small step, then $y = z$.

Formalized by `Cslib.IMP.Step.deterministic`, a theorem declared in [CSLibExt/Languages/IMP/SmallStep.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/SmallStep.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#deterministic-3).

## Big-step executions terminate in small steps

For every IMP command $c$ and states $s$ and
$s'$, if $c$ evaluates from $s$ to $s'$ in the big-step semantics, then $c$ started in $s$
terminates by small steps in $s'$: finitely many small steps lead from the configuration $(c, s)$
to $(\mathrm{skip}, s')$.

Formalized by `Cslib.IMP.Terminates.of_bigStep`, a theorem declared in [CSLibExt/Languages/IMP/Equivalence.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Equivalence.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#of-big-step).

## Prepending one small step to a big-step execution

Let $x = (c, s)$ and $y = (d, t)$ be
configurations and $s'$ a state. If $x$ moves to $y$ in one small step and $d$ evaluates from $t$
to $s'$ in the big-step semantics, then $c$ evaluates from $s$ to $s'$ in the big-step
semantics.

Formalized by `Cslib.IMP.BigStep.of_step`, a theorem declared in [CSLibExt/Languages/IMP/Equivalence.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Equivalence.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#of-step).

## Prepending finitely many small steps to a big-step execution

Let $x = (c, s)$ and
$y = (d, t)$ be configurations and $s'$ a state. If $x$ reaches $y$ in finitely many (possibly
zero) small steps and $d$ evaluates from $t$ to $s'$ in the big-step semantics, then $c$
evaluates from $s$ to $s'$ in the big-step semantics.

Formalized by `Cslib.IMP.BigStep.of_steps`, a theorem declared in [CSLibExt/Languages/IMP/Equivalence.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Equivalence.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#of-steps).

## Small-step termination implies big-step evaluation

For every IMP command $c$ and states $s$
and $s'$, if $c$ started in $s$ terminates by small steps in $s'$, then $c$ evaluates from $s$ to
$s'$ in the big-step semantics.

Formalized by `Cslib.IMP.BigStep.of_terminates`, a theorem declared in [CSLibExt/Languages/IMP/Equivalence.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Equivalence.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#of-terminates).

## Equivalence of small-step and big-step semantics

For every IMP command $c$ and states $s$
and $s'$, $c$ started in $s$ terminates by small steps in $s'$ if and only if $c$ evaluates from
$s$ to $s'$ in the big-step semantics.

Formalized by `Cslib.IMP.terminates_iff_bigStep`, a theorem declared in [CSLibExt/Languages/IMP/Equivalence.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Equivalence.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#terminates-iff-big-step).

## Small-step termination is deterministic

For every IMP command $c$ and states $s$, $s_1$,
$s_2$, if $c$ started in $s$ terminates by small steps in $s_1$ and also terminates by small steps
in $s_2$, then $s_1 = s_2$.

Formalized by `Cslib.IMP.Terminates.deterministic`, a theorem declared in [CSLibExt/Languages/IMP/Equivalence.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Equivalence.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#deterministic-2).

## Hoare validity via small-step termination

For assertions $P$ and $Q$ on states and an IMP
command $c$, the partial-correctness Hoare triple with precondition $P$, command $c$ and
postcondition $Q$ is valid if and only if, for all states $s$ and $s'$, whenever $P$ holds in $s$
and $c$ started in $s$ terminates by small steps in $s'$, $Q$ holds in $s'$.

Formalized by `Cslib.IMP.Valid.iff_terminates`, a theorem declared in [CSLibExt/Languages/IMP/Equivalence.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Equivalence.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html#iff-terminates).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Operational semantics of IMP](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/programming-language-semantics/operational-semantics-of-imp)
