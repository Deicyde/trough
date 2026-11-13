---
declaration: section
origin: cited
lean: Cslib.Turing.Universal.Clocked.cell, Cslib.Turing.Universal.Clocked.cells, Cslib.Turing.Universal.Clocked.K, Cslib.Turing.Universal.Clocked.Lab, Cslib.Turing.Universal.Clocked.Γ, Cslib.Turing.Universal.Clocked.dU, Cslib.Turing.Universal.Clocked.mark, Cslib.Turing.Universal.Clocked.prog
statement: formalized
proof: formalized
---

# Clocked universal Turing machine

37 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html).

## The cell of a number

The cell of a natural number $n$ is the list of bits consisting of
$n$ copies of the bit true (units) followed by one bit false (a marker).

Formalized by `Cslib.Turing.Universal.Clocked.cell`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#cell).

## The cells of a list of numbers

The cells of a list $(n_1, \ldots, n_m)$ of natural numbers
are the concatenation of the cells of $n_1, \ldots, n_m$ in this order, so that the cell of $n_1$
comes first (on top of a stack).

Formalized by `Cslib.Turing.Universal.Clocked.cells`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#cells).

## Stacks of the clocked universal machine

The clocked universal machine has fifteen
stacks: the state $Q$, the next state $N$, the action $A$ and the head cell $H$ (these four hold
counters of units), the cells left ($L$) and right ($R$) of the head, the code $C$, the scan
buffer $B$, the scratch counters $T$, $U$, $V$, the clock $\mathrm{Ck}$, and the parsing stacks:
the encoded input $X$, the parse buffer $P$ and the output $O$.

Formalized by `Cslib.Turing.Universal.Clocked.K`, an inductive type declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#k).

## Labels of the clocked universal machine

The labels of the program of the clocked
universal machine: the tape update (`act0`–`act3`, `wr0`, `wr1`, `mvL0`–`mvL3`, `mvR0`–`mvR3`)
and the clock tick `fin`; the scan, which starts at `sc0` and has labels for the state
(`rq0`–`rq2`; `cqA o` and `cqB o` for each comparison outcome `o`; `sq0 m` and `sq1 m` for each
bit `m`), for the head cell (`ra0`–`ra2`; `caA o`, `caB o`; `sa0 m`, `sa1 m`), for skipping the
rest of an entry (`sk3a`, `sk3b`, `sk2a`, `sk2b`, `sk1a`, `sk1b`) and for reading a match
(`rd0`–`rd7`); the restores `rs` and `nf`; the exits `hlt` and `tmo`; the parse of the encoded
input (`pc0`, `pc1`, `px0`–`px6`, `pk0`); and the output phase (`o1`–`o6`, `done`).

Formalized by `Cslib.Turing.Universal.Clocked.Lab`, an inductive type declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#lab).

## Stack alphabet of the clocked universal machine

Every stack $k$ of the clocked universal
machine holds bits: its alphabet is $\Gamma(k) = \mathrm{Bool}$.

Formalized by `Cslib.Turing.Universal.Clocked.Γ`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#untitled).

## Decoding units

The unit decoder sends the bit true (a unit) to the bit true, and sends
the bit false (a marker) to no bit, which ends a block.

Formalized by `Cslib.Turing.Universal.Clocked.dU`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#d-u).

## Moving a marker onto the scan buffer

For a label $\ell$, this instruction pops the top
symbol of the code stack $C$ and discards it (doing nothing if $C$ is empty), pushes a marker (the
bit false) onto the scan buffer $B$, and goes to $\ell$; the state bit is unchanged.

Formalized by `Cslib.Turing.Universal.Clocked.mark`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#mark).

## The clocked universal program

The program of the clocked universal machine gives an
instruction for every label. Numbers sit on stacks as counters of units (the bit true), and a cell
is a counter followed by a marker (the bit false).

Tape update. $\mathsf{act0}$ empties $Q$ and $\mathsf{act1}$ moves the counter $N$ onto $Q$.
$\mathsf{act2}$ pops $A$ and goes to $\mathsf{mvL0}$ if $A$ was empty, else to $\mathsf{act3}$,
which pops $A$ and goes to $\mathsf{mvR0}$ if $A$ was empty, else to $\mathsf{wr0}$; so the action
$0$ moves left, $1$ moves right and $a + 2$ writes $a$. $\mathsf{wr0}$ empties $H$ and
$\mathsf{wr1}$ moves the counter $A$ onto $H$. A left move ($\mathsf{mvL0}$ to $\mathsf{mvL3}$)
pushes a marker on $R$, moves the units of $H$ onto $R$, moves the units on top of $L$ onto $H$
and pops one more symbol of $L$; a right move ($\mathsf{mvR0}$ to $\mathsf{mvR3}$) does the same
with $L$ and $R$ exchanged. Writes and moves end at $\mathsf{fin}$, which pops the clock $Ck$ and
goes to $\mathsf{tmo}$ if it was empty, else to $\mathsf{sc0}$.

Scan. $\mathsf{sc0}$ goes to $\mathsf{nf}$ if $C$ is empty, else to $\mathsf{rq0}$. Then
$\mathsf{rq0}$, $\mathsf{rq1}$ move the units on top of $C$ onto $T$ and pop the next symbol of
$C$; $\mathsf{rq2}$ compares $T$ with $Q$ unit by unit, parking the popped units on $U$ and $V$;
$\mathsf{cqA}$, $\mathsf{cqB}$ move $U$ back onto $T$ and $V$ back onto $Q$; $\mathsf{sq0}$,
$\mathsf{sq1}$ move $T$ onto $B$, push a marker on $B$, and go to $\mathsf{ra0}$ if the two
counters were equal, else to $\mathsf{sk3a}$. The labels $\mathsf{ra0}$ to $\mathsf{sa1}$ do the
same with $H$ in place of $Q$, and go to $\mathsf{rd0}$ on equality, else to $\mathsf{sk2a}$.
From $\mathsf{sk3a}$, $\mathsf{sk2a}$ or $\mathsf{sk1a}$ the program moves three, two or one
further cells of $C$ onto $B$ (the units, then the next symbol replaced by a marker) and returns
to $\mathsf{sc0}$. The labels $\mathsf{rd0}$ to $\mathsf{rd3}$ move the units on top of $C$ onto
both $N$ and $B$, pop the next symbol of $C$ and push a marker on $B$; $\mathsf{rd4}$ to
$\mathsf{rd7}$ do the same with $A$ in place of $N$ and go to $\mathsf{rs}$. Finally
$\mathsf{rs}$ and $\mathsf{nf}$ move all of $B$ back onto $C$, one symbol at a time, and go to
$\mathsf{act0}$ and $\mathsf{hlt}$ respectively.

Parse. $\mathsf{pc0}$, $\mathsf{pc1}$ move the units on top of $X$ onto $Ck$ and pop the next
symbol of $X$. Then, while the top of $X$ is a unit, $\mathsf{px0}$ to $\mathsf{px2}$ move the
units on top of $X$ onto $P$, pop the next symbol of $X$ and push a marker on $P$; otherwise
$\mathsf{px3}$ pops $X$, $\mathsf{px4}$ moves all of $P$ onto $R$, $\mathsf{px5}$, $\mathsf{px6}$
move the units on top of $R$ onto $H$ and pop the next symbol of $R$, and $\mathsf{pk0}$ moves all
of $X$ onto $C$ and goes to $\mathsf{sc0}$.

Exits. $\mathsf{tmo}$ pushes a marker on $O$ and goes to $\mathsf{done}$. $\mathsf{hlt}$ pushes a
marker on $R$, $\mathsf{o1}$ moves the units of $H$ onto $R$, $\mathsf{o2}$ moves all of $R$ onto
$P$, $\mathsf{o3}$ pops the markers on top of $P$, $\mathsf{o4}$ pushes one marker on $P$ unless
$P$ is empty, $\mathsf{o5}$ moves all of $P$ onto $O$, and $\mathsf{o6}$ pushes a unit on $O$ and
goes to $\mathsf{done}$, where the program halts.

Formalized by `Cslib.Turing.Universal.Clocked.prog`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#prog).

## Entries of a code

For a code $c$, the list of quadruples $(q, a, q', s)$, one for each
state $q$ and symbol $a$ inside the table of $c$ whose table entry is a transition $(q', s)$
(enter the state $q'$ and do the action coded by $s$); halting positions are skipped. The
quadruples are listed row by row, by increasing $q$, and within a row by increasing $a$.

Formalized by `Cslib.Turing.Universal.Clocked.entries`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#entries).

## Looking up a key in a list of entries

For natural numbers $q$ and $a$ and a list of
quadruples $(q_i, a_i, q'_i, s_i)$ of natural numbers, the result is the pair $(q'_i, s_i)$ of
the first quadruple in the list with $q_i = q$ and $a_i = a$, and no result if no quadruple has
the key $(q, a)$. This is the order in which the machine scans the code stack.

Formalized by `Cslib.Turing.Universal.Clocked.findEntry`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#find-entry).

## Scanning the entries finds the table entry

For every code $c$ and all natural numbers
$q$ and $a$, looking up the key $(q, a)$ in the entries of $c$ gives the entry of the table of
$c$ at state $q$ and symbol $a$: the pair $(q', s)$ if that position holds the transition
$(q', s)$, and no result if it halts, including every position outside the table.

Formalized by `Cslib.Turing.Universal.Clocked.findEntry_entries`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#find-entry-entries).

## Numbers of a list of entries

For a list of quadruples of natural numbers, the list of
natural numbers obtained by replacing each quadruple $(q, a, q', s)$ by the four numbers
$q, a, q', s$ in this order, keeping the order of the quadruples.

Formalized by `Cslib.Turing.Universal.Clocked.entryNums`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#entry-nums).

## The code stack

The code stack of a code $c$ is the list of bits formed by the cells of the
numbers $q, a, q', s$ of every entry $(q, a, q', s)$ of $c$ (a table position $(q, a)$ holding the
transition $(q', s)$), with the entries ordered by $q$ and then by $a$, and the four numbers of an
entry in the order $q, a, q', s$.

Formalized by `Cslib.Turing.Universal.Clocked.codeCells`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#code-cells).

## The stacks of a simulated configuration

For a code $c$, a natural number $t$ (the clock),
a configuration $k$ and natural numbers $q'$ and $s$, the stacks of $c$, $t$ and $k$ with next
state $q'$ and action $s$ hold, as counters of units (the bit true): the state of $k$ on $Q$, $q'$
on $N$, $s$ on $A$, the head symbol of $k$ on $H$ and $t$ on $Ck$. The stacks $L$ and $R$ hold the
cells of the symbols left and right of the head, nearest first, $C$ holds the code stack of $c$,
and every other stack is empty.

Formalized by `Cslib.Turing.Universal.Clocked.stk`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#stk).

## Step bound of the tape update

For a configuration $k$ with state $q$, head cell $h$,
cells $\ell$ left of the head and cells $r$ right of the head (nearest first), a next state $q'$
and an action $s$, the step bound of the tape update is $q + q' + s + h + \ell_0 + r_0 + 8$, where
$\ell_0$ and $r_0$ are the first entries of $\ell$ and $r$, taken to be $0$ for an empty list.

Formalized by `Cslib.Turing.Universal.Clocked.actTime`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#act-time).

## The tape update

Let $c$ be a code, $k$ a configuration and $t$, $q'$, $s$ natural
numbers. Started at the label $\mathsf{act0}$, with any value of its internal variable, on the
stacks holding the code $c$, the clock $t$ and the configuration $k$, with $q'$ on the next-state
stack, $s$ on the action stack and all other stacks empty, the program of the clocked universal
machine reaches the label $\mathsf{fin}$, with some value of its internal variable, on the stacks
holding $c$, $t$ and the configuration obtained from $k$ by entering the state $q'$ and doing the
action coded by $s$, with the next-state, action and all other stacks empty. It does so in at
most as many steps as the step bound of the tape update for $k$, $q'$ and $s$.

Formalized by `Cslib.Turing.Universal.Clocked.act_run`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 491](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L491). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#act-run).

## Cost of scanning past one entry

The step budget for scanning past an entry
$(q, a, q', s)$ of the code stack is $5q + 5a + 2q' + 2s + 30$.

Formalized by `Cslib.Turing.Universal.Clocked.entryCost`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 664](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L664). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#entry-cost).

## Step bound of one simulated step

For a code $c$ and a configuration $k$ with state $q$,
head cell $h$, nearest left cell $l$ and nearest right cell $r$ (each read as the blank $0$ when
there is no such cell), let $|C|$ be the length of the code stack of $c$. The step bound of $c$
at $k$ is $10|C| + q + h + l + r + 10$.

Formalized by `Cslib.Turing.Universal.Clocked.stepTime`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 850](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L850). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#step-time).

## One simulated step, running case

Let $c$ be a code, $k$ and $k'$ configurations such that
one step of $c$ from $k$ gives $k'$, $t$ a natural number, $v$ a bit, and $b$ the step bound of
$c$ at $k$. Started at the label $\mathsf{sc0}$ with state bit $v$ and the stacks of the code $c$,
the clock $t$ and the configuration $k$ with next state and action $0$, the clocked universal
program reaches the label $\mathsf{fin}$ within $b$ steps, with some state bit and the stacks of
$c$, $t$ and $k'$ with next state and action $0$.

Formalized by `Cslib.Turing.Universal.Clocked.step_run_of_step_eq_some`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 870](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L870). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#step-run-of-step-eq-some).

## One simulated step, halting case

Let $c$ be a code, $k$ a configuration at which $c$ halts
(one step of $c$ from $k$ gives nothing), $t$ a natural number, $v$ a bit, and $b$ the step bound
of $c$ at $k$. Started at the label $\mathsf{sc0}$ with state bit $v$ and the stacks of the code
$c$, the clock $t$ and the configuration $k$ with next state and action $0$, the clocked universal
program reaches the label $\mathsf{hlt}$ within $b$ steps, with some state bit and the same
stacks.

Formalized by `Cslib.Turing.Universal.Clocked.step_run_of_step_eq_none`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 899](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L899). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#step-run-of-step-eq-none).

## Configurations bounded by $M$

A configuration $k$ is bounded by a natural number $M$
when its state, its head cell and every cell left and right of the head are at most $M$.

Formalized by `Cslib.Turing.Universal.Clocked.Bounded`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 927](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L927). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#bounded).

## Step bound of the clocked loop

For a code $c$ and a number $M$, the loop step time is
$10\ell + 4M + 11$, where $\ell$ is the length of the code stack of $c$. It serves as the cost
bound of one round of the loop (a simulated step and a clock tick) on configurations whose numbers
are at most $M$.

Formalized by `Cslib.Turing.Universal.Clocked.loopStepTime`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 968](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L968). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#loop-step-time).

## The clocked loop

Let $c$ be a code, let $M$ be at least the length of the code stack of
$c$, let $k$ be a configuration whose state and cells are all at most $M$, let $t$ be a natural
number and $v$ a bit, and let $k_t$ be the result of $t$ steps of $c$ from $k$, where a halted
configuration stays put. Start the program of the clocked universal machine at label `sc0` with
variable $v$ and the stacks of $c$, the clock $t$ and $k$ (next state and action $0$). If $k_t$
has halted, then within $(t + 1) \cdot L(c, M)$ steps, where $L(c, M)$ is the loop step time,
the program reaches label `hlt` with some variable and the stacks of $c$, some clock $t'$ and
$k_t$ (next state and action $0$). If instead $c$ steps $k_t$ to $k''$, then within the same
number of steps it reaches label `tmo` with some variable and the stacks of $c$, the clock $0$
and $k''$ (next state and action $0$).

Formalized by `Cslib.Turing.Universal.Clocked.loop_run`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 988](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L988). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#loop-run).

## Step bound of the clocked simulation

For a code $c$ and a clock $T$, let $|C|$ be the
length of the code stack of $c$. The step bound of the clocked simulation on the clock $T$ is
$T + 1$ times the cost of one round of the loop on configurations whose numbers are at most
$|C| + 2$, that is, $(T + 1)(14|C| + 19)$.

Formalized by `Cslib.Turing.Universal.Clocked.clockTime`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 1049](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L1049). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#clock-time).

## The clocked universal machine on stacks

Let $c$ be a code, $x$ a list of bits and $T$ a
natural number, and let $|C|$ be the length of the code stack of $c$. Start the program of the
clocked universal machine at the label $\mathsf{sc0}$, with any value of its internal variable,
on the stacks holding the code $c$, the clock $T$ and the initial configuration on $x$, all other
stacks empty. If the clocked evaluation of $c$ on $x$ for $T$ steps is defined, the machine
reaches the label $\mathsf{hlt}$ on the stacks holding $c$, some clock $t'$ and the configuration
of $c$ after $T$ steps on $x$; otherwise it reaches the label $\mathsf{tmo}$ on the stacks holding
$c$, the clock $0$ and some configuration. In both cases the internal variable ends with some
value, all other stacks are empty, and the run takes at most $(T + 1)(14|C| + 19)$ steps, the
step bound of the clocked machine on the clock $T$.

When the clocked evaluation is defined, its value is the output of the configuration of $c$ after
$T$ steps on $x$.

Formalized by `Cslib.Turing.Universal.Clocked.clocked_run`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 1056](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L1056). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#clocked-run).

## Input encoding of the clocked universal machine

For a code $c$, a list of bits $x$ and a
clock $T$, the input of the clocked universal machine is the list of bits formed by the cell of
$T$, then the cells of the input word of $x$, then the cell of $0$ (a blank cell, the single bit
false), then the code stack of $c$ in reverse order.

Formalized by `Cslib.Turing.Universal.Clocked.encIn`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 1176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L1176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#enc-in).

## Cost of reading the input

For a code $c$, a list of bits $x$ and a natural number $T$, let
$w_1, \dots, w_n$ be the input word of $x$ (false as the symbol $1$, true as $2$), with $w_1$ read
as $0$ when $x$ is empty, let $S_j = \sum_{i=1}^{n} (w_i + j)$, and let $m$ be the length of the
code stack of $c$. The cost of reading the input is
$T + 2 + (S_3 + 2) + (S_1 + 1) + (w_1 + 2) + (m + 1)$.

Formalized by `Cslib.Turing.Universal.Clocked.parseTime`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 1180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L1180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#parse-time).

## Reading the input

Let $c$ be a code, $x$ a list of bits and $T$ a natural number, and let
$p$ be the cost of reading the input of $c$, $x$ and $T$. Started at the label $\mathsf{pc0}$ with
state bit false, the input encoding of $c$, $x$ and $T$ on the stack $X$ and every other stack
empty, the clocked universal program reaches the label $\mathsf{sc0}$ in exactly $p$ steps, with
some state bit and the stacks of the code $c$, the clock $T$ and the initial configuration on $x$,
with next state and action $0$.

Formalized by `Cslib.Turing.Universal.Clocked.parse_run`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 1186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L1186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#parse-run).

## Output encoding of the clocked universal machine

The output bits of an optional list of
numbers: no result (a timeout) is encoded as the single bit false, and a result $l$ is encoded as
the bit true followed by the cells of $l$, where a number $n$ is written as $n$ bits true followed
by one bit false.

Formalized by `Cslib.Turing.Universal.Clocked.encOut`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 1263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L1263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#enc-out).

## Writing the output

Let $c$ be a code, $t$ a natural number, $k$ a configuration and $v$ a
bit, and let $N$ be the length of the cells of the head symbol of $k$ followed by the symbols to
its right (a symbol $a$ takes $a + 1$ bits). Started at the label $\mathsf{hlt}$ with state bit $v$
and the stacks of the code $c$, the clock $t$ and the configuration $k$ with next state and action
$0$, the clocked universal program reaches the label $\mathsf{done}$ within $4N + 8$ steps, with
some state bit and stacks in which the output stack $O$ holds the encoding of the output of $k$:
the bit true followed by the cells of the output of $k$.

Formalized by `Cslib.Turing.Universal.Clocked.out_run`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 1269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L1269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#out-run).

## Writing a timeout

Let $c$ be a code, $t$ a natural number, $k$ a configuration and $v$ a
bit. Started at the label $\mathsf{tmo}$ with state bit $v$ and the stacks of the code $c$, the
clock $t$ and the configuration $k$ with next state and action $0$, the clocked universal program
reaches the label $\mathsf{done}$ in exactly one step, with the same state bit and the same stacks
except that the output stack $O$ holds the timeout encoding, the single bit false.

Formalized by `Cslib.Turing.Universal.Clocked.tmo_run`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 1315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L1315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#tmo-run).

## Step bound of the clocked universal machine

For a code $c$, a list of bits $x$ and a
natural number $T$, the step bound of the whole machine on $(c, x, T)$ is the sum of three terms:
the cost of reading the input on $(c, x, T)$, the step bound of the clocked simulation on the
clock $T$, and the output bound $4\,(|x| + T + 1)\,(|C| + 3) + 8$, where $|x|$ is the length of
$x$ and $|C|$ is the length of the code stack of $c$.

Formalized by `Cslib.Turing.Universal.Clocked.univTime`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 1363](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L1363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#univ-time).

## Correctness and running time of the clocked universal machine

Let $c$ be a code, $x$ a
list of bits and $T$ a natural number. Start the clocked universal stack program at the label
$\mathrm{pc0}$ with internal bit $\mathrm{false}$, with every stack empty except $X$, which holds
the input encoding of $(c, x, T)$: the cell of $T$, the cells of the input symbols of $x$ (the
symbol $1$ for $\mathrm{false}$ and $2$ for $\mathrm{true}$), the bit $\mathrm{false}$, and the
code stack of $c$ reversed, where the cell of a number $n$ is $n$ bits $\mathrm{true}$ followed
by the bit $\mathrm{false}$. Then within at most $N(c, x, T)$ steps, where $N$ is the step bound
of the whole machine, the program reaches the label $\mathrm{done}$ (with some internal bit and
some stack contents) with the output encoding of the clocked evaluation of $c$ on $x$ with clock
$T$ on the stack $O$: the single bit $\mathrm{false}$ if the coded machine does not halt within
$T$ steps, and otherwise the bit $\mathrm{true}$ followed by the cells of its output, the tape
from the head rightwards without trailing blanks.

Formalized by `Cslib.Turing.Universal.Clocked.univ_run`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean, line 1368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Clocked.lean#L1368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#univ-run).

## The clocked universal machine as a host component

The component machine whose stacks
are the fifteen stacks of the clocked universal machine, each holding bits, whose labels and
program are those of the clocked universal machine, and whose list of stacks is, in order: the
state $Q$, the next state $N$, the action $A$, the head cell $H$, the cells left ($L$) and right
($R$) of the head, the code $C$, the scan buffer $B$, the scratch counters $T$, $U$, $V$, the
clock $\mathit{Ck}$, the encoded input $X$, the parse buffer $P$ and the output $O$.

Formalized by `Cslib.Turing.Universal.Clocked.univComp`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/Universal/PolyTime.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/PolyTime.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#univ-comp).

## The step bound of the clocked universal machine is quadratic

For every code $c$, list
of bits $x$ and clock $T \in \mathbb{N}$, the step bound of the whole clocked universal machine
on $(c, x, T)$ is at most $18 (n + 1)^2$, where $n$ is the length of the input encoding of
$(c, x, T)$.

Formalized by `Cslib.Turing.Universal.Clocked.univTime_le`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/PolyTime.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/PolyTime.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#univ-time-le).

## Step bound polynomial of the clocked universal machine

The polynomial
$18 (X + 1)^2$ with natural-number coefficients, used as the step bound of the clocked
universal machine as a host component.

Formalized by `Cslib.Turing.Universal.Clocked.univPoly`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/PolyTime.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/PolyTime.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#univ-poly).

## The clocked universal function is polynomial-time computable

There are a multi-stack
Turing machine with finitely many stacks, labels and internal states, whose input and output
alphabets are in bijection with the bits, and a polynomial $p$ with natural-number coefficients,
such that for every code $c$, list of bits $x$ and clock $T \in \mathbb{N}$ the following holds.
Let $n$ be the length of the input encoding of $(c, x, T)$. Started at its main label in its
initial internal state, with the input encoding of $(c, x, T)$ on its input stack and every other
stack empty, the machine halts within $p(n)$ steps, with its internal state again the initial
one, the output encoding of the result of the clocked evaluator on $c$, $x$ and $T$ on its output
stack, and every other stack empty; both encodings are translated letter by letter through the
inverses of the bijections.

In the proof, $p$ has degree $2$: the clocked universal machine itself takes at most
$18 (n + 1)^2$ steps, and running it as a component of the reduction host keeps the degree.

Formalized by `Cslib.Turing.Universal.Clocked.nonempty_univPolyTime`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/PolyTime.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/PolyTime.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html#nonempty-univ-poly-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Clocked universal Turing machine](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/turing-machines/universal-machines/clocked-universal-turing-machine)
