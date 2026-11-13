---
declaration: section
origin: cited
lean: Cslib.IMP.Heap, Cslib.IMP.Heap.Disjoint, Cslib.IMP.Heap.Disjoint.symm, Cslib.IMP.Heap.disjoint_empty_left, Cslib.IMP.Heap.disjoint_empty_right, Cslib.IMP.Heap.erase_union_of_notMem, Cslib.IMP.Heap.disjoint_insert_left, Cslib.IMP.Heap.disjoint_erase_left
statement: formalized
proof: formalized
---

# Heap semantics of IMP

30 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html).

## Heap

A heap is a finite partial map from addresses to values, where addresses and values
are natural numbers: it stores a value $v \in \mathbb{N}$ at each address of a finite set of
addresses in $\mathbb{N}$, called the addresses allocated in the heap.

Formalized by `Cslib.IMP.Heap`, an abbreviation declared in [CSLibExt/Languages/IMP/Heap.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/Heap.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#heap).

## Disjoint heaps

Two heaps $h_1$ and $h_2$ are disjoint when no address is allocated in
both: every address allocated in $h_1$ is not allocated in $h_2$.

Formalized by `Cslib.IMP.Heap.Disjoint`, a definition declared in [CSLibExt/Languages/IMP/Heap.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/Heap.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#disjoint).

## Symmetry of heap disjointness

For heaps $h_1$ and $h_2$, if $h_1$ and $h_2$ are
disjoint, then $h_2$ and $h_1$ are disjoint.

Formalized by `Cslib.IMP.Heap.Disjoint.symm`, a theorem declared in [CSLibExt/Languages/IMP/Heap.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/Heap.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#symm).

## The empty heap is disjoint from every heap

For every heap $h$, the empty heap is
disjoint from $h$ (with the empty heap as the first heap).

Formalized by `Cslib.IMP.Heap.disjoint_empty_left`, a theorem declared in [CSLibExt/Languages/IMP/Heap.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/Heap.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#disjoint-empty-left).

## Every heap is disjoint from the empty heap

For every heap $h$, $h$ is disjoint from
the empty heap (with the empty heap as the second heap).

Formalized by `Cslib.IMP.Heap.disjoint_empty_right`, a theorem declared in [CSLibExt/Languages/IMP/Heap.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/Heap.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#disjoint-empty-right).

## Erasing an address that the right heap of a union lacks

For heaps $h_1$ and $h_2$, let
$h_1 \cup h_2$ be their left-biased union (at an address allocated in both it keeps the value from
$h_1$). If the address $a$ is not allocated in $h_2$, then erasing $a$ from $h_1 \cup h_2$ gives
the union of $h_2$ with the heap obtained from $h_1$ by erasing $a$, taken with that heap on the
left.

Formalized by `Cslib.IMP.Heap.erase_union_of_notMem`, a theorem declared in [CSLibExt/Languages/IMP/Heap.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/Heap.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#erase-union-of-not-mem).

## Inserting an address the other heap lacks preserves disjointness

If heaps $h_1$ and
$h_2$ are disjoint and the address $a$ is not allocated in $h_2$, then for every value $v$, the
heap obtained from $h_1$ by inserting $a$ with value $v$ (overwriting any value $h_1$ stores at
$a$) is disjoint from $h_2$.

Formalized by `Cslib.IMP.Heap.disjoint_insert_left`, a theorem declared in [CSLibExt/Languages/IMP/Heap.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/Heap.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#disjoint-insert-left).

## Erasing an address preserves disjointness

If heaps $h_1$ and $h_2$ are disjoint, then
for every address $a$, the heap obtained from $h_1$ by erasing $a$ (removing the address $a$
and its value) is disjoint from $h_2$.

Formalized by `Cslib.IMP.Heap.disjoint_erase_left`, a theorem declared in [CSLibExt/Languages/IMP/Heap.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/Heap.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#disjoint-erase-left).

## Disjointness from a singleton heap

For every address $a$, value $v$ and heap $h$, the
singleton heap that stores $v$ at $a$ and allocates no other address is disjoint from $h$ if and
only if $a$ is not allocated in $h$.

Formalized by `Cslib.IMP.Heap.disjoint_singleton_left`, a theorem declared in [CSLibExt/Languages/IMP/Heap.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/Heap.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#disjoint-singleton-left).

## Reinserting an erased value restores the heap

If a heap $h$ stores the value $v$ at the
address $a$, then erasing $a$ from $h$ and then inserting $a$ with value $v$ gives back $h$.

Formalized by `Cslib.IMP.Heap.insert_erase_eq_self`, a theorem declared in [CSLibExt/Languages/IMP/Heap.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/Heap.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#insert-erase-eq-self).

## Every heap has a free address

For every heap $h$ there is an address that is not
allocated in $h$.

Formalized by `Cslib.IMP.Heap.exists_notMem`, a theorem declared in [CSLibExt/Languages/IMP/Heap.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/Heap.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#exists-not-mem).

## Heap commands

Heap commands extend the commands of IMP with heap operations. A heap
command is one of: $\mathbf{skip}$; an assignment $x := a$; a sequence $c_1; c_2$; a
conditional $\mathbf{if}\ b\ \mathbf{then}\ c_1\ \mathbf{else}\ c_2$; a loop
$\mathbf{while}\ b\ \mathbf{do}\ c$; a heap read $x := [a]$; a heap write $[a] := e$; an
allocation $x := \mathbf{alloc}(e)$; or a deallocation $\mathbf{free}(a)$. Here $x$ is a variable
(a natural number), $a$ and $e$ are arithmetic expressions, $b$ is a Boolean expression, and $c$,
$c_1$, $c_2$ are heap commands.

Formalized by `Cslib.IMP.HeapCmd`, an inductive type declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#heap-cmd).

## Heap configurations

A heap configuration is a triple $(c, s, h)$ of a heap command $c$,
a store $s$ and a heap $h$.

Formalized by `Cslib.IMP.HConfig`, an abbreviation declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#hconfig).

## Small-step semantics of heap commands

The single-step relation
$(c, s, h) \to (c', s', h')$ on heap configurations is the least relation closed under the rules
below. Here $a(s)$ is the value of an expression $a$ in the store $s$, $s[x \mapsto n]$ is $s$
with variable $x$ set to $n$, $h[\ell \mapsto n]$ is $h$ with address $\ell$ set to $n$, and
$h \setminus \ell$ is $h$ with address $\ell$ removed.

- Assignment: $(x := a, s, h) \to (\mathbf{skip}, s[x \mapsto a(s)], h)$.
- Sequence: $(\mathbf{skip}; c_2, s, h) \to (c_2, s, h)$, and if
  $(c_1, s, h) \to (c_1', s', h')$ then $(c_1; c_2, s, h) \to (c_1'; c_2, s', h')$.
- Conditional: $(\mathbf{if}\ b\ \mathbf{then}\ c_1\ \mathbf{else}\ c_2, s, h)$ steps to
  $(c_1, s, h)$ if $b(s)$ is true and to $(c_2, s, h)$ if $b(s)$ is false.
- Loop: $(\mathbf{while}\ b\ \mathbf{do}\ c, s, h)$ steps to
  $(\mathbf{if}\ b\ \mathbf{then}\ d\ \mathbf{else}\ \mathbf{skip}, s, h)$, where $d$ is the
  sequence $c; \mathbf{while}\ b\ \mathbf{do}\ c$.
- Read: if $h$ maps the address $a(s)$ to $v$, then
  $(x := [a], s, h) \to (\mathbf{skip}, s[x \mapsto v], h)$.
- Write: if $a(s)$ is allocated in $h$, then
  $([a] := e, s, h) \to (\mathbf{skip}, s, h[a(s) \mapsto e(s)])$.
- Allocation: for every address $\ell$ not allocated in $h$,
  $(x := \mathbf{alloc}(e), s, h) \to (\mathbf{skip}, s[x \mapsto \ell], h[\ell \mapsto e(s)])$.
- Deallocation: if $a(s)$ is allocated in $h$, then
  $(\mathbf{free}(a), s, h) \to (\mathbf{skip}, s, h \setminus a(s))$.

Formalized by `Cslib.IMP.HStep`, an inductive type declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#hstep).

## Multi-step heap execution

The relation $(c, s, h) \to^* (c', s', h')$ on heap
configurations is the reflexive-transitive closure of the small-step relation: it holds when the
first configuration reaches the second by a finite, possibly empty, sequence of small steps.

Formalized by `Cslib.IMP.HSteps`, an abbreviation declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#hsteps).

## Safe heap configurations

A heap configuration, consisting of a heap command, a store and
a heap, is safe when every heap configuration reachable from it in zero or more heap steps
either has command $\mathtt{skip}$ or can take a further heap step.

Formalized by `Cslib.IMP.Safe`, a definition declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#safe).

## Safety is preserved along executions

If a heap configuration is safe and reaches a second
configuration by finitely many (possibly zero) small steps, then the second configuration is
safe.

Formalized by `Cslib.IMP.Safe.of_steps`, a theorem declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#of-steps).

## Adding a frame heap preserves the ability to step

Let $h$ and $h_f$ be disjoint heaps,
$c$ a heap command and $s$ a store. If the configuration $(c, s, h)$ can take a small step, then
so can $(c, s, h \cup h_f)$.

Allocation may choose a different fresh address on the larger heap.

Formalized by `Cslib.IMP.HStep.exists_step_frame`, a theorem declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#exists-step-frame).

## Frame decomposition of a single heap step

Let $h$ and $h_f$ be disjoint heaps, $c$ a heap
command and $s$ a store, and suppose that the configuration $(c, s, h)$ can take a small step. If
$(c, s, h \cup h_f)$ takes a small step to $(c', s', h'')$, then there is a heap $h_1$, disjoint
from $h_f$, such that $(c, s, h)$ takes a small step to $(c', s', h_1)$ and $h'' = h_1 \cup h_f$.

The step-existence hypothesis forces any address the step touches to lie in $h$.

Formalized by `Cslib.IMP.HStep.decompose_of_safe_step`, a theorem declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#decompose-of-safe-step).

## Frame decomposition of heap executions

Let $h$ and $h_f$ be disjoint heaps, $c$ a heap
command and $s$ a store, and suppose that the configuration $(c, s, h)$ is safe. If
$(c, s, h \cup h_f)$ reaches $(c'', s'', h'')$ by finitely many (possibly zero) small steps, then
there is a heap $h_2$, disjoint from $h_f$, such that $(c, s, h)$ reaches $(c'', s'', h_2)$ by
finitely many small steps, $h'' = h_2 \cup h_f$, and $(c'', s'', h_2)$ is safe.

Safety supplies the step-existence that single-step decomposition needs at each stage.

Formalized by `Cslib.IMP.HSteps.decompose_of_safe`, a theorem declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#decompose-of-safe).

## Embedding of IMP into the heap language

The embedding sends each plain IMP command to
the heap command of the same shape: $\mathtt{skip}$ goes to $\mathtt{skip}$, an assignment of an
arithmetic expression to a variable goes to the same assignment, a sequence goes to the
sequence of the embeddings of its parts, and a conditional or while loop goes to the conditional
or while loop with the same guard and with each subcommand replaced by its embedding.

Formalized by `Cslib.IMP.Cmd.toHeap`, a definition declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#to-heap).

## Heap steps of embedded commands are plain steps

Let $c$ be a plain IMP command, $s$ a
store and $h$ a heap, and write $\overline{d}$ for the embedding of a plain command $d$ into the
heap language. Then $(\overline{c}, s, h)$ takes a heap step to a heap configuration $K$ if and
only if there are a plain command $c'$ and a store $s'$ such that $(c, s)$ takes a plain small
step to $(c', s')$ and $K = (\overline{c'}, s', h)$.

Formalized by `Cslib.IMP.HStep.toHeap_iff`, a theorem declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#to-heap-iff).

## Executions of embedded commands are plain executions

Let $c$ be a plain IMP command,
$s$ a store and $h$ a heap, and write $\overline{d}$ for the embedding of a plain command $d$
into the heap language. If $(\overline{c}, s, h)$ reaches a heap configuration $(c_2, s_2, h_2)$
in zero or more heap steps, then $h_2 = h$ and there is a plain command $c_2'$ with
$c_2 = \overline{c_2'}$ such that $(c, s)$ reaches $(c_2', s_2)$ in zero or more plain small
steps.

Formalized by `Cslib.IMP.HSteps.of_toHeap`, a theorem declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 506](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L506). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#of-to-heap).

## Plain executions lift to the heap language

Let $c, c_2$ be plain IMP commands, $s, s_2$
stores and $h$ a heap, and write $\overline{d}$ for the embedding of a plain command $d$ into the
heap language. If $(c, s)$ reaches $(c_2, s_2)$ in zero or more plain small steps, then
$(\overline{c}, s, h)$ reaches $(\overline{c_2}, s_2, h)$ in zero or more heap steps.

Formalized by `Cslib.IMP.HSteps.toHeap_of_steps`, a theorem declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 528](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L528). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#to-heap-of-steps).

## Embedded plain commands are safe

For every plain IMP command $c$ with embedding
$\overline{c}$ into the heap language, every store $s$ and every heap $h$, the heap
configuration $(\overline{c}, s, h)$ is safe.

This holds because plain IMP never gets stuck except at $\mathtt{skip}$.

Formalized by `Cslib.IMP.safe_toHeap`, a theorem declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#safe-to-heap).

## Embedding preserves termination

Let $c$ be a plain IMP command with embedding
$\overline{c}$ into the heap language, let $s, s'$ be stores and let $h$ be a heap. Then $c$
terminates from $s$ with final store $s'$ if and only if $(\overline{c}, s, h)$ reaches
$(\mathtt{skip}, s', h)$ in zero or more heap steps.

Formalized by `Cslib.IMP.terminates_toHeap`, a theorem declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 558](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L558). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#terminates-to-heap).

## Modified variables of a heap command

The set $\mathrm{mod}(c)$ of variables a heap command
$c$ may assign to is defined by recursion on $c$. It is empty for $\mathbf{skip}$, a heap write
$[a] := e$ and a deallocation $\mathbf{free}(a)$; it is $\{x\}$ for an assignment $x := a$, a heap
read $x := [a]$ and an allocation $x := \mathbf{alloc}(e)$; it is $\mathrm{mod}(c_1) \cup
\mathrm{mod}(c_2)$ for a sequence $c_1; c_2$ and for a conditional
$\mathbf{if}\ b\ \mathbf{then}\ c_1\ \mathbf{else}\ c_2$; and it is $\mathrm{mod}(c_0)$ for a loop
$\mathbf{while}\ b\ \mathbf{do}\ c_0$.

Formalized by `Cslib.IMP.HeapCmd.modVars`, a definition declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 573](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L573). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#mod-vars).

## Steps do not enlarge the modified variables

Write $\mathrm{mod}(c)$ for the set of
variables a heap command $c$ may assign to. If the configuration $(c, s, h)$ takes a small step to
$(c', s', h')$, then $\mathrm{mod}(c') \subseteq \mathrm{mod}(c)$.

Formalized by `Cslib.IMP.HStep.modVars_subset`, a theorem declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 590](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L590). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#mod-vars-subset).

## A heap step only changes assignable variables

If a heap configuration $(c, s, h)$ takes
one heap step to $(c', s', h')$, then $s'(x) = s(x)$ for every variable $x$ outside the set of
variables that $c$ may assign to.

Formalized by `Cslib.IMP.HStep.store_agree`, a theorem declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 615](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L615). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#store-agree).

## Heap executions only change assignable variables

If a heap configuration $(c, s, h)$
reaches a heap configuration $(c', s', h')$ in zero or more heap steps, then $s'(x) = s(x)$ for
every variable $x$ outside the set of variables that $c$ may assign to.

Formalized by `Cslib.IMP.HSteps.store_agree`, a theorem declared in [CSLibExt/Languages/IMP/HeapStep.lean, line 655](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/HeapStep.lean#L655). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html#store-agree-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Heap semantics of IMP](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/programming-language-semantics/heap-semantics-of-imp)
