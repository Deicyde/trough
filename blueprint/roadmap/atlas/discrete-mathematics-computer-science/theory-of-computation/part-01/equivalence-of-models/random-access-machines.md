---
declaration: section
origin: cited
lean: Cslib.Decidability.RAMAddr, Cslib.Decidability.RAMDest, Cslib.Decidability.RAMInstr, Cslib.Decidability.RAMState, Cslib.Decidability.ramResolve, Cslib.Decidability.ramDestIndex, Cslib.Decidability.ramStep, Cslib.Decidability.ramInit
statement: formalized
proof: formalized
---

# Random-access machines

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html).

## RAM addressing mode

An addressing mode of a random-access machine specifies an operand
by a natural number $n$ in one of three ways: immediate (the operand is the value $n$ itself),
direct (the operand is the contents of register $n$), or indirect (the operand is the contents
of the register whose index is the contents of register $n$).

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.RAMAddr`, an inductive type declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#ramaddr).

## RAM store destination

A store destination of a random-access machine names, by a
natural number $n$, the register into which the accumulator is stored: either register $n$
itself (direct) or the register whose index is the contents of register $n$ (indirect).

An immediate operand is not a valid store destination.

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.RAMDest`, an inductive type declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#ramdest).

## RAM instruction

An instruction of a random-access machine is one of the following: load
an operand into the accumulator; store the accumulator into a store destination; add an operand
to the accumulator; subtract an operand from the accumulator, truncating at $0$; jump to
instruction $q$; jump to instruction $q$ if the accumulator is $0$; halt. Here an operand is given
by a RAM addressing mode, a store destination is a RAM store destination, and the jump target $q$
is a natural number.

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.RAMInstr`, an inductive type declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#raminstr).

## RAM state

A state of a random-access machine consists of a program counter in
$\mathbb{N}$, an accumulator value in $\mathbb{N}$, and register contents, a function
$\mathbb{N} \to \mathbb{N}$ giving the contents of each register.

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.RAMState`, a structure declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#ramstate).

## Value of a RAM operand

In a RAM state with register contents $r$, an operand resolves to
a natural number: the immediate operand $n$ resolves to $n$ itself, the direct operand $n$ to
the contents $r(n)$ of register $n$, and the indirect operand $n$ to $r(r(n))$.

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.ramResolve`, a definition declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#ram-resolve).

## Register written by a RAM store

In a RAM state with register contents $r$, a store
destination resolves to a register index: the direct destination $n$ resolves to $n$, and the
indirect destination $n$ resolves to the contents $r(n)$ of register $n$.

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.ramDestIndex`, a definition declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#ram-dest-index).

## One step of a RAM machine

Let $P = (P_0, \dots, P_{\ell-1})$ be a program of length
$\ell$ and $s$ a state with program counter $p$, accumulator $a$ and register contents $r$. If
$p \ge \ell$, the step leaves $s$ unchanged. Otherwise it executes $P_p$, where $v$ denotes
the value of the instruction's operand in $s$: a load sets the accumulator to $v$, an add sets
it to $a + v$, a subtract sets it to $\max(a - v, 0)$, and a store writes $a$ into the
register that its destination resolves to in $s$; each of these also increases the program
counter by $1$. A jump to $q$ sets the program counter to $q$; a jump-if-zero to $q$ sets it
to $q$ if $a = 0$ and to $p + 1$ otherwise; a halt sets it to $\ell$. Nothing else changes.

In particular, once the program counter is at least $\ell$ (for instance after a halt), every
further step leaves the state unchanged.

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.ramStep`, a definition declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#ram-step).

## Initial RAM state

The initial state on inputs $x_0, \dots, x_{k-1}$ has program counter
$0$ and accumulator $0$; register $i$ holds $x_i$ for $i < k$, and every other register holds
$0$.

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.ramInit`, a definition declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#ram-init).

## Bounded execution of a RAM machine

For a program $P$, a natural number $t$ and a state
$s$, the state after $t$ steps of $P$ from $s$ is obtained by applying one step of $P$ to $s$
exactly $t$ times.

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.ramExecN`, a definition declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#ram-exec-n).

## Output of a RAM machine

Let $P$ be a program of length $\ell$ and $x_0, \dots, x_{k-1}$
inputs. Run $P$ from the initial state on these inputs. If for some $t$ the program counter
after $t$ steps is at least $\ell$, the output of $P$ on these inputs is the accumulator after
the least such number of steps; otherwise the output is undefined.

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.ramEval`, a definition declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#ram-eval).

## A RAM step is sticky at halting states

If the program counter of a state $s$ is at
least the length of a program $P$, then one step of $P$ leaves $s$ unchanged.

A halt instruction sets the program counter to the length of the program, so once a halt has
been executed the state no longer changes.

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.ramStep_sticky`, a theorem declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#ram-step-sticky).

## RAM execution is stable once halted

Let $P$ be a program of length $\ell$, $s$ a state
and $t$ a natural number. If the program counter after $t$ steps of $P$ from $s$ is at least
$\ell$, then the state after $t + 1$ steps of $P$ from $s$ equals the state after $t$ steps.

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.ramExecN_stable`, a theorem declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#ram-exec-n-stable).

## RAM execution stays at its halted state

Let $P$ be a program of length $\ell$, $s$ a
state and $t_1 \le t_2$ natural numbers. If the program counter after $t_1$ steps of $P$ from
$s$ is at least $\ell$, then the state after $t_2$ steps of $P$ from $s$ equals the state after
$t_1$ steps.

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.ramExecN_eq_of_halted`, a theorem declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#ram-exec-n-eq-of-halted).

## Output membership for RAM machines

Let $P$ be a program of length $\ell$, let
$x_0, \dots, x_{k-1}$ be inputs and let $t$ and $y$ be natural numbers. If, after $t$ steps of
$P$ from the initial state on these inputs, the program counter is at least $\ell$ and the
accumulator equals $y$, then the output of $P$ on these inputs is defined and equals $y$.

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.mem_ramEval_of_halted`, a theorem declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#mem-ram-eval-of-halted).

## RAM-decidable predicate

A predicate $P$ on the natural numbers is RAM decidable when
there is a RAM program, a finite list of RAM instructions, such that for every natural number $n$
the program, started with $n$ in register $0$ and with the accumulator, the program counter and
every other register at $0$, halts (its program counter reaches or passes the end of the
program) with $1$ in the accumulator if $P(n)$ holds and with $0$ in the accumulator otherwise;
that is, its RAM evaluation on the single input $n$ equals the characteristic function of $P$
at $n$.

## Sources

- Aho–Hopcroft–Ullman, *The Design and Analysis of Computer Algorithms*, 1974, §1.2.

Formalized by `Cslib.Decidability.RAMDecidable`, a definition declared in [CSLibExt/Computability/Decidability/RAMMachines.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RAMMachines.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html#ramdecidable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Random-access machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/equivalence-of-models/random-access-machines)
