---
declaration: section
origin: cited
lean: Cslib.IMP.whileFun, Cslib.IMP.whileFun_mono, Cslib.IMP.whileOrderHom, Cslib.IMP.Denote, Cslib.IMP.Denote.while_eq, Cslib.IMP.Denote.while_iff, Cslib.IMP.Denote.while_ind, Cslib.IMP.Denote.bigStep_of_denote
statement: formalized
proof: formalized
---

# Denotational semantics of IMP

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/denotational-semantics-of-imp/index.html).

## IMP

## One-step unfolding functional of a while loop

Given a Boolean expression $b$ (the guard)
and a binary relation $B$ on states (the body relation), the functional sends a relation $R$ on
states to the relation that relates $s$ to $s'$ exactly when either $b$ evaluates to false in
$s$ and $s' = s$, or $b$ evaluates to true in $s$ and there is a state $m$ with $B$ relating
$s$ to $m$ and $R$ relating $m$ to $s'$.

Formalized by `Cslib.IMP.whileFun`, a definition declared in [CSLibExt/Languages/IMP/Denotational.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Denotational.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/denotational-semantics-of-imp/index.html#while-fun).

## Monotonicity of the while-loop unfolding functional

Let $b$ be a Boolean expression, $B$
a binary relation on states, and $\Phi$ the one-step unfolding functional of a while loop with
guard $b$ and body relation $B$. Then $\Phi$ is monotone for inclusion of relations: for all
relations $R_1$ and $R_2$ on states with $R_1 \subseteq R_2$, we have
$\Phi(R_1) \subseteq \Phi(R_2)$.

Formalized by `Cslib.IMP.whileFun_mono`, a theorem declared in [CSLibExt/Languages/IMP/Denotational.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Denotational.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/denotational-semantics-of-imp/index.html#while-fun-mono).

## The while-loop functional as a monotone map

For a boolean guard $b$ and a relation $B$
between states (the body denotation), this is the map $\Phi$ on relations between states, ordered
by inclusion, where $\Phi(R)$ relates $s$ to $s'$ exactly when either $b$ is false in $s$ and
$s' = s$, or $b$ is true in $s$ and there is a state $m$ with $B(s, m)$ and $R(m, s')$. The map
$\Phi$ is monotone: $R_1 \subseteq R_2$ implies $\Phi(R_1) \subseteq \Phi(R_2)$.

Formalized by `Cslib.IMP.whileOrderHom`, a definition declared in [CSLibExt/Languages/IMP/Denotational.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Denotational.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/denotational-semantics-of-imp/index.html#while-order-hom).

## Relational denotational semantics of IMP

The denotation of an IMP command is a binary
relation on states, defined by recursion on the command. The command $\mathtt{skip}$ relates
$s$ to $s'$ iff $s' = s$. For a variable identifier $x$ and an arithmetic expression $a$, the
assignment $x := a$ relates $s$ to $s'$ iff $s'$ is $s$ with $x$ updated to the value of $a$
in $s$. The sequence $c_1; c_2$ relates $s$ to $s'$ iff there is a state $m$ such that $c_1$
relates $s$ to $m$ and $c_2$ relates $m$ to $s'$. For a Boolean expression $b$, the conditional
$\mathtt{if}\ b\ \mathtt{then}\ t\ \mathtt{else}\ e$ relates $s$ to $s'$ iff either $b$
evaluates to true in $s$ and $t$ relates $s$ to $s'$, or $b$ evaluates to false in $s$ and $e$
relates $s$ to $s'$. The denotation of $\mathtt{while}\ b\ \mathtt{do}\ c$ is the least fixed
point, for inclusion of relations, of the one-step unfolding functional of a while loop with
guard $b$ and body relation the denotation of $c$.

Formalized by `Cslib.IMP.Denote`, a definition declared in [CSLibExt/Languages/IMP/Denotational.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Denotational.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/denotational-semantics-of-imp/index.html#denote).

## The while denotation is a fixed point

Let $b$ be a Boolean expression and $c$ an IMP
command, let $W$ be the relational denotation of $\mathtt{while}\ b\ \mathtt{do}\ c$, and let
$\Phi$ be the one-step unfolding functional of a while loop with guard $b$ and body relation the
denotation of $c$. Then $W = \Phi(W)$.

Formalized by `Cslib.IMP.Denote.while_eq`, a theorem declared in [CSLibExt/Languages/IMP/Denotational.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Denotational.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/denotational-semantics-of-imp/index.html#while-eq).

## Unfolding equation for the while denotation

For every Boolean expression $b$, IMP command
$c$ and states $s$ and $s'$, the relational denotation of $\mathtt{while}\ b\ \mathtt{do}\ c$
relates $s$ to $s'$ if and only if either $b$ evaluates to false in $s$ and $s' = s$, or $b$
evaluates to true in $s$ and there is a state $m$ such that the denotation of $c$ relates $s$ to
$m$ and the denotation of the loop relates $m$ to $s'$.

Formalized by `Cslib.IMP.Denote.while_iff`, a theorem declared in [CSLibExt/Languages/IMP/Denotational.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Denotational.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/denotational-semantics-of-imp/index.html#while-iff).

## Park induction for while loops

Let $b$ be a Boolean expression, $c$ an IMP command and
$P$ a binary relation on states, and let $\Phi$ be the one-step unfolding functional of a while
loop with guard $b$ and body relation the denotation of $c$. If $\Phi(P) \subseteq P$, then
for all states $s$ and $s'$ related by the relational denotation of
$\mathtt{while}\ b\ \mathtt{do}\ c$, $P$ relates $s$ to $s'$.

Formalized by `Cslib.IMP.Denote.while_ind`, a theorem declared in [CSLibExt/Languages/IMP/Denotational.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Denotational.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/denotational-semantics-of-imp/index.html#while-ind).

## Denotational executions are big-step executions

For every IMP command $c$ and all
states $s$ and $s'$, if the relational denotation of $c$ relates $s$ to $s'$, then executing $c$
from $s$ terminates in $s'$ according to the big-step semantics.

Formalized by `Cslib.IMP.Denote.bigStep_of_denote`, a theorem declared in [CSLibExt/Languages/IMP/Denotational.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Denotational.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/denotational-semantics-of-imp/index.html#big-step-of-denote).

## Big-step executions are denotational executions

For every IMP command $c$ and all
states $s$ and $s'$, if executing $c$ from $s$ terminates in $s'$ according to the big-step
semantics, then the relational denotation of $c$ relates $s$ to $s'$.

Formalized by `Cslib.IMP.Denote.denote_of_bigStep`, a theorem declared in [CSLibExt/Languages/IMP/Denotational.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Denotational.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/denotational-semantics-of-imp/index.html#denote-of-big-step).

## Agreement of the denotational and big-step semantics of IMP

For every IMP command $c$
and all states $s$ and $s'$, the relational denotation of $c$ relates $s$ to $s'$ if and only
if executing $c$ from $s$ terminates in $s'$ according to the big-step semantics.

Formalized by `Cslib.IMP.Denote.iff_bigStep`, a theorem declared in [CSLibExt/Languages/IMP/Denotational.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Denotational.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/denotational-semantics-of-imp/index.html#iff-big-step).

## The denotational semantics of IMP is deterministic

For every IMP command $c$ and all
states $s$, $s_1$ and $s_2$, if the relational denotation of $c$ relates $s$ to $s_1$ and $s$
to $s_2$, then $s_1 = s_2$.

The proof goes through the agreement with the deterministic big-step semantics.

Formalized by `Cslib.IMP.Denote.deterministic`, a theorem declared in [CSLibExt/Languages/IMP/Denotational.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/Denotational.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/denotational-semantics-of-imp/index.html#deterministic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Denotational semantics of IMP](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/denotational-semantics-of-imp/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/programming-language-semantics/denotational-semantics-of-imp)
