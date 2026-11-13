---
declaration: section
origin: cited
lean: MetaMathlibExt.TM2Recursive.encodeNat_eq_cons, MetaMathlibExt.TM2Recursive.bitsVal, MetaMathlibExt.TM2Recursive.partrec_run, MetaMathlibExt.TM2Recursive.primrec_of_eventually_const, MetaMathlibExt.TM2Recursive.primrec₂_of_eventually_const, MetaMathlibExt.TM2Recursive.primrec₂_of_finite_left, MetaMathlibExt.TM2Recursive.primcodableArrow, MetaMathlibExt.TM2Recursive.pushes
statement: formalized
---

# Equivalence of Turing machines and recursive functions

68 results, 67 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html).

## Binary encoding, least significant bit first

For every natural number $n \neq 0$, the
binary encoding of $n$ is the list whose first bit is true exactly when $n$ is odd, followed by
the binary encoding of $\lfloor n/2 \rfloor$.

Formalized by `MetaMathlibExt.TM2Recursive.encodeNat_eq_cons`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#encode-nat-eq-cons).

## Value of a little-endian bit list

The value of a list of bits $b_0, b_1, \dots, b_{m-1}$
is $\sum_{i < m} [b_i]\, 2^i$, where $[b_i]$ is $1$ if $b_i$ is true and $0$ otherwise. So the
first bit is the least significant, and the empty list has value $0$.

Formalized by `MetaMathlibExt.TM2Recursive.bitsVal`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#bits-val).

## Running a primitive recursive machine is partial recursive

Let $\alpha$, $\sigma$ and
$\beta$ be primitive recursively encodable types, and let $\mathrm{init} : \alpha \to \sigma$,
$\mathrm{step} : \sigma \to \sigma$, $\mathrm{halted} : \sigma \to \mathrm{Bool}$ and
$\mathrm{out} : \sigma \to \beta$ be primitive recursive. Then the partial function sending $a$
to $\mathrm{out}(\mathrm{step}^k(\mathrm{init}(a)))$, where $k$ is the least natural number for
which $\mathrm{halted}(\mathrm{step}^k(\mathrm{init}(a)))$ is true, and undefined when there is
no such $k$, is partial recursive.

Formalized by `MetaMathlibExt.TM2Recursive.partrec_run`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#partrec-run).

## Eventually constant functions on ℕ are primitive recursive

Let $\beta$ be a primitive
recursively encodable type. If $g : \mathbb{N} \to \beta$ and $N \in \mathbb{N}$ satisfy
$g(c) = g(N)$ for all $c \ge N$, then $g$ is primitive recursive.

Formalized by `MetaMathlibExt.TM2Recursive.primrec_of_eventually_const`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#primrec-of-eventually-const).

## Eventually constant functions of a finite parameter are primitive recursive

Let $\alpha$
be a finite primitive recursively encodable type and $\beta$ a primitive recursively encodable
type. If $g : \alpha \to \mathbb{N} \to \beta$ and $N \in \mathbb{N}$ satisfy
$g(a, c) = g(a, N)$ for all $a \in \alpha$ and all $c \ge N$, then $g$ is primitive recursive as
a function of two arguments.

Formalized by `MetaMathlibExt.TM2Recursive.primrec₂_of_eventually_const`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#primrec-of-eventually-const-2).

## Joint primitive recursion over a finite first argument

Let $\alpha$, $\beta$ and
$\sigma$ be primitive recursively encodable types with $\alpha$ finite, and let
$g : \alpha \to \beta \to \sigma$. If $b \mapsto g(a, b)$ is primitive recursive for every
$a \in \alpha$, then $g$ is primitive recursive as a function of two arguments.

Formalized by `MetaMathlibExt.TM2Recursive.primrec₂_of_finite_left`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#primrec-of-finite-left).

## Encoding of functions on a finite type

For a finite type $K$ and a primitive recursively
encodable type $\beta$, the primitive recursive encoding of the functions $K \to \beta$
transported from that of the functions $\mathrm{Fin}\, n \to \beta$, where $n$ is the cardinality
of $K$, along a chosen bijection between $K$ and $\mathrm{Fin}\, n$.

Formalized by `MetaMathlibExt.TM2Recursive.primcodableArrow`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#primcodable-arrow).

## Symbols a statement may push

For a finite multi-stack machine, a stack $k$ and a
statement $q$ over the machine's stack alphabets, labels and internal states, the set of symbols
of stack $k$ consisting of every value, at every internal state, of the symbol function of every
push instruction onto stack $k$ that occurs in $q$, in either branch of each conditional.

Formalized by `MetaMathlibExt.TM2Recursive.pushes`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#pushes).

## Relevant symbols of a stack

For a stack index $k$, the relevant symbols of stack $k$ are
the symbols $f(v)$ of $\Gamma_k$, for every internal state $v$, over all statements that push $f$
onto stack $k$ and occur in the program of some label, together with, when $k$ is the input stack
$k_0$, every symbol of $\Gamma_{k_0}$.

Along a run started from an initial configuration, only relevant symbols occur on the stacks.

Formalized by `MetaMathlibExt.TM2Recursive.relevant`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#relevant).

## Enumeration of the relevant symbols of a stack

For a finite multi-stack machine and a
stack index $k$, a list without repetitions whose entries are exactly the relevant symbols of
stack $k$, in an order fixed by choice.

Formalized by `MetaMathlibExt.TM2Recursive.symList`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#sym-list).

## Code of a stack symbol

For a finite multi-stack machine, a stack index $k$ and a symbol
$x$ of stack $k$, the code of $x$ is the position of $x$ (counting from $0$) in the chosen
enumeration of the relevant symbols of stack $k$, or the length of that enumeration if $x$ is not
a relevant symbol.

Formalized by `MetaMathlibExt.TM2Recursive.code`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#code).

## Decoding a stack symbol

For a finite multi-stack machine, a stack index $k$ and a natural
number $c$, the decoding of $c$ is the entry at position $c$ (counting from $0$) of the chosen
enumeration of the relevant symbols of stack $k$, and is undefined when $c$ is at least the length
of that enumeration.

Formalized by `MetaMathlibExt.TM2Recursive.decode`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#decode).

## Stacks with only relevant symbols

A family of stacks $S$, consisting of a list $S_k$ of
symbols of $\Gamma_k$ for each stack index $k$, has only relevant symbols when for every stack
index $k$, every symbol on $S_k$ is a relevant symbol of stack $k$.

Formalized by `MetaMathlibExt.TM2Recursive.Relevant`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#relevant-2).

## Encoding of labels

For a finite multi-stack machine, the primitive recursive encoding of
its finite type of labels transported from that of $\mathrm{Fin}\, n$, where $n$ is the number of
labels, along a chosen bijection between the two.

Formalized by `MetaMathlibExt.TM2Recursive.primcodableΛ`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#primcodable).

## Encoding of internal states

For a finite multi-stack machine, the primitive recursive
encoding of its finite type of internal states transported from that of $\mathrm{Fin}\, n$, where
$n$ is the number of internal states, along a chosen bijection between the two.

Formalized by `MetaMathlibExt.TM2Recursive.primcodableσ`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#primcodable-2).

## Coded configurations of a multi-stack machine

For a finite multi-stack machine with label
set $\Lambda$, internal state set $\sigma$ and stack index set $K$, a coded configuration is a
triple consisting of an optional label in $\Lambda$ (no label marks a halted configuration), an
internal state in $\sigma$, and an assignment of a list of natural numbers to each $k \in K$.

Formalized by `MetaMathlibExt.TM2Recursive.CodedCfg`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#coded-cfg).

## Coded stacks

For a finite multi-stack machine, the coded stacks of a family $S$ of stacks
assign to each stack index $k$ the list obtained from the stack $S_k$ by replacing each symbol
with its code.

Formalized by `MetaMathlibExt.TM2Recursive.encStk`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#enc-stk).

## Coding a configuration

For a finite multi-stack machine, the coded configuration of a
configuration $c$ has the same optional label and internal state as $c$, and the coded stacks of
the stacks of $c$.

Formalized by `MetaMathlibExt.TM2Recursive.enc`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#enc).

## Reading the top of a coded stack

Let $k$ be a stack index of the machine and let $S$ assign
to each stack index $j$ a list $S_j$ of natural numbers (codes of symbols). The top of stack $k$ as
read from $S$ is no symbol when $S_k$ is empty. Otherwise, if $c$ is the first entry of $S_k$, it is
the decoding of $c$: the symbol of $\Gamma_k$ at position $c$, counting from $0$, in the list of
relevant symbols of stack $k$, or no symbol when $c$ is at least the length of that list.

Formalized by `MetaMathlibExt.TM2Recursive.readTop`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#read-top).

## The coded execution of a statement

This mirrors the machine's execution of one statement
on stacks of symbol codes. Given a statement $q$, an internal state $v$ and coded stacks $S$ (a list
$S_k$ of natural numbers for each stack index $k$), it returns a coded configuration (an optional
label, an internal state and coded stacks), by recursion on $q$. A push of $f$ onto stack $k$
followed by $q'$ replaces $S_k$ by the code of the symbol $f(v)$ of stack $k$ followed by $S_k$, and
continues with $q'$. A peek at stack $k$ with update $f$ followed by $q'$ continues with $q'$ from
the internal state $f(v, t)$, where $t$ is the top of coded stack $k$ as read from $S$. A pop is
the same as a peek but also removes the first entry of $S_k$ (if there is one). A load of $a$
followed by $q'$ continues with $q'$ from the internal state $a(v)$. A branch on $f$ executes its
first statement if $f(v)$ is true and its second otherwise. A goto $f$ stops with label $f(v)$,
internal state $v$ and stacks $S$, and a halt stops with no label, internal state $v$ and stacks
$S$.

Formalized by `MetaMathlibExt.TM2Recursive.stepAuxC`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#step-aux-c).

## The coded step

For a coded configuration $(l, v, S)$, consisting of an optional label $l$,
an internal state $v$ and coded stacks $S$, the coded step is undefined when $l$ is absent (the
configuration has halted). When $l$ is a label, it is the coded configuration obtained by the coded
execution of the program statement of $l$ from the internal state $v$ on the coded stacks $S$.

Formalized by `MetaMathlibExt.TM2Recursive.stepC`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#step-c).

## Updating the state from the top of a coded stack is primitive recursive

Let $k$ be a
stack index of a finite multi-stack machine, write $\Gamma_k$ for the alphabet of stack $k$, and
let $f$ be any function sending an internal state and an optional symbol of $\Gamma_k$ to an
internal state. Then the map sending an internal state $v$ and coded stacks $S$ (a list $S_j$ of
natural numbers for each stack index $j$) to $f(v, t)$, where $t$ is the top of stack $k$ as read
from $S$, is primitive recursive as a function of two arguments, for the encoding of internal
states and the encoding of functions on the finite type of stack indices.

Formalized by `MetaMathlibExt.TM2Recursive.primrec₂_readTop`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#primrec-read-top).

## Coded stacks after replacing one stack

For a finite multi-stack machine, a family $S$ of
stacks, a stack index $k$ and a list $l$ of symbols of stack $k$, the coded stacks of the family
obtained from $S$ by replacing stack $k$ with $l$ are the coded stacks of $S$ with the entry at
$k$ replaced by the list obtained from $l$ by replacing each symbol with its code.

Formalized by `MetaMathlibExt.TM2Recursive.encStk_update`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#enc-stk-update).

## The coded step on optional configurations

For a finite multi-stack machine, the coded
step extended to optional coded configurations: it sends the absent configuration to the absent
configuration, and a coded configuration $c$ to the coded step of $c$, which is itself absent
when $c$ has halted.

Formalized by `MetaMathlibExt.TM2Recursive.optStepC`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#opt-step-c).

## The coded run simulates the machine's run

Let $o$ be either no configuration or a
configuration of a finite multi-stack machine all of whose stack symbols are relevant. Let
running one step send a running configuration to its successor, and a halted configuration or no
configuration to no configuration. Then for every $j$, applying the coded step on optional
configurations $j$ times to the coding of $o$ gives the coding of the result of running $j$
steps from $o$, and if running $j$ steps from $o$ gives a configuration, all of its stack symbols
are relevant.

Formalized by `MetaMathlibExt.TM2Recursive.optStepC_iterate`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 482](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L482). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#opt-step-c-iterate).

## The initial stacks have only relevant symbols

For a finite multi-stack machine and every
list $s$ of symbols of the input alphabet $\Gamma_{k_0}$, the stacks of the initial configuration
with input $s$ (the list $s$ on the input stack $k_0$ and every other stack empty) have only
relevant symbols.

Formalized by `MetaMathlibExt.TM2Recursive.relevant_initList`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 500](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L500). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#relevant-init-list).

## Configurations before a reached one are running

Write $\mathrm{step}$ for the machine's
step map, which is undefined on halted configurations (those with no label), and iterate it as a
partial map. Let $c_0$ and $c$ be configurations and $s$ a natural number such that $s$ steps from
$c_0$ reach $c$. Then for every $j < s$, $j$ steps from $c_0$ reach some configuration $c'$, and
$c'$ is running: its label is defined.

Formalized by `MetaMathlibExt.TM2Recursive.running_before_halt`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#running-before-halt).

## Turing-computable functions are recursive

Let $f : \mathbb{N} \to \mathbb{N}$ and suppose
that some finite multi-stack Turing machine (finitely many stacks, labels and internal states,
and a finite input alphabet), together with identifications of its input and output stack
alphabets with the booleans, computes $f$ under the binary encoding of natural numbers (least
significant bit first, with $0$ encoded as the empty list): for every $n$, the machine started
at its main label in its initial internal state, with the encoding of $n$ on its input stack and
all other stacks empty, eventually reaches the halted configuration whose output stack holds the
encoding of $f(n)$, whose other stacks are empty and whose internal state is the initial one.
Then $f$ is computable (recursive).

Formalized by `MetaMathlibExt.TM2Recursive.computable_of_tm2Computable`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean, line 556](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/OfTM2.lean#L556). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#computable-of-tm2-computable).

## Bits as stack symbols

Let
$\Gamma' = \{\mathtt{cons}_l, \mathtt{cons}, \mathtt{bit0}, \mathtt{bit1}\}$ be the stack alphabet
of Mathlib's multi-stack machine $\mathrm{tr}$ that evaluates partial recursive codes. This is
the map from bits to $\Gamma'$ that sends $\mathrm{true}$ to $\mathtt{bit1}$ and $\mathrm{false}$
to $\mathtt{bit0}$.

Formalized by `MetaMathlibExt.TM2Recursive.boolToΓ'`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#bool-to).

## Reading a stack symbol as a bit

The map from the stack alphabet $\Gamma'$ of Mathlib's code
evaluator (symbols $\mathrm{cons}_l$, $\mathrm{cons}$, $\mathrm{bit0}$, $\mathrm{bit1}$) to the
booleans sends $\mathrm{bit1}$ to true and every other symbol to false.

Formalized by `MetaMathlibExt.TM2Recursive.Γ'ToBool`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#to-bool).

## The evaluator encodes numbers in binary

For every natural number $n$, the list of stack
symbols by which Mathlib's code evaluator encodes $n$ is obtained from the binary encoding of $n$
(least significant bit first) by writing each bit as $\mathrm{bit1}$ if it is true and as
$\mathrm{bit0}$ if it is false.

Formalized by `MetaMathlibExt.TM2Recursive.trNat_eq_map`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#tr-nat-eq-map).

## The stack set $K'$ is finite

The set
$K' = \{\mathrm{main}, \mathrm{rev}, \mathrm{aux}, \mathrm{stack}\}$ of the four stacks of
Mathlib's multi-stack machine that evaluates partial recursive codes is a finite type whose
elements are exactly these four stacks.

Formalized by `MetaMathlibExt.TM2Recursive.fintypeK'`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#fintype-k).

## Adapter labels

The type with exactly the five elements pre0, pre1, pre2, post1 and post2,
with decidable equality.

They label the wrapped machine's pre-phase, which copies the input bits onto the main stack of
Mathlib's code-evaluating machine $\mathrm{tr}$, and its post-phase, which copies the result back
to the output stack.

Formalized by `MetaMathlibExt.TM2Recursive.Phase`, an inductive type declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#phase).

## Stack alphabets of the wrapped machine

Let $\mathrm{tr}$ be Mathlib's multi-stack machine
that evaluates partial recursive codes, with stacks
$K' = \{\mathrm{main}, \mathrm{rev}, \mathrm{aux}, \mathrm{stack}\}$ and alphabet
$\Gamma' = \{\mathtt{cons}_l, \mathtt{cons}, \mathtt{bit0}, \mathtt{bit1}\}$. The stacks of the
wrapped machine are indexed by $K' \sqcup \{\mathrm{false}, \mathrm{true}\}$: each stack in $K'$
has alphabet $\Gamma'$, and the two stacks $\mathrm{false}$ and $\mathrm{true}$ (the input and
output stacks of the wrapped machine) have the alphabet $\{\mathrm{false}, \mathrm{true}\}$ of
bits.

Formalized by `MetaMathlibExt.TM2Recursive.FΓ`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#f).

## Support of a code

For a code $c$, the support of $c$ is the finite set of labels of
Mathlib's code evaluator $\mathrm{tr}$ that Mathlib associates with evaluating $c$ under the
halting continuation.

It contains the label at which this evaluation starts and is closed under the steps of
$\mathrm{tr}$, so it contains every label reachable from there.

Formalized by `MetaMathlibExt.TM2Recursive.supp`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#supp).

## Labels of the wrapped machine

Let $c$ be a partial recursive code and let $\mathrm{tr}$ be
Mathlib's multi-stack machine that evaluates such codes. The labels of the wrapped machine for $c$
form the disjoint union $\mathrm{Phase} \sqcup \mathrm{supp}(c)$, where
$\mathrm{Phase} = \{\mathrm{pre}_0, \mathrm{pre}_1, \mathrm{pre}_2, \mathrm{post}_1,
\mathrm{post}_2\}$ is the set of five adapter labels and $\mathrm{supp}(c)$ is Mathlib's support
of $\mathrm{tr}$ for $c$ with the halting continuation: a finite set of labels of $\mathrm{tr}$
that contains the start label for $c$ and is closed under the steps of $\mathrm{tr}$.

Formalized by `MetaMathlibExt.TM2Recursive.FΛ`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#f-2).

## Statements of the wrapped machine

Let $c$ be a partial recursive code, and let
$\mathrm{tr}$ be Mathlib's multi-stack machine that evaluates such codes, with stacks
$K' = \{\mathrm{main}, \mathrm{rev}, \mathrm{aux}, \mathrm{stack}\}$ and alphabet
$\Gamma' = \{\mathtt{cons}_l, \mathtt{cons}, \mathtt{bit0}, \mathtt{bit1}\}$. A statement of the
wrapped machine for $c$ is a statement of Mathlib's multi-stack (TM2) Turing machine model whose
stacks are indexed by $K' \sqcup \{\mathrm{false}, \mathrm{true}\}$, where each stack in $K'$ has
alphabet $\Gamma'$ and the stacks $\mathrm{false}$ and $\mathrm{true}$ have the alphabet
$\{\mathrm{false}, \mathrm{true}\}$ of bits, whose labels are the labels of the wrapped machine
for $c$, and whose internal states are the optional symbols of $\Gamma'$ (a symbol of $\Gamma'$,
or none).

Formalized by `MetaMathlibExt.TM2Recursive.FStmt`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#fstmt).

## Restricting a statement of the code evaluator to the wrapped machine

Let $\mathrm{tr}$ be
Mathlib's four-stack machine that evaluates partial recursive codes, and let $S$ be the support
of a code $c$. A statement $q$ of $\mathrm{tr}$ all of whose jump targets lie in $S$ becomes a
statement of the wrapped machine of $c$ with the same structure: each push, peek and pop acts on
the same stack of $\mathrm{tr}$ inside the wrapped machine with the same function, loads and
branches are kept, each jump goes to the same label of $\mathrm{tr}$, now read as an element of
$S$, and halting becomes a jump to the first post-phase label.

Formalized by `MetaMathlibExt.TM2Recursive.restrict`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#restrict).

## The start label lies in the support

For every code $c$, the label at which Mathlib's code
evaluator $\mathrm{tr}$ begins evaluating $c$ with the halting continuation belongs to the
support of $c$.

Formalized by `MetaMathlibExt.TM2Recursive.start_mem`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#start-mem).

## The program of the wrapped machine

Let $c$ be a partial recursive code and let
$\mathrm{tr}$ be Mathlib's multi-stack machine that evaluates such codes, with stacks
$\mathrm{main}, \mathrm{rev}, \mathrm{aux}, \mathrm{stack}$ and alphabet
$\Gamma' = \{\mathtt{cons}_l, \mathtt{cons}, \mathtt{bit0}, \mathtt{bit1}\}$. The program of the
wrapped machine for $c$ assigns a statement to each of its labels, namely the five adapter labels
$\mathrm{pre}_0, \mathrm{pre}_1, \mathrm{pre}_2, \mathrm{post}_1, \mathrm{post}_2$ and the labels
in Mathlib's finite support $\mathrm{supp}(c)$ of $\mathrm{tr}$ for $c$ with the halting
continuation. The internal state $v$ is a symbol of $\Gamma'$ or none, the input stack is the bit
stack $\mathrm{false}$ and the output stack is the bit stack $\mathrm{true}$.

At $\mathrm{pre}_0$: push $\mathtt{cons}$ onto $\mathrm{main}$ and go to $\mathrm{pre}_1$.

At $\mathrm{pre}_1$: pop the input stack and set $v$ to the popped bit as a symbol of $\Gamma'$
($\mathtt{bit1}$ for $\mathrm{true}$, $\mathtt{bit0}$ for $\mathrm{false}$), or to none if the
input stack is empty; if $v$ is a symbol, push it onto $\mathrm{rev}$ and go to $\mathrm{pre}_1$,
otherwise go to $\mathrm{pre}_2$.

At $\mathrm{pre}_2$: pop $\mathrm{rev}$ and set $v$ to the popped symbol (none if $\mathrm{rev}$
is empty); if $v$ is a symbol, push it onto $\mathrm{main}$ and go to $\mathrm{pre}_2$, otherwise
go to the start label of $\mathrm{tr}$ for $c$ with the halting continuation, which lies in
$\mathrm{supp}(c)$.

At a label $l \in \mathrm{supp}(c)$: execute the statement of $\mathrm{tr}$ at $l$, acting on the
stacks of $\mathrm{tr}$, where every jump of $\mathrm{tr}$ becomes a jump to the same label in
$\mathrm{supp}(c)$ and every halt becomes a jump to $\mathrm{post}_1$.

At $\mathrm{post}_1$: pop $\mathrm{main}$ and set $v$ to the popped symbol (none if
$\mathrm{main}$ is empty); if $v$ is none or $\mathtt{cons}$, go to $\mathrm{post}_2$, otherwise
push $v$ onto $\mathrm{rev}$ and go to $\mathrm{post}_1$.

At $\mathrm{post}_2$: pop $\mathrm{rev}$ and set $v$ to the popped symbol (none if $\mathrm{rev}$
is empty); if $v$ is a symbol, push onto the output stack the bit that is $\mathrm{true}$ if
$v = \mathtt{bit1}$ and $\mathrm{false}$ otherwise, and go to $\mathrm{post}_2$; otherwise halt.

Formalized by `MetaMathlibExt.TM2Recursive.fwdProg`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#fwd-prog).

## The wrapped machine of a code

Let $c$ be a code for a partial recursive function on lists
of natural numbers, and let $\mathrm{tr}$ be Mathlib's multi-stack machine that evaluates such
codes, with stacks $K' = \{\mathrm{main}, \mathrm{rev}, \mathrm{aux}, \mathrm{stack}\}$ and
alphabet $\Gamma' = \{\mathtt{cons}_l, \mathtt{cons}, \mathtt{bit0}, \mathtt{bit1}\}$. The
wrapped machine of $c$ is the finite multi-stack machine whose stacks are indexed by
$K' \sqcup \{\mathrm{false}, \mathrm{true}\}$, with alphabet $\Gamma'$ on each stack in $K'$ and
the alphabet of bits on the stacks $\mathrm{false}$ and $\mathrm{true}$; its input stack is
$\mathrm{false}$ and its output stack is $\mathrm{true}$; its labels are the labels of the
wrapped machine for $c$, with main label the first pre-phase adapter label $\mathrm{pre}_0$;
its internal states are the optional symbols of $\Gamma'$ (a symbol of $\Gamma'$, or none), with
initial state none; and its program is the program of the wrapped machine for $c$.

Formalized by `MetaMathlibExt.TM2Recursive.fwdTM`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#fwd-tm).

## Stack contents of the wrapped machine

Given lists $a, b, c, d$ of symbols of $\Gamma'$
and lists $i, o$ of bits, the stack contents of the wrapped machine with $a$, $b$, $c$ and $d$ on
the stacks main, rev, aux and stack, $i$ on the input stack and $o$ on the output stack.

Formalized by `MetaMathlibExt.TM2Recursive.mkStk`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#mk-stk).

## Configurations of the wrapped machine

Let $c$ be a partial recursive code, and let
$\Gamma' = \{\mathtt{cons}_l, \mathtt{cons}, \mathtt{bit0}, \mathtt{bit1}\}$ be the alphabet of
Mathlib's multi-stack machine $\mathrm{tr}$ that evaluates such codes. A configuration of the
wrapped machine for $c$ is a configuration of Mathlib's multi-stack (TM2) Turing machine model
with the stack alphabets and labels of the wrapped machine for $c$ and internal states the
optional symbols of $\Gamma'$: it consists of an optional current label (none once the machine
has halted), an internal state that is a symbol of $\Gamma'$ or none, and for each stack $k$ a
finite list of symbols of the alphabet of $k$.

Formalized by `MetaMathlibExt.TM2Recursive.FCfg`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#fcfg).

## One step of the wrapped machine

For a partial recursive code $c$, the step function of the
wrapped machine for $c$ is Mathlib's multi-stack (TM2) step function for the program of the
wrapped machine for $c$. It sends a configuration without a current label (a halted one) to
none, and a configuration with current label $l$ to the configuration obtained by executing the
statement that the program assigns to $l$ on its internal state and stacks.

Formalized by `MetaMathlibExt.TM2Recursive.fstep`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#fstep).

## Iterated steps of the wrapped machine

Let $c$ be a partial recursive code and let $s$ be
the map that sends none to none and a configuration $d$ of the wrapped machine for $c$ to the
result of one step of the wrapped machine on $d$ (which is none if $d$ has halted). For
$j \in \mathbb{N}$ and $x$ either a configuration of the wrapped machine for $c$ or none, the
$j$-fold run from $x$ is $s^{j}(x)$, the result of applying $s$ to $x$ $j$ times.

Formalized by `MetaMathlibExt.TM2Recursive.frun`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#frun).

## The first pre-phase loop of the wrapped machine

Write $\Gamma'$ for the stack alphabet of
Mathlib's code evaluator. Let $c$ be a code, $a$, $r$, $x$ and $y$ lists of symbols of $\Gamma'$,
$b$ a list of bits of length $k$ and $v$ an internal state (a symbol of $\Gamma'$ or none), and
write $\beta(b)$ for $b$ with each bit $\mathrm{true}$ replaced by the symbol bit1 and each bit
$\mathrm{false}$ by the symbol bit0 of $\Gamma'$. Started at the adapter label pre1 with internal
state $v$, the lists $a$, $r$, $x$ and $y$ on the stacks main, rev, aux and stack, $b$ on the
input stack and the output stack empty, the wrapped machine of $c$ is after exactly $k + 1$ steps
at the adapter label pre2 with internal state none, the reversal of $\beta(b)$ followed by $r$ on
the rev stack, $a$, $x$ and $y$ still on the stacks main, aux and stack, and the input and output
stacks empty.

Formalized by `MetaMathlibExt.TM2Recursive.pre1_loop`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#pre1-loop).

## Pre-phase of the wrapped machine

Let $c$ be a code and $b$ a list of bits of length $k$,
and write $\beta(b)$ for $b$ with each bit $0$ replaced by the symbol bit0 and each bit $1$ by the
symbol bit1 of $\Gamma'$. Started at the adapter label pre0 with empty local state, $b$ on the
input stack and all other stacks empty, the wrapped machine is after exactly $2(k + 1) + 1$ steps
at the label $\mathrm{trNormal}(c, \mathrm{halt})$ at which Mathlib's code-evaluating machine
$\mathrm{tr}$ starts evaluating $c$, with empty local state, $\beta(b)$ followed by the symbol
cons on the main stack and all other stacks empty.

Formalized by `MetaMathlibExt.TM2Recursive.pre_phase`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#pre-phase).

## The first post-phase loop of the wrapped machine

Write $\Gamma'$ for the stack alphabet of
Mathlib's code evaluator. Let $c$ be a code, $b$ a list of bits of length $k$, $r$ a list of
symbols of $\Gamma'$, $o$ a list of bits and $v$ an internal state (a symbol of $\Gamma'$ or
none), and write $\beta(b)$ for $b$ with each bit $\mathrm{true}$ replaced by the symbol bit1 and
each bit $\mathrm{false}$ by the symbol bit0 of $\Gamma'$. Started at the adapter label post1
with internal state $v$, $\beta(b)$ followed by the symbol cons on the main stack, $r$ on the rev
stack, $o$ on the output stack and all other stacks empty, the wrapped machine of $c$ is after
exactly $k + 1$ steps at the adapter label post2 with internal state cons, the reversal of
$\beta(b)$ followed by $r$ on the rev stack, $o$ on the output stack and all other stacks
empty.

Formalized by `MetaMathlibExt.TM2Recursive.post1_loop`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#post1-loop).

## Post-phase of the wrapped machine

Let $c$ be a code and $b$ a list of bits of length
$k$, and write $\beta(b)$ for $b$ with each bit $0$ replaced by the symbol bit0 and each bit $1$ by
the symbol bit1 of $\Gamma'$. Started at the adapter label post1 with empty local state, $\beta(b)$
followed by the symbol cons on the main stack and all other stacks empty, the wrapped machine is
after exactly $2(k + 1)$ steps in the halting configuration (no label) with empty local state,
$b$ on the output stack and all other stacks empty.

Formalized by `MetaMathlibExt.TM2Recursive.post_phase`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#post-phase).

## Lifting stacks of tr

Given contents $s$ of the four stacks main, rev, aux and stack of
Mathlib's code-evaluating machine $\mathrm{tr}$, the stack contents of the wrapped machine that
agree with $s$ on these four stacks and have empty input and output stacks.

Formalized by `MetaMathlibExt.TM2Recursive.liftStk`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#lift-stk).

## Correspondence of labels between the code evaluator and the wrapped machine

Let $c$ be a
code for a partial recursive function on lists of natural numbers and let $\mathrm{tr}$ be
Mathlib's multi-stack machine that evaluates such codes. An optional label $o$ of $\mathrm{tr}$
(a label, or none for halting) corresponds to an optional label $o'$ of the wrapped machine for
$c$ when either $o$ is none and $o'$ is the first post-phase label $\mathrm{post}_1$, or $o$ is a
label $l$ of $\mathrm{tr}$ that lies in the support $\mathrm{supp}(c)$ of $c$ and $o'$ is $l$,
read as a label of the wrapped machine.

Formalized by `MetaMathlibExt.TM2Recursive.LabelRel`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#label-rel).

## Simulation relation between the code evaluator and the wrapped machine

A configuration $x$
of Mathlib's code evaluator $\mathrm{tr}$ is related to a configuration $d$ of the wrapped machine
of a code $c$ when $d$ has the same internal state as $x$, the stacks of $d$ are the four stacks
of $x$ together with empty input and output stacks, and the labels correspond: if $x$ has halted
then $d$ is at the first post-phase label, and if $x$ is at a label $l$ then $l$ lies in the
support of $c$ and $d$ is at $l$.

Formalized by `MetaMathlibExt.TM2Recursive.TrRel`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#tr-rel).

## Reachability gives an iteration count

Let $\alpha$ be a type, let $\bot \notin \alpha$,
and let $f : \alpha \to \alpha \cup \{\bot\}$ be a partial step function, where $f(x) = \bot$
means that no step is possible from $x$. Extend $f$ to
$\bar f : \alpha \cup \{\bot\} \to \alpha \cup \{\bot\}$ by $\bar f(\bot) = \bot$. If $b \in \alpha$
is reachable from $a \in \alpha$ under $f$, that is, $b$ is obtained from $a$ by finitely many
(possibly zero) steps $x \mapsto f(x)$ none of which gives $\bot$, then there is $N \in \mathbb{N}$
with $\bar f^{N}(a) = b$.

Formalized by `MetaMathlibExt.TM2Recursive.exists_iterate_eq_of_reaches`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#exists-iterate-eq-of-reaches).

## Main phase of the wrapped machine

Let $c$ be a code and $f : \mathbb{N} \to \mathbb{N}$
such that $c$ evaluates to $[f(n)]$ on input $[n]$ for every $n$. Then for every $n$ there is
$N$ such that the wrapped machine, started at the label $\mathrm{trNormal}(c, \mathrm{halt})$ with
empty local state, the encoding $\mathrm{trList}([n])$ on the main stack and all other stacks
empty, is after exactly $N$ steps at the adapter label post1 with empty local state,
$\mathrm{trList}([f(n)])$ on the main stack and all other stacks empty.

Formalized by `MetaMathlibExt.TM2Recursive.main_phase`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#main-phase).

## The evaluator's encoding of a one-element list

For every natural number $m$, the list of
stack symbols by which Mathlib's code evaluator encodes the one-element list $[m]$ is the binary
encoding of $m$ (least significant bit first) with each bit written as $\mathrm{bit1}$ if it is
true and as $\mathrm{bit0}$ if it is false, followed by the symbol $\mathrm{cons}$.

Formalized by `MetaMathlibExt.TM2Recursive.trList_singleton`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#tr-list-singleton).

## The wrapped machine computes the function a code evaluates

Let $c$ be a code and
$f : \mathbb{N} \to \mathbb{N}$ a function such that, for every $n$, evaluating $c$ on the
one-element list $[n]$ returns $[f(n)]$. Then the wrapped machine of $c$, with input and output
alphabet the booleans, computes $f$ under the binary encoding of natural numbers (least
significant bit first): for every $n$, started with the encoding of $n$ on its input stack and
all other stacks empty, it eventually halts in its initial internal state with the encoding of
$f(n)$ on its output stack and all other stacks empty.

Formalized by `MetaMathlibExt.TM2Recursive.tm2ComputableOfCode`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 461](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L461). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#tm2-computable-of-code).

## Recursive functions are Turing-computable

Every computable function
$f : \mathbb{N} \to \mathbb{N}$ is computed by a finite multi-stack Turing machine (finitely
many stacks, labels and internal states) whose input and output alphabets are identified with
the booleans, under the binary encoding of natural numbers (least significant bit first, with
$0$ encoded as the empty list): for every $n$, the machine started with the encoding of $n$ on
its input stack and all other stacks empty eventually halts in its initial internal state with
the encoding of $f(n)$ on its output stack and all other stacks empty.

Formalized by `MetaMathlibExt.TM2Recursive.tm2Computable_of_computable`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean, line 506](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/ToTM2.lean#L506). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#tm2-computable-of-computable).

## Turing computable equals recursive

A function $f : \mathbb{N} \to \mathbb{N}$ is
computable (recursive) if and only if some bundled finite multi-stack Turing machine computes it
in binary. Here the binary word of $m \in \mathbb{N}$ is its list of binary digits, least
significant first, with $1$ read as true, $0$ as false and no leading zeros (so the word of $0$
is empty). That is, there are such a machine and identifications of its input and output stack
alphabets with the booleans such that, for every $n \in \mathbb{N}$, the machine started at its
main label in its initial internal state, with the binary word of $n$ on its input stack and
every other stack empty, reaches the halted configuration whose output stack holds the binary
word of $f(n)$, whose other stacks are empty and whose internal state is the initial one.

Formalized by `MetaMathlibExt.TM2Recursive.computable_iff_nonempty_tm2Computable`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/Equiv.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/Equiv.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#computable-iff-nonempty-tm2-computable).

## Halting of a multi-stack machine on an input

A bundled finite multi-stack Turing
machine halts on a word $l$ over its input alphabet when its evaluation from the initial
configuration on $l$ (the main label, the initial internal state, $l$ on the input stack and
every other stack empty) is defined, that is, its run from that configuration reaches a
configuration without successor.

Formalized by `MetaMathlibExt.TM2Recursive.TM2HaltsOn`, a definition declared in [MathlibExt/Computability/TuringMachine/Recursive/Halts.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/Halts.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#tm2-halts-on).

## A run that stops passes through a configuration without successor

Let
$f : \sigma \to \mathrm{Option}\ \sigma$ be a step function and $a \in \sigma$, and write
$f^{(k)}(a) \in \mathrm{Option}\ \sigma$ for the result of $k$ steps from $a$: the $k$-th
iterate, applied to $\mathrm{some}\ a$, of the map sending $\mathrm{none}$ to $\mathrm{none}$
and $\mathrm{some}\ x$ to $f(x)$. If $f^{(k)}(a) = \mathrm{none}$ for some $k$, then there are
$j \in \mathbb{N}$ and $b \in \sigma$ with $f^{(j)}(a) = \mathrm{some}\ b$ and
$f(b) = \mathrm{none}$.

Formalized by `MetaMathlibExt.TM2Recursive.exists_iterate_eq_some_of_eq_none`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/Halts.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/Halts.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#exists-iterate-eq-some-of-eq-none).

## A run halts iff it reaches a configuration without successor

Let
$f : \sigma \to \mathrm{Option}\ \sigma$ be a step function and $a \in \sigma$, and write
$f^{(k)}(a) \in \mathrm{Option}\ \sigma$ for the result of $k$ steps from $a$: the $k$-th
iterate, applied to $\mathrm{some}\ a$, of the map sending $\mathrm{none}$ to $\mathrm{none}$
and $\mathrm{some}\ x$ to $f(x)$. The evaluation of $f$ from $a$ (the configuration where the run
from $a$ stops) is defined if and only if there are $k \in \mathbb{N}$ and $b \in \sigma$ with
$f^{(k)}(a) = \mathrm{some}\ b$ and $f(b) = \mathrm{none}$.

Formalized by `MetaMathlibExt.TM2Recursive.dom_eval_iff_exists_iterate`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/Halts.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/Halts.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#dom-eval-iff-exists-iterate).

## A run stays stopped after a configuration without successor

Let
$f : \sigma \to \mathrm{Option}\ \sigma$ be a step function and $a, b \in \sigma$, and write
$f^{(k)}(a) \in \mathrm{Option}\ \sigma$ for the result of $k$ steps from $a$: the $k$-th
iterate, applied to $\mathrm{some}\ a$, of the map sending $\mathrm{none}$ to $\mathrm{none}$
and $\mathrm{some}\ x$ to $f(x)$. If $f^{(k)}(a) = \mathrm{some}\ b$ and $f(b) = \mathrm{none}$,
then $f^{(m)}(a) = \mathrm{none}$ for every $m > k$.

Formalized by `MetaMathlibExt.TM2Recursive.iterate_eq_none_of_lt`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/Halts.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/Halts.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#iterate-eq-none-of-lt).

## The halting set of a multi-stack machine is r.e

For every bundled finite multi-stack
Turing machine and every identification of its input alphabet with the booleans, the predicate
on $\mathbb{N}$ that holds at $n$ exactly when the machine halts on the binary digits of $n$
(least significant first, with $1$ read as true, $0$ as false and no leading zeros, so that $0$
gives the empty word) is recursively enumerable.

Formalized by `MetaMathlibExt.TM2Recursive.rePred_tm2HaltsOn`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/Halts.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/Halts.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#re-pred-tm2-halts-on).

## The wrapped machine of a code halts exactly where the code is defined

Let $c$ be a code
for a partial recursive function on lists of natural numbers and $n \in \mathbb{N}$, and suppose
that every value of $c$ on the one-element list $[n]$ is itself a one-element list. Then the
wrapped multi-stack machine of $c$ halts on the binary digits of $n$ (least significant first,
with $1$ read as true, $0$ as false and no leading zeros, so that $0$ gives the empty word) if
and only if the evaluation of $c$ at $[n]$ is defined.

Formalized by `MetaMathlibExt.TM2Recursive.tm2HaltsOn_fwdTM_iff`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/Halts.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/Halts.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#tm2-halts-on-fwd-tm-iff).

## Every r.e. predicate is the halting set of a machine with finite alphabets

For every
recursively enumerable predicate $p$ on $\mathbb{N}$ there are a bundled finite multi-stack Turing
machine whose stack alphabets are all finite and an identification of its input alphabet with
the booleans such that, for every $n \in \mathbb{N}$, $p(n)$ holds if and only if the machine
halts on the binary digits of $n$ (least significant first, with $1$ read as true, $0$ as false
and no leading zeros, so that $0$ gives the empty word).

Formalized by `MetaMathlibExt.TM2Recursive.exists_finite_tm2HaltsOn_iff_of_rePred`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/Halts.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/Halts.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#exists-finite-tm2-halts-on-iff-of-re-pre).

## Every r.e. predicate is the halting set of a multi-stack machine

For every recursively
enumerable predicate $p$ on $\mathbb{N}$ there are a bundled finite multi-stack Turing machine
and an identification of its input alphabet with the booleans such that, for every
$n \in \mathbb{N}$, $p(n)$ holds if and only if the machine halts on the binary digits of $n$
(least significant first, with $1$ read as true, $0$ as false and no leading zeros, so that $0$
gives the empty word).

Formalized by `MetaMathlibExt.TM2Recursive.exists_tm2HaltsOn_iff_of_rePred`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/Halts.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/Halts.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#exists-tm2-halts-on-iff-of-re-pred).

## R.e. predicates are the halting sets of multi-stack machines

A predicate $p$ on
$\mathbb{N}$ is recursively enumerable if and only if there are a bundled finite multi-stack
Turing machine and an identification of its input alphabet with the booleans such that, for
every $n \in \mathbb{N}$, $p(n)$ holds if and only if the machine halts on the binary digits of
$n$ (least significant first, with $1$ read as true, $0$ as false and no leading zeros, so that
$0$ gives the empty word).

Formalized by `MetaMathlibExt.TM2Recursive.rePred_iff_exists_tm2HaltsOn`, a theorem declared in [MathlibExt/Computability/TuringMachine/Recursive/Halts.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Recursive/Halts.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#re-pred-iff-exists-tm2-halts-on).

## Recursive functions are the Turing-computable functions

A function
$f : \mathbb{N} \to \mathbb{N}$ is computable, that is, total recursive, if and only if some finite
multi-stack Turing machine computes it on binary representations: there are a machine with
finitely many stacks, internal states and program labels and bijections from its input and output
stack alphabets to $\{0, 1\}$ such that, for every $n \in \mathbb{N}$, the machine started in its
initial state with the binary representation of $n$ (least significant bit first, with $0$
written as the empty word) on its input stack and all other stacks empty halts with the binary
representation of $f(n)$ on its output stack, all other stacks empty and its internal state back
at the initial state.

## Sources

- A. M. Turing, *On Computable Numbers* (1936); S. C. Kleene, *General recursive functions of natural numbers* (1936). Knill, *Some fundamental theorems in mathematics*, §23. Problem `turing_recursive_equiv` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.TheoryOfComputation.TuringRecursiveWanted.ModelTheory.TuringRecursive.turing_recursive_equiv` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/TuringRecursiveWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/TheoryOfComputation/TuringRecursiveWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html#turing-recursive-equiv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Equivalence of Turing machines and recursive functions](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/equivalence-of-models/equivalence-of-turing-machines-and-recursive-fun)
