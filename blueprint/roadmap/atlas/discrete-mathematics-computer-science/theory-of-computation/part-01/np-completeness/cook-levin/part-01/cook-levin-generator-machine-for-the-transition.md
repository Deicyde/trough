---
declaration: section
origin: cited
lean: Cslib.Complexity.CookLevin.Family.Layout, Cslib.Complexity.CookLevin.Family.Layout.rowW, Cslib.Complexity.CookLevin.Family.Layout.numVars, Cslib.Complexity.CookLevin.Family.Layout.xIdx, Cslib.Complexity.CookLevin.Family.Layout.cIdx, Cslib.Complexity.CookLevin.Family.Layout.nLits, Cslib.Complexity.CookLevin.Family.litPos, Cslib.Complexity.CookLevin.Family.lits
statement: formalized
proof: formalized
---

# Cook-Levin: generator machine for the transition clause families

58 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html).

## Draft C3 variable layout

## Variable layout of the transition clauses

A layout consists of four natural numbers
derived from the verifier: the size $A$ of the label/state block of a row, the number $K$ of
stacks, the number $g$ of symbol codes (code $0$ is the empty cell), and the window depth $d$.

Formalized by `Cslib.Complexity.CookLevin.Family.Layout`, a structure declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#layout).

## Variables per time step

For a layout with label/state block size $A$, $K$ stacks and $g$
symbol codes, and a height $H$, the row width is $W = A + K \cdot (H \cdot g)$: the label/state
block of $A$ variables, followed by $K \cdot H \cdot g$ cell variables.

Formalized by `Cslib.Complexity.CookLevin.Family.Layout.rowW`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#row-w).

## Number of variables of the transition-clause formula

For a layout $L$ and bounds $T$
and $H$, the number of variables is $V = (T + 1) \cdot W$, where $W$ is the number of variables
per time step at height $H$.

Formalized by `Cslib.Complexity.CookLevin.Family.Layout.numVars`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#num-vars).

## Index of a label/state variable

For height $H$, time $t$ and $a \in \mathbb{N}$, the
index of label/state variable $a$ at time $t$ is $t \cdot W + a$, where $W$ is the row width
(variables per time step) at height $H$. It is used for $a < A$, the size of the label/state
block.

Formalized by `Cslib.Complexity.CookLevin.Family.Layout.xIdx`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#x-idx).

## Index of a cell variable in the transition-family layout

For a layout $L$ with
label/state block size $A$, $K$ stacks and $g$ symbol codes, and natural numbers $H$, $t$, $k$,
$j$, $x$, the variable for stack $k$, depth $j$ from the top and symbol code $x$ at time $t$ has
index $tW + A + (kH + j)g + x$, where $W = A + KHg$ is the number of variables per time step. It is
meant for $k < K$, $j < H$ and $x < g$ but is defined for all values.

Formalized by `Cslib.Complexity.CookLevin.Family.Layout.cIdx`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#c-idx).

## Number of literals of a transition clause

For a layout $L$ with $KK$ stacks and window
depth $d$, a label-transition clause has $KK \cdot d + 2$ literals: the current label, the
$KK \cdot d$ window cells and the next label.

Formalized by `Cslib.Complexity.CookLevin.Family.Layout.nLits`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#n-lits).

## Position of a literal in a transition clause

Fix a layout with $K$ stacks and window
depth $d$, a height bound $H$, and tables giving for each situation $i$ a current label $a(i)$, a
next label $a'(i)$ and window symbol codes $w(i, k, r)$. The position of literal $j$ of clause
$(t, i)$ is: for $j = 0$, the index of the label/state variable $a(i)$ at time $t$; for
$1 \le j \le Kd$, writing $j - 1 = kd + r$ with $r < d$, the index of the cell variable for stack
$k$, depth $r$ from the top and symbol code $w(i, k, r)$ at time $t$; for $j > Kd$, the index of
the label/state variable $a'(i)$ at time $t + 1$.

The literals of a clause are numbered $0, \dots, Kd + 1$, so the last case is the next label.

Formalized by `Cslib.Complexity.CookLevin.Family.litPos`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#lit-pos).

## Literals of a transition clause

For a layout $L$ with $KK$ stacks and window depth $d$,
tables $la$, $na$, $wa$, a height $H$, a time $t$ and a situation $i$, the literals of clause
$(t, i)$ form the list of pairs $(p_j, b_j)$ for $j = 0, 1, \dots, n - 1$, where
$n = KK \cdot d + 2$ is the number of literals, $p_j$ is the position of literal $j$ of clause
$(t, i)$, and the polarity $b_j$ is true exactly when $j = n - 1$. So every literal is negative
except the last one, the next label.

Formalized by `Cslib.Complexity.CookLevin.Family.lits`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#lits).

## Dense clause from a list of literals

Given $V \in \mathbb{N}$ and a list $\ell$ of pairs
$(p, b)$ of a variable index $p$ and a sign $b$, the dense clause over $V$ variables has, for each
$v < V$, slot $v$ equal to the literal $x_v$ if the first pair in $\ell$ with index $v$ is
$(v, \mathrm{true})$, the literal $\neg x_v$ if it is $(v, \mathrm{false})$, and empty if $\ell$
has no pair with index $v$. Pairs with index at least $V$ are ignored.

Formalized by `Cslib.Complexity.CookLevin.Family.denseClause`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#dense-clause).

## The transition clause family

Fix a layout with label block size $A$, $K$ stacks, $g$
symbol codes and window depth $d$, tables $\mathrm{la}, \mathrm{na} : \mathbb{N} \to \mathbb{N}$
and $\mathrm{wa} : \mathbb{N} \to \mathbb{N} \to \mathbb{N} \to \mathbb{N}$, and
$T, H, N \in \mathbb{N}$. Let $W = A + KHg$, let $X[t, a]$ be the variable $tW + a$, and let
$C[t, k, j, x]$ be the variable $tW + A + (kH + j)g + x$. The family is the CNF formula that
lists, for each time $t < T$ and within it each situation $i < N$, the dense clause over
$(T + 1)W$ variables built from the literal list $\neg X[t, \mathrm{la}(i)]$, then
$\neg C[t, k, j, \mathrm{wa}(i, k, j)]$ for $k < K$ and $j < d$ in lexicographic order, then
$X[t + 1, \mathrm{na}(i)]$.

Formalized by `Cslib.Complexity.CookLevin.Family.family`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#family).

## Gap encoding of a dense clause

For a starting slot $m$, a list $\ell$ of literals
$(p, b)$ (variable index $p$, sign $b$) and a number of variables $V$, the gap encoding of $\ell$
from slot $m$ to $V$ is defined by recursion on $\ell$. For the empty list it is $V - m$ copies of
the absent-slot block $01$. For a list whose first literal is $(p, b)$ and whose remaining literals
form the list $r$, it is $p - m$ copies of $01$, then the two-bit slot encoding of the literal
with sign $b$ (the bit $1$ followed by the negation of $b$), then the gap encoding of $r$ from
slot $p + 1$ to $V$. Subtraction is truncated at $0$.

When the positions in $\ell$ are strictly increasing, at least $m$ and less than $V$, this is the
encoding of the slots $m, \dots, V - 1$ of the dense clause over $V$ variables with literals
$\ell$.

Formalized by `Cslib.Complexity.CookLevin.Family.gapEnc`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#gap-enc).

## Increasing literal positions

For $\mathit{lo}, V \in \mathbb{N}$, a list of literals
$(p_1, b_1), \dots, (p_n, b_n)$ with positions $p_k \in \mathbb{N}$ and signs $b_k$ has increasing
literal positions from $\mathit{lo}$ below $V$ when $\mathit{lo} \le p_1 < p_2 < \dots < p_n < V$;
for the empty list ($n = 0$) the condition is $\mathit{lo} \le V$.

Formalized by `Cslib.Complexity.CookLevin.Family.Inc`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#inc).

## Lowering the lower bound keeps a literal list increasing

For natural numbers
$lo' \le lo$ and $V$ and a list $ls$ of literals, if the positions in $ls$ are strictly
increasing, at least $lo$ and below $V$ (with $lo \le V$ if $ls$ is empty), then the same holds
with $lo'$ in place of $lo$.

Formalized by `Cslib.Complexity.CookLevin.Family.Inc.mono_lo`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#mono-lo).

## Encoding a dense clause block by block

Let $\ell = [(p_1, b_1), \dots, (p_n, b_n)]$ be
a list of literals with $p_1 < p_2 < \dots < p_n < V$. Then the bit encoding of the dense clause
over $V$ variables with literals $\ell$ is the gap encoding of $\ell$ from slot $0$ to $V$,
followed by the clause terminator $00$.

Formalized by `Cslib.Complexity.CookLevin.Family.encodeClause_denseClause`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#encode-clause-dense-clause).

## Shifting the start of a gap encoding

Let $m \le m'$ and let
$\ell = [(p_1, b_1), \dots, (p_n, b_n)]$ be a list of literals with
$m' \le p_1 < \dots < p_n < V$ (if $\ell$ is empty, require $m' \le V$). Then the gap encoding
of $\ell$ from slot $m$ to $V$ is $m' - m$ copies of the absent-slot block $01$ followed by the
gap encoding of $\ell$ from slot $m'$ to $V$.

Formalized by `Cslib.Complexity.CookLevin.Family.gapEnc_shift`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#gap-enc-shift).

## Successor of a number with a non-maximal remainder

Let $c$ and $d$ be natural numbers
with $0 < d$ and $(c \bmod d) + 1 < d$. Then $\lfloor (c + 1) / d \rfloor = \lfloor c / d \rfloor$
and $(c + 1) \bmod d = (c \bmod d) + 1$.

Formalized by `Cslib.Complexity.CookLevin.Family.div_mod_succ_of_lt`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#div-mod-succ-of-lt).

## Increasing literal sequences

Let $f$ assign to each $j \in \mathbb{N}$ a literal
$f(j) = (p_j, b_j)$ with position $p_j \in \mathbb{N}$, and let $m, V \in \mathbb{N}$. Suppose
$p_j < p_{j+1}$ whenever $j + 1 < m$, and $p_j < V$ when $j + 1 = m$. Then for all
$n, a, \mathit{lo} \in \mathbb{N}$ with $a + n = m$ such that $\mathit{lo} \le V$ if $n = 0$ and
$\mathit{lo} \le p_a$ if $n > 0$, the list $f(a), f(a + 1), \dots, f(a + n - 1)$ has increasing
literal positions from $\mathit{lo}$ below $V$.

Formalized by `Cslib.Complexity.CookLevin.Family.inc_of_mono`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#inc-of-mono).

## Well-formed situation tables for the transition clauses

Given a layout with label/state
block size $A$, $K$ stacks, $g$ symbol codes and window depth $d$, a current-code table $\ell$, a
next-code table $\nu$ and a window table $w$, the tables are well formed for situation $i$ at
height $H$ when $\ell(i) < A$, $\nu(i) < A$, $w(i, k, j) < g$ for all $k < K$ and $j < d$, and
$d \le H$.

Formalized by `Cslib.Complexity.CookLevin.Family.WF`, a structure declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#wf).

## Counters of the transition-family generator

The generator for the transition clause
families keeps fifteen unit counters, each on its own stack: $\mathrm{Tn}$, $\mathrm{Ti}$,
$\mathrm{Hs}$, $\mathrm{Gc}$, $\mathrm{HG}$, $\mathrm{Ka}$, $\mathrm{Wc}$, $\mathrm{Vc}$,
$\mathrm{TW}$, $\mathrm{P}$, $\mathrm{Q}$, $\mathrm{tmp}$, $\mathrm{md}$, $\mathrm{c1}$ and
$\mathrm{c2}$.

Formalized by `Cslib.Complexity.CookLevin.Family.CK`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#ck).

## Stacks of the clause-family generator

The stacks of the counter machine over the
generator's counters: one stack of Booleans for the output and one unit counter for each of the
generator's fifteen counters.

Formalized by `Cslib.Complexity.CookLevin.Family.GK`, an abbreviation declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#gk).

## Stack alphabets of the generator

The generator has an output stack and one counter stack
for each of its counter names; the output stack has the alphabet $\{\mathrm{false},
\mathrm{true}\}$ and every counter stack has a one-element alphabet.

Formalized by `Cslib.Complexity.CookLevin.Family.GΓ`, an abbreviation declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#g).

## Stages of the transition-clause generator's precomputation

The control stages of the
precomputation of the transition-clause generator. There are eight plain stages $eg$, $ew$,
$ek$, $dk$, $cp_1$, $cp_2$, $inc$ and $dk_2$, and three families $hg(s)$, $w(s)$ and $v(s)$
indexed by the four stages $s$ of a multiplication site.

Formalized by `Cslib.Complexity.CookLevin.Family.PS`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#ps).

## Stages of the transition-clause generator's literal routine

The control stages of the
routine of the transition-clause generator that emits one literal. There are thirteen plain
stages: two copy stages $cp_1$, $cp_2$ and the stages $ea$, $da$, $eb$, $db$, $ec$, $dec$,
$cmp$, $emL$, $bad$, $slot$ and $dq$; two families $ma(s)$ and $mb(s)$ indexed by the four
stages $s$ of a multiplication site; and two families $r(o)$ and $rB(o)$ indexed by the three
comparison outcomes $o$ (less, equal, greater).

Formalized by `Cslib.Complexity.CookLevin.Family.LS`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#ls).

## Labels of the clause-family generator

For $N, m \in \mathbb{N}$, a label is one of: a
precomputation stage; the head or the tail of the time loop; a stage of the multiplication
routine of a time step; for a situation $i < N$, one of three labels that start clause $i$, a
stage of the routine emitting literal $j$ of clause $i$ for some $j < m$, or the label that
finishes clause $i$; the label that ends a time step; or the final label $\mathsf{done}$, where a
successful run halts. There are finitely many labels; the generator uses $m$ equal to the number
of literals of a clause.

Formalized by `Cslib.Complexity.CookLevin.Family.GL`, an inductive type declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#gl).

## Entry label of a literal routine (transition-clause generator)

Among the labels of the
generator with $N$ situations and $m$ literal numbers, the entry label of literal $j \in \mathbb{N}$
of situation $i < N$ is the first stage of the routine for literal $j$ of situation $i$ when
$j < m$, and the halting label $\mathrm{done}$ when $j \ge m$.

The generator never uses it with $j \ge m$.

Formalized by `Cslib.Complexity.CookLevin.Family.GL.litL`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#lit-l).

## Label after a literal routine in the transition-family generator

Let $N$ be the number
of situations and $m$ the number of literals per clause, let $i < N$ be a situation and $j$ a
natural number. After the routine for literal $j$ of the clause of situation $i$, the generator
moves to the label that emits the leading gap of that clause if $j = 0$. Otherwise it moves to the
first label of the routine for literal $j - 1$ if $j - 1 < m$, and to the halting label if
$j - 1 \ge m$.

Formalized by `Cslib.Complexity.CookLevin.Family.GL.after`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#after).

## Entry label of the clause routine for situation $i$

For $i < N$, the generator label
$\mathrm{e00}_i$ at which the routine emitting the clause of situation $i$ starts; for $i \ge N$,
the end-of-time-step label $\mathrm{dtw}$.

Formalized by `Cslib.Complexity.CookLevin.Family.GL.sitL`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#sit-l).

## Label after a situation clause in the transition-family generator

Let $N$ be the number
of situations. For a natural number $i$, the label the generator moves to after the clause of
situation $i$ is the end-of-time-step label if $i = 0$. Otherwise it is the first label of the
clause routine for situation $i - 1$ if $i - 1 < N$, and the end-of-time-step label again if
$i - 1 \ge N$.

Formalized by `Cslib.Complexity.CookLevin.Family.GL.afterS`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#after-s).

## Stack index of a literal in a transition clause

For a layout with $K$ stacks and window
depth $d$, the stack index $k_A(j)$ of literal $j$ is $\lfloor (j - 1)/d \rfloor$ when
$1 \le j \le Kd$, and $0$ when $j = 0$ or $j > Kd$.

With the row offset $k_B$ and the constant offset $c_i$ of situation $i$, the position of literal
$j$ of clause $(t, i)$ at height $H$ is $tW + k_A(j)\,Hg + k_B(j)\,W + c_i(j)$, where $g$ is the
number of symbol codes and $W$ the number of variables per time step.

Formalized by `Cslib.Complexity.CookLevin.Family.kA`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#k-a).

## Row offset of a literal in a transition clause

For a layout with $K$ stacks and window
depth $d$, the row offset $k_B(j)$ of literal $j$ is $0$ when $j \le Kd$ and $1$ when $j > Kd$.

Among the literals $0, \dots, Kd + 1$ of a transition clause it is $1$ only for the last one,
the next-label literal, which refers to the following time step.

Formalized by `Cslib.Complexity.CookLevin.Family.kB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#k-b).

## Constant offset of a literal position

For a layout with label block size $A$, $K$
stacks, $g$ symbol codes and window depth $d$, and tables $\mathrm{la}, \mathrm{na} : \mathbb{N}
\to \mathbb{N}$ and $\mathrm{wa} : \mathbb{N} \to \mathbb{N} \to \mathbb{N} \to \mathbb{N}$, the
constant part of the position of literal $j$ of situation $i$ is $\mathrm{la}(i)$ if $j = 0$, is
$A + ((j - 1) \bmod d)\,g + \mathrm{wa}(i, \lfloor (j - 1)/d \rfloor, (j - 1) \bmod d)$ if
$1 \le j \le Kd$, and is $\mathrm{na}(i)$ if $j > Kd$.

Formalized by `Cslib.Complexity.CookLevin.Family.cst`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#cst).

## Polarity of a transition-clause literal

For a layout with $K$ stacks and window depth
$d$, a label-transition clause has $n = K d + 2$ literals, and literal $j$ is positive (polarity
$\mathrm{true}$) exactly when $j = n - 1$: only the last (next-code) literal is positive.

Formalized by `Cslib.Complexity.CookLevin.Family.sgn`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#sgn).

## Literal routine of the transition-clause generator

Fix a layout with label/state block
size $A$, $K$ stacks, $g$ symbol codes and window depth $d$, tables $\mathrm{la}$, $\mathrm{na}$,
$\mathrm{wa}$ and a number $N$ of situations, and let $n = Kd + 2$ be the number of literals of a
clause. For a situation $i < N$ and a literal number $j < n$, this assigns a generator instruction
to each stage of the routine that emits literal $j$ of the clause of situation $i$; all stages
named below are stages of this routine, and moving a counter onto targets means popping it until
it is empty and pushing one unit onto every target for each unit popped. Stage $cp_1$ moves
$\mathsf{TW}$ onto $\mathsf{Q}$ and $\mathsf{tmp}$ and goes to $cp_2$, which moves $\mathsf{tmp}$
onto $\mathsf{TW}$ and goes to $ea$. Stage $ea$ pushes $k_A(j)$ units onto $\mathsf{Ka}$, where
$k_A(j)$ is the stack index of literal $j$, and goes to $ma(\mathrm{head})$; the stages $ma(s)$
run the multiplication routine, stage $s$ at $ma(s)$, with multiplier $\mathsf{Ka}$, index
counter $\mathsf{md}$, multiplicand $\mathsf{HG}$, target $\mathsf{Q}$ and scratch
$\mathsf{tmp}$, ending at $da$; and $da$ empties $\mathsf{Ka}$ and goes to $eb$. Stage $eb$
pushes $k_B(j)$ units onto $\mathsf{Ka}$, where $k_B(j)$ is the row offset of literal $j$, and
goes to $mb(\mathrm{head})$; the stages $mb(s)$ run the multiplication routine, stage $s$ at
$mb(s)$, with multiplier $\mathsf{Ka}$, index counter $\mathsf{md}$, multiplicand
$\mathsf{Wc}$, target $\mathsf{Q}$ and scratch $\mathsf{tmp}$, ending at $db$; and $db$ empties
$\mathsf{Ka}$ and goes to $ec$. Stage $ec$ pushes $c_i(j)$ units onto $\mathsf{Q}$, where
$c_i(j)$ is the constant offset of literal $j$ of situation $i$, and goes to $dec$. Stage $dec$
pops $\mathsf{P}$ and goes to $bad$ if $\mathsf{P}$ was empty and to $cmp$ otherwise. Stage
$cmp$ pops $\mathsf{P}$ and then $\mathsf{Q}$, pushing a unit onto $\mathsf{c1}$ if the pop of
$\mathsf{P}$ found one and onto $\mathsf{c2}$ if the pop of $\mathsf{Q}$ found one; it returns
to $cmp$ if both pops found a unit, and otherwise goes to $r(\mathrm{gt})$ if only $\mathsf{P}$
had one, to $r(\mathrm{lt})$ if only $\mathsf{Q}$ had one, and to $r(\mathrm{eq})$ if neither
had one. Stage $r(o)$ moves $\mathsf{c1}$ onto $\mathsf{P}$ and goes to $rB(o)$, which moves
$\mathsf{c2}$ onto $\mathsf{Q}$ and goes to $slot$ if $o = \mathrm{eq}$ and to $emL$ otherwise.
Stage $emL$ prepends $[\mathrm{false}, \mathrm{true}]$ to the output and goes to $dec$, and
stage $bad$ halts. Stage $slot$ prepends the two-bit code $10$ to the output if $j = n - 1$ and
$11$ otherwise, and goes to $dq$, which empties $\mathsf{Q}$ and then goes to the label that
finishes the clause of situation $i$ if $j = 0$, and to the first stage of the routine for
literal $j - 1$ otherwise.

Formalized by `Cslib.Complexity.CookLevin.Family.litP`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#lit-p).

## Generator machine for the transition clause families

Fix a layout $L$ with label/state
block size $A$, $K$ stacks and $g$ symbol codes, tables $\mathrm{la}$, $\mathrm{na}$,
$\mathrm{wa}$, and a number $N$ of situations, and let $n = Kd + 2$ be the number of literals of
a clause, where $d$ is the window depth. The generator is a multi-stack machine with a Boolean
output stack, the unit counters of the generator, and a Boolean internal state; below, moving a
counter onto targets means popping it until it is empty and pushing one unit onto every target
for each unit popped, and each multiplication uses $\mathsf{md}$ as its index counter and
$\mathsf{tmp}$ as scratch. Its precomputation pushes $g$ units on $\mathsf{Gc}$, adds
$\mathsf{Hs} \cdot \mathsf{Gc}$ to $\mathsf{HG}$, pushes $A$ units on $\mathsf{Wc}$, pushes $K$
units on $\mathsf{Ka}$, adds $\mathsf{Ka} \cdot \mathsf{HG}$ to $\mathsf{Wc}$, empties
$\mathsf{Ka}$, moves $\mathsf{Tn}$ onto $\mathsf{Ka}$ and $\mathsf{tmp}$ and then $\mathsf{tmp}$
onto $\mathsf{Tn}$, pushes one unit on $\mathsf{Ka}$, adds $\mathsf{Ka} \cdot \mathsf{Wc}$ to
$\mathsf{Vc}$, empties $\mathsf{Ka}$ and goes to the loop head. At the loop head it pops
$\mathsf{Tn}$; if a unit was popped it pushes a unit on $\mathsf{Ti}$, adds
$\mathsf{Tn} \cdot \mathsf{Wc}$ to $\mathsf{TW}$ and goes to the clause routine of situation
$N - 1$ (to the end of the time step if $N = 0$); if $\mathsf{Tn}$ was empty it moves
$\mathsf{Ti}$ onto $\mathsf{Tn}$ and goes to its final label, where it halts. The clause routine
of situation $i < N$ prepends $[\mathrm{false}, \mathrm{false}]$ to the output, moves
$\mathsf{Vc}$ onto $\mathsf{P}$ and $\mathsf{tmp}$ and then $\mathsf{tmp}$ onto $\mathsf{Vc}$,
runs the literal routines of situation $i$ for literals $n - 1, n - 2, \dots, 0$ in turn, drains
$\mathsf{P}$ while prepending $[\mathrm{false}, \mathrm{true}]$ to the output once per unit, and
goes to the clause routine of situation $i - 1$, or to the end of the time step if $i = 0$. At
the end of a time step it empties $\mathsf{TW}$ and returns to the loop head.

It is meant to be started with $T$ on $\mathsf{Tn}$, $H$ on $\mathsf{Hs}$ and every other
counter empty.

Formalized by `Cslib.Complexity.CookLevin.Family.prog`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#prog).

## The clause-family generator as a finite stack machine

For a layout $L$, tables
$\mathit{la}$, $\mathit{na}$, $\mathit{wa}$ and $N$ situations, the generator program for these
data, bundled as a multi-stack Turing machine with finitely many stacks, labels and states: its
stacks are the generator's stacks (the Boolean output stack and the counters), its input stack is
the time counter and its output stack is the Boolean output stack, its alphabets are the
generator's alphabets, its labels are the generator's labels for $N$ situations and literal
numbers below the number of literals of a clause, execution starts at the first precomputation
stage, and its internal state is a Boolean, initially false.

Formalized by `Cslib.Complexity.CookLevin.Family.genTM`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#gen-tm).

## Scratch counters at rest in the clause-family generator

A counter assignment $F$ of the
generator (a natural number for each of its counters) is at rest when its six scratch counters
$Q$, $K_a$, $\mathit{tmp}$, $\mathit{md}$, $c_1$ and $c_2$ all hold $0$.

Formalized by `Cslib.Complexity.CookLevin.Family.Rest`, a structure declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#rest).

## Run of one literal routine (transition-clause generator)

Let $i < N$ be a situation, $j$
less than the number of literals, and $F$ a counter assignment whose scratch counters $Q$,
$\mathrm{Ka}$, $\mathrm{tmp}$, $\mathrm{md}$, $c_1$, $c_2$ are $0$. Let
$q = F(\mathrm{TW}) + k_A(j) F(\mathrm{HG}) + k_B(j) F(\mathrm{Wc}) + c_i(j)$, where $k_A$, $k_B$
and $c_i(j)$ are the stack index, the row offset and the constant part of the position of literal
$j$, and suppose $F(P) = q + m + 1$ for a natural number $m$. Let $K$ be the number of stacks of
the layout. Then for every output $o$ and every state $v$, the generator runs in at most

$$m(3q + 6) + 2F(\mathrm{TW}) + K(2F(\mathrm{HG}) + 3) + 2K + 2F(\mathrm{Wc}) + 4q + 22$$

steps from the first stage of the routine for literal $j$ of situation $i$, with state $v$,
counters $F$ and output $o$, to the label that follows literal $j$, with state false, counters $F$
except that $P = q$, and output $s\,(01)^m\,o$, where $s$ is the slot code of a literal with
polarity $\mathrm{sgn}(j)$.

Formalized by `Cslib.Complexity.CookLevin.Family.lit_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#lit-run).

## Boundary before a literal of a transition clause

Let $L$ be a layout with $K$ stacks and
window depth $d$, let $la$, $na$, $wa$ be the tables and $T$, $H$, $t$, $i$, $j$ natural numbers. If
$j$ is less than the number $m = Kd + 2$ of literals of a transition clause, this is the position
of literal $j$ of clause $(t, i)$; otherwise it is the number $V$ of variables of $L$ for $T$ and
$H$.

Formalized by `Cslib.Complexity.CookLevin.Family.bnd`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 618](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L618). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#bnd).

## Resting counter values in the transition-family time loop

Let $L$ be a layout with
label/state block size $A$, $K$ stacks and $g$ symbol codes, let $T$, $H$, $t$ be natural numbers,
and write $W = A + KHg$ for the number of variables per time step and $V = (T + 1)W$ for the total
number of variables. Counter values $F$ of the generator are at rest at time $t$ when the scratch
counters $\mathrm{Q}$, $\mathrm{Ka}$, $\mathrm{tmp}$, $\mathrm{md}$, $\mathrm{c1}$, $\mathrm{c2}$
are all $0$, $F(\mathrm{TW}) = tW$, $F(\mathrm{HG}) = Hg$, $F(\mathrm{Wc}) = W$ and
$F(\mathrm{Vc}) = V$.

Formalized by `Cslib.Complexity.CookLevin.Family.Base`, a structure declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 658](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L658). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#base).

## Per-literal time bound of the transition-clause generator

For a layout with label/state
block size $A$, $K$ stacks and $g$ symbol codes, and for $T, H \in \mathbb{N}$, let
$W = A + KHg$ be the number of variables per time step and $V = (T + 1)W$ the number of
variables. The per-literal time bound is $6V + K(2Hg + 3) + 2K + 2W + 22$.

It bounds the steps spent on one literal apart from the loop that emits the gap before it.

Formalized by `Cslib.Complexity.CookLevin.Family.litE`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 668](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L668). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#lit-e).

## Step bound for one clause of the transition-family generator

Let $L$ be a layout with
label/state block size $A$, $K$ stacks, $g$ symbol codes and window depth $d$, and let $T$, $H$ be
natural numbers. With $W = A + KHg$, $V = (T + 1)W$, $m = Kd + 2$ and
$E = 6V + K(2Hg + 3) + 2K + 2W + 22$, the bound is $V(3V + 6) + mE + 3V + 4$.

Formalized by `Cslib.Complexity.CookLevin.Family.clauseB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 672](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L672). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#clause-b).

## Run of the literal routines of a clause (transition-clause generator)

Let $t < T$, let
the tables be well formed for situation $i < N$ at height $H$, and let $F$ be a counter assignment
resting at time $t$: its scratch counters $Q$, $\mathrm{Ka}$, $\mathrm{tmp}$, $\mathrm{md}$, $c_1$,
$c_2$ are $0$, $F(\mathrm{TW}) = tW$, $F(\mathrm{HG}) = Hg$, $F(\mathrm{Wc}) = W$ and
$F(\mathrm{Vc}) = V$, where $g$ is the number of symbol codes of the layout, $W$ is the number of
variables per time step and $V = (T + 1)W$. Let $n$ be the number of literals of a clause. For
$j \le n$ let $b_j$ be the position of literal $j$ of clause $(t, i)$ when $j < n$, and $b_n = V$;
let $e_j$ be the gap encoding of the slots $b_j, \dots, V - 1$ whose literals are those of clause
$(t, i)$ numbered $j$ or more. Then for every output $o$, every $j \le n$ and every state $v$
there is a state $v'$ such that the generator runs in at most $b_j(3V + 6) + jE$ steps, where $E$
is the per-literal time bound, from the label that follows literal $j$ with state $v$, counters
$F$ except that $P = b_j$, and output $e_j\,00\,o$, to the leading-gap stage of situation $i$
with state $v'$, counters $F$ except that $P = b_0$, and output $e_0\,00\,o$.

The label that follows literal $j$ is the routine for literal $j - 1$, or the leading-gap stage
when $j = 0$.

Formalized by `Cslib.Complexity.CookLevin.Family.lits_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 683](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L683). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#lits-run).

## Run of the transition-family generator on one clause

Let $L$ be a layout with tables
$la$, $na$, $wa$, let $N$ be the number of situations, let $T$, $H$, $t$ be natural numbers with
$t < T$, and let $i < N$ be a situation whose tables are well formed at height $H$. Let $F$ be
counter values at rest in the time loop at time $t$ (for $T$ and $H$) with $F(\mathrm{P}) = 0$,
let $o$ be a bit string and $v$ a Boolean machine state. Started at the first label of the clause
routine for situation $i$ with state $v$, counter values $F$ and output stack $o$, the generator
reaches, in at most $C$ steps, the label after the clause of situation $i$ with state false,
counter values $F$, and output stack the encoding of the dense clause over $V$ variables with the
literals of clause $(t, i)$ followed by $o$. Here $V$ is the number of variables of $L$ for $T$
and $H$, and $C$ is the step bound for one whole clause of $L$ for $T$ and $H$.

Formalized by `Cslib.Complexity.CookLevin.Family.clause_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 738](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L738). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#clause-run).

## Encoded transition clauses of one time step

Given a layout $L$, tables
$la, na : \mathbb{N} \to \mathbb{N}$ and
$wa : \mathbb{N} \to \mathbb{N} \to \mathbb{N} \to \mathbb{N}$, and natural numbers $N$, $T$, $H$,
$t$, this is the bit string obtained by concatenating, for $i = 0, 1, \dots, N - 1$ in this order,
the encoding of the dense clause over $V$ variables whose literals are the literals of clause
$(t, i)$, where $V$ is the number of variables of $L$ for $T$ and $H$.

Formalized by `Cslib.Complexity.CookLevin.Family.blk`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 795](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L795). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#blk).

## Time-loop invariant of the transition-family generator

Let $L$ be a layout with
label/state block size $A$, $K$ stacks and $g$ symbol codes, let $T, H \in \mathbb{N}$, and write
$W = A + KHg$ for the number of variables per time step and $V = (T + 1)W$ for the total number of
variables. Counter values $f$ of the generator satisfy the time-loop invariant when the scratch
counters $\mathrm{Q}$, $\mathrm{Ka}$, $\mathrm{tmp}$, $\mathrm{md}$, $\mathrm{c1}$, $\mathrm{c2}$
are all $0$, $f(\mathrm{P}) = 0$, $f(\mathrm{TW}) = 0$, $f(\mathrm{HG}) = Hg$,
$f(\mathrm{Wc}) = W$ and $f(\mathrm{Vc}) = V$.

The counters $\mathrm{Tn}$, $\mathrm{Ti}$, $\mathrm{Hs}$ and $\mathrm{Gc}$ are not constrained.

Formalized by `Cslib.Complexity.CookLevin.Family.LoopP`, a structure declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 824](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L824). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#loop-p).

## Step bound for one time-loop iteration of the transition-family generator

For a layout
$L$ and natural numbers $N$, $T$, $H$, let $W$ be the number of variables per time step of $L$ at
height $H$ and $C$ the step bound for one whole clause of $L$ for $T$ and $H$. The bound is
$T(2W + 3) + TW + T + 3 + NC$.

Formalized by `Cslib.Complexity.CookLevin.Family.bodyB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 832](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L832). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#body-b).

## Step bound for the transition-clause generator's precomputation

For a layout $L$ with
$KK$ stacks and $g$ symbol codes and bounds $T$ and $H$, the bound is
$H (2g + 3) + KK (2Hg + 3) + (T + 1)(2W + 3) + H + 2 KK + 4T + 16$, where $W$ is the number of
variables per time step at height $H$.

Formalized by `Cslib.Complexity.CookLevin.Family.preB`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 836](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L836). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#pre-b).

## Time bound of the generator

For a layout $L$ and $N, T, H \in \mathbb{N}$, the time
bound of the whole generator is $P + T(B + 1) + T + 2$, where $P$ is the time bound of the
precomputation for $L$, $T$ and $H$, and $B$ is the time bound of one iteration of the time loop
for $L$, $N$, $T$ and $H$.

The bound is explicit; that it is at most $C\,(T + H + 1)^5$ for a constant $C$ depending only
on $L$ and $N$ is proved separately.

Formalized by `Cslib.Complexity.CookLevin.Family.genBound`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 841](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L841). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#gen-bound).

## One iteration of the time loop

Let $t < T$, suppose the tables are well formed at height
$H$ for every situation $i < N$, and let $f$ be a counter assignment that satisfies the time-loop
invariant for $T$ and $H$ and has counter $T_n$ equal to $t$. Then for every output word $o$, the
generator started at the head label of the time-step multiplication, with state $\mathrm{true}$,
counters $f$ and output $o$, reaches the time-loop head label with state $\mathrm{false}$, the same
counters $f$ and output $b_t o$ in at most $B$ steps. Here $b_t$ is the concatenation of the
encoded clauses of time step $t$ for situations $0, \dots, N-1$, and $B$ is the time-loop body
bound for $N$, $T$ and $H$.

Formalized by `Cslib.Complexity.CookLevin.Family.time_body`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 845](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L845). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#time-body).

## Generator output after part of the time loop

For a layout $L$, tables $la$, $na$, $wa$,
sizes $N$, $T$, $H$, a number $m$ of iterations and a Boolean list $o$, the output after $m$
iterations is the concatenation, over the $m$ consecutive time steps $s$ starting at $T - m$ in
increasing order, of the encoded clauses of time step $s$, followed by $o$. Here $T - m$ is
truncated subtraction, so for $m \le T$ these are the time steps $T - m, \dots, T - 1$.

Formalized by `Cslib.Complexity.CookLevin.Family.outAfter`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 907](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L907). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#out-after).

## Initial counters of the transition-clause generator

For natural numbers $T$ and $H$,
the initial counter assignment gives the counter $\mathrm{Tn}$ the value $T$, the counter
$\mathrm{Hs}$ the value $H$, and every other counter of the generator the value $0$.

Formalized by `Cslib.Complexity.CookLevin.Family.initF`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 912](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L912). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#init-f).

## Correctness of the clause-family generator, with its explicit time bound

Let $L$ be a
layout, $\mathit{la}, \mathit{na} : \mathbb{N} \to \mathbb{N}$ and
$\mathit{wa} : \mathbb{N}^3 \to \mathbb{N}$ tables, and $N, T, H \in \mathbb{N}$, and suppose the
tables are well formed at height $H$ for every situation $i < N$. Start the generator for $L$,
$\mathit{la}$, $\mathit{na}$, $\mathit{wa}$ and $N$ at its first precomputation stage, in state
false, with $T$ on the time counter and $H$ on the height counter in unary, all other counters
empty, and an arbitrary list $o$ of bits on the output stack. Then within $B(L, N, T, H)$ steps,
where $B$ is the generator's explicit time bound, it reaches its final label $\mathsf{done}$ (not
the error stage of the literal routine, which also halts), in some state, with stacks whose output
stack holds the encoding of the clause family for $L$, $\mathit{la}$, $\mathit{na}$, $\mathit{wa}$,
$T$, $H$ and $N$, followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.Family.gen_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 924](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L924). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#gen-run).

## Correctness of the clause-family generator

Let $L$ be a layout,
$\mathit{la}, \mathit{na} : \mathbb{N} \to \mathbb{N}$ and
$\mathit{wa} : \mathbb{N}^3 \to \mathbb{N}$ tables, and $N, T, H \in \mathbb{N}$, and suppose the
tables are well formed at height $H$ for every situation $i < N$. Start the generator for $L$,
$\mathit{la}$, $\mathit{na}$, $\mathit{wa}$ and $N$ at its first precomputation stage, in state
false, with $T$ on the time counter and $H$ on the height counter in unary, all other counters
empty, and an arbitrary list $o$ of bits on the output stack. Then after finitely many steps it
reaches its final label $\mathsf{done}$ (not the error stage of the literal routine, which also
halts), in some state, with stacks whose output stack holds the encoding of the clause family for
$L$, $\mathit{la}$, $\mathit{na}$, $\mathit{wa}$, $T$, $H$ and $N$, followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.Family.gen_correct`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 1010](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L1010). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#gen-correct).

## Uniform layout

For $k \in \mathbb{N}$, the layout whose label/state block size, number of
stacks, number of symbol codes and window depth are all equal to $k$.

Formalized by `Cslib.Complexity.CookLevin.Family.Layout.uni`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 1023](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L1023). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#uni).

## Uniform bound on the generator's time

For natural numbers $k \ge 1$ and $y \ge 1$, the
explicit time bound of the generator for the layout whose label block size, number of stacks,
number of symbol codes and window depth all equal $k$, with $N = k$ situations and $T = H = y$, is
at most $323\,k^5 y^5$.

Every monomial of the bound is at most $k^5 y^5$, and its coefficients sum to $323$, its value at
$k = y = 1$.

Formalized by `Cslib.Complexity.CookLevin.Family.genBound_uni`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 1033](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L1033). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#gen-bound-uni).

## Constant of the generator's time bound

For a layout $L$ with label/state block size $A$,
$K$ stacks, $g$ symbol codes and window depth $d$, and for $N$ situations, the constant is
$323\,(A + K + g + d + N + 1)^5$.

Formalized by `Cslib.Complexity.CookLevin.Family.genC`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 1051](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L1051). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#gen-c).

## Time-bound polynomial of the clause-family generator

For a layout $L$ and a number $N$
of situations, this is the polynomial $c\,(X + 1)^5$ with natural-number coefficients, where $c$
is the constant of the generator's time bound for $L$ and $N$.

Evaluated at $T + H$ it is $c\,(T + H + 1)^5$, the generator's time bound, in the polynomial form
that polynomial-time computability of a multi-stack machine uses.

Formalized by `Cslib.Complexity.CookLevin.Family.genPoly`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 1063](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L1063). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#gen-poly).

## Polynomial time bound for the clause-family generator

Let $L$ be a layout,
$\mathit{la}, \mathit{na} : \mathbb{N} \to \mathbb{N}$ and
$\mathit{wa} : \mathbb{N}^3 \to \mathbb{N}$ tables, and $N, T, H \in \mathbb{N}$, and suppose the
tables are well formed at height $H$ for every situation $i < N$. Start the generator for $L$,
$\mathit{la}$, $\mathit{na}$, $\mathit{wa}$ and $N$ at its first precomputation stage, in state
false, with $T$ on the time counter and $H$ on the height counter in unary, all other counters
empty, and an arbitrary list $o$ of bits on the output stack. Then within $c\,(T + H + 1)^5$
steps, where $c$ is the constant of the generator's time bound for $L$ and $N$, it reaches its
final label $\mathsf{done}$ (not the error stage of the literal routine, which also halts), in some
state, with stacks whose output stack holds the encoding of the clause family for $L$,
$\mathit{la}$, $\mathit{na}$, $\mathit{wa}$, $T$, $H$ and $N$, followed by $o$.

Formalized by `Cslib.Complexity.CookLevin.Family.gen_time`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Family.lean, line 1070](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Family.lean#L1070). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html#gen-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cook-Levin: generator machine for the transition clause families](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-generator-machine-for-the-transition)
