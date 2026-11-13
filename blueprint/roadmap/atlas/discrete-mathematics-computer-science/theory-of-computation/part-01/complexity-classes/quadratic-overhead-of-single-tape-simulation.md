---
declaration: section
origin: cited
lean: Cslib.Turing.TM2Time.relatesInSteps_go, Cslib.Turing.TM2Time.relatesInSteps_ret, Cslib.Turing.TM2Time.exists_relatesInSteps_stepAux, Cslib.Turing.TM2Time.exists_relatesWithinSteps_tm1_of_step, Cslib.Turing.TM2Time.tm0_step_eq_none_of_step_eq_none, Cslib.Turing.TM2Time.relatesWithinSteps_tm0_of_relatesInSteps_tm1, Cslib.Turing.TM2Time.emulationConstant, Cslib.Turing.TM2Time.exists_tm0_run_of_tm2_run
statement: formalized
proof: formalized
---

# Quadratic overhead of single-tape simulation

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/quadratic-overhead-of-single-tape-simulation/index.html).

## Multi-stack steps on the `TM1` emulator

## The emulator walks right to the top of a stack

Let $M$ be a multi-stack machine, $k$ a
stack, $L$ tape contents whose $k$-th track lists a stack $S$ from bottom to top, and
$n \le |S|$. In the $\mathrm{TM1}$ emulator of $M$, the configuration in the state that walks to
stack $k$ (for a given stack action and continuation), with internal state $v$ and head at the
bottom marker of $L$, reaches in exactly $n$ steps the same configuration with the head moved
$n$ cells to the right.

Formalized by `Cslib.Turing.TM2Time.relatesInSteps_go`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/quadratic-overhead-of-single-tape-simulation/index.html#relates-in-steps-go).

## The emulator walks back to the bottom

Let $M$ be a multi-stack machine and $L$ tape
contents. For every $n$, in the $\mathrm{TM1}$ emulator of $M$, the configuration in the return
state (for a given continuation), with internal state $v$ and head $n$ cells to the right of the
bottom marker of $L$, reaches in exactly $n$ steps the same configuration with the head at the
bottom marker.

Formalized by `Cslib.Turing.TM2Time.relatesInSteps_ret`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/quadratic-overhead-of-single-tape-simulation/index.html#relates-in-steps-ret).

## Running one statement on the emulator

Let $M$ be a multi-stack machine and $N$ a
statement over the same stack alphabets, labels and internal states, and write $|N|$ for the
structural size of $N$. Let $H \in \mathbb{N}$, let $v$ be an internal state, let $S$ be a
family of stacks $S_k$, each of height at most $H$, and let $L$ be tape contents whose $k$-th
track lists $S_k$ from bottom to top, for every $k$. Running the translation of $N$ in the
$\mathrm{TM1}$ emulator of $M$ from state $v$, with the head at the bottom marker of $L$, gives
a configuration that reaches, in some number $m \le |N| (2 (H + |N|) + 2)$ of emulator steps,
a configuration representing the result of running $N$ from state $v$ on the stacks $S$: it
has the corresponding label and the same internal state, and its head is at the bottom marker
of a tape whose $k$-th track lists the $k$-th resulting stack from bottom to top.

Formalized by `Cslib.Turing.TM2Time.exists_relatesInSteps_stepAux`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/quadratic-overhead-of-single-tape-simulation/index.html#exists-relates-in-steps-step-aux).

## One multi-stack step costs at most $1 + B(2(H + B) + 2)$ emulator steps

Let $M$ be a
multi-stack machine in which the statement of every label has size at most $B$, and consider its
emulation by a single-tape machine with an internal store that keeps the stacks side by side on
its tape. Let $c$ be a configuration of $M$ in which every stack has height at most $H$, and let
$c_1$ be a configuration of the emulator that represents $c$. If $M$ moves from $c$ to $c'$ in one
step, then there is a configuration $c_1'$ of the emulator that represents $c'$ and that the
emulator reaches from $c_1$ in at most $1 + B(2(H + B) + 2)$ steps.

The size of a statement is its structural size as a term. This is a counted form of the
correctness of the emulation.

Formalized by `Cslib.Turing.TM2Time.exists_relatesWithinSteps_tm1_of_step`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/quadratic-overhead-of-single-tape-simulation/index.html#exists-relates-within-steps-tm1-of-step).

## The emulation halts where the multi-stack machine halts

A halted configuration is
related only to configurations of the single-tape emulation that do not step.

Formalized by `Cslib.Turing.TM2Time.tm0_step_eq_none_of_step_eq_none`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/quadratic-overhead-of-single-tape-simulation/index.html#tm0-step-eq-none-of-step-eq-none).

## Each step of the $\mathrm{TM1}$ emulator is at most three single-tape steps

Let $M$ be
a multi-stack machine with a default label and a default internal state. If the
$\mathrm{TM1}$ emulator of $M$ goes from $c$ to $c'$ in exactly $m$ steps, then the
single-tape emulation of $M$ goes from the single-tape form of $c$ to the single-tape form of
$c'$ in at most $3m$ steps.

Formalized by `Cslib.Turing.TM2Time.relatesWithinSteps_tm0_of_relatesInSteps_tm1`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/quadratic-overhead-of-single-tape-simulation/index.html#relates-within-steps-tm0-of-relates-in-s).

## Emulation constant

For a bundled multi-stack machine $M$, the emulation constant is
$C = 3(2B + 1) + P$, where $B = \sum_l |M(l)|$ is the total structural size of the statements
$M(l)$ over all labels $l$ (so each statement has size at most $B$), and $P$ is the push bound
of $M$, the total number of push instructions in its statements, which bounds the number of
pushes in one step.

Formalized by `Cslib.Turing.TM2Time.emulationConstant`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/quadratic-overhead-of-single-tape-simulation/index.html#emulation-constant).

## Quadratic overhead of the single-tape emulation

Let $M$ be a bundled multi-stack
machine with emulation constant $C$, and $L$ an input for its input stack. If $M$, started on
$L$, reaches a configuration $c$ after $t$ steps, then the single-tape emulation of $M$,
started on the encoding of $L$, reaches in some number $n \le C t (|L| + C t + 1)$ of steps the
single-tape form of a configuration of the $\mathrm{TM1}$ emulator of $M$ that represents $c$:
it has the corresponding label and the same internal state, and its head is at the bottom
marker of a tape whose $k$-th track lists the $k$-th stack of $c$ from bottom to top.

Formalized by `Cslib.Turing.TM2Time.exists_tm0_run_of_tm2_run`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/quadratic-overhead-of-single-tape-simulation/index.html#exists-tm0-run-of-tm2-run).

## Single-tape emulation of halting multi-stack runs

Let $M$ be a bundled multi-stack
machine with emulation constant $C$, and $L$ an input for its input stack. If $M$, started on
$L$, reaches after $t$ steps a configuration $c$ from which it does not step, then the
single-tape emulation of $M$, started on the encoding of $L$, reaches in some number
$n \le C t (|L| + C t + 1)$ of steps a configuration from which it does not step. That
configuration is the single-tape form of a configuration of the $\mathrm{TM1}$ emulator of $M$
that represents $c$: it has the corresponding label and the same internal state, and its head
is at the bottom marker of a tape whose $k$-th track lists the $k$-th stack of $c$ from bottom
to top.

Formalized by `Cslib.Turing.TM2Time.exists_tm0_halt_of_tm2_halt`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/TM2Time.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/quadratic-overhead-of-single-tape-simulation/index.html#exists-tm0-halt-of-tm2-halt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quadratic overhead of single-tape simulation](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/quadratic-overhead-of-single-tape-simulation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/complexity-classes/quadratic-overhead-of-single-tape-simulation)
