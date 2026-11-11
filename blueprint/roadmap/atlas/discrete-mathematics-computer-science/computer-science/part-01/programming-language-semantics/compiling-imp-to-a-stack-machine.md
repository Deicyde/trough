---
declaration: section
origin: cited
lean: Cslib.IMP.StackMachine.Instr, Cslib.IMP.StackMachine.Config, Cslib.IMP.StackMachine.Step, Cslib.IMP.StackMachine.Steps, Cslib.IMP.StackMachine.Step.deterministic, Cslib.IMP.StackMachine.no_step_of_length_le, Cslib.IMP.StackMachine.alen, Cslib.IMP.StackMachine.blen
statement: formalized
proof: formalized
---

# Compiling IMP to a stack machine

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html).

## Stack machine instructions

An instruction of the stack machine is one of
$\mathsf{push}\ n$, $\mathsf{load}\ x$ and $\mathsf{store}\ x$ for natural numbers $n$ and $x$;
the arithmetic instructions $\mathsf{add}$, $\mathsf{sub}$ and $\mathsf{mul}$; the comparison and
Boolean instructions $\mathsf{eq}$, $\mathsf{le}$, $\mathsf{not}$ and $\mathsf{and}$; and the
jumps $\mathsf{jump}\ t$ and $\mathsf{jumpIfZero}\ t$ for a natural number $t$. Jump targets are
absolute program counters.

Formalized by `Cslib.IMP.StackMachine.Instr`, an inductive type declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#instr).

## Stack machine configurations

A configuration of the stack machine is a triple
$(pc, \sigma, s)$ of a program counter $pc \in \mathbb{N}$, a stack $\sigma$, which is a finite list
of natural numbers whose head is the top of the stack, and a state $s$ assigning a natural number
to each variable.

Formalized by `Cslib.IMP.StackMachine.Config`, an abbreviation declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#config).

## Step relation of the stack machine

Let $P$ be a program, that is a list of instructions,
and write $a :: \sigma$ for the stack with top $a$ above the stack $\sigma$. A configuration
$(pc, \sigma, s)$ steps to a configuration $c'$ under $P$ exactly when $pc < |P|$ and, for the
instruction at position $pc$ of $P$ (counted from $0$), one of the following holds, where
$s[x \mapsto v]$ is the state $s$ with variable $x$ set to $v$.

- $\mathsf{push}\ n$: $c' = (pc + 1, n :: \sigma, s)$.
- $\mathsf{load}\ x$: $c' = (pc + 1, s(x) :: \sigma, s)$.
- $\mathsf{store}\ x$: $\sigma = v :: \tau$ and $c' = (pc + 1, \tau, s[x \mapsto v])$.
- $\mathsf{add}$, $\mathsf{sub}$, $\mathsf{mul}$: $\sigma = a :: b :: \tau$ and
  $c' = (pc + 1, r :: \tau, s)$, where $r$ is $b + a$, $\max(b - a, 0)$ or $b \cdot a$ respectively.
- $\mathsf{eq}$, $\mathsf{le}$: $\sigma = a :: b :: \tau$ and $c' = (pc + 1, r :: \tau, s)$,
  where $r$ is $1$ if $b = a$, respectively $b \le a$, and $r = 0$ otherwise.
- $\mathsf{not}$: $\sigma = a :: \tau$ and $c' = (pc + 1, r :: \tau, s)$, where $r = 1$ if $a = 0$
  and $r = 0$ otherwise.
- $\mathsf{and}$: $\sigma = a :: b :: \tau$ and $c' = (pc + 1, r :: \tau, s)$, where $r = 1$ if
  $b \ne 0$ and $a \ne 0$, and $r = 0$ otherwise.
- $\mathsf{jump}\ t$: $c' = (t, \sigma, s)$.
- $\mathsf{jumpIfZero}\ t$: either $\sigma = 0 :: \tau$ and $c' = (t, \tau, s)$, or
  $\sigma = (n + 1) :: \tau$ for some $n$ and $c' = (pc + 1, \tau, s)$.

For binary instructions the top of the stack $a$ is thus the right operand and the value below it
$b$ is the left operand.

Formalized by `Cslib.IMP.StackMachine.Step`, an inductive type declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#step).

## Multi-step execution of the stack machine

For a program $P$, the multi-step relation on
configurations is the reflexive transitive closure of the step relation of the stack machine
running $P$: it relates $c$ to $c'$ when $c'$ is obtained from $c$ by zero or more steps.

Formalized by `Cslib.IMP.StackMachine.Steps`, an abbreviation declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#steps).

## Determinism of the stack machine

For every program $P$, the step relation of the stack
machine running $P$ is deterministic: if a configuration $x$ steps to $y$ and to $z$, then
$y = z$. The fetched instruction and the shape of the stack determine the next configuration.

Formalized by `Cslib.IMP.StackMachine.Step.deterministic`, a theorem declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#deterministic).

## No step past the end of the program

Let $P$ be a program, that is a list of instructions,
and let $(pc, \sigma, s)$ be a configuration with $|P| \le pc$. Then the stack machine running $P$
has no step from $(pc, \sigma, s)$ to any configuration, since there is no instruction at
position $pc$ to fetch.

Hence the length of the code compiled from a command at base address $0$ is a halt address for
that code.

Formalized by `Cslib.IMP.StackMachine.no_step_of_length_le`, a theorem declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#no-step-of-length-le).

## Instruction count of an arithmetic expression

The instruction count $\ell(a)$ of an
arithmetic expression $a$ is defined by recursion on $a$: a constant or a variable has count $1$,
and if $a$ is the sum, difference or product of $a_1$ and $a_2$, then
$\ell(a) = \ell(a_1) + \ell(a_2) + 1$.

It is the number of stack-machine instructions generated when $a$ is compiled.

Formalized by `Cslib.IMP.StackMachine.alen`, a definition declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#alen).

## Instruction count of a Boolean expression

The instruction count $\ell(b)$ of a Boolean
expression $b$ is defined by recursion on $b$, using the instruction count $\ell(a)$ of
arithmetic expressions $a$: a truth value has count $1$; the tests $a_1 = a_2$ and $a_1 \le a_2$
have count $\ell(a_1) + \ell(a_2) + 1$; the negation of $b_1$ has count $\ell(b_1) + 1$; and the
conjunction of $b_1$ and $b_2$ has count $\ell(b_1) + \ell(b_2) + 1$.

It is the number of stack-machine instructions generated when $b$ is compiled.

Formalized by `Cslib.IMP.StackMachine.blen`, a definition declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#blen).

## Instruction count of a command

The instruction count $\ell(c)$ of an IMP command $c$ is
defined by recursion on $c$, using the instruction counts $\ell(a)$ and $\ell(b)$ of arithmetic
and Boolean expressions: $\ell(\mathbf{skip}) = 0$; $\ell(x := a) = \ell(a) + 1$;
$\ell(c_1; c_2) = \ell(c_1) + \ell(c_2)$;
$\ell(\mathbf{if}\ b\ \mathbf{then}\ c_1\ \mathbf{else}\ c_2) =
\ell(b) + 1 + \ell(c_1) + 1 + \ell(c_2)$;
and $\ell(\mathbf{while}\ b\ \mathbf{do}\ c_1) = \ell(b) + 1 + \ell(c_1) + 1$.

It is the number of stack-machine instructions generated when $c$ is compiled.

Formalized by `Cslib.IMP.StackMachine.codeLength`, a definition declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#code-length).

## Compilation of arithmetic expressions

The compiled code of an arithmetic expression is
the list of stack-machine instructions defined by recursion: a constant $n$ compiles to the
single instruction push $n$, a variable $x$ to the single instruction load $x$, and the sum,
difference or product of $a_1$ and $a_2$ to the code of $a_1$, then the code of $a_2$, then the
single instruction add, sub or mul respectively.

Running this code leaves the value of the expression on top of the stack.

Formalized by `Cslib.IMP.StackMachine.compileA`, a definition declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#compile-a).

## Compilation of Boolean expressions

The compiled code of a Boolean expression is the list
of stack-machine instructions defined by recursion, using the compiled code of arithmetic
expressions: the truth value true compiles to the single instruction push $1$ and false to push
$0$; the test $a_1 = a_2$ (respectively $a_1 \le a_2$) compiles to the code of $a_1$, then the
code of $a_2$, then the equality (respectively order) test instruction; the negation of $b_1$
compiles to the code of $b_1$ followed by the negation instruction; and the conjunction of $b_1$
and $b_2$ compiles to the code of $b_1$, then the code of $b_2$, then the conjunction instruction.

Running this code leaves $1$ (true) or $0$ (false) on top of the stack.

Formalized by `Cslib.IMP.StackMachine.compileB`, a definition declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#compile-b).

## Compilation of commands

The compiled code $C_p(c)$ of an IMP command $c$ at base program
counter $p$ is the list of stack-machine instructions defined by recursion on $c$, where jump
targets are absolute program counters and $\ell$ denotes instruction counts:
$C_p(\mathbf{skip})$ is empty; $C_p(x := a)$ is the code of $a$ followed by the instruction
store $x$; $C_p(c_1; c_2)$ is $C_p(c_1)$ followed by $C_{p + \ell(c_1)}(c_2)$. For the
conditional $\mathbf{if}\ b\ \mathbf{then}\ c_1\ \mathbf{else}\ c_2$, put $q = p + \ell(b) + 1$
and $r = q + \ell(c_1) + 1$; its code is the code of $b$, then jump-if-zero to $r$, then
$C_q(c_1)$, then jump to $r + \ell(c_2)$, then $C_r(c_2)$. For the loop
$\mathbf{while}\ b\ \mathbf{do}\ c_1$, put $q = p + \ell(b) + 1$; its code is the code of $b$,
then jump-if-zero to $q + \ell(c_1) + 1$, then $C_q(c_1)$, then jump to $p$.

Formalized by `Cslib.IMP.StackMachine.compile`, a definition declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#compile).

## Fetching from an embedded code segment

Let $B$, $S$ and $A$ be lists of instructions and
let $i < |S|$ be a natural number. Then the instruction at position $|B| + i$ of the concatenation
$B\,S\,A$ of the three lists equals the instruction at position $i$ of $S$, positions being
counted from $0$.

Formalized by `Cslib.IMP.StackMachine.fetch_segment`, a theorem declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#fetch-segment).

## Compiled arithmetic code pushes the value of the expression

Let $a$ be an arithmetic
expression with compiled code $C(a)$ and instruction count $\ell(a)$, let $P$ and $Q$ be lists of
instructions, $\sigma$ a stack and $s$ a state, and write $|P|$ for the length of $P$. The stack
machine running the program $P \, C(a) \, Q$ (the concatenation of $P$, $C(a)$ and $Q$) goes in
finitely many steps from program counter $|P|$, stack $\sigma$ and state $s$ to program counter
$|P| + \ell(a)$, the stack obtained from $\sigma$ by pushing the value of $a$ in $s$, and the
same state $s$.

Formalized by `Cslib.IMP.StackMachine.compileA_runs`, a theorem declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#compile-a-runs).

## Compiled Boolean code pushes the truth value of the expression

Let $b$ be a Boolean
expression with compiled code $C(b)$ and instruction count $\ell(b)$, let $P$ and $Q$ be lists of
instructions, $\sigma$ a stack and $s$ a state, and write $|P|$ for the length of $P$. The stack
machine running the program $P \, C(b) \, Q$ (the concatenation of $P$, $C(b)$ and $Q$) goes in
finitely many steps from program counter $|P|$, stack $\sigma$ and state $s$ to program counter
$|P| + \ell(b)$, the stack obtained from $\sigma$ by pushing $1$ if $b$ evaluates to true in $s$
and $0$ otherwise, and the same state $s$.

Formalized by `Cslib.IMP.StackMachine.compileB_runs`, a theorem declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#compile-b-runs).

## Compiled command code simulates big-step execution

Let $c$ be a command and $s$, $s'$
states such that $c$ run from $s$ terminates in $s'$ under the big-step semantics. Let $P$ and
$Q$ be lists of instructions, $\sigma$ a stack, $|P|$ the length of $P$, $C_p(c)$ the compiled
code of $c$ at base program counter $p$, and $\ell(c)$ the instruction count of $c$. Then the
stack machine running the program $P \, C_{|P|}(c) \, Q$ (the concatenation of $P$,
$C_{|P|}(c)$ and $Q$) goes in finitely many steps from program counter $|P|$, stack $\sigma$ and
state $s$ to program counter $|P| + \ell(c)$, the same stack $\sigma$ and state $s'$.

Formalized by `Cslib.IMP.StackMachine.compile_runs`, a theorem declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 606](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L606). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#compile-runs).

## Correctness of compilation to the stack machine

Let $c$ be a command and $s$, $s'$ states
such that $c$ run from $s$ terminates in $s'$ under the big-step semantics. Let $C_0(c)$ be the
compiled code of $c$ at base program counter $0$ and $\ell(c)$ the instruction count of $c$.
Then the stack machine running $C_0(c)$ goes in finitely many steps from program counter $0$,
the empty stack and state $s$ to program counter $\ell(c)$, the empty stack and state $s'$.

Since $C_0(c)$ has exactly $\ell(c)$ instructions, no step is possible at program counter
$\ell(c)$, so the machine halts there. Only this forward simulation is claimed, not its
converse.

Formalized by `Cslib.IMP.StackMachine.compile_correct`, a theorem declared in [CSLibExt/Languages/IMP/StackMachine.lean, line 860](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/StackMachine.lean#L860). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html#compile-correct).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Compiling IMP to a stack machine](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/programming-language-semantics/compiling-imp-to-a-stack-machine)
