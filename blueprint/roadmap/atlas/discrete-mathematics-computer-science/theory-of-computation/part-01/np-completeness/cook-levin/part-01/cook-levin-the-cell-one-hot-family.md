---
declaration: section
origin: cited
lean: Cslib.Complexity.CookLevin.OneHot.aloLits, Cslib.Complexity.CookLevin.OneHot.amoLits, Cslib.Complexity.CookLevin.OneHot.rowsCNF, Cslib.Complexity.CookLevin.OneHot.cellCNF, Cslib.Complexity.CookLevin.OneHot.ohFamily, Cslib.Complexity.CookLevin.OneHot.CK, Cslib.Complexity.CookLevin.OneHot.CL, Cslib.Complexity.CookLevin.OneHot.CL.nl
statement: formalized
proof: formalized
---

# Cook-Levin: the cell one-hot family

49 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html).

## The family (pure specification)

## At-least-one literals of a cell

For $g, B \in \mathbb{N}$, the list of the $g$ positive
literals on the variables $v_B, v_{B+1}, \dots, v_{B+g-1}$, in this order, each given as the pair
of its variable index and the sign true; these are the literals of the clause
$v_B \lor \dots \lor v_{B+g-1}$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.aloLits`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#alo-lits).

## At-most-one literals for a pair

For $B, x, y \in \mathbb{N}$, the two-element list of the
negative literals on the variables $v_{B+x}$ and $v_{B+y}$, in this order, each given as the pair of
its variable index and the sign false; these are the literals of the clause
$\neg v_{B+x} \lor \neg v_{B+y}$. It is used for pairs $x < y$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.amoLits`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#amo-lits).

## At-most-one clauses of the first rows of a cell

For natural numbers $V$, $B$ and $y$,
write $p_i$ for the variable with index $i$. This is the CNF formula listing, for
$y' = 0, 1, \dots, y - 1$ in turn and within each for $x = 0, 1, \dots, y' - 1$ in turn, the
dense clause over $V$ variables built from the literals $\lnot p_{B + x}$ and $\lnot p_{B + y'}$:
its slot $i < V$ holds the literal on $p_i$ if there is one and is empty otherwise.

Formalized by `Cslib.Complexity.CookLevin.OneHot.rowsCNF`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#rows-cnf).

## One-hot clauses of a cell

For $g, V, B \in \mathbb{N}$, the CNF formula whose first clause
is the at-least-one clause $v_B \lor \dots \lor v_{B+g-1}$ and whose remaining clauses are the
at-most-one clauses $\neg v_{B+x} \lor \neg v_{B+y}$ for $x < y < g$, ordered by $y$ and then by
$x$. Each clause is written densely over the $V$ variables $v_0, \dots, v_{V-1}$; literals on
variables of index at least $V$ are dropped.

Formalized by `Cslib.Complexity.CookLevin.OneHot.cellCNF`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#cell-cnf).

## The one-hot cell family

Fix a layout with label/state block size $A$, $K$ stacks and
$g$ symbol codes, and bounds $T$ and $H$. Let $W = A + KHg$ be the row width and $V = (T+1)W$
the number of variables $v_0, \dots, v_{V-1}$. For every time $t \le T$, stack $k < K$ and depth
$j < H$, the cell with base $B = tW + A + (kH + j)g$ contributes the at-least-one clause
$v_B \lor \dots \lor v_{B+g-1}$, followed by the at-most-one clauses
$\lnot v_{B+x} \lor \lnot v_{B+y}$ for $x < y < g$, ordered by $y$ and then by $x$. Every clause
is written densely, with one slot for each of the $V$ variables. The family is the CNF formula
listing these clauses, with the cells ordered by $t$, then $k$, then $j$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.ohFamily`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#oh-family).

## Counters of the one-hot generator

The finite type of the nineteen unit counters of the
one-hot clause generator: Tn, Ti, Kc, Kd, Hs, Hi, Gc, HG, Wc, Vc, TW, KB, CB, P, Q, tmp, md,
c1 and c2.

Formalized by `Cslib.Complexity.CookLevin.OneHot.CK`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#ck).

## Clause kinds of a one-hot cell

For a natural number $g$, a clause kind of a cell with
$g$ symbol codes is either the at-least-one kind, or the at-most-one kind of a pair $(x, y)$ of
symbol codes $x, y < g$ (not necessarily ordered).

Formalized by `Cslib.Complexity.CookLevin.OneHot.CL`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#cl).

## Number of literals of a one-hot clause kind

The number of literals of the at-least-one
clause kind of a cell with $g$ symbol codes is $g$, and that of every at-most-one clause kind
$\mathrm{amo}(x, y)$ is $2$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.CL.nl`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#nl).

## Offset of a literal in a one-hot clause

The offset from the cell base of literal $l$ of a
clause kind is $l$ for the at-least-one clause, and for the at-most-one clause
$\mathrm{amo}(x, y)$ it is $x$ when $l = 0$ and $y$ otherwise.

Formalized by `Cslib.Complexity.CookLevin.OneHot.CL.off`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#off).

## Literal sign of a clause kind

For a clause kind $c$ of a cell, $\mathrm{sg}(c)$ is the
sign shared by all literals of $c$: true (positive) for the at-least-one clause and false
(negative) for every at-most-one clause $\mathrm{amo}(x, y)$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.CL.sg`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#sg).

## Well-formed clause kinds

A clause kind of a cell is well formed when it is the
at-least-one clause, or an at-most-one clause $\mathrm{amo}(x, y)$ with $x < y$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.CL.WF`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#wf).

## Stages of the one-hot precomputation

The control labels of the generator's
precomputation, sixteen in all: one each for incrementing the time counter $T_n$, writing the
number $g$ of symbol codes on the counter $G_c$, writing the label/state block size $A$ on the
counter $W_c$ and writing the number $K$ of stacks on the counter $K_c$, and one for each of the
four stages of a multiplication routine in each of the three multiplications
$HG := HG + H_s G_c$, $W_c := W_c + K_c \cdot HG$ and $V_c := V_c + T_n W_c$, where $H_s$ is the
height counter and $HG$ and $V_c$ are further counters of the generator.

Formalized by `Cslib.Complexity.CookLevin.OneHot.PS`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#ps).

## Stages of the one-hot literal routine

The stages of the routine of the one-hot generator
that emits one literal are: two copy stages, the offset stage, the decrement stage, the
comparison stage, for each ordering $o$ (less, equal, greater) two restore stages $r(o)$ and
$r_B(o)$, the gap stage, the failure stage, the slot stage and the drain stage.

Formalized by `Cslib.Complexity.CookLevin.OneHot.LS`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#ls).

## Control labels of the one-hot generator

For a natural number $g$, the labels are: a
precomputation label for each precomputation stage; for the time loop, a head, a rest label, a
multiplication label for each multiplication stage, and an end label; for the stack loop, a
head, a rest label, an emission label, two copy labels, a multiplication label for each
multiplication stage, and an end label; for the depth loop, a head, a rest label, two copy
labels, a multiplication label for each multiplication stage, and a drain label; for each
clause kind $c$ of a cell with $g$ symbol codes, a start label, two copy labels, a literal
label for each literal index $l < g$ and each literal stage, and a finishing label; and a
halting label.

The type is finite: each field ranges over a finite type (a stage, a clause kind of a cell with
$g$ symbol codes, or an index below $g$).

Formalized by `Cslib.Complexity.CookLevin.OneHot.GL`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#gl).

## Entry label of a one-hot literal routine

For a clause kind $c$ of a cell with $g$ symbol
codes and a natural number $l$, the entry label of literal $l$ of $c$ is the first-stage label
of the routine emitting literal $l$ of $c$ if $l < g$, and the halting label otherwise.

The generator never uses it with $l \ge g$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.GL.litL`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#lit-l).

## Label after a literal routine of the one-hot generator

For a clause kind $c$ of a cell
with $g$ symbol codes and an index $l$, the label the generator moves to once literals
$l, l+1, \dots$ of $c$ have been emitted (literals are emitted from the last one down to the
first): if $l = 0$, the final stage of clause $c$, which emits the leading run of empty slots;
otherwise the routine for literal $l - 1$ of $c$, or the halting label when $l - 1 \ge g$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.GL.after`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#after).

## Entry label of an at-most-one clause

Fix a number $g$ of symbol codes. For natural
numbers $x$ and $y$ with $x < y < g$, the generator label at which the emission of the
at-most-one clause for the pair $(x, y)$ of the current cell begins; for any other pair it is the
halting label, a case the generator never uses.

Formalized by `Cslib.Complexity.CookLevin.OneHot.GL.pr`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#pr).

## Entry label for the first rows of a cell

Let $g$ be the number of symbol codes of the
one-hot generator. For a natural number $y$, this is the label of the generator at which the
at-least-one clause starts when $y \le 1$; when $2 \le y \le g$, the label starting the
at-most-one clause for the pair $(y - 2, y - 1)$; and when $y \ge 2$ and $y > g$, the final
label $\mathrm{done}$.

From here, for $y \le g$, the generator emits the clauses of the rows below $y$, then the
at-least-one clause.

Formalized by `Cslib.Complexity.CookLevin.OneHot.GL.yDone`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#y-done).

## One-hot generator: the label after a clause

Let $c$ be a clause kind of a cell with $g$
symbol codes: the at-least-one clause, or the at-most-one clause $\mathrm{amo}(x, y)$ for symbol
codes $x, y < g$. The label the generator goes to after clause $c$ is the end of the cell if $c$
is the at-least-one clause. If $c = \mathrm{amo}(x, y)$ with $x > 0$, it is the start of clause
$\mathrm{amo}(x - 1, y)$ when $x - 1 < y < g$, and the halting label otherwise. If
$c = \mathrm{amo}(0, y)$, it is the start of the at-least-one clause when $y \le 1$, and the start
of clause $\mathrm{amo}(y - 2, y - 1)$ when $y \ge 2$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.GL.nextC`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#next-c).

## One-hot generator: the routine for one literal

Let $L$ be a layout with $g$ symbol codes,
$c$ a clause kind of a cell of $L$ and $l < g$ a literal index, and write $\mathrm{off}_c(l)$ for
the offset of literal $l$ of $c$ from the cell base. The routine for literal $l$ of $c$ is the
following fragment of the one-hot generator for $L$, which acts on unit counters and a Boolean
output stack. It copies the cell base counter $\mathrm{CB}$ onto counter $Q$ (restoring
$\mathrm{CB}$ through the scratch counter $\mathrm{tmp}$) and pushes $\mathrm{off}_c(l)$ more
units onto $Q$, so that $Q = \mathrm{CB} + \mathrm{off}_c(l)$ when $Q$ and $\mathrm{tmp}$ start
empty. Then it repeats: pop one unit from counter $P$, halting if $P$ is empty; compare $P$ with
$Q$ by popping both in step onto the scratch counters $c_1$ and $c_2$, then move those units back;
if $P \ne Q$, prepend the gap block $01$ to the output and repeat. Once $P = Q$, it prepends the
two-bit slot encoding of the sign of $c$ ($10$ if positive, $11$ if negative) to the output,
empties $Q$, and goes to the routine for literal $l - 1$ of $c$, or to the end of clause $c$ when
$l = 0$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.litP`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#lit-p).

## The one-hot generator

For a layout with label/state block size $A$, $K$ stacks and $g$
symbol codes, the program of a counter machine with an output bit stack and the unary counters
of the generator. Started with $T$ on the time counter $T_n$, $H$ on the height counter $H_s$ and
every other counter empty, it first sets $T_n = T + 1$, $G_c = g$, $HG = Hg$,
$W_c = A + K \cdot Hg$, $K_c = K$ and $V_c = (T + 1)W_c$. It then loops over times $t \le T$,
stacks $k < K$ and depths $j < H$; for each cell it computes the cell's base and pushes onto the
output stack the encodings of the cell's dense at-least-one and at-most-one clauses. When the
loops finish it halts.

On halting, the output stack holds the encoding of the one-hot cell family in front of its
original contents.

Formalized by `Cslib.Complexity.CookLevin.OneHot.prog`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#prog).

## The one-hot generator as a finite multi-stack machine

The one-hot generator for a layout,
bundled as a Mathlib multi-stack Turing machine with finitely many stacks, labels and internal
states: its stacks are the output bit stack and one unary counter for each counter of the
generator, its input stack is the time counter and its output stack is the output stack, it
starts at its first precomputation label with internal state false, and it runs the generator's
program.

This bundling only checks the finiteness conditions; the generator also reads the height bound
from the height counter, which a bundled machine with a single input stack does not record.

Formalized by `Cslib.Complexity.CookLevin.OneHot.ohTM`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#oh-tm).

## Literals of a one-hot clause kind

For a cell base $B$ and a clause kind $c$ of a cell
with $g$ symbol codes, the literals of $c$ form a list of pairs (variable, sign): for the
at-least-one kind, the pairs $(B + x, \mathrm{true})$ for $x = 0, \dots, g - 1$ in increasing
order; for the at-most-one kind of the pair $(x, y)$, the two pairs $(B + x, \mathrm{false})$
and $(B + y, \mathrm{false})$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.clits`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#clits).

## Boundary before a literal of a cell clause

For $V, B \in \mathbb{N}$, a clause kind $c$
and an index $l$, the number $B + o_l$ if $l$ is less than the number of literals of $c$, where
$o_l$ is the offset of literal $l$ of $c$ from the cell base, and $V$ otherwise.

Formalized by `Cslib.Complexity.CookLevin.OneHot.bnd`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#bnd).

## Empty scratch counters of the one-hot generator

For an assignment $F$ of a natural number
to each counter of the one-hot generator, $\mathrm{Rest}(F)$ holds when the five scratch counters
$Q$, $\mathit{tmp}$, $\mathit{md}$, $c_1$ and $c_2$ all have value $0$ under $F$.

These are the counters that are empty whenever a clause starts.

Formalized by `Cslib.Complexity.CookLevin.OneHot.Rest`, a structure declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#rest).

## Run of one literal routine (one-hot generator)

Let $L$ be a layout with $g$ symbol
codes, let $c$ be a clause kind of a cell with $g$ symbol codes, let $l < g$ be a literal index
with offset $\mathrm{off}_c(l)$, and let $F$ be counter values of the one-hot generator whose
scratch counters $Q$, $\mathrm{tmp}$, $\mathrm{md}$, $c_1$, $c_2$ are $0$. Let
$q, \gamma \in \mathbb{N}$ with $q = F(\mathrm{CB}) + \mathrm{off}_c(l)$ and
$F(P) = q + \gamma + 1$. Then for every output $o$ and flag $v$, the one-hot generator for $L$
runs in at most $\gamma(3q + 6) + 2F(\mathrm{CB}) + 4q + 9$ steps from the first stage of the
routine for literal $l$ of $c$, with flag $v$, counters $F$ and output $o$, to the label after
literal $l$ of $c$ (the routine for literal $l - 1$, or the final stage of $c$ if $l = 0$), with
flag false, counters $F$ except $P = q$, and output $s \cdot (01)^{\gamma} \cdot o$, where $s$ is
the two-bit slot code of the sign of $c$ ($10$ if positive, $11$ if negative).

Formalized by `Cslib.Complexity.CookLevin.OneHot.lit_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#lit-run).

## Per-literal step cost of the one-hot generator

For a natural number $V$, the cost of
emitting one literal, apart from the gap loop, is $6V + 9$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.litE`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#lit-e).

## Step budget for one one-hot clause

For natural numbers $g$ and $V$, the step budget for
one clause is $V(3V + 6) + g(6V + 9) + 3V + 4$, where $6V + 9$ is the per-literal cost apart
from the gap loop.

Formalized by `Cslib.Complexity.CookLevin.OneHot.clauseB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#clause-b).

## Run of the literal routines of a clause (one-hot generator)

Let $L$ be a layout with $g$
symbol codes, let $c$ be a well-formed clause kind of a cell with $g$ symbol codes (the
at-least-one clause, or the at-most-one clause $\mathrm{amo}(x, y)$ with $x < y$) with $n$
literals, write $\mathrm{off}_c(l)$ for the offset of literal $l$ of $c$ from the cell base, and
let $B, V \in \mathbb{N}$ with $B + g \le V$. For $l \le n$ let $b_l$ be
$B + \mathrm{off}_c(l)$ if $l < n$ and $V$ otherwise, let $\lambda_l$ be the list of literals of
$c$ at base $B$ (position and sign) from index $l$ on, and let the label after literal $l$ be the
routine for literal $l - 1$ of $c$, or the final stage of $c$ if $l = 0$. Write $E(a, \lambda)$
for the gap encoding of $\lambda$ from slot $a$ to $V$. Let $F$ be counter values of the one-hot
generator whose scratch counters $Q$, $\mathrm{tmp}$, $\mathrm{md}$, $c_1$, $c_2$ are $0$ and
with $F(\mathrm{CB}) = B$, and let $o$ be an output. Then for every $l \le n$ and flag $v$ there
is a flag $v'$ such that the one-hot generator for $L$ runs in at most $b_l(3V + 6) + l(6V + 9)$
steps from the label after literal $l$ of $c$, with flag $v$, counters $F$ except $P = b_l$ and
output $E(b_l, \lambda_l) \cdot 00 \cdot o$, to the final stage of $c$, with flag $v'$, counters
$F$ except $P = b_0$ and output $E(b_0, \lambda_0) \cdot 00 \cdot o$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.lits_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#lits-run).

## One clause of the one-hot generator

Let $L$ be a layout with $g$ symbol codes, let $c$
be a well-formed clause kind of a cell (the pair of an at-most-one kind is increasing), and let
$B$ and $V$ be natural numbers with $B + g \le V$. Let $F$ be counter values whose scratch
counters $Q$, $\mathrm{tmp}$, $\mathrm{md}$, $c_1$, $c_2$ are zero, whose cell-base counter
$\mathrm{CB}$ holds $B$, whose variable counter $\mathrm{Vc}$ holds $V$, and whose position
counter $P$ is zero. Then for every output word $o$ and every machine state $v$, the generator
of $L$ runs in at most $V(3V + 6) + g(6V + 9) + 3V + 4$ steps from the label that starts
clause $c$, with state $v$, counters $F$ and output $o$, to the label that follows clause $c$,
with state false, the same counters $F$, and output the encoding of the dense clause over $V$
variables whose literals are those of $c$ in the cell with base $B$, followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.clause_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#clause-run).

## Generator run over one row of at-most-one clauses

Let $L$ be a layout with $g$ symbol
codes, let $V$ and $B$ be natural numbers with $B + g \le V$, write $p_i$ for the variable with
index $i$, and let $F$ assign a value to each counter of the one-hot generator such that the
scratch counters are empty ($\mathrm{Rest}(F)$), $F(CB) = B$, $F(Vc) = V$ and $F(P) = 0$. Let
$y < g$, let $\beta = V(3V + 6) + g(6V + 9) + 3V + 4$ be the step budget of one clause, and for
$x' < y$ let $e_{x'}$ be the encoding of the dense clause over $V$ variables whose only literals
are $\lnot p_{B + x'}$ and $\lnot p_{B + y}$. Then for every $x < y$, every output list $o$ and
every flag $v$, the one-hot generator of $L$, started at the label of the at-most-one clause for
the pair $(x, y)$ with flag $v$, output stack $o$ and each counter $c$ holding $F(c)$, reaches
within $(x + 1) \beta$ steps the label $\mathrm{yDone}(y)$ (Y Done) with flag false, the same
counters, and output stack $e_0 e_1 \cdots e_x \, o$ (concatenation).

Formalized by `Cslib.Complexity.CookLevin.OneHot.row_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 454](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L454). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#row-run).

## Generator run over the first rows and the at-least-one clause

Let $L$ be a layout with
$g$ symbol codes, let $V$ and $B$ be natural numbers with $B + g \le V$, write $p_i$ for the
variable with index $i$, and let $F$ assign a value to each counter of the one-hot generator such
that the scratch counters are empty ($\mathrm{Rest}(F)$), $F(CB) = B$, $F(Vc) = V$ and
$F(P) = 0$. Let $\beta = V(3V + 6) + g(6V + 9) + 3V + 4$ be the step budget of one clause, and
for $y \le g$ let $e_y$ be the encoding of the CNF formula whose first clause is the dense clause
over $V$ variables with the positive literals $p_B, \dots, p_{B + g - 1}$, followed by the
at-most-one clauses of the rows $y' < y$ with base $B$ over $V$ variables (Rows CNF). Then for
every $y \le g$, every output list $o$ and every flag $v$, the one-hot generator of $L$, started
at the label $\mathrm{yDone}(y)$ (Y Done) with flag $v$, output stack $o$ and each counter $c$
holding $F(c)$, reaches within $(1 + y^2) \beta$ steps the label $\mathrm{jd}$ (which drains
$CB$) with flag false, the same counters, and output stack $e_y \, o$ (concatenation).

Formalized by `Cslib.Complexity.CookLevin.OneHot.rows_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#rows-run).

## Step bound for one cell

For $g, H, V \in \mathbb{N}$, the number
$2V + 2 + (H(2g + 3) + H + 2) + (1 + g^2)\, b + V + 1$, where $b$ is the step bound for one
clause for $g$ and $V$. It bounds the steps of one iteration of the one-hot generator's loop over
cell depths.

Formalized by `Cslib.Complexity.CookLevin.OneHot.cellB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#cell-b).

## Generator run for one cell

Let $L$ be a layout with $g$ symbol codes and let $j < H$, $V$
and $B$ be natural numbers. Let $F$ be counter values of the one-hot generator with the scratch
counters $Q$, tmp, md, $c_1$, $c_2$ empty, the counters $CB$ and $P$ zero, $Vc = V$, $Gc = g$,
$Hs = j$, $j g + KB = B$, and suppose $B + g \le V$. Then for every output $o$ and flag $v$, the
generator goes, in at most the one-cell step bound for $g$, $H$, $V$ steps, from the start of the
body of the depth loop with flag $v$, counters $F$ and output $o$ to the head of the depth loop
with flag false, counters $F$ and output the encoding of the one-hot clauses of the cell with
base $B$ over $V$ variables followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.cell_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#cell-run).

## Encoded one-hot clauses of one stack at one time step

For a layout $L$ with $g$ symbol
codes, natural numbers $T, H$, a time step $t$ and a stack $k$, the concatenation over
$j = 0, \dots, H - 1$ of the bit encodings of the one-hot clauses of the cell whose base is the
cell variable of $L$ for stack $k$, depth $j$, symbol code $0$ at time $t$, written densely over
the $V$ variables of $L$ for $T$ and $H$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.blkK`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 585](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L585). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#blk-k).

## Encoded one-hot clauses of one time step

For a layout $L$ with $K$ stacks, natural
numbers $T, H$ and a time step $t$, the concatenation over the stacks $k = 0, \dots, K - 1$ of the
encoded one-hot clauses of stack $k$ at time step $t$ (for $T$ and $H$).

Formalized by `Cslib.Complexity.CookLevin.OneHot.blkT`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 589](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L589). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#blk-t).

## Step budget for one stack iteration of the one-hot generator

For natural numbers $g$,
$K$, $H$ and $V$, let $c = V(3V + 6) + g(6V + 9) + 3V + 4$ be the step budget for one clause
and $C = 2V + 2 + (H(2g + 3) + H + 2) + (1 + g^2)c + V + 1$ the step budget for one cell. The
budget is $1 + (2V + 2) + (K(2Hg + 3) + K + 2) + (H(C + 1) + H + 2) + V + 1$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.kBodyB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 592](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L592). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#k-body-b).

## One stack iteration of the one-hot generator

Let $L$ be a layout with $g$ symbol codes,
$K$ stacks and a label/state block of size $A$, let $T$, $H$, $t$, $k$ be natural numbers with
$t \le T$ and $k < K$, let $W = A + KHg$ be the row width of $L$ at height $H$, and let
$V = (T + 1)W$ be the number of variables. For $j < H$ let $B_j = tW + A + (kH + j)g$ be the
base of the cell at time $t$, stack $k$ and depth $j$, and let $w_j$ be the encoding of the
dense clause over $V$ variables with literals $(B_j + x, \mathrm{true})$ for
$x = 0, \dots, g - 1$ in increasing order, followed by the encodings of the dense clauses over
$V$ variables with literals $(B_j + x, \mathrm{false})$ and $(B_j + y, \mathrm{false})$ for all
pairs $x < y < g$, ordered by $y$ and then by $x$. Let $F$ be counter values whose scratch
counters $Q$, $\mathrm{tmp}$, $\mathrm{md}$, $c_1$, $c_2$ are zero, with
$\mathrm{CB} = P = \mathrm{KB} = \mathrm{Hi} = 0$, $\mathrm{Vc} = V$, $\mathrm{Gc} = g$,
$\mathrm{HG} = Hg$, $\mathrm{Hs} = H$, $\mathrm{TW} = tW$ and $\mathrm{Kc} = k$. Then for every
output word $o$ and every machine state $v$, the generator of $L$ runs within the
one-stack-iteration step budget at $(g, K, H, V)$ from the label that starts the body of the
stack loop, with state $v$, counters $F$ and output $o$, to the head of the stack loop, with
state false, the same counters $F$, and output $w_0 w_1 \cdots w_{H-1}$ followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.kbody_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 596](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L596). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#kbody-run).

## Step budget for one time step of the one-hot generator

Let $L$ be a layout with $A$
label/state variables per row, $K$ stacks and $g$ symbol codes, let $T$ and $H$ be natural
numbers, $W = A + K H g$ the row width and $V = (T + 1) W$ the number of variables, and let
$\kappa$ be the step budget of one iteration of the $k$ loop for $g$, $K$, $H$ and $V$. The
budget is $T(2W + 3) + T + 2 + \bigl(K(\kappa + 1) + K + 2\bigr) + V + 1$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.tBodyB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 636](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L636). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#t-body-b).

## Generator run over one time step

Let $L$ be a layout with $A$ label/state variables per
row, $K$ stacks and $g$ symbol codes, let $t \le T$ and $H$ be natural numbers, and write
$W = A + K H g$ for the row width, $V = (T + 1) W$ for the number of variables and $p_i$ for the
variable with index $i$. Let $F$ assign a value to each counter of the one-hot generator such
that the scratch counters are empty ($\mathrm{Rest}(F)$),
$F(CB) = F(P) = F(KB) = F(TW) = F(Hi) = F(Kd) = 0$, $F(Vc) = V$, $F(Gc) = g$, $F(HG) = H g$,
$F(Hs) = H$, $F(Wc) = W$, $F(Kc) = K$ and $F(Tn) = t$. For $k < K$ and $j < H$ let
$b_{k,j} = t W + A + (k H + j) g$ be the base of cell $(k, j)$, and let $E_{k,j}$ be the encoding
of the CNF formula consisting of the dense clause over $V$ variables with the positive literals
$p_{b_{k,j}}, \dots, p_{b_{k,j} + g - 1}$, followed, for $y = 0, \dots, g - 1$ in turn and within
each for $x = 0, \dots, y - 1$ in turn, by the dense clause over $V$ variables whose only literals
are $\lnot p_{b_{k,j} + x}$ and $\lnot p_{b_{k,j} + y}$. Let $E$ be the concatenation of the
$E_{k,j}$ for $k = 0, \dots, K - 1$ and within each for $j = 0, \dots, H - 1$. Then for every
output list $o$ and every flag $v$, the one-hot generator of $L$, started at the first label of
the stage computing $TW := t W$ with flag $v$, output stack $o$ and each counter $c$ holding
$F(c)$, reaches within the time-step budget of $L$, $T$ and $H$ (T Body B) steps the head of the
time loop with flag false, the same counters, and output stack $E \, o$ (concatenation).

Formalized by `Cslib.Complexity.CookLevin.OneHot.tbody_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#tbody-run).

## Initial counters of the one-hot generator

For natural numbers $T$ and $H$, the initial
counter values are $T$ on the counter $\mathrm{Tn}$, $H$ on the counter $\mathrm{Hs}$, and $0$
on every other counter.

Formalized by `Cslib.Complexity.CookLevin.OneHot.initF`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 675](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L675). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#init-f).

## Counter values after the one-hot precomputation

For a layout with label/state block size
$A$, $K$ stacks and $g$ symbol codes, and bounds $T$ and $H$, let $W = A + KHg$. After the
precomputation the generator's counters hold $T_n = T + 1$, $H_s = H$, $G_c = g$, $HG = Hg$,
$W_c = W$, $K_c = K$ and $V_c = (T + 1)W$, and every other counter holds $0$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.preF`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 681](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L681). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#pre-f).

## Step budget of the one-hot precomputation

For a layout with label/state block size $A$,
$K$ stacks and $g$ symbol codes, bounds $T$ and $H$, and row width $W = A + KHg$, the number of
steps allotted to the generator's precomputation is
$4 + (H(2g + 3) + H + 2) + (K(2Hg + 3) + K + 2) + ((T + 1)(2W + 3) + (T + 1) + 2)$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.preB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 692](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L692). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#pre-b).

## Explicit time bound of the one-hot generator

For a layout $L$ and natural numbers $T$ and
$H$, the explicit time bound of the one-hot generator is $p + (T + 1)(b + 1) + (T + 1) + 2$,
where $p$ is the cost of its precomputation and $b$ the cost of one iteration of its time loop,
both for $L$, $T$ and $H$.

This bound is at most $668\,(A + K + g + 1)^7 (T + H + 1)^6$, where $A$ is the label block size,
$K$ the number of stacks and $g$ the number of symbol codes of $L$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.ohBound`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 697](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L697). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#oh-bound).

## Correctness of the one-hot generator, with its explicit time bound

Fix a layout, natural
numbers $T$ and $H$, and a bit string $o$. Start the one-hot generator at its first
precomputation label, with internal state false, the output stack holding $o$, the time counter
holding $T$ and the height counter holding $H$ in unary, and every other counter empty. Then
within $\beta(T, H)$ steps, where $\beta$ is the generator's explicit step bound, it reaches its
halting label, in some internal state, with the output stack holding the encoding of the one-hot
cell family for $T$ and $H$ followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.oh_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 706](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L706). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#oh-run).

## Time bound of the one-hot generator on a uniform layout

For all natural numbers $k \ge 1$
and $y \ge 1$, the explicit time bound of the one-hot generator for the layout whose label block
size, number of stacks, number of symbol codes and window depth all equal $k$, with $T = H = y$,
is at most $668\, k^7 y^6$.

Every monomial of the bound is at most $k^7 y^6$, and the coefficients sum to $668$, the value
of the bound at $k = y = 1$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.ohBound_uni`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 758](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L758). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#oh-bound-uni).

## Constant of the one-hot time bound

For a layout $L$ with label block size $A$, $K$ stacks
and $g$ symbol codes, the constant of the one-hot generator's time bound is
$668\,(A + K + g + 1)^7$; it does not depend on the window depth of $L$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.ohC`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 801](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L801). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#oh-c).

## The one-hot time bound as a polynomial

For a layout with label/state block size $A$, $K$
stacks and $g$ symbol codes, let $c = 668\,(A + K + g + 1)^7$; this is the polynomial
$c\,(X + 1)^6$ with natural-number coefficients. For natural numbers $T$ and $H$, its value at
$X = T + H$ is $c\,(T + H + 1)^6$, the bound on the number of steps of the one-hot generator
started on $T$ and $H$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.ohPoly`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 814](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L814). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#oh-poly).

## Polynomial time bound for the one-hot generator

Fix a layout with label/state block size
$A$, $K$ stacks and $g$ symbol codes, natural numbers $T$ and $H$, and a bit string $o$, and let
$c = 668\,(A + K + g + 1)^7$. Start the one-hot generator at its first precomputation label, with
internal state false, the output stack holding $o$, the time counter holding $T$ and the height
counter holding $H$ in unary, and every other counter empty. Then within $c\,(T + H + 1)^6$
steps it reaches its halting label, in some internal state, with the output stack holding the
encoding of the one-hot cell family for $T$ and $H$ followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.OneHot.oh_time`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/OneHot.lean, line 820](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/OneHot.lean#L820). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html#oh-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cook-Levin: the cell one-hot family](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-cell-one-hot-family)
