---
declaration: section
origin: cited
lean: Cslib.Complexity.CookLevin.Accept.codeLits, Cslib.Complexity.CookLevin.Accept.cellLits, Cslib.Complexity.CookLevin.Accept.accFam, Cslib.Complexity.CookLevin.Accept.CK, Cslib.Complexity.CookLevin.Accept.AK, Cslib.Complexity.CookLevin.Accept.AK.bc, Cslib.Complexity.CookLevin.Accept.AK.off, Cslib.Complexity.CookLevin.Accept.AK.sg
statement: formalized
proof: formalized
---

# Cook-Levin: generator machine for the accept family

36 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html).

## The family (pure specification)

## Literals of an accept code clause

For a layout $L$, a code $a_c$, a time $T$, a height $H$
and $u \in \mathbb{N}$, the literal list of code clause $u$ is the single literal whose variable
is the label/state variable $X[T, u]$ (entry $u$ of the label/state block at time $T$, for
height $H$) and which is positive exactly when $u = a_c$.

Formalized by `Cslib.Complexity.CookLevin.Accept.codeLits`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#code-lits).

## Literals of an accept cell clause

For a layout $L$, a stack $k_1$, a symbol code $e_a$,
a time $T$, a height $H$ and $x \in \mathbb{N}$, the literal list of cell clause $x$ is the single
literal whose variable is the cell variable $C[T, k_1, 0, x]$ (time $T$, stack $k_1$, depth $0$
from the top, symbol code $x$, for height $H$) and which is positive exactly when $x = e_a$.

Formalized by `Cslib.Complexity.CookLevin.Accept.cellLits`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#cell-lits).

## The accept family of a layout

Let $L$ be a layout with label block size $A$, $K$ stacks
and $g$ symbol codes, let $n_1, a, k_1, e, T, H$ be natural numbers, $W = A + K H g$ and
$V = (T + 1) W$. The accept family is the CNF formula over $V$ variables made of, first, for each
$u < n_1$ in increasing order, the clause whose only literal is the label variable $X[T, u]$
(variable $T W + u$), positive if $u = a$ and negative otherwise; then, for each $x < g$ in
increasing order, the clause whose only literal is the top-cell variable $C[T, k_1, 0, x]$ of
stack $k_1$ (variable $T W + A + k_1 H g + x$), positive if $x = e$ and negative otherwise. Each
clause is a dense row of $V$ slots: the slot of its variable holds the literal and every other
slot is empty (all slots are empty if the variable is at least $V$).

Formalized by `Cslib.Complexity.CookLevin.Accept.accFam`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#acc-fam).

## Counters of the accept generator

The accept-family generator has sixteen distinct unit
counters, named $\mathsf{Tn}$, $\mathsf{Hs}$, $\mathsf{Gc}$, $\mathsf{HG}$, $\mathsf{Wc}$,
$\mathsf{Kc}$, $\mathsf{K1}$, $\mathsf{Vc}$, $\mathsf{TW}$, $\mathsf{CB}$, $\mathsf{P}$,
$\mathsf{Q}$, $\mathsf{tmp}$, $\mathsf{md}$, $\mathsf{c1}$ and $\mathsf{c2}$.

Formalized by `Cslib.Complexity.CookLevin.Accept.CK`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#ck).

## Clause kinds of the accept generator

For natural numbers $n_1$ and $g$, a clause kind is
either a code clause $u$ for some $u < n_1$ or a cell clause $x$ for some $x < g$.

Formalized by `Cslib.Complexity.CookLevin.Accept.AK`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#ak).

## Base counter of an accept clause

For a clause kind $c$ of the accept generator, the
base counter of its single literal is the counter $\mathsf{TW}$ when $c$ is a code clause and
the counter $\mathsf{CB}$ when $c$ is a cell clause.

Formalized by `Cslib.Complexity.CookLevin.Accept.AK.bc`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#bc).

## Offset of a clause's literal

For $n_1, g \in \mathbb{N}$, the offset of a clause kind of
the accept generator is its index: $u$ for the code clause $u < n_1$ and $x$ for the cell clause
$x < g$. It is the distance of the clause's single literal from its base counter.

Formalized by `Cslib.Complexity.CookLevin.Accept.AK.off`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#off).

## Polarity of an accept clause's literal

Fix naturals $n_1$ and $g$, and let $a$ and $e$
be naturals. The polarity of the code clause of $u < n_1$ is true exactly when $u = a$, and the
polarity of the cell clause of $x < g$ is true exactly when $x = e$.

Formalized by `Cslib.Complexity.CookLevin.Accept.AK.sg`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#sg).

## Precomputation stages of the accept generator

Write $A$, $K$ and $g$ for the
label/state block size, the number of stacks and the number of symbol codes of the generator's
layout, and $k_1$ for the index of the stack whose top cell it checks. A precomputation stage is
one of eight plain stages or one of five multiplication stages, each of which carries a stage $s$
of the multiplication routine. Named by the step the generator takes there, in the order it runs
them, they are: push $g$ units on $\mathsf{Gc}$; multiply into $\mathsf{HG}$ at $s$; push $A$
units on $\mathsf{Wc}$; push $K$ units on $\mathsf{Kc}$; multiply into $\mathsf{Wc}$ at $s$;
multiply into $\mathsf{TW}$ at $s$; increment $\mathsf{Tn}$; multiply into $\mathsf{Vc}$ at $s$;
drain $\mathsf{TW}$ onto both $\mathsf{CB}$ and $\mathsf{tmp}$; drain $\mathsf{tmp}$ back onto
$\mathsf{TW}$; push $A$ units on $\mathsf{CB}$; push $k_1$ units on $\mathsf{K1}$; multiply into
$\mathsf{CB}$ at $s$.

Formalized by `Cslib.Complexity.CookLevin.Accept.PS`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#ps).

## Stages of the accept generator's literal routine

The stages of the accept generator's
routine emitting a clause's literal are $\mathrm{cp1}$, $\mathrm{cp2}$, $\mathrm{eo}$,
$\mathrm{dec}$, $\mathrm{cmp}$, $r(o)$ and $r_B(o)$ for each ordering $o \in \{<, =, >\}$,
$\mathrm{emL}$, $\mathrm{bad}$, $\mathrm{slot}$ and $\mathrm{dq}$. They form a finite type with
decidable equality.

Formalized by `Cslib.Complexity.CookLevin.Accept.LS`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#ls).

## Labels of the accept generator

For $n_1, g \in \mathbb{N}$, a label is one of: a
precomputation stage; $\mathrm{e00}(c)$, $\mathrm{cv1}(c)$, $\mathrm{cv2}(c)$ or
$\mathrm{fin}(c)$ for a clause kind $c$ (a code clause $u < n_1$ or a cell clause $x < g$);
$\mathrm{lit}(c, s)$ for a clause kind $c$ and a stage $s$ of the literal routine; or the halting
label $\mathrm{done}$. The labels form a finite type with decidable equality.

Formalized by `Cslib.Complexity.CookLevin.Accept.GL`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#gl).

## Entry label of an accept code clause

For a generator with $n_1$ code clauses and $g$ cell
clauses and $u \in \mathbb{N}$, the code-chain label at $u$ is the entry label of code clause $u$
when $u < n_1$, and the halting label $\mathrm{done}$ when $u \ge n_1$.

Formalized by `Cslib.Complexity.CookLevin.Accept.GL.codeFrom`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#code-from).

## Start of the accept code chain

For a generator with $n_1$ code clauses, the code chain
starts at the entry label of code clause $n_1 - 1$ (the last one, as clauses are emitted last
first), or at the halting label $\mathrm{done}$ when $n_1 = 0$.

Formalized by `Cslib.Complexity.CookLevin.Accept.GL.codeStart`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#code-start).

## Entry label of an accept cell clause

For a generator with $n_1$ code clauses and $g$ cell
clauses and $x \in \mathbb{N}$, the cell-chain label at $x$ is the entry label of cell clause $x$
when $x < g$, and the start of the code chain when $x \ge g$.

Formalized by `Cslib.Complexity.CookLevin.Accept.GL.cellFrom`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#cell-from).

## First clause label of the accept generator

Fix naturals $n_1$ and $g$, the numbers
of code clauses and of cell clauses. Clauses are emitted last first, so the label at which clause
emission starts is the start label of the cell clause of $g - 1$ when $g > 0$. When $g = 0$ it is
the start label of the code clause of $n_1 - 1$ if $n_1 > 0$, and the final label if $n_1 = 0$.

Formalized by `Cslib.Complexity.CookLevin.Accept.GL.start`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#start).

## Next label after a clause of the accept generator

Let $n_1, g \in \mathbb{N}$; clauses are
emitted last first. After the code clause $u < n_1$ the generator goes to the halting label
$\mathrm{done}$ if $u = 0$, and otherwise to the first label $\mathrm{e00}$ of code clause
$u - 1$. After the cell clause $x < g$ it goes, if $x = 0$, to the start of the code chain (the
first label of code clause $n_1 - 1$, or $\mathrm{done}$ if $n_1 = 0$), and otherwise to the
first label of cell clause $x - 1$.

Formalized by `Cslib.Complexity.CookLevin.Accept.GL.nextC`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#next-c).

## Literal routine of the accept generator

Fix a layout $L$ with $g$ symbol codes and
parameters $n_1$, $\mathrm{ac}$, $\mathrm{ea}$, and a clause kind $c$ with base counter $b(c)$,
offset $\mathrm{off}(c)$ and polarity $\sigma(c)$. The literal routine of $c$ gives the
generator's statement at each label $\mathrm{lit}(c, s)$; below, a stage $s$ stands for the label
$\mathrm{lit}(c, s)$, and moving a counter onto targets means popping it until it is empty and
pushing one unit onto every target for each unit popped. At $\mathrm{cp1}$ it moves $b(c)$ onto
$Q$ and $\mathrm{tmp}$, then goes to $\mathrm{cp2}$. At $\mathrm{cp2}$ it moves $\mathrm{tmp}$
onto $b(c)$, then goes to $\mathrm{eo}$. At $\mathrm{eo}$ it pushes $\mathrm{off}(c)$ units onto
$Q$ and goes to $\mathrm{dec}$. At $\mathrm{dec}$ it pops $P$ and goes to $\mathrm{bad}$ if $P$
was empty, else to $\mathrm{cmp}$. At $\mathrm{cmp}$ it pops one unit from each nonempty one of
$P$ and $Q$, pushing a unit onto $c_1$ for $P$ and onto $c_2$ for $Q$; it repeats
$\mathrm{cmp}$ if both were nonempty, and otherwise goes to $r(o)$, where the ordering $o$ is
$<$ if only $Q$ was nonempty, $=$ if both were empty, and $>$ if only $P$ was nonempty. At
$r(o)$ it moves $c_1$ onto $P$, then goes to $r_B(o)$. At $r_B(o)$ it moves $c_2$ onto $Q$,
then goes to $\mathrm{slot}$ if $o$ is $=$ and to $\mathrm{emL}$ otherwise. At $\mathrm{emL}$ it
prepends the bits false, true to the output and goes to $\mathrm{dec}$. At $\mathrm{bad}$ it
halts. At $\mathrm{slot}$ it prepends the bits true, $\lnot\sigma(c)$ to the output and goes to
$\mathrm{dq}$. At $\mathrm{dq}$ it empties $Q$, then goes to $\mathrm{fin}(c)$.

Formalized by `Cslib.Complexity.CookLevin.Accept.litP`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#lit-p).

## Generator machine for the accept family

Fix a layout $L$ with label/state block size
$A$, $K$ stacks and $g$ symbol codes, and naturals $n_1$, $a$, $k_1$, $e$. The generator is a
multi-stack machine with a Boolean output stack, the unit counters of the generator, and a
Boolean internal state. Its precomputation pushes $g$ units on $\mathsf{Gc}$, adds
$\mathsf{Hs} \cdot \mathsf{Gc}$ to $\mathsf{HG}$, pushes $A$ units on $\mathsf{Wc}$, pushes $K$
units on $\mathsf{Kc}$, adds $\mathsf{Kc} \cdot \mathsf{HG}$ to $\mathsf{Wc}$, adds
$\mathsf{Tn} \cdot \mathsf{Wc}$ to $\mathsf{TW}$, pushes one unit on $\mathsf{Tn}$, adds
$\mathsf{Tn} \cdot \mathsf{Wc}$ to $\mathsf{Vc}$, drains $\mathsf{TW}$ onto both $\mathsf{CB}$
and $\mathsf{tmp}$ and then $\mathsf{tmp}$ back onto $\mathsf{TW}$, pushes $A$ units on
$\mathsf{CB}$, pushes $k_1$ units on $\mathsf{K1}$, adds $\mathsf{K1} \cdot \mathsf{HG}$ to
$\mathsf{CB}$, and goes to the first clause label; each multiplication uses $\mathsf{md}$ as
its index counter and $\mathsf{tmp}$ as scratch. For each clause $c$ (a code clause of $u < n_1$
or a cell clause of $x < g$) it prepends $[\mathrm{false}, \mathrm{false}]$ to the output,
drains $\mathsf{Vc}$ onto both $\mathsf{P}$ and $\mathsf{tmp}$ and then $\mathsf{tmp}$ back onto
$\mathsf{Vc}$, runs the literal routine of $c$ with polarity parameters $a$ and $e$, drains
$\mathsf{P}$ while prepending $[\mathrm{false}, \mathrm{true}]$ to the output once per unit, and
goes to the label after $c$. At its final label it halts.

It is meant to be started with $T$ on $\mathsf{Tn}$, $H$ on $\mathsf{Hs}$ and every other
counter empty.

Formalized by `Cslib.Complexity.CookLevin.Accept.prog`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#prog).

## The accept generator as a finite multi-stack machine

For a layout $L$ with $g$ symbol
codes and natural numbers $n_1, a, k_1, e$, this is the finite multi-stack Turing machine whose
stacks are an output stack of bits and one unary counter for each of the generator's sixteen
counter names, whose input stack is the counter $T_n$ and output stack the bit stack, whose labels
are the generator's labels for $n_1$ code clauses and $g$ cell clauses with start label the first
precomputation stage, whose internal states are booleans with initial state false, and whose
transition function is the accept generator for $L$, $n_1$, $a$, $k_1$, $e$.

It serves only to check that the generator meets the finiteness conditions of a finite machine.

Formalized by `Cslib.Complexity.CookLevin.Accept.accTM`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#acc-tm).

## Empty scratch counters of the accept generator

An assignment $F$ of a natural number to
each counter of the generator satisfies this predicate when $F$ is zero on the scratch counters
$\mathsf{Q}$, $\mathsf{tmp}$, $\mathsf{md}$, $\mathsf{c1}$ and $\mathsf{c2}$.

The generator keeps these counters empty whenever a clause starts.

Formalized by `Cslib.Complexity.CookLevin.Accept.Rest`, a structure declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#rest).

## Run of the literal routine of the accept generator

Let $c$ be a clause kind with base
counter $b(c)$, offset $\mathrm{off}(c)$ and polarity $\sigma(c)$, and let $F$ assign values to
the counters of the accept generator (for layout $L$ and parameters $n_1$, $\mathrm{ac}$, $k_1$,
$\mathrm{ea}$) such that the scratch counters $Q$, $\mathrm{tmp}$, $\mathrm{md}$, $c_1$, $c_2$
are $0$. Let $q, m \in \mathbb{N}$ with $q = F(b(c)) + \mathrm{off}(c)$ and
$F(P) = q + m + 1$. Then for every output word $o$ and every Boolean state $v$, the generator
runs in at most $m(3q + 6) + 2F(b(c)) + 4q + 9$ steps from the label
$\mathrm{lit}(c, \mathrm{cp1})$, with state $v$, counters $F$ and output $o$, to the label
$\mathrm{fin}(c)$, with state false, the counters $F$ except that $P$ holds $q$, and output
$s\,z\,o$. Here $s$ is the two bits true, $\lnot\sigma(c)$ (the encoding of a slot holding a
literal of polarity $\sigma(c)$), and $z$ is $m$ copies of the two bits false, true (the
encoding of $m$ empty slots).

Formalized by `Cslib.Complexity.CookLevin.Accept.lit_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#lit-run).

## Step bound for one accept clause

For $V \in \mathbb{N}$, the step budget for one clause of
the accept generator is $B(V) = V(3V + 6) + 10V + 13$.

Formalized by `Cslib.Complexity.CookLevin.Accept.clauseB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#clause-b).

## One clause of the accept generator

Let $L$ be a layout with $g$ symbol codes, let
$n_1, a, k_1, e, V \in \mathbb{N}$, and let $c$ be a clause kind of the accept generator (a code
clause $u < n_1$ or a cell clause $x < g$) with base counter $b(c)$, offset $\mathrm{off}(c)$ and
polarity $\sigma(c)$ for $a$ and $e$. Let $F$ be counter values of the generator whose scratch
counters $\mathsf{Q}$, $\mathsf{tmp}$, $\mathsf{md}$, $\mathsf{c1}$, $\mathsf{c2}$ are $0$, with
$F(\mathsf{Vc}) = V$, $F(\mathsf{P}) = 0$ and $p = F(b(c)) + \mathrm{off}(c) < V$. Then for every
output word $o$ and every Boolean state $v$, the accept generator for $L$, $n_1$, $a$, $k_1$, $e$
runs in at most $V(3V + 6) + 10V + 13$ steps from the label $\mathrm{e00}(c)$, with state $v$,
counters $F$ and output $o$, to the label after clause $c$, with state false, the same counters
$F$, and output the encoding of the dense clause over $V$ variables whose only literal is the
variable $p$ with polarity $\sigma(c)$, followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.Accept.clause_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#clause-run).

## Run of the code-clause chain of the accept generator

Let $F$ assign values to the
counters of the accept generator (for layout $L$ and parameters $n_1$, $\mathrm{ac}$, $k_1$,
$\mathrm{ea}$) such that the scratch counters $Q$, $\mathrm{tmp}$, $\mathrm{md}$, $c_1$, $c_2$
are $0$, $F(\mathrm{Vc}) = V$, $F(P) = 0$ and $F(\mathrm{TW}) + n_1 \le V$. Then for every
$u < n_1$, every output word $o$ and every Boolean state $v$, the generator runs in at most
$(u + 1)(V(3V + 6) + 10V + 13)$ steps from the first label of code clause $u$, with state $v$,
counters $F$ and output $o$, to the halting label $\mathrm{done}$, with state false, counters $F$
and output $w_0 w_1 \cdots w_u\, o$. Here $w_i$ is the encoding of the dense clause over $V$
variables whose only literal is variable $F(\mathrm{TW}) + i$, positive if and only if
$i = \mathrm{ac}$.

Formalized by `Cslib.Complexity.CookLevin.Accept.codes_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#codes-run).

## Run of the accept cell chain

Let $L$ be a layout with $g$ symbol codes, let
$n_1, a_c, k_1, e_a \in \mathbb{N}$ be the parameters of the generator, and let $F$ give a value
to every counter of the generator such that the scratch counters $\mathsf{Q}$, $\mathsf{tmp}$,
$\mathsf{md}$, $\mathsf{c1}$, $\mathsf{c2}$ are $0$, $F(\mathsf{Vc}) = V$, $F(\mathsf{P}) = 0$,
$F(\mathsf{TW}) + n_1 \le V$ and $F(\mathsf{CB}) + g \le V$. Write
$B(V) = V(3V + 6) + 10V + 13$ for the one-clause step bound. Then for every $x < g$, every
output stack $o$ and every state bit $v$, the generator started at the entry label of cell
clause $x$ with state $v$, counters $F$ and output $o$ reaches the halting label $\mathrm{done}$
within $(x + 1)B(V) + n_1 B(V)$ steps, with state false, counters $F$, and output consisting of
the encodings of the dense clauses over $V$ variables whose single literal is at
$F(\mathsf{TW}) + u$, positive exactly when $u = a_c$, for $u = 0, \dots, n_1 - 1$, then of
those whose single literal is at $F(\mathsf{CB}) + y$, positive exactly when $y = e_a$, for
$y = 0, \dots, x$, then $o$.

Formalized by `Cslib.Complexity.CookLevin.Accept.cells_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#cells-run).

## Initial counters of the accept generator

For $T, H \in \mathbb{N}$, the initial counter
values are $T$ on the counter $\mathrm{Tn}$, $H$ on the counter $\mathrm{Hs}$, and $0$ on every
other counter.

Formalized by `Cslib.Complexity.CookLevin.Accept.initF`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#init-f).

## Counters after the precomputation of the accept generator

For a layout $L$ with $A$
label/state variables per row, $K$ stacks and $g$ symbol codes, and for $k_1, T, H \in \mathbb{N}$,
let $W = A + KHg$ be the row width. The counter values after the precomputation are $T + 1$ on
$\mathrm{Tn}$, $H$ on $\mathrm{Hs}$, $g$ on $\mathrm{Gc}$, $Hg$ on $\mathrm{HG}$, $W$ on
$\mathrm{Wc}$, $K$ on $\mathrm{Kc}$, $k_1$ on $\mathrm{K1}$, $(T + 1)W$ on $\mathrm{Vc}$, $TW$ on
$\mathrm{TW}$, $TW + A + k_1Hg$ on $\mathrm{CB}$ (the index of the cell variable of stack $k_1$,
depth $0$ and symbol code $0$ at time $T$), and $0$ on every other counter.

Formalized by `Cslib.Complexity.CookLevin.Accept.preF`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#pre-f).

## Cost of the precomputation of the accept generator

For a layout $L$ with $A$
label/state variables per row, $K$ stacks and $g$ symbol codes, and for $k_1, T, H \in \mathbb{N}$,
let $W = A + KHg$ be the row width. The step budget of the precomputation is
$3 + (H(2g + 3) + H + 2) + (K(2Hg + 3) + K + 2) + (T(2W + 3) + T + 2) + 1 +
((T + 1)(2W + 3) + (T + 1) + 2) + (2TW + 2) + 2 + (k_1(2Hg + 3) + k_1 + 2)$.

Formalized by `Cslib.Complexity.CookLevin.Accept.preB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#pre-b).

## Explicit time bound of the accept generator

For a layout $L$ with label block size $A$,
$K$ stacks and $g$ symbol codes, and natural numbers $n_1$, $k_1$, $T$, $H$, let
$W = A + K H g$ and $V = (T + 1) W$ (the number of variables). The bound is $P + (g + n_1)\,C$,
where $C = V(3V + 6) + 10V + 13$ is the cost of one clause and the precomputation cost is
$P = 3 + (H(2g + 3) + H + 2) + (K(2Hg + 3) + K + 2) + (T(2W + 3) + T + 2) + 1 +
((T + 1)(2W + 3) + (T + 1) + 2) + (2TW + 2) + 2 + (k_1(2Hg + 3) + k_1 + 2)$.

It is at most $314\,(A + K + g + n_1 + k_1 + 1)^5\,(T + H + 1)^4$.

Formalized by `Cslib.Complexity.CookLevin.Accept.accBound`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#acc-bound).

## Run of the accept generator's precomputation

Fix a layout $L$ with label/state block
size $A$, $K$ stacks and $g$ symbol codes, and naturals $n_1$, $a$, $k_1$, $e$. For all
$T, H \in \mathbb{N}$ and every list $o$ of Booleans, write $W = A + K H g$ for the row width.
The accept generator, started at its first precomputation label with internal state false,
output $o$, $T$ units on counter $\mathsf{Tn}$, $H$ units on $\mathsf{Hs}$ and every other
counter empty, reaches in at most $\mathrm{preB}(L, k_1, T, H)$ steps the first clause label
with internal state false, output still $o$, and counters $\mathsf{Tn} = T + 1$,
$\mathsf{Hs} = H$, $\mathsf{Gc} = g$, $\mathsf{HG} = H g$, $\mathsf{Wc} = W$, $\mathsf{Kc} = K$,
$\mathsf{K1} = k_1$, $\mathsf{Vc} = (T + 1) W$, $\mathsf{TW} = T W$,
$\mathsf{CB} = T W + A + k_1 H g$, and every other counter empty.

Formalized by `Cslib.Complexity.CookLevin.Accept.pre_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 442](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L442). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#pre-run).

## Correctness of the accept generator, with its explicit time bound

Let $L$ be a layout
with label block size $A$ and $K$ stacks, and let $n_1, a, k_1, e, T, H$ be natural numbers with
$n_1 \le A$, $k_1 < K$ and $H > 0$. Start the accept generator for $L$, $n_1$, $a$, $k_1$, $e$ at
its start label, with internal state false, $T$ and $H$ in unary on its counters $T_n$ and $H_s$,
all other counters empty and an arbitrary bit list $o$ on its output stack. Within a number of
steps at most the explicit time bound for $L$, $n_1$, $k_1$, $T$, $H$, it reaches the label done,
with some internal state, and its output stack then holds the binary encoding of the accept family
of $L$ for $n_1$, $a$, $k_1$, $e$ at $T$, $H$ followed by $o$.

The hypotheses say that the code block fits in the label block, that $k_1$ is a stack, and that
there is a top cell.

Formalized by `Cslib.Complexity.CookLevin.Accept.acc_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 486](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L486). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#acc-run).

## The accept generator's time bound on the uniform layout

For all natural numbers $k \ge 1$
and $y \ge 1$, the explicit time bound of the accept generator for the layout with all four
constants equal to $k$, with $n_1 = k_1 = k$ and $T = H = y$, is at most $314\,k^5 y^4$.

Every monomial of the bound is at most $k^5 y^4$, and the coefficients sum to $314$, the value of
the bound at $k = y = 1$.

Formalized by `Cslib.Complexity.CookLevin.Accept.accBound_uni`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 534](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L534). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#acc-bound-uni).

## Constant of the accept generator's time bound

For a layout $L$ with label block size
$A$, $K$ stacks and $g$ symbol codes, and natural numbers $n_1$, $k_1$, the constant is
$314\,(A + K + g + n_1 + k_1 + 1)^5$.

Formalized by `Cslib.Complexity.CookLevin.Accept.accC`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 575](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L575). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#acc-c).

## Polynomial time bound of the accept generator

Let $L$ be a layout with label block size
$A$, $K$ stacks and $g$ symbol codes, let $n_1, a, k_1, e, T, H$ be natural numbers with
$n_1 \le A$, $k_1 < K$ and $H > 0$, and let $c = 314\,(A + K + g + n_1 + k_1 + 1)^5$. Start the
accept generator for $L$, $n_1$, $a$, $k_1$, $e$ at its start label, with internal state false,
$T$ and $H$ in unary on its counters $T_n$ and $H_s$, all other counters empty and an arbitrary
bit list $o$ on its output stack. Within at most $c\,(T + H + 1)^4$ steps it reaches the label
done, with some internal state, and its output stack then holds the binary encoding of the accept
family of $L$ for $n_1$, $a$, $k_1$, $e$ at $T$, $H$ followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.Accept.acc_time`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 590](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L590). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#acc-time).

## The concrete accept family is a layout-level accept family

Let $M$ be a finite
multi-stack Turing machine with encoding $E$, let $\mathit{acc}$ be a symbol of the output stack
of $M$, and let $T$, $H$ be natural numbers. The accept family of $E$ for $\mathit{acc}$ at $T$,
$H$ equals, by definition, the accept family of the layout of $E$ at $T$, $H$ with parameters
$n_1 = A_0$, the number of (label, state) codes of $E$; $a$, the (label, state) code of the
halted configuration (no label, initial state); $k_1$, the number $E$ gives the output stack; and
$e$, the code of $\mathit{acc}$.

Formalized by `Cslib.Complexity.CookLevin.Accept.accFamily_eq`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 608](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L608). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#acc-family-eq).

## Time bound of the accept generator for a concrete machine

Let $M$ be a finite
multi-stack Turing machine with encoding $E$, let $\mathit{acc}$ be a symbol of the output stack
of $M$, and let $T$, $H$ be natural numbers with $H > 0$. Let $L$ be the layout of $E$, with
label block size $A$, $K$ stacks and $g$ symbol codes, let $A_0$ be the number of (label, state)
codes of $E$, let $k_1$ be the number $E$ gives the output stack, and let
$c = 314\,(A + K + g + A_0 + k_1 + 1)^5$. Start the accept generator for $L$, $A_0$, the code of
the halted configuration, $k_1$ and the code of $\mathit{acc}$ at its start label, with internal
state false, $T$ and $H$ in unary on its counters $T_n$ and $H_s$, all other counters empty and
an arbitrary bit list $o$ on its output stack. Within at most $c\,(T + H + 1)^4$ steps it reaches
the label done, with some internal state, and its output stack then holds the binary encoding of
the accept family of $E$ for $\mathit{acc}$ at $T$, $H$ followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.Accept.acc_gen_time`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Accept.lean, line 613](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Accept.lean#L613). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html#acc-gen-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cook-Levin: generator machine for the accept family](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-accept-fami)
