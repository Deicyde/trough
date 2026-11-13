---
declaration: section
origin: cited
lean: Cslib.Turing.MultiTapeTM.stepWith, Cslib.Turing.MultiTapeTM.step_ofTr, Cslib.Turing.MultiTapeTM.runFrom_ofTr, Cslib.Turing.MultiTapeTM.step_deterministic, Cslib.Turing.MultiTapeTM.runFrom_succ', Cslib.Turing.MultiTapeTM.runFrom_of_halted, Cslib.Turing.MultiTapeTM.halted_runFrom_mono, Cslib.Turing.MultiTapeTM.haltsAt_zero_iff
statement: formalized
proof: formalized
---

# Multi-tape Turing machines

32 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html).

## Successor under a transition function

Let $\delta$ be a transition function of a
multi-tape Turing machine with $k$ work tapes, assigning an action to each state, input symbol
and tuple of $k$ work tape symbols, where a symbol may be blank. The successor of a configuration
$c$ under $\delta$ is $c$ itself if $c$ is halted, and otherwise the configuration obtained by
applying to $c$ the action $\delta(q, a, b)$, where $q$ is the state of $c$, $a$ the symbol under
its input head and $b$ the symbols under its work tape heads.

Formalized by `Cslib.Turing.MultiTapeTM.stepWith`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#step-with).

## Step of a machine given by a transition function

Let $M$ be the deterministic multi-tape
Turing machine with initial state $q_0$ and transition function $\delta$. For every configuration
$c$, the step of $M$ from $c$ is the successor of $c$ under $\delta$: $c$ itself if $c$ is halted,
and otherwise the result of applying to $c$ the action that $\delta$ selects for the state of $c$
and the symbols under its input and work tape heads.

Formalized by `Cslib.Turing.MultiTapeTM.step_ofTr`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#step-of-tr).

## Runs of a machine given by a transition function

Let $\delta$ be a transition function
that assigns an action to every state, symbol or blank read on the input tape, and tuple of
symbols or blanks read on the work tapes, and let $M$ be the deterministic multi-tape Turing
machine with initial state $q_0$ and transition function $\delta$. Let $S_\delta$ be the map on
configurations that fixes every halted configuration and sends a running configuration in state
$q$ to the result of applying to it the action that $\delta$ selects for $q$ and the symbols or
blanks under its heads. For every configuration $c$ and every $t \in \mathbb{N}$, the run of $M$
from $c$ is in configuration $S_\delta^t(c)$ after $t$ steps, where $S_\delta^t$ is the $t$-fold
iterate of $S_\delta$.

Formalized by `Cslib.Turing.MultiTapeTM.runFrom_ofTr`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#run-from-of-tr).

## Step determinism

Let $M$ be a deterministic multi-tape Turing machine, with the one-step
relation it inherits as a nondeterministic machine. If a configuration $c$ steps to both $c_1$
and $c_2$, then $c_1 = c_2$.

Formalized by `Cslib.Turing.MultiTapeTM.step_deterministic`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#step-deterministic).

## Peeling off the first step of a run

For a configuration $c$ of a deterministic
multi-tape Turing machine and every $t \in \mathbb{N}$, the run from $c$ after $t + 1$ steps is in
the same configuration as the run from the successor of $c$ after $t$ steps.

Formalized by `Cslib.Turing.MultiTapeTM.runFrom_succ'`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#run-from-succ).

## Halted configurations are fixed

If a configuration $c$ of a deterministic multi-tape
Turing machine is halted, then for every $t \in \mathbb{N}$ the run from $c$ is in configuration
$c$ after $t$ steps.

Formalized by `Cslib.Turing.MultiTapeTM.runFrom_of_halted`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#run-from-of-halted).

## Halting persists along a run

For a configuration $c$ of a deterministic multi-tape Turing
machine and steps $s \le t$, if the run from $c$ is halted after $s$ steps, then it is halted after
$t$ steps.

Formalized by `Cslib.Turing.MultiTapeTM.halted_runFrom_mono`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#halted-run-from-mono).

## Halting at step zero

A deterministic multi-tape Turing machine started in a
configuration $c$ halts at step $0$ if and only if $c$ is halted.

Formalized by `Cslib.Turing.MultiTapeTM.haltsAt_zero_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#halts-at-zero-iff).

## Run composition for halting

Let $c$ be a configuration of a deterministic multi-tape
Turing machine and let $m, n \in \mathbb{N}$. If the run from $c$ is not halted after any $s < m$
steps, and the run from the configuration reached after $m$ steps halts at step $n$ (it is halted
after $n$ steps and not halted after fewer), then the run from $c$ halts at step $m + n$.

Formalized by `Cslib.Turing.MultiTapeTM.haltsAt_add`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#halts-at-add).

## Halting step after a run prefix

Let $M$ be a deterministic multi-tape Turing machine,
$c$ a configuration of $M$ and $m, n$ natural numbers. If $M$ started in $c$ halts at step
$m + n$, that is, it is halted after $m + n$ steps and not halted after any fewer, then $M$
started in the configuration reached from $c$ after $m$ steps halts at step $n$.

Formalized by `Cslib.Turing.MultiTapeTM.HaltsAt.runFrom`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#run-from).

## A time bound forces halting

If a deterministic multi-tape Turing machine runs in time $t$
on input $w$, then the run from the initial configuration on $w$ is halted after $t$ steps.

Formalized by `Cslib.Turing.MultiTapeTM.halted_runFrom_of_runsInTime`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#halted-run-from-of-runs-in-time).

## Time bounds of deterministic machines

Let $M$ be a deterministic multi-tape Turing
machine, $w$ an input and $t$ a natural number. Then $M$ runs in time $t$ on $w$, that is, every
computation path of $M$ on $w$ with at least $t$ steps ends in a halted configuration, if and only
if $M$ started in its initial configuration on $w$ is halted after $t$ steps.

Formalized by `Cslib.Turing.MultiTapeTM.runsInTime_iff_halted`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#runs-in-time-iff-halted).

## Output determinism

A deterministic machine computes at most one output on an input.

Formalized by `Cslib.Turing.MultiTapeTM.computes_unique`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#computes-unique).

## Computing an output means halting with it

A deterministic multi-tape Turing machine
computes the output $o$ on input $w$ if and only if there is a step $t$ at which the run from the
initial configuration on $w$ halts (it is halted after $t$ steps and not halted after any $s < t$
steps) and the configuration it reaches after $t$ steps has output tape $o$.

Formalized by `Cslib.Turing.MultiTapeTM.computes_iff_exists_haltsAt`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#computes-iff-exists-halts-at).

## Output at a time bound

If a deterministic multi-tape Turing machine runs in time $t$ on
input $w$, then for every word $o$ the machine computes $o$ on $w$ if and only if the
configuration reached from the initial configuration on $w$ after $t$ steps has output tape $o$.

Formalized by `Cslib.Turing.MultiTapeTM.computes_iff_output_of_runsInTime`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Basic.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#computes-iff-output-of-runs-in-time).

## Space of the deterministic computation path

Let $M$ be a deterministic multi-tape
Turing machine, $x$ an input and $t \in \mathbb{N}$. The number of work-tape cells visited along
the computation path of $M$ on $x$ made of the first $t$ steps from the initial configuration
equals the space used by the run of $M$ from the initial configuration on $x$ up to step $t$.
Both count the visited cells on each work tape separately and sum over the work tapes.

Formalized by `Cslib.Turing.MultiTapeTM.space_ofDeterministic`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#space-of-deterministic).

## Space bounds of deterministic machines

Let $M$ be a deterministic multi-tape Turing
machine, $x$ an input and $s \in \mathbb{N}$. Then $M$ runs in space $s$ on $x$, that is, every
computation path of $M$ on $x$ visits at most $s$ work-tape cells, if and only if for every
$t \in \mathbb{N}$ the run of $M$ from the initial configuration on $x$ visits at most $s$
work-tape cells within its first $t$ steps. Visited cells are counted on each work tape
separately and summed over the work tapes.

Formalized by `Cslib.Turing.MultiTapeTM.runsInSpace_iff_forall_spaceUsed_le`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#runs-in-space-iff-forall-space-used-le).

## Relabelling the successor state of an action

For a map $f : Q \to Q'$ of states and an
action $a$ of a machine with $k$ work tapes and states $Q$, the relabelled action is the action
with states $Q'$ that moves the input head, writes and moves on the work tapes and outputs exactly
as $a$ does, and whose successor state is $f(q)$ when $a$ goes to state $q$ and is halting when $a$
halts.

Formalized by `Cslib.Turing.MultiTapeTM.relabelAction`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#relabel-action).

## Applying a relabelled action

Let $f : Q \to Q'$ be a map of states; relabelling by $f$
replaces a state $q$ by $f(q)$ and keeps the halting state. For every action $a$ of a machine with
$k$ work tapes and states $Q$ and every configuration $c$ of such a machine, applying $a$ with its
successor state relabelled by $f$ to $c$ with its state relabelled by $f$ gives the configuration
obtained by applying $a$ to $c$ and then relabelling its state by $f$.

Formalized by `Cslib.Turing.MultiTapeTM.apply_relabelAction`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#apply-relabel-action).

## Simulation up to a state relabelling

Let $M$ and $M'$ be deterministic machines with $k$
work tapes over the same alphabet, with state sets $Q$ and $Q'$, and let $f : Q \to Q'$. Then $M'$
simulates $M$ up to the relabelling $f$ when the initial state of $M'$ is $f(q_0)$, where $q_0$ is
the initial state of $M$, and for every state $q \in Q$, every possibly blank symbol $a$ under the
input head and every tuple $w$ of possibly blank symbols under the work heads, the action of $M'$
in state $f(q)$ reading $a$ and $w$ is the action of $M$ in state $q$ reading $a$ and $w$ with its
successor state relabelled by $f$ (a successor state $q'$ becomes $f(q')$, and halting stays
halting).

Nothing is required of $M'$ in states outside the range of $f$, and $f$ need not be injective.

Formalized by `Cslib.Turing.MultiTapeTM.IsRelabelling`, a structure declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#is-relabelling).

## Relabelling preserves halting

Let $f$ be a map of states. For every configuration $c$,
the configuration obtained from $c$ by replacing its state $q$ by $f(q)$, and keeping the halting
state, is halted if and only if $c$ is halted.

Formalized by `Cslib.Turing.MultiTapeTM.halted_mapState_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#halted-map-state-iff).

## Every machine is a relabelling of itself

Every deterministic machine with $k$ work tapes
simulates itself up to the identity relabelling of its states.

Formalized by `Cslib.Turing.MultiTapeTM.IsRelabelling.refl`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#refl).

## Relabellings compose

Let $M$, $M'$ and $M''$ be multi-tape Turing machines with the same
number of work tapes and the same alphabet, with state sets $Q$, $Q'$ and $Q''$. If $M'$
simulates $M$ up to the state relabelling $f : Q \to Q'$ and $M''$ simulates $M'$ up to the
state relabelling $g : Q' \to Q''$, then $M''$ simulates $M$ up to the state relabelling
$g \circ f$.

Formalized by `Cslib.Turing.MultiTapeTM.IsRelabelling.trans`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#trans).

## Relabelled machines step in lockstep

Let $M$ and $M'$ be multi-tape Turing machines
with the same number of work tapes and the same alphabet, with state sets $Q$ and $Q'$, such that
$M'$ simulates $M$ up to the state relabelling $f : Q \to Q'$. For a configuration $c$ of $M$,
write $f_*(c)$ for the configuration of $M'$ obtained by replacing the state $q$ of $c$ by
$f(q)$ and keeping the input head, the work tapes, the work heads and the output (a halted
configuration stays halted). Then for every configuration $c$ of $M$, one step of $M'$ from
$f_*(c)$ gives $f_*(c')$, where $c'$ is the result of one step of $M$ from $c$.

Formalized by `Cslib.Turing.MultiTapeTM.IsRelabelling.step`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#step).

## Lockstep runs

Let $M$ and $M'$ be multi-tape Turing machines with the same number of
work tapes and the same alphabet, with state sets $Q$ and $Q'$, such that $M'$ simulates $M$ up
to the state relabelling $f : Q \to Q'$. For a configuration $c$ of $M$, write $f_*(c)$ for the
configuration of $M'$ obtained by replacing the state $q$ of $c$ by $f(q)$ and keeping the input
head, the work tapes, the work heads and the output (a halted configuration stays halted). Then
for every configuration $c$ of $M$ and every $t \in \mathbb{N}$, running $M'$ for $t$ steps from
$f_*(c)$ gives $f_*(c_t)$, where $c_t$ is the configuration reached by running $M$ for $t$ steps
from $c$.

Formalized by `Cslib.Turing.MultiTapeTM.IsRelabelling.runFrom`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#run-from-2).

## Initial configurations under relabelling

Let $M$ and $M'$ be deterministic machines with
$k$ work tapes over the same alphabet such that $M'$ simulates $M$ up to a state relabelling $f$.
Then for every input word $x$, the initial configuration of $M'$ on $x$ is the initial
configuration of $M$ on $x$ with its state $q$ replaced by $f(q)$.

Formalized by `Cslib.Turing.MultiTapeTM.IsRelabelling.initCfg`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#init-cfg).

## Lockstep runs from the initial configuration

Let $M$ and $M'$ be deterministic machines
with $k$ work tapes over the same alphabet such that $M'$ simulates $M$ up to a state relabelling
$f$. Then for every input word $x$ and every $t \in \mathbb{N}$, the configuration of $M'$ after
$t$ steps on input $x$ is the configuration of $M$ after $t$ steps on input $x$ with its state
relabelled by $f$: a state $q$ becomes $f(q)$ and the halting state stays halting.

Formalized by `Cslib.Turing.MultiTapeTM.IsRelabelling.runFrom_initCfg`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#run-from-init-cfg).

## Relabelling preserves what a machine computes

Let $M$ and $M'$ be deterministic machines
with $k$ work tapes over the same alphabet such that $M'$ simulates $M$ up to a state relabelling
$f$. Then for all words $x$ and $o$ over the alphabet, $M'$ started on input $x$ eventually halts
with output $o$ if and only if $M$ does.

Formalized by `Cslib.Turing.MultiTapeTM.IsRelabelling.computes_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#computes-iff).

## Relabelling preserves time bounds

Let $M$ and $M'$ be multi-tape Turing machines with
the same number of work tapes and the same alphabet such that $M'$ simulates $M$ up to a state
relabelling $f$. Then for every input $x$ and every $t \in \mathbb{N}$, $M'$ runs in time $t$ on
$x$ if and only if $M$ runs in time $t$ on $x$.

Formalized by `Cslib.Turing.MultiTapeTM.IsRelabelling.runsInTime_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#runs-in-time-iff).

## Relabelling preserves space bounds

Let $M$ and $M'$ be multi-tape Turing machines with
the same number of work tapes and the same alphabet such that $M'$ simulates $M$ up to a state
relabelling $f$. Then for every input $x$ and every $s \in \mathbb{N}$, $M'$ runs in space $s$
on $x$ if and only if $M$ runs in space $s$ on $x$.

Formalized by `Cslib.Turing.MultiTapeTM.IsRelabelling.runsInSpace_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#runs-in-space-iff).

## Relabelling preserves computing a function within time and space bounds

Let $M$ and $M'$
be deterministic machines with $k$ work tapes over the same alphabet such that $M'$ simulates $M$
up to a state relabelling $f$. Let $e_{\mathrm{in}}$ and $e_{\mathrm{out}}$ be injective encodings
of types $\alpha$ and $\beta$ as words over the alphabet, $g : \alpha \to \beta$ a function and
$t, s : \alpha \to \mathbb{N}$ bounds. Then $M'$ computes $g$ with respect to these encodings in
time $t$ and space $s$ if and only if $M$ does. Here a machine does so when, for every
$a \in \alpha$, on input $e_{\mathrm{in}}(a)$ it eventually halts with output
$e_{\mathrm{out}}(g(a))$, every computation path of at least $t(a)$ steps ends halted, and every
computation path visits at most $s(a)$ work-tape cells.

Formalized by `Cslib.Turing.MultiTapeTM.IsRelabelling.computesFunInTimeAndSpace_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#computes-fun-in-time-and-space-iff).

## Relabelling preserves deciding a language

Let $M$ and $M'$ be deterministic machines with
$k$ work tapes over the alphabet $\{\mathrm{false}, \mathrm{true}\}$ such that $M'$ simulates $M$
up to a state relabelling $f$. Then for every set $L$ of binary words, $M'$ decides $L$ if and only
if $M$ decides $L$.

Formalized by `Cslib.Turing.MultiTapeTM.IsRelabelling.decides_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Relabel.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html#decides-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multi-tape Turing machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/multi-tape-turing-machines)
