---
declaration: section
origin: cited
lean: Cslib.Algorithms.CCS.GoBackN.Name, Cslib.Algorithms.CCS.GoBackN.Sender, Cslib.Algorithms.CCS.GoBackN.Receiver, Cslib.Algorithms.CCS.GoBackN.ackUpdate, Cslib.Algorithms.CCS.GoBackN.senderSteps, Cslib.Algorithms.CCS.GoBackN.dataSteps, Cslib.Algorithms.CCS.GoBackN.receiverSteps, Cslib.Algorithms.CCS.GoBackN.bufferSteps
statement: formalized
proof: formalized
---

# Go-back-N protocol

35 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html).

## Channel names of go-back-N

The channel names of the go-back-N protocol are
$\mathsf{acc}$ (accept a message from the user), $\mathsf{del}$ (deliver a message to the user)
and, for every natural number $k$: $\mathsf{send}\,k$ (sender to data channel, a frame with
sequence number $k$), $\mathsf{recv}\,k$ (data channel to receiver), $\mathsf{ack}\,k$ (receiver
to sender, the cumulative acknowledgement naming $k$ as the next expected frame) and
$\mathsf{reply}\,k$ (receiver to the acknowledgement channel, in the lossy variant).

The protocol only uses the sequence numbers $0$, $1$ and $2$.

Formalized by `Cslib.Algorithms.CCS.GoBackN.Name`, an inductive type declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#name).

## Go-back-N sender state

A state of the go-back-N sender is a triple of natural numbers:
the base of the window (the sequence number of the oldest unacknowledged frame), the number of
outstanding messages (accepted but not yet acknowledged), and the offset from the base of the
next frame to transmit.

Formalized by `Cslib.Algorithms.CCS.GoBackN.Sender`, a structure declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#sender).

## Receiver states of go-back-N

A receiver state is one of the following, for a natural
number $e$ or $k$: expecting the frame with sequence number $e$; about to deliver $e$, having
received the expected frame $e$; or about to acknowledge $k$, the next expected sequence
number.

Formalized by `Cslib.Algorithms.CCS.GoBackN.Receiver`, an inductive type declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#receiver).

## Sender update on an acknowledgement

For a go-back-N sender with window base $b$, $c$
outstanding messages and next-frame offset $o$, and an acknowledgement $k$, let
$d = \max(k + 3 - b, 0) \bmod 3$. If $1 \le d \le c$, the window slides: the new sender has
base $k$, $c - d$ outstanding messages and next-frame offset $\max(o - d, 0)$. Otherwise the
sender is unchanged.

Formalized by `Cslib.Algorithms.CCS.GoBackN.ackUpdate`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#ack-update).

## Sender transitions of go-back-N

The transitions of a sender with window base $b$, $n$
outstanding messages and next offset $o$, as pairs of a label and a successor state, in this
order: if $n < 2$, an input on $\mathsf{acc}$ to $(b, n + 1, o)$; if $o < n$, an output on
$\mathsf{send}\,((b + o) \bmod 3)$ to $(b, n, o + 1)$; if $0 < n$, a silent timeout step to
$(b, n, 0)$; and, for each $k = 0, 1, 2$, an input on $\mathsf{ack}\,k$ to the state given by
the window update of the sender for acknowledgement $k$.

Formalized by `Cslib.Algorithms.CCS.GoBackN.senderSteps`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#sender-steps).

## Transitions of the go-back-N data channel

The data channel holds at most one frame.
When empty, for each sequence number $k \in \{0, 1, 2\}$ it can input on channel
$\mathrm{send}_k$ and then hold frame $k$. When holding frame $k$, it can either output on
channel $\mathrm{recv}_k$ or silently lose the frame by a $\tau$ step; in both cases it becomes
empty.

Formalized by `Cslib.Algorithms.CCS.GoBackN.dataSteps`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#data-steps).

## Receiver transitions of go-back-N

The transitions of the receiver, as pairs of a label
and a successor state. Expecting $e$, for each $k = 0, 1, 2$ it can input on $\mathsf{recv}\,k$
and then is about to deliver $e$ if $k = e$, and about to acknowledge $e$ otherwise. About to
deliver $e$, it outputs on $\mathsf{del}$ and is then about to acknowledge $(e + 1) \bmod 3$.
About to acknowledge $k$, it outputs on $\mathsf{ack}\,k$ and then expects $k$.

Formalized by `Cslib.Algorithms.CCS.GoBackN.receiverSteps`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#receiver-steps).

## Transitions of the two-place buffer

The transitions of the go-back-N two-place buffer
at occupancy $n \in \mathbb{N}$: if $n < 2$ it inputs on $\mathsf{acc}$ and moves to occupancy
$n + 1$, and if $n > 0$ it outputs on $\mathsf{del}$ and moves to occupancy $n - 1$. It has no
other transitions.

Formalized by `Cslib.Algorithms.CCS.GoBackN.bufferSteps`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#buffer-steps).

## Transitions of the lossy acknowledgement channel

The lossy one-place acknowledgement
channel of the lossy go-back-N variant, given by its transitions in each state. When empty, it
inputs on $\mathsf{reply}_k$ and then holds $k$, for each $k \in \{0, 1, 2\}$. When it holds
$k$, it either outputs on $\mathsf{ack}_k$ or silently loses $k$, and in both cases it becomes
empty. It has no other transitions.

Formalized by `Cslib.Algorithms.CCS.GoBackN.ackChannelSteps`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#ack-channel-steps).

## Receiver transitions of lossy go-back-N

The transitions of the receiver of the lossy
variant, as pairs of a label and a successor state, are those of the receiver of the reliable
protocol, except in the state about to acknowledge $k$: there the only transition is an output on
$\mathsf{reply}\,k$, to the acknowledgement channel, after which the receiver expects $k$.

Formalized by `Cslib.Algorithms.CCS.GoBackN.lossyReceiverSteps`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#lossy-receiver-steps).

## Process constants of the go-back-N model

The process constants of the go-back-N
specification, one for each state of each component: a sender constant for each sender state, a
data-channel constant for each channel content (empty or a natural number), a receiver constant
for each receiver state, a buffer constant for each occupancy $n \in \mathbb{N}$, an
acknowledgement-channel constant for each channel content (empty or a natural number), and a
constant for each receiver state of the lossy variant.

Formalized by `Cslib.Algorithms.CCS.GoBackN.Agent`, an inductive type declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#agent).

## Recursive CCS specification of go-back-N

The specification assigns to every process
constant the choice, over the transitions listed for its state, of the prefixes $a.K$, where $a$
is the label of the transition and $K$ is the process constant for its target state; an empty
list gives the inactive process. The constants are those of the sender, the data channel, the
receiver, the two-place buffer, the acknowledgement channel and the receiver of the lossy
variant, and their transitions are the sender steps, data channel steps, receiver steps, buffer
steps, acknowledgement channel steps and lossy receiver steps respectively.

Formalized by `Cslib.Algorithms.CCS.GoBackN.spec`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#spec).

## Labelled transition system of go-back-N

The labelled transition system whose states are
the CCS processes over the go-back-N channel names and process constants, whose labels are the
CCS labels over the channel names, and whose transitions are those generated by the go-back-N
recursive specification.

Formalized by `Cslib.Algorithms.CCS.GoBackN.lts`, an abbreviation declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#lts).

## Internal channels of go-back-N

The internal channels of the go-back-N protocol are
$\mathrm{send}_k$ (sender to data channel), $\mathrm{recv}_k$ (data channel to receiver) and
$\mathrm{ack}_k$ (receiver to sender) for $k \in \{0, 1, 2\}$; all of them are restricted.

Formalized by `Cslib.Algorithms.CCS.GoBackN.internal`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#internal).

## Go-back-N configurations

A configuration of the go-back-N protocol consists of a
sender state, the content of the data channel (either empty or a single frame with sequence
number $k \in \mathbb{N}$), and a receiver state.

Formalized by `Cslib.Algorithms.CCS.GoBackN.Config`, an abbreviation declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#config).

## Go-back-N protocol process in a configuration

For a configuration consisting of a sender
state $s$, a data channel content $d$ (empty or one frame) and a receiver state $r$, the protocol
process is the parallel composition $(S_s \mid D_d) \mid R_r$ of the process constants for the
sender in state $s$, the data channel holding $d$ and the receiver in state $r$, with the internal
channels restricted: the send, receive and acknowledgement channels for the sequence numbers $0$,
$1$ and $2$.

Formalized by `Cslib.Algorithms.CCS.GoBackN.system`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#system).

## Transitions of go-back-N configurations

The transitions of a go-back-N configuration
(sender, data channel, receiver) are those of the parallel composition of the three components,
in which one component moves alone or two components synchronize on complementary labels in a
silent step, restricted to the silent steps and the steps whose label is not on an internal
channel ($\mathsf{send}_k$, $\mathsf{recv}_k$ or $\mathsf{ack}_k$ for $k \in \{0, 1, 2\}$).

Formalized by `Cslib.Algorithms.CCS.GoBackN.configSteps`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#config-steps).

## The two-place buffer process

For an occupancy $n \in \mathbb{N}$, the process constant
of the go-back-N specification for the two-place buffer holding $n$ messages.

Formalized by `Cslib.Algorithms.CCS.GoBackN.buffer`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#buffer).

## Initial configuration of go-back-N

The initial configuration of the go-back-N
protocol consists of the sender with window base $0$, no outstanding messages and next-frame
offset $0$; the empty data channel; and the receiver expecting sequence number $0$.

Formalized by `Cslib.Algorithms.CCS.GoBackN.initial`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#initial).

## The go-back-N protocol

The go-back-N protocol with window size $2$ and sequence
numbers modulo $3$ is the recursive CCS process in its initial configuration: the parallel
composition of the sender with an empty window based at $0$, the empty lossy one-place data
channel, and the receiver expecting $0$, with the internal channels $\mathrm{send}_k$,
$\mathrm{recv}_k$ and $\mathrm{ack}_k$ for $k \in \{0, 1, 2\}$ restricted.

Formalized by `Cslib.Algorithms.CCS.GoBackN.goBackN`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#go-back-n).

## The empty two-place buffer

The two-place buffer process of the go-back-N model with
occupancy $0$.

Formalized by `Cslib.Algorithms.CCS.GoBackN.buf`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#buf).

## Weak-bisimulation certificate for go-back-N

A list of $147$ pairs, each a go-back-N
configuration together with the occupancy of the two-place buffer it simulates, namely the number
of accepted but undelivered messages. It contains every reachable configuration, and it is
ordered so that every pair can reach the visible actions of its buffer state through pairs listed
earlier.

Formalized by `Cslib.Algorithms.CCS.GoBackN.certificate`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#certificate).

## Go-back-N with window 2 implements a two-place buffer

Over a lossy
one-place data channel, with timeouts and cumulative acknowledgements, the
protocol is weakly bisimilar to the empty two-place buffer.

Formalized by `Cslib.Algorithms.CCS.GoBackN.goBackN_weaklyBisimilar_buffer`, a theorem declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#go-back-n-weakly-bisimilar-buffer).

## Go-back-N with window 2 is observation congruent to a two-place buffer

The
go-back-N protocol is observation congruent (rooted weakly bisimilar) to the empty two-place
buffer: every transition of either process is matched by a rooted weak transition of the
other with the same label (silent steps, a step with that label, silent steps), and the
resulting processes are weakly bisimilar.

Formalized by `Cslib.Algorithms.CCS.GoBackN.goBackN_observationCongruent_buffer`, a theorem declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#go-back-n-observation-congruent-buffer).

## Internal channels of lossy go-back-N

The list of channels restricted in the lossy
variant: the internal channels of the reliable protocol, namely $\mathsf{send}\,k$,
$\mathsf{recv}\,k$ and $\mathsf{ack}\,k$ for $k = 0, 1, 2$, followed by the channels
$\mathsf{reply}\,0$, $\mathsf{reply}\,1$ and $\mathsf{reply}\,2$ from the receiver to the
acknowledgement channel.

Formalized by `Cslib.Algorithms.CCS.GoBackN.lossyInternal`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#lossy-internal).

## Configurations of lossy go-back-N

A configuration of the lossy go-back-N variant is a
go-back-N configuration (sender state, data channel content, receiver state) together with the
content of the acknowledgement channel, either empty or a single acknowledgement
$k \in \mathbb{N}$.

Formalized by `Cslib.Algorithms.CCS.GoBackN.LossyConfig`, an abbreviation declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#lossy-config).

## The lossy go-back-N process in a configuration

Let $c$ be a configuration of the lossy
variant, and let $S$, $D$, $R$ and $A$ be the process constants for its sender state, its
data-channel content, its receiver state (as a receiver of the lossy variant) and its
acknowledgement-channel content. The process of the lossy variant in $c$ is
$((S \mid D) \mid R) \mid A$ with the internal channels of the lossy variant restricted.

Formalized by `Cslib.Algorithms.CCS.GoBackN.lossySystem`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#lossy-system).

## Transitions of lossy go-back-N configurations

The transitions of a configuration of
the lossy go-back-N variant come from the parallel composition of the sender, the data
channel, the lossy-variant receiver and the acknowledgement channel (in each composition
either side moves alone, or the two sides synchronize on complementary input and output
labels in a silent step), keeping only the silent transitions and those whose label is not
on an internal channel $\mathrm{send}_k$, $\mathrm{recv}_k$, $\mathrm{ack}_k$ or
$\mathrm{reply}_k$, $k \in \{0, 1, 2\}$.

Formalized by `Cslib.Algorithms.CCS.GoBackN.lossyConfigSteps`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#lossy-config-steps).

## Go-back-N with a lossy acknowledgement channel

The process of the lossy variant of
go-back-N in its initial configuration: the sender's window is based at $0$ with no outstanding
messages and next offset $0$, the data channel and the acknowledgement channel are empty, and
the receiver expects frame $0$.

Formalized by `Cslib.Algorithms.CCS.GoBackN.lossyGoBackN`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#lossy-go-back-n).

## Configuration transitions are process transitions in lossy go-back-N

Let $c$ and $c'$
be configurations of the lossy variant and $a$ a label. If $(a, c')$ is one of the
configuration-level transitions of $c$, then in the labelled transition system of the go-back-N
specification the lossy process in configuration $c$ has a transition labelled $a$ to the lossy
process in configuration $c'$.

Formalized by `Cslib.Algorithms.CCS.GoBackN.lossy_step`, a theorem declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#lossy-step).

## The silent closure of the buffer is trivial

For every occupancy $n$, every process
reachable from the go-back-N buffer with occupancy $n$ by zero or more silent steps is that
buffer itself.

Formalized by `Cslib.Algorithms.CCS.GoBackN.buffer_silentClosure`, a theorem declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#buffer-silent-closure).

## Visible weak steps of the buffer

For every occupancy $n$ and every visible label $a$, if
the go-back-N buffer with occupancy $n$ reaches a process $Q$ by a weak transition labelled $a$
(silent steps, one $a$-step, silent steps), then $Q$ is the buffer with some occupancy $m$ such
that the buffer at occupancy $n$ has a transition labelled $a$ to occupancy $m$.

Formalized by `Cslib.Algorithms.CCS.GoBackN.buffer_weakStep`, a theorem declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#buffer-weak-step).

## Silent closure of the stuck lossy go-back-N configuration

The list of the seven
configurations of go-back-N with a lossy acknowledgement channel in which the sender's window has
base $0$ with two outstanding messages, the receiver holds frame $1$ about to deliver it, and the
acknowledgement channel is empty, while the sender's offset of the next frame to transmit and the
data channel are, in order: offset $2$ and empty, offset $0$ and empty, offset $1$ holding frame
$0$, offset $0$ holding frame $0$, offset $1$ and empty, offset $2$ holding frame $1$, and offset
$0$ holding frame $1$.

The first is the stuck configuration, reached after the acknowledgement of frame $0$ was lost; the
list is closed under silent steps (proved separately), so it contains every configuration
silently reachable from it.

Formalized by `Cslib.Algorithms.CCS.GoBackN.stuckClosure`, a definition declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#stuck-closure).

## The stuck lossy go-back-N configuration refuses new messages

Consider go-back-N with a
lossy acknowledgement channel in the configuration where the sender's window has base $0$ with two
outstanding messages, both transmitted (offset of the next frame $2$), the data channel and the
acknowledgement channel are empty, and the receiver holds frame $1$ about to deliver it. This
process has no weak transition labelled by accepting a message: no sequence of silent steps
followed by an accept input and further silent steps is possible from it.

Formalized by `Cslib.Algorithms.CCS.GoBackN.stuck_not_hasOutLabel_acc`, a theorem declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#stuck-not-has-out-label-acc).

## Lossy acknowledgements break the buffer specification

With a lossy
acknowledgement channel and the deliver-then-acknowledge receiver, go-back-N is
not weakly bisimilar to the two-place buffer. Accept two messages, deliver the
first and lose its acknowledgement, and let the receiver take the second frame:
the buffer now holds one message and accepts another, but the protocol cannot
accept before it delivers.

Formalized by `Cslib.Algorithms.CCS.GoBackN.lossyGoBackN_not_weaklyBisimilar_buffer`, a theorem declared in [CSLibExt/Algorithms/CCS/GoBackN.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/GoBackN.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html#lossy-go-back-n-not-weakly-bisimilar-buf).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Go-back-N protocol](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/concurrent-systems-and-protocols/go-back-n-protocol)
