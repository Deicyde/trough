---
declaration: section
origin: cited
lean: Cslib.Complexity.CookLevin.Assembly.HK, Cslib.Complexity.CookLevin.Assembly.HΓ, Cslib.Complexity.CookLevin.Assembly.eU, Cslib.Complexity.CookLevin.Assembly.eS, Cslib.Complexity.CookLevin.Assembly.eH, Cslib.Complexity.CookLevin.Assembly.eA, Cslib.Complexity.CookLevin.Assembly.eI, Cslib.Complexity.CookLevin.Assembly.embU
statement: formalized
proof: formalized
---

# Cook-Levin: the five generators as sub-machines of one host

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html).

## Host stacks and the five embeddings

## Stacks of the Cook–Levin host machine

The host has a shared output stack, an input-code
stack, and five private counter blocks: an update block and a situation-definition block, each
with one stack per counter of the family generator, and a shift block, an accept block and an
init block, with one stack per counter of the shift, accept and init generator respectively.

Formalized by `Cslib.Complexity.CookLevin.Assembly.HK`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#hk).

## Alphabets of the Cook–Levin host machine

For $g \in \mathbb{N}$, the host stacks carry
the following alphabets: the shared output stack holds Booleans, the input-code stack holds codes
in $\{0, \dots, g - 1\}$, and every stack of every private counter block has a one-element
alphabet.

Formalized by `Cslib.Complexity.CookLevin.Assembly.HΓ`, an abbreviation declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#h).

## Host stack renaming for the update generator

The map from the stacks of the
clause-family generator, used as the update generator, to the host stacks that sends the output
stack to the shared output stack and the counter stack of each counter $x$ to the counter $x$ of
the host's update block.

Formalized by `Cslib.Complexity.CookLevin.Assembly.eU`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#e-u).

## Host stack renaming for the situation-definition generator

The map from the stacks of
the clause-family generator, used as the situation-definition generator, to the host stacks that
sends the output stack to the shared output stack and the counter stack of each counter $x$ to
the counter $x$ of the host's situation-definition block.

Formalized by `Cslib.Complexity.CookLevin.Assembly.eS`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#e-s).

## Host stack renaming for the shift generator

The map from the stacks of the shift
generator to the host stacks that sends the output stack to the shared output stack and the
counter stack of each shift counter $x$ to the counter $x$ of the host's shift block.

Formalized by `Cslib.Complexity.CookLevin.Assembly.eH`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#e-h).

## Host stack renaming for the accept generator

The map from the stacks of the accept
generator to the host stacks that sends the output stack to the shared output stack and the
counter stack of each accept counter $x$ to the counter $x$ of the host's accept block.

Formalized by `Cslib.Complexity.CookLevin.Assembly.eA`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#e-a).

## Host stack renaming for the init generator

The map from the stacks of the init
generator to the host stacks that sends the output stack to the shared output stack, the input
stack to the host's input-code stack, and the counter stack of each init counter $x$ to the
counter $x$ of the host's init block.

Formalized by `Cslib.Complexity.CookLevin.Assembly.eI`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#e-i).

## Embedding of the update generator's stacks into the host

For $g \in \mathbb{N}$, this is
the stack embedding of the family generator's stacks (a Boolean output stack and one unit counter
stack per counter) into the host stacks with $g$ input codes, used for the update generator: the
output stack goes to the host's shared output stack, and the counter stack $x$ goes to the stack
$x$ of the host's private update block. Distinct stacks go to distinct host stacks, and each
stack's alphabet is identified with its host stack's alphabet by the identity.

Formalized by `Cslib.Complexity.CookLevin.Assembly.embU`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#emb-u).

## Embedding of the situation-definition generator into the host

For $g$ input codes, the
stack embedding of the clause-family generator's stacks, used as the situation-definition
generator, into the host stacks that sends the output stack to the shared output stack and the
counter stack of each counter $x$ to the counter $x$ of the host's situation-definition block,
identifying each stack's alphabet with itself.

Formalized by `Cslib.Complexity.CookLevin.Assembly.embS`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#emb-s).

## Embedding of the shift generator into the host

For $g$ input codes, the stack embedding
of the shift generator's stacks into the host stacks that sends the output stack to the shared
output stack and the counter stack of each shift counter $x$ to the counter $x$ of the host's
shift block, identifying each stack's alphabet with itself.

Formalized by `Cslib.Complexity.CookLevin.Assembly.embH`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#emb-h).

## Embedding of the accept generator into the host

For $g$ input codes, the stack embedding
of the accept generator's stacks into the host stacks that sends the output stack to the shared
output stack and the counter stack of each accept counter $x$ to the counter $x$ of the host's
accept block, identifying each stack's alphabet with itself.

Formalized by `Cslib.Complexity.CookLevin.Assembly.embA`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#emb-a).

## Embedding of the init generator into the host

For $g$ input codes, the stack embedding
of the init generator's stacks (with input alphabet the $g$ codes) into the host stacks that
sends the output stack to the shared output stack, the input stack to the host's input-code
stack, and the counter stack of each init counter $x$ to the counter $x$ of the host's init
block, identifying each stack's alphabet with itself.

Formalized by `Cslib.Complexity.CookLevin.Assembly.embI`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#emb-i).

## Labels of the Cook–Levin host machine

For parameters $N, n_L, K, g, d, n_1, n_Y$, the
host labels consist of a copy of the family generator's labels (for $N$ situations and $n_L$
literals) for the update phase, a second copy of them for the situation-definition phase, a copy
of the shift generator's labels (for $N$ situations, $K$ stacks, $g$ symbols and depth $d$), a
copy of the accept generator's labels (for $n_1$ code clauses and $g$ symbols), a copy of the
init generator's labels (for $g$ symbols and $n_Y$ certificate codes), and one final label.

Formalized by `Cslib.Complexity.CookLevin.Assembly.HL`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#hl).

## Chaining step of the host program

For a host label $l$, the chaining step is the host
statement that sets the Boolean internal state to false (the state in which every generator
starts) and then jumps to $l$.

Formalized by `Cslib.Complexity.CookLevin.Assembly.chain`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#chain).

## The host program

Given the five generator programs (update, situation definition, shift,
accept and init), the host program runs init, then update, then situation definition, then shift,
then accept. At each label of a generator other than its final label, the host executes that
generator's statement with the generator's stacks embedded into the host stacks (output onto the
shared output stack, counters onto the generator's own private counter block, and for init the
input stack onto the host's input-code stack) and its labels renamed into the host's copy of
them. At a generator's final label the host performs one chaining step: it resets the Boolean
state to false and jumps to the start label of the next generator, and after accept it jumps to
the final host label, where it halts.

Formalized by `Cslib.Complexity.CookLevin.Assembly.hprog`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#hprog).

## The host as a finite multi-stack Turing machine

Given the five generator programs (update
and situation-definition programs over the family generator's stacks, a shift program, an accept
program, and an init program whose input alphabet has $g$ codes), the host machine is the finite
multi-stack Turing machine whose stacks are the host stacks, with the input-code stack as input
stack and the shared output stack as output stack, whose alphabets are the host alphabets, whose
labels are the host labels, whose start label is the init generator's start label, whose
internal state is a Boolean with initial value false, and whose program is the host program built
from the five generator programs.

This is a finiteness check only: the input and output stacks are provisional until the
precomputation is attached.

Formalized by `Cslib.Complexity.CookLevin.Assembly.hostTM`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#host-tm).

## Sequencing

Let $P_u$, $P_s$ (update and situation definition), $P_h$ (shift), $P_a$
(accept) and $P_i$ (init) be generator programs that halt at their label `done`, and let $\xi$ be
a list of input codes. Suppose that for each generator $j \in \{u, s, h, a, i\}$ there are counter
values $F_j$, a word $w_j$ and a bound $B_j$ such that, for every output word $o$, the run of $P_j$
from its start label with state bit false, on stacks holding the counters $F_j$ and the output $o$
(for init, also $\xi$ on its input stack), reaches `done` within $B_j$ steps, with some state bit
and with output $w_j o$. Let $o$ be a word and let $S_0$ be host stacks whose output stack holds
$o$, whose input stack holds $\xi$, and whose private block of each generator $j$ holds the
counters $F_j$. Then the host program on $P_u, P_s, P_h, P_a, P_i$, started at the init
generator's start label with state bit false on $S_0$, reaches its final label within
$B_i + B_u + B_s + B_h + B_a + 5$ steps, with some state bit and with output
$w_a w_h w_s w_u w_i o$.

Formalized by `Cslib.Complexity.CookLevin.Assembly.seq_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#seq-run).

## The host on the real generators of a machine

Let $M$ be a finite multi-stack Turing
machine with encoding data $E$, let $Y$ be a list of input symbols, and let $\mathit{acc}$ be an
output symbol. This is the host program whose five generators are the real ones for $M$. The
update generator is the family generator of $E$ for the (label, state) codes, window codes and
next (label, state) codes of the situations of $E$. The situation-definition generator is the
family generator of $E$ for the same (label, state) codes and window codes, with the positions of
the situation variables in place of the next codes. The shift generator is the one of $E$. The
accept generator is the one for the number of (label, state) codes, the code of the halted label
with the initial internal state, the number of the output stack, and the code of $\mathit{acc}$
on the output stack. The init generator is the one for the code of the start label and initial
state of $M$, the number of the input stack, and the sorted distinct codes of the symbols of $Y$.
The input itself is not a parameter: the init generator reads it from the host's input-code
stack.

Formalized by `Cslib.Complexity.CookLevin.Assembly.realProg`, an abbreviation declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#real-prog).

## The formula emitted by the host

Let $M$ be a finite multi-stack Turing machine with
encoding data $E$, let $x$ and $Y$ be lists of input symbols, let $\mathit{acc}$ be an output
symbol, and let $m, T \in \mathbb{N}$. Let $H = m + (T + 1) d + 1$ be the stack cap, where $d$ is
the window depth of $M$. The CNF formula $\Phi(x, Y, \mathit{acc}, m, T)$ is the concatenation, in
this order, of the accept family for $\mathit{acc}$, the shift family, the situation-definition
family, the update family, and the init family for $x$, $Y$ and $m$, all at run length $T$ and
stack cap $H$.

Formalized by `Cslib.Complexity.CookLevin.Assembly.Phi`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#phi).

## Step bound of the host

Let $M$ be a finite multi-stack Turing machine with encoding data
$E$, let $Y$ be a list of input symbols, and let $m, T \in \mathbb{N}$. Let $H = m + (T + 1) d + 1$,
where $d$ is the window depth of $M$, and let $R = T + H + 1$. Let $L$ be the layout of $E$ and $N$
its number of situations. Let $c_I$ be the init generator's constant for $L$, the number of
distinct codes of symbols of $Y$, and the number of the input stack; let $c_F$ be the family
generator's constant for $L$ and $N$; let $c_S$ be the shift generator's constant for $L$ and $N$;
and let $c_A$ be the accept generator's constant for $L$, the number of (label, state) codes, and
the number of the output stack. The step bound is

$$c_I R^5 + c_F R^5 + c_F R^5 + c_S R^6 + c_A R^4 + 5,$$

the bounds of the init, update, situation-definition, shift and accept generators plus five
chaining steps.

Formalized by `Cslib.Complexity.CookLevin.Assembly.realB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#real-b).

## The assembled generator, after the precomputation

Let $E$ be an encoding of a machine
$M$, let $x$ and $Y$ be lists of input symbols of $M$, let $a$ be a symbol of its output stack,
and let $m, T \in \mathbb{N}$ with $|x| \le m$. Put $H = m + (T + 1)d + 1$, where $d$ is the
window depth of $M$. Let $S_0$ be host stacks whose output stack holds a word $o$, whose input
stack holds the symbol codes of $x$ in reverse order, whose update, situation-definition, shift
and accept blocks each hold $T$ on the time counter, $H$ on the height counter and nothing on the
other counters, and whose init block holds $T$, $|x|$, $m - |x|$ and $H - m$ on its four size
counters and nothing on the others. Then the host program on the real generators of $E$ for $Y$
and $a$, started at the init generator's start label with state bit false on $S_0$, reaches its
final label within the step bound $\mathrm{realB}(E, Y, m, T)$ (the five generators' bounds plus
five chaining steps), with some state bit and with output stack the dense encoding of the formula
$\Phi(E, x, Y, a, m, T)$ followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.Assembly.real_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#real-run).

## Correctness of the assembled formula

Let $M$ be a finite multi-stack Turing machine with
encoding data $E$, let $x$ and $Y$ be lists of input symbols of $M$, let $\mathit{acc}$ be an
output symbol of $M$, and let $m, T \in \mathbb{N}$. Suppose that $|x| \le m$ and that
$\mathit{acc}$ is one of the effective symbols of the output stack under $E$. Then the formula
$\Phi(x, Y, \mathit{acc}, m, T)$ emitted by the host is satisfiable if and only if there is a list
$y$ of input symbols, all belonging to $Y$, such that the concatenation $xy$ has length at most
$m$ and the idle-extended run of $M$ from the initial configuration on input $xy$ is, after $T$
steps, an accepting configuration for $\mathit{acc}$: halted, in the initial internal state, with
$\mathit{acc}$ on top of the output stack.

The proof carries the soundness and completeness of the five families through the
concatenation.

Formalized by `Cslib.Complexity.CookLevin.Assembly.phi_iff`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Assembly.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/Assembly.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html#phi-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cook-Levin: the five generators as sub-machines of one host](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-the-five-generators-as-sub-machines-o)
