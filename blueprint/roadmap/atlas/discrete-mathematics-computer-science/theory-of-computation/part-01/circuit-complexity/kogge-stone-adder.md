---
declaration: section
origin: cited
lean: Cslib.Circuits.appendGates, Cslib.Circuits.appendGates_eval_lt, Cslib.Circuits.appendGates_eval_le, Cslib.Circuits.appendGates_eval_ge, Cslib.Circuits.CarryLookahead.combine, Cslib.Circuits.CarryLookahead.gpBit, Cslib.Circuits.CarryLookahead.gpRange, Cslib.Circuits.CarryLookahead.gpRange_add
statement: formalized
proof: formalized
---

# Kogge–Stone adder

44 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html).

## Appending a block of gates

## Appending a block of gates

Let $p$ be a straight-line program with $g$ gates over $m$
inputs, let $c \in \mathbb{N}$, and for each $j < c$ let $f_j$ be a line (a gate operation with
its argument wires) that reads the inputs and the first $g + j$ gates. Appending
$f_0, \dots, f_{c-1}$ to $p$ gives the program with $g + c$ gates whose first $g$ gates are
those of $p$ and whose gate $g + j$ is $f_j$ for each $j < c$. It is defined by recursion on
$c$, adding one gate at a time.

Formalized by `Cslib.Circuits.appendGates`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#append-gates).

## Appending gates keeps the old gate values

Let $p$ be a program with $g$ gates over $m$
inputs, let $c \in \mathbb{N}$, and for each $j < c$ let $f_j$ be a line that reads the inputs
and the first $g + j$ gates. Under any interpretation of the gate symbols and any input values,
for every $k < g$ the value of gate $k$ of the program obtained by appending
$f_0, \dots, f_{c-1}$ to $p$ equals the value of gate $k$ of $p$.

Formalized by `Cslib.Circuits.appendGates_eval_lt`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#append-gates-eval-lt).

## Appending one more gate keeps the earlier gate values

Let $p$ be a program with $g$
gates over $m$ inputs, let $c \in \mathbb{N}$, and for each $j \le c$ let $f_j$ be a line that
reads the inputs and the first $g + j$ gates. Under any interpretation of the gate symbols and
any input values, for every $k < g + c$ the value of gate $k$ of the program obtained by
appending $f_0, \dots, f_c$ to $p$ equals the value of gate $k$ of the program obtained by
appending $f_0, \dots, f_{c-1}$ to $p$ (no gates when $c = 0$).

Formalized by `Cslib.Circuits.appendGates_eval_le`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#append-gates-eval-le).

## Values of appended gates

Let $p$ be a program with $g$ gates over $m$ inputs, let
$c \in \mathbb{N}$, and for each $j < c$ let $f_j$ be a line that reads the inputs and the first
$g + j$ gates. Under any interpretation of the gate symbols and any input values $x$, for every
$j < c$ the value of gate $g + j$ of the program obtained by appending $f_0, \dots, f_{c-1}$ to
$p$ is the value of the line $f_j$ on $x$ and the values of gates $0, \dots, g + j - 1$ of that
same program.

Formalized by `Cslib.Circuits.appendGates_eval_ge`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#append-gates-eval-ge).

## Combining generate–propagate pairs

For pairs of Booleans $(G, P)$ and $(G', P')$, their
combination is $(G \lor (P \land G'), P \land P')$.

When $(G, P)$ are the generate and propagate signals of a block of bits placed directly above a
block with signals $(G', P')$, the combination gives the signals of the joined block.

Formalized by `Cslib.Circuits.CarryLookahead.combine`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#combine).

## Generate and propagate signals of a bit

For bit vectors $x, y$ of width $n$ and an index
$i \in \mathbb{N}$, the generate–propagate pair of bit $i$ is $(x_i \wedge y_i,\ x_i \oplus y_i)$,
where $x_i$ and $y_i$ are bit $i$ of $x$ and $y$, taken to be false when $i \ge n$.

Formalized by `Cslib.Circuits.CarryLookahead.gpBit`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#gp-bit).

## Generate and propagate signals of a block

For bit vectors $x, y$ of the same width, a
start bit $\ell$ and a length $m$, the generate–propagate pair $\mathrm{GP}(\ell, m)$ of the block
of bits $\ell, \dots, \ell + m - 1$ is defined by recursion on $m$: the empty block has
$\mathrm{GP}(\ell, 0) = (\mathrm{false}, \mathrm{true})$, and
$\mathrm{GP}(\ell, m + 1) = \mathrm{gp}(\ell + m) \circ \mathrm{GP}(\ell, m)$, where
$\mathrm{gp}(\ell + m)$ is the generate–propagate pair of bit $\ell + m$ and $\circ$ is the block
operator with its left argument placed above its right.

Formalized by `Cslib.Circuits.CarryLookahead.gpRange`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#gp-range).

## Adjacent blocks compose

Fix bit vectors $x, y$ of the same width, write
$\mathrm{GP}(\ell, m)$ for the generate–propagate pair of the block of the $m$ bits
$\ell, \dots, \ell + m - 1$, and write $h \circ l$ for the block operator with $h$ placed above
$l$. Then for all natural numbers $\ell, a, b$,
$\mathrm{GP}(\ell, a + b) = \mathrm{GP}(\ell + a, b) \circ \mathrm{GP}(\ell, a)$.

Formalized by `Cslib.Circuits.CarryLookahead.gpRange_add`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#gp-range-add).

## The carry out of a block of bits

Let $x, y$ be $n$-bit vectors and $c$ a carry-in bit,
and for $i \in \mathbb{N}$ let $c_i$ be the carry into bit $i$ when computing $x + y + c$, that
is, $c_i$ holds exactly when $(x \bmod 2^i) + (y \bmod 2^i) + c \ge 2^i$, where $x$, $y$ are
read as natural numbers and $c$ counts as $1$ when true. For all $a, \ell \in \mathbb{N}$, if
$(G, P)$ are the generate and propagate signals of the block of bits $a, \dots, a + \ell - 1$,
then $c_{a + \ell} = G \lor (P \land c_a)$.

Formalized by `Cslib.Circuits.CarryLookahead.carry_add`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#carry-add).

## Lowest bit of a Kogge-Stone block

The lowest bit of the block that bit $i$ holds after $k$
Kogge-Stone levels, $i + 1 - \min(i + 1, 2^k)$, that is, $\max(0, i + 1 - 2^k)$.

Formalized by `Cslib.Circuits.CarryLookahead.lowBit`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#low-bit).

## The block held after Kogge-Stone levels

Fix bit vectors $x, y$ of the same width. For
$k, i \in \mathbb{N}$, the pair $S_k(i)$ that bit $i$ holds after $k$ Kogge-Stone levels is the
generate–propagate pair of the block of the $\min(i + 1, 2^k)$ bits ending at bit $i$, that is,
of the bits $i + 1 - \min(i + 1, 2^k), \dots, i$.

Formalized by `Cslib.Circuits.CarryLookahead.gpSpec`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#gp-spec).

## The Kogge-Stone step

Fix bit vectors $x, y$ of the same width and write $S_k(i)$ for the
generate–propagate pair of the block of the $\min(i + 1, 2^k)$ bits ending at bit $i$, the pair
bit $i$ holds after $k$ Kogge-Stone levels. For all $k, i \in \mathbb{N}$: if $2^k \le i$, then
$S_{k+1}(i) = S_k(i) \circ S_k(i - 2^k)$, where $\circ$ is the block operator with its left
argument placed above its right; otherwise $S_{k+1}(i) = S_k(i)$.

Formalized by `Cslib.Circuits.CarryLookahead.gpSpec_succ`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#gp-spec-succ).

## Carries from the Kogge–Stone prefixes

Let $x, y$ be $n$-bit vectors, $c$ a carry-in bit,
and $K$, $i$ natural numbers with $n \le 2^K$ and $i < n$. Let $(G, P)$ be the generate and
propagate signals that bit $i$ holds after $K$ Kogge–Stone levels, those of the block of the at
most $2^K$ bits ending at bit $i$. Then the carry into bit $i + 1$ of $x + y + c$, which is true
exactly when $(x \bmod 2^{i+1}) + (y \bmod 2^{i+1}) + c \ge 2^{i+1}$, equals
$G \lor (P \land c)$.

Since $n \le 2^K$, that block is the whole prefix of bits $0, \dots, i$.

Formalized by `Cslib.Circuits.CarryLookahead.carry_of_gpSpec`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#carry-of-gp-spec).

## Gate count of the first Kogge-Stone levels

For an $n$-bit adder, the number $L_n(k)$ of
gates in level $0$ together with the first $k$ Kogge-Stone levels is given by $L_n(0) = 2n$ and
$L_n(k + 1) = L_n(k) + 3n$, so $L_n(k) = 2n + 3nk$.

Formalized by `Cslib.Circuits.CarryLookahead.levelBase`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#level-base).

## Index of the generate gate

For $n$-bit Kogge-Stone adders, the generate signal of bit $i$
after level $0$ is held by gate $2i$, and after Kogge-Stone level $k + 1$ by gate
$2n + 3nk + 3i + 1$; here $2n + 3nk$ is the number of gates in levels $0, \dots, k$.

Formalized by `Cslib.Circuits.CarryLookahead.gNum`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#g-num).

## Propagate gate of a bit in the Kogge–Stone adder

For natural numbers $n$, $k$ and $i$,
$p_n(k, i)$ is the index of the gate holding the propagate signal of bit $i$ after level $k$ of
the $n$-bit carry-lookahead adder: $p_n(0, i) = 2i + 1$, and $p_n(k + 1, i) = 2n + 3nk + 3i + 2$,
where $2n + 3nk$ is the number of gates in levels $0, \dots, k$.

Formalized by `Cslib.Circuits.CarryLookahead.pNum`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#p-num).

## Kogge–Stone partner bit

The bit combined with bit $i$ at level $k + 1$ of the Kogge–Stone
adder is bit $i - 2^k$ if $2^k \le i$, and bit $i$ itself otherwise.

Formalized by `Cslib.Circuits.CarryLookahead.partner`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#partner).

## Gates of level 0

Gate $j < 2n$ of level $0$ of the $n$-bit adder of $x$ and $y$ reads the
inputs $\lfloor j/2 \rfloor$ and $n + \lfloor j/2 \rfloor$, which carry bit $\lfloor j/2 \rfloor$
of $x$ and of $y$. For even $j$ it is an AND gate, the generate signal of that bit; for odd $j$ it
is an XOR gate, its propagate signal.

Formalized by `Cslib.Circuits.CarryLookahead.line0`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#line0).

## Gates of a Kogge-Stone level

Gate $j < 3n$ of Kogge-Stone level $k + 1$ of the $n$-bit
adder serves bit $i = \lfloor j/3 \rfloor$ and its partner $q$, which is $i - 2^k$ if $2^k \le i$
and $i$ otherwise. Write $G_b$ and $P_b$ for the generate and propagate gates of bit $b$ after
level $k$. If $j \equiv 0 \pmod 3$ the gate computes $P_i \wedge G_q$; if $j \equiv 1 \pmod 3$ it
computes the new generate signal $G_i \vee (P_i \wedge G_q)$ from $G_i$ and the previous gate; if
$j \equiv 2 \pmod 3$ it computes the new propagate signal $P_i \wedge P_q$.

Formalized by `Cslib.Circuits.CarryLookahead.lineK`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#line-k).

## The first Kogge-Stone levels

For an $n$-bit adder, the program over the XOR, AND and OR
gates on $2n + 1$ inputs obtained from the empty program by appending the $2n$ gates of level
$0$ and then, in turn, the $3n$ gates of each Kogge-Stone level $1, \dots, k$. It has
$2n + 3nk$ gates.

Formalized by `Cslib.Circuits.CarryLookahead.levels`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#levels).

## Gates of the final level

Gate $j < 3n$ of the final level of the $n$-bit adder with $K$
Kogge-Stone levels serves bit $i = \lfloor j/3 \rfloor$. Write $G_i$ and $P_i$ for the generate and
propagate gates of bit $i$ after the $K$ levels, $p_i$ for the propagate gate of bit $i$ at level
$0$, and $c$ for the carry input. If $j \equiv 0 \pmod 3$ the gate computes $P_i \wedge c$; if
$j \equiv 1 \pmod 3$ it computes the carry $c_{i+1} = G_i \vee (P_i \wedge c)$ from $G_i$ and the
previous gate; if $j \equiv 2 \pmod 3$ it computes the sum bit $p_i \oplus c_i$, where $c_0 = c$
and, for $i \ge 1$, $c_i$ is the carry gate of bit $i - 1$.

Formalized by `Cslib.Circuits.CarryLookahead.lineF`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#line-f).

## Gates of the carry-lookahead adder

For natural numbers $n$ and $K$, the gate program of
the $n$-bit adder with $K$ Kogge–Stone levels is the straight-line program over the XOR/AND/OR
basis on $2n + 1$ inputs (the $n$ bits of one summand, the $n$ bits of the other and a carry-in
$c$) made of level $0$ and Kogge–Stone levels $1, \dots, K$, followed by a final level of $3n$
gates. For each bit $i < n$, let $G_i$ and $P_i$ be the generate and propagate gates of bit $i$
after level $K$ and $p_i$ its propagate gate at level $0$. Gate $3i$ of the final level computes
$P_i \land c$, gate $3i + 1$ computes $G_i \lor (P_i \land c)$, and gate $3i + 2$ computes
$p_i \oplus c$ when $i = 0$ and the XOR of $p_i$ with gate $3(i - 1) + 1$ of the final level
otherwise.

Formalized by `Cslib.Circuits.CarryLookahead.claProgram`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#cla-program).

## Kogge–Stone carry-lookahead adder

For natural numbers $n$ and $K$, the $n$-bit
carry-lookahead adder with $K$ levels is the circuit over the XOR/AND/OR basis with $2n + 1$
inputs (the bits $x_0, \dots, x_{n-1}$ of one summand, the bits $y_0, \dots, y_{n-1}$ of the
other, and a carry-in $c$) and $n + 1$ outputs, whose gates are those of the $n$-bit adder
program with $K$ Kogge–Stone levels. For $i < n$, output $i$ is the sum gate of bit $i$ in the
final level; output $n$ is the carry gate of bit $n - 1$ in the final level, or the input $c$
when $n = 0$.

When $n \le 2^K$, the outputs are the $n$ bits of $x + y + c$ and its carry out.

Formalized by `Cslib.Circuits.CarryLookahead.carryLookaheadAdder`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#carry-lookahead-adder).

## Number of carry-lookahead levels

For a natural number $n$, the number of Kogge–Stone
levels used for $n$ bits is $\lfloor \log_2 n \rfloor + 1$, with $\lfloor \log_2 0 \rfloor = 0$.

This number satisfies $n \le 2^{\lfloor \log_2 n \rfloor + 1}$.

Formalized by `Cslib.Circuits.CarryLookahead.claLevels`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#cla-levels).

## Level 0 computes generate and propagate

Let $x$ and $y$ be $n$-bit vectors and $c$ a carry
bit, and evaluate level $0$ of the adder on the bits of $x$, the bits of $y$ and $c$. For every
bit $i < n$, the gate holding the generate signal of bit $i$ carries the generate signal, and the
gate holding its propagate signal carries the propagate signal, of the block consisting of bit $i$
alone, namely $x_i \wedge y_i$ and $x_i \oplus y_i$.

Formalized by `Cslib.Circuits.CarryLookahead.levels_zero_eval`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#levels-zero-eval).

## Each Kogge-Stone level is correct

Let $x$ and $y$ be $n$-bit vectors and $c$ a carry bit,
and evaluate level $0$ and the first $k$ Kogge-Stone levels of the adder on the bits of $x$, the
bits of $y$ and $c$. For every bit $i < n$, the gate holding the generate signal of bit $i$
carries the generate signal, and the gate holding its propagate signal carries the propagate
signal, of the block of the at most $2^k$ bits ending at $i$, that is, of the bits
$\max(0, i + 1 - 2^k), \dots, i$.

Formalized by `Cslib.Circuits.CarryLookahead.levels_eval`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#levels-eval).

## Level-0 gates are unchanged by later levels

For the $n$-bit adder, every interpretation
of the XOR, AND and OR gates in a type $U$, every assignment of values in $U$ to the $2n + 1$
inputs, and every $K$, each of the $2n$ gates of level $0$ has the same value in the program with
level $0$ and $K$ Kogge-Stone levels as in the program with level $0$ alone.

Formalized by `Cslib.Circuits.CarryLookahead.levels_eval_base`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#levels-eval-base).

## The carry gates

Let $x, y$ be $n$-bit vectors, $c$ a carry-in bit and $K$ a natural number
with $n \le 2^K$. Evaluate the gate program of the $n$-bit adder with $K$ Kogge–Stone levels in
the Boolean interpretation of the XOR/AND/OR basis, on the input made of the bits of $x$, the bits
of $y$ and $c$. Then for every $i < n$, gate $3i + 1$ of the final level holds the carry into bit
$i + 1$ of $x + y + c$, which is true exactly when
$(x \bmod 2^{i+1}) + (y \bmod 2^{i+1}) + c \ge 2^{i+1}$.

Formalized by `Cslib.Circuits.CarryLookahead.claProgram_carry`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#cla-program-carry).

## The sum gates

Let $x, y$ be $n$-bit vectors with bits $x_i$, $y_i$, $c$ a carry-in bit
and $K$ a natural number with $n \le 2^K$. Evaluate the gate program of the $n$-bit adder with
$K$ Kogge–Stone levels in the Boolean interpretation of the XOR/AND/OR basis, on the input made
of the bits of $x$, the bits of $y$ and $c$. Then for every $i < n$, gate $3i + 2$ of the final
level is $x_i \oplus y_i \oplus c_i$, where $c_i$ is the carry into bit $i$ of $x + y + c$, true
exactly when $(x \bmod 2^i) + (y \bmod 2^i) + c \ge 2^i$.

Formalized by `Cslib.Circuits.CarryLookahead.claProgram_sum`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#cla-program-sum).

## Sum bits of the carry-lookahead adder

Let $x, y$ be $n$-bit vectors, $c$ a carry-in bit
and $K$ a natural number with $n \le 2^K$. Evaluate the $n$-bit Kogge–Stone carry-lookahead adder
with $K$ levels in the Boolean interpretation of the XOR/AND/OR basis, on the input made of the
bits of $x$, the bits of $y$ and $c$. Then for every $i < n$, output $i$ of the adder is bit $i$
(the bit of weight $2^i$) of the sum $x + y + c$ taken modulo $2^n$.

Formalized by `Cslib.Circuits.CarryLookahead.carryLookaheadAdder_sum`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#carry-lookahead-adder-sum).

## Carry out of the carry-lookahead adder

Let $n, K \in \mathbb{N}$ with $n \le 2^K$, let
$x, y$ be $n$-bit vectors and let $c$ be a carry-in bit. Evaluate the $n$-bit Kogge-Stone
carry-lookahead adder with $K$ levels over the Boolean XOR/AND/OR basis on the input that lists
the bits of $x$ from least to most significant, then those of $y$ in the same order, then $c$.
Its output $n$, the last of its $n + 1$ outputs numbered from $0$, is the carry out of
$x + y + c$: it is true exactly when $x + y + c \ge 2^n$, where $x$, $y$ are read as natural
numbers and $c$ counts as $1$ when true.

Formalized by `Cslib.Circuits.CarryLookahead.carryLookaheadAdder_carry`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#carry-lookahead-adder-carry).

## Gate count of the carry-lookahead adder

For all $n, K \in \mathbb{N}$, the $n$-bit
Kogge-Stone carry-lookahead adder with $K$ levels has exactly $5n + 3nK$ gates: $2n$ in the
first level, $3n$ in each of the $K$ Kogge-Stone levels, and $3n$ in the final level.

Formalized by `Cslib.Circuits.CarryLookahead.carryLookaheadAdder_size`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 486](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L486). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#carry-lookahead-adder-size).

## The depth interpretation

For a signature $\sigma$, the depth interpretation is the
interpretation of $\sigma$ in $\mathbb{N}$ that sends an operation symbol of arity $k$, applied to
argument depths $d_0, \dots, d_{k-1}$, to $\max(0, d_0, \dots, d_{k-1}) + 1$: a gate is one deeper
than its deepest argument, and a gate without arguments has depth $1$.

Formalized by `Cslib.Circuits.depthInterpretation`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 504](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#depth-interpretation).

## Gate depths are evaluation in the depth interpretation

For every program $p$ over a
signature $\sigma$, the depth of each gate of $p$ equals the value of that gate when $p$ is
evaluated under the depth interpretation of $\sigma$ with every input set to $0$.

Formalized by `Cslib.Circuits.Program.depths_eq_eval`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#depths-eq-eval).

## Depth of an arithmetic gate

For each gate of the arithmetic basis (XOR, AND or OR) and all
argument depths $d_0, d_1 \in \mathbb{N}$, the depth interpretation of the arithmetic signature
assigns the gate the depth $\max(d_0, d_1) + 1$.

Formalized by `Cslib.Circuits.depthInterpretation_arith`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 518](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L518). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#depth-interpretation-arith).

## Depths after each level

In the program made of level $0$ and the first $k$ Kogge-Stone
levels of the $n$-bit adder, where inputs have depth $0$ and a gate is one deeper than its deepest
argument, for every bit $i < n$ the gate holding the generate signal of bit $i$ has depth $2k + 1$
and the gate holding its propagate signal has depth $k + 1$.

Formalized by `Cslib.Circuits.CarryLookahead.levels_depth`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 559](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L559). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#levels-depth).

## Depth of the carry gates

For all natural numbers $n$, $K$ and $i < n$, in the gate program
of the $n$-bit adder with $K$ Kogge–Stone levels, the carry gate of bit $i$ in the final level
(gate $3i + 1$ of that level) has depth $\max(2K + 1, K + 2) + 1$, where inputs have depth $0$
and each gate is one deeper than its deepest argument.

Formalized by `Cslib.Circuits.CarryLookahead.claProgram_carry_depth`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 613](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L613). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#cla-program-carry-depth).

## Depth of the sum gates

For all natural numbers $n$, $K$ and $i < n$, in the gate program
of the $n$-bit adder with $K$ Kogge–Stone levels, the sum gate of bit $i$ in the final level
(gate $3i + 2$ of that level) has depth $2$ if $i = 0$ and depth $\max(2K + 1, K + 2) + 2$
otherwise, where inputs have depth $0$ and each gate is one deeper than its deepest argument.

Formalized by `Cslib.Circuits.CarryLookahead.claProgram_sum_depth`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 636](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L636). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#cla-program-sum-depth).

## Exact depth of the carry-lookahead adder

For all $K \ge 1$ and $n \ge 2$, the $n$-bit
Kogge-Stone carry-lookahead adder with $K$ levels has depth exactly $2K + 3$, the depth being the
largest depth of an output with the inputs at depth $0$.

With $K = \lfloor \log_2 n \rfloor + 1$ levels this is $2 \lfloor \log_2 n \rfloor + 5$,
logarithmic in $n$, while the depth of the ripple-carry adder grows linearly in $n$.

Formalized by `Cslib.Circuits.CarryLookahead.carryLookaheadAdder_depth`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 666](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L666). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#carry-lookahead-adder-depth).

## Depth of the carry-lookahead adder with logarithmically many levels

For every
$n \ge 2$, the $n$-bit Kogge-Stone carry-lookahead adder with $\lfloor \log_2 n \rfloor + 1$
levels has depth exactly $2 \lfloor \log_2 n \rfloor + 5$, the depth being the largest depth of
an output with the inputs at depth $0$.

Formalized by `Cslib.Circuits.CarryLookahead.carryLookaheadAdder_depth_claLevels`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 692](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L692). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#carry-lookahead-adder-depth-cla-levels).

## Carry depth in the ripple-carry adder

For $i \in \mathbb{N}$, the carry depth of bit $i$
is $0$ if $i = 0$ and $2i + 1$ if $i \ge 1$. It is used as the depth of the carry into bit $i$
of the ripple-carry adder, where the carry into bit $0$ is the carry-in input.

Formalized by `Cslib.Circuits.RippleCarry.carryDepth`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 707](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L707). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#carry-depth).

## Gate-depth formula for the ripple-carry adder

Let $c(i)$ be the carry depth of bit $i$:
$c(0) = 0$ and $c(i) = 2i + 1$ for $i \ge 1$. The formula assigns to gate $j$ of the ripple-carry
adder, for every $j \in \mathbb{N}$, the depth $1$ when $j \bmod 5$ is $0$ or $2$, the depth
$\max(1, c(\lfloor j/5 \rfloor)) + 1$ when $j \bmod 5$ is $1$ or $3$, and the depth
$c(\lfloor j/5 \rfloor + 1)$ when $j \bmod 5 = 4$.

Formalized by `Cslib.Circuits.RippleCarry.gateDepth`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 710](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L710). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#gate-depth).

## Gate depths of the ripple-carry adder

For natural numbers $n$, $g \le 5n$ and $j < g$,
evaluating the first $g$ gates of the $n$-bit ripple-carry adder in $\mathbb{N}$, with every
input at depth $0$ and every gate one deeper than its deepest argument, gives gate $j$ the depth
$d(j)$. Here, with $q = \lfloor j / 5 \rfloor$, $c(0) = 0$ and $c(i) = 2i + 1$ for $i \ge 1$,
$d(j) = 1$ if $j \bmod 5 \in \{0, 2\}$, $d(j) = \max(1, c(q)) + 1$ if $j \bmod 5 \in \{1, 3\}$,
and $d(j) = c(q + 1)$ if $j \bmod 5 = 4$.

Formalized by `Cslib.Circuits.RippleCarry.rcaProgram_depth`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 738](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L738). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#rca-program-depth).

## The ripple-carry adder has linear depth

For every $n \ge 1$, the $n$-bit ripple-carry
adder has depth $2n + 1$, the length of its carry chain.

Formalized by `Cslib.Circuits.rippleCarryAdder_depth`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean, line 782](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/CarryLookahead.lean#L782). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html#ripple-carry-adder-depth).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kogge–Stone adder](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/circuit-complexity/kogge-stone-adder)
