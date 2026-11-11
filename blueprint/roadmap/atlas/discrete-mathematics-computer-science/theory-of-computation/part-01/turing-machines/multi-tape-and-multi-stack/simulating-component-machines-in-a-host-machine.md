---
declaration: section
origin: cited
lean: Cslib.Complexity.Host.Comp, Cslib.Complexity.Host.HK, Cslib.Complexity.Host.allKs, Cslib.Complexity.Host.HΓ, Cslib.Complexity.Host.P0, Cslib.Complexity.Host.HLab, Cslib.Complexity.Host.HLab.equiv, Cslib.Complexity.Host.emb
statement: formalized
proof: formalized
---

# Simulating component machines in a host machine

37 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html).

## Component machine

A component machine consists of a finite type $K$ of stacks with
decidable equality, a finite alphabet $\Gamma_k$ for each stack $k$, a finite type $L$ of labels
with decidable equality, a multi-stack Turing machine program assigning to each label in $L$ a
statement over the alphabets $\Gamma$ and the labels $L$ with Boolean internal state, and a list
of the stacks in which every stack occurs exactly once, so that a host can empty all of them.

Formalized by `Cslib.Complexity.Host.Comp`, a structure declared in [CSLibExt/Computability/Complexity/Host.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#comp).

## Stacks of the generic host

For a component machine $c$ with stack indices $K$, the host
stacks are an input stack, an output stack, two buffers $X_1$ and $W_1$ used in phase 0 (which
moves the input onto the component's stacks), and one copy of each component stack $k \in K$.

Formalized by `Cslib.Complexity.Host.HK`, an inductive type declared in [CSLibExt/Computability/Complexity/Host.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#hk).

## The list of host stacks

For a component machine $c$, the host stacks are listed as the
input stack, the output stack, the two buffer stacks $X_1$ and $W_1$, and then the host's copies
of the stacks of $c$, in the order of the list of stacks that $c$ carries.

Formalized by `Cslib.Complexity.Host.allKs`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#all-ks).

## Alphabets of the generic host

For a component machine $c$ with stack alphabets
$(\Gamma_k)_k$ and a type $\alpha$, the alphabet of a host stack is $\alpha$ on the input stack,
$\Gamma_k$ on the host copy of the component's stack $k$, and the booleans on the output stack and
on the two phase-0 buffers.

Formalized by `Cslib.Complexity.Host.HΓ`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#h).

## Phase-0 labels of the generic host

The six labels of a host's phase 0, which moves the
input onto the component's stacks: two for the two passes that move the first block $x$, one that
drops the separator, two for the two passes that move the second block $w$, and one that resets
the state and starts the component.

Formalized by `Cslib.Complexity.Host.P0`, an inductive type declared in [CSLibExt/Computability/Complexity/Host.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#p0).

## Labels of the generic host

For a component machine $c$ with labels $L$, and with $P_0$ the
set of phase-0 labels, the host labels are one label for each $p \in P_0$, one copy of each
component label $l \in L$, and, for each boolean answer $a$, a cleanup label and an output label
carrying $a$.

Formalized by `Cslib.Complexity.Host.HLab`, an inductive type declared in [CSLibExt/Computability/Complexity/Host.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#hlab).

## Labels of the generic host as a sum type

For a component machine $c$ with labels $L$, let
$P_0$ be the set of phase-0 labels and $B = \{\mathrm{false}, \mathrm{true}\}$. The host labels of
$c$ are in bijection with the disjoint union $P_0 \sqcup L \sqcup B \sqcup B$: the phase-0 label
$p$ corresponds to $p$, the host copy of the component label $l$ to $l$, the cleanup label with
answer $a$ to $a$ in the first copy of $B$, and the output label with answer $a$ to $a$ in the
second copy of $B$.

The bijection shows that there are finitely many host labels.

Formalized by `Cslib.Complexity.Host.HLab.equiv`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#equiv).

## The component's stacks inside a host

For a component machine $c$ and an input alphabet
$\alpha$, the stack embedding of $c$ into the host over $\alpha$ sends each stack $k$ of $c$ to
the host's copy of $k$, whose alphabet is the alphabet $\Gamma_k$ of $k$, and identifies the two
alphabets by the identity. Distinct stacks have distinct copies, so the embedding is injective.

Formalized by `Cslib.Complexity.Host.emb`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#emb).

## Agreement with the embedded component

Let $c$ be a component machine and $\alpha$ an
input alphabet. For stack contents $S$ of $c$ and stack contents $T$ of the host over $\alpha$,
$T$ agrees with $S$ under the embedding of the component's stacks into the host if and only if,
for every stack $k$ of $c$, the host's copy of $k$ holds exactly $S(k)$.

Formalized by `Cslib.Complexity.Host.agree_emb`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#agree-emb).

## Moving a bit block through a buffer

Let $a$, $t$, $b$ be pairwise distinct stacks of a
program $M$ with Boolean state, and let $l_1$, $l_2$, $l_3$ be labels such that $M$ runs at $l_1$
the bit-moving loop from $a$ to $t$ with decoder $d$ and encoder $g_t$, looping at $l_1$ and
exiting to $l_2$, and at $l_2$ the bit-moving loop from $t$ to $b$ with decoder $d_t$ and encoder
$g$, looping at $l_2$ and exiting to $l_3$, where $d_t$ decodes $g_t(y)$ to $y$ for every bit $y$.
Let $x = x_1 \cdots x_n$ be a bit list and $S$ stack contents in which $a$ holds a bit block for
$x$ under $d$ followed by a rest $A$ that ends a bit block under $d$, and $t$ is empty. Then for
every state $v$ there are a state $v'$ and stack contents $S'$ such that $M$ runs in exactly
$2n + 2$ steps from label $l_1$, state $v$ and stacks $S$ to label $l_3$, state $v'$ and stacks
$S'$, where $S'(a) = A$, $S'(t)$ is empty, $S'(b)$ is $g(x_1), \dots, g(x_n)$ (top first)
followed by $S(b)$, and $S'(k) = S(k)$ for every other stack $k$.

Formalized by `Cslib.Complexity.Host.move2_run`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#move2-run).

## Cleanup stacks of the generic host

For a component machine $c$ and a host stack $o$, the
cleanup stacks are the list of all host stacks with $o$ removed, in the order of the list of
host stacks. The cleanup empties these stacks and leaves the output stack $o$.

Formalized by `Cslib.Complexity.Host.cleanKs`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#clean-ks).

## Membership in the cleanup stacks of the generic host

For a component machine $c$ and host
stacks $o$ and $k$, the stack $k$ belongs to the list of stacks that the cleanup for the output
stack $o$ empties if and only if $k \ne o$.

Formalized by `Cslib.Complexity.Host.mem_cleanKs`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#mem-clean-ks).

## Cleanup in a host

Let $c$ be a component machine, $\alpha$ an input alphabet, $o$ a host
stack, $a$ a bit, and $M$ a host program with Boolean state whose statement at the cleanup label
for $a$ is the cleanup round on the list of all host stacks with $o$ removed, kept in the order
of the list of host stacks, repeating at the cleanup label for $a$ and exiting to the output
label for $a$. If $S$ assigns to every host stack at most $m$ symbols, then for every state $v$,
$M$ runs from the cleanup label for $a$ with state $v$ and stacks $S$ to the output label for $a$
in at most $m + 1$ steps, ending with state false, stack $o$ holding $S(o)$ and every other stack
empty.

Formalized by `Cslib.Complexity.Host.cleanup_run`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#cleanup-run).

## Stack lengths grow by at most the push bound per step

Let $M$ be a finite multi-stack
Turing machine with push bound $B$. If every stack of $S$ has length at most $N$ and $M$ runs in
$n$ steps from a configuration with some label, state $v$ and stacks $S$ to a configuration with
some label, state $v'$ and stacks $S'$, then every stack of $S'$ has length at most $N + Bn$.

Formalized by `Cslib.Complexity.Host.stk_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#stk-length-le).

## Initial configuration of a finite multi-stack machine

For a finite multi-stack Turing
machine $M$ with input stack $k_0$, main label $\lambda_0$ and initial internal state $\sigma_0$,
and a list $l$ over the alphabet of $k_0$, the initial configuration of $M$ on $l$ has current
label $\lambda_0$, internal state $\sigma_0$, the list $l$ on $k_0$ and every other stack empty.

Formalized by `Cslib.Complexity.Host.initList_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#init-list-eq).

## Halting configuration of a finite multi-stack machine

For a finite multi-stack Turing
machine $M$ with output stack $k_1$ and initial internal state $\sigma_0$, and a list $l$ over the
alphabet of $k_1$, the halting configuration of $M$ with output $l$ has no current label, internal
state $\sigma_0$, the list $l$ on $k_1$ and every other stack empty.

Formalized by `Cslib.Complexity.Host.haltList_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#halt-list-eq).

## Stack lengths when only one stack is filled

Let $c$ be a component machine and consider
its host with input alphabet $\alpha$. If a host stack $o$ holds a list $l$ and every other host
stack is empty, then every host stack has length at most the length of $l$.

Formalized by `Cslib.Complexity.Host.update_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#update-length-le).

## Component labels in the reduction host

For a component with exit label $\mathit{done}$,
the label $\mathit{done}$ is sent to the host's cleanup label with answer false, and every other
component label $l$ to the host label that runs the component at $l$.

Formalized by `Cslib.Complexity.Host.φR`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#r).

## Reduction host program

The program of the reduction host for a component with stacks
$c_X$ and $c_O$, an encoding $g_X$ of bits as symbols of $c_X$ and labels $\mathit{start}$ and
$\mathit{done}$. Phase 0 moves the whole input stack onto the buffer $X_1$ with the bit-moving
loop, then moves $X_1$ onto the host's copy of $c_X$ re-encoded by $g_X$ (so in the original
order), then sets the state to false and goes to $\mathit{start}$, or to the cleanup if
$\mathit{start} = \mathit{done}$. At the host label of a component label $l$ it runs the
component's statement at $l$ on the host's copies of the component stacks, with every jump to
$\mathit{done}$ sent to the cleanup. The cleanup pops every stack other than the copy of $c_O$
once per round, repeating while something was popped, and then goes to the final label, which
halts. The phase-0 labels for a separator and a second block halt.

Formalized by `Cslib.Complexity.Host.rprog`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#rprog).

## Reduction host machine

The reduction host as a finite multi-stack Turing machine: its
stacks are the host stacks with the host alphabets for bit input, its labels are the host labels,
its state is a bit starting at false, its program is the reduction host program started at the
first phase-0 label, its input stack is the input stack (raw bits) and its output stack is the
host's copy of the component's stack $c_O$.

Formalized by `Cslib.Complexity.Host.rtm`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#rtm).

## Step bound of the reduction host

Let $c$ be a component machine with stacks $c_X$ and
$c_O$, an encoding $g_X$ of bits as symbols of $c_X$ and labels $\mathit{start}$ and
$\mathit{done}$, and let $B$ be the push bound of the reduction host machine built from these
data. For a polynomial $p$ with natural-number coefficients, the step bound of the reduction host
is the polynomial in the variable $X$

$$(B + 1)(2X + 3 + p) + X + 2.$$

At an input length $n$ it counts phase 0 and the component, at most $2n + 3 + p(n)$ steps, then
the cleanup, which takes at most one step more than the longest stack, of length at most $n$
plus $B$ times the steps so far, and the halt.

Formalized by `Cslib.Complexity.Host.rtime`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#rtime).

## The reduction host embeds the component

Let $c$ be a component machine with stacks
$c_X$ and $c_O$, a map $g_X$ from bits to the alphabet of $c_X$, and labels $s$ and $d$,
and suppose that $c$ halts at $d$. Rename the labels of $c$ by sending $d$ to the cleanup label
with answer false and every other label $l$ to the host's copy of $l$, and embed the stacks of
$c$ as the host's copies over the bit input alphabet. Then the reduction host built from
$c_X$, $c_O$, $g_X$, $s$ and $d$ embeds $c$: for every label $l$ of $c$, either $c$ halts at
$l$, or the host's statement at the renamed label of $l$ is the statement of $c$ at $l$ with
stacks and labels translated.

Formalized by `Cslib.Complexity.Host.embeds_rprog`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#embeds-rprog).

## The reduction host's run on one input

Let $c$ be a component with stacks $c_X$ and $c_O$,
an encoding $g_X$ of bits as symbols of $c_X$, an identification $e_O$ of the alphabet of $c_O$
with the bits, and labels $\mathit{start}$ and $\mathit{done}$, where the component halts at
$\mathit{done}$. Let $p$ be a polynomial with natural-number coefficients and $x$, $o$ bit lists,
and suppose that the component, started at $\mathit{start}$ with state false, with $x$ encoded by
$g_X$ on $c_X$ and every other stack empty, reaches $\mathit{done}$ within $p(|x|)$ steps with
some state and stacks in which $c_O$ holds $o$ translated symbol by symbol by $e_O^{-1}$. Then the
reduction host program, started at its first phase-0 label with state false, $x$ on the input
stack and every other stack empty, halts within $T(|x|)$ steps, where $T$ is the reduction host's
step bound for $p$, with state false, $o$ translated by $e_O^{-1}$ on the host's copy of $c_O$ and
every other stack empty.

Formalized by `Cslib.Complexity.Host.rprog_run_at`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#rprog-run-at).

## The reduction host's run

Let $c$ be a component with stacks $c_X$ and $c_O$, an encoding
$g_X$ of bits as symbols of $c_X$, an identification $e_O$ of the alphabet of $c_O$ with the bits,
and labels $\mathit{start}$ and $\mathit{done}$, where the component halts at $\mathit{done}$. Let
$f$ be a function from bit lists to bit lists and $p$ a polynomial with natural-number
coefficients, and suppose that for every bit list $y$ the component, started at $\mathit{start}$
with state false, with $y$ encoded by $g_X$ on $c_X$ and every other stack empty, reaches
$\mathit{done}$ within $p(|y|)$ steps with some state and stacks in which $c_O$ holds $f(y)$
translated symbol by symbol by $e_O^{-1}$. Then for every bit list $x$ the reduction host program,
started at its first phase-0 label with state false, $x$ on the input stack and every other stack
empty, halts within $T(|x|)$ steps, where $T$ is the reduction host's step bound for $p$, with
state false, $f(x)$ translated by $e_O^{-1}$ on the host's copy of $c_O$ and every other stack
empty.

Formalized by `Cslib.Complexity.Host.rprog_run`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#rprog-run).

## Reduction host

Let $c$ be a component with stacks $c_X$ and $c_O$, an encoding $g_X$ of
bits as symbols of $c_X$, an identification $e_O$ of the alphabet of $c_O$ with the bits, and
labels $\mathit{start}$ and $\mathit{done}$, where the component halts at $\mathit{done}$. Let $f$
be a function from bit lists to bit lists and $p$ a polynomial with natural-number coefficients.
Suppose that for every bit list $x$ the component, started at $\mathit{start}$ with state false,
with $x$ encoded by $g_X$ on $c_X$ and every other stack empty, reaches $\mathit{done}$ within
$p(|x|)$ steps with some state and stacks in which $c_O$ holds $f(x)$ translated symbol by symbol
by $e_O^{-1}$. Then $f$ is computable in polynomial time on raw bit lists (the identity as input
and output encoding): by the reduction host machine, with the bits as input alphabet, $e_O$ as
output alphabet and the reduction host's step bound for $p$ as time bound.

Formalized by `Cslib.Complexity.Host.reduction`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#reduction).

## Reduction host, canonical form

Let $c$ be a component machine with stacks $c_X$ and
$c_O$ and labels $\mathit{start}$ and $\mathit{done}$, where the statement at $\mathit{done}$ is
the halting statement. Let $g_X$ map bits to symbols of $c_X$, let $e_O$ be a bijection from the
alphabet of $c_O$ to the booleans, let $f$ map bit lists to bit lists, and let $p$ be a polynomial
with coefficients in $\mathbb{N}$. Suppose that for every bit list $x$, the component started at
$\mathit{start}$ with internal state false, with $g_X$ applied to each bit of $x$ on $c_X$ and
every other stack empty, reaches the label $\mathit{done}$ in at most $p(|x|)$ steps with stack
$c_O$ holding exactly $e_O^{-1}$ applied to each bit of $f(x)$. Then $f$ is polynomial-time
computable for the canonical bitstring encodings.

Formalized by `Cslib.Complexity.Host.isPolyTime_reduction`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#is-poly-time-reduction).

## Decider host

Let $c$ be a component machine with stacks $c_X$ and $c_O$ and labels
$\mathit{start}$ and $\mathit{done}$, where the statement at $\mathit{done}$ is the halting
statement. Let $g_X$ map bits to symbols of $c_X$, let $e_O$ be a bijection from the alphabet of
$c_O$ to the booleans, let $L$ map bit lists to booleans, and let $p$ be a polynomial with
coefficients in $\mathbb{N}$. Suppose that for every bit list $x$, the component started at
$\mathit{start}$ with internal state false, with $g_X$ applied to each bit of $x$ on $c_X$ and
every other stack empty, reaches the label $\mathit{done}$ in at most $p(|x|)$ steps with exactly
the one symbol $e_O^{-1}(L(x))$ on $c_O$. Then $L$ is polynomial-time computable for the
canonical bitstring encodings, that is, $L$ belongs to the class $\mathrm{P}$ of decision
problems decidable in polynomial time.

The proof applies the reduction host to $x \mapsto [L(x)]$, read with the one-bit encoding of the
booleans.

Formalized by `Cslib.Complexity.Host.isPolyTime_decider`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#is-poly-time-decider).

## Relabelling in the verifier host

Given labels $\mathit{yes}$ and $\mathit{no}$ of a
component machine $c$, a label $l$ of $c$ is sent to the host label that starts the cleanup with
answer true if $l = \mathit{yes}$, to the host label that starts the cleanup with answer false if
$l \ne \mathit{yes}$ and $l = \mathit{no}$, and to the host label that runs the component at $l$
otherwise.

Formalized by `Cslib.Complexity.Host.φV`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#v).

## Reading a bit of $x$

On the pair alphabet of the $x \# w$ input, the symbol that
encodes a bit $b$ of $x$ (the left injection of $b$) is read as the bit $b$; every other symbol,
the separator $\#$ or a bit of $w$ (both right injections), is read as no bit.

Formalized by `Cslib.Complexity.Host.dX`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#d-x).

## Reading a bit of $w$

On the pair alphabet of the $x \# w$ input, the symbol that
encodes a bit $b$ of $w$ (the right injection of $\mathrm{some}\,b$) is read as the bit $b$;
every other symbol, a bit of $x$ (a left injection) or the separator $\#$ (the right injection
of $\mathrm{none}$), is read as no bit.

Formalized by `Cslib.Complexity.Host.dW`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#d-w).

## Verifier host program

The program of the verifier host for a component machine $c$ with
stacks $c_X$ and $c_W$, encodings $g_X$ and $g_W$ of bits as symbols of $c_X$ and $c_W$, and
labels $\mathit{start}$, $\mathit{yes}$ and $\mathit{no}$, on the host stacks with the work
alphabet of the dense-SAT verifier on the input stack. On an input $x \# w$ in the pair encoding,
phase 0 moves the symbols on top of the input stack that encode bits of $x$ onto the buffer $X_1$
with the bit-moving loop, then moves $X_1$ onto the host's copy of $c_X$ re-encoded by $g_X$ (so
in the original order); it pops one symbol off the input stack (the separator $\#$); it moves
the symbols that encode bits of $w$ onto the buffer $W_1$ and then $W_1$ onto the host's copy of
$c_W$ re-encoded by $g_W$; then it sets the state to false and goes to the renamed label of
$\mathit{start}$. Here a label of $c$ is renamed to the cleanup label with answer true if it is
$\mathit{yes}$, to the cleanup label with answer false if it is $\mathit{no}$ but not
$\mathit{yes}$, and to the host's copy of itself otherwise. At the host's copy of a component
label $l$ it runs the component's statement at $l$ on the host's copies of the component stacks,
with every jump target renamed. The cleanup label with answer $a$ pops every stack other than the
output stack once per round, repeating while something was popped, and then goes to the output
label with answer $a$, which pushes $a$ on the output stack and halts.

Formalized by `Cslib.Complexity.Host.vprog`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#vprog).

## The verifier host machine

The verifier host as a finite multi-stack Turing machine for a
component machine $c$: its stacks are the host stacks, with the pair alphabet on the input stack,
the alphabets of $c$ on the component's stacks and bits on the other stacks; its labels are the
host labels and its program is the verifier host program; it starts at the first phase-0 label
with a boolean internal state, initially false; it reads its input from the input stack and leaves
its output on the output stack.

Formalized by `Cslib.Complexity.Host.vtm`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#vtm).

## Step bound of the verifier host

Let $c$ be a component machine with stacks $c_X$ and
$c_W$, encodings $g_X$ and $g_W$ of bits as symbols of $c_X$ and $c_W$, and labels
$\mathit{start}$, $\mathit{yes}$ and $\mathit{no}$, and let $B$ be the push bound of the verifier
host machine built from these data. For a polynomial $p$ with natural-number coefficients, the
step bound of the verifier host is the polynomial in the variable $X$

$$(B + 1)(2X + 4 + p) + X + 2.$$

At an input length $n$ it counts phase 0 and the component, at most $2n + 4 + p(n)$ steps, then
the cleanup, which takes at most one step more than the longest stack, of length at most $n$
plus $B$ times the steps so far, and the output step.

Formalized by `Cslib.Complexity.Host.vtime`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#vtime).

## The verifier host embeds the component

Let $c$ be a component machine with stacks $c_X$
and $c_W$, maps $g_X$ and $g_W$ from bits to the alphabets of $c_X$ and $c_W$, and labels
$\mathit{start}$, $\mathit{yes}$ and $\mathit{no}$, and suppose that the statement of $c$ at
$\mathit{yes}$ and the statement of $c$ at $\mathit{no}$ are the halt statement. Rename the labels
of $c$ by sending $\mathit{yes}$ to the cleanup label with answer true, $\mathit{no}$ (when it
differs from $\mathit{yes}$) to the cleanup label with answer false, and every other label $l$ to
the host's copy of $l$, and embed the stacks of $c$ as the host's copies over the work alphabet
of the dense-SAT verifier. Then the verifier host program built from $c_X$, $c_W$, $g_X$, $g_W$,
$\mathit{start}$, $\mathit{yes}$ and $\mathit{no}$ embeds $c$: for every label $l$ of $c$, either
the statement of $c$ at $l$ is the halt statement, or the host's statement at the renamed label
of $l$ is the statement of $c$ at $l$ with stacks and labels translated.

Formalized by `Cslib.Complexity.Host.embeds_vprog`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#embeds-vprog).

## The verifier host's run

Let $c$ be a component machine with stacks $c_X \ne c_W$, maps
$g_X$ and $g_W$ from bits to the alphabets of $c_X$ and $c_W$, and labels $\mathit{start}$,
$\mathit{yes}$ and $\mathit{no}$ with $\mathit{yes} \ne \mathit{no}$, where the program halts at
$\mathit{yes}$ and at $\mathit{no}$. Let $f$ assign a boolean to each pair of bit lists and let
$p$ be a polynomial with natural number coefficients. Suppose that for all bit lists $x$ and $w$,
the component started at $\mathit{start}$ with state false, the bits of $x$ mapped by $g_X$ on
$c_X$, the bits of $w$ mapped by $g_W$ on $c_W$ and every other stack empty reaches the label
$\mathit{yes}$ if $f(x, w)$ is true and $\mathit{no}$ otherwise within $p(|x| + |w|)$ steps. Then
for all bit lists $x$ and $w$, with $n$ the length of the pair encoding of $(x, w)$, the verifier
host program started at its first phase-0 label with state false, the pair encoding of $(x, w)$
on the input stack and every other stack empty halts within $T(n)$ steps, where $T$ is the
verifier host's step bound for $p$, with state false, the one-element list $[f(x, w)]$ on the
output stack and every other stack empty.

Formalized by `Cslib.Complexity.Host.vprog_run`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#vprog-run).

## Verifier host

Let $c$ be a component machine with stacks $c_X \ne c_W$, maps $g_X$ and
$g_W$ from bits to the alphabets of $c_X$ and $c_W$, and labels $\mathit{start}$, $\mathit{yes}$
and $\mathit{no}$ with $\mathit{yes} \ne \mathit{no}$, where the program halts at $\mathit{yes}$
and at $\mathit{no}$. Let $f$ assign a boolean to each pair of bit lists and let $p$ be a
polynomial with natural number coefficients. Suppose that for all bit lists $x$ and $w$, the
component started at $\mathit{start}$ with state false, the bits of $x$ mapped by $g_X$ on $c_X$,
the bits of $w$ mapped by $g_W$ on $c_W$ and every other stack empty reaches the label
$\mathit{yes}$ if $f(x, w)$ is true and $\mathit{no}$ otherwise within $p(|x| + |w|)$ steps. Then
the verifier host machine computes $(x, w) \mapsto f(x, w)$ in polynomial time, with the verifier
host's step bound for $p$ as time bound: on the pair encoding of $(x, w)$, over the pair alphabet,
it outputs the one-element bit list $[f(x, w)]$.

Formalized by `Cslib.Complexity.Host.verifier`, a definition declared in [CSLibExt/Computability/Complexity/Host.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#verifier).

## Verifier host, canonical form

Let $c$ be a component machine with distinct stacks $c_X$
and $c_W$ and labels $\mathit{start}$, $\mathit{yes}$ and $\mathit{no}$, where
$\mathit{yes} \ne \mathit{no}$ and the statements at $\mathit{yes}$ and $\mathit{no}$ are the
halting statement. Let $g_X$ and $g_W$ map bits to symbols of $c_X$ and $c_W$, let $f$ assign a
boolean $f(x, w)$ to all bit lists $x$ and $w$, and let $p$ be a polynomial with coefficients in
$\mathbb{N}$. Suppose that for all bit lists $x$ and $w$, the component started at
$\mathit{start}$ with internal state false, with $g_X$ applied to each bit of $x$ on $c_X$, $g_W$
applied to each bit of $w$ on $c_W$ and every other stack empty, reaches in at most
$p(|x| + |w|)$ steps the label $\mathit{yes}$ if $f(x, w)$ is true and the label $\mathit{no}$ if
it is false. Then the map $(x, w) \mapsto f(x, w)$ on pairs of bit lists is polynomial-time
computable for the canonical bitstring encodings.

Formalized by `Cslib.Complexity.Host.isPolyTime_verifier`, a theorem declared in [CSLibExt/Computability/Complexity/Host.lean, line 565](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/Host.lean#L565). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html#is-poly-time-verifier).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Simulating component machines in a host machine](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/simulating-component-machines-in-a-host-machine)
