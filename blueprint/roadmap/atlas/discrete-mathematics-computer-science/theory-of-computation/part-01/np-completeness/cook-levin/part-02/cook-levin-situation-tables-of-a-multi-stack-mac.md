---
declaration: section
origin: cited
lean: Cslib.Complexity.CookLevin.Situation.readTop, Cslib.Complexity.CookLevin.Situation.eff, Cslib.Complexity.CookLevin.Situation.ops, Cslib.Complexity.CookLevin.Situation.PushSym, Cslib.Complexity.CookLevin.Situation.eff_bound, Cslib.Complexity.CookLevin.Situation.eff_pushed, Cslib.Complexity.CookLevin.Situation.Enc, Cslib.Complexity.CookLevin.Situation.depth
statement: formalized
proof: formalized
---

# Cook-Levin: situation tables of a multi-stack machine and the correctness of the formula

161 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/index.html).

## Top of a stack as read from the windows

Let $W$ assign to each stack $k$ a window, a list
of entries that are symbols of $k$ or the empty cell $\bot$; let $P$ assign to each stack $k$ a
list of symbols of $k$; and let $c$ assign a natural number to each stack. The top of stack $k$ is
the first element of $P(k)$ when $P(k)$ is nonempty. Otherwise it is the entry of $W(k)$ at
position $c(k)$, counting from $0$, or $\bot$ when $W(k)$ has fewer than $c(k) + 1$ entries.

Here $P(k)$ lists the symbols pushed in this step and still on top, and $c(k)$ counts the original
symbols already consumed.

Formalized by `Cslib.Complexity.CookLevin.Situation.readTop`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#read-top).

## Symbolic effect of a statement tree

Let $W$ assign to each stack $k$ a window $W_k$, a
list of cells each holding a symbol or $\bot$. The window top of stack $k$ for pushed lists $P$
and consumption counts $c$ is the head of $P_k$ if $P_k$ is nonempty, and otherwise the entry of
$W_k$ at position $c_k$ (counting from $0$), or $\bot$ if there is none. The effect of a statement
tree $q$ from a state $v$, pushed lists $P$ and consumption counts $c$ is a label (or none), a
state, pushed lists and consumption counts, defined by recursion on $q$: a push onto stack $k$
prepends the symbol computed from $v$ to $P_k$ and continues; a peek on stack $k$ replaces $v$ by
the state computed from $v$ and the window top of $k$ and continues; a pop on stack $k$ does the
same, also removes the head of $P_k$ (if any), and increases $c_k$ by one if $P_k$ was empty;
a load replaces $v$ by the state computed from $v$ and continues; a branch continues with the
subtree selected by $v$; a goto returns the label computed from $v$, and a halt returns no
label, each together with the current $v$, $P$ and $c$.

Thus $P_k$ holds the symbols pushed in this step and still on top, and $c_k$ counts the original
symbols consumed, a push followed by a pop cancelling.

Formalized by `Cslib.Complexity.CookLevin.Situation.eff`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#eff).

## Stack operations on a path of a statement tree

For a statement tree $q$ of a multi-stack
Turing machine, $\operatorname{ops}(q)$ is the largest number of push, peek and pop nodes on a path
from the root of $q$ to a leaf. Load and branch nodes do not count, and goto and halt leaves
contribute $0$.

Formalized by `Cslib.Complexity.CookLevin.Situation.ops`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#ops).

## Symbols a statement tree can push

Let $q$ be a statement tree of a multi-stack Turing
machine with state type $\sigma$, let $k$ be a stack and $x$ a symbol of the alphabet of $k$. Then
$x$ can be pushed onto $k$ by $q$ when $q$ contains a push node onto stack $k$ with symbol
function $f$ and some state $v \in \sigma$ satisfies $x = f(v)$. Every push node of $q$ counts,
whichever branches are taken.

Formalized by `Cslib.Complexity.CookLevin.Situation.PushSym`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#push-sym).

## The symbolic effect grows by at most the number of stack operations

Let $q$ be a statement
tree, let $W$ assign to each stack a window (a list of cells, each a symbol or $\bot$), and let
$n(q)$ be the largest number of push, peek and pop nodes on a root-to-leaf path of $q$. For every
state $v$, pushed lists $P$ and consumption counts $c$, the pushed lists $P'$ and consumption
counts $c'$ of the symbolic effect of $q$ on $W$ from $v$, $P$, $c$ satisfy
$|P'_k| \le |P_k| + n(q)$ and $c'_k \le c_k + n(q)$ for every stack $k$.

Formalized by `Cslib.Complexity.CookLevin.Situation.eff_bound`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#eff-bound).

## Pushed symbols come from the start or from push nodes

Let $q$ be a statement tree, let $W$
assign to each stack a window, and for each stack $k$ let $Q_k$ be a property of symbols of
stack $k$ such that every symbol that some push node of $q$ can push onto stack $k$, for some
state, satisfies $Q_k$. Then for every state $v$, pushed lists $P$ and consumption counts $c$
such that every symbol of $P_k$ satisfies $Q_k$ for every stack $k$, every symbol of the pushed
list on stack $k$ produced by the symbolic effect of $q$ on $W$ from $v$, $P$, $c$ satisfies
$Q_k$, for every stack $k$.

Formalized by `Cslib.Complexity.CookLevin.Situation.eff_pushed`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#eff-pushed).

## Encoding data for a finite TM2 machine

An encoding of a finite TM2 machine $M$ consists
of a number $K$, a map $\kappa$ from the stacks of $M$ to the naturals below $K$ and a map
$\kappa'$ from naturals to stacks with $\kappa'(\kappa(k)) = k$ for every stack $k$ and
$\kappa(\kappa'(n)) = n$ for every $n < K$; a number $A_0$, a map $\lambda$ from pairs (label
or halted, state) to the naturals below $A_0$ and a map $\lambda'$ back with
$\lambda'(\lambda(x)) = x$ for every pair $x$ and $\lambda(\lambda'(a)) = a$ for every
$a < A_0$; and for each stack $k$ a size $s_k$, effective symbols $d_k(i)$ for $i < s_k$, and a
symbol code map $e_k$ on the alphabet of stack $k$ with $e_k(d_k(i)) = i + 1$. It is required
that every symbol that a push node of the statement tree of some label can push onto stack $k$,
for some state, is an effective symbol of stack $k$, and that every symbol of the input stack's
alphabet is an effective symbol of the input stack.

Symbol code $0$ stands for $\bot$, the empty cell.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc`, a structure declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#enc).

## Window depth of a machine

For a finite TM2 machine $M$, the window depth is the maximum,
over all labels $l$ of $M$, of the largest number of push, peek and pop nodes on a root-to-leaf
path of the statement tree of $l$.

Formalized by `Cslib.Complexity.CookLevin.Situation.depth`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#depth).

## The situation step

Let $M$ be a finite multi-stack Turing machine, let $l$ be either a
label of $M$ or $\mathrm{none}$ (the halted label), let $v$ be a state of $M$, and let $W$ assign
to each stack $k$ a window, a list of entries that are symbols of $k$ or the empty cell. If
$l = \mathrm{none}$, the step returns the label $\mathrm{none}$, the state $v$, no pushed symbols on
any stack and no consumed symbols on any stack. If $l$ is a label, the step is the effect, read
from the windows $W$, of the statement tree of $l$ started in state $v$ with nothing pushed and
nothing consumed.

Formalized by `Cslib.Complexity.CookLevin.Situation.sitStep`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#sit-step).

## Symbol-code bound

For an encoding $E$ of a finite TM2 machine $M$, the symbol-code bound
is $g = 1 + \max_k s_k$, where the maximum runs over all stacks $k$ of $M$ and $s_k$ is the size
of the effective alphabet of stack $k$.

Effective symbols of stack $k$ have codes $1, \dots, s_k$, all below $g$; code $0$ is $\bot$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.g`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#g).

## Number of window combinations

For an encoding $E$ of a finite TM2 machine $M$ with $K$
numbered stacks and symbol-code bound $g$, the number of window combinations is $G = g^{K d}$,
where $d$ is the window depth of $M$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.G`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#g-2).

## Number of situations

For an encoding $E$ of a finite multi-stack Turing machine $M$, the
number of situations is $N = A_0 \cdot G$, where $A_0$ is the number of (label, state) codes of
$E$ and $G$ is the number of window combinations.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.N`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#n).

## Clause layout of a machine encoding

For an encoding $E$ of a finite TM2 machine $M$, the
layout of the transition clauses has label/state block size $A = A_0 + N$, where $A_0$ is the
number of label/state codes and $N = A_0 G$ is the number of situations ($G$ the number of
window combinations), together with the number $K$ of numbered stacks, the symbol-code bound $g$
and the window depth $d$ of $M$. The block is a one-hot part on $[0, A_0)$ followed by one
variable per situation.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.layout`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#layout).

## Label/state code of a situation

For an encoding $E$ of a finite TM2 machine with $A_0$
label/state codes and $G$ window combinations, the label/state code of a situation
$i \in \mathbb{N}$ is $\lfloor i / G \rfloor \bmod A_0$, the top digit of $i$ in the mixed radix
whose lower digits are the window symbol codes.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.la`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#la).

## Window symbol code of a situation

Let $E$ be an encoding of a finite multi-stack Turing
machine $M$, let $s_\kappa$ be the size of the effective alphabet of stack $\kappa$ in $E$, let
$g = 1 + \max_\kappa s_\kappa$ (so the empty-cell code $0$ and every effective symbol code are
below $g$), and let $d$ be the window depth of $M$. For natural numbers $i$, $k$ and $j$, the
window symbol code of situation $i$ on stack number $k$ at depth $j$ is the base-$g$ digit of $i$
at position $kd + j$, namely $\lfloor i / g^{kd + j} \rfloor \bmod g$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.wa`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#wa).

## Position of a situation's variable

For an encoding $E$ of a finite multi-stack Turing
machine $M$ with $A_0$ (label, state) codes and a natural number $i$, the variable of situation
$i$ sits at position $A_0 + i$ of the label/state block of a row.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sa`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#sa).

## Decoding a symbol code

For an encoding $E$ of a finite TM2 machine $M$, a stack $k$
and a natural number $c$, the decoded symbol is the effective symbol of stack $k$ with index
$c - 1$ when $1 \le c$ and $c - 1 < s_k$, where $s_k$ is the size of the effective alphabet of
stack $k$; otherwise, in particular for $c = 0$, it is $\bot$ (no symbol).

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.decO`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#dec-o).

## Decoded windows of a situation

Let $E$ be an encoding of a finite multi-stack Turing
machine $M$ with window depth $d$, and let $i$ be a natural number. The window of situation $i$ on
stack $k$ is the list of length $d$ whose entry at position $j < d$ decodes the window symbol code
$c$ of situation $i$ on the stack number of $k$ at depth $j$. A code with $1 \le c \le s_k$, where
$s_k$ is the size of the effective alphabet of $k$, decodes to the effective symbol of $k$ with
index $c - 1$; every other code decodes to the empty cell $\bot$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.win`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#win).

## Effect of a situation

Let $E$ be an encoding of a finite multi-stack Turing machine $M$
and $i$ a natural number. Let $(l, v)$, an optional label and a state, be the result of decoding
the label/state code of situation $i$ with the inverse (label, state) numbering of $E$, and let
$W$ be the decoded windows of situation $i$. The effect of situation $i$ is the situation step of
$M$ from $l$, $v$ and $W$: a new optional label, a new state, the symbols left pushed on each
stack, and the number of original symbols consumed from each stack.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.res`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#res).

## Next label/state code of a situation

For an encoding $E$ of a finite multi-stack Turing
machine $M$ and a natural number $i$, the next label/state code of situation $i$ is the code, in
the (label, state) numbering of $E$, of the pair formed by the label and the state that the effect
of situation $i$ produces.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.na`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-01/index.html#na).

## Push-count table of a situation

Fix an encoding record $E$ of a finite multi-stack
machine. For a situation $i$ and a stack number $k$, $\mathrm{pl}(i, k)$ is the number of symbols
that the effect of situation $i$ has pushed onto the stack that the inverse stack numbering of $E$
assigns to $k$ and that are still on top of that stack at the end of the step.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.pl`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#pl).

## Consumption table of a situation

Fix an encoding record $E$ of a finite multi-stack
machine. For a situation $i$ and a stack number $k$, $\mathrm{cn}(i, k)$ is the number of original
symbols that the effect of situation $i$ consumes from the stack that the inverse stack numbering
of $E$ assigns to $k$; a symbol pushed and then popped within the same step is not counted.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.cn`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#cn).

## Pushed-symbol table of a situation

Fix an encoding record $E$ of a finite multi-stack
machine. For a situation $i$, a stack number $k$ and a depth $j$, $\mathrm{pu}(i, k, j)$ is the
code of the symbol at position $j$ from the top (counting from $0$) among the symbols that the
effect of situation $i$ leaves pushed on the stack that the inverse stack numbering of $E$ assigns
to $k$, and $0$ if fewer than $j + 1$ symbols are left pushed there.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.pu`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#pu).

## The symbol-code bound is positive

For an encoding $E$ of a finite TM2 machine, the
symbol-code bound $g$ of $E$ satisfies $0 < g$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.g_pos`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#g-pos).

## Symbols left pushed by a situation are effective

Let $E$ be an encoding of a finite
multi-stack Turing machine $M$, and for each stack $k$ of $M$ let $s_k$ be the size of the
effective alphabet of stack $k$ in $E$ and $\mathrm{dec}_k(n)$, for $n < s_k$, its $n$-th
effective symbol. For every $i \in \mathbb{N}$, every stack $k$ of $M$ and every symbol $x$ of the
alphabet of stack $k$: if $x$ is among the symbols that the effect of situation $i$ leaves pushed
on stack $k$, then $x = \mathrm{dec}_k(n)$ for some $n < s_k$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.res_pushed`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#res-pushed).

## Pushed codes are valid symbol codes

Fix an encoding record $E$ of a finite multi-stack
machine. Let $i$ be a situation, $k$ a stack number, $s$ the stack that the inverse stack numbering
of $E$ assigns to $k$, $n_s$ the size of the effective alphabet of $s$, and $j < \mathrm{pl}(i, k)$.
Then there is a symbol $x$ at position $j$ from the top (counting from $0$) among the symbols the
effect of situation $i$ leaves pushed on $s$, such that $\mathrm{pu}(i, k, j)$ is the code of $x$,
$1 \le \mathrm{pu}(i, k, j) \le n_s$, and decoding $\mathrm{pu}(i, k, j)$ on stack $s$ gives $x$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.pu_valid`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#pu-valid).

## The transition tables of a machine are well formed

Let $M$ be a finite multi-stack
Turing machine with window depth $d$, let $E$ be an encoding of $M$ with $A_0$ label/state codes,
$K$ stacks, $g$ symbol codes and $N$ situations, and let $H \ge d$. For every $i \in \mathbb{N}$,
the current-code table $\mathrm{la}$, the next-code table $\mathrm{na}$ and the window table
$\mathrm{wa}$ of $E$ are well formed for the transition clauses of the layout of $E$ at situation
$i$ and height $H$: that is, $\mathrm{la}(i) < A_0 + N$, $\mathrm{na}(i) < A_0 + N$,
$\mathrm{wa}(i, k, j) < g$ for all $k < K$ and $j < d$, and $d \le H$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.wf_upd`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#wf-upd).

## The situation-definition tables of a machine are well formed

Let $M$ be a finite
multi-stack Turing machine with window depth $d$, let $E$ be an encoding of $M$ with $A_0$
label/state codes, $K$ stacks, $g$ symbol codes and $N$ situations, and let $H \ge d$. For every
situation $i < N$, the current-code table $\mathrm{la}$ of $E$, the table
$\mathrm{sa}(i) = A_0 + i$ as next-code table and the window table $\mathrm{wa}$ of $E$ are well
formed for the transition clauses of the layout of $E$ at situation $i$ and height $H$: that is,
$\mathrm{la}(i) < A_0 + N$, $\mathrm{sa}(i) < A_0 + N$, $\mathrm{wa}(i, k, j) < g$ for all
$k < K$ and $j < d$, and $d \le H$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.wf_sdef`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#wf-sdef).

## The cell-shift tables of a machine are well formed

Let $M$ be a finite multi-stack Turing
machine with window depth $d$, let $E$ be an encoding of $M$ with $A_0$ label/state codes, $K$
stacks, $g$ symbol codes and $N$ situations, and let $H \ge d$. Then the table
$\mathrm{sa}(i) = A_0 + i$, the push counts $\mathrm{pl}$, the consumption counts $\mathrm{cn}$
and the pushed codes $\mathrm{pu}$ of $E$ are well formed for the cell-shift clauses of the layout
of $E$ with $N$ situations at height $H$: that is, $0 < g$, $d \le H$,
$\mathrm{sa}(i) < A_0 + N$ for all $i < N$, and for all $i < N$ and $k < K$ we have
$\mathrm{pl}(i, k) \le d$, $\mathrm{cn}(i, k) \le d$ and $\mathrm{pu}(i, k, j) < g$ for all
$j < \mathrm{pl}(i, k)$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.wf_sh`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#wf-sh).

## Halted situations stay fixed

If the (label, state) pair decoded from the code
$\mathrm{la}(i)$ of situation $i$ has no label, so the machine has halted, then for every stack
number $k$ the next code equals the current one, $\mathrm{na}(i) = \mathrm{la}(i)$, and
$\mathrm{pl}(i, k) = 0$ and $\mathrm{cn}(i, k) = 0$: nothing is left pushed and nothing is
consumed.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.halted`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#halted).

## Mixed-radix number

For a base $b$, a top digit $c$, a length $m$ and digits
$D : \mathbb{N} \to \mathbb{N}$, $\mathrm{mix}(b, c, 0, D) = c$ and
$\mathrm{mix}(b, c, m + 1, D) = D(0) + b \cdot \mathrm{mix}(b, c, m, n \mapsto D(n + 1))$; that
is, $D(0) + b\,(D(1) + b\,(\cdots + b\,(D(m - 1) + b\,c)))$, least significant digit first.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.mix`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#mix).

## Mixed-radix index of a situation

Fix an encoding record $E$ of a finite multi-stack
machine $M$. Let $K$ be the number of stacks of $E$, $d$ the window depth of $M$, $A_0$ the number
of (label, state) codes of $E$, $g$ the symbol-code bound of $E$ and $N$ the number of situations.
For a code $c < A_0$ and window contents $w(k, j)$ with $w(k, j) < g$ for all $k < K$ and $j < d$,
let $i = \mathrm{mix}(g, c, K d, D)$ with digits $D(n) = w(\lfloor n / d \rfloor, n \bmod d)$.
Then $i < N$, $\mathrm{la}(i) = c$, and $\mathrm{wa}(i, k, j) = w(k, j)$ for all $k < K$ and
$j < d$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.mix_sit`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#mix-sit).

## Situation surjectivity

Let $E$ be an encoding of a finite multi-stack Turing machine $M$
with $A_0$ label/state codes, $K$ stacks, $g$ symbol codes, window depth $d$ and $N$ situations.
For every $c < A_0$ and every $w : \mathbb{N} \to \mathbb{N} \to \mathbb{N}$ with $w(k, j) < g$
for all $k < K$ and $j < d$, there is a situation $i < N$ whose label/state code
$\mathrm{la}(i)$ equals $c$ and whose window codes satisfy $\mathrm{wa}(i, k, j) = w(k, j)$ for
all $k < K$ and $j < d$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sit_surj`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#sit-surj).

## Finite set of pushable symbols

For a stack $k$ and a statement tree $q$ of a multi-stack
machine with a finite set of states, the finite set of symbols of stack $k$ that some push
instruction of $q$ on stack $k$ pushes for some state: the union, over all push instructions on
$k$ in all branches of $q$, of the images of their push functions over all states.

Formalized by `Cslib.Complexity.CookLevin.Situation.pushFS`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#push-fs).

## Pushable and input symbols of a stack

For a finite multi-stack Turing machine $M$ and a
stack $k$ of $M$, this is the finite set of symbols of stack $k$ consisting of every symbol that
some push node on stack $k$ in the statement of some label of $M$ pushes in some state, together
with, when $k$ is the input stack $k_0$, every symbol of the alphabet of $k_0$.

Formalized by `Cslib.Complexity.CookLevin.Situation.symSet`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 510](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L510). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#sym-set).

## The classical encoding record of a finite multi-stack machine

For every finite
multi-stack Turing machine $M$, an encoding record of $M$, built with classical choice. If $M$ has
$K$ stacks, they are numbered $0, \dots, K - 1$ by a bijection, and numbers $n \ge K$ decode to the
input stack. The pairs of an optional label and a state are numbered $0, \dots, A_0 - 1$ by a
bijection, where $A_0$ is the number of such pairs, and numbers $c \ge A_0$ decode to the pair of
no label and the initial state. The effective alphabet of stack $k$ is the finite set of symbols
that some statement of $M$ can push on $k$, together with the whole input alphabet when $k$ is
the input stack; its $s_k$ elements are listed by a bijection with $\{0, \dots, s_k - 1\}$, a
symbol in it gets code its position in that list plus $1$, and a symbol outside it gets code $0$.

Only the existence of this record is used later.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.ofFinTM2`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 529](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L529). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#of-fin-tm2).

## Time bound of the transition-clause generator on the tables of a machine

Let $M$ be a
finite multi-stack Turing machine with window depth $d$, let $E$ be an encoding of $M$ with $N$
situations, and let $H \ge d$ and $T \in \mathbb{N}$. Run the transition-clause generator for the
layout of $E$, the current-code table $\mathrm{la}$, the next-code table $\mathrm{na}$ and the
window table $\mathrm{wa}$ of $E$ and $N$ situations, started at its first precomputation stage,
in state false, with $T$ on the time counter and $H$ on the height counter in unary, all other
counters empty, and an arbitrary list $o$ of bits on the output stack. Then within
$c\,(T + H + 1)^5$ steps, where $c$ is the constant of the generator's time bound for this layout
and $N$, it reaches its final label $\mathsf{done}$, in some state, with stacks whose output stack
holds the encoding of the transition clause family for this layout, $\mathrm{la}$, $\mathrm{na}$,
$\mathrm{wa}$, $T$, $H$ and $N$, followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.Situation.upd_time`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 562](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L562). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#upd-time).

## Time bound of the situation-definition generator on the tables of a machine

Let $M$ be a
finite multi-stack Turing machine with window depth $d$, let $E$ be an encoding of $M$ with $A_0$
label/state codes and $N$ situations, and let $H \ge d$ and $T \in \mathbb{N}$. Run the
transition-clause generator for the layout of $E$, the current-code table $\mathrm{la}$ of $E$,
the table $\mathrm{sa}(i) = A_0 + i$ (the position of the variable of situation $i$) in place of
the next-code table, the window table $\mathrm{wa}$ of $E$ and $N$ situations, started at its
first precomputation stage, in state false, with $T$ on the time counter and $H$ on the height
counter in unary, all other counters empty, and an arbitrary list $o$ of bits on the output
stack. Then within $c\,(T + H + 1)^5$ steps, where $c$ is the constant of the generator's time
bound for this layout and $N$, it reaches its final label $\mathsf{done}$, in some state, with
stacks whose output stack holds the encoding of the transition clause family for this layout,
$\mathrm{la}$, $\mathrm{sa}$, $\mathrm{wa}$, $T$, $H$ and $N$, followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.Situation.sdef_time`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 571](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L571). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#sdef-time).

## Time bound of the shift generator on the tables of a machine

Let $M$ be a finite
multi-stack Turing machine with window depth $d$, let $E$ be an encoding of $M$ with $A_0$
label/state codes and $N$ situations, and let $H \ge d$ and $T \in \mathbb{N}$. Run the cell-shift
generator for the layout of $E$, the table $\mathrm{sa}(i) = A_0 + i$ (the position of the
variable of situation $i$), the push counts $\mathrm{pl}$, the consumption counts $\mathrm{cn}$
and the pushed codes $\mathrm{pu}$ of $E$ and $N$ situations, started at its first precomputation
stage, in state false, with $T$ on the time counter and $H$ on the height counter in unary, all
other counters empty, and an arbitrary list $o$ of bits on the output stack. Then within
$c\,(T + H + 1)^6$ steps, where $c$ is the constant of the shift-generator time bound for this
layout and $N$, it reaches its final label $\mathsf{done}$, in some state, with stacks whose
output stack holds the encoding of the cell-shift clause family for this layout, $\mathrm{sa}$,
$\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$, $N$, $T$ and $H$, followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.Situation.shift_time`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 580](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L580). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#shift-time).

## Top window of a stack

For $d \in \mathbb{N}$ and a list $L = [x_0, x_1, \dots]$ over a
type $\alpha$ (a stack, top first), the window of depth $d$ of $L$ is the list of length $d$ over
$\alpha$ extended by the empty cell $\bot$ whose entry $j$ is $x_j$ if $j$ is less than the length
of $L$ and $\bot$ otherwise.

Formalized by `Cslib.Complexity.CookLevin.Situation.window`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 596](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L596). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-02/index.html#window).

## Applying an effect to the original stacks

Let $S_0$ assign a list $S_0(k)$ to each stack
$k$, and let $r = (\ell, v, P, c)$ consist of a label $\ell$ (possibly the halted label), a state
$v$, a list $P(k)$ for each stack $k$ and a natural number $c(k)$ for each stack $k$. This is the
configuration with label $\ell$, state $v$, and stack $k$ equal to $P(k)$ followed by $S_0(k)$
with its first $c(k)$ symbols (from the top) removed.

Applied to an effect, $P(k)$ is the pushed prefix still on top of stack $k$ and $c(k)$ is the net
number of original symbols consumed.

Formalized by `Cslib.Complexity.CookLevin.Situation.applyEff`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 601](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L601). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#apply-eff).

## Reading the top through the windows

Let $d \in \mathbb{N}$, let $S_0$ and $P$ assign a list
to each stack, let $c$ assign a natural number to each stack, and let $k$ be a stack with
$c(k) < d$. Reading the top of stack $k$ from the depth-$d$ windows of the lists $S_0$, with pushed
symbols $P$ and consumption counts $c$, gives the first symbol of $P(k)$ followed by $S_0(k)$ with
its first $c(k)$ symbols removed, or ⊥ if that list is empty.

Formalized by `Cslib.Complexity.CookLevin.Situation.readTop_eq`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#read-top-eq).

## The symbolic effect of a statement agrees with the real step

Let $q$ be a statement tree
of a multi-stack machine, $d \in \mathbb{N}$, and $S_0$ an assignment of a list $S_0(k)$ to each
stack $k$. Let $v$ be a state, $P$ an assignment of a list $P(k)$ to each stack, and $c$ an
assignment of a natural number $c(k)$ to each stack with $c(k) + \operatorname{ops}(q) \le d$ for
every $k$. Then running $q$ from state $v$ on the stacks whose stack $k$ is $P(k)$ followed by
$S_0(k)$ with its first $c(k)$ symbols removed gives the configuration obtained by applying to
$S_0$ the effect of $q$ computed from $v$, $P$, $c$ and the depth-$d$ windows of the $S_0(k)$.

Here $\operatorname{ops}(q)$ is the largest number of push, peek and pop nodes on a path of $q$,
so the hypothesis keeps every read inside the windows.

Formalized by `Cslib.Complexity.CookLevin.Situation.eff_agree`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 617](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L617). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#eff-agree).

## Idle-extended step

For a finite TM2 machine $M$ and a configuration $c$, the idle-extended
step of $M$ at $c$ is the configuration that one step of $M$ produces from $c$ when the label of
$c$ is not the halted label, and is $c$ itself when it is (a halted configuration stays put).

Formalized by `Cslib.Complexity.CookLevin.Situation.stepI`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 688](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L688). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#step-i).

## Idle-extended run

For a finite TM2 machine $M$ and a configuration $c$, the idle-extended
run of $M$ from $c$ is the sequence of configurations whose term at time $0$ is $c$ and whose term
at time $t + 1$ is the idle-extended step of $M$ applied to its term at time $t$.

Formalized by `Cslib.Complexity.CookLevin.Situation.runI`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#run-i).

## Windows of a configuration

Let $M$ be a finite TM2 machine with window depth $d$ and let
$c$ be a configuration. The window of $c$ on stack $k$ is the list of length $d$ whose entry at
position $j < d$ is the symbol at depth $j$ of stack $k$ (counted from the top, starting at $0$)
when the stack has more than $j$ symbols, and the empty cell $\bot$ otherwise.

Formalized by `Cslib.Complexity.CookLevin.Situation.winC`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 696](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L696). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#win-c).

## The idle-extended step is the situation step applied to the stacks

Let $M$ be a finite
TM2 machine and $c$ a configuration with label $l$, state $v$ and stacks $S$, and let
$(l', v', P, n)$ be the situation step of $M$ at label $l$ and state $v$ on the windows of $c$.
Then the idle-extended step of $M$ at $c$ is the configuration with label $l'$, state $v'$ and,
on each stack $k$, the list $P_k$ placed on top of what remains of $S_k$ after removing its top
$n_k$ symbols.

This is an equality of full configurations and needs no bound on the stack heights.

Formalized by `Cslib.Complexity.CookLevin.Situation.step_agree`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 702](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L702). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#step-agree).

## Label-and-state code of a configuration

For an encoding $E$ of a machine $M$ and a
configuration $c$ of $M$, this is the number that $E$'s (label, state) numbering assigns to the
pair formed by the label of $c$ (possibly the halted label) and the state of $c$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.code`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 721](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L721). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#code).

## Cell code of a configuration

For an encoding $E$ of a machine $M$, a configuration $c$ of
$M$ and natural numbers $k$ and $j$, this is the code under $E$ of the symbol at position $j$
(counting from $0$ at the top) of the stack that $E$'s inverse stack numbering assigns to $k$, in
$c$; it is $0$ (the code of ⊥) if that stack has at most $j$ symbols.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.cell`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 724](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L724). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#cell).

## Situation index of a configuration

Fix an encoding $E$ of a finite TM2 machine $M$, with
$K$ stacks, symbol-code bound $g$ and window depth $d$. The situation index of a configuration $c$
is the number

$$\sum_{k < K} \sum_{j < d} \mathrm{cell}_c(k, j)\, g^{kd + j} + \mathrm{code}(c)\, g^{Kd},$$

where $\mathrm{code}(c)$ is the combined (label, state) code of $c$ and $\mathrm{cell}_c(k, j)$ is
the cell code of $c$ on stack number $k$ at depth $j$ ($0$ for the empty cell).

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sitIdx`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 727](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L727). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#sit-idx).

## The table-driven row update

Fix an encoding $E$ of a finite TM2 machine, a row height $H$,
a situation $i$ and an old row $\mathrm{old}$ giving a code for each stack number $k$ and depth
$j$. For a stack number $k$, write $p$ for the number of symbols situation $i$ leaves pushed on
stack $k$ and $n$ for the number of original symbols it consumes from stack $k$. The updated row
at $(k, j)$ is the code of the symbol situation $i$ leaves at depth $j$ of stack $k$ if $j < p$;
otherwise it is $\mathrm{old}(k, j - p + n)$ if $j < (H \mathbin{\dot{-}} \max(p, n)) + p$, where
$\dot{-}$ is truncated subtraction; otherwise it is $0$, the empty cell.

These are the three cases the shift clauses force: pushed fill, in-range shift and overflow.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.tabRow`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 732](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L732). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#tab-row).

## Good configurations

For an encoding $E$ of a machine $M$, a configuration $c$ of $M$ is
good when every symbol on every stack $k$ of $c$ is one of the effective symbols of stack $k$
listed by $E$ (so that it has a code).

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.Good`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 738](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L738). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#good).

## The situation index matches the code and windows

Fix an encoding $E$ of a finite TM2
machine $M$, with $K$ stacks, $N$ situations and window depth $d$. If every symbol on every stack
of a configuration $c$ lies in the effective alphabet of $E$, then the situation index $i$ of $c$
satisfies $i < N$, the label/state code of situation $i$ equals the combined (label, state) code
of $c$, and for all $k < K$ and $j < d$ the window symbol code of situation $i$ on stack $k$ at
depth $j$ equals the cell code of $c$ on stack number $k$ at depth $j$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sitIdx_spec`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 764](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L764). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#sit-idx-spec).

## Cells of a pushed prefix over a truncated stack

Let $e$ map elements of $\alpha$ to natural
numbers, and for a list $L$ over $\alpha$ and $i \in \mathbb{N}$ let $L\langle i\rangle$ be $e$ of
the entry of $L$ at position $i$ (counting from $0$), or $0$ if $L$ has at most $i$ entries.
Subtraction of natural numbers is truncated at $0$. Let $P$ and $S$ be lists over $\alpha$ and
$n, H, d, j \in \mathbb{N}$ with $|P| \le d$, $n \le d$ and $|S| \le H - d$, and let $Q$ be $P$
followed by $S$ with its first $n$ entries removed. If $j < |P|$ then
$Q\langle j\rangle = P\langle j\rangle$; otherwise, if $j < (H - \max(|P|, n)) + |P|$ then
$Q\langle j\rangle = S\langle j - |P| + n\rangle$; and otherwise $Q\langle j\rangle = 0$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.row_cell`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 782](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L782). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#row-cell).

## The table-driven step

Fix an encoding $E$ of a finite TM2 machine $M$, with $K$ stacks
and window depth $d$, and a natural number $H$. Let $c$ be a configuration such that every symbol
on every stack of $c$ lies in the effective alphabet of $E$ and every stack of $c$ has length at
most $H \mathbin{\dot{-}} d$ (truncated subtraction). Let $c'$ be the idle-extended step of $M$ at
$c$ and $i$ the situation index of $c$. Then the combined (label, state) code of $c'$ is the next
label/state code after situation $i$, and for all $k < K$ and $j < H$ the cell code of $c'$ on
stack number $k$ at depth $j$ is the value at $(k, j)$ of the table-driven row update with height
$H$ and situation $i$ applied to the cell codes of $c$.

No hypothesis $d \le H$ is needed: if $H < d$, every stack of $c$ is empty.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.table_agree`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 800](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L800). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#table-agree).

## Reads of the in-range shift stay in the row

Fix an encoding $E$ of a finite TM2 machine
and natural numbers $H$, $i$, $k$ and $j$. Write $p$ for the number of symbols situation $i$
leaves pushed on stack number $k$ and $n$ for the number of original symbols it consumes from
stack number $k$. If $p \le j$ and $j < (H \mathbin{\dot{-}} \max(p, n)) + p$, where $\dot{-}$ is
truncated subtraction, then $j - p + n < H$.

So every old cell that the table-driven row update reads lies in the row of height $H$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.tabRow_reads_lt`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 817](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L817). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#tab-row-reads-lt).

## The idle-extended step preserves good configurations

Let $E$ be an encoding of a finite
TM2 machine $M$ and let $c$ be a configuration of $M$. If $c$ is good for $E$, then so is the
idle-extended step of $M$ at $c$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.good_step`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 823](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L823). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#good-step).

## The table-driven step along a run

Fix an encoding $E$ of a finite TM2 machine $M$, with
$K$ stacks, $N$ situations and window depth $d$, a natural number $H$, an input list $s$ and a
time $t$. For each time $u$ let $c_u$ be the configuration at time $u$ of the idle-extended run
of $M$ from the initial configuration of $M$ on input $s$, and let $i$ be the situation index of
$c_t$. If every stack of $c_t$ has length at most $H \mathbin{\dot{-}} d$ (truncated subtraction),
then $i < N$; the label/state code of situation $i$ is the combined (label, state) code of $c_t$;
for all $k < K$ and $j < d$ the window symbol code of situation $i$ on stack $k$ at depth $j$ is
the cell code of $c_t$ on stack number $k$ at depth $j$; the combined (label, state) code of
$c_{t+1}$ is the next label/state code after situation $i$; and for all $k < K$ and $j < H$ the
cell code of $c_{t+1}$ on stack number $k$ at depth $j$ is the value at $(k, j)$ of the
table-driven row update with height $H$ and situation $i$ applied to the cell codes of $c_t$.

Unlike the single-step version, no alphabet hypothesis is needed: every symbol on a stack of such
a run lies in the effective alphabet of $E$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.table_agree_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 849](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L849). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#table-agree-run).

## Reading a list from a sequence of cells

For $f$ mapping each natural number to an element
of $\alpha$ or to ⊥, and $j, m \in \mathbb{N}$, this is the list $[x_0, \dots, x_{r-1}]$ with
$f(j + i) = x_i$ for each $i < r$, where $r = m$ if none of $f(j), \dots, f(j + m - 1)$ is ⊥, and
otherwise $r$ is the least $i < m$ with $f(j + i) = \bot$.

Formalized by `Cslib.Complexity.CookLevin.Situation.decS`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 869](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L869). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#dec-s).

## Reading back a list from its cells

Let $f$ map each natural number to an element of
$\alpha$ or to ⊥, let $S$ be a list over $\alpha$, and let $j, m \in \mathbb{N}$. Suppose that for
every $i \in \mathbb{N}$, $f(j + i)$ is the entry of $S$ at position $i$ (counting from $0$) when
$i$ is less than the length of $S$, and ⊥ otherwise. If $S$ has length at most $m$, then reading
$f$ from position $j$ for at most $m$ positions, stopping at the first ⊥, gives $S$.

Formalized by `Cslib.Complexity.CookLevin.Situation.decS_of_list`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 904](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L904). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-03/index.html#dec-s-of-list).

## Entries of a decoded stack on prefix-form input

Let $f : \mathbb{N} \to
\mathrm{Option}\,\alpha$ and write $\bot$ for the absent value. For $j, m \in \mathbb{N}$ let
$\mathrm{decS}(f, j, m)$ be the list of the values $f(j), f(j + 1), \dots$, read for at most $m$
positions and stopped at the first $\bot$. Suppose $f$ is in prefix form on the window from $j$
to $j + m$: whenever $j \le a \le b < j + m$ and $f(a) = \bot$, also $f(b) = \bot$. Then for every
$i < m$, the $i$-th entry of $\mathrm{decS}(f, j, m)$, taken to be $\bot$ when the list has at
most $i$ entries, equals $f(j + i)$.

Formalized by `Cslib.Complexity.CookLevin.Situation.getElem?_decS`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 917](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L917). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#get-elem-dec-s).

## Stack heights grow by at most the window depth per step

Let $M$ be a finite multi-stack
Turing machine (finitely many stacks, labels and states, and a finite input alphabet), and let $d$
be its window depth, the largest number of push, peek and pop nodes on a root-to-leaf path of any
of its statement trees. For every configuration $c$ of $M$ and every stack $k$, the length of
stack $k$ after one idle-extended step of $M$ from $c$ is at most the length of stack $k$ of $c$
plus $d$.

Formalized by `Cslib.Complexity.CookLevin.Situation.stepI_height`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 937](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L937). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#step-i-height).

## C1 decoder (decoding a row)

Let $E$ be an encoding of a machine $M$, let
$H, n \in \mathbb{N}$, and let $w : \mathbb{N} \to \mathbb{N} \to \mathbb{N}$. The decoded
configuration has the label and the state that the inverse (label, state) numbering of $E$
assigns to $n$. For each stack $k$ of $M$, with stack number $\kappa$, the decoded stack $k$
lists, from the top, the symbols of stack $k$ with codes $w(\kappa, 0), w(\kappa, 1), \dots$,
stopping before the first $j$ at which $w(\kappa, j)$ is $0$ or is not a valid code of stack
$k$, and taking at most $H$ symbols. The valid codes of stack $k$ are $1, \dots, s$, where $s$ is
the size of its effective alphabet, and code $i + 1$ stands for symbol number $i$ of that
alphabet, counting from $0$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.decRow`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 957](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L957). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#dec-row).

## Well-formed rows of cells

Let $M$ be a finite multi-stack Turing machine and $E$ an
encoding of $M$ with $K$ numbered stacks, let $H \in \mathbb{N}$, and let
$w : \mathbb{N} \to \mathbb{N} \to \mathbb{N}$ assign a code $w(k, j)$ to each stack number $k$
and depth $j$. The row $w$ is well formed at height $H$ when for every $k < K$ and every $j < H$:
$w(k, j)$ is at most the size of the effective alphabet of the stack numbered $k$, and if
$w(k, j) = 0$ then $w(k, b) = 0$ for every $b$ with $j \le b < H$.

Code $0$ is the empty cell, so the second condition says that each stack is in prefix form.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.RowOK`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 961](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L961). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#row-ok).

## C1a (decoding recovers a good configuration)

Let $E$ be an encoding of a machine $M$,
let $H \in \mathbb{N}$, and let $c$ be a good configuration of $M$ (every symbol on every stack
of $c$ lies in the effective alphabet of $E$) all of whose stacks have length at most $H$. Then
the row decoder of $E$ at height $H$, applied to the (label, state) code of $c$ and the cell
array of $c$, returns $c$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.decRow_enc`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 977](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L977). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#dec-row-enc).

## C1b (decoding a well-formed row loses nothing)

Let $E$ be an encoding of a machine $M$
with $K$ numbered stacks and $A_0$ (label, state) codes, let $H \in \mathbb{N}$, let $n < A_0$,
and let $w : \mathbb{N} \to \mathbb{N} \to \mathbb{N}$ be a well-formed row of height $H$: for
all $k < K$ and $j < H$, $w(k, j)$ is at most the size of the effective alphabet of stack number
$k$, and if $w(k, j) = 0$ then $w(k, b) = 0$ for every $b$ with $j \le b < H$. Let $c$ be the
configuration that the row decoder of $E$ at height $H$ returns on code $n$ and array $w$. Then
the (label, state) code of $c$ is $n$, and the cell code of $c$ at stack number $k$ and depth $j$
equals $w(k, j)$ for all $k < K$ and $j < H$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.enc_decRow`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 989](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L989). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#enc-dec-row).

## C1c (cell arrays of good configurations are well-formed rows)

Let $E$ be an encoding
of a machine $M$ with $K$ numbered stacks, and let $c$ be a good configuration of $M$, that is,
every symbol on every stack of $c$ lies in the effective alphabet of $E$. Let $w$ be the cell
array of $c$: $w(k, j)$ is the code of the symbol at depth $j$ from the top of stack number $k$,
or $0$ if there is none. Then for every $H \in \mathbb{N}$, $w$ is a well-formed row of height
$H$: for all $k < K$ and $j < H$, the code $w(k, j)$ is at most the size of the effective
alphabet of stack number $k$, and if $w(k, j) = 0$ then $w(k, b) = 0$ for every $b$ with
$j \le b < H$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.cell_rowOK`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1002](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1002). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#cell-row-ok).

## C1d (decoded configurations are good)

Let $E$ be an encoding of a machine $M$. For all
$H, n \in \mathbb{N}$ and every $w : \mathbb{N} \to \mathbb{N} \to \mathbb{N}$, the configuration
that the row decoder of $E$ at height $H$ returns on code $n$ and array $w$ is good: every symbol
on each of its stacks lies in the effective alphabet of $E$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.decRow_good`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1019](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1019). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#dec-row-good).

## C1e (the row decoder reads only the window)

Let $E$ be an encoding of a machine $M$
with $K$ numbered stacks, let $H, n \in \mathbb{N}$, and let
$w, w' : \mathbb{N} \to \mathbb{N} \to \mathbb{N}$. If $w(k, j) = w'(k, j)$ for all $k < K$ and
$j < H$, then the row decoder of $E$ at height $H$ returns the same configuration on code $n$
and array $w$ as on code $n$ and array $w'$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.decRow_congr`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1031](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1031). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#dec-row-congr).

## Good configurations are determined by their row (C1f)

Let $M$ be a finite multi-stack
Turing machine and $E$ an encoding of $M$ with $K$ numbered stacks, let $H \in \mathbb{N}$, and
for a configuration $c$ write $\mathrm{cell}(c, k, j)$ for the code of the symbol at depth $j$ of
the stack numbered $k$ ($0$ if there is none). Let $c$ and $c'$ be configurations that are good
for $E$ (every stack symbol lies in the effective alphabet of its stack) and all of whose stacks
have length at most $H$. If $c$ and $c'$ have the same (label, state) code and
$\mathrm{cell}(c, k, j) = \mathrm{cell}(c', k, j)$ for all $k < K$ and $j < H$, then $c = c'$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.row_inj`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1039](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1039). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#row-inj).

## C2' (decoding the table-driven row gives the next configuration)

Let $E$ be an encoding
of a machine $M$ with window depth $d$, let $H \ge d$ be a natural number, and let $c$ be a good
configuration of $M$ (every symbol on every stack of $c$ lies in the effective alphabet of $E$)
all of whose stacks have length at most $H - d$. Let $i$ be the situation index of $c$. Then the
row decoder of $E$ at height $H$, applied to the next (label, state) code of situation $i$ and to
the table-driven row update at height $H$ of situation $i$ on the cell array of $c$, returns the
idle-extended step of $c$: the configuration after one step of $M$, or $c$ itself if $c$ is
halted.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.decRow_tabRow`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1047](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1047). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#dec-row-tab-row).

## Truth of a variable under an assignment

For an assignment $a$, given as a list of
booleans, and a variable index $v \in \mathbb{N}$, the variable $v$ is true under $a$ when $v$ is
less than the length of $a$ and the entry of $a$ at position $v$ is true. In particular, variables
with index at least the length of $a$ are not true.

Formalized by `Cslib.Complexity.CookLevin.Situation.Tr`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1064](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1064). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#tr).

## L0 (a satisfied dense clause has a satisfied listed literal)

Let $V \in \mathbb{N}$, let
$\ell$ be a list of pairs $(p, b)$ of a variable index $p \in \mathbb{N}$ and a sign $b$ (true or
false), and let $a$ be a list of booleans. If $a$ satisfies the dense clause over $V$ variables
built from $\ell$, then some pair $(p, b) \in \ell$ has $p$ less than the length of $a$ and
$a_p = b$.

Formalized by `Cslib.Complexity.CookLevin.Situation.clauseSat_dense`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1078](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1078). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#clause-sat-dense).

## In-range shift forcing (L1)

Let $L$ be a layout with $K$ stacks and $g$ symbol codes,
let $sa$, $pl$, $cn$, $pu$ be situation tables and $N, T, H \in \mathbb{N}$, and let $a$ be an
assignment satisfying the cell-shift clause family of $L$ with these tables and bounds $N$, $T$,
$H$. Call a variable true when its index is less than the length of $a$ and $a$ is true there.
Write $S[t, i]$ for the label/state variable $sa(i)$ of row $t + 1$ and $C[t, k, j, x]$ for the
cell variable of row $t$, stack $k$, depth $j$ and symbol code $x$ (both at height $H$). Let
$t < T$, $i < N$, $k < K$, $x < g$ and $u < H - \max(pl(i, k), cn(i, k))$, with truncated
subtraction. If $S[t, i]$ and $C[t, k, u + cn(i, k), x]$ are true, then
$C[t + 1, k, u + pl(i, k), x]$ is true.

Formalized by `Cslib.Complexity.CookLevin.Situation.sh_force`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1092](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1092). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#sh-force).

## Cell block of a row equal to an array

Let $E$ be an encoding of a machine $M$ with $K$
numbered stacks and $g$ symbol codes, let $a$ be a list of booleans, let $H, t \in \mathbb{N}$,
and let $w : \mathbb{N} \to \mathbb{N} \to \mathbb{N}$. The cell block of row $t$ is exactly
$w$ under $a$ when, for all $k < K$, $j < H$ and $x < g$, the cell variable for time $t$,
stack $k$, depth $j$ and symbol code $x$ in the layout of $E$ at height $H$ is true under $a$ if
and only if $x = w(k, j)$. A variable $v$ is true under $a$ when $v$ is less than the length of
$a$ and the entry of $a$ at position $v$ is true.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.CellsAre`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#cells-are).

## Cell literals of an array hold in a row

Let $E$ be an encoding of a machine $M$ with
$K$ numbered stacks, let $a$ be a list of booleans, let $H, t \in \mathbb{N}$, and let
$w : \mathbb{N} \to \mathbb{N} \to \mathbb{N}$. The cell literals of $w$ hold in row $t$ under
$a$ when, for all $k < K$ and $j < H$, the cell variable for time $t$, stack $k$, depth $j$ and
symbol code $w(k, j)$ in the layout of $E$ at height $H$ is true under $a$, that is, its index is
less than the length of $a$ and the entry of $a$ at that index is true.

Unlike the exact form, this says nothing about the cell variables for other symbol codes.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.CellsHold`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#cells-hold).

## Positive core of the shift step (L2⁺)

Let $M$ be a finite multi-stack Turing machine and
$E$ an encoding of $M$ with $K$ numbered stacks, tables $sa$, $pl$, $cn$, $pu$ and $N$ situations,
let $T, H, t \in \mathbb{N}$ with $t < T$, and let $a$ be an assignment satisfying the cell-shift
clause family of the layout of $E$ with these tables and bounds $N$, $T$, $H$. Call a variable
true when its index is less than the length of $a$ and $a$ is true there. Write $S[t, i]$ for the
label/state variable $sa(i)$ of row $t + 1$, $C[t, k, j, x]$ for the cell variable of row $t$,
stack $k$, depth $j$ and symbol code $x$ (both at height $H$), and $\mathrm{cell}(c, k, j)$ for
the code at depth $j$ of the stack numbered $k$ of a configuration $c$ ($0$ if there is none).
Let $c$ be a configuration that is good for $E$ (every stack symbol lies in the effective
alphabet of its stack), with situation index $i$. Suppose that
$C[t, k', j', \mathrm{cell}(c, k', j')]$ is true for all $k' < K$ and $j' < H$, and that
$S[t, i]$ is true. Then for every $k < K$ and every $j$ with
$pl(i, k) \le j < H - \max(pl(i, k), cn(i, k)) + pl(i, k)$ (truncated subtraction), the variable
$C[t + 1, k, j, R(k, j)]$ is true, where $R$ is the table-driven row update at height $H$ of the
cells of $c$ for situation $i$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sh_hold`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#sh-hold).

## Exact shift step (L2)

Let $M$ be a finite multi-stack Turing machine and $E$ an encoding
of $M$ with $K$ numbered stacks, $g$ symbol codes, tables $sa$, $pl$, $cn$, $pu$ and $N$
situations, let $T, H, t \in \mathbb{N}$ with $t < T$, and let $a$ be an assignment satisfying
the cell-shift clause family of the layout of $E$ with these tables and bounds $N$, $T$, $H$.
Call a variable true when its index is less than the length of $a$ and $a$ is true there. Write
$S[t, i]$ for the label/state variable $sa(i)$ of row $t + 1$, $C[t, k, j, x]$ for the cell
variable of row $t$, stack $k$, depth $j$ and symbol code $x$ (both at height $H$), and
$\mathrm{cell}(c, k, j)$ for the code at depth $j$ of the stack numbered $k$ of a configuration
$c$ ($0$ if there is none). Let $c$ be a configuration that is good for $E$ (every stack symbol
lies in the effective alphabet of its stack), with situation index $i$. Suppose that for all
$k' < K$, $j' < H$ and $x < g$ the variable $C[t, k', j', x]$ is true exactly when
$x = \mathrm{cell}(c, k', j')$, and that $S[t, i]$ is true. Let $k < K$ and
$pl(i, k) \le j < H - \max(pl(i, k), cn(i, k)) + pl(i, k)$ (truncated subtraction), and suppose
at most one $x < g$ makes $C[t + 1, k, j, x]$ true. Then for every $x < g$, $C[t + 1, k, j, x]$
is true exactly when $x = R(k, j)$, where $R$ is the table-driven row update at height $H$ of the
cells of $c$ for situation $i$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sh_step_cell`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#sh-step-cell).

## Exact shift step on a real run (L3)

Let $M$ be a finite multi-stack Turing machine and
$E$ an encoding of $M$ with $K$ numbered stacks, $g$ symbol codes, tables $sa$, $pl$, $cn$, $pu$
and $N$ situations, let $T, H, t \in \mathbb{N}$ with $t < T$, and let $a$ be an assignment
satisfying the cell-shift clause family of the layout of $E$ with these tables and bounds $N$,
$T$, $H$. Call a variable true when its index is less than the length of $a$ and $a$ is true
there. Write $S[t, i]$ for the label/state variable $sa(i)$ of row $t + 1$, $C[t, k, j, x]$ for
the cell variable of row $t$, stack $k$, depth $j$ and symbol code $x$ (both at height $H$), and
$\mathrm{cell}(c, k, j)$ for the code at depth $j$ of the stack numbered $k$ of a configuration
$c$ ($0$ if there is none). Fix an input list $s$, let $c_n$ be the configuration after $n$
idle-extended steps of $M$ from the initial configuration on $s$, and let $i$ be the situation
index of $c_t$. Suppose that every stack of $c_t$ has length at most $H - d$, where $d$ is the
window depth of $M$, that for all $k' < K$, $j' < H$ and $x < g$ the variable $C[t, k', j', x]$
is true exactly when $x = \mathrm{cell}(c_t, k', j')$, and that $S[t, i]$ is true. Let $k < K$
and $pl(i, k) \le j < H - \max(pl(i, k), cn(i, k)) + pl(i, k)$, and suppose at most one $x < g$
makes $C[t + 1, k, j, x]$ true. Then for every $x < g$, $C[t + 1, k, j, x]$ is true exactly when
$x = \mathrm{cell}(c_{t+1}, k, j)$. Subtraction is truncated at $0$.

No row is decoded in the proof.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sh_step_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#sh-step-run).

## Positive shift step on a real run (L3⁺)

Let $M$ be a finite multi-stack Turing machine
and $E$ an encoding of $M$ with $K$ numbered stacks, tables $sa$, $pl$, $cn$, $pu$ and $N$
situations, let $T, H, t \in \mathbb{N}$ with $t < T$, and let $a$ be an assignment satisfying
the cell-shift clause family of the layout of $E$ with these tables and bounds $N$, $T$, $H$.
Call a variable true when its index is less than the length of $a$ and $a$ is true there. Write
$S[t, i]$ for the label/state variable $sa(i)$ of row $t + 1$, $C[t, k, j, x]$ for the cell
variable of row $t$, stack $k$, depth $j$ and symbol code $x$ (both at height $H$), and
$\mathrm{cell}(c, k, j)$ for the code at depth $j$ of the stack numbered $k$ of a configuration
$c$ ($0$ if there is none). Fix an input list $s$, let $c_n$ be the configuration after $n$
idle-extended steps of $M$ from the initial configuration on $s$, and let $i$ be the situation
index of $c_t$. Suppose that every stack of $c_t$ has length at most $H - d$, where $d$ is the
window depth of $M$, that $C[t, k', j', \mathrm{cell}(c_t, k', j')]$ is true for all $k' < K$
and $j' < H$, and that $S[t, i]$ is true. Then for every $k < K$ and every $j$ with
$pl(i, k) \le j < H - \max(pl(i, k), cn(i, k)) + pl(i, k)$, the variable
$C[t + 1, k, j, \mathrm{cell}(c_{t+1}, k, j)]$ is true. Subtraction is truncated at $0$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sh_step_run_pos`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-04/index.html#sh-step-run-pos).

## Transition clauses force the next label

Let $L$ be a layout with $K$ stacks and window
depth $d$, let $\mathrm{la}, \mathrm{na} : \mathbb{N} \to \mathbb{N}$ and
$\mathrm{wa} : \mathbb{N} \to \mathbb{N} \to \mathbb{N} \to \mathbb{N}$ be tables, and let $a$ be
an assignment satisfying the transition clause family of $L$, $\mathrm{la}$, $\mathrm{na}$ and
$\mathrm{wa}$ for bounds $T$, $H$ and $N$. Write $X[t, b]$ and $C[t, k, j, x]$ for the
label/state and cell variables at height $H$. Suppose $t < T$, $i < N$, $X[t, \mathrm{la}(i)]$ is
true under $a$, and for every $n < Kd$, writing $q = \lfloor n / d \rfloor$ and
$r = n \bmod d$, the variable $C[t, q, r, \mathrm{wa}(i, q, r)]$ is true under $a$. Then
$X[t + 1, \mathrm{na}(i)]$ is true under $a$.

The window literals are indexed by $n$ exactly as in the clause, and no one-hot hypothesis on $a$
is needed.

Formalized by `Cslib.Complexity.CookLevin.Situation.fam_force`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#fam-force).

## Transition clauses force the next label, stack-and-depth form

Let $L$ be a layout with
$K$ stacks and window depth $d$, let $\mathrm{la}, \mathrm{na} : \mathbb{N} \to \mathbb{N}$ and
$\mathrm{wa} : \mathbb{N} \to \mathbb{N} \to \mathbb{N} \to \mathbb{N}$ be tables, and let $a$ be
an assignment satisfying the transition clause family of $L$, $\mathrm{la}$, $\mathrm{na}$ and
$\mathrm{wa}$ for bounds $T$, $H$ and $N$. Write $X[t, b]$ and $C[t, k, j, x]$ for the
label/state and cell variables at height $H$. If $t < T$, $i < N$, $X[t, \mathrm{la}(i)]$ is true
under $a$, and $C[t, k, j, \mathrm{wa}(i, k, j)]$ is true under $a$ for all $k < K$ and $j < d$,
then $X[t + 1, \mathrm{na}(i)]$ is true under $a$.

Formalized by `Cslib.Complexity.CookLevin.Situation.fam_force_kj`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#fam-force-kj).

## The code of a configuration holds in a row

Given an encoding of a machine $M$, an
assignment $a$, a height $H$, a time $t$ and a configuration $c$ of $M$, the code of $c$ holds in
row $t$ when the label/state variable of row $t$ (at height $H$) whose index is the combined
(label, state) code of $c$ is true under $a$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.CodeHolds`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#code-holds).

## L2 (S-definition, positive)

Let $E$ be an encoding of the machine $M$ with $K$ stacks and
layout $L$, let $d$ be the window depth of $M$, let $H \in \mathbb{N}$ with $d \le H$, let $W$ be
the row width of $L$ at height $H$, and write $X[t, x] = tW + x$ for the label/state variables and
$C[t, k, j, x]$ for the cell variable of row $t$, stack $k$, depth $j$ and symbol code $x$. For a
configuration $c$ write $\kappa(c)$ for its (label, state) code and $\gamma_c(k, j)$ for the code
of its cell at stack $k$ and depth $j$. Let $T, t \in \mathbb{N}$ with $t < T$, and let the
assignment $a$ satisfy the transition clause family of $L$ for $T$, $H$ and the number $N$ of
situations, with the current-label table $\mathrm{la}$ and the window table $\mathrm{wa}$ of $E$,
and with the table $\mathrm{sa}$ of $E$ (where $\mathrm{sa}(i)$ is the position of the variable of
situation $i$ in the label/state block) in place of the next-label table. Let $c$ be a good
configuration with situation index $i$ such that $X[t, \kappa(c)]$ is true under $a$ and
$C[t, k, j, \gamma_c(k, j)]$ is true under $a$ for all $k < K$ and $j < H$. Then the variable
$X[t + 1, \mathrm{sa}(i)]$ is true under $a$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sd_hold`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#sd-hold).

## L3 (S-definition, real run)

Let $E$ be an encoding of the machine $M$ with $K$ stacks and
layout $L$, let $d$ be the window depth of $M$, let $H \in \mathbb{N}$ with $d \le H$, let $W$ be
the row width of $L$ at height $H$, and write $X[t, x] = tW + x$ for the label/state variables and
$C[t, k, j, x]$ for the cell variable of row $t$, stack $k$, depth $j$ and symbol code $x$. For a
configuration $c$ write $\kappa(c)$ for its (label, state) code and $\gamma_c(k, j)$ for the code
of its cell at stack $k$ and depth $j$. Fix an input list $s$, let $c_n$ be the configuration
after $n$ steps of the idle-extended run of $M$ from the initial configuration on $s$, let
$T, t \in \mathbb{N}$ with $t < T$, and let $i$ be the situation index of $c_t$. Let the
assignment $a$ satisfy the transition clause family of $L$ for $T$, $H$ and the number $N$ of
situations, with the current-label table $\mathrm{la}$ and the window table $\mathrm{wa}$ of $E$,
and with the table $\mathrm{sa}$ of $E$ (where $\mathrm{sa}(i)$ is the position of the variable of
situation $i$ in the label/state block) in place of the next-label table. If $X[t, \kappa(c_t)]$
is true under $a$ and $C[t, k, j, \gamma_{c_t}(k, j)]$ is true under $a$ for all $k < K$ and
$j < H$, then the variable $X[t + 1, \mathrm{sa}(i)]$ is true under $a$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sd_step_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#sd-step-run).

## Composition with the shift family

Let $E$ be an encoding of the machine $M$ with $K$
stacks, layout $L$, $N$ situations and situation tables $\mathrm{la}$, $\mathrm{wa}$,
$\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$ and $\mathrm{pu}$, let $d$ be the window depth of $M$,
let $H \in \mathbb{N}$ with $d \le H$, and let $T, t \in \mathbb{N}$ with $t < T$. Call a
variable true under an assignment $a$ when its index is less than the length of $a$ and $a$ is
true there. Write $X[r, x]$ for the label/state variable $x$ of row $r$ and $C[r, k, j, x]$ for
the cell variable of row $r$, stack $k$, depth $j$ and symbol code $x$ (both at height $H$). For
a configuration $c$ write $\kappa(c)$ for its (label, state) code and $\gamma_c(k, j)$ for the
code of its cell at stack $k$ and depth $j$ ($0$ if there is none). Fix an input list $s$, let
$c_n$ be the configuration after $n$ steps of the idle-extended run of $M$ from the initial
configuration on $s$, and let $i$ be the situation index of $c_t$. Let $a$ satisfy both the
transition clause family of $L$ for $T$, $H$ and $N$ with the tables $\mathrm{la}$ and
$\mathrm{wa}$ and with $\mathrm{sa}$ in place of the next-label table, and the cell-shift clause
family of $L$ with the tables $\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$ for $N$,
$T$ and $H$. Suppose that every stack of $c_t$ has length at most $H - d$, that
$X[t, \kappa(c_t)]$ is true, and that $C[t, k', j', \gamma_{c_t}(k', j')]$ is true for all
$k' < K$ and $j' < H$. Then for every $k < K$ and every $j$ with
$\mathrm{pl}(i, k) \le j < H - \max(\mathrm{pl}(i, k), \mathrm{cn}(i, k)) + \mathrm{pl}(i, k)$,
the variable $C[t + 1, k, j, \gamma_{c_{t+1}}(k, j)]$ is true. Subtraction is truncated at $0$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sdsh_step_run_pos`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#sdsh-step-run-pos).

## Update forcing (positive)

Let $E$ be an encoding of the machine $M$ with $K$ stacks and
layout $L$, let $d$ be the window depth of $M$, let $H \in \mathbb{N}$ with $d \le H$, let $W$ be
the row width of $L$ at height $H$, and write $X[t, x] = tW + x$ for the label/state variables and
$C[t, k, j, x]$ for the cell variable of row $t$, stack $k$, depth $j$ and symbol code $x$. For a
configuration $c$ write $\kappa(c)$ for its (label, state) code and $\gamma_c(k, j)$ for the code
of its cell at stack $k$ and depth $j$. Let $T, t \in \mathbb{N}$ with $t < T$, and let the
assignment $a$ satisfy the transition clause family of $L$ with the current-label table
$\mathrm{la}$, the next-label table $\mathrm{na}$ and the window table $\mathrm{wa}$ of $E$, for
$T$, $H$ and the number $N$ of situations. Let $c$ be a good configuration with situation index
$i$ such that $X[t, \kappa(c)]$ is true under $a$ and $C[t, k, j, \gamma_c(k, j)]$ is true under
$a$ for all $k < K$ and $j < H$. Then the variable $X[t + 1, \mathrm{na}(i)]$ is true under $a$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.upd_hold`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#upd-hold).

## Update forcing, real run

Let $E$ be an encoding of the machine $M$ with $K$ stacks and
layout $L$, let $d$ be the window depth of $M$, let $H \in \mathbb{N}$ with $d \le H$, let $W$ be
the row width of $L$ at height $H$, and write $X[t, x] = tW + x$ for the label/state variables and
$C[t, k, j, x]$ for the cell variable of row $t$, stack $k$, depth $j$ and symbol code $x$. For a
configuration $c$ write $\kappa(c)$ for its (label, state) code and $\gamma_c(k, j)$ for the code
of its cell at stack $k$ and depth $j$. Fix an input list $s$, let $c_n$ be the configuration
after $n$ steps of the idle-extended run of $M$ from the initial configuration on $s$, let
$T, t \in \mathbb{N}$ with $t < T$, and suppose every stack of $c_t$ has length at most $H - d$.
Let the assignment $a$ satisfy the transition clause family of $L$ with the current-label table
$\mathrm{la}$, the next-label table $\mathrm{na}$ and the window table $\mathrm{wa}$ of $E$, for
$T$, $H$ and the number $N$ of situations. If $X[t, \kappa(c_t)]$ is true under $a$ and
$C[t, k, j, \gamma_{c_t}(k, j)]$ is true under $a$ for all $k < K$ and $j < H$, then the variable
$X[t + 1, \kappa(c_{t+1})]$ is true under $a$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.upd_step_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#upd-step-run).

## Pushed-fill forcing

Let $L$ be a layout with $A$ label/state variables, $K$ stacks and
$g$ symbol codes, let $\mathrm{sa}, \mathrm{pl}, \mathrm{cn}, \mathrm{pu}$ be situation tables and
$N, T, H \in \mathbb{N}$, and write $W = A + KHg$, $X[t, x] = tW + x$ and
$C[t, k, j, x] = tW + A + (kH + j)g + x$. If the assignment $a$ satisfies the cell-shift family
of these data, $t < T$, $i < N$, $k < K$, $j < \mathrm{pl}(i, k)$ and the variable
$X[t + 1, \mathrm{sa}(i)]$ is true under $a$, then the variable
$C[t + 1, k, j, \mathrm{pu}(i, k, j)]$ is true under $a$.

Only the situation literal is read.

Formalized by `Cslib.Complexity.CookLevin.Situation.pf_force`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#pf-force).

## Overflow forcing

Let $L$ be a layout with $K$ stacks, let $\mathrm{sa}$, $\mathrm{pl}$,
$\mathrm{cn}$ and $\mathrm{pu}$ be situation tables, and let $a$ be an assignment satisfying the
cell-shift clause family of $L$ and these tables for bounds $N$, $T$ and $H$. Write $X[t, b]$ and
$C[t, k, j, x]$ for the label/state and cell variables at height $H$. If $t < T$, $i < N$,
$k < K$, $r < \mathrm{cn}(i, k) - \mathrm{pl}(i, k)$ and the situation variable
$X[t + 1, \mathrm{sa}(i)]$ is true under $a$, then the variable
$C[t + 1, k, H - \mathrm{cn}(i, k) + \mathrm{pl}(i, k) + r, 0]$ is true under $a$, where symbol
code $0$ is the empty cell. Subtraction is truncated at zero.

Formalized by `Cslib.Complexity.CookLevin.Situation.ov_force`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1338](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#ov-force).

## Pushed-fill forcing for a good configuration

Let $E$ be an encoding of the machine $M$
with $K$ stacks and layout $L$, let $H \in \mathbb{N}$, let $W$ be the row width of $L$ at height
$H$, and write $X[t, x] = tW + x$ for the label/state variables and $C[t, k, j, x]$ for the cell
variable of row $t$, stack $k$, depth $j$ and symbol code $x$. Let $T, t \in \mathbb{N}$ with
$t < T$, let the assignment $a$ satisfy the cell-shift family of $E$ (tables $\mathrm{sa}$,
$\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$ and $N$ situations) for $T$ and $H$, and let $c$ be a
good configuration with situation index $i$ such that $X[t + 1, \mathrm{sa}(i)]$ is true under
$a$. Then for all $k < K$ and $j < \mathrm{pl}(i, k)$ the variable $C[t + 1, k, j, r]$ is true
under $a$, where $r$ is the entry at stack $k$ and depth $j$ of the table-driven row update, at
height $H$ and for situation $i$, of the cell codes of $c$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.pf_hold`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1362](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#pf-hold).

## Overflow cells of the next row hold the table value

Let $E$ be an encoding of a machine
$M$ with $K$ stacks and window depth $d$, and let $a$ be an assignment satisfying the cell-shift
clause family of $E$'s layout and tables $\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$,
$\mathrm{pu}$ for $E$'s number of situations and bounds $T$ and $H$. Write $X[t, b]$ and
$C[t, k, j, x]$ for the label/state and cell variables at height $H$. Let $t < T$, let $c$ be a
configuration of $M$ all of whose stack symbols have codes, suppose $d \le H$, let $i$ be the
situation index of $c$, and suppose $X[t + 1, \mathrm{sa}(i)]$ is true under $a$. Then for every
$k < K$ and every $j$ with
$H - \max(\mathrm{pl}(i, k), \mathrm{cn}(i, k)) + \mathrm{pl}(i, k) \le j < H$, the variable
$C[t + 1, k, j, x]$ is true under $a$, where $x$ is the value at $(k, j)$ of the table-driven row
update at height $H$ of the cells of $c$ for situation $i$. Subtraction is truncated at zero.

At these depths the table-driven row update is $0$, the empty cell.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.ov_hold`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#ov-hold).

## Pushed-fill forcing on a real run

Let $E$ be an encoding of the machine $M$ with $K$
stacks and layout $L$, let $d$ be the window depth of $M$, let $H \in \mathbb{N}$ with $d \le H$,
let $W$ be the row width of $L$ at height $H$, and write $X[t, x] = tW + x$ for the label/state
variables and $C[t, k, j, x]$ for the cell variable of row $t$, stack $k$, depth $j$ and symbol
code $x$. Fix an input list $s$, let $c_n$ be the configuration after $n$ steps of the
idle-extended run of $M$ from the initial configuration on $s$, let $T, t \in \mathbb{N}$ with
$t < T$, let $i$ be the situation index of $c_t$, and suppose every stack of $c_t$ has length at
most $H - d$. Let the assignment $a$ satisfy the cell-shift family of $E$ (tables $\mathrm{sa}$,
$\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$ and $N$ situations) for $T$ and $H$, and suppose
$X[t + 1, \mathrm{sa}(i)]$ is true under $a$. Then for all $k < K$ and $j < \mathrm{pl}(i, k)$ the
variable $C[t + 1, k, j, x]$ is true under $a$, where $x$ is the code of the cell of $c_{t+1}$ at
stack $k$ and depth $j$ (code $0$ if that cell is empty).

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.pf_step_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1392](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#pf-step-run).

## Overflow cells of the next row on a real run

Let $E$ be an encoding of a machine $M$ with
$K$ stacks and window depth $d$, let $s$ be an input, and let $c_t$ be the configuration at step
$t$ of the idle-extended run of $M$ from the initial configuration on input $s$. Let $a$ be an
assignment satisfying the cell-shift clause family of $E$'s layout and tables $\mathrm{sa}$,
$\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$ for $E$'s number of situations and bounds $T$ and $H$,
and write $X[t, b]$ and $C[t, k, j, x]$ for the label/state and cell variables at height $H$.
Suppose $t < T$, every stack of $c_t$ has length at most $H - d$, $d \le H$, and
$X[t + 1, \mathrm{sa}(i)]$ is true under $a$, where $i$ is the situation index of $c_t$. Then for
every $k < K$ and every $j$ with
$H - \max(\mathrm{pl}(i, k), \mathrm{cn}(i, k)) + \mathrm{pl}(i, k) \le j < H$, the variable
$C[t + 1, k, j, x]$ is true under $a$, where $x$ is the code of the cell of stack number $k$ at
depth $j$ from the top in $c_{t+1}$ ($0$ if that cell is empty). Subtraction is truncated at
zero.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.ov_step_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1403](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#ov-step-run).

## Stack cap

For natural numbers $m$, $T$ and $d$ (an input bound, a run length and a
per-step growth), the stack cap is $H = m + (T + 1) d + 1$.

It is used with $d$ the window depth of the machine.

Formalized by `Cslib.Complexity.CookLevin.Situation.capH`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#cap-h).

## Stack heights along a run

Let $M$ be a finite TM2 machine with window depth $d$, let $c$
be a configuration and $k$ a stack. For every $t \in \mathbb{N}$, stack $k$ of the configuration
reached from $c$ after $t$ steps of the idle-extended run has length at most the length of stack
$k$ of $c$ plus $t \cdot d$.

Formalized by `Cslib.Complexity.CookLevin.Situation.runI_height`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1423](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#run-i-height).

## Stack heights are at most the cap minus the window depth

Let $M$ be a finite
multi-stack Turing machine with window depth $d$, let $m$, $T$ and $t$ be natural numbers with
$t \le T$, and let $s$ be an input of length at most $m$. In the idle-extended run of $M$ from the
initial configuration on input $s$, every stack of the configuration at step $t$ has length at
most $H - d$, where $H = m + (T + 1) d + 1$ is the stack cap for input bound $m$, run length $T$
and per-step growth $d$.

Formalized by `Cslib.Complexity.CookLevin.Situation.capH_height`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#cap-h-height).

## Stack-cap constraint 1

For natural numbers $\ell$, $m$, $T$ and $d$ with $\ell \le m$, we
have $\ell + (T + 1) d \le H$, where $H = m + (T + 1) d + 1$ is the stack cap for input bound $m$,
run length $T$ and per-step growth $d$.

Formalized by `Cslib.Complexity.CookLevin.Situation.capH_c1`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1455](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#cap-h-c1).

## Stack-cap constraint 2

For natural numbers $m$, $T$ and $d$ with $T \ge 1$, the stack cap
$H = m + (T + 1) d + 1$ for input bound $m$, run length $T$ and per-step growth $d$ satisfies
$2d \le H$.

Formalized by `Cslib.Complexity.CookLevin.Situation.capH_c2`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1459](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1459). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#cap-h-c2).

## The three depth regions cover every depth exactly once

Let $p, q, H, j$ be natural
numbers with $j < H$, and let $m = H - \max(p, q) + p$, where the subtraction is truncated at
$0$. Then $j$ lies in exactly one of the ranges $j < p$ (pushed fill), $p \le j < m$ (in-range
shift) and $m \le j < H$ (overflow).

These are the depth hypotheses of the pushed-fill, in-range shift and overflow lemmas; nothing is
assumed about $p$, $q$ and $H$.

Formalized by `Cslib.Complexity.CookLevin.Situation.region_cover`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1467](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-05/index.html#region-cover).

## Cell literals propagate one step along the real run

Let $E$ be an encoding of a machine
$M$ with window depth $d$, let $s$ be a list of symbols of the input stack of $M$, and for each
$n$ let $c_n$ be the configuration after $n$ steps of the idle-extended run of $M$ from its
initial configuration on $s$. Let $T, H, t$ be natural numbers with $t < T$ and $d \le H$.
Suppose an assignment $a$ satisfies the transition clause family of $E$ with the
situation-variable table $\mathrm{sa}$ in place of the next-label table (the S-definition family)
at $T$, $H$ and the number $N$ of situations of $E$, and satisfies the cell-shift clause family
of $E$ at $N$, $T$, $H$. Suppose also that every stack of $c_t$ has length at most $H - d$, that
the code literal of $c_t$ holds in row $t$ (the label/state variable of row $t$ for the code of
$c_t$ is true under $a$), and that the cell literals of $c_t$ hold in row $t$ (for every stack
number $k$ below the number of stacks and every depth $j < H$, the cell variable of row $t$ for
stack $k$, depth $j$ and the code of the symbol of $c_t$ there, $0$ if there is none, is true
under $a$). Then the cell literals of $c_{t+1}$ hold in row $t + 1$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.cells_step_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1480](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#cells-step-run).

## One-step invariant

Fix an encoding $E$ of a machine $M$ with $K$ stacks, window depth $d$
and $N$ situations, natural numbers $T$, $H$, $t$ with $t < T$ and $d \le H$, an assignment $a$
and an input list $s$, and let $c_t$ be the configuration at time $t$ of the idle-extended run of
$M$ from the start configuration on $s$.
Suppose $a$ satisfies the transition clause families of the layout of $E$ with tables
$(\mathrm{la}, \mathrm{na}, \mathrm{wa})$ and $(\mathrm{la}, \mathrm{sa}, \mathrm{wa})$ and the
cell-shift clause family with tables $(\mathrm{sa}, \mathrm{pl}, \mathrm{cn}, \mathrm{pu})$, all
for time bound $T$, height $H$ and $N$ situations.
Say that a configuration $c$ is tracked in row $t$ when, in the layout of $E$ at height $H$, the
literal of the (label, state) code of $c$ in row $t$ is true under $a$ and, for every stack number
$k < K$ and depth $j < H$, the literal of the cell code of $c$ at stack $k$ and depth $j$ in row
$t$ is true under $a$.
If every stack of $c_t$ has length at most $H - d$ and $c_t$ is tracked in row $t$, then
$c_{t+1}$ is tracked in row $t + 1$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.row_step_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1496](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1496). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#row-step-run).

## One-step invariant at the stack cap

Fix an encoding $E$ of a machine $M$ with $K$ stacks,
window depth $d$ and $N$ situations, natural numbers $m$, $T$, $t$ with $t < T$, an assignment
$a$ and an input list $s$ of length at most $m$. Let $H = m + (T + 1)d + 1$ be the stack cap and
let $c_t$ be the configuration at time $t$ of the idle-extended run of $M$ from the start
configuration on $s$.
Suppose $a$ satisfies the transition clause families of the layout of $E$ with tables
$(\mathrm{la}, \mathrm{na}, \mathrm{wa})$ and $(\mathrm{la}, \mathrm{sa}, \mathrm{wa})$ and the
cell-shift clause family with tables $(\mathrm{sa}, \mathrm{pl}, \mathrm{cn}, \mathrm{pu})$, all
for time bound $T$, height $H$ and $N$ situations.
Say that a configuration $c$ is tracked in row $t$ when, in the layout of $E$ at height $H$, the
literal of the (label, state) code of $c$ in row $t$ is true under $a$ and, for every stack number
$k < K$ and depth $j < H$, the literal of the cell code of $c$ at stack $k$ and depth $j$ in row
$t$ is true under $a$.
If $c_t$ is tracked in row $t$, then $c_{t+1}$ is tracked in row $t + 1$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.row_step_capH`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1508](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#row-step-cap-h).

## Row-0 obligation

For an encoding $E$ of a machine $M$ with $K$ stacks, an assignment $a$, a
height $H$ and an input list $s$, let $c$ be the start configuration of $M$ on $s$. The row-0
obligation says that, in the layout of $E$ at height $H$, the literal of the (label, state) code
of $c$ in row $0$ is true under $a$ and, for every stack number $k < K$ and depth $j < H$, the
literal of the cell code of $c$ at stack $k$ and depth $j$ in row $0$ is true under $a$.

This is a positive form: the literals of the other cell codes are not required to be false.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.Row0`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1531](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#row0).

## Init obligation, input pinned

Let $E$ be an encoding of a machine $M$ with window depth
$d$, let $a$ be an assignment, let $x$ and $Y$ be lists of symbols of the input stack of $M$, and
let $m, T$ be natural numbers, and put $H = m + (T + 1)d + 1$. The init obligation for $a$, $x$,
$Y$, $m$ and $T$ holds when there is a list $y$ of symbols of $Y$ with $|x| + |y| \le m$ such that
the row-0 obligation holds for $a$ at height $H$ and the input $x$ followed by $y$: under $a$, the
code literal of row $0$ and the cell literals of row $0$ at every depth below $H$ are true for the
initial configuration of $M$ on that input.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.InitObl`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1537](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1537). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#init-obl).

## Row-$t$ induction

Fix an encoding $E$ of a machine $M$ with $K$ stacks, window depth $d$
and $N$ situations, natural numbers $T$ and $H$ with $d \le H$, an assignment $a$ and an input list
$s$, and let $c_t$ be the configuration at time $t$ of the idle-extended run of $M$ from the start
configuration on $s$.
Suppose $a$ satisfies the transition clause families of the layout of $E$ with tables
$(\mathrm{la}, \mathrm{na}, \mathrm{wa})$ and $(\mathrm{la}, \mathrm{sa}, \mathrm{wa})$ and the
cell-shift clause family with tables $(\mathrm{sa}, \mathrm{pl}, \mathrm{cn}, \mathrm{pu})$, all
for time bound $T$, height $H$ and $N$ situations.
Say that a configuration $c$ is tracked in row $t$ when, in the layout of $E$ at height $H$, the
literal of the (label, state) code of $c$ in row $t$ is true under $a$ and, for every stack number
$k < K$ and depth $j < H$, the literal of the cell code of $c$ at stack $k$ and depth $j$ in row
$t$ is true under $a$.
If, for every $t < T$, every stack of $c_t$ has length at most $H - d$, and the row-0 obligation
holds for $a$, height $H$ and the input $s$, then $c_t$ is tracked in row $t$ for every
$t \le T$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.rows_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1544](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1544). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#rows-run).

## Row induction at the stack cap

Fix an encoding $E$ of a machine $M$ with $K$ stacks,
window depth $d$ and $N$ situations, natural numbers $m$ and $T$, an assignment $a$ and an input
list $s$ of length at most $m$. Let $H = m + (T + 1)d + 1$ be the stack cap and let $c_t$ be the
configuration at time $t$ of the idle-extended run of $M$ from the start configuration on $s$.
Suppose $a$ satisfies the transition clause families of the layout of $E$ with tables
$(\mathrm{la}, \mathrm{na}, \mathrm{wa})$ and $(\mathrm{la}, \mathrm{sa}, \mathrm{wa})$ and the
cell-shift clause family with tables $(\mathrm{sa}, \mathrm{pl}, \mathrm{cn}, \mathrm{pu})$, all
for time bound $T$, height $H$ and $N$ situations.
Say that a configuration $c$ is tracked in row $t$ when, in the layout of $E$ at height $H$, the
literal of the (label, state) code of $c$ in row $t$ is true under $a$ and, for every stack number
$k < K$ and depth $j < H$, the literal of the cell code of $c$ at stack $k$ and depth $j$ in row
$t$ is true under $a$.
If the row-0 obligation holds for $a$, height $H$ and the input $s$, then $c_t$ is tracked in row
$t$ for every $t \le T$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.rows_capH`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1562](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1562). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#rows-cap-h).

## Run tracking from the init obligation

Fix an encoding $E$ of a machine $M$ with $K$
stacks, window depth $d$ and $N$ situations, lists $x$ and $Y$ of input symbols, natural numbers
$m$ and $T$, and an assignment $a$, and let $H = m + (T + 1)d + 1$ be the stack cap.
Suppose $a$ satisfies the transition clause families of the layout of $E$ with tables
$(\mathrm{la}, \mathrm{na}, \mathrm{wa})$ and $(\mathrm{la}, \mathrm{sa}, \mathrm{wa})$ and the
cell-shift clause family with tables $(\mathrm{sa}, \mathrm{pl}, \mathrm{cn}, \mathrm{pu})$, all
for time bound $T$, height $H$ and $N$ situations.
Say that a configuration $c$ is tracked in row $t$ when, in the layout of $E$ at height $H$, the
literal of the (label, state) code of $c$ in row $t$ is true under $a$ and, for every stack number
$k < K$ and depth $j < H$, the literal of the cell code of $c$ at stack $k$ and depth $j$ in row
$t$ is true under $a$.
If the init obligation holds for $a$, $x$, $Y$, $m$ and $T$, then there is a list $y$ of input
symbols, each occurring in $Y$, such that the concatenation $xy$ has length at most $m$ and, for
every $t \le T$, the configuration at time $t$ of the idle-extended run of $M$ from the start
configuration on $xy$ is tracked in row $t$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.rows_of_init`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1573](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1573). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#rows-of-init).

## Satisfying a concatenation of CNF formulas

For dense CNF formulas $\varphi$ and $\psi$
and a finite bit sequence $a$, $a$ satisfies the concatenation of $\varphi$ and $\psi$ (the
clauses of $\varphi$ followed by those of $\psi$) if and only if $a$ satisfies both $\varphi$ and
$\psi$.

Formalized by `Cslib.Complexity.CookLevin.Situation.cnfSat_append`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1588](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1588). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#cnf-sat-append).

## Positive dense unit clauses force their variable

If an assignment $a$ satisfies a CNF
formula $\varphi$ containing the dense clause over $V$ variables built from the literal list
whose only entry is the pair $(v, \mathrm{true})$, then variable $v$ is true under $a$.

Formalized by `Cslib.Complexity.CookLevin.Situation.unit_force`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1594](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1594). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#unit-force).

## Index of the empty-cell variable of the input stack

For an encoding $E$ and natural numbers
$H$ and $j$, this is the index, in the layout of $E$ at height $H$, of the cell variable for row
$0$, the stack number of the input stack, depth $j$ from the top and symbol code $0$ (the empty
cell).

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.zIdx`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1606](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1606). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#z-idx).

## Start-code clause of the init family

Let $E$ be an encoding of a machine $M$ and let
$T, H$ be natural numbers. The start-code clause is the CNF formula with a single clause: the
dense clause over the $(T + 1)W$ variables of the layout of $E$, where $W$ is its row width at
height $H$, whose only literal is the positive literal of the label/state variable of row $0$ for
the code under $E$ of the pair formed by the main label of $M$ and its initial state.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.initCode`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1609](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#init-code).

## Empty-stack clauses of the init family

Let $E$ be an encoding of a machine $M$ with $K$
numbered stacks and let $T, H$ be natural numbers. The empty-stack clauses form the CNF formula
that lists, for each stack number $k < K$ other than the number of the input stack in increasing
order and, within it, each depth $j < H$ in increasing order, the dense clause over the
$(T + 1)W$ variables of the layout of $E$, where $W$ is its row width at height $H$, whose only
literal is the positive literal of the cell variable of row $0$ for stack $k$, depth $j$ and code
$0$, the empty cell. They ask that every stack other than the input stack be empty in row $0$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.initOther`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1614](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1614). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#init-other).

## Input clauses of the init family

Let $E$ be an encoding of a machine $M$, let
$x = x_0 x_1 \cdots x_{n-1}$ be a list of symbols of the input stack of $M$, and let $T, H$ be
natural numbers. The input clauses form the CNF formula that lists, for $j = 0, 1, \dots, n - 1$
in order, the dense clause over the $(T + 1)W$ variables of the layout of $E$, where $W$ is its
row width at height $H$, whose only literal is the positive literal of the cell variable of row
$0$ for the input stack, depth $j$ and the symbol code under $E$ of $x_j$. They pin the input $x$
at the top of the input stack, one cell at a time.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.initIn`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1619](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1619). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#init-in).

## Certificate clauses of the init family

Let $E$ be an encoding of a machine $M$, let $x$
and $Y$ be lists of symbols of the input stack of $M$, and let $m, T, H$ be natural numbers. For a
depth $j$ and a symbol code $c$, write $C_0[j, c]$ for the cell variable of row $0$, input stack,
depth $j$ and code $c$ in the layout of $E$ at height $H$, and let $e$ be the symbol code of $E$
on the input stack. The certificate clauses form the CNF formula that lists, for each depth
$j = |x|, |x| + 1, \dots, m - 1$ in order (none if $m \le |x|$), the dense clause over the
$(T + 1)W$ variables of the layout, where $W$ is its row width at height $H$, whose literals are
$C_0[j, 0]$ followed by $C_0[j, e(z)]$ for each $z$ in $Y$ in order, all positive.

Code $0$ is the empty cell, so the clause for $j$ asks that depth $j$ of the input stack be empty
or hold a symbol of $Y$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.initCert`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1624](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1624). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#init-cert).

## Prefix clauses of the init family

Let $E$ be an encoding of a machine $M$, let $x$ be a
list of symbols of the input stack of $M$, and let $m, T, H$ be natural numbers. For a depth $j$,
write $Z_j$ for the cell variable of row $0$, input stack, depth $j$ and code $0$ (the empty cell)
in the layout of $E$ at height $H$. The prefix clauses form the CNF formula that lists, for
$j = |x|, |x| + 1, \dots, m - 1$ in order (none if $m \le |x|$), the dense clause over the
$(T + 1)W$ variables of the layout, where $W$ is its row width at height $H$, with the literals
$\neg Z_j$ and $Z_{j+1}$. On these depths, an empty cell forces an empty cell one level deeper.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.initPre`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1630](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1630). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#init-pre).

## Length-bound clauses of the init family

For an encoding $E$ and natural numbers $m$, $T$
and $H$, this is the CNF formula with one clause for each depth $j$ with $m \le j < H$, in
increasing order of $j$: the dense clause over the variables of the transition-clause formula of
the layout of $E$ at bounds $T$ and $H$, built from the single positive literal of the empty-cell
variable of the input stack at depth $j$ in row $0$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.initTail`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1635](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1635). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#init-tail).

## The row-0 init family of an encoding

Let $E$ be an encoding of a machine $M$, let $x$ and
$Y$ be lists of symbols of the input stack of $M$, and let $m, T, H$ be natural numbers. The init
family is the CNF formula whose clauses are, in this order, those of the start-code clause at
$(T, H)$, the empty-stack clauses at $(T, H)$, the input clauses of $x$ at $(T, H)$, the
certificate clauses of $x$ and $Y$ at $(m, T, H)$, the prefix clauses of $x$ at $(m, T, H)$ and
the tail clauses at $(m, T, H)$.

Together they ask that row $0$ hold the start code, empty stacks other than the input stack, the
input $x$ at the top of the input stack, cells that are empty or hold a symbol of $Y$ at the
depths $|x| \le j < m$, with an empty cell at such a depth $j$ forcing an empty cell at $j + 1$,
and empty cells at the depths $m \le j < H$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.initFamily`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1641](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#init-family).

## Init semantics

Fix an encoding $E$ of a machine $M$, lists $x$ and $Y$ of symbols of the
input alphabet, natural numbers $m$, $T$, $H$ with $|x| \le m < H$, and an assignment $a$ that
satisfies the init family of $E$ for $x$, $Y$, $m$, $T$ and $H$. Then there is a list $y$ of
input symbols, each occurring in $Y$, such that the concatenation $xy$ has length at most $m$ and
the row-0 obligation holds for $a$, height $H$ and the input $xy$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.init_row0`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1653](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1653). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#init-row0).

## The init family discharges the init obligation

Let $E$ be an encoding of a machine $M$
with window depth $d$, let $x$ and $Y$ be lists of symbols of the input stack of $M$, and let
$m, T$ be natural numbers with $|x| \le m$, and put $H = m + (T + 1)d + 1$. If an assignment $a$
satisfies the init family of $E$ for $x$, $Y$, $m$, $T$ and $H$, then the init obligation holds
for $a$, $x$, $Y$, $m$ and $T$: there is a list $y$ of symbols of $Y$ with $|x| + |y| \le m$ such
that the row-0 obligation holds for $a$ at height $H$ and the input $x$ followed by $y$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.init_obl`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1735](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1735). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-06/index.html#init-obl-2).

## A satisfying assignment tracks a certified run

Let $E$ be an encoding of a machine $M$
with window depth $d$, let $x$ and $Y$ be lists of symbols of the input stack of $M$, let
$m, T \in \mathbb{N}$ with $|x| \le m$, and let $H = m + (T + 1)d + 1$ be the corrected stack cap.
Write $\mathrm{la}, \mathrm{na}, \mathrm{sa}, \mathrm{wa}, \mathrm{pl}, \mathrm{cn}, \mathrm{pu}$
for the situation tables of $E$ and $N$ for its number of situations. Suppose an assignment $a$
satisfies the following families at bounds $T$ and $H$: the transition clause family of the layout
of $E$ for $N$ situations with tables $\mathrm{la}$, $\mathrm{na}$, $\mathrm{wa}$ (the update
family); the transition clause family for $N$ situations with tables $\mathrm{la}$,
$\mathrm{sa}$, $\mathrm{wa}$ (the S-definition family); the cell-shift clause family for $N$
situations with tables $\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$; and the init
family of $E$ for $x$, $Y$, $m$. Then there is a list $y$ of symbols, each in $Y$, with
$|xy| \le m$ such that for every $t \le T$, if $c_t$ is the configuration after $t$ steps of the
idle-extended run of $M$ from the initial configuration on input $xy$, then under $a$ the variable
of row $t$ for the (label, state) code of $c_t$ is true, and for every stack number $k$ of $E$ and
every depth $j < H$ the variable of row $t$ for stack $k$, depth $j$ and the cell code of $c_t$ at
$(k, j)$ is true.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.rows_of_initFamily`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1742](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1742). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#rows-of-init-family).

## Faithful literal list

A list $\ell$ of literals $(p, b)$, each a variable index
$p \in \mathbb{N}$ with a sign $b$, is faithful for $V \in \mathbb{N}$ when every literal $(p, b)$
of $\ell$ has $p < V$ and the first literal of $\ell$ with index $p$ is $(p, b)$.

Equivalently, every literal of $\ell$ survives into the dense clause over $V$ variables built from
$\ell$: it is in range, and not shadowed by an earlier literal at the same index with the other
sign.

Formalized by `Cslib.Complexity.CookLevin.Situation.Faithful`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1761](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1761). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#faithful).

## Faithful dense clause family

A CNF formula $\varphi$ is a faithful family over $V$
variables when every clause of $\varphi$ is the dense clause over $V$ variables built from some
list of literals that is faithful for $V$.

Formalized by `Cslib.Complexity.CookLevin.Situation.FamOK`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1765](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1765). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#fam-ok).

## Faithful dense clause family with positive literals

A CNF formula $\varphi$ is a faithful
family with positive literals over $V$ variables when every clause of $\varphi$ is the dense clause
over $V$ variables built from some list $\ell$ of literals that is faithful for $V$ and contains a
positive literal $(p, \mathrm{true})$ for some $p$.

Formalized by `Cslib.Complexity.CookLevin.Situation.FamPos`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1769](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1769). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#fam-pos).

## Exact clause semantics

Let $V \in \mathbb{N}$, let $\ell$ be a list of pairs $(p, b)$ of a
variable index $p$ and a sign $b$ that is faithful for $V$, and let $a$ be a list of Booleans.
Then $a$ satisfies the dense clause over $V$ variables built from $\ell$ if and only if some
$(p, b) \in \ell$ has $p < |a|$ and $a_p = b$.

Formalized by `Cslib.Complexity.CookLevin.Situation.clauseSat_iff`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1777](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1777). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#clause-sat-iff).

## The all-true assignment satisfies a faithful clause with a positive literal

Let
$V \in \mathbb{N}$ and let $\ell$ be a list of literals that is faithful for $V$ and contains a
positive literal $(p, \mathrm{true})$. Then the all-true assignment of length $V$ satisfies the
dense clause over $V$ variables built from $\ell$.

Formalized by `Cslib.Complexity.CookLevin.Situation.sat_allTrue`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1834](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1834). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#sat-all-true).

## Variables of rows up to the time bound

Let $L$ be a layout, let $T$, $H$, $t$ and $p$ be
natural numbers with $t \le T$, and let $W$ be the number of variables per time step of $L$ at
height $H$. If $p < (t + 1) W$, then $p$ is less than the number of variables of $L$ for bounds
$T$ and $H$.

Formalized by `Cslib.Complexity.CookLevin.Situation.lt_numVars`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1847](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1847). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#lt-num-vars).

## The init family is faithful with positive literals

Let $E$ be an encoding of a machine
$M$, let $x$ and $Y$ be lists of symbols of the input stack of $M$, and let $m, T, H \in \mathbb{N}$
with $|x| \le m < H$. Let $V$ be the number of variables of the layout of $E$ at bounds $T$ and
$H$. Then every clause of the init family of $E$ for $x$, $Y$, $m$, $T$, $H$ is the dense clause
over $V$ variables built from a list of literals that is faithful for $V$ and contains a positive
literal; that is, the init family is a faithful family with positive literals over $V$ variables.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.init_pos`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1919](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1919). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#init-pos).

## Accepting code

For an encoding $E$ of a finite stack machine $M$, the accepting code is
the (label, state) code that $E$ assigns to the pair of the halted label and the initial state of
$M$, the label and state of a halted configuration as acceptance reads it.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.acode`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1969](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1969). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#acode).

## Accept-code clauses

Let $E$ be an encoding of a finite stack machine $M$ with $A_0$
(label, state) codes, let $c^\ast$ be the code that $E$ assigns to the halted label together with
the initial state of $M$, and let $T, H \in \mathbb{N}$. In the layout of $E$ at height $H$, let
$W$ be the row width, $V = (T + 1)W$ the number of variables, and $X[t, u] = tW + u$ the
label/state variable $u$ at time $t$. The accept-code clauses are the CNF formula listing, for
each $u < A_0$ in increasing order, the dense clause over $V$ variables built from the single
literal $X[T, u]$ if $u = c^\ast$ and $\neg X[T, u]$ otherwise.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.accCode`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1972](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1972). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#acc-code).

## Accept-cell clauses

Let $E$ be an encoding of a finite stack machine $M$ with output
stack $k_1$, $g$ symbol codes and stack numbering $\kappa$, let $\alpha$ be a symbol of stack $k_1$
with code $e$, and let $T, H \in \mathbb{N}$. In the layout of $E$ at height $H$, let $W$ be the
row width, $V = (T + 1)W$ the number of variables, and $C[t, k, j, x]$ the variable for stack $k$,
depth $j$ and symbol code $x$ at time $t$. The accept-cell clauses are the CNF formula listing,
for each $x < g$ in increasing order, the dense clause over $V$ variables built from the single
literal $C[T, \kappa(k_1), 0, x]$ if $x = e$ and $\neg C[T, \kappa(k_1), 0, x]$ otherwise.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.accCell`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1977](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1977). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#acc-cell).

## The accept family

Let $E$ be an encoding of a finite stack machine $M$, let $\alpha$ be a
symbol of the output stack of $M$, and let $T, H \in \mathbb{N}$. The accept family for $\alpha$ at
bounds $T$ and $H$ is the CNF formula formed by the accept-code clauses at $T$ and $H$ followed by
the accept-cell clauses for $\alpha$ at $T$ and $H$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.accFamily`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 1983](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L1983). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#acc-family).

## Accept-code clauses pin the (label, state) code

Let $E$ be an encoding of a finite stack
machine $M$ with $A_0$ (label, state) codes, let $\alpha$ be a symbol of the output stack of $M$,
and let $T, H, u \in \mathbb{N}$ with $u < A_0$. In the layout of $E$ at height $H$, let $X[t, w]$
be the label/state variable $w$ at time $t$, and call a variable $v$ true under an assignment $a$
when $v < |a|$ and $a_v$ is true. If an assignment $a$ satisfies the accept family for $\alpha$
at bounds $T$ and $H$, and $X[T, u]$ is true under $a$, then $u$ is the code that $E$ assigns to
the halted label together with the initial state of $M$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.acc_code`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2004](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2004). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#acc-code-2).

## Accept-cell clauses pin the top output symbol

Let $E$ be an encoding of a finite stack
machine $M$ with output stack $k_1$, $g$ symbol codes and stack numbering $\kappa$, let $\alpha$
be a symbol of stack $k_1$, and let $T, H, x \in \mathbb{N}$ with $x < g$. In the layout of $E$
at height $H$, let $C[t, k, j, z]$ be the variable for stack $k$, depth $j$ and symbol code $z$
at time $t$, and call a variable $v$ true under an assignment $a$ when $v < |a|$ and $a_v$ is
true. If an assignment $a$ satisfies the accept family for $\alpha$ at bounds $T$ and $H$, and
the variable $C[T, \kappa(k_1), 0, x]$ is true under $a$, then $x$ is the code of $\alpha$ for
stack $k_1$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.acc_cell`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2010](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2010). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#acc-cell-2).

## Accepting configuration

A configuration $c$ of a finite stack machine $M$ is accepting
for a symbol $\alpha$ of the output stack of $M$ when $c$ is halted (it has no label), its state
is the initial state of $M$, and the output stack of $c$ is nonempty with top symbol $\alpha$.

This is the shape of the halting configuration with output $[\alpha]$ that acceptance reads.

Formalized by `Cslib.Complexity.CookLevin.Situation.Accepts`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2019](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2019). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#accepts).

## Satisfying assignments yield accepting runs

Let $E$ be an encoding of a finite stack
machine $M$ with input stack $k_0$ and output stack $k_1$, let $x$ and $Y$ be lists of symbols of
$k_0$, let $m, T \in \mathbb{N}$ with $|x| \le m$, and let $\alpha$ be a symbol of $k_1$ that is one
of the effective symbols of $E$ for $k_1$. Put $H = m + (T + 1)d + 1$, where $d$ is the window
depth of $M$, and let $N$ be the number of situations of $E$. Suppose an assignment $a$ satisfies,
at bounds $T$ and $H$, the update family (the transition clause family of the layout of $E$ with
tables $\mathrm{la}, \mathrm{na}, \mathrm{wa}$ and $N$ situations), the S-definition family (the
same with $\mathrm{sa}$ in place of $\mathrm{na}$), the cell-shift family with tables
$\mathrm{sa}, \mathrm{pl}, \mathrm{cn}, \mathrm{pu}$ and $N$ situations, the init family for $x$,
$Y$ and $m$, and the accept family for $\alpha$. Then there is a list $y$ whose entries all occur
in $Y$ such that $|xy| \le m$ and the idle-extended run of $M$ from the initial configuration on
input $xy$ is, after $T$ steps, an accepting configuration for $\alpha$.

Apart from the accept family, no one-hot or at-most-one clauses are assumed.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.accept_sound`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2029](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2029). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#accept-sound).

## No accepting certificate, no satisfying assignment

Let $E$ be an encoding of a machine
$M$ with window depth $d$, let $x$ and $Y$ be lists of symbols of the input stack of $M$, let
$m, T \in \mathbb{N}$ with $|x| \le m$, let $H = m + (T + 1)d + 1$, and let $\alpha$ be a symbol
of the output stack of $M$ in the effective alphabet of $E$. Write
$\mathrm{la}, \mathrm{na}, \mathrm{sa}, \mathrm{wa}, \mathrm{pl}, \mathrm{cn}, \mathrm{pu}$ for
the situation tables of $E$ and $N$ for its number of situations. Suppose that for no list $y$
of symbols, each in $Y$, with $|xy| \le m$, the configuration after $T$ steps of the
idle-extended run of $M$ from the initial configuration on input $xy$ is an accepting
configuration for $\alpha$. Then no assignment satisfies all five of the following families at
bounds $T$ and $H$: the transition clause family of the layout of $E$ for $N$ situations with
tables $\mathrm{la}$, $\mathrm{na}$, $\mathrm{wa}$ (the update family); the transition clause
family for $N$ situations with tables $\mathrm{la}$, $\mathrm{sa}$, $\mathrm{wa}$ (the
S-definition family); the cell-shift clause family for $N$ situations with tables $\mathrm{sa}$,
$\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$; the init family of $E$ for $x$, $Y$, $m$; and the
accept family of $E$ for $\alpha$.

In particular, the all-true assignment does not satisfy all five.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.unsat_of_noAccept`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2065](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2065). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#unsat-of-no-accept).

## The all-true assignment satisfies the transition, shift and init families

Let $E$ be an
encoding of a machine $M$ with window depth $d$, let $x$ and $Y$ be lists of symbols of the input
stack of $M$, and let $m, T, H \in \mathbb{N}$ with $|x| \le m < H$ and $d \le H$. Write
$\mathrm{la}, \mathrm{na}, \mathrm{sa}, \mathrm{wa}, \mathrm{pl}, \mathrm{cn}, \mathrm{pu}$ for the
situation tables of $E$, $N$ for its number of situations and $V$ for the number of variables of
its layout at bounds $T$ and $H$. Then the all-true assignment of length $V$ satisfies each of the
following families at bounds $T$ and $H$: the transition clause family of the layout of $E$ for
$N$ situations with tables $\mathrm{la}$, $\mathrm{na}$, $\mathrm{wa}$ (the update family); the
transition clause family for $N$ situations with tables $\mathrm{la}$, $\mathrm{sa}$,
$\mathrm{wa}$ (the S-definition family); the cell-shift clause family for $N$ situations with
tables $\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$; and the init family of $E$ for
$x$, $Y$, $m$.

Every clause of these families has a positive literal at an index below $V$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.trans_allTrue`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2078](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2078). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#trans-all-true).

## The all-true assignment violates the accept family

Let $E$ be an encoding of a finite
stack machine $M$, let $\alpha$ be a symbol of the output stack of $M$, and let
$T, H \in \mathbb{N}$. The assignment that sets all $V$ variables to true, where $V$ is the number
of variables of the layout of $E$ at bounds $T$ and $H$, does not satisfy the accept family for
$\alpha$ at bounds $T$ and $H$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.accFamily_allTrue`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2096](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2096). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#acc-family-all-true).

## Unfolding the idle-extended run from the front

For a finite TM2 machine $M$, a
configuration $c$ and every $n \in \mathbb{N}$, the configuration at time $n + 1$ of the
idle-extended run of $M$ from $c$ equals the configuration at time $n$ of the idle-extended run
of $M$ from the idle-extended step of $M$ at $c$.

Formalized by `Cslib.Complexity.CookLevin.Situation.runI_succ'`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-07/index.html#run-i-succ).

## The idle-extended run follows the real run

Let $M$ be a finite stack machine, let
$n \in \mathbb{N}$, and let $c, c'$ be configurations of $M$. If iterating the step function of
$M$ $n$ times as a partial function, starting from $c$, yields $c'$, then the idle-extended run
of $M$ from $c$ is at $c'$ after $n$ steps.

Formalized by `Cslib.Complexity.CookLevin.Situation.runI_of_iterate`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#run-i-of-iterate).

## A halted configuration is fixed by the idle-extended run

Let $M$ be a finite stack
machine and $c$ a configuration of $M$ whose label is empty (that is, $c$ has halted). Then for
every $t \in \mathbb{N}$, the idle-extended run of $M$ from $c$ is at $c$ after $t$ steps.

Formalized by `Cslib.Complexity.CookLevin.Situation.runI_halted`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#run-i-halted).

## The idle-extended run stays at the halting configuration

Let $M$ be a machine, $s$ a
word over its input alphabet and $l'$ a list over its output alphabet. Suppose that $M$, started
in the initial configuration on $s$, reaches the halting configuration with output $l'$ (halted,
in the initial state, with $l'$ on the output stack and every other stack empty) in at most $p$
steps. Then for every $T \ge p$, the configuration reached after $T$ steps of the idle-extended
run of $M$ from the initial configuration on $s$ is that halting configuration.

Formalized by `Cslib.Complexity.CookLevin.Situation.runI_haltList`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#run-i-halt-list).

## Acceptance of a halting configuration

Let $M$ be a machine, $l'$ a list over its output
alphabet and $\mathrm{acc}$ an output symbol. The halting configuration with output $l'$ (halted,
in the initial state, with $l'$ on the output stack and every other stack empty) is accepting for
$\mathrm{acc}$ if and only if $l'$ is nonempty and its first element is $\mathrm{acc}$.

Formalized by `Cslib.Complexity.CookLevin.Situation.accepts_haltList`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#accepts-halt-list).

## Uniqueness of quotient and remainder

Let $W$, $t$, $t'$, $r$ and $r'$ be natural
numbers with $r < W$ and $r' < W$. If $tW + r = t'W + r'$, then $t = t'$ and $r = r'$.

Formalized by `Cslib.Complexity.CookLevin.Situation.row_pos_inj`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#row-pos-inj).

## Equal low-order digits give equal residues

Let $b$, $i$, $i'$ and $n$ be natural
numbers. If $\lfloor i / b^e \rfloor \bmod b = \lfloor i' / b^e \rfloor \bmod b$ for every
$e < n$, that is, $i$ and $i'$ have the same first $n$ base-$b$ digits, then
$i \bmod b^n = i' \bmod b^n$.

Formalized by `Cslib.Complexity.CookLevin.Situation.mod_pow_eq_of_digits`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#mod-pow-eq-of-digits).

## Situation injectivity

Let $M$ be a finite stack machine with encoding data $E$, and write
$N$ for the number of situations of $E$, $K$ for the number of stacks of $E$ and $d$ for the
window depth of $M$. Let $c$ be a configuration of $M$ all of whose stack symbols lie in the
effective alphabets of $E$, and let $i < N$. If the label/state code of situation $i$ equals the
(label, state) code of $c$, and for every stack number $k < K$ and every depth $j < d$ the window
code of situation $i$ at stack $k$, depth $j$ equals the cell code of $c$ at stack $k$, depth
$j$, then $i$ is the situation index of $c$.

This is the converse of the fact that the situation index of such a $c$ is below $N$ and has the
code and the windows of $c$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sit_inj`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#sit-inj).

## The real run's literals

Let $M$ be a finite stack machine with encoding data $E$, let $s$
be an input of $M$ and $H \in \mathbb{N}$, and for $t \in \mathbb{N}$ let $c_t$ be the
configuration after $t$ steps of the idle-extended run of $M$ from its start configuration on $s$.
Variable indices are those of the layout of $E$ at height $H$, $K$ is the number of stacks of $E$,
and $A_0$ is the number of (label, state) codes of $E$. An index $p$ is a run literal when, for
some time $t$, it is one of the following: the label/state variable at time $t$ for the
(label, state) code of $c_t$; for some stack number $k < K$ and depth $j < H$, the cell variable
at time $t$ for stack $k$, depth $j$ and the cell code of $c_t$ at stack $k$, depth $j$ (code $0$,
the empty cell, included); or the label/state variable at time $t + 1$ for $A_0 + i$, where $i$
is the situation index of $c_t$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.RunLit`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#run-lit).

## The assignment of the real run's literals

Let $E$ be an encoding of the machine $M$, let
$s$ be a word over the input alphabet, let $T$ and $H$ be natural numbers, and let $V$ be the
number of variables of the transition-clause formula for $T$ and $H$. The assignment is the list
of $V$ truth values whose entry $p$, for each $p < V$, is true exactly when $p$ is one of the
real run's literals of $s$ at height $H$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.runAsg`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#run-asg).

## Faithful clauses with a literal agreeing with the real run are satisfied

Let $M$ be a
finite stack machine with encoding data $E$, let $s$ be an input of $M$, let
$T, H \in \mathbb{N}$, and let $V$ be the number of variables of the layout of $E$ for $T$ and
$H$. Let $\ell$ be a list of literals that is faithful for $V$, and let $(p, b) \in \ell$ be a
literal such that $b$ is true exactly when $p$ is a run literal of $s$ at height $H$. Then the
dense clause over $V$ variables built from $\ell$ is satisfied by the run assignment of $s$ for
$T$ and $H$, which is true exactly on the run literals.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sat_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#sat-run).

## Situation variables lie in the label/state block

Let $E$ be an encoding of a finite TM2
machine with $N$ situations. For every natural number $i < N$, the position of the variable of
situation $i$ is less than the label/state block size $A$ of the clause layout of $E$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sa_lt`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#sa-lt).

## Transition families with a run-literal head are satisfied by the run

Let $E$ be an
encoding of the machine $M$ with layout $L$, $N$ situations, label/state table $\mathrm{la}$ and
window table $\mathrm{wa}$, let $d$ be the window depth of $M$, and let $T, H \in \mathbb{N}$ with
$d \le H$. Write $X[r, x]$ for the index of the label/state variable $x$ of row $r$ at height
$H$. Fix an input list $s$, let $c_t$ be the configuration after $t$ steps of the idle-extended
run of $M$ from the initial configuration on $s$, and let $\nu : \mathbb{N} \to \mathbb{N}$ be a
next-label table such that $\mathrm{la}$, $\nu$ and $\mathrm{wa}$ are well formed for $L$ at
height $H$ for every situation $i < N$. Suppose that for every $t < T$, with $i_t$ the situation
index of $c_t$, the index $X[t + 1, \nu(i_t)]$ is one of the real run's literals of $s$ at
height $H$. Then the assignment of the real run's literals of $s$ for $T$ and $H$ satisfies the
transition clause family of $L$ with the tables $\mathrm{la}$, $\nu$ and $\mathrm{wa}$ for $T$,
$H$ and $N$.

In clause $(t, i)$ the head literal is true when $i$ is the situation index of $c_t$; otherwise
the clause is satisfied by a body literal whose variable is false, by situation injectivity.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.fam_complete`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#fam-complete).

## The run assignment satisfies the update family

Let $M$ be a finite stack machine with
encoding data $E$, let $N$ be the number of situations of $E$, let $s$ be an input of $M$, and
let $T, H \in \mathbb{N}$ with $d \le H$, where $d$ is the window depth of $M$. For
$t \in \mathbb{N}$ let $c_t$ be the configuration after $t$ steps of the idle-extended run of $M$
from its start configuration on $s$, and suppose that for every $t < T$ every stack of $c_t$ has
length at most $H - d$. Then the run assignment of $s$ for $T$ and $H$ (true exactly on the run
literals) satisfies the transition clause family of the layout of $E$ at height $H$, for times
$t < T$ and situations $i < N$, with the tables $\mathrm{la}$, $\mathrm{na}$ and $\mathrm{wa}$
of $E$.

In the clause of the real situation, the head literal is the code of the real next
configuration, by the agreement of the tables with the machine's step.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.upd_complete`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#upd-complete).

## The run assignment satisfies the situation-definition family

Let $M$ be a finite stack
machine with encoding data $E$, let $N$ be the number of situations of $E$, let $s$ be an input
of $M$, and let $T, H \in \mathbb{N}$ with $d \le H$, where $d$ is the window depth of $M$. Then
the run assignment of $s$ for $T$ and $H$ (true exactly on the run literals) satisfies the
transition clause family of the layout of $E$ at height $H$, for times $t < T$ and situations
$i < N$, with the tables $\mathrm{la}$ and $\mathrm{wa}$ of $E$ and with the situation positions
$\mathrm{sa}$ of $E$ in place of the next-label table.

In the clause of the real situation, the head literal is the real situation literal, by the
definition of the run literals.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sdef_complete`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#sdef-complete).

## The run assignment satisfies the cell-shift family

Let $M$ be a finite stack machine
with encoding data $E$, let $N$ be the number of situations of $E$, let $s$ be an input of $M$,
and let $T, H \in \mathbb{N}$ with $d \le H$, where $d$ is the window depth of $M$. For
$t \in \mathbb{N}$ let $c_t$ be the configuration after $t$ steps of the idle-extended run of $M$
from its start configuration on $s$, and suppose that for every $t < T$ every stack of $c_t$ has
length at most $H - d$. Then the run assignment of $s$ for $T$ and $H$ (true exactly on the run
literals) satisfies the cell-shift clause family (shift, overflow and pushed-fill clauses) of the
layout of $E$ with the tables $\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$ of $E$,
for $N$ situations, times $t < T$ and height $H$.

Off the real situation the negated situation literal is true; on it, the target cell of row
$t + 1$ is the one given by the table-driven row update.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.shift_complete`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2407](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#shift-complete).

## Unit clauses on run literals are satisfied

Let $M$ be a finite stack machine with
encoding data $E$, let $s$ be an input of $M$, let $T, H \in \mathbb{N}$, and let $V$ be the
number of variables of the layout of $E$ for $T$ and $H$. If $p < V$ is a run literal of $s$ at
height $H$, then the dense clause over $V$ variables whose only literal is $x_p$ is satisfied by
the run assignment of $s$ for $T$ and $H$, which is true exactly on the run literals.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.sat_unit`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#sat-unit).

## Row-0 cells of the start configuration are run literals

Let $E$ be an encoding of the
machine $M$ with $K$ stacks, let $s$ be a word over the input alphabet, and let $H$, $k$ and $j$
be natural numbers with $k < K$ and $j < H$. Let $x$ be the code of the cell of stack $k$ at
depth $j$ in the initial configuration on $s$. Then the cell variable of time $0$, stack $k$,
depth $j$ and symbol code $x$ at height $H$ is one of the real run's literals of $s$ at
height $H$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.lit_cell0`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2479](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#lit-cell0).

## Completeness of the init family

Let $E$ be an encoding of the machine $M$, let $x$, $y$
and $Y$ be words over the input alphabet such that every letter of $y$ occurs in $Y$, and let
$m$, $T$ and $H$ be natural numbers with $|xy| \le m < H$, where $xy$ is the concatenation. Then
the assignment of the real run's literals of $xy$ for $T$ steps at height $H$ satisfies the init
family (clauses I1 to I6) for $x$, $Y$, $m$, $T$ and $H$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.init_complete`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2489](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#init-complete).

## Completeness of the accept family

Let $E$ be an encoding of the machine $M$, let $s$ be
a word over the input alphabet, let $T$ and $H$ be natural numbers with $H > 0$, and let
$\mathrm{acc}$ be a symbol of the output stack. Suppose that the configuration reached after $T$
steps of the idle-extended run of $M$ from the initial configuration on $s$ is accepting for
$\mathrm{acc}$: it is halted, its state is the initial state of $M$, and $\mathrm{acc}$ is on top
of its output stack. Then the assignment of the real run's literals of $s$ for $T$ steps at
height $H$ satisfies the accept family for $\mathrm{acc}$ at $T$ and $H$, both its positive and
its negated unit clauses.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.acc_complete`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2594](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2594). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#acc-complete).

## Completeness of the five clause families

Let $E$ be an encoding of the machine $M$, let
$x$, $y$ and $Y$ be words over the input alphabet such that every letter of $y$ occurs in $Y$, and
let $m$ and $T$ be natural numbers with $|xy| \le m$, where $xy$ is the concatenation. Let $d$ be
the window depth of $M$, let $H = m + (T + 1)d + 1$ be the stack cap, and let $a$ be the
assignment of the real run's literals of $xy$ for $T$ steps at height $H$. Suppose that the
configuration reached after $T$ steps of the idle-extended run of $M$ from the initial
configuration on $xy$ is accepting for the output symbol $\mathrm{acc}$: it is halted, its state
is the initial state of $M$, and $\mathrm{acc}$ is on top of its output stack. Then the length of
$a$ is the number of variables of the transition-clause formula for $T$ and $H$, and $a$
satisfies each of the following, all for $T$ steps at height $H$: the update family (the
transition clause family with tables $\mathrm{la}$, $\mathrm{na}$, $\mathrm{wa}$ and $N$
situations), the S-definition family (the transition clause family with tables $\mathrm{la}$,
$\mathrm{sa}$, $\mathrm{wa}$ and $N$ situations), the cell-shift family with tables
$\mathrm{sa}$, $\mathrm{pl}$, $\mathrm{cn}$, $\mathrm{pu}$ and $N$ situations, the init family for
$x$, $Y$ and $m$, and the accept family for $\mathrm{acc}$.

No bound $|x| \le m$ and no encodability of $\mathrm{acc}$ is needed in this direction.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.accept_complete`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2617](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2617). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-08/index.html#accept-complete).

## The five Cook–Levin clause families are satisfiable iff some certificate is accepted

Let $E$ be an encoding of the multi-stack machine $M$, with input stack $k_0$, output stack
$k_1$ and window depth $d$. Let $x$ and $Y$ be lists of input symbols, let $m, T \in \mathbb{N}$,
let $\mathrm{acc}$ be an output symbol, and let $H = m + (T + 1)d + 1$ be the stack cap. Suppose
$|x| \le m$ and $\mathrm{acc}$ is one of the effective symbols that $E$ fixes for stack $k_1$.
Then some list $a$ of Booleans satisfies all five of the following CNF formulas, each for $T$
steps and cap $H$: the transition family with tables $\mathrm{la}, \mathrm{na}, \mathrm{wa}$ and
the transition family with tables $\mathrm{la}, \mathrm{sa}, \mathrm{wa}$, both over the layout
of $E$ and its $N$ situations; the cell-shift family over the same layout with tables
$\mathrm{sa}, \mathrm{pl}, \mathrm{cn}, \mathrm{pu}$ and $N$ situations; the init family for $x$,
$Y$ and $m$; and the accept family for $\mathrm{acc}$, if and only if there is a list $y$ of
input symbols, all in $Y$, with $|xy| \le m$ such that the idle-extended run of $M$ from the
initial configuration on input $xy$ is, after $T$ steps, an accepting configuration for
$\mathrm{acc}$: halted, in the initial state, with $\mathrm{acc}$ on top of stack $k_1$.

Formalized by `Cslib.Complexity.CookLevin.Situation.Enc.five_iff`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Situation.lean, line 2637](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Situation.lean#L2637). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/part-09/index.html#five-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cook-Levin: situation tables of a multi-stack machine and the correctness of the formula](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-situation-tables-of-a-multi-stack-mac)
