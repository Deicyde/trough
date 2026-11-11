---
declaration: section
origin: cited
lean: Cslib.Decidability.CounterInstr, Cslib.Decidability.CounterState, Cslib.Decidability.counterStep, Cslib.Decidability.counterInit, Cslib.Decidability.counterExecN, Cslib.Decidability.counterEval, Cslib.Decidability.counterStep_sticky, Cslib.Decidability.counterExecN_stable
statement: formalized
proof: formalized
---

# Counter machines

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/counter-machines/index.html).

## Counter-machine instructions

A counter-machine instruction is one of: increment register
$r$, decrement register $r$, or jump to instruction $q$ if register $r$ is zero, where the
register index $r$ and the jump target $q$ are natural numbers.

Decrementing a register that holds $0$ leaves it at $0$.

## Sources

- Minsky, *Computation: Finite and Infinite Machines*, 1967, §11.

Formalized by `Cslib.Decidability.CounterInstr`, an inductive type declared in [CSLibExt/Computability/Decidability/CounterMachines.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CounterMachines.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/counter-machines/index.html#counter-instr).

## Counter-machine states

A counter-machine state consists of a program counter, which is a
natural number, and the register contents, a function assigning a natural number to every
register index $i \in \mathbb{N}$.

## Sources

- Minsky, *Computation: Finite and Infinite Machines*, 1967, §11.

Formalized by `Cslib.Decidability.CounterState`, a structure declared in [CSLibExt/Computability/Decidability/CounterMachines.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CounterMachines.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/counter-machines/index.html#counter-state).

## One step of a counter machine

Let $p$ be a counter-machine program, a list of
instructions indexed from $0$, and let $s$ be a state with program counter $c$. If $c$ is at
least the length of $p$ (the machine has halted), the step leaves $s$ unchanged. Otherwise it
executes instruction $c$ of $p$: increment register $r$ adds $1$ to register $r$ and sets the
program counter to $c + 1$; decrement register $r$ subtracts $1$ from register $r$ if it is
positive, leaves it at $0$ otherwise, and sets the program counter to $c + 1$; jump to $q$ if
register $r$ is zero leaves the registers unchanged and sets the program counter to $q$ if
register $r$ holds $0$ and to $c + 1$ otherwise.

Because halted states are fixed, the step can be iterated any number of times.

## Sources

- Minsky, *Computation: Finite and Infinite Machines*, 1967, §11.

Formalized by `Cslib.Decidability.counterStep`, a definition declared in [CSLibExt/Computability/Decidability/CounterMachines.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CounterMachines.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/counter-machines/index.html#counter-step).

## Initial state of a counter machine

The initial counter-machine state on a list of inputs
$x_0, \dots, x_{k-1}$ has program counter $0$, register $i$ holding $x_i$ for each $i < k$, and
every other register holding $0$.

## Sources

- Minsky, *Computation: Finite and Infinite Machines*, 1967, §11.

Formalized by `Cslib.Decidability.counterInit`, a definition declared in [CSLibExt/Computability/Decidability/CounterMachines.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CounterMachines.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/counter-machines/index.html#counter-init).

## Bounded execution of a counter machine

For a counter-machine program $p$, a natural
number $t$ and a state $s$, the execution of $p$ for $t$ steps from $s$ is the state obtained from
$s$ by applying $t$ single steps of $p$.

## Sources

- Minsky, *Computation: Finite and Infinite Machines*, 1967, §11.

Formalized by `Cslib.Decidability.counterExecN`, a definition declared in [CSLibExt/Computability/Decidability/CounterMachines.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CounterMachines.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/counter-machines/index.html#counter-exec-n).

## Output of a counter machine

The output of a counter-machine program $p$ on a list of
inputs is the partial natural number obtained as follows: run $p$ from the initial state on those
inputs; if for some number $t$ of steps the program counter is at least the length of $p$ (the
machine has halted), the output is the content of register $0$ after the least such $t$; if no
such $t$ exists, the output is undefined.

## Sources

- Minsky, *Computation: Finite and Infinite Machines*, 1967, §11.

Formalized by `Cslib.Decidability.counterEval`, a definition declared in [CSLibExt/Computability/Decidability/CounterMachines.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CounterMachines.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/counter-machines/index.html#counter-eval).

## A counter step is sticky at halting states

Past the end of the
program the state does not change.

## Sources

- Minsky, *Computation: Finite and Infinite Machines*, 1967, §11.

Formalized by `Cslib.Decidability.counterStep_sticky`, a theorem declared in [CSLibExt/Computability/Decidability/CounterMachines.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CounterMachines.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/counter-machines/index.html#counter-step-sticky).

## Counter-machine execution is stable once halted

Let $p$ be a counter-machine program,
$s$ a state and $t$ a natural number. If the state reached from $s$ after $t$ steps of $p$ has
program counter at least the length of $p$, then the state reached from $s$ after $t + 1$ steps
equals the state reached after $t$ steps.

## Sources

- Minsky, *Computation: Finite and Infinite Machines*, 1967, §11.

Formalized by `Cslib.Decidability.counterExecN_stable`, a theorem declared in [CSLibExt/Computability/Decidability/CounterMachines.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CounterMachines.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/counter-machines/index.html#counter-exec-n-stable).

## Counter-machine execution is constant after halting

Let $p$ be a counter-machine
program, $s$ a state, and $t_1 \le t_2$ natural numbers. If the state reached from $s$ after
$t_1$ steps of $p$ has program counter at least the length of $p$, then the state reached from $s$
after $t_2$ steps equals the state reached after $t_1$ steps.

## Sources

- Minsky, *Computation: Finite and Infinite Machines*, 1967, §11.

Formalized by `Cslib.Decidability.counterExecN_eq_of_halted`, a theorem declared in [CSLibExt/Computability/Decidability/CounterMachines.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CounterMachines.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/counter-machines/index.html#counter-exec-n-eq-of-halted).

## Output membership for counter machines

Let $P$ be a counter-machine program, let $x$ be
a list of natural-number inputs, and let $t$ and $y$ be natural numbers. If the state reached
after $t$ steps of $P$ from the initial state on $x$ has program counter at least the length
of $P$ (so the machine has halted) and register $0$ holds $y$ in that state, then the output
of $P$ on $x$ is defined and equals $y$.

## Sources

- Minsky, *Computation: Finite and Infinite Machines*, 1967, §11.

Formalized by `Cslib.Decidability.mem_counterEval_of_halted`, a theorem declared in [CSLibExt/Computability/Decidability/CounterMachines.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CounterMachines.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/counter-machines/index.html#mem-counter-eval-of-halted).

## Counter-machine decidable predicates

A predicate $P$ on the natural numbers is
counter-machine decidable when some counter-machine program computes its characteristic
function: for every natural number $n$, the output of the program on the single input $n$ is
defined and equals $1$ if $P(n)$ holds and $0$ otherwise.

## Sources

- Minsky, *Computation: Finite and Infinite Machines*, 1967, §11.

Formalized by `Cslib.Decidability.CounterDecidable`, a definition declared in [CSLibExt/Computability/Decidability/CounterMachines.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CounterMachines.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/counter-machines/index.html#counter-decidable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Counter machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/counter-machines/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/equivalence-of-models/counter-machines)
