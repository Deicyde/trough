---
declaration: section
origin: cited
lean: Cslib.Turing.SingleTapeTM.FenceSymbol, Cslib.Turing.SingleTapeTM.FenceState, Cslib.Turing.SingleTapeTM.FenceSymbol.read, Cslib.Turing.SingleTapeTM.FenceSymbol.ofCell, Cslib.Turing.SingleTapeTM.FenceSymbol.read_ofCell, Cslib.Turing.SingleTapeTM.FenceSymbol.read_map_sym, Cslib.Turing.SingleTapeTM.FenceSymbol.ofCell_ne_wall, Cslib.Turing.SingleTapeTM.fenceInput
statement: formalized
proof: formalized
---

# Emptiness problem for linear bounded automata

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html).

## Fenced alphabet

For an alphabet $\Sigma$, the tape alphabet of the fenced machine consists
of a symbol for each letter of $\Sigma$, two kinds of padding cells (left and right), which the
simulated machine reads as blanks, and the wall, which marks the ends of the input.

Formalized by `Cslib.Turing.SingleTapeTM.FenceSymbol`, an inductive type declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#fence-symbol).

## States of the fenced machine

For a set of states $Q$, the states of the fenced machine are
two start states, a running state for each state $q \in Q$ of the simulated machine, and a trap
state.

Formalized by `Cslib.Turing.SingleTapeTM.FenceState`, an inductive type declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#fence-state).

## Simulated cell of a fenced cell

The simulated cell of a cell of the fenced machine is
the cell of the simulated machine that it stands for: a symbol of the simulated machine stands
for itself, and every other cell (a padding cell, a wall or a blank) stands for a blank.

Formalized by `Cslib.Turing.SingleTapeTM.FenceSymbol.read`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#read).

## Fenced cell of a write

For a cell $o$ of the simulated machine, a symbol or a blank,
the fenced cell of $o$ is the cell the fenced machine writes for a write of $o$: $o$ itself if
$o$ is a symbol, and the padding cell $\mathrm{pad}$ if $o$ is a blank.

Formalized by `Cslib.Turing.SingleTapeTM.FenceSymbol.ofCell`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#of-cell).

## Reading back a fenced cell of a write

For every cell $o$ of the simulated machine, a
symbol or a blank, the simulated cell of the fenced cell of $o$ is $o$.

Formalized by `Cslib.Turing.SingleTapeTM.FenceSymbol.read_ofCell`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#read-of-cell).

## Reading back a copied cell

Let $o$ be a cell of the simulated machine, a symbol or a
blank, and copy it to the fenced machine, a symbol as itself and a blank as a blank. Then the
simulated cell of the copy is $o$.

Formalized by `Cslib.Turing.SingleTapeTM.FenceSymbol.read_map_sym`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#read-map-sym).

## A fenced cell of a write is never a wall

For every cell $o$ of the simulated machine, a
symbol or a blank, the fenced cell of $o$ is not a wall.

Formalized by `Cslib.Turing.SingleTapeTM.FenceSymbol.ofCell_ne_wall`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#of-cell-ne-wall).

## Fenced input

For a word $w$ over an alphabet $\Sigma$ and $i, j \in \mathbb{N}$, the fenced
input of $w$ with $i$ padding cells on the left and $j$ on the right is the word over the fenced
alphabet of $\Sigma$ made of a wall, $i$ left padding cells, the letters of $w$ as symbols, $j$
right padding cells and a wall, in this order.

Formalized by `Cslib.Turing.SingleTapeTM.fenceInput`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#fence-input).

## Cells of a fenced input

Let $w$ be a word of length $\ell$ and $i, j, n \in \mathbb{N}$.
The cell at position $n$, counting from $0$, of the fenced input of $w$ with $i$ left and $j$
right padding cells is the wall if $n = 0$; a left padding cell if $1 \le n \le i$; the letter of
$w$ at position $n - i - 1$, also counting from $0$, as a symbol, if $i < n \le i + \ell$; a right
padding cell if $i + \ell < n \le i + \ell + j$; the wall if $n = i + \ell + j + 1$; and there is
no cell at a larger position $n$.

Formalized by `Cslib.Turing.SingleTapeTM.getElem?_fenceInput`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#get-elem-fence-input).

## Length of a fenced input

For a word $w$ of length $n$ and natural numbers $i$ and $j$,
the fenced input of $w$ with $i$ padding cells on the left and $j$ on the right has length
$i + n + j + 2$: the word, the two paddings and the two walls.

Formalized by `Cslib.Turing.SingleTapeTM.length_fenceInput`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#length-fence-input).

## A transition lifted to the fenced machine

A transition of a single-tape machine $M$, made
of an optional symbol to write, an optional move and an optional next state, becomes the
transition of the fenced machine of $M$ that writes the symbol, or a right padding cell where $M$
writes a blank, makes the same move, and goes to the running state of the next state $q$ of $M$,
or halts where $M$ halts.

Formalized by `Cslib.Turing.SingleTapeTM.fenceLift`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#fence-lift).

## The running transition of the fenced machine

In the running state of a state $q$ of a
single-tape machine $M$, the fenced machine of $M$ acts on the cell under its head as follows: on a
symbol $a$ it makes the lifted transition of $M$ in state $q$ on $a$; on a left or right padding
cell it makes the lifted transition of $M$ in state $q$ on a blank; on a wall or a blank cell it
leaves the cell unchanged, does not move, and enters the trap.

Formalized by `Cslib.Turing.SingleTapeTM.fenceRun`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#fence-run).

## The fenced machine

For a single-tape machine $M$ over a finite inhabited alphabet $\Sigma$,
the fenced machine of $M$ is the single-tape machine over the fenced alphabet of $\Sigma$ whose
states are the states of the fenced machine for the states of $M$, which starts in the first start
state and acts on the cell under its head as follows. In the first start state, on a wall it moves
right into the second start state, and on any other cell it leaves the cell unchanged, does not
move and enters the trap. In the second start state, on a left padding cell it moves right and
stays in that state, and on any other cell it makes the running transition of the initial state of
$M$. In the running state of a state $q$ of $M$ it makes the running transition of $q$. In the
trap it leaves the cell unchanged, does not move and stays in the trap.

So on the fenced input of a word $w$ it moves right off the left wall and over the left padding,
then runs $M$ from its initial state, and enters the trap when it reads a wall or a blank cell. On
a blank cell, in every state, it writes a blank and does not move.

Formalized by `Cslib.Turing.SingleTapeTM.fence`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#fence).

## The fenced machine is a linear bounded automaton

For every single-tape Turing machine
$M$, the fenced machine of $M$ is a linear bounded automaton.

On a blank cell, in every state, the fenced machine writes a blank and does not move.

Formalized by `Cslib.Turing.SingleTapeTM.isLBA_fence`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#is-lba-fence).

## The fenced machine halts on some padding of a word iff the machine halts on it

Let $M$ be
a single-tape machine over a finite inhabited alphabet and $w$ a word over that alphabet. The
fenced machine of $M$ halts on the fenced input of $w$ with $i$ padding cells on the left and $j$
on the right for some $i, j \in \mathbb{N}$ if and only if $M$ halts on $w$.

A halting run of $M$ of $n$ steps stays within $n$ cells of its start, so it runs unchanged inside
the walls of the fenced input of $w$ with $n + 1$ padding cells on each side; conversely, the
fenced machine halts only by simulating a halting run of $M$.

Formalized by `Cslib.Turing.SingleTapeTM.exists_haltsOn_fence_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 459](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L459). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#exists-halts-on-fence-iff).

## The fenced machine halts on no padding of a word iff the machine does not halt on it

Let
$M$ be a single-tape machine over a finite inhabited alphabet and $w$ a word over that alphabet.
The fenced machine of $M$ halts on none of the fenced inputs of $w$, with $i$ padding cells on the
left and $j$ on the right for $i, j \in \mathbb{N}$, if and only if $M$ does not halt on $w$.

Formalized by `Cslib.Turing.SingleTapeTM.forall_not_haltsOn_fence_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#forall-not-halts-on-fence-iff).

## Emptiness of a linear bounded automaton on computable input slices is undecidable

There
exist a finite inhabited alphabet $\Gamma$ with a primitive recursive encoding, a linear bounded
automaton $F$ over the fenced alphabet of $\Gamma$, and a primitive recursive map $e$ from codes of
partial recursive functions to words over $\Gamma$, such that the set of codes $c$ for which $F$
halts on none of the fenced inputs of $e(c)$, with $i$ padding cells on the left and $j$ on the
right for any $i, j \in \mathbb{N}$, is neither computable nor recursively enumerable.

This is the code-free form of Sipser, Theorem 5.10. Take for $F$ the fenced machine of a
single-tape recognizer $R$ of the set of codes that halt on input $0$, and for $e(c)$ the input of
$c$ to $R$: then $F$ halts on no fenced input of $e(c)$ iff $c$ does not halt on $0$. The word
$e(c)$ does not see the paddings $i$ and $j$, so $F$ itself runs the computation within the space
they give.

Sipser's $E_{\mathrm{LBA}}$ is a language of machine descriptions, the LBAs with empty language;
without a type of codes for machines, this is the form available. Each slice, the set of fenced
inputs of $e(c)$ over all paddings, is regular because of its shape: a wall, any number of left
padding cells, the word $e(c)$, any number of right padding cells and a wall. Informally: with codes of machines, the LBA that checks that its input lies in the slice of $c$
and then runs $F$ has empty language iff $F$ halts on no input of the slice, and
$E_{\mathrm{LBA}}$ is undecidable by the same reduction.

Formalized by `Cslib.Turing.SingleTapeTM.exists_isLBA_not_computablePred_forall_not_haltsOn`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean, line 494](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Fence.lean#L494). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html#exists-is-lba-not-computable-pred-forall).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Emptiness problem for linear bounded automata](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/undecidable-problems/emptiness-problem-for-linear-bounded-automata)
