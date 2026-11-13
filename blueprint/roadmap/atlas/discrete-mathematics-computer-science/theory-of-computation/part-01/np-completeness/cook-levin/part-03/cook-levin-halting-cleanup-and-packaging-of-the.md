---
declaration: section
origin: cited
lean: Cslib.Complexity.CookLevin.Package.xfer_drain, Cslib.Complexity.CookLevin.Package.drainS, Cslib.Complexity.CookLevin.Package.drainB, Cslib.Complexity.CookLevin.Package.drain_run, Cslib.Complexity.CookLevin.Package.DL, Cslib.Complexity.CookLevin.Package.dlab, Cslib.Complexity.CookLevin.Package.idE, Cslib.Complexity.CookLevin.Package.dks
statement: formalized
proof: formalized
---

# Cook-Levin: halting cleanup and packaging of the reduction machine

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html).

## A generic drain phase

## Draining a stack with the transfer loop

Let $M$ be a TM2 machine whose state type
carries a flag bit, and suppose that the statement of $M$ at label $\ell$ is the transfer loop
that pops stack $k$ with no target stacks, returning to $\ell$ while the pop succeeds and going
to label $\ell'$ once stack $k$ is empty. Then for every state $v$ and every stack assignment
$S$, writing $S_k$ for the contents of stack $k$ under $S$ and $|S_k|$ for its length, in
exactly $|S_k| + 1$ steps the machine goes from label $\ell$ with state $v$ and stacks $S$ to
label $\ell'$ with the state that stores the flag bit false and the stacks of $S$ with stack
$k$ replaced by the empty list, all other stacks unchanged.

Formalized by `Cslib.Complexity.CookLevin.Package.xfer_drain`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#xfer-drain).

## The drain program

Given a list $k_0, \dots, k_{m-1}$ of stacks, a type $\Lambda$ of
labels and labels $\lambda : \mathbb{N} \to \Lambda$, stage $i$ of the drain program is as
follows. For $i < m$ it pops stack $k_i$, recording in the state whether a symbol was popped, and
jumps to $\lambda(i)$ if one was and to $\lambda(i + 1)$ if the stack was empty; repeated, this
empties $k_i$. For $i \ge m$ it sets the state to store the flag bit false and halts.

Formalized by `Cslib.Complexity.CookLevin.Package.drainS`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#drain-s).

## Drain step count

For a list $k_1, \dots, k_m$ of stacks and contents $S$ assigning a
list $S_k$ to each stack $k$, the drain step count is $1 + \sum_{i=1}^{m} (|S_{k_i}| + 1)$.

Formalized by `Cslib.Complexity.CookLevin.Package.drainB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#drain-b).

## The drain

Let $M$ be a multi-stack machine program with labels in a type $\Lambda$, let
$k_0, \dots, k_{m-1}$ be a list of distinct stacks, and let $\lambda : \mathbb{N} \to \Lambda$ be
labels such that for every $i \le m$ the instruction of $M$ at $\lambda(i)$ is stage $i$ of the
drain program for this list and these labels. Then for every state $v$ and stack contents $S$,
the machine runs in exactly $1 + \sum_{i < m} (|S_{k_i}| + 1)$ steps from label $\lambda(0)$,
state $v$ and contents $S$ to the halted configuration whose state stores the flag bit false and
whose contents are empty on each $k_i$ and equal to $S$ on every other stack.

Formalized by `Cslib.Complexity.CookLevin.Package.drain_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#drain-run).

## Labels of the composed machine

For a type $\Lambda$ of labels and $n \in \mathbb{N}$, a
label of the composed machine is either a label $l \in \Lambda$ of the original machine or a
drain stage $i \in \{0, \dots, n\}$.

Formalized by `Cslib.Complexity.CookLevin.Package.DL`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#dl).

## Drain-stage label

For $n, j \in \mathbb{N}$, the label of the composed machine with
drain stages $0, \dots, n$ that names drain stage $\min(j, n)$.

Formalized by `Cslib.Complexity.CookLevin.Package.dlab`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#dlab).

## The identity stack embedding

For a family of stack alphabets $\Gamma$ indexed by $K$,
the identity stack embedding of $\Gamma$ into itself sends every stack to itself and identifies
every alphabet with itself by the identity bijection: a pure relabelling.

Formalized by `Cslib.Complexity.CookLevin.Package.idE`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#id-e).

## Stacks to drain

The list of all stacks of the full machine other than its output
stack, each appearing exactly once, in an unspecified order. These are the stacks that the drain
empties before the composed machine halts.

Formalized by `Cslib.Complexity.CookLevin.Package.dks`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#dks).

## Only the output stack survives the drain

For any alphabets and any assignment $T$ of
contents to the stacks of the full machine, the contents that are empty on every stack to drain
and agree with $T$ elsewhere are the contents that agree with $T$ on the output stack and are
empty on every other stack.

Formalized by `Cslib.Complexity.CookLevin.Package.drained`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#drained).

## The composed program

Let $g, r \in \mathbb{N}$, let $P$ be a program with labels
$\Lambda$ and Boolean state over the stacks of the full machine with alphabets $F\Gamma_{g,r}$,
and let $\mathit{fin} \in \Lambda$. The composed program has as labels the labels of $P$ and the
drain stages $0, \dots, n$, where $n$ is the number of stacks other than the output stack. At a
label $\ell \ne \mathit{fin}$ it runs $P(\ell)$ with every jump target relabelled; at
$\mathit{fin}$ it jumps to drain stage $0$; at drain stage $i < n$ it empties the $i$-th stack
other than the output stack (in a fixed order) and moves to stage $i + 1$, and at stage $n$ it
sets the state to false and halts.

Formalized by `Cslib.Complexity.CookLevin.Package.gprog`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#gprog).

## Running a program, then the drain

Let $g, r \in \mathbb{N}$, let $P$ be a program with
labels $\Lambda$ and Boolean state over the stacks of the full machine with alphabets
$F\Gamma_{g,r}$, and let $\mathit{fin}$ be a label with $P(\mathit{fin}) = \mathrm{halt}$.
Suppose $P$ goes in at most $B$ steps from the configuration with label $\ell$, state $v$ and
stacks $S$ to the configuration with label $\mathit{fin}$, state $v'$ and stacks $T$. Then the
composed program of $P$ and $\mathit{fin}$ goes in at most $B + 1 + d(T)$ steps from label $\ell$
(as a label of the composed program), state $v$ and stacks $S$ to the halted configuration with
state false in which every stack other than the output stack is empty and the output stack is
that of $T$. Here $d(T)$, the step count of the drain, is $1$ plus the sum of $|T_q| + 1$ over
the stacks $q$ other than the output stack.

Formalized by `Cslib.Complexity.CookLevin.Package.g_run_gen`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#g-run-gen).

## Step bound for draining bounded stacks

Let $g, r, h \in \mathbb{N}$ and let $T$ assign
to every stack $k$ of the full machine (with alphabets $\Gamma_{g,r}$) a list $T_k$ of length at
most $h$. Let $L$ be the number of stacks other than the output stack. Then the drain step count
$1 + \sum_k (|T_k| + 1)$, summed over the stacks $k$ other than the output stack, is at most
$L(h + 1) + 1$.

Formalized by `Cslib.Complexity.CookLevin.Package.drainB_le`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#drain-b-le).

## The reduction machine

Fix $r \in \mathbb{N}$, a finite TM2 machine $M$ with an encoding
$E$, a list $Y$ of input symbols of $M$, an output symbol $a$, a map $\iota$ from
$\{0, \dots, r-1\}$ to input symbols, an input symbol $\mathit{sep}$, a polynomial $k$ with
coefficients in $\mathbb{N}$ and $c, e \in \mathbb{N}$. The reduction machine is the finite TM2
machine with the stacks and alphabets of the full machine, input on the raw-input stack and
output on the output stack; its labels are those of the full machine together with the drain
stages $0, \dots, n$, where $n$ is the number of stacks other than the output stack; it starts at
the read-loop label with state false; and its program is the composed program of the full
machine's program and its final label: the full machine, followed by the drain.

Formalized by `Cslib.Complexity.CookLevin.Package.gTM`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#g-tm).

## The formula emitted on a raw input

Fix $r \in \mathbb{N}$, a finite TM2 machine $M$ with
an encoding $E$, a list $Y$ of input symbols of $M$, an output symbol $a$, a map $\iota$ from
$\{0, \dots, r-1\}$ to input symbols, an input symbol $\mathit{sep}$, a polynomial $k$ with
coefficients in $\mathbb{N}$ and $c, e \in \mathbb{N}$. For a raw input $s$, a list over
$\{0, \dots, r-1\}$, let $x$ be $s$ with each symbol mapped by $\iota$, followed by
$\mathit{sep}$, let $m = |s| + 1 + k(|s|)$ and $T = (m + c)^e$. The emitted formula for $s$ is
the bit-string encoding of the assembled Cook–Levin formula $\Phi_E(x, Y, a, m, T)$.

Formalized by `Cslib.Complexity.CookLevin.Package.phiOf`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#phi-of).

## Step bound of the composed machine

Fix the verifier data (an encoding $E$ of a stack
machine $M$, a list $Y$ of input symbols, an output symbol $\mathrm{acc}$, a map $\iota$ into
the input alphabet, a separator $\mathrm{sep}$, a polynomial $k$ and $c, e \in \mathbb{N}$) and an
input length $n$. Let $B(n)$ be the step bound of the full machine on inputs of length $n$, let
$D$ be the depth of the full machine (the most push, peek and pop operations on any path of one
of its instructions), and let $L$ be the number of stacks other than the output stack. The step
bound of the composed machine is $B(n) + 1 + (L(n + B(n) D + 1) + 1)$.

Formalized by `Cslib.Complexity.CookLevin.Package.gB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#g-b).

## The reduction machine halts with the emitted formula

Fix $r \in \mathbb{N}$, a finite TM2
machine $M$ with an encoding $E$, a list $Y$ of input symbols of $M$, an output symbol $a$, a map
$\iota$ from $\{0, \dots, r-1\}$ to input symbols, an input symbol $\mathit{sep}$, a polynomial
$k$ with coefficients in $\mathbb{N}$ and $c, e \in \mathbb{N}$. For every raw input $s$, a list
over $\{0, \dots, r-1\}$, the program of the reduction machine goes in at most $g_B(|s|)$ steps
from the initial configuration on input $s$ to the halting configuration with output the emitted
formula for $s$ (no label, the initial state, that formula on the output stack and every other
stack empty), where $g_B$ is the step bound of the composed machine.

No assumption on the verifier data is needed.

Formalized by `Cslib.Complexity.CookLevin.Package.g_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#g-run).

## A bounded halting run certifies the output

Let $M$ be a finite TM2 machine, $l$ a list
over its input alphabet, $l'$ a list over its output alphabet and $B \in \mathbb{N}$. If the
program of $M$ goes in at most $B$ steps from the initial configuration on input $l$ (its start
label, its initial state, $l$ on the input stack and every other stack empty) to the halting
configuration with output $l'$ (no label, the initial state, $l'$ on the output stack and every
other stack empty), then $M$ outputs $l'$ on input $l$ within $B$ steps.

Formalized by `Cslib.Complexity.CookLevin.Package.outputsOfRunLe`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#outputs-of-run-le).

## A bounded halting run certifies the output, up to an equal output

Let $M$ be a finite TM2
machine, $l$ a list over its input alphabet, $l'$ and $l''$ lists over its output alphabet and
$B \in \mathbb{N}$. If the program of $M$ goes in at most $B$ steps from the initial
configuration on input $l$ to the halting configuration with output $l''$, and $l'' = l'$, then
$M$ outputs $l'$ on input $l$ within $B$ steps.

Formalized by `Cslib.Complexity.CookLevin.Package.outputsOfRunLe'`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#outputs-of-run-le-2).

## One polynomial bounds the reduction machine

Fix $r \in \mathbb{N}$, a finite TM2 machine
$M$ with an encoding $E$, a list $Y$ of input symbols of $M$, an output symbol $a$, a map $\iota$
from $\{0, \dots, r-1\}$ to input symbols, an input symbol $\mathit{sep}$, a polynomial $k$ with
coefficients in $\mathbb{N}$ and $c, e \in \mathbb{N}$. There is a polynomial $p$ with
coefficients in $\mathbb{N}$ such that for every raw input $s$, a list over
$\{0, \dots, r-1\}$, the reduction machine on input $s$ outputs the emitted formula for $s$
within $p(|s|)$ steps.

Formalized by `Cslib.Complexity.CookLevin.Package.g_outputs`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#g-outputs).

## The Cook–Levin reduction function

Fix $r \in \mathbb{N}$, a finite TM2 machine $M$ with
an encoding $E$, a list $Y$ of input symbols of $M$, an output symbol $\mathrm{acc}$ of $M$, a
map $\iota$ from $\{0, \dots, r-1\}$ to input symbols of $M$, an input symbol $\mathit{sep}$ of
$M$, a polynomial $k$ with coefficients in $\mathbb{N}$ and $c, e \in \mathbb{N}$. Let
$\mathit{ea}$ encode the elements of a type $\alpha$ as lists over an alphabet $\Sigma$, and let
$\mathit{eqv}$ be a bijection from $\{0, \dots, r-1\}$ to $\Sigma$. The reduction function sends
$u \in \alpha$ to the emitted formula for the raw input $s$ obtained by applying
$\mathit{eqv}^{-1}$ to each symbol of $\mathit{ea}(u)$: the dense encoding of the assembled
Cook–Levin formula $\Phi_E(x, Y, \mathrm{acc}, m, T)$, where $x$ is $s$ with each symbol mapped
by $\iota$, followed by $\mathit{sep}$, $m = |s| + 1 + k(|s|)$ and $T = (m + c)^e$.

Formalized by `Cslib.Complexity.CookLevin.Package.fR`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#f-r).

## The reduction machine as a polynomial-time computation

Fix $r \in \mathbb{N}$, a finite
TM2 machine $M$ with an encoding $E$, a list $Y$ of input symbols of $M$, an output symbol $a$, a
map $\iota$ from $\{0, \dots, r-1\}$ to input symbols, an input symbol $\mathit{sep}$, a
polynomial $k$ with coefficients in $\mathbb{N}$ and $c, e \in \mathbb{N}$. Let $\mathit{ea}$
encode the elements of a type $\alpha$ as lists over an alphabet $\Sigma$, and let $\mathit{eqv}$
be a bijection from $\{0, \dots, r-1\}$ to $\Sigma$. This is a polynomial-time TM2 computation of
the reduction function $f_R$, which sends $u \in \alpha$ to the emitted formula for the raw input
obtained by applying $\mathit{eqv}^{-1}$ to each symbol of $\mathit{ea}(u)$, from the encoding
$\mathit{ea}$ to the identity encoding of bit strings: the machine is the reduction machine, its
input alphabet is identified with $\Sigma$ by $\mathit{eqv}$, its output alphabet with the
Booleans by the identity, and its time bound is a polynomial $p$ with $p(n) = g_B(n)$ for all
$n$, where $g_B$ is the step bound of the composed machine.

Formalized by `Cslib.Complexity.CookLevin.Package.gComp`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Package.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Package.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html#g-comp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cook-Levin: halting cleanup and packaging of the reduction machine](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-halting-cleanup-and-packaging-of-the)
