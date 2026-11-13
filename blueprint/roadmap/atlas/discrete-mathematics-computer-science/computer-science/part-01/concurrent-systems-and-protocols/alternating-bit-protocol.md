---
declaration: section
origin: cited
lean: Cslib.Algorithms.CCS.AlternatingBit.Name, Cslib.Algorithms.CCS.AlternatingBit.Sender, Cslib.Algorithms.CCS.AlternatingBit.Channel, Cslib.Algorithms.CCS.AlternatingBit.Receiver, Cslib.Algorithms.CCS.AlternatingBit.senderSteps, Cslib.Algorithms.CCS.AlternatingBit.dataSteps, Cslib.Algorithms.CCS.AlternatingBit.receiverSteps, Cslib.Algorithms.CCS.AlternatingBit.ackSteps
statement: formalized
proof: formalized
---

# Alternating bit protocol

45 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html).

## Alternating-bit channel names

The channel names of the alternating-bit protocol are
$\mathit{acc}$ (accept a message from the user), $\mathit{del}$ (deliver a message to the
user), and, for each bit $b$, the internal names $\mathit{send}_b$ (sender to data channel),
$\mathit{recv}_b$ (data channel to receiver), $\mathit{reply}_b$ (receiver to acknowledgement
channel) and $\mathit{ack}_b$ (acknowledgement channel to sender).

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.Name`, an inductive type declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#name).

## Sender states of the data-free alternating-bit protocol

For each bit $b$, the sender
has three states: $\mathrm{accept}(b)$, ready to accept a message to be sent with bit $b$;
$\mathrm{transmit}(b)$, about to transmit a frame tagged with bit $b$; and $\mathrm{await}(b)$,
waiting for the acknowledgement of bit $b$. These six states are all the sender states.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.Sender`, an inductive type declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#sender).

## States of a one-place channel

A one-place channel is either empty or full, holding a single
bit.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.Channel`, an inductive type declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#channel).

## Alternating-bit receiver states

A state of the alternating-bit receiver is, for a bit
$b$, either expecting a frame with bit $b$, about to deliver the message of a frame with bit
$b$, or about to acknowledge bit $b$.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.Receiver`, an inductive type declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#receiver).

## Alternating-bit sender transitions

The sender of the alternating-bit protocol has the
following transitions. Ready to accept with bit $b$, it can input on $\mathit{acc}$ and become
about to transmit $b$. About to transmit $b$, it can output on $\mathit{send}_b$ and then await
the acknowledgement of $b$. Awaiting the acknowledgement of $b$, it can input on
$\mathit{ack}_b$ and become ready to accept with bit $\lnot b$, input on
$\mathit{ack}_{\lnot b}$ and keep waiting, or time out by a silent step and become about to
transmit $b$ again.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.senderSteps`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#sender-steps).

## Alternating-bit data channel transitions

The one-place data channel of the
alternating-bit protocol has the following transitions. When empty, it can input on
$\mathit{send}_b$ and become full with bit $b$, for each bit $b$. When full with bit $b$, it can
output on $\mathit{recv}_b$ and become empty, or lose the bit by a silent step and become empty.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.dataSteps`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#data-steps).

## Alternating-bit receiver transitions

The receiver of the alternating-bit protocol has
the following transitions. Expecting bit $b$, it can input on $\mathit{recv}_b$ and become ready
to deliver $b$, or input on $\mathit{recv}_{\lnot b}$ and become ready to acknowledge $\lnot b$.
Ready to deliver $b$, it can output on $\mathit{del}$ and become ready to acknowledge $b$. Ready
to acknowledge $b$, it can output on $\mathit{reply}_b$ and then expect $\lnot b$.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.receiverSteps`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#receiver-steps).

## Transitions of the acknowledgement channel in the data-free alternating-bit protocol

When
empty, the lossy one-place acknowledgement channel can, for either bit $b$, input on
$\mathit{reply}_b$ and become full with bit $b$. When full with bit $b$, it can output on
$\mathit{ack}_b$ or make a silent $\tau$ step (losing the bit), in both cases becoming empty. These
are all its transitions.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.ackSteps`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#ack-steps).

## Transitions of the data-free one-place buffer

The one-place buffer has two states, empty
(false) and full (true). When empty, its only transition is an input on $\mathit{acc}$ to the full
state; when full, its only transition is an output on $\mathit{del}$ to the empty state.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.bufferSteps`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#buffer-steps).

## Process constants of the data-free alternating-bit protocol

There is one process constant
for each sender state, each state of the data channel, each receiver state, each state of the
acknowledgement channel, and each state of the one-place buffer (empty or full).

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.Agent`, an inductive type declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#agent).

## Recursive specification of the data-free alternating-bit protocol

The process constants
are the states of the five agents: the sender, the data channel, the receiver, the
acknowledgement channel and the one-place buffer. For a state $x$ of one of these agents, let
$(a_1, x_1), \dots, (a_n, x_n)$ be the transitions of $x$ as listed by the transition function
of its agent, let $X_i$ be the constant of the same agent at state $x_i$, and let $\mathbf{0}$
be the inactive process. The specification defines the constant of $x$ as the choice of
prefixes $a_1.X_1 + (a_2.X_2 + \cdots + (a_n.X_n + \mathbf{0}))$.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.spec`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#spec).

## Alternating-bit transition system

The labelled transition system whose states are the
CCS processes over the alternating-bit channel names and process constants, whose labels are the
CCS labels over those names, and whose transitions are the steps of the CCS operational
semantics for the recursive specification that defines each process constant (one per state of
the sender, the data channel, the receiver, the acknowledgement channel and the one-place
buffer) as the choice of its listed transitions.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.lts`, an abbreviation declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#lts).

## Internal channels of the alternating-bit protocol

The internal channel names, all of
which the protocol restricts, are $\mathit{send}_b$, $\mathit{recv}_b$, $\mathit{reply}_b$ and
$\mathit{ack}_b$ for both bits $b$, that is, every channel name except $\mathit{acc}$ and
$\mathit{del}$.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.internal`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#internal).

## Alternating-bit configuration

A configuration of the alternating-bit protocol consists
of a sender state, a state of the data channel, a receiver state and a state of the
acknowledgement channel.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.Config`, an abbreviation declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#config).

## The alternating-bit protocol in a configuration

Consider a configuration with sender
state $s$, data channel state $d$, receiver state $r$ and acknowledgement channel state $k$.
Write $\mathrm{Sender}(s)$, $\mathrm{Data}(d)$, $\mathrm{Receiver}(r)$ and $\mathrm{Ack}(k)$
for the constants of the four agents at these states, and let $L$ be the set of internal
channels $\mathrm{send}(b)$, $\mathrm{recv}(b)$, $\mathrm{reply}(b)$ and $\mathrm{ack}(b)$ for
both bits $b$. The protocol process is the parallel composition of these constants with every
internal channel restricted,
$(((\mathrm{Sender}(s) \mid \mathrm{Data}(d)) \mid \mathrm{Receiver}(r)) \mid \mathrm{Ack}(k))
\setminus L$.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.system`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#system).

## Alternating-bit configuration transitions

The transitions of a configuration of the
alternating-bit protocol, listed as pairs of a label and a successor configuration, are obtained
by composing the transitions of the sender, the data channel, the receiver and the
acknowledgement channel in parallel, in that order (at each stage either side moves alone, or
the two sides synchronize on an input and the complementary output on the same channel name,
giving a silent step), and then keeping only the silent steps and the steps whose channel name
is not one of the internal channel names.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.configSteps`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#config-steps).

## The data-free one-place buffer in a given state

For a Boolean $f$, $\mathit{buffer}(f)$ is
the process constant for the one-place buffer that is full if $f$ is true and empty if $f$ is
false.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.buffer`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#buffer).

## Initial alternating-bit configuration

The initial configuration of the alternating-bit
protocol has the sender ready to accept a message with bit $\mathrm{false}$, both channels
empty, and the receiver expecting bit $\mathrm{false}$.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.initial`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#initial).

## The data-free alternating-bit protocol

The process $\mathit{abp}$ is the protocol in its
initial configuration: the parallel composition of the sender, the lossy one-place data channel,
the receiver and the lossy one-place acknowledgement channel, with all eight internal channels
$\mathit{send}_b$, $\mathit{recv}_b$, $\mathit{reply}_b$ and $\mathit{ack}_b$ (for both bits $b$)
restricted, where the sender is ready to accept a message to be sent with bit $0$, both channels
are empty, and the receiver expects bit $0$.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.abp`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#abp).

## The data-free one-place buffer

The process $\mathit{buf}$ is the one-place buffer in its
empty state. By the specification it accepts on $\mathit{acc}$ and becomes full, and the full
buffer delivers on $\mathit{del}$ and becomes empty again, so
$\mathit{buf} = \mathit{acc}.\overline{\mathit{del}}.\mathit{buf}$.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.buf`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#buf).

## Weak-bisimulation certificate for the data-free alternating-bit protocol

The list of every
reachable protocol configuration, paired with the buffer state it simulates (full from the accept
of a message until its delivery), sorted by silent distance to the next visible action.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.certificate`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#certificate).

## The alternating-bit protocol implements a one-place buffer

In the labelled transition
system of the protocol's recursive CCS specification, the data-free alternating-bit protocol over
lossy one-place channels is weakly bisimilar to the one-place buffer
$\mathit{buf} = \mathit{acc}.\overline{\mathit{del}}.\mathit{buf}$.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.abp_weaklyBisimilar_buffer`, a theorem declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#abp-weakly-bisimilar-buffer).

## The alternating-bit protocol is observation congruent to a one-place buffer

In the
labelled transition system of the protocol's recursive CCS specification, the data-free
alternating-bit protocol over lossy one-place channels is rooted weakly bisimilar (observation
congruent) to the one-place buffer
$\mathit{buf} = \mathit{acc}.\overline{\mathit{del}}.\mathit{buf}$.

This is stronger than weak bisimilarity; it holds because initially neither process can move
silently.

Formalized by `Cslib.Algorithms.CCS.AlternatingBit.abp_observationCongruent_buffer`, a theorem declared in [CSLibExt/Algorithms/CCS/AlternatingBit.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBit.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#abp-observation-congruent-buffer).

## Channel names of the alternating-bit protocol with data

For bits $b$ and $d$, where $b$ is
a sequence bit and $d$ a data bit, the channel names are $\mathsf{acc}(d)$ (accept the data bit
$d$ from the user), $\mathsf{del}(d)$ (deliver the data bit $d$ to the user), $\mathsf{send}(b, d)$
(sender to data channel), $\mathsf{recv}(b, d)$ (data channel to receiver), $\mathsf{reply}(b)$
(receiver to acknowledgement channel) and $\mathsf{ack}(b)$ (acknowledgement channel to sender).

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.Name`, an inductive type declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#name-2).

## Sender states of the alternating-bit protocol with data

For bits $b$ and $d$, a sender
state is $\mathsf{accept}(b)$, ready to accept a message to be sent with sequence bit $b$;
$\mathsf{transmit}(b, d)$, about to transmit the data bit $d$ with sequence bit $b$; or
$\mathsf{await}(b, d)$, waiting for the acknowledgement of $b$ while holding $d$ for
retransmission.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.Sender`, an inductive type declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#sender-2).

## Receiver states of the alternating-bit protocol with data

For bits $b$ and $d$, a receiver
state is $\mathsf{expect}(b)$, expecting a frame with sequence bit $b$; $\mathsf{deliver}(b, d)$,
about to deliver the data bit $d$ of a frame with sequence bit $b$; or $\mathsf{reply}(b)$, about
to acknowledge $b$.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.Receiver`, an inductive type declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#receiver-2).

## Sender transitions of the alternating-bit protocol with data

The transitions of each
sender state, as a list of pairs of a label and a successor state, for bits $b$ and $d$:
$\mathsf{accept}(b)$ inputs on $\mathsf{acc}(d)$ and moves to $\mathsf{transmit}(b, d)$, for
$d = \mathrm{false}$ and then $d = \mathrm{true}$; $\mathsf{transmit}(b, d)$ outputs on
$\mathsf{send}(b, d)$ and moves to $\mathsf{await}(b, d)$; and $\mathsf{await}(b, d)$ inputs on
$\mathsf{ack}(b)$ and moves to $\mathsf{accept}(\lnot b)$, inputs on $\mathsf{ack}(\lnot b)$ and
stays in $\mathsf{await}(b, d)$, or times out by a silent step $\tau$ back to
$\mathsf{transmit}(b, d)$, in this order.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.senderSteps`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#sender-steps-2).

## Data-channel transitions of the alternating-bit protocol with data

The data channel is a
lossy one-place channel whose content is either empty or a pair $(b, d)$ of a sequence bit $b$
and a data bit $d$. Its transitions, as a list of pairs of a label and a successor content: the
empty channel inputs on $\mathsf{send}(b, d)$ and then holds $(b, d)$, for the four pairs $(b, d)$
in the order $(\mathrm{false}, \mathrm{false})$, $(\mathrm{false}, \mathrm{true})$,
$(\mathrm{true}, \mathrm{false})$, $(\mathrm{true}, \mathrm{true})$; a channel holding $(b, d)$
either outputs on $\mathsf{recv}(b, d)$ and becomes empty, or loses the frame by a silent step
$\tau$ and becomes empty.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.dataSteps`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#data-steps-2).

## Receiver transitions of the alternating-bit protocol with data

The transitions of each
receiver state, as a list of pairs of a label and a successor state, for bits $b$ and $d$:
$\mathsf{expect}(b)$ inputs on $\mathsf{recv}(b, d)$ and moves to $\mathsf{deliver}(b, d)$, or
inputs a duplicate on $\mathsf{recv}(\lnot b, d)$ and moves to the state $\mathsf{reply}(\lnot b)$,
these two for $d = \mathrm{false}$ and then for $d = \mathrm{true}$; $\mathsf{deliver}(b, d)$
outputs on $\mathsf{del}(d)$ and moves to the state $\mathsf{reply}(b)$; and the state
$\mathsf{reply}(b)$ outputs on the channel $\mathsf{reply}(b)$ and moves to
$\mathsf{expect}(\lnot b)$. So the receiver delivers the data of an expected frame and
acknowledges a duplicate again.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.receiverSteps`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#receiver-steps-2).

## Acknowledgement channel of the alternating-bit protocol with data

The transitions of the
lossy one-place acknowledgement channel: when empty, it can take an input on $\mathrm{reply}_b$
for either bit $b$ and then holds $b$; when holding $b$, it can either output on $\mathrm{ack}_b$
or lose $b$ by a silent step, and in both cases it becomes empty.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.ackSteps`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#ack-steps-2).

## Transitions of the one-place buffer of bits

When empty, the buffer can take an input on
$\mathrm{acc}_d$ for either bit $d$ and then holds $d$; when holding $d$, its only transition is
an output on $\mathrm{del}_d$, after which it is empty.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.bufferSteps`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#buffer-steps-2).

## Process constants of the alternating-bit protocol with data

There is one process constant
for each sender state, each content of the data channel (empty, or a sequence bit with a data
bit), each receiver state, each content of the acknowledgement channel (empty, or a bit), and each
content of the one-place buffer of bits (empty, or a bit).

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.Agent`, an inductive type declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#agent-2).

## Recursive specification of the alternating-bit protocol with data

There is a separate
process constant $X_s$ for each state $s$ of each of five components: the sender, the lossy data
channel, the receiver, the lossy acknowledgement channel and the one-place buffer of bits. If
$(a_1, s_1), \dots, (a_n, s_n)$ are the listed transitions of $s$ in its component, then the body
of $X_s$ is the choice of prefixes $a_1.X_{s_1} + (a_2.X_{s_2} + \dots + (a_n.X_{s_n} + 0))$,
where each $X_{s_i}$ is the constant of the same component and $0$ is the inactive process; the
body is $0$ when $s$ has no listed transitions.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.spec`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#spec-2).

## Transition system of the alternating-bit protocol with data

The labelled transition
system whose states are the CCS processes over the protocol's channel names and process
constants, whose labels are the CCS labels over its channel names, and whose transitions are
generated by the protocol's recursive specification.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.lts`, an abbreviation declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#lts-2).

## Internal channels of the alternating-bit protocol with data

The list of the channel names
that the protocol restricts: $\mathsf{send}(b, d)$ followed by $\mathsf{recv}(b, d)$ for the pairs
$(b, d)$ in the order $(\mathrm{false}, \mathrm{false})$, $(\mathrm{false}, \mathrm{true})$,
$(\mathrm{true}, \mathrm{false})$, $(\mathrm{true}, \mathrm{true})$, then
$\mathsf{reply}(\mathrm{false})$, $\mathsf{reply}(\mathrm{true})$, $\mathsf{ack}(\mathrm{false})$
and $\mathsf{ack}(\mathrm{true})$.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.internal`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#internal-2).

## Configurations of the alternating-bit protocol with data

A configuration consists of a
sender state, the content of the data channel (empty, or a pair of a sequence bit and a data
bit), a receiver state, and the content of the acknowledgement channel (empty, or a bit).

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.Config`, an abbreviation declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#config-2).

## The alternating-bit protocol with data in a configuration

For a configuration $c$ made of
a sender state $s$, a data-channel content $d$, a receiver state $r$ and an
acknowledgement-channel content $k$, the protocol process at $c$ is
$((X_s \mid X_d) \mid X_r) \mid X_k$ with every internal channel restricted, where $X_s$, $X_d$,
$X_r$ and $X_k$ are the process constants of these states. The internal channels are all channel
names other than accepting and delivering a data bit.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.system`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#system-2).

## Transitions of the alternating-bit protocol with data

For a configuration, made of a
sender state, a data-channel content, a receiver state and an acknowledgement-channel content,
the transitions are those of the parallel composition of the sender, the data channel, the
receiver and the acknowledgement channel, where one component moves alone or two components
synchronize on complementary labels in a silent step. Of these, only the silent steps and the
actions on names that are not internal channels are kept; the internal channels are the sending,
receiving, reply and acknowledgement channels.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.configSteps`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#config-steps-2).

## The one-place buffer of bits with given content

For a content $q$, which is either empty
or a bit, the process constant of the one-place buffer of bits holding $q$.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.buffer`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#buffer-2).

## Initial configuration of the alternating-bit protocol with data

The configuration in
which the sender is in state $\mathsf{accept}(\mathrm{false})$, ready to accept a message to be
sent with sequence bit false, the data channel and the acknowledgement channel are empty, and
the receiver is in state $\mathsf{expect}(\mathrm{false})$, expecting a frame with sequence bit
false.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.initial`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#initial-2).

## The alternating-bit protocol with data

The protocol process in its initial
configuration: the sender is ready to accept a data bit, to be sent with sequence bit false, the
data channel and the acknowledgement channel are empty, and the receiver expects a frame with
sequence bit false. The four agents run in parallel, with all internal channels restricted.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.abpData`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#abp-data).

## The empty one-place buffer of bits

The process constant of the one-place buffer of bits
with empty content.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.buf`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#buf-2).

## Weak-bisimulation certificate for the alternating-bit protocol with data

A list of 220
pairs, each a protocol configuration together with the buffer content it simulates: every
reachable configuration with the buffer content it simulates, listed so that every pair reaches
the visible actions of its buffer state through pairs listed earlier.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.certificate`, a definition declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#certificate-2).

## The alternating-bit protocol transmits data correctly

It is weakly
bisimilar to the empty one-place buffer of bits.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.abpData_weaklyBisimilar_buffer`, a theorem declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#abp-data-weakly-bisimilar-buffer).

## The alternating-bit protocol with data is observation congruent to the buffer

In the
labelled transition system of the protocol's recursive specification, the alternating-bit protocol
with data is observation congruent (rooted weakly bisimilar) to the empty one-place buffer of
bits: every transition of either process with some label is matched by the other process through
silent steps, then one actual step with the same label, then silent steps, and the two resulting
processes are weakly bisimilar.

Formalized by `Cslib.Algorithms.CCS.AlternatingBitData.abpData_observationCongruent_buffer`, a theorem declared in [CSLibExt/Algorithms/CCS/AlternatingBitData.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/AlternatingBitData.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html#abp-data-observation-congruent-buffer).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Alternating bit protocol](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/concurrent-systems-and-protocols/alternating-bit-protocol)
