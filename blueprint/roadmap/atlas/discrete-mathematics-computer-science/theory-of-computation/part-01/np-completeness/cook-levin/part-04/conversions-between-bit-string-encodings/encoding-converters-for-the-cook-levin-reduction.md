---
declaration: section
origin: cited
lean: Cslib.Complexity.DenseSAT.ToCanonical.Stk, Cslib.Complexity.DenseSAT.ToCanonical.Γ, Cslib.Complexity.DenseSAT.ToCanonical.Lab, Cslib.Complexity.DenseSAT.ToCanonical.St, Cslib.Complexity.DenseSAT.ToCanonical.isFst, Cslib.Complexity.DenseSAT.ToCanonical.isSnd, Cslib.Complexity.DenseSAT.ToCanonical.bit, Cslib.Complexity.DenseSAT.ToCanonical.prog
statement: formalized
proof: formalized
---

# Encoding converters for the Cook-Levin reduction

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html).

## From `w # y` to the canonical pair encoding

## Stacks of the converter to the canonical pair encoding

The converter has four stacks: the
input stack, whose symbols are left-tagged bits, right-tagged bits and the separator (the input
is the bits of a first bit list tagged left, a separator, then the bits of a second bit list
tagged right); the output stack, holding bits; and two stashes, holding the bits of the first
and of the second list.

Formalized by `Cslib.Complexity.DenseSAT.ToCanonical.Stk`, an inductive type declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#stk).

## Stack alphabets of the separator-to-canonical converter

The input stack of the converter
from the separator form of a pair to its canonical encoding has the verifier's alphabet, and each
of its other three stacks (the output and the two stashes) has the alphabet of bits.

Formalized by `Cslib.Complexity.DenseSAT.ToCanonical.Γ`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#untitled).

## Labels of the converter to the canonical pair encoding

The machine that turns the
separated form of a pair $(x, w)$ of bit lists (the bits of $x$ tagged left, a separator, then
the bits of $w$ tagged right) into the canonical encoding of the pair has five labels: reading
the first part, reading the second part, emitting the second part, writing the separator, and
emitting the first part.

Formalized by `Cslib.Complexity.DenseSAT.ToCanonical.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#lab).

## States of the converter to the canonical pair encoding

A state of the converter is
either empty or one symbol of the verifier's input alphabet, that is, a left-tagged bit, a
right-tagged bit or the separator.

The state holds the last symbol popped; bits popped from the stashes are stored as left-tagged
bits.

Formalized by `Cslib.Complexity.DenseSAT.ToCanonical.St`, an abbreviation declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#st).

## Left-tagged state test

For a state $s$ of the pair-to-canonical converter (either empty
or a symbol of the verifier alphabet), the test is true exactly when $s$ is a left-tagged bit
$\mathrm{inl}\,b$ for some bit $b$, and false when $s$ is empty, the separator
$\mathrm{inr}(\mathrm{none})$ or a right-tagged bit.

Formalized by `Cslib.Complexity.DenseSAT.ToCanonical.isFst`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#is-fst).

## Right-tagged state test

For a state $s$ of the pair-to-canonical converter (either empty
or a symbol of the verifier alphabet), the test is true exactly when $s$ is a right-tagged bit
$\mathrm{inr}(\mathrm{some}\,b)$ for some bit $b$, and false when $s$ is empty, the separator
$\mathrm{inr}(\mathrm{none})$ or a left-tagged bit.

Formalized by `Cslib.Complexity.DenseSAT.ToCanonical.isSnd`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#is-snd).

## Bit carried by a converter state

For a state $s$ of the pair-to-canonical converter
(either empty or a symbol of the verifier alphabet), the bit of $s$ is $b$ when $s$ is a
left-tagged bit $\mathrm{inl}\,b$ or a right-tagged bit $\mathrm{inr}(\mathrm{some}\,b)$, and
$\mathrm{false}$ when $s$ is empty or the separator $\mathrm{inr}(\mathrm{none})$.

Formalized by `Cslib.Complexity.DenseSAT.ToCanonical.bit`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#bit).

## Program of the converter to the canonical pair encoding

The machine has an input stack
of symbols, each a left-tagged bit, a right-tagged bit or the separator, and three stacks of
bits: the output and two stashes. Its program first pops input symbols and pushes the bit of
each left-tagged one onto the first stash, until the input is empty or the symbol popped is not
a left-tagged bit. It then pops input symbols and pushes the bit of each right-tagged one onto
the second stash, until the input is empty or the symbol popped is not a right-tagged bit. Next
it pops each bit $b$ of the second stash and pushes false, $b$, true onto the output, and then
pushes a single false. Finally it pops each bit $b$ of the first stash and pushes false, true,
$b$, true, true, true onto the output, and halts when the first stash is empty.

Each output block is pushed in reverse, so that it reads true, $b$, false (respectively true,
true, true, $b$, true, false) from the top.

Formalized by `Cslib.Complexity.DenseSAT.ToCanonical.prog`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#prog).

## Machine converting the separator form of a pair to its canonical encoding

The
multi-stack Turing machine with the four stacks of the converter to the canonical pair encoding
(input, output and two stashes), whose input stack holds symbols of the verifier's alphabet
(left-tagged bits, right-tagged bits and the separator) and whose other stacks hold bits, reading
its input from the input stack and leaving its output on the output stack, with the five labels
of that converter and start label $\mathrm{readFst}$, the converter's states (empty or one
verifier symbol) as internal states, initially empty, and the program of the converter to the
canonical pair encoding. It pops input symbols, pushing the bit of each left-tagged one onto the
first stash, until the input is empty or the symbol popped is not a left-tagged bit. It then pops
input symbols, pushing the bit of each right-tagged one onto the second stash, until the input is
empty or the symbol popped is not a right-tagged bit. Next it pops each bit $b$ of the second
stash and pushes a block reading true, $b$, false from the top onto the output, pushes a single
false, pops each bit $b$ of the first stash and pushes a block reading true, true, true, $b$,
true, false from the top, and halts when the first stash is empty.

Formalized by `Cslib.Complexity.DenseSAT.ToCanonical.tm`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#tm).

## Stack contents of the converter to the canonical pair encoding

Given a list $i$ of input
symbols and bit lists $o$, $a$ and $b$, this is the contents of the four stacks of the converter
with $i$ on the input stack, $o$ on the output stack, $a$ on the first stash and $b$ on the
second stash.

Formalized by `Cslib.Complexity.DenseSAT.ToCanonical.stk`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#stk-2).

## Runs of the converter to the canonical pair encoding

For a natural number $n$ and
configurations $c$ and $d$ of the converter, this is the proposition that $n$ steps of its
program lead from $c$ to $d$: applying the step function $n$ times to $c$ is defined at every
step (no configuration before the last one is halted) and gives $d$.

Formalized by `Cslib.Complexity.DenseSAT.ToCanonical.Run`, an abbreviation declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#run).

## Run of the pair-to-canonical converter

Let $x$ and $w$ be bit lists, write $x \# w$ for
the verifier input of the pair $(x, w)$, and read $1$ for true and $0$ for false. Let
$\mathrm{encFst}(x)$ replace each bit $b$ of $x$ by $1, 1, 1, b, 1, 0$ and $\mathrm{encSnd}(w)$
replace each bit $b$ of $w$ by $1, b, 0$. The program of the pair-to-canonical converter goes in
exactly $2|x| + 2|w| + 5$ steps from the configuration at label $\mathrm{readFst}$ with empty
state, $x \# w$ on the input stack and the output stack and both stashes empty, to the halted
configuration with empty state, empty input stack and stashes, and output stack reading
$\mathrm{encFst}(x)$, then $0$, then $\mathrm{encSnd}(w)$ from the top.

Formalized by `Cslib.Complexity.DenseSAT.ToCanonical.convert_run`, a theorem declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#convert-run).

## Canonical bit-list decoder

This is a multi-stack Turing machine over the alphabet
$\mathrm{Bool}$, with time bound $n + 2$, such that for every bit list $x$, started on the
canonical bitstring encoding of $x$, it halts within $n + 2$ steps, where $n$ is the length of
that encoding, with $x$ on its output stack and all other stacks empty. So the identity on bit
lists is computable in polynomial time from the canonical encoding to the raw bits.

Formalized by `Cslib.Complexity.DenseSAT.ToCanonical.computable`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#computable).

## Stacks of the bit-list converters

The two bit-list converters use three stacks: the
input stack, the output stack and one stash.

Formalized by `Cslib.Complexity.DenseSAT.BStk`, an inductive type declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#bstk).

## Labels of the bit-list converters

The two bit-list converters have two program labels,
$\mathrm{read}$ and $\mathrm{emit}$.

Formalized by `Cslib.Complexity.DenseSAT.BLab`, an inductive type declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#blab).

## Stack contents of the bit-list converters

For bit lists $i$, $o$ and $a$, this assigns
contents to the three stacks of the bit-list converters: $i$ to the input stack, $o$ to the
output stack and $a$ to the stash. Every stack alphabet is $\mathrm{Bool}$.

Formalized by `Cslib.Complexity.DenseSAT.bstk`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#bstk-2).

## Program of the bit-list decoder

The program of the machine that decodes the canonical
encoding of a bit list acts on the three stacks of the bit-list converters, all over bits, with an
optional bit as internal state. At label $\mathrm{read}$ it pops a symbol from the input stack into
the state (which becomes empty if the input is empty). If that symbol is true, it pops a second
symbol $b$ into the state, pops and discards a third, pushes $b$ onto the stash (false if the
input ran out before $b$) and returns to $\mathrm{read}$; otherwise it goes to $\mathrm{emit}$. At
label $\mathrm{emit}$ it pops a bit from the stash, pushes it onto the output and returns to
$\mathrm{emit}$, and it halts when the stash is empty.

Formalized by `Cslib.Complexity.DenseSAT.DecodeBits.prog`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#prog-2).

## Machine decoding the canonical encoding of a bit list

The multi-stack Turing machine with
the three stacks of the bit-list converters (input, output and a stash), all over bits, reading
its input from the input stack and leaving its output on the output stack, with the two labels
$\mathrm{read}$ and $\mathrm{emit}$ and start label $\mathrm{read}$, an optional bit as internal
state, initially empty, and the program of the bit-list decoder. It repeatedly pops an input
symbol; while that symbol is true, it pops two more and pushes the first of them onto the stash
(false if the input ran out before it). Then it moves the stash, bit by bit, onto the output, and
halts.

Formalized by `Cslib.Complexity.DenseSAT.DecodeBits.tm`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#tm-2).

## Runs of the bit-list decoder

For a natural number $n$ and configurations $c$ and $d$ of
the machine decoding the canonical encoding of a bit list (each an optional label, an optional bit
as internal state and the contents of the three bit stacks), this is the proposition that $n$
steps of its program lead from $c$ to $d$: applying the step function $n$ times to $c$ is defined
at every step (no configuration before the last one is halted) and gives $d$.

Formalized by `Cslib.Complexity.DenseSAT.DecodeBits.Run`, an abbreviation declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#run-2).

## Polynomial-time decoder of the canonical bit-list encoding

This is a multi-stack Turing
machine whose input and output alphabets are the bits, together with the polynomial time bound
$t(n) = n + 2$, such that for every bit list $x$, whose canonical bitstring encoding has length
$n$, the machine started with that encoding on its input stack and all other stacks empty halts
within $t(n)$ steps with $x$ on its output stack, all other stacks empty and its internal state
back to the initial one. So the identity on bit lists is computable in polynomial time from the
canonical encoding to the raw bits.

The canonical encoding writes each bit $b$ of $x$ as the three bits true, $b$, false.

Formalized by `Cslib.Complexity.DenseSAT.DecodeBits.computable`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#computable-2).

## Program of the bit-list encoder

The program of the machine that writes the canonical
encoding of a bit list acts on the three stacks of the bit-list converters, all over bits, with an
optional bit as internal state. At label $\mathrm{read}$ it pops a bit from the input stack,
pushes it onto the stash and returns to $\mathrm{read}$; when the input is empty it goes to
$\mathrm{emit}$. At label $\mathrm{emit}$ it pops a bit $b$ from the stash, pushes false, $b$ and
true onto the output, so that the output then reads true, $b$, false from the top, and returns to
$\mathrm{emit}$; it halts when the stash is empty.

Formalized by `Cslib.Complexity.DenseSAT.EncodeBits.prog`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#prog-3).

## Machine writing the canonical encoding of a bit list

The multi-stack Turing machine with
the three stacks of the bit-list converters (input, output and a stash), all over bits, reading
its input from the input stack and leaving its output on the output stack, with the two labels
$\mathrm{read}$ and $\mathrm{emit}$ and start label $\mathrm{read}$, an optional bit as internal
state, initially empty, and the program of the bit-list encoder. It moves the input, bit by bit,
onto the stash. Then it pops the stash bit by bit, pushing for each bit $b$ the three bits false,
$b$, true onto the output, so that each block reads true, $b$, false from the top, and halts.

Formalized by `Cslib.Complexity.DenseSAT.EncodeBits.tm`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#tm-3).

## Runs of the bit-list encoder

For a natural number $n$ and configurations $c$ and $d$ of
the machine writing the canonical encoding of a bit list (each an optional label, an optional bit
as internal state and the contents of the three bit stacks), this is the proposition that $n$
steps of its program lead from $c$ to $d$: applying the step function $n$ times to $c$ is defined
at every step (no configuration before the last one is halted) and gives $d$.

Formalized by `Cslib.Complexity.DenseSAT.EncodeBits.Run`, an abbreviation declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#run-3).

## Polynomial-time encoder to the canonical bit-list encoding

This is a multi-stack Turing
machine whose input and output alphabets are the bits, together with the polynomial time bound
$t(n) = 2n + 2$, such that for every bit list $x$ of length $n$, the machine started with $x$ on
its input stack and all other stacks empty halts within $t(n)$ steps with the canonical bitstring
encoding of $x$ on its output stack, all other stacks empty and its internal state back to the
initial one. So the identity on bit lists is computable in polynomial time from the raw bits to
the canonical encoding.

The canonical encoding writes each bit $b$ of $x$ as the three bits true, $b$, false.

Formalized by `Cslib.Complexity.DenseSAT.EncodeBits.computable`, a definition declared in [CSLibExt/Computability/Complexity/EncodingConverters.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/EncodingConverters.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html#computable-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Encoding converters for the Cook-Levin reduction](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/encoding-converters-for-the-cook-levin-reduction)
