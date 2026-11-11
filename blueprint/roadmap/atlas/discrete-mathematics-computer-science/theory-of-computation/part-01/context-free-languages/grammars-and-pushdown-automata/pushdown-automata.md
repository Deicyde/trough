---
declaration: section
origin: cited
lean: Cslib.Automata.PDA, Cslib.Automata.PDA.Config, Cslib.Automata.PDA.Step, Cslib.Automata.PDA.Derives, Cslib.Automata.PDA.Derives.append_input_stack, Cslib.Automata.PDA.FinitelySupported, Cslib.Automata.PDA.initConfig, Cslib.Automata.PDA.accepts
statement: formalized
proof: formalized
---

# Pushdown automata

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html).

## Automata

## Pushdown automaton

A pushdown automaton over an input alphabet $T$, with
states in $\sigma$ and stack alphabet $\Gamma$, consists of a transition function, a start
state in $\sigma$ and an initial stack symbol in $\Gamma$. The transition function assigns
to each state $q$, each input option (a letter of $T$, or none for an
$\varepsilon$-transition) and each popped stack symbol $\gamma$ a finite set of pairs
$(q', u)$ of a next state $q'$ and a list $u$ of stack symbols to push.

This is the generalized model: the state and stack types themselves are unrestricted,
and only each transition is finitely branching. A standard (textbook) pushdown
automaton is additionally finitely supported; without that, the language it accepts can
be an arbitrary language, so the conversion from pushdown automata back to context-free
grammars needs finiteness hypotheses.

Formalized by `Cslib.Automata.PDA`, a structure declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#pda).

## Pushdown automaton configuration

A configuration of a pushdown automaton with input
alphabet $T$, states in $\sigma$ and stack alphabet $\Gamma$ consists of a current state in
$\sigma$, the remaining unread input (a word over $T$), and the stack contents (a list over
$\Gamma$ whose first element is the top of the stack).

Formalized by `Cslib.Automata.PDA.Config`, a structure declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#config).

## One step of a pushdown automaton

Write a configuration of a pushdown automaton
$M$ as $(q, w, s)$: state $q$, remaining input $w$, and stack $s$ listed from the top.
A configuration $(q, w, \gamma s)$ steps to $(q', w, u s)$ whenever $(q', u)$ is an
$\varepsilon$-transition of $M$ from $q$ with top symbol $\gamma$, and a configuration
$(q, a w, \gamma s)$ steps to $(q', w, u s)$ whenever $(q', u)$ is a transition of $M$
from $q$ on the input letter $a$ with top symbol $\gamma$. There are no other steps: a
step pops the top symbol, consumes at most one input letter, and pushes the list $u$
with its head as the new top.

Formalized by `Cslib.Automata.PDA.Step`, an inductive type declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#step).

## Multi-step computation of a pushdown automaton

For a pushdown automaton $M$, a
configuration $c$ derives a configuration $c'$ when $M$ can reach $c'$ from $c$ in zero or more
computation steps; that is, derivation is the reflexive transitive closure of the one-step
computation relation of $M$.

Formalized by `Cslib.Automata.PDA.Derives`, an abbreviation declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#derives).

## Computations extend by unread input and stack bottom

Let $M$ be a pushdown automaton.
If $M$ can compute from a configuration with state $q$, remaining input $w$ and stack $s$ to a
configuration with state $q'$, remaining input $w'$ and stack $s'$, then for every word $v$ and
every list $t$ of stack symbols, $M$ can compute from the configuration with state $q$,
remaining input $wv$ and stack $st$ to the configuration with state $q'$, remaining input $w'v$
and stack $s't$. Here $st$ is the stack $s$ with $t$ placed below it.

Formalized by `Cslib.Automata.PDA.Derives.append_input_stack`, a theorem declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#append-input-stack).

## Finitely supported pushdown automata

A pushdown automaton $M$ is finitely supported when
there are finite sets $\sigma_0$ of states, $\Gamma_0$ of stack symbols and $T_0$ of input letters
such that the start state lies in $\sigma_0$, the initial stack symbol lies in $\Gamma_0$, every
transition from a state in $\sigma_0$ that pops a symbol in $\Gamma_0$ (on any input letter or on
$\varepsilon$) moves to a state in $\sigma_0$ and pushes only symbols in $\Gamma_0$, and there is
no transition from a state in $\sigma_0$ popping a symbol in $\Gamma_0$ that consumes an input
letter outside $T_0$.

This is the finiteness condition of a standard pushdown automaton; computations from the initial
configuration then only ever visit finitely many states, push finitely many stack symbols, and
respond to finitely many input letters.

Formalized by `Cslib.Automata.PDA.FinitelySupported`, a definition declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#finitely-supported).

## Initial configuration of a pushdown automaton

The initial configuration of a pushdown
automaton $M$ on an input word $w$ has the start state of $M$ as its state, all of $w$ as its
remaining input, and the stack consisting of the initial stack symbol of $M$ alone.

Formalized by `Cslib.Automata.PDA.initConfig`, a definition declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#init-config).

## Language accepted by a pushdown automaton

The language accepted by a pushdown
automaton $M$, by empty stack, consists of the words $w$ for which some computation of $M$
leads from the initial configuration on input $w$ to a configuration, in some state, with no
remaining input and an empty stack.

Formalized by `Cslib.Automata.PDA.accepts`, a definition declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#accepts).

## Closed sets of stack symbols

A finite set $\Gamma_0$ of stack symbols is closed for a
pushdown automaton $M$ when every transition of $M$ that pops a symbol in $\Gamma_0$, from any
state and on any input letter or on $\varepsilon$, pushes only symbols in $\Gamma_0$.
Computations starting with a stack inside a closed set keep their stack inside it.

Formalized by `Cslib.Automata.PDA.ClosedUnder`, a definition declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#closed-under).

## Lifting a stack to a set of stack symbols

Given a finite set $\Gamma_0$ of
stack symbols and a stack $s = \gamma_1 \cdots \gamma_n$ all of whose symbols lie in
$\Gamma_0$, the lifted stack is the same list $\gamma_1 \cdots \gamma_n$, in the same
order, regarded as a stack over the alphabet $\Gamma_0$.

Formalized by `Cslib.Automata.PDA.liftStack`, a definition declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#lift-stack).

## Restricting the stack alphabet of a pushdown automaton

Let $M$ be a pushdown
automaton with stack alphabet $\Gamma$, and let $\Gamma_0 \subseteq \Gamma$ be a finite set
of stack symbols that contains the initial stack symbol of $M$ and is closed for $M$.
The restriction of $M$ to $\Gamma_0$ is the pushdown automaton with the same input
alphabet, states and start state as $M$, stack alphabet $\Gamma_0$, and the initial stack
symbol of $M$ as its initial stack symbol. Its transitions from a state $q$ on an input
option $o$ with top symbol $\gamma \in \Gamma_0$ are the transitions $(q', u)$ of $M$ from
$q$ on $o$ with top symbol $\gamma$, with the pushed list $u$ read as a list over
$\Gamma_0$; closedness guarantees that every symbol of $u$ lies in $\Gamma_0$.

The restricted automaton has a finite stack alphabet and accepts the same language as
$M$.

Formalized by `Cslib.Automata.PDA.restrict`, a definition declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#restrict).

## Transitions of the restricted pushdown automaton

Let $M$ be a pushdown
automaton with stack alphabet $\Gamma$, and let $M|_{\Gamma_0}$ be its restriction to a
finite set $\Gamma_0 \subseteq \Gamma$ of stack symbols that contains the initial stack
symbol and is closed for $M$. Let $q, q'$ be states, $o$ an input option (an input
letter, or none for an $\varepsilon$-transition), $\gamma \in \Gamma_0$ and $s$ a list of
symbols of $\Gamma_0$. Then $(q', s)$ is a transition of $M|_{\Gamma_0}$ from $q$ on $o$
with top symbol $\gamma$ if and only if $(q', s)$, with $s$ read as a list of symbols
of $\Gamma$, is a transition of $M$ from $q$ on $o$ with top symbol $\gamma$.

Formalized by `Cslib.Automata.PDA.mem_restrict_step`, a theorem declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#mem-restrict-step).

## Computations of the restriction are computations of the automaton

Let $M$ be a pushdown
automaton and let $\Gamma_0$ be a finite set of stack symbols that contains the initial stack
symbol of $M$ and is closed for $M$. If the restriction of $M$ to $\Gamma_0$ can compute from a
configuration with state $q$, remaining input $w$ and stack $s$ to a configuration with state
$q'$, remaining input $w'$ and stack $s'$, then $M$ can compute from the configuration
$(q, w, s)$ to the configuration $(q', w', s')$, where the stacks $s$ and $s'$ over $\Gamma_0$ are
read as stacks over the full stack alphabet of $M$.

Formalized by `Cslib.Automata.PDA.derives_val_of_derives_restrict`, a theorem declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#derives-val-of-derives-restrict).

## Computations stay inside a closed set of stack symbols

Let $M$ be a pushdown
automaton and $\Gamma_0$ a finite set of stack symbols that is closed for $M$. If a
configuration $c$ derives a configuration $c'$ in zero or more steps of $M$, and every
symbol on the stack of $c$ lies in $\Gamma_0$, then every symbol on the stack of $c'$ lies
in $\Gamma_0$.

Formalized by `Cslib.Automata.PDA.stack_subset_of_derives`, a theorem declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#stack-subset-of-derives).

## Computations inside a closed set lift to the restriction

Let $M$ be a pushdown automaton
and let $\Gamma_0$ be a finite set of stack symbols that contains the initial stack symbol of $M$
and is closed for $M$. Suppose $M$ can compute from a configuration with state $q$, remaining
input $w$ and stack $s$ to a configuration with state $q'$, remaining input $w'$ and stack $s'$,
and every symbol of $s$ lies in $\Gamma_0$. Then the symbols of $s'$ also lie in $\Gamma_0$, and
the restriction of $M$ to $\Gamma_0$ can compute from the configuration $(q, w, s)$ to the
configuration $(q', w', s')$, with $s$ and $s'$ read as stacks over $\Gamma_0$.

Formalized by `Cslib.Automata.PDA.derives_restrict_of_derives`, a theorem declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#derives-restrict-of-derives).

## Restricting the stack alphabet preserves the accepted language

Let $M$ be a pushdown
automaton and let $\Gamma_0$ be a finite set of stack symbols of $M$ that contains the initial
stack symbol of $M$ and is closed for $M$. Then the restriction of $M$ to the stack alphabet
$\Gamma_0$ accepts, by empty stack, exactly the same language as $M$.

Formalized by `Cslib.Automata.PDA.accepts_restrict`, a theorem declared in [CSLibExt/Computability/Automata/PDA/Basic.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/PDA/Basic.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html#accepts-restrict).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pushdown automata](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/pushdown-automata)
