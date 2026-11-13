---
declaration: section
origin: cited
lean: Cslib.Complexity.CookLevin.InitFamily.IK, Cslib.Complexity.CookLevin.InitFamily.IΓ, Cslib.Complexity.CookLevin.InitFamily.emb, Cslib.Complexity.CookLevin.InitFamily.liftE, Cslib.Complexity.CookLevin.InitFamily.run_lift, Cslib.Complexity.CookLevin.InitFamily.rdS, Cslib.Complexity.CookLevin.InitFamily.read_run, Cslib.Complexity.CookLevin.InitFamily.zB
statement: formalized
proof: formalized
---

# Cook-Levin: generator machine for the initial-row family

74 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html).

## An input stack beside a counter machine

## Stacks of a counter machine with an input stack

For a counter type $C$, the stacks are
those of the counter machine with counters $C$ (its output stack and one counter stack for each
element of $C$), plus one additional input stack.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.IK`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#ik).

## Alphabets of a counter machine with an input stack

For a counter type $C$ and an input
alphabet $G$, each stack of the counter machine with counters $C$ keeps its alphabet there
(Booleans on the output stack, a single symbol on each counter stack), and the input stack has
alphabet $G$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.IΓ`, an abbreviation declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#i).

## Stacks of a counter machine with an extra input stack

Given stack contents $S$ of a
counter machine with counters indexed by $C$ (a list over the alphabet of each of its stacks)
and a list $x$ of symbols from $G$, the combined stack contents give each stack $k$ of the
counter machine the list $S(k)$ and give the extra input stack the list $x$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.emb`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#emb).

## The counter stacks inside the generator's stacks

For a counter index type $C$ and an
input alphabet $G$, the stack embedding of a counter machine over $C$ into the same machine with
one extra input stack over $G$: each stack (the output stack or a counter) goes to its copy among
the extended machine's stacks, with the identity map on its alphabet.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.liftE`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#lift-e).

## Run lifting

Let $M$ be a counter machine (unit counters indexed by $C$ and a Boolean
output stack) and $M'$ a machine on the same stacks plus an input stack over $G$, such that $M'$
embeds $M$ along the inclusion of the counter stacks with the same labels (at every label whose
statement is not the halt statement, $M'$ runs $M$'s statement). If $M$ runs in $n$ steps from
optional label $l$, flag $v$ and stacks $S$ to a label $l'$, flag $v'$ and stacks $S'$, then for
every input list $xs$ over $G$, $M'$ runs in $n$ steps from label $l$, flag $v$, stacks $S$ and
input stack $xs$ to label $l'$, flag $v'$, stacks $S'$ and input stack $xs$.

This is an instance of run embedding.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.run_lift`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#run-lift).

## Read test for one code

Given labels $\mathrm{hit}(i)$ and $\mathrm{miss}(i)$ for the
codes $i < g$, the read test for code $i$ is the statement, on a counter machine's stacks plus an
input stack of codes, that peeks at the top of the input stack and sets the flag to whether it
equals $i$. If it does, the test pops it and goes to $\mathrm{hit}(i)$; otherwise (including when
the input stack is empty) it goes to $\mathrm{miss}(i)$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.rdS`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#rd-s).

## The read chain

Let $M'$ be a machine on a counter machine's stacks plus an input stack of
codes $< g$, with labels $\mathrm{rd}(i)$, $\mathrm{hit}(i)$ and $\mathrm{miss}(i)$ for $i < g$,
such that at $\mathrm{rd}(i)$ it runs the read test for code $i$ with these hit and miss labels,
and $\mathrm{miss}(i) = \mathrm{rd}(i + 1)$ whenever $i + 1 < g$. Then for all counter stacks $S$,
codes $c$, input lists $xs$, all $k$ and codes $i$ with $i + k = c$, and every flag $v$, the
machine $M'$ goes in exactly $k + 1$ steps from label $\mathrm{rd}(i)$, flag $v$, stacks $S$ and
input $c$ followed by $xs$ to label $\mathrm{hit}(c)$, flag true, stacks $S$ and input $xs$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.read_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#read-run).

## Empty-cell variable of the initial row

For a variable layout $L$, a stack number $k_0$, a
number $H$ of tracked depths per stack and a depth $j$, this is the index of the cell variable
of $L$ at time $0$ for stack $k_0$, depth $j$ and symbol code $0$ (the empty cell $\bot$), namely
$A + (k_0 H + j)\,g$, where $A$ is the size of the label/state block of $L$ and $g$ is its number
of symbol codes.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.zB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#z-b).

## Start-code clause of the initial row (I1)

For a layout $L$, a label/state code $i_c$ and
natural numbers $T$ and $H$, the start-code formula consists of a single clause: the dense clause
over the variables of $L$ for $T$ time steps and depth $H$ whose only literal is the positive
literal on the time-$0$ label/state variable with code $i_c$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.iCode`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#i-code).

## Row-0 clauses for the other stacks

Let $L$ be a layout with label block size $A$, $K$
stacks and $g$ symbol codes, let $k_0$ be a stack, and let $T, H$ be natural numbers. This is the
CNF over $V = (T + 1)(A + KHg)$ variables that has, for every stack $k < K$ with $k \ne k_0$ and
every depth $j < H$ (stacks in increasing order, then depths in increasing order), the dense
clause over $V$ variables whose only literal is the positive literal of variable
$A + (kH + j)g$, the row-$0$ variable saying that stack $k$ holds code $0$ (the empty cell) at
depth $j$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.iOther`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#i-other).

## Input clauses of the initial row (I3)

For a layout $L$ with $g$ symbol codes, a stack
number $k_0$, a list $x = (x_0, \dots, x_{\ell - 1})$ of codes below $g$ and natural numbers $T$
and $H$, the input formula has, for each $j = 0, 1, \dots, \ell - 1$ in order, one dense clause
over the variables of $L$ for $T$ time steps and depth $H$, whose only literal is the positive
literal on the time-$0$ cell variable of stack $k_0$ at depth $j$ with code $x_j$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.iIn`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#i-in).

## Certificate clauses of the initial row (I4)

Let $L$ be a layout with label block size
$A$, $K$ stacks and $g$ symbol codes, let $k_0$ be a stack, let $y = (y_1, \dots, y_r)$ be a list
of natural numbers and let $n, m, T, H$ be natural numbers. For a depth $j$ and a code $x$ write
$C_{j,x} = A + (k_0 H + j)g + x$ for the row-$0$ variable saying that stack $k_0$ holds code $x$
at depth $j$. This is the CNF over $V = (T + 1)(A + KHg)$ variables that has, for
$i = 0, 1, \dots, m - n - 1$ in order (no clauses if $m \le n$), the dense clause over $V$
variables whose literals are the positive literals of the variables $C_{n+i,0}$, $C_{n+i,y_1}$,
$\dots$, $C_{n+i,y_r}$: the cell at depth $n + i$ is empty or holds one of the codes in $y$.

In use, $y$ lists the certificate codes, sorted and distinct.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.iCert`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#i-cert).

## Row-0 prefix clauses

Let $L$ be a layout with label block size $A$, $K$ stacks and $g$
symbol codes, let $k_0$ be a stack, let $n, m, T, H$ be natural numbers, and write
$z_j = A + (k_0 H + j)g$ for the row-$0$ variable saying that stack $k_0$ holds code $0$ (the
empty cell) at depth $j$. This is the CNF over $V = (T + 1)(A + KHg)$ variables that has, for
$i = 0, 1, \dots, m - n - 1$ in order (no clauses if $m \le n$), the dense clause over $V$
variables whose literals are the negative literal of variable $z_{n+i}$ and the positive literal
of variable $z_{n+i+1}$: an empty cell at depth $n + i$ forces an empty cell at depth
$n + i + 1$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.iPre`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#i-pre).

## Row-0 tail clauses

Let $L$ be a layout with label block size $A$, $K$ stacks and $g$
symbol codes, let $k_0$ be a stack, let $m, T, H$ be natural numbers, and write
$z_j = A + (k_0 H + j)g$ for the row-$0$ variable saying that stack $k_0$ holds code $0$ (the
empty cell) at depth $j$. This is the CNF over $V = (T + 1)(A + KHg)$ variables that has, for
$i = 0, 1, \dots, H - m - 1$ in order (no clauses if $H \le m$), the dense clause over $V$
variables whose only literal is the positive literal of variable $z_{m+i}$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.iTail`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#i-tail).

## The init family

Let $L$ be a layout, let $i_c$ be a label/state code, let $k_0$ be a
stack, let $y$ be a list of natural numbers, let $x$ be a list of symbol codes of $L$ of length
$\ell$, and let $m, T, H$ be natural numbers. The init family is the CNF formula obtained by
concatenating, in this order: the start-code clause of the initial row for $i_c$, $T$, $H$ (I1);
the row-$0$ clauses for the stacks other than $k_0$ for $T$, $H$ (I2); the input clauses of the
initial row for $k_0$, $x$, $T$, $H$ (I3); the certificate clauses of the initial row for $k_0$,
$y$, $n = \ell$, $m$, $T$, $H$ (I4); the row-$0$ prefix clauses for $k_0$, $n = \ell$, $m$, $T$,
$H$ (I5); and the row-$0$ tail clauses for $k_0$, $m$, $T$, $H$ (I6).

Formalized by `Cslib.Complexity.CookLevin.InitFamily.initFam`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#init-fam).

## Counters of the initial-row generator

The unit-counter stacks of the generator are
indexed by a finite type with 27 distinct elements: Tn, Xn, En, Fn, Gc, Mm, Hs, HG, Wc, Vc, KA,
ZA, Z45, Z6, Z1, Z2, N1, N2, CB, Zr, P, Q, tmp, md, c1, c2 and Id. Equality on it is
decidable.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.CK`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#ck).

## Loop phases of the initial-row generator

The five phase loops of the generator for the
initial-row clauses, in the order the generator runs them (its input loop runs between the
certificate phase and the two stack phases): the tail phase (the row-$0$ cells of the stack $k_0$
holding the input, past the certificate block, are empty), the prefix phase (an empty cell in the
certificate block is followed by an empty cell), the certificate phase (each certificate cell is
empty or holds a certificate code), and two stack phases making every stack other than $k_0$
empty, first the stacks $k > k_0$, then the stacks $k < k_0$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.PH`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#ph).

## Loop-count counter of a phase (initial-row generator)

Let $k_0$ be the index of the
input stack in the tableau layout. For a loop phase $p$, the generator counter whose units count
the remaining iterations of the loop of $p$: Fn for the I6 phase, En for both the I5 and the I4
phase, N2 for the I2 phase over the stacks $k > k_0$, and N1 for the I2 phase over the stacks
$k < k_0$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.PH.cN`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#c-n).

## Base counter of a phase (initial-row generator)

Let $k_0$ be the index of the input
stack in the tableau layout. For a loop phase $p$, the generator counter holding the base of the
loop of $p$, the cell base of its iteration $0$: Z6 for the I6 phase, Z45 for both the I5 and the
I4 phase, Z2 for the I2 phase over the stacks $k > k_0$, and Z1 for the I2 phase over the stacks
$k < k_0$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.PH.cZ`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#c-z).

## Clause kinds of the initial-row generator

For $g, n \in \mathbb{N}$, a clause kind is
either the start-code clause (I1), an input clause (I3) with a symbol code $c < g$, or the clause
of one of the five loop phases $p$. The parameter $n$ only indexes the type. There are finitely
many clause kinds and their equality is decidable.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.CL`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#cl).

## Number of literals of a clause kind

For clause kinds over $g$ codes and $n$ certificate
codes, a clause of the certificate phase has $n + 1$ literals, a clause of the prefix phase has $2$,
and every other clause kind has $1$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.CL.nl`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#nl).

## Literal offsets

Fix numbers $i_c$ and $g'$ and a list $y = (y_1, \dots, y_r)$ of
numbers. The offset from the clause base of literal $l$ in a clause of kind $c$ is $i_c$ for the
start-code clause; $x$ for the input clause with code $x$; for the certificate phase, $y_l$ if
$1 \le l \le r$ and $0$ otherwise; for the prefix phase, $0$ if $l = 0$ and $g'$ otherwise; and $0$
for the other three phases.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.CL.off`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#off).

## Literal signs of an init-family clause kind

For a clause kind $c$ of the init-family
generator and a literal index $l \in \mathbb{N}$, the sign of literal $l$ of $c$ is positive in
every case except one: for the prefix-form phase (clause group I5), literal $0$ is negative and
every literal $l \ne 0$ is positive.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.CL.sg`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#sg).

## Base counter of a clause kind (initial-row generator)

For a clause kind $c$, the
generator counter whose value is added to the literal offsets of $c$ to give the literal
positions: the counter Zr for the start-code clause (I1), and the counter CB for every other
clause kind.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.CL.bc`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#bc).

## Labels of the first precomputation part

The finite type of labels with which the
generator sets the counters $G_c = g$, $M_m = m$, $H_s = H$, $HG = H \cdot g$, $W_c = W$ and
$V_c = V$, where $g$ is the number of symbol codes, $m$ the end of the certificate block, $H$ the
stack height, $W$ the row width and $V$ the number of variables. It consists of thirteen single
labels and three multiplication loops, each with one label per multiplication stage.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.PS1`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#ps1).

## Labels of the second precomputation part

The finite type of labels with which the
generator computes the row-0 cell bases $Z_A, Z_{45}, Z_6, Z_1, Z_2$ and the loop counts
$N_1, N_2$. It consists of sixteen single labels and five multiplication loops, each with one label
per multiplication stage.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.PS2`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#ps2).

## Stages of the literal routine (initial-row generator)

The stages of the generator's
routine that emits one literal of a clause: two stages copying the clause base into a target
counter, a stage adding the literal's offset to the target, a stage decrementing the position
counter, a stage comparing the position with the target, two restore stages for each comparison
outcome (less, equal or greater), a stage emitting one empty slot, a halting error stage, a stage
emitting the literal's slot, and a stage draining the target counter.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.LS`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#ls).

## Labels of the initial-row generator

For natural numbers $g$ and $n$, the labels are: a
label for each stage of the first precomputation part and one for each stage of the second; for
each loop phase $p$, a loop-head label, a counter-reset label, two base-copy labels, a
multiplication label for each multiplication stage and a base-drain label; for the input loop,
a head label, two base-copy labels, a multiplication label for each multiplication stage, a read
test for each code $i < g$ and a base-drain label; an error label; for each clause kind $c$ for
$g$ and $n$, a clause-start label, two labels copying the variable count, a literal label for
each literal index $l < n + 2$ and each literal stage, and a label emitting the leading gap; and
a final label. The label type has decidable equality and is finite.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.GL`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#gl).

## Entry label of a literal routine (initial-row generator)

For a clause kind $c$ and
$l \in \mathbb{N}$, among the generator labels with parameters $g$ and $n$: the first stage of the
routine for literal $l$ of $c$ if $l < n + 2$, and the label $\mathrm{done}$ otherwise (that
case is never used).

Formalized by `Cslib.Complexity.CookLevin.InitFamily.GL.litL`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#lit-l).

## Label after a literal routine (initial-row generator)

Let $g, n \in \mathbb{N}$, let $c$
be a clause kind of the generator with parameters $g$ and $n$, and let $l \in \mathbb{N}$. If
$l = 0$, the label is the final routine of $c$, which emits the leading gap. If $l \ge 1$, it is
the start of the routine for literal $l - 1$ of $c$ when $l - 1 < n + 2$, and the halting label
otherwise. The generator goes here after the routine for literal $l$, and with $l$ the number
of literals of $c$ before its first literal routine, so literals are emitted from the last to
the first.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.GL.after`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#after).

## Label after a phase loop

Write $k_0$ for the stack holding the input. The label the
generator moves to when the loop of phase $p$ finishes: the loop head of the prefix phase after
the tail phase, the loop head of the certificate phase after the prefix phase, the head of the
input loop after the certificate phase, the loop head of the phase for the stacks $k < k_0$ after
the phase for the stacks $k > k_0$, and the first step of the start-code clause after the phase
for the stacks $k < k_0$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.GL.next`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#next).

## Label after a clause

The label the generator moves to after emitting a clause of kind $c$:
the halting label after the start-code clause, the end of the input-loop iteration (which drains
the clause base) after an input clause, and the end of the loop iteration of phase $p$ (which
drains the clause base) after a clause of phase $p$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.GL.nextC`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#next-c).

## The first read test

For $g, n \in \mathbb{N}$, the generator label that tests for input
code $0$ when $g > 0$, and the error label when $g = 0$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.GL.rd0`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#rd0).

## Label after a failed read test

For a code $i < g$, the label reached when the read test
for $i$ fails is the read test for $i + 1$ if $i + 1 < g$, and the halting error label otherwise.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.GL.miss`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#miss).

## Labels of the initial-row generator for a layout

For a layout $L$ and a list $y$ of
certificate codes, the label type of the generator is the type of labels of the initial-row
generator with parameters $g$, the number of symbol codes of $L$, and $n$, the length of $y$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.Lb`, an abbreviation declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#lb).

## The literal routine of the initial-row generator

For a clause kind $c$ and a literal
index $l < n + 2$, where $n$ is the number of certificate codes, the counter program at the
stages of the routine for literal $l$ of $c$. It copies the base counter of $c$ into the counter
$Q$ (restoring the base counter through a scratch counter) and adds the offset of literal $l$ to
$Q$. It then repeats: pop a unit from the counter $P$ (halting if $P$ is empty) and compare $P$
with $Q$, restoring both. If they are equal, it prepends the slot code of the sign of literal $l$
to the output, empties $Q$ and goes to the label before literal $l$: the routine for literal
$l - 1$, or the leading gap of the clause if $l = 0$. Otherwise it prepends the gap code $01$ to
the output and repeats.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.litP`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#lit-p).

## The counter part of the initial-row generator

Let $L$ be a layout with label block size
$A$, $K$ stacks and $g$ symbol codes, let $i_c$ and $k_0$ be natural numbers and let $y$ be a list
of $n$ certificate codes. The counter part assigns to each label of the initial-row generator for
$g$ and $n$ a statement of the counter machine with the generator's counters and a Boolean flag,
as follows. Every pop sets the flag to whether a unit was popped, and pushes leave it unchanged.
Below, to copy $a$ into $b$ is to use two labels, the first moving $a$ unit by unit into both $b$
and the scratch counter tmp and the second moving tmp back into $a$; to multiply $a \cdot b$ into
$c$ is to run the multiplication routine adding $a \cdot b$ to $c$ with loop index md and scratch
tmp; to add $j$ to $a$ is to prepend $j$ units to $a$ in one step; and to drain $a$ is to empty
it one unit per step.

The first precomputation part adds $g$ to Gc; copies Xn into Mm, En into Mm, Mm into Hs and Fn
into Hs; multiplies Hs $\cdot$ Gc into HG; adds $A$ to Wc and $K$ to KA; multiplies KA $\cdot$ HG
into Wc and drains KA; increments Tn; and multiplies Tn $\cdot$ Wc into Vc. The second part adds
$A$ to ZA and $k_0$ to KA, multiplies KA $\cdot$ HG into ZA and drains KA; copies ZA into Z45 and
multiplies Xn $\cdot$ Gc into Z45; copies ZA into Z6 and multiplies Mm $\cdot$ Gc into Z6; adds
$A$ to Z1; copies ZA into Z2 and HG into Z2; adds $k_0$ to KA, multiplies KA $\cdot$ Hs into N1
and drains KA; adds $K - k_0 - 1$ (truncated subtraction) to KA, multiplies KA $\cdot$ Hs into N2,
drains KA and goes to the loop head of the tail phase.

For a loop phase $p$ with loop-count counter $N_p$ and base counter $Z_p$, the loop head pops
$N_p$; if a unit was popped it pushes a unit onto Id and goes to the body, otherwise it goes to
the counter-reset label, which moves Id back into $N_p$ and goes to the label after the loop of
$p$. The body, made of the base-copy and multiplication labels of $p$, copies $Z_p$ into CB,
multiplies $N_p \cdot$ Gc into CB and goes to the clause-start label of the clause of phase $p$;
the base-drain label of $p$ drains CB and goes to the loop head of $p$. The head of the input
loop pops Xn and goes to the loop head of the phase for the stacks $k > k_0$ if Xn was empty;
otherwise its base-copy and multiplication labels copy ZA into CB, multiply Xn $\cdot$ Gc into CB
and go to the first read test, or to the error label if $g = 0$. The base-drain label of the
input loop drains CB and goes to the head of the input loop. The read tests, the error label and
the final label halt.

For a clause kind $c$, the clause-start label prepends $00$ to the output; the two labels copying
the variable count then copy Vc into $P$ and go to the label after the literal routine for $c$ and
$\mathrm{nl}(c)$, the number of literals of $c$; the labels of literal $l$ of $c$ run the literal
routine of $c$ for $l$; and the leading-gap label of $c$ drains $P$, prepending $01$ to the output
for each unit, and then goes to the label after $c$.

The read tests $\mathrm{rd}(i)$ halt here; the generator replaces them by tests on its input
stack.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.prog`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#prog).

## The initial-row generator

Let $L$ be a layout with $g$ symbol codes, let $i_c$ and $k_0$
be natural numbers and let $y$ be a list of certificate codes. The generator assigns to each label
of the initial-row generator for $L$ and $y$ a machine statement with a Boolean flag on the stacks
of the counter machine with the generator's counters plus an input stack of codes below $g$, as
follows. At the read test label $\mathrm{rd}(i)$ for a code $i < g$, it is the read test for code
$i$ that goes on success to the clause-start label of the input clause with code $i$ and on
failure to the label after a failed read test for $i$. At every other label, it is the statement
of the counter part of the generator for $L$, $i_c$, $k_0$, $y$ at that label, translated along
the embedding of the counter stacks into the generator's stacks, with labels unchanged.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.iprog`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#iprog).

## The init generator as a finite multi-stack machine

For a layout $L$ with $g$ symbol
codes, a start code $i_c$, a stack $k_0$ and a code list $Y$, this is the finite multi-stack
Turing machine whose stacks are the generator's counters, its Boolean output stack and an extra
input stack, with the extra stack as input stack and the Boolean stack as output stack; whose
stack alphabets are unit symbols on the counters, bits on the output stack and codes below $g$
on the input stack; whose labels are the generator's labels, starting at the first
precomputation label; whose internal state is a Boolean starting at false; and whose transition
function is the generator for $L, i_c, k_0, Y$.

It records only that the generator is a finite machine.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.initTM`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#init-tm).

## Literals of a clause kind

Given natural numbers $i_c$ and $g'$, a list $y$ of natural
numbers, a base position $B$ and a clause kind $c$, the literal list of $c$ at base $B$ is the
list of the pairs $(B + \mathrm{off}(c, l), \mathrm{sg}(c, l))$ for $l = 0, 1, \dots,
\mathrm{nl}(c) - 1$ in order, where $\mathrm{nl}(c)$ is the number of literals of $c$,
$\mathrm{off}(c, l)$ is the offset of literal $l$ (computed from $i_c$, $g'$ and $y$) and
$\mathrm{sg}(c, l)$ is its sign.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.clits`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#clits).

## Well-formed init-family clause kinds

Fix natural numbers $i_c$ and $g'$ and a list $Y$ of
natural numbers, which determine the offsets of the literals of each clause kind from the base.
A clause kind $c$ is well formed when these offsets are strictly increasing: for every
$l \in \mathbb{N}$ with $l + 1$ less than the number of literals of $c$, the offset of literal $l$
of $c$ is less than the offset of literal $l + 1$ of $c$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.WF`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#wf).

## Boundary before a literal (initial-row generator)

For a bound $V$, a base $B$, a clause
kind $c$ and $l \in \mathbb{N}$, the boundary before literal $l$ is $B + \mathrm{off}_c(l)$, the
position of literal $l$, when $l$ is less than the number of literals of $c$, and $V$ otherwise.
Here $\mathrm{off}_c(l)$ is the offset of literal $l$ of $c$ determined by the start code $ic$,
the symbol count $g'$ and the certificate codes $ycs$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.bnd`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 497](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#bnd).

## Literals of a clause kind in range

Given the start code $i_c$, a code count $g'$, the
certificate codes $y$, a bound $V$, a base $B$ and a clause kind $c$ of the init generator, all
literals of $c$ are in range when $B + \mathrm{off}_c(l) < V$ for every literal index $l$ less
than the number of literals of $c$, where $\mathrm{off}_c(l)$ is the offset of literal $l$ of $c$
determined by $i_c$, $g'$ and $y$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.InR`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 501](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L501). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#in-r).

## Empty scratch counters

An assignment $F$ of natural numbers to the generator's counters
has empty scratch counters when $F(Q) = F(\mathrm{tmp}) = F(\mathrm{md}) = F(c_1) = F(c_2) = 0$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.Rest`, a structure declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#rest).

## Run of one literal routine (initial-row generator)

For a layout and a list of $n$
certificate codes, let $c$ be a clause kind with base counter $b$, let $l < n + 2$ be a literal
index with offset $\mathrm{off}(l)$, and let $F$ be counter values whose scratch counters $Q$,
$\mathrm{tmp}$, $\mathrm{md}$, $c_1$, $c_2$ are $0$. Let $\gamma \in \mathbb{N}$, let
$q = F(b) + \mathrm{off}(l)$ and suppose $F(P) = q + \gamma + 1$. Then for every output $o$ and
flag $v$, the counter program runs in at most $\gamma(3q + 6) + 2F(b) + 4q + 9$ steps from the
first stage of the routine for literal $l$ of $c$, with flag $v$, counters $F$ and output $o$, to
the label before literal $l$ (the routine for literal $l - 1$, or the leading gap if $l = 0$),
with flag false, counters $F$ except $P = q$, and output $s \cdot (01)^{\gamma} \cdot o$, where
$s$ is the slot code of the sign of literal $l$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.lit_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#lit-run).

## Per-literal step cost of the initial-row generator

For $V \in \mathbb{N}$, the
per-literal cost is $6V + 9$.

It bounds the steps the generator spends on one literal apart from the gap loop.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.litE`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 584](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L584). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#lit-e).

## Step bound for one clause (initial-row generator)

For natural numbers $m$ and $V$,

$$\mathrm{clauseB}(m, V) = V(3V + 6) + m \cdot \mathrm{litE}(V) + 3V + 4,$$

where $\mathrm{litE}(V) = 6V + 9$ is the per-literal cost apart from the gap loop.

It bounds the steps the generator takes to emit one clause with at most $m$ literals over $V$
variables.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.clauseB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 587](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L587). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#clause-b).

## Run of the literal routines of a clause (initial-row generator)

Let $c$ be a clause
kind with $k$ literals at base $B$, the $j$-th at position $B + \mathrm{off}(j)$, such that the
offsets are strictly increasing and every position is below $V$. For $l \le k$ let $b_l$ be
$B + \mathrm{off}(l)$ if $l < k$ and $V$ otherwise, let $\lambda_l$ be the list of literals of
$c$ (position and sign) from index $l$ on, and let the label before literal $l$ be the first
stage of the routine for literal $l - 1$, or the leading-gap stage of $c$ if $l = 0$. Write
$E(a, \lambda)$ for the gap encoding of the slots $a, \dots, V - 1$ with literals $\lambda$. Let
$F$ be counter values whose scratch counters $Q$, $\mathrm{tmp}$, $\mathrm{md}$, $c_1$, $c_2$ are
$0$ and whose base counter for $c$ equals $B$, and let $o$ be an output. Then for every $l \le k$
and flag $v$ there is a flag $v'$ such that the counter program runs in at most
$b_l(3V + 6) + l(6V + 9)$ steps from the label before literal $l$, with flag $v$, counters $F$
except $P = b_l$ and output $E(b_l, \lambda_l) \cdot 00 \cdot o$, to the leading-gap stage of
$c$, with flag $v'$, counters $F$ except $P = b_0$ and output $E(b_0, \lambda_0) \cdot 00 \cdot o$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.lits_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 590](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L590). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#lits-run).

## Run of one clause (initial-row generator)

Let $L$ be a layout with $g$ symbol codes, let
$i_c$ and $k_0$ be natural numbers and let $y$ be a list of $n$ certificate codes. Let $c$ be a
clause kind for $g$ and $n$ that is well formed for $i_c$, $g$ and $y$, and let $V, B$ be natural
numbers such that all literals of $c$ at base $B$ (for $i_c$, $g$ and $y$) are in range below $V$.
Let $F$ be counter values of the generator with empty scratch counters such that $F(b) = B$ for
the base counter $b$ of $c$, $F(\mathrm{Vc}) = V$ and $F(P) = 0$. Then for every output $o$ and
flag $v$, the counter part of the generator for $L$, $i_c$, $k_0$, $y$ runs within the step bound
$\mathrm{clauseB}(n + 2, V)$ for one clause from the clause-start label of $c$, with flag $v$,
counters $F$ and output $o$, to the label after $c$, with flag false, counters $F$ and output
$w \cdot o$, where $w$ is the dense encoding of the dense clause over $V$ variables built from the
literal list of $c$ at base $B$ (for $i_c$, $g$ and $y$).

Formalized by `Cslib.Complexity.CookLevin.InitFamily.clause_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 643](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L643). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#clause-run).

## Step bound for one loop iteration (initial-row generator)

For natural numbers
$m, g, N, V$,

$$\mathrm{bodyB}(m,g,N,V) = 2V + 2 + (N(2g+3) + N + 2) + g + 1 + \mathrm{clauseB}(m,V) + V + 1,$$

where $\mathrm{clauseB}(m, V)$ is the step bound for one clause with at most $m$ literals.

It bounds one iteration of any phase loop, and one I3 iteration including its read.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.bodyB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 700](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L700). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#body-b).

## One phase-loop iteration of the initial-row generator

Let $L$ be a layout with $g$
symbol codes, let $ic, k_0 \in \mathbb{N}$, let $ycs$ be a list of $n$ certificate codes, and let
$p$ be a loop phase with base counter $c_Z(p)$ and loop-count counter $c_N(p)$. Let $F$ give the
value of each generator counter, with the scratch counters empty ($\mathrm{Rest}(F)$),
$F(\mathrm{CB}) = F(\mathrm{P}) = 0$, $F(\mathrm{Vc}) = V$, $F(\mathrm{Gc}) = g$, $F(c_Z(p)) = Z$
and $F(c_N(p)) = t$. Suppose $t < N$ and $tg + Z \le V$, the clause kind of $p$ has strictly
increasing literal offsets, and all its literals at base $tg + Z$ lie below $V$. Then for every
output $o$ and flag $v$, the counter program of the generator runs in at most
$\mathrm{bodyB}(n + 2, g, N, V)$ steps from label $b_1(p)$ with flag $v$, counters $F$ and output
$o$ to the loop head of $p$ with flag false, counters $F$ and output
$\mathrm{encodeClause}(\mathrm{denseClause}(V, \mathrm{clits}(tg + Z, p)))$ followed by $o$.
Here $\mathrm{clits}(tg + Z, p)$ are the literals of the clause kind of $p$ at base $tg + Z$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.body_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 704](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L704). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#body-run).

## One phase loop

Fix a layout $L$ with $g$ symbol codes, a start code $i_c$, a stack index
$k_0$ and a list $y$ of $n$ certificate codes, and let $M$ be the counter part of the initial-row
generator for these parameters. Let $p$ be a loop phase with loop counter $N_p$ and base counter
$Z_p$, and let $F$ be counter values with the scratch counters $Q$, $\mathrm{tmp}$, $\mathrm{md}$,
$c_1$, $c_2$ empty, $F(\mathrm{CB}) = F(P) = F(\mathrm{Id}) = 0$, $F(\mathrm{Vc}) = V$,
$F(\mathrm{Gc}) = g$, $F(Z_p) = Z$ and $F(N_p) = N$, where $N \le N_b$. Suppose the literal offsets
of phase $p$ (for $i_c$, $g$ and $y$) are strictly increasing and, for every $t < N$,
$tg + Z \le V$ and every literal of the phase-$p$ clause at base $tg + Z$ has position below $V$.
Then for every output $o$ and flag $v$, $M$ goes in at most $N_b(b + 1) + N_b + 2$ steps from the
loop head of phase $p$ with flag $v$, counters $F$ and output $o$ to the label after the loop of
phase $p$ with flag false, counters $F$ and output $B_0 B_1 \cdots B_{N-1}\, o$. Here $B_t$ is the
encoding of the dense clause over $V$ variables with the literals of the phase-$p$ clause at base
$tg + Z$, and $b$ is the loop-iteration cost bound for $n + 2$ literals, $g$ codes, loop count
$N_b$ and $V$ variables.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.phase_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 737](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L737). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#phase-run).

## Counter part of one I3 iteration

Let $L$ be a layout with $g$ symbol codes. Suppose the
counters $F$ of the init generator's counter part have $Q$, $\mathrm{tmp}$, $\mathrm{md}$, $c_1$,
$c_2$ and $\mathrm{CB}$ equal to $0$, $\mathrm{Gc} = g$, $\mathrm{ZA} = Z$ and
$\mathrm{Xn} = r + 1$. Then for every output $o$ and flag $v$, the counter part, started at the
head of the I3 loop with flag $v$, counters $F$ and output $o$, reaches the first read test (the
halting label if $g = 0$) in at most $1 + (2Z + 2) + (r(2g + 3) + r + 2)$ steps, with flag false,
output $o$, and the counters of $F$ except that $\mathrm{Xn} = r$ and $\mathrm{CB} = rg + Z$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.i3pre_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 763](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L763). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#i3pre-run).

## The I3 loop

Let $L$ be a layout with $g$ symbol codes, consider the init generator for a
start code, a stack $k_0$ and a list of $\ell$ certificate codes, and let
$x = (x_0, \dots, x_{s-1})$ be a list of codes $x_j < g$. Suppose its counters $F$ have $Q$,
$\mathrm{tmp}$, $\mathrm{md}$, $c_1$, $c_2$, $\mathrm{CB}$ and $P$ equal to $0$,
$\mathrm{Vc} = V$, $\mathrm{Gc} = g$ and $\mathrm{ZA} = Z$, that $jg + Z + g \le V$ for every
$j < s$, and that $s \le N_b$. Then for every $r \le s$, every output $o$ and every flag $v$, the
generator, started at the head of the I3 loop with flag $v$, the counters of $F$ except
$\mathrm{Xn} = r$, output $o$, and $x_{r-1}, \dots, x_1, x_0$ on its input stack (top first),
reaches in at most $r\beta + 1$ steps the head of the I2 loop over the stacks above $k_0$, with
flag false, the counters of $F$ except $\mathrm{Xn} = 0$, an empty input stack, and output
$e_0 e_1 \cdots e_{r-1}$ followed by $o$. Here $e_j$ is the encoding of the dense clause over
$V$ variables whose only literal is the positive literal of variable $jg + Z + x_j$, and
$\beta = 3V^2 + 12V + (\ell + 2)(6V + 9) + (2g + 4)N_b + g + 10$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.i3_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 799](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L799). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#i3-run).

## Row-0 cells fit in the variable range

For a layout $L$ with $A$ label/state variables,
$KK$ stacks and $g$ symbol codes, and all $T, H, q \in \mathbb{N}$ with $q < KK \cdot H$, we have
$A + q g + g \le V$, where $V$ is the number of variables of $L$ for time bound $T$ and stack
height $H$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.qpos`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 955](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L955). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#qpos).

## Concatenating consecutive blocks of indices

Let $\varphi$ be a function from the natural
numbers to a type $\alpha$ and let $H$, $s$, $r$ be natural numbers. Concatenating, for
$k = s, s + 1, \dots, s + r - 1$ in order, the lists
$[\varphi(kH), \varphi(kH + 1), \dots, \varphi(kH + H - 1)]$ gives the list
$[\varphi(sH), \varphi(sH + 1), \dots, \varphi(sH + rH - 1)]$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.flat_blocks`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1013](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1013). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#flat-blocks).

## Initial counters of the init generator

For natural numbers $T, n, e, f$, the counters
$\mathrm{Tn}$, $\mathrm{Xn}$, $\mathrm{En}$ and $\mathrm{Fn}$ of the generator hold $T$, $n$, $e$
and $f$ respectively, and every other counter holds $0$.

In use, $n$ is the length of the input code list, $e = m - n$ and $f = H - m$, where $m$ is the
depth at which the certificate block ends and $H$ is the stack height.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.initF`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1066](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1066). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#init-f).

## Counters after the precomputation

For a layout $L$ with $A$ label/state variables, $K$
stacks and $g$ symbol codes, a stack index $k_0$ and numbers $T, n, e, f$, write $H = n + e + f$.
The counter values after the precomputation are $\mathrm{Tn} = T + 1$, $\mathrm{Xn} = n$,
$\mathrm{En} = e$, $\mathrm{Fn} = f$, $\mathrm{Gc} = g$, $\mathrm{Mm} = n + e$, $\mathrm{Hs} = H$,
$\mathrm{HG} = Hg$, $\mathrm{Wc} = A + KHg$ (the row width), $\mathrm{Vc} = (T + 1)(A + KHg)$ (the
number of variables), $\mathrm{ZA} = A + k_0Hg$, $\mathrm{Z45} = A + (k_0H + n)g$,
$\mathrm{Z6} = A + (k_0H + n + e)g$, $\mathrm{Z1} = A$, $\mathrm{Z2} = A + (k_0 + 1)Hg$,
$\mathrm{N1} = k_0H$ and $\mathrm{N2} = (K - k_0 - 1)H$ (truncated subtraction), and $0$ for every
other counter.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.preF`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1074](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1074). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#pre-f).

## Step bound for the precomputation

For a layout $L$ with $A$ label/state variables, $K$
stacks and $g$ symbol codes, and numbers $k_0, q, T, n, e, f$, write $h = n + e + f$. The bound is

$$
1 + (2n + 2) + (2e + 2) + (2(n + e) + 2) + (2f + 2) + (h(2g + 3) + h + 2) + 1 + 1 +
(K(2hg + 3) + K + 2) + (K + 1) + 1 + ((T + 1)(2(Khg + A) + 3) + (T + 1) + 2) + 1 + 1 +
(k_0(2hg + 3) + k_0 + 2) + (k_0 + 1) + (2(k_0 hg + A) + 2) + (n(2g + 3) + n + 2) +
(2(k_0 hg + A) + 2) + ((n + e)(2g + 3) + (n + e) + 2) + 1 + (2(k_0 hg + A) + 2) + (2hg + 2) +
1 + (k_0(2h + 3) + k_0 + 2) + (k_0 + 1) + 1 + (q(2h + 3) + q + 2) + (q + 1).
$$

The precomputation uses it with $q = K - k_0 - 1$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.preB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1095](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1095). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#pre-b).

## Run of the precomputation (initial-row generator)

Let $L$ be a layout with $K$ stacks,
let $i_c$ and $k_0$ be natural numbers and let $y$ be a list of certificate codes. For all natural
numbers $T, n, e, f$ and every output $o$, the counter part of the generator for $L$, $i_c$,
$k_0$, $y$ runs within $\mathrm{preB}(L, k_0, K - k_0 - 1, T, n, e, f)$ steps, the step bound for
the precomputation (with truncated subtraction), from the label $\mathrm{eg}$ of the first
precomputation part (its first stage), with flag false, the initial counters for $T, n, e, f$ and
output $o$, to the loop head of the tail phase, with flag false, the counters after the
precomputation for $L, k_0, T, n, e, f$ and output $o$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.pre_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#pre-run).

## The I3 loop on the whole input

Let $L$ be a layout with $g$ symbol codes, consider the
init generator for a start code, a stack $k_0$ and a list of $\ell$ certificate codes, and let
$x = (x_0, \dots, x_{s-1})$ be a list of codes $x_j < g$. Suppose its counters $F$ have $Q$,
$\mathrm{tmp}$, $\mathrm{md}$, $c_1$, $c_2$, $\mathrm{CB}$ and $P$ equal to $0$,
$\mathrm{Vc} = V$, $\mathrm{Gc} = g$, $\mathrm{ZA} = Z$ and $\mathrm{Xn} = s$, that
$jg + Z + g \le V$ for every $j < s$, and that $s \le N_b$. Then for every output $o$ and every
flag $v$, the generator, started at the head of the I3 loop with flag $v$, counters $F$, output
$o$, and $x_{s-1}, \dots, x_1, x_0$ on its input stack (top first), reaches in at most
$s\beta + 1$ steps the head of the I2 loop over the stacks above $k_0$, with flag false, the
counters of $F$ except $\mathrm{Xn} = 0$, an empty input stack, and output
$e_0 e_1 \cdots e_{s-1}$ followed by $o$. Here $e_j$ is the encoding of the dense clause over
$V$ variables whose only literal is the positive literal of variable $jg + Z + x_j$, and
$\beta = 3V^2 + 12V + (\ell + 2)(6V + 9) + (2g + 4)N_b + g + 10$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.i3_full`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#i3-full).

## Step bound of one phase loop (initial-row generator)

For $m, g, N, V \in \mathbb{N}$,
the cost of one phase loop with count bound $N$ is $N(\beta + 1) + N + 2$, where $\beta$ is the
cost of one loop iteration with clauses of at most $m$ literals, $g$ symbol codes, count bound
$N$ and $V$ variables.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.loopB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#loop-b).

## Time bound of the init generator

Let $L$ be a layout with $A$ label/state variables,
$K$ stacks and $g$ symbol codes, and let $n_Y, k_0, q, T, n, e, f$ be natural numbers. Put
$H = n + e + f$ and let $V = (T + 1)(A + K H g)$ be the number of variables. The bound is the
precomputation cost $\mathrm{preB}(L, k_0, q, T, n, e, f)$, plus $6$ times the phase-loop cost
$\mathrm{loopB}(n_Y + 2, g, K H + H, V)$, plus the clause cost $\mathrm{clauseB}(n_Y + 2, V)$.

The generator uses it with $q = K - k_0 - 1$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.initBound`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#init-bound).

## Correctness of the init generator, with its explicit time bound

Let $L$ be a layout with
$A$ label/state variables, $K$ stacks and $g > 0$ symbol codes, let $i_c < A$ and $k_0 < K$, and
let $Y$ be a strictly increasing list of codes with $0 < y < g$ for every $y \in Y$. Let $xs$ be a
list of codes below $g$ with $n = |xs|$, let $T, e, f$ be natural numbers with $f > 0$, and let
$o$ be a bit string. Start the generator for $L, i_c, k_0, Y$ at its start label with state false,
with the counters $\mathrm{Tn}, \mathrm{Xn}, \mathrm{En}, \mathrm{Fn}$ holding $T, n, e, f$ in
unary and all other counters empty, $o$ on the output stack, and $xs$ reversed on the input
stack. Then within $\mathrm{initBound}(L, |Y|, k_0, K - k_0 - 1, T, n, e, f)$ steps it reaches
the final label $\mathrm{done}$, and its output stack there is the bit encoding of the
layout-level init family for $L, i_c, k_0, Y, xs$, $m = n + e$, $T$ and $H = n + e + f$, followed
by $o$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.init_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#init-run).

## Time bound of the init generator at uniform parameters

For all natural numbers $k \ge 1$
and $y \ge 1$, let $L$ be the uniform layout with all four parameters equal to $k$. Then the time
bound of the init generator for $L$ with $n_Y = k_0 = q = k$ and $T = n = e = f = y$ is at most
$18928\,k^5 y^5$.

Every monomial of the bound is then at most $k^5 y^5$, and $18928$ is the value of the bound at
$k = y = 1$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.initBound_uni`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1396](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#init-bound-uni).

## Constant of the init generator's time bound

For a layout $L$ with $A$ label/state
variables, $K$ stacks and $g$ symbol codes, and natural numbers $n_Y$ and $k_0$, the constant is
$18928\,(A + K + g + n_Y + k_0 + 1)^5$.

It depends only on $A$, $K$, $g$, the number $n_Y$ of certificate codes and the input stack
$k_0$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.initC`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1427](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#init-c).

## Polynomial time bound for the init generator

Let $L$ be a layout with $A$ label/state
variables, $K$ stacks and $g > 0$ symbol codes, let $i_c < A$ and $k_0 < K$, and let $Y$ be a
strictly increasing list of codes with $0 < y < g$ for every $y \in Y$. Let $xs$ be a list of
codes below $g$ with $n = |xs|$, let $T, e, f$ be natural numbers with $f > 0$, and let $o$ be a
bit string. Start the generator for $L, i_c, k_0, Y$ at its start label with state false, with
the counters $\mathrm{Tn}, \mathrm{Xn}, \mathrm{En}, \mathrm{Fn}$ holding $T, n, e, f$ in unary
and all other counters empty, $o$ on the output stack, and $xs$ reversed on the input stack.
Then within $C\,(T + n + e + f + 1)^5$ steps, where $C = 18928\,(A + K + g + |Y| + k_0 + 1)^5$,
it reaches the final label $\mathrm{done}$, and its output stack there is the bit encoding of the
layout-level init family for $L, i_c, k_0, Y, xs$, $m = n + e$, $T$ and $H = n + e + f$, followed
by $o$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.init_time`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1446](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#init-time).

## Lookup in an all-positive literal list

Let $\lambda$ be a list of pairs of a natural
number and a boolean in which every boolean is true. For every $v \in \mathbb{N}$, looking up $v$
in $\lambda$ (the boolean of the first pair with first entry $v$, if any) gives true if $v$ is
the first entry of some pair in $\lambda$, and no value otherwise.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.lookup_pos`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1465](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1465). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#lookup-pos).

## Dense clauses of positive literals depend only on their positions

Let $\ell$ and
$\ell'$ be lists of literals (pairs of a position and a sign) in which every sign is positive. If
every natural number $v$ is a position of $\ell$ exactly when it is a position of $\ell'$, then
for every $V$ the dense clause over $V$ variables with literals $\ell$ equals the dense clause
over $V$ variables with literals $\ell'$: order and repetitions in the lists are irrelevant.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.denseClause_congr`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1480](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#dense-clause-congr).

## Sorted certificate code list

Given an encoding $E$ of a machine $M$ and a list $Y$ of
symbols of the input stack of $M$, this is the list of the distinct codes that $E$ assigns to the
symbols of $Y$ on the input stack, sorted in strictly increasing order.

Besides the empty cell, these are the codes allowed in the certificate cells of the initial row
(clause group I4).

Formalized by `Cslib.Complexity.CookLevin.InitFamily.ycs`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1491](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1491). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#ycs).

## Codes of input symbols

Let $E$ be an encoding of a finite multi-stack Turing machine $M$,
and let $g$ be the number of symbol codes of the layout of $E$. A symbol $z$ of the input stack
of $M$ is sent to its symbol code under $E$, viewed as an element of $\{0, \dots, g - 1\}$; the
code is below $g$ because every input symbol is an effective symbol of the input stack.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.encF`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1495](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1495). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#enc-f).

## The init family of an encoding is a layout-level init family

Let $E$ be an encoding of a
machine $M$, let $x$ and $Y$ be lists of symbols of the input stack of $M$, and let $m, T, H$ be
natural numbers. The init family of $E$ for $x, Y, m, T, H$ equals the layout-level init family
over the layout of $E$ with start code the code of the pair of the main label and the initial
state of $M$, stack $k_0$ the number of the input stack, code list the codes of the symbols of $Y$
in increasing order without repetitions, input codes the codes of the symbols of $x$, and the
same $m, T, H$.

The family of $E$ lists the certificate symbols $Y$ in their given order, possibly with repeated
codes; the equality holds because order and repetitions do not change these clauses.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.initFamily_eq`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1513](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#init-family-eq).

## Time and output of the init generator for an encoding

Let $E$ be an encoding of a
machine $M$, let $x$ and $Y$ be lists of symbols of the input stack of $M$, let $m, T, H$ be
natural numbers with $|x| \le m < H$, and let $o$ be a bit string. Let $C$ be the time constant
for the layout of $E$, the number of distinct codes of $Y$ and the number $k_0$ of the input
stack. Start the generator for $E$ (start code: the code of the pair of the main label and the
initial state; stack $k_0$; code list: the distinct codes of $Y$ in increasing order) at its
start label with state false, with the counters $\mathrm{Tn}, \mathrm{Xn}, \mathrm{En},
\mathrm{Fn}$ holding $T$, $|x|$, $m - |x|$, $H - m$ in unary and all other counters empty, $o$
on the output stack, and the list of codes of $x$, reversed, on the input stack. Then within
$C\,(T + H + 1)^5$ steps it reaches the final label $\mathrm{done}$, and its output stack there
is the bit encoding of the init family of $E$ for $x, Y, m, T, H$ followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.init_gen_time`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1551](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#init-gen-time).

## The init generator at the stack cap

Let $E$ be an encoding of a machine $M$ with window
depth $d$, let $x$ and $Y$ be lists of symbols of the input stack of $M$, let $m, T$ be natural
numbers with $|x| \le m$, let $H = m + (T + 1)d + 1$ be the stack cap, and let $o$ be a bit
string. Let $C$ be the time constant for the layout of $E$, the number of distinct codes of $Y$
and the number $k_0$ of the input stack. Start the generator for $E$ (start code: the code of
the pair of the main label and the initial state; stack $k_0$; code list: the distinct codes of
$Y$ in increasing order) at its start label with state false, with the counters $\mathrm{Tn},
\mathrm{Xn}, \mathrm{En}, \mathrm{Fn}$ holding $T$, $|x|$, $m - |x|$, $H - m$ in unary and all
other counters empty, $o$ on the output stack, and the list of codes of $x$, reversed, on the
input stack. Then within $C\,(T + H + 1)^5$ steps it reaches the final label $\mathrm{done}$,
and its output stack there is the bit encoding of the init family of $E$ for $x, Y, m, T, H$
followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.InitFamily.init_gen_capH`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean, line 1575](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/InitFamily.lean#L1575). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html#init-gen-cap-h).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cook-Levin: generator machine for the initial-row family](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-initial-row)
