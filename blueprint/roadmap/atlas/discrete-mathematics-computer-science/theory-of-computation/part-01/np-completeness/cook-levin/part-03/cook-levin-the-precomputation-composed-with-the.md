---
declaration: section
origin: cited
lean: Cslib.Complexity.CookLevin.Precompute.tg, Cslib.Complexity.CookLevin.Precompute.xf, Cslib.Complexity.CookLevin.Precompute.xferS, Cslib.Complexity.CookLevin.Precompute.PW, Cslib.Complexity.CookLevin.Precompute.powS, Cslib.Complexity.CookLevin.Precompute.powB, Cslib.Complexity.CookLevin.Precompute.pow_run, Cslib.Complexity.CookLevin.Precompute.HW
statement: formalized
proof: formalized
---

# Cook-Levin: the precomputation, composed with the assembled generator

53 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html).

## Counter-view additions: decrement, multi-target transfer, the power loop

## Unit targets of a multi-target transfer

For a list $y_1, \dots, y_j$ of counters, the list
of transfer targets that pushes one unit on each counter $y_i$, in the same order.

Formalized by `Cslib.Complexity.CookLevin.Precompute.tg`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#tg).

## Counters after a multi-target transfer

Given counter values $F : C \to \mathbb{N}$, a
counter $x \in C$ and a list $Y$ of counters, the counter values after transferring $x$ to $Y$
form the function that sends $x$ to $0$, sends every $z \ne x$ occurring in $Y$ to
$F(z) + F(x)$, and sends every other $z$ to $F(z)$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.xf`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#xf).

## Multi-target transfer

Let $M$ be a counter machine with counters indexed by $C$, a
Boolean output stack and a Boolean state, let $x \in C$, and let $Y$ be a list of distinct
counters not containing $x$. Suppose the instruction at label $\ell$ is the transfer loop that
pops counter $x$ and pushes one unit on every counter of $Y$, returning to $\ell$ while $x$ is
nonempty and continuing at label $\ell'$ once it is empty. Then for all counter values
$F : C \to \mathbb{N}$, every state bit $v$ and every output stack $o$, the machine runs in
exactly $F(x) + 1$ steps from label $\ell$ with state $v$, counter values $F$ and output stack $o$
to label $\ell'$ with state false, output stack $o$ and the counter values after transferring
$x$ to $Y$: counter $x$ becomes $0$, each counter of $Y$ gains $F(x)$, and every other counter
keeps its value.

Formalized by `Cslib.Complexity.CookLevin.Precompute.xferS`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#xfer-s).

## Stages of the power loop

The labels of one power-loop site: a head stage, a
multiplication stage $\mathrm{mul}(s)$ for each stage $s$ of a multiplication site, a drain stage
and a move stage.

Formalized by `Cslib.Complexity.CookLevin.Precompute.PW`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#pw).

## Power-loop program

Given six counters $b$, $k$, $p$, $q$, $a$, $t$, a label for each
power-loop stage and an exit label, the power loop is the following program on the stages. At
the head stage it pops one unit from $k$; if $k$ was empty it goes to the exit label, otherwise
to the first multiplication stage. The multiplication stages add $p \cdot b$ to $q$ (a
multiplication site with index counter $a$ and scratch counter $t$) and then go to the drain
stage. The drain stage empties $p$ and goes to the move stage. The move stage moves the contents
of $q$ onto $p$ and returns to the head stage.

When the six counters are distinct and $q = a = t = 0$ at the start, each round multiplies $p$ by
$b$, so the loop replaces $p$ by $p \cdot b^k$ and ends with $k = 0$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.powS`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#pow-s).

## Step budget of the power loop

For natural numbers $j$ (the number of rounds), $p$ (the
start value) and $b$ (the base), the step budget of the power loop is
$j \, (p \, (b + 1)^j \, (3 b + 5) + 5) + 1$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.powB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#pow-b).

## The power loop

Let $b, k, p, q, a, t$ be pairwise distinct counters of a counter machine
$M$, let $\mu$ assign a label to each power-loop stage and let $\nu$ be a label. Suppose that for
every power-loop stage $s$ the label $\mu(s)$ runs the power-loop program for $b, k, p, q, a, t$
with stage labels $\mu$ and exit label $\nu$ at stage $s$. Let $j \in \mathbb{N}$, let $F$ be
counter values with $F(k) = j$ and $F(q) = F(a) = F(t) = 0$, let $v$ be a flag and $o$ an
output. Then $M$ runs from the head stage $\mu(\mathrm{hd})$ with flag $v$, counters $F$ and
output $o$ to the label $\nu$ with flag false, output $o$, and counters $F$ except that $p$ holds
$F(p) \cdot F(b)^j$ and $k$ holds $0$, within $j\,(F(p)\,(F(b) + 1)^j\,(3F(b) + 5) + 5) + 1$
steps, the step budget of the power loop for $j$ rounds, start value $F(p)$ and base $F(b)$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.pow_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#pow-run).

## Stages of a Horner round

The Horner-round stages are $\mathsf{mul}(s)$, one for each
stage $s$ of a multiplication site, and the three stages $\mathsf{drn}$, $\mathsf{mv}$ and
$\mathsf{add}$. In a Horner round they label the multiplication, draining the accumulator,
moving the product into the accumulator, and adding the coefficient.

Formalized by `Cslib.Complexity.CookLevin.Precompute.HW`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#hw).

## The statements of one Horner round

For counters $b, \mathit{acc}, q, d, t$, a number
$a \in \mathbb{N}$, stage labels $\mu$ and an exit label $\nu$: the statements performing
$\mathit{acc} \leftarrow \mathit{acc} \cdot b + a$ in four stages, each stage reaching the next
through $\mu$. The multiplication stages add $\mathit{acc} \cdot b$ to $q$ (with index counter $d$
and scratch counter $t$), then the drain stage empties $\mathit{acc}$, the move stage transfers
$q$ into $\mathit{acc}$, and the add stage pushes $a$ units onto $\mathit{acc}$ and continues at
$\nu$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.hornS`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#horn-s).

## Step count of one Horner round

For an accumulator value $A$ and a base $b$, the number
$A(2b + 3) + A + 2 + (A + 1) + (Ab + 1) + 1$: the exact number of steps one Horner round takes
from $\mathit{acc} = A$ with base $b$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.hornStep`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#horn-step).

## One Horner round

Let $b, \mathit{acc}, q, d, t$ be pairwise distinct counters of a
counter machine $M$, let $a \in \mathbb{N}$, let $\mu$ assign a label to each Horner-round stage
and let $\nu$ be a label. Suppose that for every Horner-round stage $s$ the label $\mu(s)$ runs
the Horner-round statement for $b, \mathit{acc}, q, d, t, a$ with stage labels $\mu$ and exit
label $\nu$ at stage $s$. Let $F$ be counter values with $F(q) = F(d) = F(t) = 0$, let $v$ be a
flag and $o$ an output, and let $h$ be the step count of one Horner round. Then $M$ runs from the
first multiplication stage $\mu(\mathrm{mul\ head})$ with flag $v$, counters $F$ and output $o$
in exactly $h(F(\mathit{acc}), F(b))$ steps to the label $\nu$ with flag false, output $o$, and
counters $F$ except that $\mathit{acc}$ holds $F(\mathit{acc}) \cdot F(b) + a$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.horn_round`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#horn-round).

## Horner value

For a list $c_1, \dots, c_\ell$ of natural numbers and natural numbers $b$
and $A$, the Horner value of $c_1, \dots, c_\ell$ with base $b$ from accumulator $A$ is the number
obtained from the starting value $x = A$ by replacing $x$ by $x b + c_i$ for $i = 1, \dots, \ell$
in turn; for the empty list it is $A$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.hornVal`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#horn-val).

## Step count of the Horner rounds

For a list $cs$ of coefficients, a base $b$ and an
accumulator value $A$: $0$ if $cs$ is empty, and if $cs$ is $a$ followed by $cs'$, the step count
$h(A, b)$ of one Horner round from $A$ with base $b$ plus the step count of $cs'$ with base $b$
from accumulator $A b + a$. This is the exact number of steps of the Horner rounds.

Formalized by `Cslib.Complexity.CookLevin.Precompute.hornT`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#horn-t).

## Horner rounds

Let $b, \mathit{acc}, q, d, t$ be pairwise distinct counters of a counter
machine $M$, let $c_0, \dots, c_{\ell-1}$ be natural numbers, let $\mu$ assign a label
$\mu(i, s)$ to each $i \in \mathbb{N}$ and each Horner-round stage $s$, and let $\nu$ be a label.
Suppose that for every $i < \ell$ and every stage $s$ the label $\mu(i, s)$ runs, at stage $s$,
the statement of one Horner round for $b, \mathit{acc}, q, d, t$ and the number $c_i$, with
stage labels $\mu(i, \cdot)$ and exit label $\mu(i + 1, \mathrm{mul\ head})$ if $i + 1 < \ell$
and $\nu$ otherwise. Then for all $i, j \in \mathbb{N}$ with $i + j = \ell$, all counter values
$F$ with $F(q) = F(d) = F(t) = 0$, every flag $v$ and every output $o$, there is a flag $v'$ such
that $M$ runs in exactly $h$ steps from the label $\mu(i, \mathrm{mul\ head})$ if $i < \ell$ and
$\nu$ otherwise, with flag $v$, counters $F$ and output $o$, to the label $\nu$ with flag $v'$,
output $o$, and counters $F$ except that $\mathit{acc}$ holds the Horner value of
$c_i, \dots, c_{\ell-1}$ with base $F(b)$ from accumulator $F(\mathit{acc})$. Here $h$ is the
step count of the Horner rounds over $c_i, \dots, c_{\ell-1}$ with base $F(b)$ from accumulator
$F(\mathit{acc})$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.horner_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#horner-run).

## Splitting off the starting accumulator in Horner evaluation

For a list
$c_1, \dots, c_\ell$ of natural numbers and natural numbers $b$ and $A$, write $h(x)$ for the
Horner value of $c_1, \dots, c_\ell$ with base $b$ from accumulator $x$: the number obtained
from the starting value $x$ by replacing the current value $y$ by $y b + c_i$ for
$i = 1, \dots, \ell$ in turn. Then $h(A) = A b^{\ell} + h(0)$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.hornVal_eq`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#horn-val-eq).

## Coefficient list of a polynomial

For a polynomial $p$ with natural-number coefficients
and natural degree $d$ (where $d = 0$ when $p = 0$), the coefficient list of $p$ is
$[p_d, p_{d-1}, \dots, p_1, p_0]$, where $p_i$ is the coefficient of $X^i$ in $p$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.coeffs`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#coeffs).

## Horner's rule

For every polynomial $p$ with natural coefficients and every
$b \in \mathbb{N}$, running Horner rounds with base $b$ on the coefficients of $p$ (highest degree
first), starting from accumulator $0$, yields $p(b)$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.hornVal_coeffs`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#horn-val-coeffs).

## Scratch counters of the counter program

The type of the twelve private counters of the
precomputation's counter program, with constructors $N$, $P$, $Q$, $AD$, $TMP$, $KC$, $Mc$, $B$,
$Tc$, $Fx$, $Dd$, $Hc$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.PS`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#ps).

## Target counters of the counter program

The type of the twelve counters that the
precomputation's counter program loads for the host, with constructors $uT$, $uH$, $sT$, $sH$,
$hT$, $hH$, $aT$, $aH$, $iT$, $iX$, $iE$, $iF$.

They hold the twelve preloads of the assembled generator's run.

Formalized by `Cslib.Complexity.CookLevin.Precompute.PT`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#pt).

## Counters of the counter program

A counter of the counter program is either a scratch
counter $s(x)$, for one of the twelve scratch counter names $x$, or a target counter $t(y)$, for
one of the twelve target counter names $y$: the counters are the disjoint union of the scratch
counters and the target counters.

Formalized by `Cslib.Complexity.CookLevin.Precompute.CC`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#cc).

## Labels of the counter program

For $D \in \mathbb{N}$, the number of Horner rounds, the
labels of the counter program are $p_1$; a label $\mathrm{hr}(i, s)$ for each round $i < D$ and
each Horner-round stage $s$; the labels $x_1, x_2, x_3, x_4, c_1, c_2, x_6, x_7, x_8$; a label
$w_2(s)$ for each power-loop stage $s$; $x_9$; a label $\mathrm{ml}(s)$ for each stage $s$ of a
multiplication site; the labels $x_{10}, x_{11}, x_{12}, x_{13}, x_{14}$; and
$\mathrm{done}$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.PL`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#pl).

## Horner-round labels indexed by natural numbers

For a number $D$ of Horner rounds,
$i \in \mathbb{N}$ and a Horner-round stage $s$: the counter-program label for stage $s$ of
Horner round $i$ if $i < D$, and otherwise the label $x_1$ that follows the Horner rounds.

Indices $i \ge D$ are never reached.

Formalized by `Cslib.Complexity.CookLevin.Precompute.hlab`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#hlab).

## The counter program

For a polynomial $k$ with natural-number coefficients, whose
coefficient list $\kappa_0, \dots, \kappa_{D-1}$ has length $D$, and $c, e, d \in \mathbb{N}$,
the counter program is the program with the labels of the counter program for $D$ Horner rounds
that acts on a Boolean output stack and on the scratch and target counters of the counter
program as follows. It runs $D$ Horner rounds, round $i$ with coefficient $\kappa_i$, base $N$,
accumulator $P$, product counter $Q$, index counter $AD$ and scratch counter $TMP$. It moves $P$
onto both $Mc$ and the target $iE$, moves $N$ onto both $Mc$ and the target $iX$, and adds one
unit to each of $Mc$ and $iX$. It adds $Mc$ to $B$, restoring $Mc$ through $TMP$, adds $c$ units
to $B$, $e$ units to $KC$ and one unit to $Tc$, and runs the power loop with base $B$, round
counter $KC$, accumulator $Tc$, product counter $Q$, index counter $AD$ and scratch counter
$TMP$. It adds $d$ units to $Dd$, adds $Dd \cdot Tc$ to $Fx$ (index counter $AD$, scratch
counter $TMP$) and adds $d + 1$ more units to $Fx$. It moves $Fx$ onto both $Hc$ and the target
$iF$ and moves $Mc$ onto $Hc$. Finally it moves $Tc$ onto each of the targets
$uT, sT, hT, aT, iT$, moves $Hc$ onto each of the targets $uH, sH, hH, aH$, and halts.

Started with $n$ on $N$ and every other counter empty, the program computes $P = k(n)$ by
Horner's rule, $m = n + 1 + k(n)$ on $Mc$, $T = (m + c)^e$ on $Tc$, $dT + d + 1$ on $Fx$ and
$m + dT + d + 1$ on $Hc$, and so loads the twelve target counters.

Formalized by `Cslib.Complexity.CookLevin.Precompute.cprog`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 430](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L430). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#cprog).

## Total length bound

For a polynomial $k$ with natural-number coefficients and
$n \in \mathbb{N}$, the total length bound is $m = n + 1 + k(n)$.

So a word $x$ of length $n + 1$ followed by a word $y$ has length at most $m$ exactly when $y$
has length at most $k(n)$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.mOf`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#m-of).

## The precomputed time bound

For a polynomial $k$ with natural coefficients and
$c, e, n \in \mathbb{N}$, the time bound is $T = (m + c)^e$, where $m = n + 1 + k(n)$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.TOf`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#tof).

## Start counter values

For a natural number $n$, the start counter values of the counter
program give the scratch counter $N$ the value $n$ and every other counter the value $0$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.F0`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 461](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L461). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#f0).

## Counter values after the Horner loop

For a polynomial $k$ with natural-number
coefficients and $n \in \mathbb{N}$, this is the assignment of values to the counters of the
counter program that gives the scratch counter $N$ the value $n$, the scratch counter $P$ the
value $k(n)$, and every other counter the value $0$.

The counter program reaches these values after its Horner loop has evaluated $k(n)$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.F1`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#f1).

## Counter values before the power loop

For a polynomial $k$ with natural-number
coefficients and $c, e, n \in \mathbb{N}$, write $m = n + 1 + k(n)$. This is the assignment of
values to the counters of the counter program that gives the scratch counters $\mathit{Mc}$,
$B$, $\mathit{KC}$ and $\mathit{Tc}$ the values $m$, $m + c$, $e$ and $1$, the target counters
$\mathit{iX}$ and $\mathit{iE}$ the values $n + 1$ and $k(n)$, and every other counter the value
$0$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.F2`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#f2).

## Counter values after the power loop

For a polynomial $k$ with natural-number
coefficients and $c, e, n \in \mathbb{N}$, write $m = n + 1 + k(n)$. This is the assignment of
values to the counters of the counter program that gives the scratch counters $\mathit{Mc}$,
$B$ and $\mathit{Tc}$ the values $m$, $m + c$ and $(m + c)^e$, the target counters $\mathit{iX}$
and $\mathit{iE}$ the values $n + 1$ and $k(n)$, and every other counter the value $0$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.F3`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 482](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L482). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#f3).

## Target counter values

For a polynomial $k$ with natural-number coefficients and natural
numbers $c, e, d, n$, let $m = n + 1 + k(n)$, $T = (m + c)^e$ and let $H = m + (T + 1)d + 1$ be
the stack cap. The target values on the twelve target counters assign $T$ to each of
$u_T, s_T, h_T, a_T, i_T$, assign $H$ to each of $u_H, s_H, h_H, a_H$, and assign $n + 1$ to
$i_X$, $k(n)$ to $i_E$ and $(T + 1)d + 1$ to $i_F$.

In particular the value at $i_F$ is $H - m$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.tv`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 491](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L491). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#tv).

## Counter values at the end of the counter program

For a polynomial $k$ with
natural-number coefficients and $c, e, d, n \in \mathbb{N}$, write $m = n + 1 + k(n)$ and
$T = (m + c)^e$. This is the assignment of values to the counters of the counter program that
gives the scratch counters $B$ and $\mathit{Dd}$ the values $m + c$ and $d$, gives each target
counter its target value ($T$ for $\mathit{uT}$, $\mathit{sT}$, $\mathit{hT}$, $\mathit{aT}$ and
$\mathit{iT}$; $m + (T + 1)d + 1$ for $\mathit{uH}$, $\mathit{sH}$, $\mathit{hH}$ and
$\mathit{aH}$; $n + 1$ for $\mathit{iX}$; $k(n)$ for $\mathit{iE}$; $(T + 1)d + 1$ for
$\mathit{iF}$), and gives every other scratch counter the value $0$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.F4`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#f4).

## Step budget of the counter program

For a polynomial $k$ with natural-number coefficients
and natural numbers $c, e, d, n$, let $m = n + 1 + k(n)$, $T = (m + c)^e$ and
$H = m + (T + 1)d + 1$. The step budget of the counter program at $(k, c, e, d, n)$ is

$$
1 + h + (k(n) + 1) + (n + 1) + 2 + (2m + 2) + 3 + p + 1 + (d(2T + 3) + d + 2) + 1 +
(dT + d + 2) + (m + 1) + (T + 1) + (H + 1),
$$

where $h$ is the exact step count of the Horner rounds over the coefficient list of $k$ with
base $n$ from accumulator $0$, and $p = e\left((m + c + 1)^e (3(m + c) + 5) + 5\right) + 1$ is
the step budget of the power loop with $e$ rounds, start value $1$ and base $m + c$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.cB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 506](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L506). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#c-b).

## The counter program's run

Let $k$ be a polynomial with natural-number coefficients, let
$c, e, d, n$ be natural numbers, and put $m = n + 1 + k(n)$ and $T = (m + c)^e$. Start the
counter program for $k, c, e, d$ at its first label with any flag, any output stack $o$, the
scratch counter $N$ equal to $n$ and every other counter equal to $0$. Then, in a number of
steps at most the step budget of the counter program at $(k, c, e, d, n)$, it reaches its label
$\mathrm{done}$ with flag false, output stack $o$, and counter values $T$ on the targets
$uT, sT, hT, aT, iT$; $m + (T + 1)d + 1$ on the targets $uH, sH, hH, aH$; $n + 1$ on $iX$;
$k(n)$ on $iE$; $(T + 1)d + 1$ on $iF$; $m + c$ on the scratch counter $B$; $d$ on the scratch
counter $Dd$; and $0$ on every other counter.

Formalized by `Cslib.Complexity.CookLevin.Precompute.cprog_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#cprog-run).

## Stacks of the full machine

The full machine has one stack for each host stack, one
stack for the raw input, and one stack for each scratch counter of the counter program.

Formalized by `Cslib.Complexity.CookLevin.Precompute.FK`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 569](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L569). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#fk).

## Alphabets of the full machine

For natural numbers $g, r$, the alphabet of a stack of the
full machine is the host's alphabet with $g$ input codes on each host stack,
$\{0, 1, \dots, r - 1\}$ on the raw input stack, and the one-point type on each private
counter.

Formalized by `Cslib.Complexity.CookLevin.Precompute.FΓ`, an abbreviation declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 576](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L576). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#f).

## Labels of the full machine

For $D \in \mathbb{N}$ and a type $\Lambda$ of host labels,
the labels of the full machine are the read-loop label, one label for each label of the counter
program with $D$ Horner rounds, and one label for each element of $\Lambda$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.FL`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 582](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L582). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#fl).

## Host counter of each target

The map from the twelve targets to host stacks: $uT$ and $uH$
go to the counters $T_n$ and $H_s$ of the update generator's block, $sT$ and $sH$ to those of the
situation-definition generator's block, $hT$ and $hH$ to those of the shift generator's block,
$aT$ and $aH$ to those of the accept generator's block, and $iT$, $iX$, $iE$, $iF$ to the counters
$T_n$, $X_n$, $E_n$, $F_n$ of the init generator's block.

Formalized by `Cslib.Complexity.CookLevin.Precompute.tgt`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 589](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L589). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#tgt).

## Stack renaming of the counter program

The stack renaming of the counter program into the
full machine sends the output stack to the host's output stack, each scratch counter $x$ to the
full machine's private counter for $x$, and each target counter $y$ to the host counter that
receives $y$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.eC`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 604](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L604). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#e-c).

## Embedding of the counter program's stacks

For natural numbers $g, r$, the stack embedding
of the counter program into the full machine with $g$ input codes and $r$ raw input symbols
renames stacks by the stack renaming of the counter program and identifies the alphabet of each
stack with that of its image by the identity (Booleans on the output stack, the one-point type
on each counter).

Formalized by `Cslib.Complexity.CookLevin.Precompute.embC`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 614](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L614). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#emb-c).

## Embedding of the host's stacks

For natural numbers $g, r$, the stack embedding of the
host into the full machine with $g$ input codes and $r$ raw input symbols sends each host stack
to the same host stack of the full machine and identifies their alphabets by the identity.

Formalized by `Cslib.Complexity.CookLevin.Precompute.embH`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 633](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L633). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#emb-h).

## The read loop

Given a code map $c_f$ from the raw alphabet $\mathrm{Fin}\,r$ to the code
alphabet $\mathrm{Fin}\,g$, a separator code $c_s$ and a list $L$ of raw symbols, the read-loop
statement tests the symbols $i$ of $L$ in order against the top of the raw input stack. At the
first $i$ found on top, it pops it, pushes $c_f(i)$ on the host input stack and one unit on the
scratch counter $N$, and goes back to the read-loop label (with the flag true). If no symbol of
$L$ is on top, in particular when the raw input is empty, it pushes $c_s$ on the input stack, sets
the flag to false and goes to the first label of the counter program.

The full program takes $L$ to be all of $\mathrm{Fin}\,r$, so each step reads one input symbol.

Formalized by `Cslib.Complexity.CookLevin.Precompute.rdT`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 647](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L647). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#rd-t).

## Stacks during the read loop

For a list $s$ of raw symbols in $\mathrm{Fin}\,r$, a list
$w$ of input codes in $\mathrm{Fin}\,g$, $n \in \mathbb{N}$ and a list $o$ of booleans, these are
the stack contents of the full machine in which the raw-input stack holds $s$, the host input
stack holds $w$, the host output stack holds $o$, the scratch counter $N$ holds $n$ units, and
every other stack is empty.

During the read loop, $s$ is the unread rest of the input and $w$ holds the codes read so far.

Formalized by `Cslib.Complexity.CookLevin.Precompute.fst`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 654](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L654). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#fst).

## The read loop's run

Let $M$ be a program of the full machine whose read-loop label carries
the read loop over all of $\mathrm{Fin}\,r$, with code map $c_f$ and separator code $c_s$, and let
$o$ be a list of booleans. For every raw input $s = s_1 \cdots s_\ell$, list of codes $w$,
$n \in \mathbb{N}$ and flag $v$: started at the read-loop label with flag $v$, raw input stack $s$,
input stack $w$, scratch counter $N = n$, output stack $o$ and every other stack empty, $M$ runs in
exactly $\ell + 1$ steps to the counter program's first label, with flag false, raw input stack
empty, input stack $c_s, c_f(s_\ell), \dots, c_f(s_1)$ followed by $w$, scratch counter
$N = n + \ell$, output stack $o$ and every other stack empty.

Formalized by `Cslib.Complexity.CookLevin.Precompute.read_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 711](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L711). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#read-run).

## The full program

Let $\gamma : \mathrm{Fin}\,r \to \mathrm{Fin}\,g$ code the raw
symbols, let $\sigma \in \mathrm{Fin}\,g$ be a separator code, let $k$ be a polynomial with
natural-number coefficients, let $c, e, d \in \mathbb{N}$, and let $h$ be a host program with
labels $\Lambda$ and start label $\lambda_0 \in \Lambda$. The full program, whose counter-program
labels have $D$ Horner rounds for $D$ the length of the coefficient list of $k$, runs at the
read-loop label the read loop for $\gamma$ and $\sigma$ over all raw symbols; at a
counter-program label $l$ other than the final one, the counter program for $k, c, e, d$ at $l$,
embedded with its scratch counters on the full machine's private counters, its target counters on
the corresponding host counters and its output on the host output; at the final counter-program
label, a step that sets the state to false and jumps to the host label $\lambda_0$; and at a host
label $l$, the statement $h(l)$ on the host stacks.

Formalized by `Cslib.Complexity.CookLevin.Precompute.fprog`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 741](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L741). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#fprog).

## The precomputation

Fix the full program built from a code map $c_f$ from the raw alphabet
$\mathrm{Fin}\,r$ to the code alphabet $\mathrm{Fin}\,g$, a separator code $c_s$, a polynomial $k$
with natural coefficients, constants $c, e, d \in \mathbb{N}$, a host program and its start label.
Let $s = s_1 \cdots s_n$ be a raw input word and $o$ a list of booleans. Started at the read-loop
label with flag false, raw input stack $s$, output stack $o$ and every other stack empty, the full
program reaches the host's start label with flag false within $n + 1 + B + 1$ steps, where $B$ is
the counter program's step budget for $k, c, e, d$ at $n$. The stacks it reaches satisfy: the
output stack is still $o$; the input stack is $c_s, c_f(s_n), \dots, c_f(s_1)$; for every target
$y$, the host counter receiving $y$ has length equal to the target value of $y$ for $k, c, e, d$
at $n$; and every host stack other than the output stack, the input stack and the host counters
receiving targets is empty.

These are the preloads that the assembled generator's run expects.

Formalized by `Cslib.Complexity.CookLevin.Precompute.pre_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 776](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L776). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#pre-run).

## The full program on the real generators

For an encoding $E$ of a machine $M$, a list
$Y$ of symbols of the input stack alphabet of $M$, a symbol $a$ of the output stack alphabet of
$M$, a map $\iota$ from the raw symbols $\mathrm{Fin}\,r$ to input stack symbols of $M$, an input
stack symbol $\sigma$ of $M$ (the separator), a polynomial $k$ with natural-number coefficients
and $c, e \in \mathbb{N}$, this is the full program in which each raw symbol $i$ is coded by the
code of $\iota(i)$ under $E$, the separator code is the code of $\sigma$ under $E$,
$d = \operatorname{depth} M$, the host program is the host running the real generators of $M$
for $Y$ and $a$, and the host starts at the start label of its initial-row generator.

Formalized by `Cslib.Complexity.CookLevin.Precompute.fullProg`, an abbreviation declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 819](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L819). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#full-prog).

## Step bound of the full machine

For an encoding $E$ of a machine $M$, a list $Y$ of
symbols of the input stack alphabet of $M$, a polynomial $k$ with natural-number coefficients and
$c, e, n \in \mathbb{N}$, write $m = n + 1 + k(n)$ and $T = (m + c)^e$. The bound is
$n + 1 + C + 1 + R$, where $C$ is the step budget of the counter program for $k$, $c$, $e$,
$d = \operatorname{depth} M$ and $n$, and $R$ is the host's step bound for $E$ and $Y$ at $m$
and $T$.

It bounds the number of steps of the full machine on a raw input of length $n$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.fullB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 825](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L825). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#full-b).

## The composed machine, raw input to formula

From the raw input `s` (all other stacks
empty, output `o`), the full machine halts its host part at `fin` within `fullB` steps, having
prepended exactly `encodeCNF (Phi …)` for `x = s.map ι ++ [sep]`, `m = |s| + 1 + k(|s|)`,
`T = (m + c)^e`. **No hypotheses** (`|x| ≤ m` is discharged here).

Formalized by `Cslib.Complexity.CookLevin.Precompute.full_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 835](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L835). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#full-run).

## The full machine as a finite multi-stack Turing machine

Given $r \in \mathbb{N}$, an
encoding $E$ of the machine $M$, a list $Y_s$ of input symbols of $M$, an output symbol $a$ of
$M$, a map $\iota$ from $\{0, \dots, r - 1\}$ to input symbols of $M$, an input symbol $\sigma$ of
$M$ (the separator), a polynomial $k$ with natural coefficients and $c, e \in \mathbb{N}$: the
finite multi-stack machine whose stacks are the full stacks (the host's stacks, the raw input
stack and the scratch counters) with the full alphabets, whose labels are the full labels, with
start label the read label, internal states the booleans with initial state false, and program
the full program built from these data. Its input stack is the raw input stack and its output
stack is the host's output stack.

Formalized by `Cslib.Complexity.CookLevin.Precompute.fullTM`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 888](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L888). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#full-tm).

## Initial configuration of the full machine

Let $E$ be encoding data for a finite
multi-stack Turing machine $M$, and let $r$ be a natural number. Fix a list $Y$ of input-stack
symbols of $M$, an output-stack symbol $a$ of $M$, a map $\iota$ from $\{0, \dots, r-1\}$ to
input-stack symbols of $M$, a separator input-stack symbol $\sigma$ of $M$, a polynomial $k$ with
natural-number coefficients and natural numbers $c$ and $e$. On every raw input $s$, a word over
$\{0, \dots, r-1\}$, the initial configuration of the full machine built from these data is at
the read-loop label with internal state false, its raw-input stack holds $s$, and all its other
stacks (the code stack, the output stack, the scratch counters and the remaining host stacks)
are empty.

Formalized by `Cslib.Complexity.CookLevin.Precompute.initList_full`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 901](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L901). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#init-list-full).

## Polynomial functions on the naturals

A function $f : \mathbb{N} \to \mathbb{N}$ is
polynomial when there is a polynomial $p$ with natural-number coefficients such that
$f(n) = p(n)$ for every $n \in \mathbb{N}$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.IsPoly`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 917](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L917). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#is-poly).

## The Horner step count is polynomial

Let $cs$ be a list of natural numbers and let
$A : \mathbb{N} \to \mathbb{N}$ be a polynomial function, that is, there is a polynomial $q$ with
natural-number coefficients such that $A(n) = q(n)$ for all $n$. Then $n \mapsto h(n, A(n))$ is a
polynomial function in the same sense, where $h(b, a)$ is the step count of the Horner rounds over
$cs$ with base $b$ from accumulator $a$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.IsPoly.hornT`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 937](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L937). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#horn-t-2).

## Polynomial time bound of the composed machine

Let $M$ be a finite multi-stack machine
with encoding data $E$, let $Y$ be a list of symbols of the input stack of $M$, $a$ a symbol of
its output stack, $\iota$ a map from the raw symbols $\mathrm{Fin}\,r$ to symbols of the input
stack, $\sigma$ a symbol of the input stack (the separator), $k$ a polynomial with
natural-number coefficients and $c, e \in \mathbb{N}$. Then there is a polynomial $p$ with
natural-number coefficients such that the following holds for every raw input
$s = s_1 \cdots s_n$ over $\mathrm{Fin}\,r$ and every list $o$ of booleans. Write
$m = n + 1 + k(n)$, $T = (m + c)^e$ and $x = \iota(s_1) \cdots \iota(s_n)\,\sigma$. The full
program on the real generators for $E$, $Y$, $a$, $\iota$, $\sigma$, $k$, $c$ and $e$, started at
its read-loop label with flag false, $s$ on the raw input stack, $o$ on the host output stack and
every other stack empty, reaches the host's final label within $p(n)$ steps, with some flag and
some stack contents in which the host output stack holds the dense encoding of the formula
$\Phi(x, Y, a, m, T)$ emitted by the host, followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.Precompute.full_time_poly`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Precompute.lean, line 971](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Precompute.lean#L971). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html#full-time-poly).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cook-Levin: the precomputation, composed with the assembled generator](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-precomputation-composed-with-the)
