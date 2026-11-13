---
declaration: section
origin: cited
lean: MetaMathlibExt.TM2Program.Flag, MetaMathlibExt.TM2Program.iter_none, MetaMathlibExt.TM2Program.Run, MetaMathlibExt.TM2Program.Run.single, MetaMathlibExt.TM2Program.cnt, MetaMathlibExt.TM2Program.incr, MetaMathlibExt.TM2Program.decr, MetaMathlibExt.TM2Program.pushAll
statement: formalized
proof: formalized
---

# Programming multi-stack machines

59 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html).

## Flag bit of a machine state

A flag on a type $\sigma$ of machine states consists of a map
$\mathrm{tag} : \mathrm{Bool} \to \sigma$ that stores a bit in a state and a map
$\mathrm{untag} : \sigma \to \mathrm{Bool}$ that reads it back, such that
$\mathrm{untag}(\mathrm{tag}(\beta)) = \beta$ for every bit $\beta$. The program primitives use it
to branch on whether a pop found a symbol.

Formalized by `MetaMathlibExt.TM2Program.Flag`, a class declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#flag).

## A halted run stays halted

Let $f : \sigma \to \mathrm{Option}\,\sigma$ be a partial step
function and let $\hat f$ be its lift to $\mathrm{Option}\,\sigma$, which sends $\mathrm{none}$ to
$\mathrm{none}$ and $\mathrm{some}\,x$ to $f(x)$. Then $\hat f^{\,n}(\mathrm{none}) = \mathrm{none}$
for every $n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.TM2Program.iter_none`, a theorem declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#iter-none).

## Exact-length runs of a TM2 machine

Let $M$ be a TM2 machine, given by a statement for
each label, and let $c$ and $d$ be configurations. For $n \in \mathbb{N}$, $M$ runs from $c$ to
$d$ in exactly $n$ steps when applying the step function of $M$ $n$ times, starting at $c$, is
defined at every step (no configuration before the last one has halted) and ends at $d$.

Formalized by `MetaMathlibExt.TM2Program.Run`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#run).

## A single step executes the statement at the current label

Let $M$ be a TM2 machine, $l$
a label, $v$ an internal state, $S$ an assignment of a list of symbols to each stack, and $d$ a
configuration. If executing the statement $M(l)$ from state $v$ and stacks $S$ yields $d$, then
$M$ runs in exactly one step from the configuration with label $l$, state $v$ and stacks $S$ to
$d$.

Formalized by `MetaMathlibExt.TM2Program.Run.single`, a theorem declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#single).

## Unary counter

The unary counter with unit symbol $u$ and value $n \in \mathbb{N}$ is the
list $u^n$ consisting of exactly $n$ copies of $u$.

Formalized by `MetaMathlibExt.TM2Program.cnt`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#cnt).

## Counter increment

For a stack $k$, a symbol $u$ of stack $k$ (the unit of a unary
counter) and a label $\ell$, this statement pushes $u$ onto stack $k$ and then goes to label
$\ell$.

Formalized by `MetaMathlibExt.TM2Program.incr`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#incr).

## Decrement

For a stack $k$ and labels $\ell_0$ and $\ell_+$, this machine statement pops
stack $k$, stores in the state whether a symbol was popped, and goes to $\ell_+$ if a symbol was
popped and to $\ell_0$ if stack $k$ was empty.

Formalized by `MetaMathlibExt.TM2Program.decr`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#decr).

## Pushing symbols onto several stacks

Let $ps$ be a list of pairs $(k, x)$ of a stack index
$k$ and a symbol $x$ of the alphabet of stack $k$, and let $q$ be a statement of a TM2 machine.
This is the statement that, for each pair $(k, x)$ of $ps$ in list order, pushes $x$ onto stack
$k$, and then continues with $q$.

Formalized by `MetaMathlibExt.TM2Program.pushAll`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#push-all).

## Adding units to target stacks

Let $ps$ be a list of pairs $(j, x)$ of a stack $j$ and a
symbol $x$ of stack $j$, let $i \in \mathbb{N}$ and let $S$ be stacks. The resulting stacks are
as follows: if $(k, x)$ is the first pair in $ps$ whose stack is $k$, stack $k$ holds $i$ copies
of $x$ followed by $S_k$ (so the copies are on top); if no pair in $ps$ has stack $k$, stack $k$
holds $S_k$.

When the stacks in the pairs of $ps$ are distinct, the first pair with stack $k$ is the only one.

Formalized by `MetaMathlibExt.TM2Program.addU`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#add-u).

## Counter transfer loop

For a stack $k$, a list $ps$ of pairs $(t, x)$ of a stack $t$ and a
symbol $x$ of stack $t$, and labels $\ell$ and $\ell'$, this machine statement pops stack $k$,
stores in the state whether a symbol was popped, and branches on it: if a symbol was popped, it
pushes $x$ onto $t$ for each pair $(t, x)$ of $ps$ in list order and goes to $\ell$; if stack $k$
was empty, it goes to $\ell'$.

Placed at label $\ell$, it pops $k$ until $k$ is empty and pushes one copy of every target symbol
per popped symbol: with $ps$ empty it drains $k$, with one target it moves the counter, and with
two targets it copies it.

Formalized by `MetaMathlibExt.TM2Program.xfer`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#xfer).

## Running a counter transfer

Let $M$ be a multi-stack machine whose state carries a
flag bit, and suppose that at label $\ell$ it executes the transfer loop that empties stack $k$
into the targets $p_1, \dots, p_m$ and then goes to label $\ell'$. Here each target $p_i$ is a
pair of a stack $t_i$ and a symbol $x_i$ of its alphabet, the stacks $t_1, \dots, t_m$ are
distinct, and $k$ is none of them. Let $u$ be a symbol of stack $k$. Then for every $n$, every
state $v$ and all stack contents $S$ in which stack $k$ holds exactly $u^n$, the machine goes in
exactly $n + 1$ steps from label $\ell$ with state $v$ and stacks $S$ to label $\ell'$ with the
state that stores the flag value false and the stacks obtained from $S$ by emptying stack $k$
and then pushing $n$ copies of $x_i$ on each stack $t_i$.

Formalized by `MetaMathlibExt.TM2Program.xfer_run`, a theorem declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#xfer-run).

## One round of counter comparison

For stacks $a, b, t_a, t_b$, symbols $u_{t_a}$ of stack
$t_a$ and $u_{t_b}$ of stack $t_b$, and labels $\mathit{self}$, $\mathit{lt}$, $\mathit{eq}$ and
$\mathit{gt}$, this machine statement pops stack $a$ and then stack $b$; after each pop it stores
in the state whether the pop found a symbol and branches on it. If both pops found a symbol, it
pushes $u_{t_a}$ onto $t_a$, then $u_{t_b}$ onto $t_b$, and goes to $\mathit{self}$. If only the
pop of $a$ found a symbol, it pushes $u_{t_a}$ onto $t_a$ and goes to $\mathit{gt}$; if only the
pop of $b$ found one, it pushes $u_{t_b}$ onto $t_b$ and goes to $\mathit{lt}$; if neither did,
it goes to $\mathit{eq}$.

Formalized by `MetaMathlibExt.TM2Program.cmpStep`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#cmp-step).

## The comparison loop

Let $a, b, t_a, t_b$ be pairwise distinct stacks with unit symbols
$u_a, u_b, u_{t_a}, u_{t_b}$, and let $r$ map each ordering to a label. Suppose the machine $M$
has at label $\ell$ the comparison round of $a$ and $b$ with scratch stacks $t_a, t_b$ and units
$u_{t_a}, u_{t_b}$ that repeats at $\ell$ and exits to $r(\mathrm{lt})$, $r(\mathrm{eq})$ and
$r(\mathrm{gt})$: it pops $a$ and $b$, pushes $u_{t_a}$ onto $t_a$ if $a$ was non-empty and
$u_{t_b}$ onto $t_b$ if $b$ was non-empty, and goes to $\ell$ if both were non-empty, to
$r(\mathrm{lt})$ if only $b$ was, to $r(\mathrm{eq})$ if neither was and to $r(\mathrm{gt})$ if
only $a$ was. Then for all $m, n, p, q \in \mathbb{N}$, every state $v$ and all stacks $S$ in
which $a, b, t_a, t_b$ hold exactly $u_a^m, u_b^n, u_{t_a}^p, u_{t_b}^q$ respectively, there are
a state $v'$ and stacks $S'$ such that exactly $\min(m, n) + 1$ steps of $M$ lead from label
$\ell$ with state $v$ and stacks $S$ to label $r(\mathrm{compare}(m, n))$ with state $v'$ and
stacks $S'$, where in $S'$ the stack $a$ holds $u_a^{m - \min(m, n+1)}$, $b$ holds
$u_b^{n - \min(n, m+1)}$, $t_a$ holds $u_{t_a}^{p + \min(m, n+1)}$, $t_b$ holds
$u_{t_b}^{q + \min(n, m+1)}$, and every other stack is as in $S$.

Formalized by `MetaMathlibExt.TM2Program.cmpLoop_run`, a theorem declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#cmp-loop-run).

## Non-destructive comparison of two counters

Let $M$ be a TM2 machine whose state type
carries a flag bit, let $a, b, t_a, t_b$ be pairwise distinct stacks with symbols $u_a$, $u_b$,
$u_{t_a}$, $u_{t_b}$ of their alphabets, let $\ell$ be a label and let $r$, $r'$, $o$ map each
ordering to a label. Suppose that $M$ has at $\ell$ the comparison round of $a$ and $b$ with
scratch stacks $t_a, t_b$ and units $u_{t_a}, u_{t_b}$ that goes to $\ell$ again and exits to
$r(\mathrm{lt})$, $r(\mathrm{eq})$ and $r(\mathrm{gt})$, and that for every ordering $\omega$,
$M$ has at $r(\omega)$ the counter transfer loop of $t_a$ into the single target $(a, u_a)$ that
repeats at $r(\omega)$ and exits to $r'(\omega)$, and has at $r'(\omega)$ the counter transfer
loop of $t_b$ into the single target $(b, u_b)$ that repeats at $r'(\omega)$ and exits to
$o(\omega)$. Write $\mathrm{compare}(m, n)$ for the ordering of natural numbers $m$ and $n$, and
$[m \ne n]$ for $1$ if $m \ne n$ and $0$ otherwise. Then for all $m, n \in \mathbb{N}$, every
state $v$ and all stacks $S$ in which $a$ holds exactly $u_a^m$, $b$ holds exactly $u_b^n$ and
$t_a$ and $t_b$ are empty, $M$ runs in exactly $3\min(m, n) + 3 + [m \ne n]$ steps from label
$\ell$ with state $v$ and stacks $S$ to label $o(\mathrm{compare}(m, n))$ with the state that
stores the flag value false and with the same stacks $S$.

Formalized by `MetaMathlibExt.TM2Program.cmp_run`, a theorem declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#cmp-run).

## Sum of consecutive values

For $f : \mathbb{N} \to \mathbb{N}$ and $i, j \in \mathbb{N}$,
$\mathrm{sumFrom}(f, i, j) = f(i) + f(i+1) + \dots + f(i+j-1)$ is the sum of $f(t)$ over the
$j$ indices $t$ with $i \le t < i + j$; it is $0$ when $j = 0$.

Formalized by `MetaMathlibExt.TM2Program.sumFrom`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#sum-from).

## Termwise bound on a sum of consecutive values

Let $f : \mathbb{N} \to \mathbb{N}$ and
$c, i, j \in \mathbb{N}$. If $f(t) \le c$ for every $t$ with $i \le t < i + j$, then
$\mathrm{sumFrom}(f, i, j) = f(i) + f(i+1) + \dots + f(i+j-1)$ is at most $j \cdot c$.

Formalized by `MetaMathlibExt.TM2Program.sumFrom_le`, a theorem declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 444](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#sum-from-le).

## Loop head of a for loop over a counter

For stacks $c$ and $c'$, a symbol $u'$ of stack
$c'$ and labels $b$ and $r$, the loop head is the statement that pops stack $c$, replaces the
machine state by the state whose flag bit records whether a symbol was popped, and branches on
that bit: if a symbol was popped, it pushes $u'$ onto the index stack $c'$ and goes to label $b$
(the loop body); if $c$ was empty, it goes to label $r$.

Formalized by `MetaMathlibExt.TM2Program.forHead`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 461](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L461). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#for-head).

## Exact running time of a for loop over a counter

Let $M$ be a multi-stack machine whose
states carry a flag bit, with $\mathrm{tag}(\beta)$ the state storing the bit $\beta$; write $(\ell,
v, S)$ for the configuration at label $\ell$ with state $v$ and stack contents $S$, and $u^m$ for a
stack holding exactly $m$ copies of the symbol $u$. Let $c \ne c'$ be stacks with a symbol $u$ of
stack $c$ and a symbol $u'$ of stack $c'$, and let $h, b, r, e$ be labels such that at $h$ the
machine runs the loop head on $c$ with index stack $c'$ (pop $c$; if a symbol was popped, push $u'$
onto $c'$ and go to $b$, otherwise go to $r$), and at $r$ it runs the transfer that drains $c'$,
pushing one $u$ onto $c$ per popped symbol, and then goes to $e$. Let $n \in \mathbb{N}$, let
$\mathrm{cost} : \mathbb{N} \to \mathbb{N}$, and let $P(i, S)$ be a predicate such that $P(i, S)$
implies $P(i, S')$ whenever $S$ and $S'$ agree on every stack other than $c$ and $c'$. Assume that
for every $i < n$ and all stack contents $S$ with $S_c = u^{n-1-i}$, $S_{c'} = u'^{\,i+1}$ and $P(i,
S)$, there are a state $v'$ and stack contents $S'$ such that $M$ goes from $(b,
\mathrm{tag}(\mathrm{true}), S)$ to $(h, v', S')$ in exactly $\mathrm{cost}(i)$ steps, with $S'_c =
S_c$, $S'_{c'} = S_{c'}$ and $P(i + 1, S')$. Then for every state $v$ and all stack contents $S$
with $S_c = u^n$, $S_{c'}$ empty and $P(0, S)$, there are stack contents $S'$ such that $M$ goes
from $(h, v, S)$ to $(e, \mathrm{tag}(\mathrm{false}), S')$ in exactly $\sum_{i < n}
(\mathrm{cost}(i) + 1) + n + 2$ steps, with $S'_c = u^n$, $S'_{c'}$ empty and $P(n, S')$.

Formalized by `MetaMathlibExt.TM2Program.forLoop_run`, a theorem declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#for-loop-run).

## Pushing a list of symbols onto one stack

Let $k$ be a stack index, $xs = [x_1, \dots, x_m]$
a list of symbols of the alphabet of stack $k$, and $q$ a statement of a TM2 machine. This is the
statement that pushes $x_1, \dots, x_m$ onto stack $k$ in that order, so that $x_m$ ends on top
when $m \ge 1$, and then continues with $q$.

Formalized by `MetaMathlibExt.TM2Program.pushList`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#push-list).

## Pushing a constant list

For a stack $k$, a list $(x_1, \dots, x_m)$ of symbols of
stack $k$ and a label $\ell$, this statement pushes $x_1, \dots, x_m$ onto stack $k$ in this order,
so that $x_m$ ends on top, and then goes to label $\ell$. The machine executes it in a single
step.

Formalized by `MetaMathlibExt.TM2Program.emit`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 547](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L547). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#emit).

## Copying a counter through a scratch stack

Let $a, c, t$ be pairwise distinct stacks with
unit symbols $u_a, u_c, u_t$. Write $\mathrm{xfer}(k, ps, \ell, \ell')$ for the transfer loop at
label $\ell$ that pops stack $k$ until it is empty, pushing $x$ onto stack $j$ for each pair
$(j, x)$ in $ps$ per popped symbol, and then goes to $\ell'$. Suppose the machine $M$ has
$M(l_1) = \mathrm{xfer}(a, [(c, u_c), (t, u_t)], l_1, l_2)$ and
$M(l_2) = \mathrm{xfer}(t, [(a, u_a)], l_2, \mathit{next})$. Let $m, p \in \mathbb{N}$, let $v$
be a state and let $S$ be stacks in which $a$ holds exactly $u_a^m$, $c$ holds $u_c^p$ and $t$ is
empty. Then exactly $2m + 2$ steps of $M$ lead from label $l_1$ with state $v$ and stacks $S$ to
label $\mathit{next}$ with the state storing the flag false and the stacks $S$ with $c$ replaced
by $u_c^{m+p}$.

Formalized by `MetaMathlibExt.TM2Program.copy_run`, a theorem declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 582](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L582). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#copy-run).

## Adding two counters into a third

Let $a, b, c, t$ be stacks with $a \ne c$, $a \ne t$,
$b \ne c$, $b \ne t$ and $c \ne t$, with unit symbols $u_a, u_b, u_c, u_t$. Write
$\mathrm{xfer}(k, ps, \ell, \ell')$ for the transfer loop at label $\ell$ that pops stack $k$ until
it is empty, pushing $x$ onto stack $j$ for each pair $(j, x)$ in $ps$ per popped symbol, and then
goes to $\ell'$. Suppose the machine $M$ has
$M(l_1) = \mathrm{xfer}(a, [(c, u_c), (t, u_t)], l_1, l_2)$,
$M(l_2) = \mathrm{xfer}(t, [(a, u_a)], l_2, l_3)$,
$M(l_3) = \mathrm{xfer}(b, [(c, u_c), (t, u_t)], l_3, l_4)$ and
$M(l_4) = \mathrm{xfer}(t, [(b, u_b)], l_4, \mathit{next})$. Let $m, n, p \in \mathbb{N}$, let $v$
be a state and let $S$ be stacks in which $a$ holds exactly $u_a^m$, $b$ holds $u_b^n$, $c$ holds
$u_c^p$ and $t$ is empty. Then exactly $2m + 2n + 4$ steps of $M$ lead from label $l_1$ with
state $v$ and stacks $S$ to label $\mathit{next}$ with the state storing the flag false and the
stacks $S$ with $c$ replaced by $u_c^{m+n+p}$.

Formalized by `MetaMathlibExt.TM2Program.add_run`, a theorem declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 610](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L610). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#add-run).

## Multiplying unary counters

Let $M$ be a multi-stack machine whose states carry a flag
bit, with $\mathrm{tag}(\mathrm{false})$ the state storing the bit false; write $(\ell, v, S)$ for
the configuration at label $\ell$ with state $v$ and stack contents $S$, and $u^m$ for a stack
holding exactly $m$ copies of the symbol $u$. Let $a, a', b, c, t$ be pairwise distinct stacks
with symbols $u_a, u_{a'}, u_b, u_c, u_t$ of the respective stacks, and let $h, \ell_1, \ell_2, r,
e$ be labels such that: at $h$ the machine runs the loop head on $a$ with index stack $a'$ (pop
$a$; if a symbol was popped, push $u_{a'}$ onto $a'$ and go to $\ell_1$, otherwise go to $r$); at
$\ell_1$ it runs the transfer that drains $b$, pushing $u_c$ onto $c$ and $u_t$ onto $t$ per
popped symbol, and then goes to $\ell_2$; at $\ell_2$ it runs the transfer that drains $t$,
pushing $u_b$ onto $b$ per popped symbol, and then goes to $h$; and at $r$ it runs the transfer
that drains $a'$, pushing $u_a$ onto $a$ per popped symbol, and then goes to $e$. Then for all
$m, n, p \in \mathbb{N}$, every state $v$ and all stack contents $S$ with $S_a = u_a^m$, $S_{a'}$
empty, $S_b = u_b^n$, $S_c = u_c^p$ and $S_t$ empty, $M$ goes from $(h, v, S)$ to
$(e, \mathrm{tag}(\mathrm{false}), S')$ in exactly $m(2n + 3) + m + 2$ steps, where $S'$ agrees
with $S$ on every stack except $c$ and $S'_c = u_c^{mn + p}$.

Formalized by `MetaMathlibExt.TM2Program.mul_run`, a theorem declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 627](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L627). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#mul-run).

## Repeated block

For a list $ys$ and $n \in \mathbb{N}$, $\mathrm{rep}(ys, n)$ is the
concatenation of $n$ copies of $ys$; it is the empty list when $n = 0$.

Formalized by `MetaMathlibExt.TM2Program.rep`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 682](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L682). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#rep).

## Prepending a constant list

For a stack $k$, a list $(y_1, \dots, y_m)$ of symbols of
stack $k$ and a label $\ell$, this statement pushes $y_m, \dots, y_1$ onto stack $k$ in this order
and then goes to label $\ell$; it is the constant-list push of the reversed list. Afterwards
$y_1, \dots, y_m$ sit on top of stack $k$, read from the top down.

Formalized by `MetaMathlibExt.TM2Program.emitR`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 698](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L698). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#emit-r).

## Draining a counter while prepending a block

Let $k$ and $o$ be stack indices, $ys$ a list
of symbols of the alphabet of stack $o$, and $\ell$ and $\ell'$ labels. This is the TM2 statement
that pops stack $k$ and sets the internal state to the flag bit recording whether a symbol was
popped. If one was, it prepends $ys$ to stack $o$ (so that $ys$ reads from the top down) and goes
to $\ell$; if stack $k$ was empty, it goes to $\ell'$.

Used as the statement at label $\ell$ with $k \ne o$, it empties a unary counter on stack $k$ and
prepends one copy of $ys$ to stack $o$ per unit removed, then goes to $\ell'$.

Formalized by `MetaMathlibExt.TM2Program.xferE`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 707](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L707). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#xfer-e).

## Gap emission

Let $P, Q, T_1, T_2, o$ be pairwise distinct stacks, with unit symbols
$u_P, u_Q, u_{T_1}, u_{T_2}$ for the first four, and let $ys$ be a list of symbols of stack $o$.
Write $\mathrm{xfer}(k, ps, \ell, \ell')$ for the transfer loop at label $\ell$ that pops stack
$k$ until it is empty, pushing $x$ onto stack $j$ for each pair $(j, x)$ in $ps$ per popped
symbol, and then goes to $\ell'$. Let $r, r_B, \mathit{out}$ map each ordering to a label, with
$\mathit{out}(\mathrm{eq}) = \mathit{next}$ and $\mathit{out}(\omega) = \mathit{emit}$ for every
ordering $\omega \ne \mathrm{eq}$. Suppose the machine $M$ has: at label $\mathit{dec}$ the
decrement of $P$ that goes to $\mathit{cmp}$ if a symbol was popped and to $\mathit{ifZero}$ if
$P$ was empty; at label $\mathit{cmp}$ the comparison round of $P$ and $Q$ with scratch stacks
$T_1, T_2$ and units $u_{T_1}, u_{T_2}$ that repeats at $\mathit{cmp}$ and exits to
$r(\mathrm{lt})$, $r(\mathrm{eq})$ and $r(\mathrm{gt})$; for every ordering $\omega$,
$M(r(\omega)) = \mathrm{xfer}(T_1, [(P, u_P)], r(\omega), r_B(\omega))$ and
$M(r_B(\omega)) = \mathrm{xfer}(T_2, [(Q, u_Q)], r_B(\omega), \mathit{out}(\omega))$; and at
label $\mathit{emit}$ the statement that prepends $ys$ to stack $o$ (so that $ys$ reads top-down)
and goes to $\mathit{dec}$. Let $q \in \mathbb{N}$. Then for every $g \in \mathbb{N}$, every
state $v$ and all stacks $S$ in which $P$ holds exactly $u_P^{q+g+1}$, $Q$ holds $u_Q^q$, and
$T_1$ and $T_2$ are empty, exactly $g(3q + 6) + 3q + 4$ steps of $M$ lead from label
$\mathit{dec}$ with state $v$ and stacks $S$ to label $\mathit{next}$ with the state storing the
flag false and the stacks $S$ with $P$ replaced by $u_P^q$ and $o$ replaced by $g$ copies of $ys$
concatenated, followed by the old contents of $o$.

Formalized by `MetaMathlibExt.TM2Program.emitDiff_run`, a theorem declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 750](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L750). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#emit-diff-run).

## Reachability for a TM2 machine

For a TM2 machine $M$ and configurations $c$ and $d$, $d$
is reachable from $c$ when there is some $n \in \mathbb{N}$ such that $M$ runs from $c$ to $d$
in exactly $n$ steps.

Formalized by `MetaMathlibExt.TM2Program.Reach`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 825](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L825). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#reach).

## A for loop over a counter reaches its exit

Let $M$ be a multi-stack machine whose states
carry a flag bit, with $\mathrm{tag}(\beta)$ the state storing the bit $\beta$; write $(\ell, v, S)$
for the configuration at label $\ell$ with state $v$ and stack contents $S$, and $u^m$ for a stack
holding exactly $m$ copies of the symbol $u$. Let $c \ne c'$ be stacks with a symbol $u$ of stack
$c$ and a symbol $u'$ of stack $c'$, and let $h, b, r, e$ be labels such that at $h$ the machine
runs the loop head on $c$ with index stack $c'$ (pop $c$; if a symbol was popped, push $u'$ onto
$c'$ and go to $b$, otherwise go to $r$), and at $r$ it runs the transfer that drains $c'$, pushing
one $u$ onto $c$ per popped symbol, and then goes to $e$. Let $n \in \mathbb{N}$, and let $P(i, S)$
be a predicate such that $P(i, S)$ implies $P(i, S')$ whenever $S$ and $S'$ agree on every stack
other than $c$ and $c'$. Assume that for every $i < n$ and all stack contents $S$ with $S_c =
u^{n-1-i}$, $S_{c'} = u'^{\,i+1}$ and $P(i, S)$, there are a state $v'$ and stack contents $S'$ such
that $M$ goes from $(b, \mathrm{tag}(\mathrm{true}), S)$ to $(h, v', S')$ in finitely many steps,
with $S'_c = S_c$, $S'_{c'} = S_{c'}$ and $P(i + 1, S')$. Then for every state $v$ and all stack
contents $S$ with $S_c = u^n$, $S_{c'}$ empty and $P(0, S)$, there are stack contents $S'$ such that
$M$ goes from $(h, v, S)$ to $(e, \mathrm{tag}(\mathrm{false}), S')$ in finitely many steps, with
$S'_c = u^n$, $S'_{c'}$ empty and $P(n, S')$.

Formalized by `MetaMathlibExt.TM2Program.forLoop_reach`, a theorem declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 841](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L841). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#for-loop-reach).

## Runs within a step budget

For a TM2 machine $M$, a bound $B \in \mathbb{N}$ and
configurations $c$ and $d$, $M$ runs from $c$ to $d$ within $B$ steps when there is some
$n \le B$ such that $M$ runs from $c$ to $d$ in exactly $n$ steps.

Formalized by `MetaMathlibExt.TM2Program.RunLe`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 901](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L901). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#run-le).

## Budgeted run

For a machine $M$, numbers $K, X \in \mathbb{N}$ and configurations $c$ and
$d$, the budgeted run from $c$ to $d$ with $K$ steps already spent and budget $X$ holds when there
is an $n \in \mathbb{N}$ with $K + n \le X$ such that $n$ steps of $M$ lead from $c$ to $d$.

It is used for goal-directed chaining of runs: the chaining lemmas only increase $K$.

Formalized by `MetaMathlibExt.TM2Program.Bud`, a definition declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 907](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L907). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#bud).

## Time bound for a for loop over a counter

Let $M$ be a multi-stack machine whose states
carry a flag bit, with $\mathrm{tag}(\beta)$ the state storing the bit $\beta$; write $(\ell, v, S)$
for the configuration at label $\ell$ with state $v$ and stack contents $S$, and $u^m$ for a stack
holding exactly $m$ copies of the symbol $u$. Let $c \ne c'$ be stacks with a symbol $u$ of stack
$c$ and a symbol $u'$ of stack $c'$, and let $h, b, r, e$ be labels such that at $h$ the machine
runs the loop head on $c$ with index stack $c'$ (pop $c$; if a symbol was popped, push $u'$ onto
$c'$ and go to $b$, otherwise go to $r$), and at $r$ it runs the transfer that drains $c'$, pushing
one $u$ onto $c$ per popped symbol, and then goes to $e$. Let $n \in \mathbb{N}$, let $B \in
\mathbb{N}$, and let $P(i, S)$ be a predicate such that $P(i, S)$ implies $P(i, S')$ whenever $S$
and $S'$ agree on every stack other than $c$ and $c'$. Assume that for every $i < n$ and all stack
contents $S$ with $S_c = u^{n-1-i}$, $S_{c'} = u'^{\,i+1}$ and $P(i, S)$, there are a state $v'$ and
stack contents $S'$ such that $M$ goes from $(b, \mathrm{tag}(\mathrm{true}), S)$ to $(h, v', S')$
in at most $B$ steps, with $S'_c = S_c$, $S'_{c'} = S_{c'}$ and $P(i + 1, S')$. Then for every state
$v$ and all stack contents $S$ with $S_c = u^n$, $S_{c'}$ empty and $P(0, S)$, there are stack
contents $S'$ such that $M$ goes from $(h, v, S)$ to $(e, \mathrm{tag}(\mathrm{false}), S')$ in at
most $n(B + 1) + n + 2$ steps, with $S'_c = u^n$, $S'_{c'}$ empty and $P(n, S')$.

Formalized by `MetaMathlibExt.TM2Program.forLoop_le`, a theorem declared in [MathlibExt/Computability/TuringMachine/Program.lean, line 944](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Program.lean#L944). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#for-loop-le).

## Bit test for the top of a stack

Let $d$ be a decoder that reads each symbol either as a
bit or as a marker. For an optional symbol $o$ (the top of a stack, absent when the stack is
empty), the test is true when $o$ is a symbol that $d$ reads as a bit, and false when $o$ is
absent or $d$ reads it as a marker.

Formalized by `MetaMathlibExt.TM2Program.isBit`, a definition declared in [MathlibExt/Computability/TuringMachine/BitOps.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/BitOps.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#is-bit).

## Bit on top of a stack

Let $d$ be a decoder that reads each symbol either as a bit or as
a marker. For an optional symbol $o$ (the top of a stack, absent when the stack is empty), the
bit of $o$ under $d$ is $x$ when $o$ is a symbol that $d$ reads as the bit $x$, and false when $o$
is absent or $d$ reads it as a marker.

Formalized by `MetaMathlibExt.TM2Program.bitOf`, a definition declared in [MathlibExt/Computability/TuringMachine/BitOps.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/BitOps.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#bit-of).

## Bit blocks

Let $d$ be a decoder that reads each symbol either as a bit or as a marker. A
list of symbols $s_1, \dots, s_n$ is the bit block of a bit string $p$ under $d$ when $p$ has the
same length $n$ and, for each $i$, $d$ reads $s_i$ as the $i$-th bit of $p$.

Formalized by `MetaMathlibExt.TM2Program.IsBitBlock`, a definition declared in [MathlibExt/Computability/TuringMachine/BitOps.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/BitOps.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#is-bit-block).

## End of a bit block

Let $d$ be a decoder that reads each symbol either as a bit or as a
marker. A list of symbols $A$ (the rest of a stack below a block) ends a bit block under $d$ when
$A$ is empty or $d$ reads its first symbol as a marker.

Formalized by `MetaMathlibExt.TM2Program.EndsBitBlock`, a definition declared in [MathlibExt/Computability/TuringMachine/BitOps.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/BitOps.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#ends-bit-block).

## Bit-moving loop

For stacks $a$ and $b$, a decoder $d$ reading each symbol of $a$ as a bit
or a marker, an encoder $g$ from bits to symbols of $b$, and labels $\mathit{self}$ and
$\mathit{next}$, the bit-moving loop from $a$ to $b$ is the statement that looks at the top of
$a$: if it is a symbol that $d$ reads as a bit $x$, it pops it, pushes $g(x)$ onto $b$ and goes to
$\mathit{self}$; if it is a marker or $a$ is empty, it goes to $\mathit{next}$. It overwrites the
state with a flag bit, used as scratch.

Formalized by `MetaMathlibExt.TM2Program.moveB`, a definition declared in [MathlibExt/Computability/TuringMachine/BitOps.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/BitOps.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#move-b).

## Running the bit-moving loop

Let $a \ne b$ be stacks of a program $M$ whose state carries
a flag bit, $d$ a decoder reading each symbol of $a$ as a bit or a marker, $g$ an encoder from bits
to symbols of $b$, and $\mathit{self}$, $\mathit{next}$ labels such that $M$ runs at
$\mathit{self}$ the bit-moving loop from $a$ to $b$ with decoder $d$ and encoder $g$, looping at
$\mathit{self}$ and exiting to $\mathit{next}$. Let $p = p_1 \cdots p_n$ be a bit list and $S$
stack contents in which $a$ holds a bit block for $p$ under $d$ followed by a rest $A$ that ends a
bit block under $d$. Then for every state $v$ there are a state $v'$ and stack contents $S'$ such
that $M$ runs in exactly $n + 1$ steps from label $\mathit{self}$, state $v$ and stacks $S$ to
label $\mathit{next}$, state $v'$ and stacks $S'$, where $S'(a) = A$, $S'(b)$ is
$g(p_n), \dots, g(p_1)$ (top first) followed by $S(b)$, and $S'(k) = S(k)$ for every other stack
$k$.

Formalized by `MetaMathlibExt.TM2Program.moveB_run`, a theorem declared in [MathlibExt/Computability/TuringMachine/BitOps.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/BitOps.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#move-b-run).

## Bit-block comparison statement

Let $a$ and $b$ be stacks with decoders $d_a$ and $d_b$
that read each symbol either as a bit or as a marker, let $t_a$ and $t_b$ be scratch stacks with
bit encoders $e_a$ and $e_b$, and let $\ell$, $\ell_=$ and $\ell_{\ne}$ be labels. The comparison
statement with loop label $\ell$ performs one round of comparison: if the tops of $a$ and $b$ are
the same bit $x$, it pops both, pushes $e_a(x)$ onto $t_a$ and $e_b(x)$ onto $t_b$, and goes to
$\ell$. Otherwise it changes no stack: it goes to $\ell_=$ if neither top is a bit (each of $a$
and $b$ is empty or has a marker on top), and to $\ell_{\ne}$ if the tops are different bits or
exactly one of them is a bit. It records its tests in the one-bit flag of the machine state.

Formalized by `MetaMathlibExt.TM2Program.cmpB`, a definition declared in [MathlibExt/Computability/TuringMachine/BitOps.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/BitOps.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#cmp-b).

## Four pairwise distinct stacks

Four stack indices $a$, $b$, $t_a$, $t_b$ are pairwise
distinct: $a \ne b$, $a \ne t_a$, $a \ne t_b$, $b \ne t_a$, $b \ne t_b$ and $t_a \ne t_b$.

These are the two compared stacks and the two scratch stacks of the bit-block comparison.

Formalized by `MetaMathlibExt.TM2Program.Distinct4`, a structure declared in [MathlibExt/Computability/TuringMachine/BitOps.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/BitOps.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#distinct4).

## Comparison pops a common prefix

Suppose the program has at label $\ell$ the bit-block
comparison statement of stacks $a$ and $b$ (decoders $d_a$, $d_b$) with scratch stacks $t_a$ and
$t_b$ (encoders $e_a$, $e_b$) and loop label $\ell$, and that $a$, $b$, $t_a$, $t_b$ are pairwise
distinct. Let $p = p_1 \dots p_n$ be a bit string, and take a configuration at label $\ell$, with
any state, in which stack $a$ holds a list $X$ on top of $A$ and stack $b$ holds a list $Y$ on
top of $B$, where $X$ is the bit block $p$ under $d_a$ and $Y$ is the bit block $p$ under $d_b$.
Then in exactly $n$ steps the program reaches a configuration at label $\ell$, with some state,
in which stack $a$ is $A$, stack $b$ is $B$, stack $t_a$ holds $e_a(p_n), \dots, e_a(p_1)$ on top
of its old contents, stack $t_b$ holds $e_b(p_n), \dots, e_b(p_1)$ on top of its old contents,
and every other stack is unchanged.

Formalized by `MetaMathlibExt.TM2Program.cmpB_prefix`, a theorem declared in [MathlibExt/Computability/TuringMachine/BitOps.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/BitOps.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#cmp-b-prefix).

## Deciding step of the comparison

Suppose the program has at label $\ell$ the bit-block
comparison statement of stacks $a$ and $b$ (decoders $d_a$, $d_b$; scratch stacks arbitrary) with
loop label $\ell$, equality label $\ell_=$ and mismatch label $\ell_{\ne}$. From a configuration
at label $\ell$, with any state, in which the tops of $a$ and $b$ are not the same bit, the
program takes one step to a configuration with the same stacks and some state, at label $\ell_=$
if neither top is a bit (each of $a$ and $b$ is empty or has a marker on top) and at label
$\ell_{\ne}$ otherwise.

Formalized by `MetaMathlibExt.TM2Program.cmpB_last`, a theorem declared in [MathlibExt/Computability/TuringMachine/BitOps.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/BitOps.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#cmp-b-last).

## Correctness of the bit-block comparison

Suppose the program has at label $\ell$ the
bit-block comparison statement of stacks $a$ and $b$ (decoders $d_a$, $d_b$) with scratch stacks
$t_a$ and $t_b$ (encoders $e_a$, $e_b$), loop label $\ell$, equality label $\ell_=$ and mismatch
label $\ell_{\ne}$, and that $a$, $b$, $t_a$, $t_b$ are pairwise distinct. Let $u$ and $w$ be bit
strings, and take a configuration at label $\ell$, with any state, in which stack $a$ holds a
list $X$ on top of $A$ and stack $b$ holds a list $Y$ on top of $B$, where $X$ is the bit block
$u$ under $d_a$, $Y$ is the bit block $w$ under $d_b$, $A$ ends a bit block under $d_a$ and $B$
ends a bit block under $d_b$. Then there is a common prefix $c = c_1 \dots c_m$ of $u$ and $w$,
after which $u$ and $w$ do not continue with the same bit, such that in exactly $m + 1$ steps the
program reaches a configuration, with some state, at label $\ell_=$ if $u = w$ and at label
$\ell_{\ne}$ otherwise, in which stack $a$ holds $X$ without its first $m$ symbols on top of $A$,
stack $b$ holds $Y$ without its first $m$ symbols on top of $B$, stack $t_a$ holds
$e_a(c_m), \dots, e_a(c_1)$ on top of its old contents, stack $t_b$ holds
$e_b(c_m), \dots, e_b(c_1)$ on top of its old contents, and every other stack is unchanged.

Formalized by `MetaMathlibExt.TM2Program.cmpB_run`, a theorem declared in [MathlibExt/Computability/TuringMachine/BitOps.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/BitOps.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#cmp-b-run).

## Recovering a bit block from its bits

Let $d$ be a decoder reading symbols as bits or
markers and $g$ an encoder from bits to symbols such that $g(b) = x$ whenever $d$ reads $x$ as the
bit $b$. If the symbol list $xs$ is a bit block for the bit list $u$ under $d$ and
$c = c_1 \cdots c_m$ is a prefix of $u$, then the first $m$ symbols of $xs$ are
$g(c_1), \dots, g(c_m)$.

Formalized by `MetaMathlibExt.TM2Program.IsBitBlock.take_eq_map`, a theorem declared in [MathlibExt/Computability/TuringMachine/BitOps.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/BitOps.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#take-eq-map).

## Restoring a stack after a comparison

Let $t \ne a$ be stacks with decoders $d_t$ and
$d_a$ that read each symbol either as a bit or as a marker. Let $e_t$ be a bit encoder for $t$
that $d_t$ reads back ($d_t$ reads $e_t(x)$ as the bit $x$), and let $g_a$ be a bit encoder for
$a$ that inverts $d_a$ ($g_a(x) = s$ whenever $d_a$ reads the symbol $s$ as the bit $x$). Suppose
the program has at label $\ell$ the bit-block move statement from $t$ (decoder $d_t$) onto $a$
(re-encoding $g_a$) with loop label $\ell$ and exit label $\ell'$. Let $X$ be the bit block of a
bit string $u$ under $d_a$ and let $c = c_1 \dots c_m$ be a prefix of $u$. From a configuration
at label $\ell$, with any state, in which stack $t$ holds $e_t(c_m), \dots, e_t(c_1)$ on top of a
list $R$ that ends a bit block under $d_t$, and stack $a$ holds $X$ without its first $m$ symbols
on top of a list $A$, the program reaches in exactly $m + 1$ steps a configuration at label
$\ell'$, with some state, in which stack $t$ is $R$, stack $a$ holds $X$ on top of $A$, and every
other stack is unchanged.

Formalized by `MetaMathlibExt.TM2Program.moveB_restore`, a theorem declared in [MathlibExt/Computability/TuringMachine/BitOps.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/BitOps.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#move-b-restore).

## Popping a list of stacks

For a list $ks$ of stacks and a statement $q$, this is the
statement that pops the stacks listed in $ks$ in order, once per entry (an empty stack stays
empty), after each pop replacing the state by the one storing the old flag or-ed with whether
that pop found a symbol, and then continues with $q$.

Formalized by `MetaMathlibExt.TM2Program.popAll`, a definition declared in [MathlibExt/Computability/TuringMachine/Cleanup.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Cleanup.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#pop-all).

## Cleanup round

For a list $ks$ of stacks and labels $\mathit{self}$ and $\mathit{next}$,
the cleanup round is the statement that sets the state to the one storing the flag value false,
pops the stacks listed in $ks$ in order, once per entry (an empty stack stays empty), while
recording in the flag whether some pop found a symbol, and then goes to $\mathit{self}$ if one
did and to $\mathit{next}$ otherwise.

Formalized by `MetaMathlibExt.TM2Program.cleanS`, a definition declared in [MathlibExt/Computability/TuringMachine/Cleanup.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Cleanup.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#clean-s).

## Cleanup empties its stacks

Let $ks$ be a list of pairwise distinct stacks of a program
$M$ whose state carries a flag bit, and $\mathit{self}$, $\mathit{next}$ labels such that $M$
runs at $\mathit{self}$ the cleanup round for $ks$, looping at $\mathit{self}$ and exiting to
$\mathit{next}$. Let $m$ be a natural number and $S$ stack contents in which every stack of $ks$
holds at most $m$ symbols. Then for every state $v$, $M$ runs in at most $m + 1$ steps from label
$\mathit{self}$, state $v$ and stacks $S$ to label $\mathit{next}$, the state storing the flag
value false, and the stacks $S'$ with $S'(k)$ empty for every $k$ in $ks$ and $S'(k) = S(k)$ for
every other stack $k$.

Formalized by `MetaMathlibExt.TM2Program.clean_run`, a theorem declared in [MathlibExt/Computability/TuringMachine/Cleanup.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Cleanup.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#clean-run).

## Stack embedding

Given a family of stack alphabets $\Gamma$ indexed by the stacks $K$ of a
sub-machine and a family $\Gamma'$ indexed by the stacks $K'$ of a host, a stack embedding
consists of an injective map $e : K \to K'$ renaming the stacks together with, for each stack
$k \in K$, a bijection $\iota_k : \Gamma_k \to \Gamma'_{e(k)}$ from the alphabet of $k$ onto the
alphabet of its image.

Formalized by `MetaMathlibExt.TM2Embedding.SEmb`, a structure declared in [MathlibExt/Computability/TuringMachine/StackEmbedding.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/StackEmbedding.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#semb).

## Translating a statement along a stack embedding

Let $E$ be a stack embedding with stack
renaming $e$ and alphabet bijections $\iota_k$, and let $\varphi$ map the sub-machine's labels to
the host's labels. The translation of a sub-machine statement is the host statement obtained
recursively, where $s$ denotes the current state. A push of the symbol $f(s)$ on stack $k$
becomes a push of $\iota_k(f(s))$ on stack $e(k)$. A peek or pop on stack $k$ becomes a peek or
pop on stack $e(k)$ whose result is mapped back by $\iota_k^{-1}$ before the state update. A jump
to label $f(s)$ becomes a jump to $\varphi(f(s))$. State updates, branches and halt are kept, with
their sub-statements translated.

Formalized by `MetaMathlibExt.TM2Embedding.mapS`, a definition declared in [MathlibExt/Computability/TuringMachine/StackEmbedding.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/StackEmbedding.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#map-s).

## Embedding of a machine in a host

Let $E$ be a stack embedding and $\varphi$ a map from
the labels of a machine $M$ to the labels of a host machine $M'$ over the same internal states.
Then $M$ embeds in $M'$ along $E$ and $\varphi$ when, for every label $\ell$ of $M$, either the
statement of $M'$ at $\varphi(\ell)$ is the statement of $M$ at $\ell$ translated along $E$ and
$\varphi$, or the statement of $M$ at $\ell$ is the halt statement (in which case $M'$ may do
anything at $\varphi(\ell)$).

Formalized by `MetaMathlibExt.TM2Embedding.Embeds`, a definition declared in [MathlibExt/Computability/TuringMachine/StackEmbedding.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/StackEmbedding.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#embeds).

## Agreement of host and sub-machine stacks

Let $E$ be a stack embedding with stack
renaming $e$ and alphabet bijections $\iota_k$. Stack contents $S$ of the sub-machine and $S'$
of the host agree when, for every sub-machine stack $k$, the host stack $e(k)$ holds the list
obtained from $S(k)$ by applying $\iota_k$ to each symbol.

Formalized by `MetaMathlibExt.TM2Embedding.Agree`, a definition declared in [MathlibExt/Computability/TuringMachine/StackEmbedding.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/StackEmbedding.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#agree).

## Frame condition for a stack embedding

Let $E$ be a stack embedding with stack renaming
$e$. Two contents $S'$ and $S''$ of the host's stacks satisfy the frame condition when every host
stack $k'$ outside the image of $e$ has the same contents in both: $S''(k') = S'(k')$ whenever
$e(k) \ne k'$ for every sub-machine stack $k$.

Formalized by `MetaMathlibExt.TM2Embedding.Frame`, a definition declared in [MathlibExt/Computability/TuringMachine/StackEmbedding.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/StackEmbedding.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#frame).

## Executing a translated statement

Let $E$ be a stack embedding with stack renaming $e$, and
let $\varphi$ map sub-machine labels to host labels. Let $q$ be a sub-machine statement, $v$ a
state, $S$ sub-machine stacks and $S'$ host stacks that agree with $S$. Let executing $q$ from
state $v$ and stacks $S$ yield the next label $\ell$ (possibly none), state $w$ and stacks $T$.
Then there are host stacks $T'$ such that executing the translation of $q$ along $E$ and
$\varphi$ from state $v$ and stacks $S'$ yields the next label $\varphi(\ell)$ (none if $\ell$ is
none), state $w$ and stacks $T'$. Moreover $T'$ agrees with $T$, and $S'$, $T'$ satisfy the frame
condition.

Formalized by `MetaMathlibExt.TM2Embedding.stepAux_mapS`, a theorem declared in [MathlibExt/Computability/TuringMachine/StackEmbedding.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/StackEmbedding.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#step-aux-map-s).

## Run embedding

Let $E$ be a stack embedding with stack renaming $e$, let $\varphi$ map the
labels of a machine $M$ to those of a host machine $M'$, and suppose $M$ embeds in $M'$ along $E$
and $\varphi$. Suppose $M$ goes in exactly $n$ steps from label $\ell$, state $v$ and stacks $S$ to
a live label $\ell'$, state $v'$ and stacks $T$, where the start may also be the halted
configuration with no label (whose image under $\varphi$ again has no label). If host stacks $S'$
agree with $S$, then there are host stacks $T'$ such that $M'$ goes in exactly $n$ steps from
label $\varphi(\ell)$, state $v$ and stacks $S'$ to label $\varphi(\ell')$, state $v'$ and stacks
$T'$. Moreover $T'$ agrees with $T$, and $S'$, $T'$ satisfy the frame condition: host stacks
outside the image of $e$ are unchanged.

Formalized by `MetaMathlibExt.TM2Embedding.run_embed`, a theorem declared in [MathlibExt/Computability/TuringMachine/StackEmbedding.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/StackEmbedding.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#run-embed).

## Run embedding for bounded runs

Let $E$ be a stack embedding with stack renaming $e$, let
$\varphi$ map the labels of a machine $M$ to those of a host machine $M'$, and suppose $M$ embeds
in $M'$ along $E$ and $\varphi$. Suppose $M$ goes in at most $B$ steps from label $\ell$, state $v$
and stacks $S$ to label $\ell'$, state $v'$ and stacks $T$, and host stacks $S'$ agree with $S$.
Then there are host stacks $T'$ such that $M'$ goes in at most $B$ steps from label
$\varphi(\ell)$, state $v$ and stacks $S'$ to label $\varphi(\ell')$, state $v'$ and stacks $T'$.
Moreover $T'$ agrees with $T$, and $S'$, $T'$ satisfy the frame condition: host stacks outside
the image of $e$ are unchanged.

Formalized by `MetaMathlibExt.TM2Embedding.runLe_embed`, a theorem declared in [MathlibExt/Computability/TuringMachine/StackEmbedding.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/StackEmbedding.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#run-le-embed).

## Exact program matching transports a run with its step count

Exact program matching transports a run, including a halted endpoint, while preserving
the local state, embedded stacks, untouched host stacks, and exact number of steps.

Formalized by `MetaMathlibExt.TM2Embedding.run_embed_exact`, a theorem declared in [MathlibExt/Computability/TuringMachine/ExactStackEmbedding.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/ExactStackEmbedding.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#run-embed-exact).

## Exact run transport to supplied host final stacks

Source-shaped transport to supplied host final stacks: agreement fixes embedded slots
and the frame condition fixes every other slot, so the host endpoint is exact.

Formalized by `MetaMathlibExt.TM2Embedding.run_embed_exact_of_agree_frame`, a theorem declared in [MathlibExt/Computability/TuringMachine/ExactStackEmbedding.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/ExactStackEmbedding.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#run-embed-exact-of-agree-frame).

## Exact matching transports a bounded run

Exact matching transports a bounded run with arbitrary optional endpoints, retaining
the same step witness and budget as well as agreement and the host frame.

Formalized by `MetaMathlibExt.TM2Embedding.runLe_embed_exact`, a theorem declared in [MathlibExt/Computability/TuringMachine/ExactStackEmbedding.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/ExactStackEmbedding.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html#run-le-embed-exact).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Programming multi-stack machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/programming-multi-stack-machines)
