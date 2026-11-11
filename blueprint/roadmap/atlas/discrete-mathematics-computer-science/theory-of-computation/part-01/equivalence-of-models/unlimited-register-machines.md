---
declaration: section
origin: cited
lean: Cslib.URM.encodeInstr, Cslib.URM.encodeInstr_unpair_fst, Cslib.URM.encodeInstr_unpair_snd, Cslib.URM.codedStep, Cslib.URM.primrec_codedStep, Cslib.URM.regBound, Cslib.URM.toRegs, Cslib.URM.toCoded
statement: formalized
proof: formalized
---

# Unlimited register machines

47 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html).

## Code of a URM instruction

**Code of a URM instruction** as a natural number: the instruction tag paired with the
paired arguments, `Z n ↦ pair 0 n`, `S n ↦ pair 1 n`, `T m n ↦ pair 2 (pair m n)`,
`J m n q ↦ pair 3 (pair m (pair n q))`.

Formalized by `Cslib.URM.encodeInstr`, a definition declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#encode-instr).

## Tag of an instruction code

For every URM instruction $I$, unpairing the code of $I$
gives first component $0$ if $I$ is a zero instruction $Z\,n$, $1$ if it is a successor
instruction $S\,n$, $2$ if it is a transfer $T\,m\,n$, and $3$ if it is a jump $J\,m\,n\,q$.

Formalized by `Cslib.URM.encodeInstr_unpair_fst`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#encode-instr-unpair-fst).

## Payload of an instruction code

Write $\langle a, b \rangle$ for the pairing of natural
numbers $a$ and $b$. For every URM instruction $I$, unpairing the code of $I$ gives second
component $n$ if $I$ is $Z\,n$ or $S\,n$, $\langle m, n \rangle$ if $I$ is $T\,m\,n$, and
$\langle m, \langle n, q \rangle \rangle$ if $I$ is $J\,m\,n\,q$.

Formalized by `Cslib.URM.encodeInstr_unpair_snd`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#encode-instr-unpair-snd).

## One coded URM step

A coded state is a program counter $k$ together with a list $r$ of
register contents (in use, the contents of registers $0, \dots, R$, where $R$ is the register bound
of the program), and a program is given by the list $c$ of its instruction codes. Write $c_k$ for
entry $k$ of $c$, and $r_j$ for entry $j$ of $r$, read as $0$ when $j$ is past the end of $r$;
setting an entry past the end of $r$ leaves $r$ unchanged. If $k$ is at least the length of $c$,
the state is halted and has no successor. Otherwise unpair the code $c_k$ as $(i, a)$. If
$i = 0$, the successor is $(k + 1, r')$ where $r'$ is $r$ with entry $a$ set to $0$. If $i = 1$,
it is $(k + 1, r')$ where $r'$ is $r$ with entry $a$ set to $r_a + 1$. If $i = 2$, unpair $a$ as
$(m, n)$; the successor is $(k + 1, r')$ where $r'$ is $r$ with entry $n$ set to $r_m$. If
$i = 3$, unpair $a$ as $(m, b)$ and $b$ as $(n, q)$; the successor is $(q, r)$ if $r_m = r_n$ and
$(k + 1, r)$ otherwise. Any other tag $i$ (which never occurs for a genuine instruction code)
gives no successor.

Formalized by `Cslib.URM.codedStep`, a definition declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#coded-step).

## The coded step is primitive recursive

**The coded step is primitive recursive**, for any fixed list of instruction codes.

Formalized by `Cslib.URM.primrec_codedStep`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#primrec-coded-step).

## Register bound

The register bound $R$ of a URM program $p$ is the sum, over the
instructions of $p$, of the largest register index each instruction refers to. Every register
that an instruction of $p$ can read or write is at most $R$.

Formalized by `Cslib.URM.regBound`, a definition declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#reg-bound).

## Register list

For a URM program $p$ with register bound $R$, the register list of a
register state $\sigma$ is the list $(\sigma(0), \sigma(1), \dots, \sigma(R))$ of the contents of
registers $0, \dots, R$.

Formalized by `Cslib.URM.toRegs`, an abbreviation declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#to-regs).

## Coded machine state

For a URM program $p$ with register bound $R$, the coded state of a
machine state $s$ is the pair consisting of the program counter of $s$ and the register list
$(r_0, \dots, r_R)$ of the contents of registers $0, \dots, R$ of $s$.

Formalized by `Cslib.URM.toCoded`, an abbreviation declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#to-coded).

## Decoding a coded state

A coded state is a pair $(c, \ell)$ of a natural number $c$ and a
list $\ell$ of natural numbers. Its machine state has program counter $c$, and register $n$
holds the $n$-th entry of $\ell$ (counting from $0$) when $n$ is less than the length of $\ell$,
and $0$ otherwise.

Formalized by `Cslib.URM.ofCoded`, an abbreviation declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#of-coded).

## Length of the register list

For a URM program $p$ with register bound $R$ and a register
state $\sigma$, the register list of $\sigma$ (the contents of registers $0, \dots, R$) has length
$R + 1$.

Formalized by `Cslib.URM.length_toRegs`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#length-to-regs).

## Reading the register list

Let $p$ be a URM program with register bound $R$ and
$\sigma$ a register state. For every $n$, the entry at position $n$ of the register list of
$\sigma$, read with default $0$, is $\sigma(n)$ if $n \le R$ and $0$ otherwise.

Formalized by `Cslib.URM.getD_toRegs`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#get-d-to-regs).

## Updating a register updates the register list

Let $p$ be a URM program with register
bound $R$, let $\sigma$ be a register state, and let $n \le R$ and $v$ be natural numbers. The
register list of the state obtained from $\sigma$ by setting register $n$ to $v$ equals the
register list of $\sigma$ with its entry at position $n$ replaced by $v$.

Formalized by `Cslib.URM.toRegs_update`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#to-regs-update).

## Instructions stay within the register bound

For a URM program $p$ with register bound
$R$ and every instruction $I$ of $p$, the largest register index referenced by $I$ is at most
$R$.

Formalized by `Cslib.URM.maxRegister_le_regBound`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#max-register-le-reg-bound).

## Written registers lie within the register bound

Let $p$ be a URM program with register
bound $R$. If an instruction of $p$ writes to register $n$, then $n \le R$.

Formalized by `Cslib.URM.writesTo_le_regBound`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#writes-to-le-reg-bound).

## Registers read by a program lie within the register bound

Let $p$ be a URM program. If
$n$ is a register read by some instruction of $p$, then $n$ is at most the register bound of
$p$.

Formalized by `Cslib.URM.reads_le_regBound`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#reads-le-reg-bound).

## Decoding and re-encoding a coded state gives it back

Let $p$ be a URM program with
register bound $R$, and let $c$ be a coded state: a program counter together with a list of
register contents. If the list has length $R + 1$, then the coded state, with respect to $p$, of
the machine state decoded from $c$ is $c$.

Formalized by `Cslib.URM.toCoded_ofCoded`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#to-coded-of-coded).

## A state that can step is running

If a state $s$ of a URM program $p$ makes a step to some
state, then the program counter of $s$ is less than the number of instructions of $p$.

Formalized by `Cslib.URM.pc_lt_of_step`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#pc-lt-of-step).

## Instruction codes by position

If the URM program $p$ has instruction $I$ at position
$pc$, then the entry at position $pc$ of the list of instruction codes of $p$, read with
default $0$, is the code of $I$.

Formalized by `Cslib.URM.getD_codes`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#get-d-codes).

## A machine step is a coded step

Let $p$ be a URM program, let $R$ be the sum over the
instructions of $p$ of the largest register index each one mentions, and let $s'$ be a state
that $p$ reaches from the state $s$ in one step. Then the coded step, run on the list of codes of
the instructions of $p$, sends the coded state of $s$ (its program counter together with the list
of the contents of its registers $0, \dots, R$) to the coded state of $s'$.

Formalized by `Cslib.URM.codedStep_of_step`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#coded-step-of-step).

## A coded step is a machine step

Let $p$ be a URM program and $s$ a machine state. If one
coded URM step, run on the list of codes of the instructions of $p$ from the coded state of $s$,
yields $c'$, then there is a machine state $s'$ such that $p$ steps from $s$ to $s'$ in one step
and the coded state of $s'$ is $c'$.

Formalized by `Cslib.URM.step_of_codedStep`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#step-of-coded-step).

## URM-decidable predicate

A predicate $P$ on the natural numbers is URM-decidable when
some URM program computes its characteristic function: started on any input $n$ (register $0$
holding $n$, all other registers $0$), the program halts, and register $0$ then holds $1$ if
$P(n)$ holds and $0$ otherwise.

Formalized by `Cslib.URM.Decidable`, a definition declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#decidable).

## URM-recognizable predicates

A predicate $P$ on the natural numbers is URM-recognizable
when there is a URM program that, started with input $n$ in register $0$ and every other register
$0$, halts if and only if $P(n)$ holds.

Formalized by `Cslib.URM.Recognizable`, a definition declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 583](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L583). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#recognizable).

## One-step function on coded states

Given a list of instruction codes, the one-step
function sends a coded state $s$ to the result of one coded URM step from $s$ when that step is
defined, and leaves $s$ unchanged when it is not (in particular when $s$ is halted).

Formalized by `Cslib.URM.stepFn`, a definition declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 593](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L593). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#step-fn).

## The one-step function is primitive recursive

For every list of natural numbers, read as
instruction codes, the function on coded states (pairs of a program counter and a register list)
that sends a coded state to its successor under one coded step, and a coded state with no
successor to itself, is primitive recursive.

Formalized by `Cslib.URM.primrec_stepFn`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 597](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L597). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#primrec-step-fn).

## Bounded execution

For a list of instruction codes, a number $t$ and a coded state $s$,
bounded execution applies the one-step function for these codes $t$ times, starting from
$s$.

Formalized by `Cslib.URM.execN`, a definition declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 602](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L602). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#exec-n).

## Bounded execution unfolds by one step

For a list of instruction codes, a number $t$
and a coded state $s$, bounded execution for $t + 1$ steps from $s$ is the one-step function
applied to the result of bounded execution for $t$ steps from $s$.

Formalized by `Cslib.URM.execN_succ`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 606](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L606). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#exec-n-succ).

## Initial coded state

For a URM program $p$ with register bound $R$ and an input $x$,
the initial coded state has program counter $0$ and register list $(x, 0, \dots, 0)$ of
length $R + 1$: register $0$ holds $x$ and registers $1, \dots, R$ hold $0$.

Formalized by `Cslib.URM.initCoded`, a definition declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 612](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L612). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#init-coded).

## The initial coded state is primitive recursive in the input

**The initial coded state is primitive recursive in the input.**

Formalized by `Cslib.URM.primrec_initCoded`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 616](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L616). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#primrec-init-coded).

## Bounded execution is primitive recursive in the input and the step bound

For a URM
program $p$, the bounded execution of $p$ for $t$ steps ($t$ iterations of the one-step
function on the list of instruction codes of $p$), started from the initial coded state for
input $x$, is a primitive recursive function of the pair $(x, t)$.

Formalized by `Cslib.URM.primrec_execN`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 623](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L623). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#primrec-exec-n).

## The initial coded state codes the initial machine state

For a URM program $p$ and an
input $x$, the initial coded state for $x$ equals the coded state of the initial machine state
with input list $[x]$.

Formalized by `Cslib.URM.initCoded_eq_toCoded`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 629](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L629). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#init-coded-eq-to-coded).

## Bounded execution only reaches codes of reachable states

Let $p$ be a URM program,
$x$ an input and $t$ a natural number. Then there is a machine state $s'$, reachable from the
initial state with input list $[x]$ by steps of $p$, whose coded state equals the result of
bounded execution for $t$ steps on the instruction codes of $p$ from the initial coded state
for $x$.

Formalized by `Cslib.URM.execN_toCoded_steps`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 643](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L643). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#exec-n-to-coded-steps).

## A halted coded state gives a halting machine run

Let $p$ be a URM program, $x$ an input
and $t$ a number. If bounded execution for $t$ steps on the instruction codes of $p$ from the
initial coded state for $x$ reaches a program counter at least the length of the list of
instruction codes, then $p$ halts on the input list $[x]$.

Formalized by `Cslib.URM.halts_of_execN_halted`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 666](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L666). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#halts-of-exec-n-halted).

## Every reachable state is reached by bounded execution

Let $p$ be a URM program and $x$
an input. If a machine state $s$ is reachable from the initial state with input list $[x]$ by
steps of $p$, then for some number $t$, bounded execution for $t$ steps on the instruction codes
of $p$ from the initial coded state for $x$ gives the coded state of $s$.

Formalized by `Cslib.URM.exists_execN_eq_of_steps`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 679](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#exists-exec-n-eq-of-steps).

## Bounded URM execution is stable once halted

Let $c$ be a list of instruction codes, $s$
a coded state and $t$ a natural number. If after $t$ steps of bounded execution of $c$ from $s$
the program counter is at least the length of $c$, then $t + 1$ steps of bounded execution of $c$
from $s$ give the same coded state as $t$ steps.

Formalized by `Cslib.URM.execN_succ_of_halted`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 694](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L694). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#exec-n-succ-of-halted).

## Bounded URM execution stays at its halted value

Let $c$ be a list of instruction codes,
$s$ a coded state, and $t_1 \le t_2$ natural numbers. If after $t_1$ steps of bounded execution
of $c$ from $s$ the program counter is at least the length of $c$, then $t_2$ steps of bounded
execution of $c$ from $s$ give the same coded state as $t_1$ steps.

Formalized by `Cslib.URM.execN_eq_of_le`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 705](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L705). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#exec-n-eq-of-le).

## Output after a given number of steps

For a URM program $p$, an input $x$ and a number
$t$, run bounded execution for $t$ steps on the instruction codes of $p$ from the initial coded
state for $x$. If the resulting program counter is less than the length of the list of
instruction codes, the program is still running and there is no output; otherwise the output
is the entry at position $0$ of the resulting register list, read with default $0$.

Formalized by `Cslib.URM.haltedOutput`, a definition declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 718](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L718). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#halted-output).

## The URM output after a given number of steps is computable

For every URM program $p$,
the function sending an input $x$ and a step count $t$ to the output of $p$ on $x$ after $t$ steps
(nothing while $p$ is still running, the contents of register $0$ once it has halted) is a
computable function of the pair $(x, t)$.

Unbounded search over $t$ then shows that URM evaluation is partial recursive.

Formalized by `Cslib.URM.computable₂_haltedOutput`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 725](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L725). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#computable-halted-output).

## A URM-computable partial function is partial recursive

Let $f$ be a partial function
from $\mathbb{N}$ to $\mathbb{N}$. Suppose some URM program has the following property for every
natural number $x$: started with $x$ in register $0$ and all other registers $0$, it halts
exactly when $f(x)$ is defined, and then it holds $f(x)$ in register $0$. Then $f$ is partial
recursive.

The URM evaluation is the unbounded search for the first halting step of the coded execution.

Formalized by `Cslib.URM.partrec_of_computable`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 746](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L746). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#partrec-of-computable).

## A URM-decidable predicate is computable

If a predicate $P$ on the natural numbers is
URM-decidable, then it is a computable predicate: its Boolean decision function, sending $n$ to
whether $P(n)$ holds, is computable.

Formalized by `Cslib.URM.Decidable.computablePred`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 821](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L821). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#computable-pred).

## A URM-recognizable predicate is recursively enumerable

**A URM-recognizable predicate is recursively enumerable.**

Formalized by `Cslib.URM.Recognizable.rePred`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 831](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L831). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#re-pred).

## A URM-decidable predicate is decidable by a single-tape Turing machine

**A URM-decidable predicate is decidable by a single-tape Turing machine.**

Formalized by `Cslib.URM.Decidable.singleTapeDecidable`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 841](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L841). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#single-tape-decidable).

## A URM-decidable predicate is decidable by a multi-stack Turing machine

**A URM-decidable predicate is decidable by a multi-stack Turing machine.**

Formalized by `Cslib.URM.Decidable.tm2Decidable`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 846](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L846). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#tm2-decidable).

## A URM-recognizable predicate is recognizable by a single-tape Turing machine

**A URM-recognizable predicate is recognizable by a single-tape Turing machine.**

Formalized by `Cslib.URM.Recognizable.singleTapeRecognizable`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 851](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L851). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#single-tape-recognizable).

## A URM-recognizable predicate is recognizable by a multi-stack Turing machine

**A URM-recognizable predicate is recognizable by a multi-stack Turing machine.**

Formalized by `Cslib.URM.Recognizable.tm2Recognizable`, a theorem declared in [CSLibExt/Computability/Decidability/URMBridge.lean, line 856](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/URMBridge.lean#L856). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#tm2-recognizable).

## A URM-computable total function is computed by a multi-stack Turing machine

Let
$f : \mathbb{N} \to \mathbb{N}$. Suppose there is a URM program that, for every $n \in \mathbb{N}$,
started with $n$ in register $0$ and all other registers $0$, halts with $f(n)$ in register $0$.
Then there is a multi-stack Turing machine that computes $f$ with input and output numbers
written in binary: started on the binary word of $n$, it halts with the binary word of $f(n)$.

## Sources

- Sipser, *Introduction to the Theory of Computation*, 3rd ed., §3.1 (Church–Turing thesis) and §3.3 (equivalence of models).

Formalized by `Cslib.Decidability.urmComputable_to_tm2`, a theorem declared in [CSLibExt/Computability/Decidability/ChurchTuring.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/ChurchTuring.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#urm-computable-to-tm2).

## URM-decidability implies multi-stack decidability

Every predicate $P$ on $\mathbb{N}$ that is URM-decidable is decidable by a multi-stack Turing
machine.

## Sources

- Sipser, *Introduction to the Theory of Computation*, 3rd ed., §3.1 (Church–Turing thesis).

Formalized by `Cslib.Decidability.urmDecidable_to_tm2Decidable`, a theorem declared in [CSLibExt/Computability/Decidability/ChurchTuring.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/ChurchTuring.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#urm-decidable-to-tm2-decidable).

## URM-recognizability implies multi-stack recognizability

Every predicate $P$ on $\mathbb{N}$ that is URM-recognizable is recognizable by a multi-stack
Turing machine.

## Sources

- Sipser, *Introduction to the Theory of Computation*, 3rd ed., §3.1 (Church–Turing thesis).

Formalized by `Cslib.Decidability.urmRecognizable_to_tm2Recognizable`, a theorem declared in [CSLibExt/Computability/Decidability/ChurchTuring.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/ChurchTuring.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html#urm-recognizable-to-tm2-recognizable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unlimited register machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/equivalence-of-models/unlimited-register-machines)
