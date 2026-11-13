---
declaration: section
origin: cited
lean: Cslib.Complexity.DenseSAT.Converter.encFst, Cslib.Complexity.DenseSAT.Converter.encSnd, Cslib.Complexity.DenseSAT.Converter.bitEncode_pair_eq, Cslib.Complexity.DenseSAT.Converter.Stk, Cslib.Complexity.DenseSAT.Converter.Γ, Cslib.Complexity.DenseSAT.Converter.Lab, Cslib.Complexity.DenseSAT.Converter.St, Cslib.Complexity.DenseSAT.Converter.prog
statement: formalized
proof: formalized
---

# From the canonical pair encoding to the w # y form

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html).

## The canonical encoding of a pair of bit lists

## Converter encoding of the first component

For a bit list $x$, the bit list obtained by
replacing every bit $b$ of $x$, in order, with the six bits true, true, true, $b$, true, false.

Formalized by `Cslib.Complexity.DenseSAT.Converter.encFst`, a definition declared in [CSLibExt/Computability/Complexity/PairEncodingConverter.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PairEncodingConverter.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html#enc-fst).

## Converter encoding of the second component

For a bit list $w$, the bit list obtained by
replacing every bit $b$ of $w$, in order, with the three bits true, $b$, false.

Formalized by `Cslib.Complexity.DenseSAT.Converter.encSnd`, a definition declared in [CSLibExt/Computability/Complexity/PairEncodingConverter.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PairEncodingConverter.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html#enc-snd).

## Canonical encoding of a pair of bit lists

For bit lists $x$ and $w$, the canonical
bitstring encoding of the pair $(x, w)$ is the concatenation of three parts: every bit $b$ of $x$,
in order, written as the six bits true, true, true, $b$, true, false; then a single false; then
every bit $b$ of $w$, in order, written as the three bits true, $b$, false.

Formalized by `Cslib.Complexity.DenseSAT.Converter.bitEncode_pair_eq`, a theorem declared in [CSLibExt/Computability/Complexity/PairEncodingConverter.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PairEncodingConverter.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html#bit-encode-pair-eq).

## Stacks of the pair-encoding converter

The machine that rewrites the canonical encoding
of a pair of bit lists into the verifier's input form has four stacks: the input stack, the
output stack, and two stash stacks, one for each component of the pair.

Formalized by `Cslib.Complexity.DenseSAT.Converter.Stk`, an inductive type declared in [CSLibExt/Computability/Complexity/PairEncodingConverter.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PairEncodingConverter.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html#stk).

## Stack alphabets of the pair-encoding converter

The output stack of the converter has as
its alphabet the verifier's work alphabet $G = \{0,1\} \sqcup (\{0,1\} \cup \{\#\})$; the input
stack and the two stash stacks have the bits $\{0,1\}$ as their alphabet.

Formalized by `Cslib.Complexity.DenseSAT.Converter.Γ`, a definition declared in [CSLibExt/Computability/Complexity/PairEncodingConverter.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PairEncodingConverter.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html#untitled).

## Labels of the pair-encoding converter

The five labels of the converter program: read the
first component, read the second component, emit the second component, emit the separator, and
emit the first component.

Formalized by `Cslib.Complexity.DenseSAT.Converter.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/PairEncodingConverter.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PairEncodingConverter.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html#lab).

## State of the pair-encoding converter

The internal state of the converter is an optional
bit: either a bit or nothing. It records the last bit the program stored.

Formalized by `Cslib.Complexity.DenseSAT.Converter.St`, an abbreviation declared in [CSLibExt/Computability/Complexity/PairEncodingConverter.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PairEncodingConverter.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html#st).

## Program of the pair-encoding converter

The program over the converter's four stacks,
five labels and states (a bit or nothing). Each pop either stores the popped bit in the state
(nothing if the stack is empty) or leaves the state unchanged, and each push of the stored bit
uses false when the state holds nothing.

At *read first*: pop the input, storing; if the state is true, pop the input twice without
storing, once storing and twice without storing, push the stored bit onto the first stash and go
to *read first*; otherwise go to *read second*. At *read second*: pop the input, storing; if the
state is true, pop the input once storing and once without storing, push the stored bit onto the
second stash and go to *read second*; otherwise go to *emit second*. At *emit second*: pop the
second stash, storing; if a bit was popped, push it onto the output as a right-tagged bit and go
to *emit second*; otherwise go to *separator*. At *separator*: push the separator onto the
output and go to *emit first*. At *emit first*: pop the first stash, storing; if a bit was
popped, push it onto the output as a left-tagged bit and go to *emit first*; otherwise halt.

Formalized by `Cslib.Complexity.DenseSAT.Converter.prog`, a definition declared in [CSLibExt/Computability/Complexity/PairEncodingConverter.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PairEncodingConverter.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html#prog).

## The pair-encoding converter machine

The converter is the finite multi-stack Turing
machine whose stacks are the input stack, the output stack and the two stash stacks, with bits
as the alphabet of every stack except the output stack, which holds the verifier's symbols. Its
labels are the five phases (read the first component, read the second, emit the second, emit
the separator, emit the first), and it starts in the phase that reads the first component. Its
internal state is an optional bit (the last bit popped), initially empty, and it runs the
converter program. Input is read from the input stack, which holds bits, and output is written
to the output stack.

Formalized by `Cslib.Complexity.DenseSAT.Converter.tm`, a definition declared in [CSLibExt/Computability/Complexity/PairEncodingConverter.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PairEncodingConverter.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html#tm).

## Stack contents of the pair-encoding converter

For bit lists $i$, $a$, $b$ and a list $o$ of
verifier symbols, the contents of the converter's four stacks with $i$ on the input stack, $o$ on
the output stack, $a$ on the first stash and $b$ on the second stash.

Formalized by `Cslib.Complexity.DenseSAT.Converter.stk`, a definition declared in [CSLibExt/Computability/Complexity/PairEncodingConverter.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PairEncodingConverter.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html#stk-2).

## Runs of the pair-encoding converter

For $n \in \mathbb{N}$ and configurations $c$ and $d$
of the converter, the statement that $n$ steps of the converter program lead from $c$ to $d$.

Formalized by `Cslib.Complexity.DenseSAT.Converter.Run`, an abbreviation declared in [CSLibExt/Computability/Complexity/PairEncodingConverter.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PairEncodingConverter.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html#run).

## Full run of the pair-encoding converter

For bit lists $x$ and $w$, the converter program
goes in exactly $2|x| + 2|w| + 5$ steps from the configuration at the label *read first*, with
no bit in the state, the input stack holding every bit $b$ of $x$ in order as the six bits true,
true, true, $b$, true, false, then a single false, then every bit $b$ of $w$ in order as the three
bits true, $b$, false, and the other three stacks empty, to the halted configuration with no bit
in the state, the verifier's pair encoding of $(x, w)$ on the output stack and the other three
stacks empty.

Formalized by `Cslib.Complexity.DenseSAT.Converter.convert_run`, a theorem declared in [CSLibExt/Computability/Complexity/PairEncodingConverter.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PairEncodingConverter.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html#convert-run).

## Polynomial-time conversion to the verifier's pair encoding

A polynomial-time computation
of the identity map on pairs $(x, w)$ of bit lists, from the canonical bitstring encoding of
$(x, w)$ to the verifier's pair encoding of $(x, w)$ (the bits of $x$, the separator, then the
bits of $w$), by the converter machine, with the bits and the verifier's symbols themselves as
input and output alphabets and time bound $n + 5$: started on the canonical encoding of $(x, w)$,
a list of length $n$, the converter halts within $n + 5$ steps with no bit in its state, the
verifier's pair encoding of $(x, w)$ on its output stack and every other stack empty.

Formalized by `Cslib.Complexity.DenseSAT.Converter.computable`, a definition declared in [CSLibExt/Computability/Complexity/PairEncodingConverter.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PairEncodingConverter.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html#computable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: From the canonical pair encoding to the w # y form](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/from-the-canonical-pair-encoding-to-the-w-y-form)
