---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Stack.push, Cslib.Algorithms.Lean.Stack.pop, Cslib.Algorithms.Lean.Stack.top, Cslib.Algorithms.Lean.Stack.pop_eq, Cslib.Algorithms.Lean.Stack.top_eq, Cslib.Algorithms.Lean.Stack.operations_spec, Cslib.Algorithms.Lean.Stack.multipop, Cslib.Algorithms.Lean.Stack.multipop_ret
statement: formalized
proof: formalized
---

# Stack with multipop

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html).

## Stack push

Stacks over a type $\alpha$ are lists of elements of $\alpha$, with the first
element as the top. Pushing $v \in \alpha$ onto a stack $s$ returns the stack with top $v$
followed by the elements of $s$, at cost $1$ (one successful push event).

Formalized by `Cslib.Algorithms.Lean.Stack.push`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Basic.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Basic.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#push).

## Stack pop

Stacks over a type $\alpha$ are lists of elements of $\alpha$, with the first
element as the top. Popping the empty stack returns underflow (no value) at cost $0$. Popping a
stack with top $v$ and remaining stack $t$ returns the pair $(v, t)$ at cost $1$ (one successful
pop event).

Formalized by `Cslib.Algorithms.Lean.Stack.pop`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Basic.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Basic.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#pop).

## Stack top

Stacks over a type $\alpha$ are lists of elements of $\alpha$, with the first
element as the top. Reading the top of the empty stack returns underflow (no value) at cost $0$.
Reading the top of a stack with top $v$ returns $v$ at cost $1$ (one successful top event); the
stack itself is not returned or changed.

Formalized by `Cslib.Algorithms.Lean.Stack.top`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Basic.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Basic.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#top).

## Result and cost of stack pop

Let $s$ be a stack over a type $\alpha$ (a list of elements
of $\alpha$ whose first element is the top). If $s$ is empty, popping $s$ returns underflow (no
value) at cost $0$. If $s$ has top $h$ and remaining stack $t$, popping $s$ returns the pair
$(h, t)$ at cost $1$.

This holds for every type $\alpha$; no element of $\alpha$ is assumed to exist.

Formalized by `Cslib.Algorithms.Lean.Stack.pop_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Basic.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Basic.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#pop-eq).

## Result and cost of reading the stack top

Let $s$ be a stack over a type $\alpha$ (a list
of elements of $\alpha$ whose first element is the top). If $s$ is empty, reading the top of $s$
returns underflow (no value) at cost $0$. If $s$ has top $h$, reading the top of $s$ returns $h$
at cost $1$.

This holds for every type $\alpha$; no element of $\alpha$ is assumed to exist.

Formalized by `Cslib.Algorithms.Lean.Stack.top_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Basic.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Basic.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#top-eq).

## Result and cost of the stack operations

Let $\alpha$ be a type, let $s$ be a stack over
$\alpha$ (a list of elements of $\alpha$ whose first element is the top) and let $v \in \alpha$.
Pushing $v$ onto $s$ returns the stack with top $v$ followed by the elements of $s$, at cost $1$.
Popping $s$ returns underflow (no value) at cost $0$ if $s$ is empty, and returns the pair
$(h, t)$ at cost $1$ if $s$ has top $h$ and remaining stack $t$. Reading the top of $s$ returns
underflow (no value) at cost $0$ if $s$ is empty, and returns $h$ at cost $1$ if $s$ has top $h$.

Formalized by `Cslib.Algorithms.Lean.Stack.operations_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Basic.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Basic.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#operations-spec).

## MULTIPOP

For a stack $S$, stored as a list with its top first, and a natural number $k$,
MULTIPOP of $S$ with count $k$ repeatedly removes the top element while the stack is nonempty and
fewer than $k$ elements have been removed, and returns the remaining stack. Each removed element
costs one unit, and nothing else is charged.

This is MULTIPOP from CLRS, fourth edition, Section 16.1.

Formalized by `Cslib.Algorithms.Lean.Stack.multipop`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#multipop).

## Result of MULTIPOP

For every stack $S$, stored as a list with its top first, and every
natural number $k$, the stack returned by MULTIPOP of $S$ with count $k$ is $S$ with its top $k$
elements removed, or the empty stack if $S$ has fewer than $k$ elements.

Formalized by `Cslib.Algorithms.Lean.Stack.multipop_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#multipop-ret).

## Cost of MULTIPOP

For every stack $S$ and every natural number $k$, the cost of MULTIPOP
of $S$ with count $k$ is $\min(|S|, k)$, where $|S|$ is the number of elements of $S$.

Formalized by `Cslib.Algorithms.Lean.Stack.multipop_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#multipop-time).

## MULTIPOP with an integer count

For a stack $S$ and an integer $k$, MULTIPOP with integer
count $k$ is MULTIPOP of $S$ with the natural count $\max(k, 0)$, with the same result and cost.
In particular, a count $k \le 0$ removes nothing.

Formalized by `Cslib.Algorithms.Lean.Stack.multipopSigned`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#multipop-signed).

## MULTIPOP with a nonpositive count does nothing

For every stack $S$ and every integer
$k \le 0$, MULTIPOP with integer count $k$ applied to $S$ returns $S$ at cost $0$.

Formalized by `Cslib.Algorithms.Lean.Stack.multipopSigned_of_nonpos`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#multipop-signed-of-nonpos).

## Stack operations for the MULTIPOP aggregate analysis

For a type $\alpha$ of stack
entries, a stack operation is one of the following: $\mathrm{PUSH}(x)$ for an element
$x \in \alpha$, $\mathrm{POP}$, or $\mathrm{MULTIPOP}(k)$ for an integer count $k$.

These are the operations whose sequences CLRS analyse in Section 16.1.

Formalized by `Cslib.Algorithms.Lean.Stack.Operation`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#operation).

## Running a sequence of stack operations

Given a stack $S$ and a finite sequence of
operations, each a PUSH of a value, a POP or a MULTIPOP with an integer count, the operations are
applied to $S$ in order. PUSH of $x$ puts $x$ on top at cost $1$; POP removes the top element at
cost $1$; MULTIPOP with count $k$ is MULTIPOP with an integer count, costing one unit per element
removed. If a POP meets an empty stack, the run stops and reports an error, that POP is not
charged, and the cost is that of the operations before it. Otherwise the run returns the final
stack, and its cost is the sum of the costs of all operations.

Formalized by `Cslib.Algorithms.Lean.Stack.execute`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#execute).

## Running a PUSH agrees with the standalone PUSH

For every stack $S$, every value $x$ and
every finite sequence $\sigma$ of stack operations, running PUSH $x$ followed by $\sigma$ on $S$
has the same result and cost as first performing the standalone PUSH of $x$ on $S$ and then
running $\sigma$ on the resulting stack, the two costs being added.

Formalized by `Cslib.Algorithms.Lean.Stack.execute_push_eq_bind_push`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#execute-push-eq-bind-push).

## Running a POP agrees with the standalone POP

For every stack $S$ and every finite
sequence $\sigma$ of stack operations, running POP followed by $\sigma$ on $S$ has the same result
and cost as first performing the standalone POP on $S$ and then, if it reports underflow,
stopping with an error at no further cost, or, if it removes the top element and leaves the stack
$S'$, running $\sigma$ on $S'$, the two costs being added.

Formalized by `Cslib.Algorithms.Lean.Stack.execute_pop_eq_bind_pop`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#execute-pop-eq-bind-pop).

## Cost balance for stack operation sequences

For every stack $S$ and every finite sequence
$\sigma$ of stack operations, if running $\sigma$ on $S$ succeeds with final stack $F$, then the
cost of the run plus the number of elements of $F$ equals the number of elements of $S$ plus
twice the number of PUSH operations in $\sigma$.

Formalized by `Cslib.Algorithms.Lean.Stack.execute_balance`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#execute-balance).

## Aggregate cost of stack operation sequences

For every stack $S$ and every sequence of
$n$ stack operations (PUSH, POP and MULTIPOP), if running the sequence on $S$ succeeds, that is,
no POP meets an empty stack, then its cost is at most $|S| + 2n$, where $|S|$ is the number of
elements of $S$.

Formalized by `Cslib.Algorithms.Lean.Stack.execute_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Stack/Multipop.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html#execute-time-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stack with multipop](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/linear-structures/stack-with-multipop)
