---
declaration: section
origin: cited
lean: Cslib.Complexity.CookLevin.Shift.shLits, Cslib.Complexity.CookLevin.Shift.ovLits, Cslib.Complexity.CookLevin.Shift.pfLits, Cslib.Complexity.CookLevin.Shift.shBlk, Cslib.Complexity.CookLevin.Shift.shFamily, Cslib.Complexity.CookLevin.Shift.WF, Cslib.Complexity.CookLevin.Shift.depth_cover, Cslib.Complexity.CookLevin.Shift.depth_disjoint
statement: formalized
proof: formalized
---

# Cook-Levin: generator machine for the cell-shift family

75 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html).

## The family (pure specification)

## Literals of an in-range shift clause

Fix a layout $L$ and tables $\mathrm{sa}$,
$\mathrm{pl}$, $\mathrm{cn}$. For a height $H$, write $C[t,k,j,x]$ for the cell variable of
stack $k$, depth $j$ and symbol code $x$ at time $t$, and $X[t,a]$ for the label/state variable
$a$ at time $t$. With $c = \mathrm{cn}(i,k)$ and $p = \mathrm{pl}(i,k)$, the literals of the
clause $(t, i, k, u, x)$ are, as (variable, sign) pairs in this order, $\neg C[t,k,u+c,x]$,
$\neg X[t+1,\mathrm{sa}(i)]$ and $C[t+1,k,u+p,x]$. Writing $S[t,i] = X[t+1,\mathrm{sa}(i)]$ for
the situation variable of situation $i$ at time $t$, this is the clause
$\neg C[t,k,u+c,x] \lor \neg S[t,i] \lor C[t+1,k,u+p,x]$.

When all indices are in range, the literals are in increasing variable order: a row $t$ cell, the
label/state block of row $t+1$, then a row $t+1$ cell.

Formalized by `Cslib.Complexity.CookLevin.Shift.shLits`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sh-lits).

## Literals of an overflow clause

For a layout $L$ with label block size $A$, $K$ stacks and
$g$ symbol codes, row width $W = A + K H g$, situation offsets $s_a$, push counts $p$, consumed
counts $c$ and numbers $H, t, i, k, r$, write $S[t, i] = (t + 1) W + s_a(i)$ for the situation
variable (the label/state variable $s_a(i)$ of row $t + 1$), and
$C[t', k', j, x] = t' W + A + (k' H + j) g + x$ for the cell variable of row $t'$, stack $k'$,
depth $j$ and symbol code $x$. The overflow clause $(t, i, k, r)$ is the list of two (variable,
sign) literals $\neg S[t, i] \lor C[t + 1, k, H - c(i, k) + p(i, k) + r, 0]$: first the negated
situation variable $S[t, i]$, then the positive cell variable of row $t + 1$, stack $k$, depth
$H - c(i, k) + p(i, k) + r$ and symbol code $0$ (the empty cell). Subtraction is truncated at
zero.

Formalized by `Cslib.Complexity.CookLevin.Shift.ovLits`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#ov-lits).

## Literals of a pushed-fill clause

For a layout $L$ with label block size $A$, $K$ stacks
and $g$ symbol codes, row width $W = A + K H g$, situation offsets $s_a$, pushed codes $p_u$ and
numbers $H, t, i, k, j$, write $S[t, i] = (t + 1) W + s_a(i)$ for the situation variable (the
label/state variable $s_a(i)$ of row $t + 1$), and
$C[t', k', j', x] = t' W + A + (k' H + j') g + x$ for the cell variable of row $t'$, stack $k'$,
depth $j'$ and symbol code $x$. The pushed-fill clause $(t, i, k, j)$ is the list of two
(variable, sign) literals $\neg S[t, i] \lor C[t + 1, k, j, p_u(i, k, j)]$: first the negated
situation variable $S[t, i]$, then the positive cell variable of row $t + 1$, stack $k$, depth
$j$ and symbol code $p_u(i, k, j)$. It is used for depths $j$ below the number of symbols that
situation $i$ pushes on stack $k$.

Formalized by `Cslib.Complexity.CookLevin.Shift.pfLits`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#pf-lits).

## The shift block of a situation and a stack

Fix a layout with $A$ label variables, $K$
stacks and $g$ symbol codes, the generator's parameters $sa$, $pl$, $cn$, $pu$, and
$T, H, t, i, k \in \mathbb{N}$. Write $p = pl(i, k)$, $c = cn(i, k)$, $W = A + K H g$ for the row
width and $V = (T + 1) W$ for the number of variables. The block is the CNF formula consisting, in
this order, of: for each $u < H - \max(p, c)$ and each $x < g$ (ordered by $u$, then $x$), the
dense clause over $V$ variables with the in-range shift literals for $(t, i, k, u, x)$; for each
$r < c - p$, the dense clause over $V$ variables with the overflow literals for $(t, i, k, r)$;
and for each $j < p$, the dense clause over $V$ variables with the pushed-fill literals for
$(t, i, k, j)$. Subtraction is truncated at $0$.

Formalized by `Cslib.Complexity.CookLevin.Shift.shBlk`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sh-blk).

## The cell-shift clause family

Fix a layout $L$ with $K$ stacks and situation tables
$\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$. For $N, T, H \in \mathbb{N}$, the
shift family is the CNF formula obtained by concatenating the shift blocks of situation $i$ and
stack $k$ at time $t$ for all $t < T$, $i < N$ and $k < K$, ordered lexicographically by
$(t, i, k)$.

Formalized by `Cslib.Complexity.CookLevin.Shift.shFamily`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sh-family).

## Well-formed situation tables for the cell-shift family

Given a layout with label/state
block size $A$, $K$ stacks, $g$ symbol codes and window depth $d$, a situation-offset table
$\mathrm{sa}$, push-count and consumed-count tables $\mathrm{pl}$ and $\mathrm{cn}$ and a
pushed-code table $\mathrm{pu}$, the tables are well formed for $N$ situations at height $H$ when
$g > 0$, $d \le H$, $\mathrm{sa}(i) < A$ for every $i < N$, and for all $i < N$ and $k < K$:
$\mathrm{pl}(i, k) \le d$, $\mathrm{cn}(i, k) \le d$, and $\mathrm{pu}(i, k, j) < g$ for every
$j < \mathrm{pl}(i, k)$.

Formalized by `Cslib.Complexity.CookLevin.Shift.WF`, a structure declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#wf).

## Coverage of target depths

Let $p, c, H$ be natural numbers with $p \le H$ and $c \le H$,
and let $m = \max(p, c)$. Every natural number $j < H$ satisfies $j < p$, or $j = u + p$ for some
natural number $u < H - m$, or $j = H - c + p + r$ for some natural number $r < c - p$, where
$c - p$ is truncated subtraction (zero when $c \le p$).

In the cell-shift family these are the pushed-fill, in-range and overflow target depths of a
stack in the row after a time step.

Formalized by `Cslib.Complexity.CookLevin.Shift.depth_cover`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#depth-cover).

## Bounds on in-range and overflow target depths

Let $p, c, H$ be natural numbers with
$p \le H$ and $c \le H$, and let $m = \max(p, c)$. For every natural number $u < H - m$ we have
$p \le u + p$, $u + p < H - c + p$ and $u + p < H$. For every natural number $r < c - p$, where
$c - p$ is truncated subtraction, we have $H - m + p = H - c + p$ and $H - c + p + r < H$.

Formalized by `Cslib.Complexity.CookLevin.Shift.depth_disjoint`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#depth-disjoint).

## Counters of the cell-shift generator

The type with 23 elements, one for each unit counter
of the counter machine that emits the cell-shift clause family: $\mathrm{Tn}$, $\mathrm{Ti}$,
$\mathrm{Hs}$, $\mathrm{Gc}$, $\mathrm{HG}$, $\mathrm{Wc}$, $\mathrm{Vc}$, $\mathrm{TW}$,
$\mathrm{TW1}$, $\mathrm{KB}$, $\mathrm{U}$, $\mathrm{Ui}$, $\mathrm{R}$, $\mathrm{Ri}$,
$\mathrm{CB}$, $\mathrm{CW}$, $\mathrm{P}$, $\mathrm{Q}$, $\mathrm{tmp}$, $\mathrm{md}$,
$\mathrm{Ka}$, $\mathrm{c1}$ and $\mathrm{c2}$.

Formalized by `Cslib.Complexity.CookLevin.Shift.CK`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#ck).

## Base counters of literal positions

The three bases $s$, $cb$ and $cw$ from which a literal
position is computed; at time step $t$, with $W$ the row width, $s$ stands for the counter
$TW1 = (t + 1) \cdot W$ and serves the situation variable.

Formalized by `Cslib.Complexity.CookLevin.Shift.BS`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#bs).

## Counter holding a literal base

The map from the three kinds of literal base to
counters of the generator. With $t$ the current time step and $W$ the number of variables per
time step, the situation base goes to the counter holding $(t + 1) W$, the start of row
$t + 1$; the current-row cell base goes to the cell-base counter; and the next-row cell base
goes to the counter holding the cell base plus $W$.

Formalized by `Cslib.Complexity.CookLevin.Shift.BS.k`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#k).

## Clause kinds of the cell-shift family

For natural numbers $g$ and $d$, a clause kind is
either an in-range shift clause $\mathrm{sh}(x)$ for a symbol code $x < g$, the overflow-fill
clause $\mathrm{ov}$, or a pushed-fill clause $\mathrm{pf}(j)$ for a pushed depth $j < d$. These
are the kinds of clause in the block of a situation $i$ and a stack $k$.

Formalized by `Cslib.Complexity.CookLevin.Shift.CL`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#cl).

## Number of literals of a cell-shift clause kind

An in-range shift clause has $3$
literals, and an overflow clause and a pushed-fill clause have $2$ each.

Formalized by `Cslib.Complexity.CookLevin.Shift.CL.nl`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#nl).

## Base counter of a literal

For a clause kind $c$ and $l \in \mathbb{N}$: if $c$ is an
in-range shift clause, literal $l$ has base $cb$ when $l = 0$, $s$ when $l = 1$ and $cw$ when
$l \ge 2$; if $c$ is an overflow or pushed-fill clause, it has base $s$ when $l = 0$ and $cw$
otherwise.

Formalized by `Cslib.Complexity.CookLevin.Shift.CL.bs`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#bs-2).

## Constant offsets of the literals of a clause kind

Let $g$ be the number of symbol codes
of the clause kinds, and let $s, p, c \in \mathbb{N}$ and $q : \mathbb{N} \to \mathbb{N}$
(situation offset, push count, consumed count and pushed codes). The constant offset of literal
$l$ is: for an in-range shift clause $\mathrm{sh}(x)$, $cg + x$ if $l = 0$, $s$ if $l = 1$ and
$pg + x$ otherwise; for the overflow-fill clause $\mathrm{ov}$, $s$ if $l = 0$ and $pg$
otherwise; for a pushed-fill clause $\mathrm{pf}(j)$, $s$ if $l = 0$ and $jg + q(j)$
otherwise.

Formalized by `Cslib.Complexity.CookLevin.Shift.CL.cs`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#cs).

## Literal signs of a shift clause kind

For a clause kind $c$ of a cell-shift block and
$l \in \mathbb{N}$, the sign of literal $l$ of $c$ is positive exactly when $l + 1$ equals the
number of literals of $c$; so only the last literal is positive.

Formalized by `Cslib.Complexity.CookLevin.Shift.CL.sg`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sg).

## Precomputation stages of the shift generator

The labels of the precomputation that the
cell-shift generator runs before its time loop: six plain stages and three multiplication sites,
each of the latter tagged with a stage of the multiplication routine. For a layout with $A$ label
variables, $K$ stacks and $g$ symbol codes, and the inputs $T$ (number of time steps) and $H$
(height), in order of execution they set a counter $G$ to $g$; set a counter $HG$ to $H g$ (a
multiplication site); set the row-width counter $W$ to $A$; set a scratch counter to $K$; add
$K \cdot HG$ to $W$ (a multiplication site), so that $W = A + K H g$; empty the scratch counter;
set the variable counter $V$ to $T W$ (a multiplication site); and add $W$ to $V$ in two copy
steps, so that $V = (T + 1) W$.

Formalized by `Cslib.Complexity.CookLevin.Shift.PS`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#ps).

## Stages of the cell-shift literal routine

The routine emitting one literal has fifteen
stages: two copy stages, an offset stage, a decrement stage, a compare stage, two restore stages
for each comparison outcome (less, equal, greater), an absent-slot emission stage, a failure
stage, a slot emission stage and a drain stage.

Formalized by `Cslib.Complexity.CookLevin.Shift.LS`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#ls).

## Setup and loop stages of a cell-shift block

The finite type of stages of the setup and
loops of an $(i, k)$ block of the cell-shift generator: the base stages $\mathrm{kbE}$,
$\mathrm{kbC1}$, $\mathrm{kbC2}$, $\mathrm{kbK}$, $\mathrm{kbM}(s)$ for each stage $s$ of the
multiplication routine, $\mathrm{kbD}$, $\mathrm{uC1}$ and $\mathrm{uC2}$; the overflow-loop
stages $\mathrm{oE}$, $\mathrm{oHead}$, $\mathrm{oRest}$, $\mathrm{oC1}$, $\mathrm{oC2}$,
$\mathrm{oR1}$, $\mathrm{oR2}$, $\mathrm{oM}(s)$ for each stage $s$ of the multiplication routine,
and $\mathrm{oD}$; the in-range-loop and drain stages $\mathrm{sHead}$, $\mathrm{sRest}$,
$\mathrm{dU}$, $\mathrm{dR}$ and $\mathrm{dKB}$; and the pushed-fill stages $\mathrm{fC1}$,
$\mathrm{fC2}$, $\mathrm{fW1}$, $\mathrm{fW2}$ and $\mathrm{fD1}$.

Formalized by `Cslib.Complexity.CookLevin.Shift.ST`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#st).

## Loop-body stages of the cell-shift generator

For a symbol count $g$ and a window depth
$d$, the finite type of stages of the loop body of an $(i, k)$ block: for each flag $b$, two
stages adding the block base, four stages building the second base and two drain stages; one
stage for each stage of the multiplication routine; and for each clause kind $c$ (over $g$ and
$d$), a terminator stage, two stages loading the variable count, one stage for each literal
position $l < 3$ and each stage of the literal routine, and a finishing stage. The flag $b$ is
true in the in-range loop and false in the overflow loop.

Formalized by `Cslib.Complexity.CookLevin.Shift.BD`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#bd).

## Labels of the cell-shift generator

For natural numbers $N$, $K$, $g$ and $d$, a label is
one of: a precomputation stage $\mathrm{pre}(s)$; a time-loop label $\mathrm{tHead}$,
$\mathrm{tRest}$, $\mathrm{tw}(s)$ for a multiplication stage $s$, $\mathrm{t1a}$,
$\mathrm{t1b}$, $\mathrm{t1c}$, $\mathrm{t1d}$, $\mathrm{tEnd}$ or $\mathrm{tEnd2}$; a setup or
loop stage $\mathrm{s}(i, k, x)$ of the block of situation $i < N$ and stack $k < K$; a decrement
step $\mathrm{sb}(i, k, r)$ with $r < d + 1$; a loop-body stage $\mathrm{b}(i, k, x)$ of that
block, over clause kinds with parameters $g$ and $d$; or a halting label $\mathrm{bad}$ or
$\mathrm{done}$.

Formalized by `Cslib.Complexity.CookLevin.Shift.GL`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#gl).

## Entry label of a literal routine of the cell-shift generator

For a situation $i < N$, a
stack $k < K$, a clause kind $c$ and $l \in \mathbb{N}$, the entry label of literal $l$ is the
first stage of the routine emitting literal $l$ of a clause of kind $c$ in block $(i, k)$ when
$l < 3$, and the generator's final label when $l \ge 3$ (that case is never used).

Formalized by `Cslib.Complexity.CookLevin.Shift.GL.litL`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#lit-l).

## Label after a literal routine

For block $(i, k)$ of the cell-shift generator, a clause
kind $c$ and $l \in \mathbb{N}$, with the literals of a clause emitted from the last down to the
first: the label is the finishing stage of clause $c$ in block $(i, k)$ when $l = 0$; otherwise it
is the first stage of the routine for literal $l - 1$ of $c$ in block $(i, k)$ when $l - 1 < 3$,
and the final label $\mathrm{done}$, at which the generator halts, otherwise.

Formalized by `Cslib.Complexity.CookLevin.Shift.GL.after`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#after).

## Entry label of the in-range chain

For a situation $i < N$, a stack $k < K$ and a number
$n$, the label of the generator with $N$ situations, $K$ stacks, $g$ symbol codes and window
depth $d$ from which the in-range shift clauses for the symbol codes $x < n$ of the current cell
pair of block $(i, k)$ are emitted before the in-range drains: the in-range drain stage
$\mathrm{dCB}$ of block $(i, k)$ if $n = 0$, the first stage of the routine emitting the in-range
shift clause for symbol code $n - 1$ of block $(i, k)$ if $1 \le n \le g$, and the halting label
$\mathrm{done}$ (unused) if $n > g$.

Formalized by `Cslib.Complexity.CookLevin.Shift.GL.xFrom`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#x-from).

## Entry label of the pushed-fill chain

For a situation $i < N$, a stack $k < K$ and a
number $n$, the label of the generator with $N$ situations, $K$ stacks, $g$ symbol codes and
window depth $d$ from which the pushed-fill clauses $j < n$ of block $(i, k)$ are emitted before
the fill drains: the fill-drain stage $\mathrm{fD1}$ of block $(i, k)$ if $n = 0$, the first
stage of the routine emitting pushed-fill clause $n - 1$ of block $(i, k)$ if $1 \le n \le d$,
and the halting label $\mathrm{done}$ (unused) if $n > d$.

Formalized by `Cslib.Complexity.CookLevin.Shift.GL.pfFrom`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#pf-from).

## Label after a clause of the cell-shift generator

For a situation $i < N$ and a stack
$k < K$, in block $(i, k)$: after the in-range clause for symbol $x$ the generator goes to the
start of the in-range clause for symbol $x - 1$, or to the in-range drains when $x = 0$; after
the overflow clause it goes to the overflow drains; after the pushed-fill clause for depth $j$
it goes to the start of the pushed-fill clause for depth $j - 1$, or to the pushed-fill drains
when $j = 0$.

Formalized by `Cslib.Complexity.CookLevin.Shift.GL.nextC`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#next-c).

## Label of the decrement chain

Among the generator labels for $N$ situations, $K$ stacks,
$g$ symbol codes and window depth $d$, take a situation $i < N$, a stack $k < K$ and
$n \in \mathbb{N}$. The label is the pushed-fill setup label of block $(i, k)$ if $n = 0$, the
decrement label of block $(i, k)$ with index $n - 1$ if $1 \le n \le d + 1$, and the terminal
label otherwise. It marks the point where $n$ decrements of the counter $U$ remain before the
pushed-fill setup.

Formalized by `Cslib.Complexity.CookLevin.Shift.GL.sbL`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sb-l).

## Entry label of the situation chain

For a natural number $n$, with $N$ the number of
situations and $K$ the number of stacks, this is the end-of-time-step label when $n = 0$ or
$K = 0$; the first setup stage of block $(n - 1, K - 1)$ when $1 \le n \le N$ and $K \ge 1$;
and the terminal (halting) label when $n > N$ and $K \ge 1$. For $n \le N$ it is the label
from which the generator emits the blocks of situations $i < n$ and then ends the time step.

Formalized by `Cslib.Complexity.CookLevin.Shift.GL.iFrom`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#i-from).

## Entry label of the stack chain of a situation

For natural numbers $i$ and $n$, with $N$
the number of situations and $K$ the number of stacks, this is the entry label of the situation
chain for $i$ when $n = 0$; the first setup stage of block $(i, n - 1)$ when $1 \le n \le K$ and
$i < N$; and the terminal (halting) label otherwise. For $i < N$ and $n \le K$ it is the label
from which the generator emits the blocks of stacks $k < n$ of situation $i$ and then the blocks
of situations $< i$.

Formalized by `Cslib.Complexity.CookLevin.Shift.GL.ik`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#ik).

## Labels of the shift generator

For a layout with $K$ stacks, $g$ symbol codes and
window depth $d$, and a number $N$ of situations, the labels of the generator are the finite
label type with parameters $N$, $K$, $g$ and $d$.

Formalized by `Cslib.Complexity.CookLevin.Shift.Lab`, an abbreviation declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#lab).

## Constant offset of a literal in a block

Let $L$ be a layout with $K$ stacks, $g$ symbol
codes and window depth $d$, let $N \in \mathbb{N}$ be the number of situations, and let
$\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$ and $\mathrm{pu}$ give the situation offsets, push
counts, consumed counts and pushed codes. For a situation $i < N$, a stack $k < K$, a clause kind
$c$ with parameters $g$ and $d$, and $l \in \mathbb{N}$, the constant offset of literal $l$ of $c$
in block $(i, k)$ is the constant offset of literal $l$ of $c$ with situation offset
$\mathrm{sa}(i)$, push count $\mathrm{pl}(i, k)$, consumed count $\mathrm{cn}(i, k)$ and pushed
codes $j \mapsto \mathrm{pu}(i, k, j)$.

Formalized by `Cslib.Complexity.CookLevin.Shift.csv`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#csv).

## Literal routine of the cell-shift generator

For a situation $i < N$, a stack $k < K$, a
clause kind $c$ and a literal index $l < 3$, this is the program fragment, indexed by the stages
of the literal routine, that emits literal $l$ of clause $c$ in block $(i, k)$. Write $B$ for the
base counter of literal $l$ and $a$ for its constant offset in block $(i, k)$. Started with $Q$
and the scratch counters empty, the routine copies the value $b$ of $B$ into the counter $Q$
through a scratch counter, restoring $B$, and adds $a$, so that $Q = b + a$. It then repeats:
decrement the counter $P$, halting if $P$ is already $0$; compare $P$ with $Q$ through two
scratch counters, restoring both; if they differ, push the absent-slot code $01$ onto the output
and repeat; if they are equal, push the slot code of a literal whose sign is positive exactly
when $l$ is the last literal of $c$. Finally it empties $Q$ and jumps to the routine of literal
$l - 1$, or to the end of the clause when $l = 0$.

Formalized by `Cslib.Complexity.CookLevin.Shift.litP`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#lit-p).

## Block stages of the cell-shift generator

For a layout $L$ with label block size $A$ and
$K$ stacks, push-count and consumed-count tables $\mathrm{pl}$ and $\mathrm{cn}$, a number $N$ of
situations, a situation $i < N$ and a stack $k < K$, write $p = \mathrm{pl}(i, k)$ and
$c = \mathrm{cn}(i, k)$.
This assigns a statement of the generator to each setup or loop stage of block $(i, k)$; below,
"add $X$ to $Y$" copies counter $X$ onto $Y$ through the scratch counter $\mathrm{tmp}$ in two
stages, restoring $X$, and "drain $X$" empties $X$. The setup pushes $A$ units onto $\mathrm{KB}$,
adds $\mathrm{TW}$ to $\mathrm{KB}$, pushes $k$ units onto $\mathrm{Ka}$, adds
$\mathrm{Ka} \cdot \mathrm{HG}$ to $\mathrm{KB}$ by the multiplication routine (index
$\mathrm{md}$, scratch $\mathrm{tmp}$), drains $\mathrm{Ka}$, adds $\mathrm{Hs}$ to $\mathrm{U}$,
and goes to the label of the decrement chain for $\max(p, c)$. The pushed-fill stages add
$\mathrm{KB}$ and then $\mathrm{Wc}$ to $\mathrm{CW}$ and go to the entry label of the pushed-fill
chain for $p$; the fill drain drains $\mathrm{CW}$, and the next stage pushes $c - p$ units onto
$\mathrm{R}$ (truncated subtraction). The overflow loop pops $\mathrm{R}$, pushing each unit on
the index counter $\mathrm{Ri}$; for each popped unit it adds $\mathrm{U}$ and then $\mathrm{R}$ to
$\mathrm{Ka}$, adds $\mathrm{Ka} \cdot \mathrm{Gc}$ to $\mathrm{CB}$ by the multiplication
routine, drains $\mathrm{Ka}$ and runs the loop body with flag false; when $\mathrm{R}$ is empty it
moves $\mathrm{Ri}$ back onto $\mathrm{R}$. The in-range loop likewise pops $\mathrm{U}$ onto
$\mathrm{Ui}$ and runs the loop body with flag true for each popped unit, and when $\mathrm{U}$ is
empty moves $\mathrm{Ui}$ back onto $\mathrm{U}$. Finally it drains $\mathrm{U}$, $\mathrm{R}$ and
$\mathrm{KB}$ and goes to the entry label of the stack chain of situation $i$ for $k$.

Formalized by `Cslib.Complexity.CookLevin.Shift.stP`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#st-p).

## Loop body of the cell-shift generator

For a layout $L$ with $g$ symbol codes and a block
$(i, k)$, the generator's statement at each loop-body stage, with flag $b$ true in the in-range
loop and false in the overflow loop: add the counter $KB$ to the counter $CB$; when $b$ is true,
add the product of the counters $U$ and $Gc$ to $CB$; add $CB$ and then the counter $Wc$ to the
counter $CW$; then start the in-range clauses for the symbols $x = g - 1, \dots, 0$ when $b$ is
true, and the overflow clause otherwise. A clause $c$ (in-range, overflow or pushed fill)
prepends the terminator $00$ to the output, adds the counter $Vc$ to the counter $P$, runs the
literal routines of $c$ from the last down to the first, drains $P$ prepending $01$ per unit, and
goes on to the next clause of its chain; after the last pushed-fill clause it returns to the
fill drain of the block setup, and after the last in-range clause and after the overflow clause
the drain stages empty $CB$ and then $CW$ and return to the head of the in-range loop when $b$ is
true, and of the overflow loop otherwise.

Formalized by `Cslib.Complexity.CookLevin.Shift.bdP`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#bd-p).

## The cell-shift generator

For a layout $L$ with label block size $A$, $K$ stacks and $g$
symbol codes, tables $s_a, p, c, p_u$ and $N$ situations, the counter machine with the unit
counters of the generator and a Boolean output stack, meant to start with $T$ units on
$\mathrm{Tn}$, $H$ on $\mathrm{Hs}$ and everything else empty. Its precomputation puts $g$ units
on $\mathrm{Gc}$, adds $\mathrm{Hs} \cdot \mathrm{Gc}$ to $\mathrm{HG}$, puts $A$ units on
$\mathrm{Wc}$ and $K$ on $\mathrm{Ka}$, adds $\mathrm{Ka} \cdot \mathrm{HG}$ to $\mathrm{Wc}$,
drains $\mathrm{Ka}$, adds $\mathrm{Tn} \cdot \mathrm{Wc}$ to $\mathrm{Vc}$ and then adds
$\mathrm{Wc}$ to $\mathrm{Vc}$. The time loop then pops one unit of $\mathrm{Tn}$ per iteration,
pushing it on $\mathrm{Ti}$; each iteration adds $\mathrm{Tn} \cdot \mathrm{Wc}$ to
$\mathrm{TW}$, adds $\mathrm{TW}$ and then $\mathrm{Wc}$ to $\mathrm{TW1}$, runs the blocks of
all $N$ situations, and drains $\mathrm{TW}$ and $\mathrm{TW1}$. When $\mathrm{Tn}$ is empty it
moves $\mathrm{Ti}$ back onto $\mathrm{Tn}$ and halts at $\mathrm{done}$. The stages of a block
$(i, k)$ run the block routine, its loop-body stages run the loop-body routine, and its
decrement stages pop $\mathrm{U}$ and continue the decrement chain, halting at $\mathrm{bad}$ if
$\mathrm{U}$ is empty. Additions go through the scratch counters $\mathrm{md}$ and $\mathrm{tmp}$
and restore their sources when the scratch counters start empty.

Formalized by `Cslib.Complexity.CookLevin.Shift.prog`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#prog).

## The cell-shift generator as a finite stack machine

For a layout $L$, situation tables
$\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$ and $N$ situations, the cell-shift
generator for these data, bundled as a multi-stack Turing machine with finitely many stacks,
labels and states: its stacks are the Boolean output stack and one counter stack for each counter
of the generator, its input stack is the counter $\mathrm{Tn}$ and its output stack is the Boolean
output stack, its alphabets are the counter-machine alphabets (Booleans on the output stack, a
unit symbol on each counter), its labels are the labels of the shift generator for $L$ and $N$,
execution starts at the first precomputation stage, its internal state is a Boolean, initially
false, and its transition function is the cell-shift generator.

It serves only to check that the generator meets the finiteness conditions of a finite machine.

Formalized by `Cslib.Complexity.CookLevin.Shift.shTM`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sh-tm).

## Literals of a clause kind at given positions

Let $c$ be a clause kind with $n$ literals
($n = 3$ for an in-range shift clause, $n = 2$ for an overflow-fill or pushed-fill clause) and let
$\mathrm{pos} : \mathbb{N} \to \mathbb{N}$. The literals of $c$ at positions $\mathrm{pos}$ are the
list $(\mathrm{pos}(0), b_0), \dots, (\mathrm{pos}(n - 1), b_{n - 1})$ of variable-sign pairs,
where the sign $b_l$ is true (a positive literal) exactly when $l = n - 1$.

Formalized by `Cslib.Complexity.CookLevin.Shift.clits`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#clits).

## Increasing literal positions below a bound

For $p : \mathbb{N} \to \mathbb{N}$ and
$n, V \in \mathbb{N}$, the positions $p$ are increasing for $n$ literals below $V$ when
$p(l) < p(l + 1)$ for every $l$ with $l + 1 < n$, and $p(n - 1) < V$ if $n \ge 1$.

Formalized by `Cslib.Complexity.CookLevin.Shift.Mono`, a structure declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 442](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L442). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#mono).

## Boundary before a literal

For $V, n, l \in \mathbb{N}$ and literal positions
$pos : \mathbb{N} \to \mathbb{N}$, the boundary before literal $l$ is $pos(l)$ if $l < n$, and $V$
otherwise.

Formalized by `Cslib.Complexity.CookLevin.Shift.bnd`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#bnd).

## Empty scratch counters of the shift generator

A valuation $F$ of the generator's counters
satisfies this predicate when the five scratch counters $Q$, $\mathit{tmp}$, $\mathit{md}$, $c_1$
and $c_2$ all have value $0$ under $F$. The generator keeps them empty whenever a clause starts.

Formalized by `Cslib.Complexity.CookLevin.Shift.Rest`, a structure declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 482](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L482). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#rest).

## One literal routine of the cell-shift generator

Let $i < N$ be a situation, $k < K$ a
stack, $c$ a clause kind and $l < 3$ a literal index. Let $F$ be counter values whose scratch
counters ($Q$, the copy buffer, the multiplication buffer and the two comparison buffers) are
$0$, let $b$ be the value under $F$ of the base counter of literal $l$, and let $a$ be the
constant offset of literal $l$ of $c$ in block $(i, k)$. Let $q, m \in \mathbb{N}$ satisfy
$q = b + a$ and $F(P) = q + m + 1$. Then for every output $o$ and internal state $v$, the
generator goes in at most $m(3q + 6) + 2b + 4q + 9$ steps from the start of the routine of
literal $l$, with state $v$, counters $F$ and output $o$, to the start of the routine of literal
$l - 1$ (the end-of-clause label of $c$ when $l = 0$), with state false, counters $F$ except
that $P = q$, and output the slot code of literal $l$ (sign positive exactly when $l$ is the last
literal of $c$), followed by $m$ copies of $01$, followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.Shift.lit_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 497](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#lit-run).

## Per-literal step overhead of the cell-shift generator

For $V \in \mathbb{N}$, the
per-literal overhead is $6V + 9$.

It is the step budget for emitting one literal of a clause over $V$ variables, not counting the
loop that emits the gap before the literal.

Formalized by `Cslib.Complexity.CookLevin.Shift.litE`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#lit-e).

## Step bound for one clause

For a natural number $V$ (the number of variables), the step
bound for one clause of at most three literals is $V(3V + 6) + 3(6V + 9) + 3V + 4$, where
$6V + 9$ is the per-literal cost apart from the gap loop.

Formalized by `Cslib.Complexity.CookLevin.Shift.clauseB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 534](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L534). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#clause-b).

## The literal routines of one clause of the cell-shift generator

Fix $V \in \mathbb{N}$, a
situation $i < N$, a stack $k < K$, a clause kind $c$ with $n$ literals, positions
$p : \mathbb{N} \to \mathbb{N}$, counter values $F$ whose scratch counters are $0$, and an output
$o$. Suppose that for every $l$ the position $p(l)$ is the value under $F$ of the base counter of
literal $l$ plus its constant offset in block $(i, k)$, that this base value is at most $V$, that
$p(l) < p(l + 1)$ whenever $l + 1 < n$, and that $p(n - 1) < V$ if $n \ge 1$. Let
$\beta(l) = p(l)$ for $l < n$ and $\beta(l) = V$ otherwise, and let $E(l)$ be the gap encoding,
from slot $\beta(l)$ up to $V$, of literals $l, \dots, n - 1$ of $c$ at positions $p$, each
with sign positive exactly when it is the last literal. Then for every $l \le n$ and every
internal state $v$ there is a state $v'$ such that the generator goes in at most
$\beta(l)(3V + 6) + l(6V + 9)$ steps from the start of the routine of literal $l - 1$ (the
end-of-clause label of $c$ when $l = 0$), with state $v$, counters $F$ except that
$P = \beta(l)$, and output $E(l)$ followed by $00$ and $o$, to the end-of-clause label of $c$,
with state $v'$, counters $F$ except that $P = \beta(0)$, and output $E(0)$ followed by $00$
and $o$.

Formalized by `Cslib.Complexity.CookLevin.Shift.lits_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 537](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L537). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#lits-run).

## One clause of the cell-shift generator

Let $M$ be the cell-shift generator for a layout
$L$ with $K$ stacks, $g$ symbol codes and window depth $d$, situation offsets $\mathrm{sa}$, push
counts $\mathrm{pl}$, consumed counts $\mathrm{cn}$, pushed codes $\mathrm{pu}$ and $N$
situations. Fix a situation $i < N$, a stack $k < K$, a clause kind $c$ with parameters $g$ and
$d$ and with $n$ literals, positions $\mathrm{pos} : \mathbb{N} \to \mathbb{N}$, counter values $F$
and $V \in \mathbb{N}$. For each $l \in \mathbb{N}$ let $b_l$ be the counter holding the base of
literal $l$ of $c$ and $o_l$ the constant offset of literal $l$ of $c$ in block $(i, k)$. Assume
that the scratch counters $\mathrm{Q}$, $\mathrm{tmp}$, $\mathrm{md}$, $\mathrm{c1}$ and
$\mathrm{c2}$ are zero in $F$; that $\mathrm{pos}(l) = F(b_l) + o_l$ and $F(b_l) \le V$ for every
$l \in \mathbb{N}$; that $\mathrm{pos}(l) < \mathrm{pos}(l + 1)$ whenever $l + 1 < n$ and
$\mathrm{pos}(n - 1) < V$; and that $F(\mathrm{Vc}) = V$ and $F(\mathrm{P}) = 0$. Then for every
output word $w$ and flag $v$, $M$ runs in at most $V(3V + 6) + 3(6V + 9) + 3V + 4$ steps (the step
bound for one clause) from the configuration with label $\mathrm{e00}(c)$ of block $(i, k)$, flag
$v$, counter values $F$ and output $w$ to the configuration with the label that follows clause $c$
in block $(i, k)$, flag false, counter values $F$ and output $e$ followed by $w$, where $e$ is the
encoding of the dense clause over $V$ variables whose literals are those of $c$ at positions
$\mathrm{pos}$.

Formalized by `Cslib.Complexity.CookLevin.Shift.clause_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 588](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L588). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#clause-run).

## First cell variable of a block

For a layout with label block size $A$, $K$ stacks
and $g$ symbol codes, a stack height $H$, a time $t$ and a stack $k$, this is the number
$k \cdot (H g) + (t W + A)$, where $W = A + K H g$ is the number of variables per time step.
It is the index of the variable for depth $0$ and symbol code $0$ of stack $k$ in row $t$.

Formalized by `Cslib.Complexity.CookLevin.Shift.kbv`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 634](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L634). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#kbv).

## Literal positions of an in-range shift clause

For a layout $L$ with label block size $A$,
$K$ stacks and $g$ symbol codes, row width $W = A + K H g$, situation offsets $s_a$, push counts
$p$, consumed counts $c$ and numbers $H, t, i, k, u, x, l$, the position of literal $l$ of the
in-range shift clause $(t, i, k, u, x)$ is: if $l = 0$, the cell variable of row $t$, stack $k$,
depth $u + c(i, k)$ and symbol code $x$, namely $t W + A + (k H + u + c(i, k)) g + x$; if
$l = 1$, the situation variable $(t + 1) W + s_a(i)$; and if $l \ge 2$, the cell variable of row
$t + 1$, stack $k$, depth $u + p(i, k)$ and symbol code $x$, namely
$(t + 1) W + A + (k H + u + p(i, k)) g + x$.

Formalized by `Cslib.Complexity.CookLevin.Shift.shPos`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 637](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L637). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sh-pos).

## Literal positions of an overflow clause

For a layout $L$ with label block size $A$, $K$
stacks and $g$ symbol codes, row width $W = A + K H g$, situation offsets $s_a$, push counts $p$,
consumed counts $c$ and numbers $H, t, i, k, r, l$, the position of literal $l$ of the overflow
clause $(t, i, k, r)$ is the situation variable $(t + 1) W + s_a(i)$ if $l = 0$, and otherwise the
cell variable of row $t + 1$, stack $k$, depth $H - c(i, k) + p(i, k) + r$ and symbol code $0$,
namely $(t + 1) W + A + (k H + H - c(i, k) + p(i, k) + r) g$. Subtraction is truncated at $0$.

Formalized by `Cslib.Complexity.CookLevin.Shift.ovPos`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 642](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L642). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#ov-pos).

## Literal positions of a pushed-fill clause

For a layout $L$ with label block size $A$,
$K$ stacks and $g$ symbol codes, row width $W = A + K H g$, situation offsets $s_a$, pushed codes
$p_u$ and numbers $H, t, i, k, j, l$, the position of literal $l$ of the pushed-fill clause
$(t, i, k, j)$ is the situation variable $(t + 1) W + s_a(i)$ if $l = 0$, and otherwise the cell
variable of row $t + 1$, stack $k$, depth $j$ and symbol code $p_u(i, k, j)$, namely
$(t + 1) W + A + (k H + j) g + p_u(i, k, j)$.

Formalized by `Cslib.Complexity.CookLevin.Shift.pfPos`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 713](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L713). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#pf-pos).

## Counter state of a loop body

For a layout $L$ with label block size $A$, $KK$ stacks and
$g$ symbol codes, $T, H, t \in \mathbb{N}$ and counter contents $F$, let $W = A + KK \cdot H g$ be
the row width. The condition holds when the scratch counters $Q$, $tmp$, $md$, $c_1$, $c_2$ and
the counter $P$ are empty, $Vc$ holds the variable count $(T + 1) W$, $Gc$ holds $g$, $Wc$ holds
$W$, $TW$ holds $t W$ and $TW1$ holds $(t + 1) W$.

Formalized by `Cslib.Complexity.CookLevin.Shift.Body`, a structure declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 741](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L741). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#body).

## The in-range chain of the cell-shift generator

Let $L$ be a layout with label block size
$A$, $K$ stacks, $g$ symbol codes and window depth $d$, let $H, T \in \mathbb{N}$, let
$W = A + K H g$ be the row width and $V = (T + 1) W$ the number of variables, and let the tables
$\mathrm{sa}, \mathrm{pl}, \mathrm{cn}, \mathrm{pu}$ be well formed for $N$ situations and height
$H$: $g > 0$, $d \le H$, and for all $i < N$ and $k < K$, $\mathrm{sa}(i) < A$,
$\mathrm{pl}(i, k) \le d$, $\mathrm{cn}(i, k) \le d$ and $\mathrm{pu}(i, k, j) < g$ for every
$j < \mathrm{pl}(i, k)$. Let $t < T$, $i < N$, $k < K$ and $u \in \mathbb{N}$ with
$u + \max(\mathrm{pl}(i, k), \mathrm{cn}(i, k)) < H$, let $b = k H g + t W + A$ be the first
cell variable of stack $k$ in row $t$, and let $F$ be counter values in which $\mathrm{Q}$,
$\mathrm{tmp}$, $\mathrm{md}$, $\mathrm{c1}$, $\mathrm{c2}$ and $\mathrm{P}$ are $0$,
$F(\mathrm{Vc}) = V$, $F(\mathrm{Gc}) = g$, $F(\mathrm{Wc}) = W$, $F(\mathrm{TW}) = t W$,
$F(\mathrm{TW1}) = (t + 1) W$, $F(\mathrm{CB}) = u g + b$ and $F(\mathrm{CW}) = u g + b + W$.
Then for every $n \le g$, every output word $o$ and every flag $v$ there is a flag $v'$ such that
the generator for these data, started at the entry label of the in-range chain for $n$ in block
$(i, k)$ with flag $v$, counters $F$ and output $o$, reaches the in-range drain stage
$\mathrm{dCB}$ of block $(i, k)$ with flag $v'$, counters $F$ and output $e_0 e_1 \cdots e_{n-1}$
followed by $o$ in at most $n \cdot \mathrm{clauseB}(V)$ steps, where
$\mathrm{clauseB}(V) = V(3V + 6) + 3(6V + 9) + 3V + 4$ and $e_x$ is the encoding of the dense
clause over $V$ variables whose literals are the in-range shift literals for $(t, i, k, u, x)$.

Formalized by `Cslib.Complexity.CookLevin.Shift.xs_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 750](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L750). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#xs-run).

## The pushed-fill chain of the cell-shift generator

Let $L$ be a layout with label block
size $A$, $K$ stacks and $g$ symbol codes, let $W = A + K H g$ be the row width and
$V = (T + 1) W$ the number of variables, and let the tables $s_a, p, c, p_u$ be well formed for
$N$ situations and height $H$. Let $t < T$, $i < N$, $k < K$, and let $F$ be counter values in
which $\mathrm{Q}$, $\mathrm{tmp}$, $\mathrm{md}$, $\mathrm{c1}$, $\mathrm{c2}$ and $\mathrm{P}$
are $0$, $F(\mathrm{Vc}) = V$, $F(\mathrm{Gc}) = g$, $F(\mathrm{Wc}) = W$, $F(\mathrm{TW}) = t W$,
$F(\mathrm{TW1}) = (t + 1) W$ and $F(\mathrm{CW}) = k H g + t W + A + W$. Then for every
$n \le p(i, k)$, every output word $o$ and every flag $v$ there is a flag $v'$ such that the
generator for these data, started at the entry label of the pushed-fill chain for $n$ in block
$(i, k)$ with flag $v$, counters $F$ and output $o$, reaches the fill-drain stage $\mathrm{fD1}$
of block $(i, k)$ (before draining) with flag $v'$, counters $F$ and output
$e_0 e_1 \cdots e_{n-1}$ followed by $o$ in at most $n \cdot \mathrm{clauseB}(V)$ steps, where
$\mathrm{clauseB}(V) = 3 V^2 + 27 V + 31$ and $e_j$ is the encoding of the dense clause over $V$
variables whose literals are those of the pushed-fill clause $(t, i, k, j)$.

Formalized by `Cslib.Complexity.CookLevin.Shift.pf_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 782](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L782). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#pf-run).

## The decrement chain takes $n$ steps

Fix a layout with $K$ stacks and window depth $d$,
the generator's remaining parameters with $N$ situations, a situation $i < N$ and a stack $k < K$.
For every $n \le d + 1$, every counter valuation $F$ and every $h$ with $F(U) = h + n$, every flag
$v$ and every output $o$, there is a flag $v'$ such that the generator, started at the
decrement-chain label for $n$ remaining decrements of block $(i, k)$ with flag $v$, counters $F$
and output $o$, reaches in exactly $n$ steps the pushed-fill setup label of block $(i, k)$ with
flag $v'$, the counters $F$ with $U$ set to $h$, and the same output $o$.

Formalized by `Cslib.Complexity.CookLevin.Shift.sb_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 817](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L817). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sb-run).

## Step bound for one in-range loop iteration

For natural numbers $g$, $H$ and $V$, with
$B(V)$ the cost bound of one clause over $V$ variables, the bound is
$(2V + 2) + (H(2g + 3) + H + 2) + (2V + 2) + (2V + 2) + g \cdot B(V) + (V + 1) + (V + 1)$.

Formalized by `Cslib.Complexity.CookLevin.Shift.sBodyB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 862](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L862). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#s-body-b).

## Step budget of one overflow iteration of the cell-shift generator

For
$g, H, d, V \in \mathbb{N}$, the budget is

$$(2H + 2) + (2d + 2) + (H(2g + 3) + H + 2) + (H + 1) + 3(2V + 2) + B(V) + 2(V + 1),$$

where $B(V) = V(3V + 6) + 3(6V + 9) + 3V + 4$ is the step budget of one clause. It bounds the
steps of one iteration of the overflow loop.

Formalized by `Cslib.Complexity.CookLevin.Shift.oBodyB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 867](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L867). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#o-body-b).

## One iteration of the in-range loop of the cell-shift generator

Let $L$ be a layout with
label block size $A$, $K$ stacks, $g$ symbol codes and window depth $d$, let $T, H \in \mathbb{N}$,
let $W = A + K H g$ be the row width and $V = (T + 1) W$ the number of variables, and let the
situation-offset, push-count, consumed-count and pushed-code tables $s_a, p, c, p_u$ be well
formed for $N$ situations and height $H$. Let $t < T$, $i < N$, $k < K$ and $u \in \mathbb{N}$
with $u + \max(p(i, k), c(i, k)) < H$. Let $F$ be counter values in which $\mathrm{Q}$,
$\mathrm{tmp}$, $\mathrm{md}$, $\mathrm{c1}$, $\mathrm{c2}$, $\mathrm{P}$, $\mathrm{CB}$ and
$\mathrm{CW}$ are $0$, $F(\mathrm{Vc}) = V$, $F(\mathrm{Gc}) = g$, $F(\mathrm{Wc}) = W$,
$F(\mathrm{TW}) = t W$, $F(\mathrm{TW1}) = (t + 1) W$, $F(\mathrm{KB}) = k H g + t W + A$ and
$F(\mathrm{U}) = u$. Then for every output word $o$ and flag $v$, the generator for these data,
started at the in-range variant of the first loop-body stage $\mathrm{bC1}$ of block $(i, k)$
with flag $v$, counters $F$ and output $o$, reaches the in-range loop head $\mathrm{sHead}$ of
block $(i, k)$ with flag false, counters $F$ and output $e_0 e_1 \cdots e_{g-1}$ followed by $o$
in at most $3(2V + 2) + (H(2g + 3) + H + 2) + g B(V) + 2(V + 1)$ steps, where
$B(V) = V(3V + 6) + 3(6V + 9) + 3V + 4$ is the step budget of one clause and $e_x$ is the
encoding of the dense clause over $V$ variables whose literals are the in-range shift literals
for $(t, i, k, u, x)$.

Formalized by `Cslib.Complexity.CookLevin.Shift.sbody_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 872](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L872). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sbody-run).

## One iteration of the overflow loop of the cell-shift generator

Let $L$ be a layout with
label block size $A$, $K$ stacks, $g$ symbol codes and window depth $d$, let $W = A + K H g$ be the
row width and $V = (T + 1) W$ the number of variables, and let the tables $s_a, p, c, p_u$ be well
formed for $N$ situations and height $H$. Let $t < T$, $i < N$, $k < K$ and
$r < c(i, k) - p(i, k)$. Let $F$ be counter values in which $\mathrm{Q}$, $\mathrm{tmp}$,
$\mathrm{md}$, $\mathrm{c1}$, $\mathrm{c2}$, $\mathrm{P}$, $\mathrm{Ka}$, $\mathrm{CB}$ and
$\mathrm{CW}$ are $0$, $F(\mathrm{Vc}) = V$, $F(\mathrm{Gc}) = g$, $F(\mathrm{Wc}) = W$,
$F(\mathrm{TW}) = t W$, $F(\mathrm{TW1}) = (t + 1) W$, $F(\mathrm{KB}) = k H g + t W + A$,
$F(\mathrm{U}) = H - \max(p(i, k), c(i, k))$ and $F(\mathrm{R}) = r$. Then for every output word
$o$ and flag $v$, the generator for these data, started at stage $\mathrm{oC1}$ of block $(i, k)$
with flag $v$, counters $F$ and output $o$, reaches stage $\mathrm{oHead}$ of block $(i, k)$ with
flag false, counters $F$ and output $e$ followed by $o$ in at most
$\mathrm{oBodyB}(g, H, d, V) = 3 V^2 + 35 V + 2 g H + 7 H + 2 d + 46$ steps, where $e$ is the
encoding of the dense clause over $V$ variables whose literals are those of the overflow clause
$(t, i, k, r)$.

Formalized by `Cslib.Complexity.CookLevin.Shift.obody_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 918](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L918). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#obody-run).

## Counter state at the start of a block

For a layout $L$ with $g$ symbol codes,
$T, H, t \in \mathbb{N}$ and counter contents $F$: $F$ is a loop-body counter state for
$L, T, H, t$, the counters $KB$, $U$, $Ui$, $R$, $Ri$, $Ka$, $CB$ and $CW$ are empty, $HG$ holds
$H \cdot g$ and $Hs$ holds $H$.

Formalized by `Cslib.Complexity.CookLevin.Shift.Blk`, a structure declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 996](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L996). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#blk).

## Step budget for one block of the shift generator

For natural numbers $g$, $K$, $H$,
$d$ and $V$ (in use: the number of symbol codes, the number of stacks, the stack height, the
window depth and the number of variables), the budget is

$$
1 + (2V + 2) + 1 + \bigl(K(2V + 3) + K + 2\bigr) + (K + 1) + (2H + 2) + d + 1 +
\bigl((2V + 2) + (2V + 2) + d\,c(V) + (V + 1)\bigr) + \bigl(d\,(o + 1) + d + 2\bigr) +
\bigl(H\,(s + 1) + H + 2\bigr) + (H + 1) + (d + 1) + (V + 1),
$$

where $c(V)$ is the step budget of one clause, $o$ is the step budget $o(g, H, d, V)$ of one
iteration of the overflow loop, and $s$ is the step budget $s(g, H, V)$ of one iteration of
the in-range loop.

Formalized by `Cslib.Complexity.CookLevin.Shift.ikB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1009](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1009). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#ik-b).

## Correctness of the shift generator on one block

Let $t < T$, assume the
well-formedness conditions for $N$ situations and stack height $H$, let $i < N$ and $k < K$,
where $K$ is the number of stacks, and let $F$ be counter values satisfying the block-start
conditions at time $t$. Then for every output $o$ and every Boolean state $v$, the generator,
started at the first setup stage of block $(i, k)$ with state $v$, counters $F$ and output $o$,
reaches in at most $B$ steps the entry label of the stacks $< k$ of situation $i$, with state
false, counters $F$ and output $e$ followed by $o$. Here $e$ is the encoding of the clause block
of situation $i$, stack $k$ at time $t$, and $B$ is the step budget for one block with
$V = (T + 1) W$ variables, $W$ being the number of variables per time step.

Formalized by `Cslib.Complexity.CookLevin.Shift.ik_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1031](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1031). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#ik-run).

## Encoded blocks of one situation

For a layout $L$ with $KK$ stacks, family data
$sa, pl, cn, pu$ and $T, H, t, i \in \mathbb{N}$, the bit string obtained by concatenating, for
$k = 0, \dots, KK - 1$ in order, the encoding of the clause block of situation $i$, stack $k$ at
time $t$.

Formalized by `Cslib.Complexity.CookLevin.Shift.blkI`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#blk-i).

## Encoded blocks of one time step

For a layout $L$, family data $sa, pl, cn, pu$ and
$N, T, H, t \in \mathbb{N}$, the bit string obtained by concatenating, for situations
$i = 0, \dots, N - 1$ in order, the encoded blocks of situation $i$ at time $t$.

Formalized by `Cslib.Complexity.CookLevin.Shift.blkT`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#blk-t).

## Correctness of the shift generator on the stack chain of a situation

Let $t < T$,
assume the well-formedness conditions for $N$ situations and stack height $H$, let $i < N$,
and let $F$ be counter values satisfying the block-start conditions at time $t$. Then for
every $n \le K$, where $K$ is the number of stacks, every output $o$ and every Boolean state
$v$, there is a Boolean state $v'$ such that the generator, started at the entry label of the
stacks $< n$ of situation $i$ with state $v$, counters $F$ and output $o$, reaches in at most
$n \cdot B$ steps the entry label of the situation chain for $i$, with state $v'$, counters $F$
and output $e_0 e_1 \cdots e_{n-1}$ followed by $o$. Here $e_k$ is the encoding of the clause
block of situation $i$, stack $k$ at time $t$, and $B$ is the step budget for one block with
$V = (T + 1) W$ variables, $W$ being the number of variables per time step.

Formalized by `Cslib.Complexity.CookLevin.Shift.ks_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#ks-run).

## Correctness of the shift generator on the situation chain

Let $t < T$, assume the
well-formedness conditions for $N$ situations and stack height $H$, and let $F$ be counter
values satisfying the block-start conditions at time $t$. Then for every $n \le N$, every
output $o$ and every Boolean state $v$, there is a Boolean state $v'$ such that the generator,
started at the entry label of the situation chain for $n$ with state $v$, counters $F$ and
output $o$, reaches in at most $n \cdot (K \cdot B)$ steps the end-of-time-step label with
state $v'$, counters $F$ and output $e_0 e_1 \cdots e_{n-1}$ followed by $o$. Here $K$ is the
number of stacks, $e_i$ is the concatenated encoding of the clause blocks of situation $i$ for
the stacks $0, \dots, K - 1$ at time $t$, and $B$ is the step budget for one block with
$V = (T + 1) W$ variables, $W$ being the number of variables per time step.

Formalized by `Cslib.Complexity.CookLevin.Shift.is_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#is-run).

## Step budget for one time step of the shift generator

Let $L$ be a layout with $K$
stacks, $g$ symbol codes and window depth $d$, let $N, T, H \in \mathbb{N}$, let $V = (T + 1) W$
be the number of variables, $W$ being the number of variables per time step at height $H$, and
let $B$ be the step budget for one block of the shift generator for $g$, $K$, $H$, $d$ and $V$.
The budget is

$$
\bigl(T(2V + 3) + T + 2\bigr) + (2V + 2) + (2V + 2) + N(K B) + (V + 1) + (V + 1).
$$

Formalized by `Cslib.Complexity.CookLevin.Shift.tBodyB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#t-body-b).

## One iteration of the time loop of the shift generator

Let $L$ be a layout with $g$ symbol
codes, let $\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$ be situation tables, let
$N, T, H, t \in \mathbb{N}$ with $t < T$, and suppose the tables are well formed for $N$
situations at height $H$. Write $W$ for the number of variables per time step at height $H$ and
$V = (T + 1) W$ for the number of variables. Let $F$ be counter values of the cell-shift generator
with empty scratch counters, with $\mathrm{Vc} = V$, $\mathrm{Gc} = g$, $\mathrm{Wc} = W$,
$\mathrm{Tn} = t$, $\mathrm{HG} = H g$ and $\mathrm{Hs} = H$, and with $\mathrm{P}$,
$\mathrm{TW}$, $\mathrm{TW1}$, $\mathrm{KB}$, $\mathrm{U}$, $\mathrm{Ui}$, $\mathrm{R}$,
$\mathrm{Ri}$, $\mathrm{Ka}$, $\mathrm{CB}$ and $\mathrm{CW}$ all $0$. Then for every output list
$o$ and every Boolean state $v$ there is a Boolean state $v'$ such that the generator, started at
the label $\mathrm{tw}(\mathrm{head})$ (the first stage of the time-loop multiplication) in state
$v$ with counters $F$ and output $o$, reaches the time-loop head $\mathrm{tHead}$ within at most
the step budget for one time step of the shift generator for $L$, $N$, $T$, $H$, in state $v'$
with counters $F$ and output the encoded blocks of time step $t$ followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.Shift.tbody_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#tbody-run).

## Initial counter values of the shift generator

For natural numbers $T$ and $H$, the
assignment of counter values that puts $T$ on the time-bound input counter, $H$ on the
stack-height input counter, and $0$ on every other counter of the generator.

Formalized by `Cslib.Complexity.CookLevin.Shift.initF`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#init-f).

## Counters after the precomputation of the cell-shift generator

For a layout $L$ with label
block size $A$, $K$ stacks and $g$ symbol codes and numbers $T, H$, the counter values with $T$ on
$\mathrm{Tn}$, $H$ on $\mathrm{Hs}$, $g$ on $\mathrm{Gc}$, $H g$ on $\mathrm{HG}$, the row width
$W = A + K H g$ on $\mathrm{Wc}$, the number of variables $(T + 1) W$ on $\mathrm{Vc}$, and $0$
on every other counter.

Formalized by `Cslib.Complexity.CookLevin.Shift.preF`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#pre-f).

## Cost of the precomputation of the cell-shift generator

For a layout $L$ with label block
size $A$, $K$ stacks and $g$ symbol codes, numbers $T$ and $H$, and the row width
$W = A + K H g$, this is the step bound

$$
1 + (H (2 g + 3) + H + 2) + 1 + 1 + (K (2 H g + 3) + K + 2) + (K + 1) +
(T (2 W + 3) + T + 2) + (2 W + 2).
$$

Formalized by `Cslib.Complexity.CookLevin.Shift.preB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#pre-b).

## Explicit time bound of the shift generator

For a layout $L$ and $N, T, H \in \mathbb{N}$,
the bound is $P + (T(B + 1) + T + 2)$, where $P$ is the cost of the precomputation for $L$, $T$,
$H$ and $B$ is the cost of one iteration of the time loop for $L$, $N$, $T$, $H$.

A separate result bounds it by a constant depending only on $L$ and $N$ times $(T + H + 1)^6$.

Formalized by `Cslib.Complexity.CookLevin.Shift.shBound`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sh-bound).

## Correctness of the shift generator, with its explicit time bound

Let $L$ be a layout, let
$\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$ be situation tables and let
$N, T, H \in \mathbb{N}$, and suppose the tables are well formed for $N$ situations at height
$H$. Start the cell-shift generator for $L$, $\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$,
$\mathrm{pu}$ and $N$ at its first precomputation stage, in state false, with $T$ on the counter
$\mathrm{Tn}$ and $H$ on the counter $\mathrm{Hs}$ in unary, all other counters empty, and an
arbitrary list $o$ of bits on the output stack. Then within at most the explicit time bound of
the shift generator for $L$, $N$, $T$, $H$ steps it reaches its final label $\mathrm{done}$, in
some state, with stacks whose output stack holds the encoding of the cell-shift clause family for
$L$, $\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$, $N$, $T$ and $H$, followed by
$o$.

Formalized by `Cslib.Complexity.CookLevin.Shift.sh_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sh-run).

## Time bound of the shift generator on uniform layouts

Let $k \ge 1$ and $y \ge 1$ be
natural numbers and let $L_k$ be the layout with every constant equal to $k$. Then the explicit
time bound of the shift generator for $L_k$ with $N = k$ situations and $T = H = y$ is at most
$828\, k^7 y^6$.

Every monomial of the bound is then at most $k^7 y^6$, and the coefficients sum to $828$, the
value of the bound at $k = y = 1$.

Formalized by `Cslib.Complexity.CookLevin.Shift.shBound_uni`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sh-bound-uni).

## Constant of the shift-generator time bound

For a layout $L$ with label/state block size
$A$, $K$ stacks, $g$ symbol codes and window depth $d$, and a natural number $N$, the constant is
$828 \cdot (A + K + g + d + N + 1)^7$.

It depends only on $A$, $K$, $g$, $d$ and $N$, not on the time bound $T$ or the height $H$.

Formalized by `Cslib.Complexity.CookLevin.Shift.shC`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sh-c).

## The shift-generator time bound as a polynomial

For a layout $L$ with label/state block
size $A$, $K$ stacks, $g$ symbol codes and window depth $d$, and a natural number $N$, let
$c = 828\,(A + K + g + d + N + 1)^7$ be the constant of the shift-generator time bound; this is
the polynomial $c\,(X + 1)^6$ with natural-number coefficients.

For natural numbers $T$ and $H$, its value at $X = T + H$ is $c\,(T + H + 1)^6$, the bound on
the number of steps of the shift generator started on $T$ and $H$.

Formalized by `Cslib.Complexity.CookLevin.Shift.shPoly`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sh-poly).

## Polynomial time bound for the shift generator

Let $L$ be a layout with label/state block
size $A$, $K$ stacks, $g$ symbol codes and window depth $d$, let $\mathrm{sa}$, $\mathrm{pl}$,
$\mathrm{cn}$, $\mathrm{pu}$ be situation tables and let $N, T, H \in \mathbb{N}$, and suppose
the tables are well formed for $N$ situations at height $H$. Start the cell-shift generator for
$L$, $\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$ and $N$ at its first
precomputation stage, in state false, with $T$ on the counter $\mathrm{Tn}$ and $H$ on the counter
$\mathrm{Hs}$ in unary, all other counters empty, and an arbitrary list $o$ of bits on the output
stack. Then within at most $c\,(T + H + 1)^6$ steps, where $c = 828\,(A + K + g + d + N + 1)^7$
is the constant of the shift-generator time bound for $L$ and $N$, it reaches its final label
$\mathrm{done}$, in some state, with stacks whose output stack holds the encoding of the
cell-shift clause family for $L$, $\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$,
$N$, $T$ and $H$, followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.Shift.sh_time`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Shift.lean, line 1402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Shift.lean#L1402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html#sh-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cook-Levin: generator machine for the cell-shift family](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-cell-shift)
