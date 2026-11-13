---
declaration: section
origin: cited
lean: MetaMathlibExt.TM2Composition.CK, MetaMathlibExt.TM2Composition.X, MetaMathlibExt.TM2Composition.CΓ, MetaMathlibExt.TM2Composition.CΛ, MetaMathlibExt.TM2Composition.Cσ, MetaMathlibExt.TM2Composition.pop1, MetaMathlibExt.TM2Composition.push1, MetaMathlibExt.TM2Composition.pop2
statement: formalized
proof: formalized
---

# Composition of multi-stack machines

34 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html).

## Stack indices of the composite machine

For finite multi-stack Turing machines $M_1$ and
$M_2$ with stack index sets $K_1$ and $K_2$, the stacks of their composite machine are indexed by
the disjoint union $K_1 \sqcup K_2 \sqcup \{\ast\}$: the stacks of $M_1$, the stacks of $M_2$, and
one scratch stack $\ast$.

Formalized by `MetaMathlibExt.TM2Composition.CK`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#ck).

## Intermediate alphabet of the composite machine

For a multi-stack Turing machine (a TM2
machine) $M_2$ with input stack $k_0$, this is the alphabet of the symbols on stack $k_0$ of $M_2$.

When a machine $M_1$ is composed with $M_2$, the composite machine uses this alphabet for its
scratch stack and for the symbol held in its control state.

Formalized by `MetaMathlibExt.TM2Composition.X`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#x).

## Stack alphabets of the composite machine

Let $M_1$ and $M_2$ be finite multi-stack Turing
machines and let $X$ be the alphabet of the input stack of $M_2$. The stacks of their composite
machine are the stacks of $M_1$, the stacks of $M_2$ and one scratch stack. Each stack of $M_1$
keeps its alphabet from $M_1$, each stack of $M_2$ keeps its alphabet from $M_2$, and the scratch
stack has alphabet $X$.

Formalized by `MetaMathlibExt.TM2Composition.CΓ`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#c).

## Labels of the composite machine

Let $M_1$ and $M_2$ be finite multi-stack Turing
machines with label sets $\Lambda_1$ and $\Lambda_2$, and let $X$ be the alphabet of the input
stack of $M_2$. The label set of their composite machine is the disjoint union of $\Lambda_1$,
$\Lambda_2$ and two copies of $X \sqcup \{\bot\}$, one for each copy loop: in each copy, $\bot$
labels the step that pops and $x \in X$ labels the step that pushes $x$.

Formalized by `MetaMathlibExt.TM2Composition.CΛ`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#c-2).

## States of the composite machine

Let $M_1$ and $M_2$ be finite multi-stack Turing machines
with internal state sets $\sigma_1$ and $\sigma_2$, and let $X$ be the alphabet of the input stack
of $M_2$. The internal states of their composite machine are the triples in
$\sigma_1 \times \sigma_2 \times (X \sqcup \{\bot\})$: a state of $M_1$, a state of $M_2$, and
either the symbol just popped by a copy loop or $\bot$ when there is none.

Formalized by `MetaMathlibExt.TM2Composition.Cσ`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#c-3).

## Pop label of the first copy loop

In the composite machine of $M_1$ and $M_2$, this is
the label $\mathrm{none}$ in the first copy-loop part of the label set; the composite program
uses it to pop a symbol from $M_1$'s output stack.

Formalized by `MetaMathlibExt.TM2Composition.pop1`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#pop1).

## Push labels of the first copy loop

In the composite machine of $M_1$ and $M_2$, for a
symbol $x$ of $M_2$'s input alphabet, this is the label $\mathrm{some}\ x$ in the first copy-loop
part of the label set; the composite program uses it to push $x$ on the scratch stack.

Formalized by `MetaMathlibExt.TM2Composition.push1`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#push1).

## Pop label of the second copy loop

In the composite machine of $M_1$ and $M_2$, this is
the label $\mathrm{none}$ in the second copy-loop part of the label set; the composite program
uses it to pop a symbol from the scratch stack.

Formalized by `MetaMathlibExt.TM2Composition.pop2`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#pop2).

## Push labels of the second copy loop

In the composite machine of $M_1$ and $M_2$, for a
symbol $x$ of $M_2$'s input alphabet, this is the label $\mathrm{some}\ x$ in the second
copy-loop part of the label set; the composite program uses it to push $x$ on $M_2$'s input
stack.

Formalized by `MetaMathlibExt.TM2Composition.push2`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#push2).

## Scratch stack of the composite machine

For multi-stack Turing machines (TM2 machines)
$M_1$ and $M_2$ with stack index types $K_1$ and $K_2$, the composite machine has stack indices
$K_1 \oplus K_2 \oplus \mathrm{Unit}$; its scratch stack is the index given by the unique element
of the $\mathrm{Unit}$ summand.

Formalized by `MetaMathlibExt.TM2Composition.tmp`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#tmp).

## Lifting a statement of the first machine

Given finite multi-stack Turing machines
$M_1$ and $M_2$, a statement of $M_1$ is translated into a statement of their composite
machine, whose state is a triple $(v_1, v_2, o)$, by recursion on the statement: an operation
on a stack $k$ of $M_1$ acts on the copy of $k$ among the composite stacks, every read or update
of $M_1$'s state reads or updates the component $v_1$ and leaves $v_2$ and $o$ unchanged, a
branch tests $v_1$, a jump to a label $l$ of $M_1$ becomes a jump to the copy of $l$, and
halting becomes a jump to the pop label of the first copy loop, which moves $M_1$'s output.

Formalized by `MetaMathlibExt.TM2Composition.lift₁`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#lift).

## Lifting a statement of the second machine

Given finite multi-stack Turing machines
$M_1$ and $M_2$, a statement of $M_2$ is translated into a statement of their composite
machine, whose state is a triple $(v_1, v_2, o)$, by recursion on the statement: an operation
on a stack $k$ of $M_2$ acts on the copy of $k$ among the composite stacks, every read or update
of $M_2$'s state reads or updates the component $v_2$ and leaves $v_1$ and $o$ unchanged, a
branch tests $v_2$, a jump to a label $l$ of $M_2$ becomes a jump to the copy of $l$, and
halting stays halting.

Formalized by `MetaMathlibExt.TM2Composition.lift₂`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#lift-2).

## The program of the composite machine

Let $M_1$ and $M_2$ be finite multi-stack Turing
machines and $\varphi$ a map from $M_1$'s output alphabet to $M_2$'s input alphabet. At a label
of $M_1$ or of $M_2$ the composite program runs the lifted statement of that machine at that
label. At the pop label of the first copy loop it pops $M_1$'s output stack, stores the image
under $\varphi$ of the popped symbol (or nothing) in the third state component, and jumps to the
push label of the first loop for that image, or to the pop label of the second loop if the
stack was empty. At the push label of the first loop for $x$ it pushes $x$ on the scratch stack
and jumps to the first pop label. At the pop label of the second loop it pops the scratch
stack, stores the popped symbol (or nothing) in the third state component, and jumps to the
push label of the second loop for that symbol, or to the copy of $M_2$'s main label if the
scratch stack was empty. At the push label of the second loop for $x$ it pushes $x$ on $M_2$'s
input stack and jumps to the second pop label.

Formalized by `MetaMathlibExt.TM2Composition.prog`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#prog).

## The composite machine

Let $M_1$ and $M_2$ be finite multi-stack Turing machines, let $X$ be
the alphabet of the input stack of $M_2$, and let $\varphi$ map the output alphabet of $M_1$ to $X$.
The composite machine has the stacks of $M_1$, the stacks of $M_2$ and one scratch stack with
alphabet $X$; its input stack is that of $M_1$ and its output stack is that of $M_2$. It starts
at the main label of $M_1$, in the state made of the initial states of $M_1$ and $M_2$ and no held
symbol. It runs $M_1$; when $M_1$ halts, it pops the output stack of $M_1$ onto the scratch stack,
translating each symbol by $\varphi$, then pops the scratch stack onto the input stack of $M_2$,
then runs $M_2$ from its main label, and it halts when $M_2$ halts.

Formalized by `MetaMathlibExt.TM2Composition.compTM`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#comp-tm).

## Assembling the stacks of the composite machine

Given finite multi-stack Turing machines
$M_1$ and $M_2$, contents $S_1$ for the stacks of $M_1$, contents $S_2$ for the stacks of $M_2$,
and a list $t$ of symbols of $M_2$'s input alphabet, the stack contents of their composite
machine put $S_1(k)$ on the copy of each stack $k$ of $M_1$, $S_2(k)$ on the copy of each stack
$k$ of $M_2$, and $t$ on the scratch stack.

Formalized by `MetaMathlibExt.TM2Composition.mkStk`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#mk-stk).

## Composite label of an $M_1$ label

A label $l$ of $M_1$ is sent to $l$ viewed as a label of
the $M_1$ part of the composite of $M_1$ and $M_2$, and the halted label is sent to the label that
pops $M_1$'s output stack, which starts the first copy loop.

Formalized by `MetaMathlibExt.TM2Composition.lab₁`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#lab).

## Embedding of $M_1$'s configurations into the composite machine

A configuration $c$ of $M_1$
is sent to the configuration of the composite of $M_1$ and $M_2$ whose label is the label of $c$
viewed as a label of the $M_1$ part, or the label that pops $M_1$'s output stack (the start of the
first copy loop) if $c$ is halted, whose state is $(v, q_2, \mathrm{none})$ with $v$ the state of
$c$ and $q_2$ the initial state of $M_2$, and whose stacks are the stacks of $c$ on $M_1$'s stacks,
with $M_2$'s stacks and the scratch stack empty.

Formalized by `MetaMathlibExt.TM2Composition.emb₁`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#emb).

## Embedding of $M_2$'s configurations into the composite machine

A configuration $c$ of $M_2$
is sent to the configuration of the composite of $M_1$ and $M_2$ whose label is the label of $c$
viewed as a label of the $M_2$ part (halted if $c$ is halted), whose state is
$(q_1, v, \mathrm{none})$ with $q_1$ the initial state of $M_1$ and $v$ the state of $c$, and whose
stacks are the stacks of $c$ on $M_2$'s stacks, with $M_1$'s stacks and the scratch stack
empty.

Formalized by `MetaMathlibExt.TM2Composition.emb₂`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#emb-2).

## Simulation transports runs

Let $f : \alpha \to \mathrm{Option}\,\alpha$ and
$g : \beta \to \mathrm{Option}\,\beta$ be partial step functions (a value $\mathrm{none}$ means
halting) and $e : \alpha \to \beta$ a map such that $f(c) = c'$ implies $g(e(c)) = e(c')$ for all
$c, c'$. Then for every $n$ and all $c, d \in \alpha$, if $n$ steps of $f$ starting from $c$ end
at $d$, then $n$ steps of $g$ starting from $e(c)$ end at $e(d)$.

Halted configurations are absorbing, so every intermediate configuration of such a run is live.

Formalized by `MetaMathlibExt.TM2Composition.iter_sim`, a theorem declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#iter-sim).

## First copy loop of the composite machine

Consider the composite program of machines $M_1$
and $M_2$ with symbol translation $\varphi$. Suppose it is at the label that pops $M_1$'s output
stack, with state $(v_1, v_2, o)$, with $M_1$'s stacks holding $S_1$, $M_2$'s stacks holding $S_2$,
the scratch stack holding $t$, and $M_1$'s output stack holding the list $y$. Then after exactly
$2|y| + 1$ steps it is at the label that pops the scratch stack, with state
$(v_1, v_2, \mathrm{none})$, $M_1$'s output stack empty and its other stacks unchanged, $M_2$'s
stacks still $S_2$, and the scratch stack holding the reverse of the list obtained by applying
$\varphi$ to each symbol of $y$, followed by $t$.

Formalized by `MetaMathlibExt.TM2Composition.copy₁`, a theorem declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#copy).

## Second copy loop of the composite machine

Consider the composite program of machines
$M_1$ and $M_2$ with symbol translation $\varphi$. Suppose it is at the label that pops the
scratch stack, with state $(v_1, v_2, o)$, with $M_1$'s stacks holding $S_1$, $M_2$'s stacks
holding $S_2$, and the scratch stack holding the list $t$. Then after exactly $2|t| + 1$ steps it
is at the start label of $M_2$, with state $(v_1, v_2, \mathrm{none})$, $M_1$'s stacks still
$S_1$, $M_2$'s input stack holding the reverse of $t$ followed by its previous contents, $M_2$'s
other stacks unchanged, and the scratch stack empty.

Formalized by `MetaMathlibExt.TM2Composition.copy₂`, a theorem declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#copy-2).

## Number of push instructions in a TM2 statement

For a statement $q$ of a multi-stack
Turing machine (Mathlib's TM2 model), this is the number of push nodes in $q$: a push node counts
$1$ plus the count of its continuation; peek, pop and load nodes count as their continuation; a
branch counts the sum of its two branches; goto and halt count $0$.

It is an upper bound on the number of symbols pushed in one step.

Formalized by `MetaMathlibExt.TM2Composition.pushes`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#pushes).

## Push bound of a finite multi-stack Turing machine

For a finite multi-stack Turing
machine $M$ (Mathlib's TM2 model with finitely many labels), the push bound of $M$ is the sum,
over all labels $l$ of $M$, of the number of push instructions in the statement that $M$
assigns to $l$.

No stack of $M$ grows by more than the push bound in a single step.

Formalized by `MetaMathlibExt.TM2Composition.pushBound`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#push-bound).

## Evaluation of a natural-number polynomial is monotone

For every polynomial $p$ with
coefficients in $\mathbb{N}$ and all natural numbers $a \le b$, we have $p(a) \le p(b)$.

Formalized by `MetaMathlibExt.TM2Composition.eval_mono`, a theorem declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#eval-mono).

## Stacks of the initial configuration are no longer than the input

Let $M$ be a finite
multi-stack Turing machine (Mathlib's TM2 model with finitely many stacks, function labels and
internal states, and a finite input alphabet) with input stack $k_0$, and let $l$ be a list of
symbols from the alphabet of stack $k_0$. Then for every stack $k$ of $M$, the stack $k$ in the
initial configuration of $M$ on input $l$ has length at most the length of $l$.

The initial configuration holds $l$ on stack $k_0$ and leaves every other stack empty.

Formalized by `MetaMathlibExt.TM2Composition.initList_stk_length_le`, a theorem declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#init-list-stk-length-le).

## Symbol translation between composed machines

Let $h_1$ be a polynomial-time TM2
computation of $f : \alpha \to \beta$ and $h_2$ one of $g : \beta \to \gamma$, where $\beta$ is
encoded by lists over an alphabet $\Gamma_\beta$. A symbol $y$ of the output-stack alphabet of
$h_1$'s machine is sent to the symbol of the input-stack alphabet of $h_2$'s machine that
corresponds, under $h_2$'s input alphabet bijection with $\Gamma_\beta$, to the letter that $y$
corresponds to under $h_1$'s output alphabet bijection with $\Gamma_\beta$.

Formalized by `MetaMathlibExt.TM2Composition.glue`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#glue).

## Intermediate length bound of the composite machine

Let $h_1$ be a polynomial-time TM2
computation of $f : \alpha \to \beta$ with polynomial time bound $p_1 \in \mathbb{N}[X]$, and let
$c$ be the push bound of the machine of $h_1$. This is the polynomial
$X + c\,p_1 \in \mathbb{N}[X]$.

Evaluated at the length $n$ of an input, its value $n + c\,p_1(n)$ bounds the length of the
intermediate string that the machine of $h_1$ writes for the composite machine.

Formalized by `MetaMathlibExt.TM2Composition.midPoly`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 527](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L527). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#mid-poly).

## Time bound of the composite machine

Let $p_1, p_2 \in \mathbb{N}[X]$ be the polynomial time
bounds of a machine $M_1$ computing $f$ and a machine $M_2$ computing $g$, and let $c$ be the sum,
over the labels of $M_1$, of the number of push instructions in the statement at that label. The
composite time bound is the polynomial $p_1 + 4(X + c\,p_1) + 2 + p_2 \circ (X + c\,p_1)$.

The two copy loops take $2m + 1$ steps each on an intermediate string of length
$m \le n + c\,p_1(n)$, where $n$ is the input length.

Formalized by `MetaMathlibExt.TM2Composition.compTime`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 532](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L532). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#comp-time).

## The composite machine computes the composite function in time

Let $M_1$ compute
$f : \alpha \to \beta$ in polynomial time from the encoding $e_\alpha$ to $e_\beta$, and let $M_2$
compute $g : \beta \to \gamma$ in polynomial time from $e_\beta$ to $e_\gamma$. For every
$a \in \alpha$, let $n$ be the length of $e_\alpha(a)$ and $T$ the composite time bound. Started on
$e_\alpha(a)$, written in the input alphabet of $M_1$, the composite machine of $M_1$ and $M_2$
(with the glue map from output symbols of $M_1$ to input symbols of $M_2$) reaches within
$T(n)$ steps the halted configuration whose output stack holds $e_\gamma(g(f(a)))$, written in the
output alphabet of $M_2$, whose other stacks are empty and whose internal state is the initial
one.

Formalized by `MetaMathlibExt.TM2Composition.compOutputs`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 537](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L537). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#comp-outputs).

## The composite polynomial-time TM2 computation

Let $h_1$ be a polynomial-time TM2
computation of $f : \alpha \to \beta$ with respect to encodings $e_\alpha$ and $e_\beta$, and
let $h_2$ be one of $g : \beta \to \gamma$ with respect to $e_\beta$ and $e_\gamma$. This is the
polynomial-time TM2 computation of $g \circ f$ with respect to $e_\alpha$ and $e_\gamma$ whose
machine is the composite machine of the machines of $h_1$ and $h_2$ with the glue map between
them, whose input alphabet bijection is that of $h_1$, whose output alphabet bijection is that of
$h_2$, and whose time bound is the composite time bound of $h_1$ and $h_2$.

It witnesses that polynomial-time TM2 computability is closed under composition.

Formalized by `MetaMathlibExt.TM2Composition.compComputable`, a definition declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 615](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L615). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#comp-computable).

## Polynomial-time TM2-computable functions are closed under composition

Let $\alpha$,
$\beta$, $\gamma$ be types encoded as lists over alphabets by $e_\alpha$, $e_\beta$, $e_\gamma$.
If $f : \alpha \to \beta$ is computable in polynomial time by a multi-stack Turing machine (a
TM2 machine) with respect to $e_\alpha$ and $e_\beta$, and $g : \beta \to \gamma$ is computable
in polynomial time by a TM2 machine with respect to $e_\beta$ and $e_\gamma$, then there is a TM2
machine computing $g \circ f$ in polynomial time with respect to $e_\alpha$ and $e_\gamma$.

## Sources

- Mathlib PR #44441 states the same result as `TM2ComputableInPolyTime.comp`.

Formalized by `MetaMathlibExt.tm2ComputableInPolyTime_comp`, a theorem declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 633](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L633). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#tm2-computable-in-poly-time-comp).

## Composition of polynomial-time functions under encodings

Let $e_\alpha$, $e_\beta$,
$e_\gamma$ be encodings of types $\alpha$, $\beta$, $\gamma$ as lists over alphabets
$\Gamma_\alpha$, $\Gamma_\beta$, $\Gamma_\gamma$. If $f : \alpha \to \beta$ is polynomial-time
computable with respect to $e_\alpha$ and $e_\beta$, and $g : \beta \to \gamma$ is polynomial-time
computable with respect to $e_\beta$ and $e_\gamma$, then $g \circ f$ is polynomial-time
computable with respect to $e_\alpha$ and $e_\gamma$.

Formalized by `MetaMathlibExt.ComplexityTheory.IsPolyTimeWithEncoding.comp`, a theorem declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 644](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L644). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#comp).

## Polynomial-time functions are closed under composition

Let $\alpha$, $\beta$, $\gamma$ be
types with canonical bitstring encodings. If $f : \alpha \to \beta$ and $g : \beta \to \gamma$ are
polynomial-time computable, then so is $g \circ f$.

Formalized by `MetaMathlibExt.ComplexityTheory.IsPolyTime.comp`, a theorem declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 653](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L653). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#comp-2).

## P is closed under polynomial-time preimages

Let $L$ be a decision problem on bitstrings and
let $f$ be a polynomial-time computable function from bitstrings to bitstrings. If $L$ is in P,
then $L \circ f$ is in P. In particular P is closed under polynomial-time many-one reductions.

Formalized by `MetaMathlibExt.ComplexityTheory.comp_mem_P`, a theorem declared in [MathlibExt/Computability/TuringMachine/Composition.lean, line 660](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Composition.lean#L660). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html#comp-mem-p).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Composition of multi-stack machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/turing-machines/multi-tape-and-multi-stack/composition-of-multi-stack-machines)
