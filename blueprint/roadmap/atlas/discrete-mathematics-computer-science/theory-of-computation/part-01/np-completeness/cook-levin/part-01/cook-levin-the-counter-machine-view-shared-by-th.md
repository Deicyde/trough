---
declaration: section
origin: cited
lean: Cslib.Complexity.CookLevin.CounterView.MS, Cslib.Complexity.CookLevin.CounterView.SK, Cslib.Complexity.CookLevin.CounterView.SΓ, Cslib.Complexity.CookLevin.CounterView.st, Cslib.Complexity.CookLevin.CounterView.mulS, Cslib.Complexity.CookLevin.CounterView.gapS, Cslib.Complexity.CookLevin.CounterView.bud_st, Cslib.Complexity.CookLevin.CounterView.stLoop
statement: formalized
proof: formalized
---

# Cook-Levin: the counter-machine view shared by the clause generators

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-counter-machine-view-shared-by-th/index.html).

## Stages of the multiplication routine

The stages of the counter-machine multiplication
routine form the four-element type with elements head, body, l2 and rest.

Formalized by `Cslib.Complexity.CookLevin.CounterView.MS`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/CounterView.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/CounterView.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-counter-machine-view-shared-by-th/index.html#ms).

## Stacks of a counter machine

For a type $C$, the stacks of a counter machine with
counters indexed by $C$ are an output stack $\mathrm{out}$ and one counter stack $c_x$ for each
$x \in C$.

Formalized by `Cslib.Complexity.CookLevin.CounterView.SK`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/CounterView.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/CounterView.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-counter-machine-view-shared-by-th/index.html#sk).

## Alphabets of a counter machine

For a type $C$, the output stack $\mathrm{out}$ of a
counter machine with counters indexed by $C$ has the Booleans as its alphabet, and each counter
stack $c_x$ has a one-element alphabet.

Formalized by `Cslib.Complexity.CookLevin.CounterView.SΓ`, an abbreviation declared in [CSLibExt/Computability/Complexity/CookLevin/CounterView.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/CounterView.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-counter-machine-view-shared-by-th/index.html#s).

## Stacks holding given counter values

For a type $C$, counter values
$f : C \to \mathbb{N}$ and a list $o$ of Booleans, $\mathrm{st}(f, o)$ is the stack contents of a
counter machine whose output stack $\mathrm{out}$ holds $o$ and whose counter stack $c_x$ holds
exactly $f(x)$ copies of the unit symbol, for each $x \in C$.

Formalized by `Cslib.Complexity.CookLevin.CounterView.st`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/CounterView.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/CounterView.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-counter-machine-view-shared-by-th/index.html#st).

## The multiplication routine of a counter machine

Let $a, a_d, b, c, t$ be
counters, let $\mathrm{mk}$ assign a label to each stage of the multiplication routine, and let
$\mathrm{next}$ be a label. The routine assigns to each stage the following counter-machine
instruction. At head: pop a unit from $a$, then push a unit onto $a_d$ and go to
$\mathrm{mk}(\mathrm{body})$, or go to $\mathrm{mk}(\mathrm{rest})$ if $a$ was empty. At body:
pop a unit from $b$, then push a unit onto each of $c$ and $t$ and go to
$\mathrm{mk}(\mathrm{body})$, or go to $\mathrm{mk}(\mathrm{l2})$ if $b$ was empty. At l2: pop a
unit from $t$, then push a unit onto $b$ and go to $\mathrm{mk}(\mathrm{l2})$, or go to
$\mathrm{mk}(\mathrm{head})$ if $t$ was empty. At rest: pop a unit from $a_d$, then push a unit
onto $a$ and go to $\mathrm{mk}(\mathrm{rest})$, or go to $\mathrm{next}$ if $a_d$ was empty.
In each instruction the pop sets the flag to true if a unit was popped and to false if the
counter was empty, and the pushes leave the flag unchanged.

Started at head with $a, a_d, b, c, t$ distinct and $a_d$ and $t$ empty, the routine ends at
$\mathrm{next}$ having added $a \cdot b$ to $c$, with every other counter unchanged; $a_d$
serves as the loop index and $t$ as scratch.

Formalized by `Cslib.Complexity.CookLevin.CounterView.mulS`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/CounterView.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/CounterView.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-counter-machine-view-shared-by-th/index.html#mul-s).

## Gap emission in the counter view

Let $M$ be a counter machine, let $P, Q, T_1, T_2$ be
pairwise distinct counters, let $y$ be a list of Booleans, let $\mathrm{dec}$, $\mathrm{cmp}$,
$\mathrm{emit}$, $z$, $\mathrm{next}$ be labels, and let $r$, $r'$, $\mathrm{out}$ assign a label
to each comparison outcome $\omega$, which is one of $\mathrm{lt}$, $\mathrm{eq}$, $\mathrm{gt}$.
In the instructions below, every pop sets the flag to true if a unit was popped and to false if
the stack was empty, and pushing or prepending leaves the flag unchanged.
Suppose that at $\mathrm{dec}$, $M$ pops a unit from $P$ and goes to $\mathrm{cmp}$, or to $z$ if
$P$ was empty; at $\mathrm{cmp}$, $M$ pops a unit from each of $P$ and $Q$, pushes a unit onto
$T_1$ if $P$ was nonempty and onto $T_2$ if $Q$ was nonempty, and goes back to $\mathrm{cmp}$ if
both were nonempty, and otherwise to $r(\mathrm{lt})$, $r(\mathrm{eq})$ or $r(\mathrm{gt})$
according as only $Q$, neither, or only $P$ was nonempty; for each $\omega$, at $r(\omega)$, $M$
pops a unit from $T_1$, then pushes a unit onto $P$ and stays at $r(\omega)$, or goes to
$r'(\omega)$ if $T_1$ was empty; at $r'(\omega)$, $M$ pops a unit from $T_2$, then pushes a unit
onto $Q$ and stays at $r'(\omega)$, or goes to $\mathrm{out}(\omega)$ if $T_2$ was empty;
$\mathrm{out}(\mathrm{eq}) = \mathrm{next}$ and
$\mathrm{out}(\mathrm{lt}) = \mathrm{out}(\mathrm{gt}) = \mathrm{emit}$; and at $\mathrm{emit}$,
$M$ prepends $y$ to the output stack and goes to $\mathrm{dec}$. Let $q, g \in \mathbb{N}$ and
let $F$ be counter values with $F(P) = q + g + 1$, $F(Q) = q$ and $F(T_1) = F(T_2) = 0$. Then
for every flag $v$ and every list $o$ of Booleans, $M$ goes in exactly
$g(3q + 6) + 3q + 4$ steps from label $\mathrm{dec}$, flag $v$ and stacks $\mathrm{st}(F, o)$
to label $\mathrm{next}$, flag false and stacks $\mathrm{st}(F', y^g o)$, where $F'$ agrees
with $F$ except that $F'(P) = q$, and $y^g o$ is $g$ copies of $y$ followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.CounterView.gapS`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/CounterView.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/CounterView.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-counter-machine-view-shared-by-th/index.html#gap-s).

## Budgeted runs transport along equal counter values

Let $M$ be a counter machine, let
$K, X \in \mathbb{N}$, let $F$ and $F'$ be counter values with $F = F'$, let $l$ be a label or
the halting state, $v$ a flag, $o$ a list of Booleans and $d$ a configuration. If there is $n$
with $K + n \le X$ such that $M$ goes in exactly $n$ steps from the configuration with label $l$,
flag $v$ and stacks $\mathrm{st}(F', o)$ to $d$, then the same holds from the configuration with
label $l$, flag $v$ and stacks $\mathrm{st}(F, o)$.

Formalized by `Cslib.Complexity.CookLevin.CounterView.bud_st`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/CounterView.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/CounterView.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-counter-machine-view-shared-by-th/index.html#bud-st).

## A runtime `for` loop in the counter view

Let $M$ be a counter machine, let $c \ne c_d$
be counters, and let $\mathrm{head}$, $\mathrm{body}$, $\mathrm{rest}$, $\mathrm{next}$ be labels
such that at $\mathrm{head}$, $M$ pops a unit from $c$, then pushes a unit onto $c_d$ and goes to
$\mathrm{body}$, or goes to $\mathrm{rest}$ if $c$ was empty; and at $\mathrm{rest}$, $M$ pops a
unit from $c_d$, then pushes a unit onto $c$ and stays at $\mathrm{rest}$, or goes to
$\mathrm{next}$ if $c_d$ was empty. Each of these pops sets the flag to true if a unit was popped
and to false if the stack was empty, and the pushes leave the flag unchanged. Let
$n, B \in \mathbb{N}$, let $\mathrm{blk}$ assign a list of Booleans to each natural number, and
let $f$ be counter values with $f(c) = n$ and $f(c_d) = 0$; for $t < n$ write $g_t$ for the
counter values that agree with $f$ except that $g_t(c) = t$ and $g_t(c_d) = n - t$, and write
juxtaposition of lists for concatenation. Suppose that for every $t < n$ and every list $o$ of
Booleans, $M$ goes in at most $B$ steps from label $\mathrm{body}$, flag true and stacks
$\mathrm{st}(g_t, o)$ to label $\mathrm{head}$, some flag and stacks
$\mathrm{st}(g_t, \mathrm{blk}(t)\, o)$. Then for every flag $v$ and every list $o$ of Booleans,
$M$ goes in at most $n(B + 1) + n + 2$ steps from label $\mathrm{head}$, flag $v$ and stacks
$\mathrm{st}(f, o)$ to label $\mathrm{next}$, flag false and stacks
$\mathrm{st}(f, \mathrm{blk}(0)\, \mathrm{blk}(1) \cdots \mathrm{blk}(n-1)\, o)$.

The body runs with $c$ holding $t = n - 1, \dots, 0$ in that order, so the blocks end up in
ascending order.

Formalized by `Cslib.Complexity.CookLevin.CounterView.stLoop`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/CounterView.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/CounterView.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-counter-machine-view-shared-by-th/index.html#st-loop).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cook-Levin: the counter-machine view shared by the clause generators](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-counter-machine-view-shared-by-th/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-counter-machine-view-shared-by-th)
