---
declaration: section
origin: cited
lean: Cslib.Complexity.Path.encodeP, Cslib.Complexity.Path.decodeP, Cslib.Complexity.Path.arc, Cslib.Complexity.Path.pathDec, Cslib.Complexity.Path.initMarks, Cslib.Complexity.Path.markPass, Cslib.Complexity.Path.reachMarks, Cslib.Complexity.Path.pathCheck
statement: formalized
proof: formalized
---

# Graph reachability

63 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html).

## Encoding of a PATH instance

Writing $1$ for true and $0$ for false, the instance with
source $s$, target $t$ and the digraph given by $n$ and the edge list $E$ is encoded as $s$ ones,
a zero, $t$ ones, a zero, then $n$ ones and a zero, followed, for each pair $(u, v)$ of $E$ in
order, by $u$ ones, a zero, $v$ ones and a zero.

Formalized by `Cslib.Complexity.Path.encodeP`, a definition declared in [CSLibExt/Computability/Complexity/Path.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Path.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#encode-p).

## Decoding a PATH instance

Writing $1$ for true and $0$ for false, a bit string $x$ is parsed
by reading a unary number $s$ (a run of ones ended by a zero), then a unary number $t$ from the
rest, then a graph from what remains: a unary number $n$ followed by pairs $(u, v)$ of unary
numbers until the input ends. The result is $(s, t, n, E)$, with $E$ the list of these pairs in
order; there is no result unless the input ends right after $n$ or right after a complete pair.

Formalized by `Cslib.Complexity.Path.decodeP`, a definition declared in [CSLibExt/Computability/Complexity/Path.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Path.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#decode-p).

## Arcs of the PATH digraph

For $n \in \mathbb{N}$ and a list $E$ of pairs of natural
numbers, there is an arc from $u$ to $v$ when the pair $(u, v)$ occurs in $E$, $u < n$ and $v < n$;
listed pairs with an end at least $n$ give no arc.

Formalized by `Cslib.Complexity.Path.arc`, a definition declared in [CSLibExt/Computability/Complexity/Path.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Path.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#arc).

## The PATH problem

PATH is the decision problem that accepts a bit string $x$ exactly when
$x$ is the encoding of some instance $(s, t, n, E)$ with $s < n$, $t < n$ and a sequence
$s = v_0, v_1, \dots, v_k = t$ with $k \ge 0$ such that each $(v_i, v_{i+1})$ is an arc, that is,
a pair listed in $E$ with both ends below $n$.

Formalized by `Cslib.Complexity.Path.pathDec`, a definition declared in [CSLibExt/Computability/Complexity/Path.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Path.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#path-dec).

## Initial marks

For $n, s \in \mathbb{N}$, the initial marks are the list of $n$ booleans
whose entry at position $i < n$ is true exactly when $i = s$; all entries are false when
$s \ge n$.

Formalized by `Cslib.Complexity.Path.initMarks`, a definition declared in [CSLibExt/Computability/Complexity/Path.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Path.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#init-marks).

## One marking pass

Given $n \in \mathbb{N}$, an edge list $E$ and a list $m$ of booleans
(the marks), the pass scans the pairs $(u, v)$ of $E$ in order and, whenever $u < n$, $v < n$
and position $u$ of the current marks is true, sets position $v$ to true. A position beyond the
end of the list counts as false and setting it changes nothing. Marks set earlier in the pass
are seen by later pairs.

Formalized by `Cslib.Complexity.Path.markPass`, a definition declared in [CSLibExt/Computability/Complexity/Path.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Path.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#mark-pass).

## Reach marks

For $n, s \in \mathbb{N}$ and an edge list $E$, the reach marks are obtained
from the initial marks of $s$ among $0, \dots, n - 1$ by applying the marking pass over $E$ with
bound $n$ exactly $n$ times.

Formalized by `Cslib.Complexity.Path.reachMarks`, a definition declared in [CSLibExt/Computability/Complexity/Path.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Path.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#reach-marks).

## The marking algorithm for PATH

On a bit string $x$, the check decodes $x$ as a PATH
instance. If decoding fails it returns false; if it yields $(s, t, n, E)$ it returns true exactly
when $s < n$, $t < n$ and position $t$ of the marks after $n$ marking passes from $s$ over $E$
is true.

Formalized by `Cslib.Complexity.Path.pathCheck`, a definition declared in [CSLibExt/Computability/Complexity/Path.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Path.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#path-check).

## Decoding inverts the PATH instance encoding

For natural numbers $s, t, n$ and a list $E$
of pairs of natural numbers, the PATH instance parser applied to the PATH instance encoding of
$(s, t, n, E)$ succeeds and returns $(s, t, n, E)$.

Formalized by `Cslib.Complexity.Path.decodeP_encodeP`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#decode-p-encode-p).

## The PATH instance parser succeeds exactly on encodings

For a bit string $x$, natural
numbers $s, t, n$ and a list $E$ of pairs of natural numbers, the PATH instance parser applied to
$x$ succeeds with result $(s, t, n, E)$ if and only if $x$ is the PATH instance encoding of
$(s, t, n, E)$.

Formalized by `Cslib.Complexity.Path.decodeP_eq_some`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#decode-p-eq-some).

## The PATH instance encoding is injective

Let $s, t, n, s', t', n'$ be natural numbers and
$E, E'$ lists of pairs of natural numbers. If the PATH instance encodings of $(s, t, n, E)$ and
$(s', t', n', E')$ are equal, then $s = s'$, $t = t'$, $n = n'$ and $E = E'$.

Formalized by `Cslib.Complexity.Path.encodeP_inj`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#encode-p-inj).

## Setting an entry of a boolean list to true

Let $m$ be a list of booleans and $v, w$
natural numbers, and read a position at or beyond the end of a list as $\mathrm{false}$. Set
the entry of $m$ at position $w$ to $\mathrm{true}$, leaving $m$ unchanged if $w$ is not less
than the length of $m$. Then position $v$ of the result holds $\mathrm{true}$ if and only if
position $v$ of $m$ holds $\mathrm{true}$, or $v = w$ and $w$ is less than the length of $m$.

Formalized by `Cslib.Complexity.Path.getD_set_true`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#get-d-set-true).

## The initial marks mark exactly the source, if it is a vertex

Let $n, s, v$ be natural
numbers, and read a position at or beyond the end of a list as $\mathrm{false}$. Position $v$ of
the initial marks for $n$ vertices and source $s$ holds $\mathrm{true}$ if and only if $v < n$
and $v = s$.

Formalized by `Cslib.Complexity.Path.initMarks_getD`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#init-marks-get-d).

## A marking pass preserves the length

Let $n$ be a natural number, $E$ a list of pairs of
natural numbers and $m$ a list of booleans. A marking pass over $E$ for $n$ vertices, applied to
$m$, gives a list of the same length as $m$.

Formalized by `Cslib.Complexity.Path.length_markPass`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#length-mark-pass).

## Marks persist through a pass

Let $n, v \in \mathbb{N}$, let $E$ be a list of pairs of
natural numbers and let $m$ be a list of booleans. If $v < |m|$ and the $v$-th entry of $m$
(counting from $0$) is true, then the same holds for the result of the marking pass of $E$ with
bound $n$ on $m$.

Formalized by `Cslib.Complexity.Path.markPass_mono`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#mark-pass-mono).

## Soundness of a pass

Let $n \in \mathbb{N}$, let $P$ be a property of natural numbers and
let $E$ be a list of pairs of natural numbers such that $P(u)$ implies $P(v)$ whenever
$(u, v) \in E$, $u < n$ and $v < n$. If $m$ is a list of booleans such that $P(v)$ holds for every
$v < |m|$ whose entry in $m$ is true, then $P(v)$ holds for every $v$ whose entry is true in the
result of the marking pass of $E$ with bound $n$ on $m$.

Formalized by `Cslib.Complexity.Path.markPass_sound`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#mark-pass-sound).

## A pass marks the heads of arcs with marked tails

Let $n \in \mathbb{N}$, let $E$ be a
list of pairs of natural numbers and let $m$ be a list of booleans, where $m$ marks $w$ when
$w < |m|$ and the $w$-th entry of $m$ (counting from $0$) is true. If $(u, v) \in E$ with $u < n$
and $v < n$, $v < |m|$ and $m$ marks $u$, then the result of the marking pass of $E$ with bound $n$
on $m$ marks $v$.

Formalized by `Cslib.Complexity.Path.markPass_closed`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#mark-pass-closed).

## Counting true entries of pointwise dominated boolean lists

Let $l_1$ and $l_2$ be lists
of booleans of the same length such that every position holding $\mathrm{true}$ in $l_1$ also
holds $\mathrm{true}$ in $l_2$. Then $l_1$ has at most as many $\mathrm{true}$ entries as $l_2$,
and strictly fewer if $l_1 \ne l_2$.

Formalized by `Cslib.Complexity.Path.count_lt_of_getD_imp`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#count-lt-of-get-d-imp).

## A pass either changes nothing or adds a mark

For every $n \in \mathbb{N}$, every list $E$
of pairs of natural numbers and every list $m$ of booleans, let $m'$ be the result of the marking
pass of $E$ with bound $n$ on $m$. Then $m' = m$, or $m'$ has strictly more entries equal to true
than $m$.

Formalized by `Cslib.Complexity.Path.markPass_eq_or_count_lt`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#mark-pass-eq-or-count-lt).

## Repeated marking passes preserve the length

Let $n$ be a natural number, $E$ a list of
pairs of natural numbers and $m$ a list of booleans. For every natural number $k$, applying $k$
marking passes over $E$ for $n$ vertices to $m$ gives a list of the same length as $m$.

Formalized by `Cslib.Complexity.Path.length_iterate_markPass`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#length-iterate-mark-pass).

## Marks survive repeated passes

Let $n$ and $v$ be natural numbers, $E$ a list of pairs of
natural numbers and $m$ a list of booleans whose position $v$ holds $\mathrm{true}$ (positions at
or beyond the end read as $\mathrm{false}$). Then for every natural number $k$, position $v$
still holds $\mathrm{true}$ after $k$ marking passes over $E$ for $n$ vertices, starting from
$m$.

Formalized by `Cslib.Complexity.Path.iterate_markPass_mono`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#iterate-mark-pass-mono).

## The final marks have one entry per vertex

For natural numbers $n, s$ and a list $E$ of
pairs of natural numbers, the marks after $n$ marking passes over $E$ for $n$ vertices, starting
from the initial marks for source $s$, form a list of length $n$.

Formalized by `Cslib.Complexity.Path.length_reachMarks`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#length-reach-marks).

## Repeated passes reach a fixpoint

Let $n, s \in \mathbb{N}$ with $s < n$ and let $E$ be a
list of pairs of natural numbers. Let $r$ be the list obtained from the initial marks (only $s$
marked among $0, \dots, n - 1$) by $n$ marking passes of $E$ with bound $n$. Then one more
marking pass of $E$ with bound $n$ leaves $r$ unchanged.

Each pass that changes the marks adds at least one mark, the initial marks contain one mark, and
there are at most $n$ marks.

Formalized by `Cslib.Complexity.Path.markPass_reachMarks`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#mark-pass-reach-marks).

## The final marks are exactly the reachable vertices

Let $n, s, t \in \mathbb{N}$ with
$s < n$ and $t < n$, and let $E$ be a list of pairs of natural numbers. Start from the marks on
$0, \dots, n - 1$ in which only $s$ is marked and apply $n$ marking passes of $E$ with bound $n$.
Then $t$ is marked if and only if $t$ is reachable from $s$ in zero or more steps along the arcs
of $E$ below $n$, the pairs $(u, v) \in E$ with $u < n$ and $v < n$.

Formalized by `Cslib.Complexity.Path.reachMarks_getD_iff`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#reach-marks-get-d-iff).

## The marking algorithm decides PATH

For every bit string $x$, the marking algorithm
returns the same answer on $x$ as the decision problem PATH.

Formalized by `Cslib.Complexity.Path.pathDec_eq_pathCheck`, a theorem declared in [CSLibExt/Computability/Complexity/PathCorrect.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathCorrect.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#path-dec-eq-path-check).

## Stacks of the PATH marking machine

The PATH marking machine, run on an instance with
source $s$, target $t$ and $n$ vertices, has eleven stacks: the input stack $X$, the output stack
$O$, the stack $E$ of the edge bits (reversed between passes), the junk stack $J$, the counters
$S$, $T$ and $N$ for $s$, $t$ and $n$ ($N$ counts the passes left), the counters $U$ and $V$ for
the endpoints $u$ and $v$ of an arc, the mark stack $M$ (with the mark of vertex $0$ on top) and
the stack $P$ of parked marks.

Formalized by `Cslib.Complexity.Path.Machine.K`, an inductive type declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#k).

## Stack alphabets of the PATH marking machine

The output stack $O$ of the PATH marking
machine holds Booleans, and every other stack holds symbols of the SAT verifier's symbol
alphabet.

Formalized by `Cslib.Complexity.Path.Machine.Γ`, a definition declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#untitled).

## Labels of the PATH marking machine

For an instance with source $s$, target $t$, $n$
vertices and arcs $(u, v)$, the labels of the PATH marking machine are $\mathsf{rdS}$,
$\mathsf{rdT}$ and $\mathsf{rdN}$ (read $s$, $t$ and $n$); $\mathsf{val0}$, $\mathsf{valU}$ and
$\mathsf{valV}$ (validate the edge list: at a pair, inside $u$, inside $v$); $\mathsf{goS}$ and
$\mathsf{backS}$ (walk to $s$ and set its mark, then restore); $\mathsf{pass}$ (the pass loop),
$\mathsf{ld}$ (reload the edges) and $\mathsf{edge}$ (the edge loop); $\mathsf{rdU}$ and
$\mathsf{rdV}$ (read $u$ and $v$); $\mathsf{go1}$ and, for each bit $b$, $\mathsf{back1}(b)$
(walk to $u$, then restore holding its mark $b$); $\mathsf{go2}$ and $\mathsf{back2}$ (walk to
$v$ and set its mark, then restore); $\mathsf{drV}$ (drain the counter stack $V$);
$\mathsf{goT}$ (walk to $t$ and answer); $\mathsf{bad}$ (answer false); and $\mathsf{done}$
(halt).

Formalized by `Cslib.Complexity.Path.Machine.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#lab).

## Statements of the PATH marking machine

The statements of the multi-stack Turing machine
(TM2) model whose stacks carry the stack alphabets $\Gamma$ of the marking machine, whose labels
are the labels of the marking machine, and whose internal state is a boolean.

Formalized by `Cslib.Complexity.Path.Machine.Stmt`, an abbreviation declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#stmt).

## The counter unit of the PATH marking machine

The unit symbol of the counters of the PATH
marking machine is the clause-end symbol $\mathrm{cl}$ of the SAT verifier's symbol alphabet.

Formalized by `Cslib.Complexity.Path.Machine.one`, an abbreviation declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#one).

## The unary read instruction

Given a stack $d$, an encoding $g$ of bits as symbols of $d$,
a list $ps$ of stack–symbol pairs and labels $\ell$ and $\ell'$, the instruction of the marking
machine that jumps to `bad` if $X$ is empty, and otherwise pops the top of $X$ as a bit $b$ (a
symbol that is not a bit counts as false) and pushes $g(b)$ on $d$; then, if $b$ is true, it
pushes $a$ on $q$ for each pair $(q, a)$ of $ps$, in order, and jumps to $\ell$, and if $b$ is
false it jumps to $\ell'$. Run at its own label $\ell$, it reads a unary number off $X$.

Formalized by `Cslib.Complexity.Path.Machine.readS`, a definition declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#read-s).

## Walk step of the PATH marking machine

Given a counter stack $c$, a label $\ell$ and a
final statement $f$, the walk step pops the top of $c$. If $c$ was nonempty, it goes to $\ell$
after moving the top mark of the marks stack $M$, if there is one, onto the parked stack $P$:
the mark is popped, read as a bit (a symbol that is not a bit reads as false), and pushed on
$P$ as that bit. If $c$ was empty, it runs $f$.

Formalized by `Cslib.Complexity.Path.Machine.walkS`, a definition declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#walk-s).

## Mark-setting step

For a label $\ell$, the statement of the marking machine that pops the
top cell of the mark stack $M$ and, if there was one, pushes the set mark (the bit true) onto $M$
in its place; in either case it then goes to $\ell$.

Formalized by `Cslib.Complexity.Path.Machine.setS`, a definition declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#set-s).

## The marking machine for PATH

The multi-stack machine program whose input lies on the
stack $X$ and whose answer is pushed on the Boolean stack $O$. To read a unary number off $X$ onto
a stack $d$, it pops a bit off $X$ and pushes it on $d$, repeating while the bit is true and
moving on after the first false bit; an empty $X$ jumps to `bad`. To walk along a counter $c$, it
pops units off $c$ one at a time, each time moving the top mark of $M$ (if there is one) onto $P$,
until $c$ is empty. To restore, it moves the bits on top of $P$ back onto $M$ one at a time.

At `rdS`, `rdT` and `rdN` it reads $s$, $t$ and $n$ in turn off $X$ onto $J$, pushing a counter
unit on $S$, $T$ or $N$ respectively for each true bit, and at `rdN` also a cleared mark on $M$;
then it goes to `val0`. At `val0` it goes to `goS` if $X$ is empty, and otherwise reads two unary
numbers off $X$ onto $E$ (at `valU` and `valV`) and returns to `val0`. At `goS` it walks along $S$
and then sets the top mark of $M$ (if any); at `backS` it restores and goes to `pass`. At `pass`
it pops a unit off $N$ and goes to `ld`, or to `goT` if $N$ is empty. At `ld` it moves the bits on
top of $E$ onto $X$, then goes to `edge`. At `edge` it goes to `pass` if $X$ is empty, and
otherwise reads $u$ and $v$ off $X$ onto $E$ (at `rdU` and `rdV`), pushing a counter unit on $U$,
respectively $V$, for each true bit, and then goes to `go1`. At `go1` it walks along $U$ and reads
the top mark $b$ of $M$ (false if there is none); at `back1 b` it restores and goes to `go2` if $b$
is true and to `drV` otherwise. At `go2` it walks along $V$ and sets the top mark of $M$ (if any);
at `back2` it restores and goes to `edge`. At `drV` it empties $V$ and goes to `edge`. At `goT` it
walks along $T$, pushes the top mark of $M$ (false if there is none) on $O$ and goes to `done`. At
`bad` it pushes false on $O$ and goes to `done`. At `done` it halts.

Formalized by `Cslib.Complexity.Path.Machine.prog`, a definition declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#prog).

## Start label of the PATH marking machine

The marking machine for PATH starts at the label
that reads the source vertex $s$, in unary, off the input.

Formalized by `Cslib.Complexity.Path.Machine.start`, a definition declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#start).

## Setting the first mark

For a list of booleans, the list obtained by setting its first
entry: the empty list is left unchanged, and a list $b :: r$ with first entry $b$ and remaining
entries $r$ becomes $\mathrm{true} :: r$.

Formalized by `Cslib.Complexity.Path.Machine.setHead`, a definition declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#set-head).

## Setting an entry by splitting the list

For every list $m$ of booleans and every natural
number $j$, the first $j$ entries of $m$ followed by the remaining entries with their first entry
set to true (the empty list stays empty) equal $m$ with entry $j$ set to true (which is $m$
itself when $j \ge |m|$).

Formalized by `Cslib.Complexity.Path.Machine.take_append_setHead`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#take-append-set-head).

## Reading the mark of vertex $j$

Let $m$ be a list of Boolean marks and $j$ a natural
number. Drop the first $j$ marks of $m$ and write the rest as bit symbols; reading the top symbol
as a bit, with false when there is no top symbol, gives the entry of $m$ at position $j$ (counting
from $0$), or false when $j$ is at least the length of $m$.

Formalized by `Cslib.Complexity.Path.Machine.bitOf_drop`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#bit-of-drop).

## Out-of-range arcs need no guard

Let $m$ be a list of $n$ Boolean marks and let $u$, $v$
be natural numbers; write $m_u$ for the entry of $m$ at position $u$ (counting from $0$), taken to
be false when $u \ge n$. If $u < n$, $v < n$ and $m_u$ is true, set position $v$ of $m$ to true,
and otherwise keep $m$; the result is the same as setting position $v$ of $m$ to true when $m_u$ is
true and keeping $m$ otherwise.

Setting a position $v \ge n$ leaves the list unchanged, so the machine, which reads the mark of $u$
and then sets the mark of $v$, ignores an arc with an end past the last vertex, as the marking
algorithm does.

Formalized by `Cslib.Complexity.Path.Machine.arc_eq`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#arc-eq).

## Initial marks by setting one entry

For all natural numbers $n$ and $s$, setting entry $s$
of the list of $n$ copies of false to true (which changes nothing when $s \ge n$) gives the
initial marks of $n$ vertices from $s$: the list of length $n$ whose entry $i$ is true exactly
when $i = s$.

Formalized by `Cslib.Complexity.Path.Machine.set_replicate`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#set-replicate).

## A cleared mark or nothing reads as cleared

For every decidable proposition $p$, the
optional mark that is a cleared mark (false) when $p$ holds and absent otherwise, read with
default false, is false.

Formalized by `Cslib.Complexity.Path.Machine.getD_ite`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#get-d-ite).

## A pass sets no mark when none is set

For all natural numbers $n$ and $k$ and every list
$es$ of arcs of natural numbers, one pass of the marking algorithm with $n$ vertices over $es$
(Mark Pass) maps the list of $k$ cleared marks to itself.

Formalized by `Cslib.Complexity.Path.Machine.markPass_replicate`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#mark-pass-replicate).

## The marking algorithm reads the mark of the target

If a bit string $x$ parses as a PATH
instance with source $s$, target $t$, $n$ vertices and edge list $es$, then the marking algorithm
on $x$ returns the mark of $t$ in the reach marks of $s$ (the marks after $n$ marking passes over
$es$, starting from the marks on $0, \dots, n - 1$ with only $s$ marked, and none if $s \ge n$),
where a vertex $t \ge n$ counts as unmarked.

So the checks $s < n$ and $t < n$ of the marking algorithm are implied: a vertex $t \ge n$ has no
mark, and for $s \ge n$ every mark stays cleared.

Formalized by `Cslib.Complexity.Path.Machine.pathCheck_eq`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#path-check-eq).

## Agreement off a set of stacks

For a list $A$ of stacks of the marking machine and two
contents $S$, $S'$ of its stacks, $S'$ agrees with $S$ off $A$ when every stack not in $A$ holds
the same list in $S'$ as in $S$.

Formalized by `Cslib.Complexity.Path.Machine.Fr`, a definition declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#fr).

## Frames are reflexive

For every list $A$ of stacks of the marking machine and every
assignment $S$ of contents to its stacks, $S$ agrees with itself off $A$.

Formalized by `Cslib.Complexity.Path.Machine.Fr.refl`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#refl).

## Frames compose

Let $A$, $B$, $C$ be lists of stacks such that every stack in $A$ or in
$B$ is in $C$. If stacks $S_2$ agree with $S_1$ on every stack outside $A$, and $S_3$ agree with
$S_2$ on every stack outside $B$, then $S_3$ agree with $S_1$ on every stack outside $C$.

Formalized by `Cslib.Complexity.Path.Machine.Fr.trans`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#trans).

## Updating a framed stack preserves the frame

Let $A$ be a list of stacks of the PATH
marking machine, and let $S$ and $S'$ be stack contents such that $S'$ agrees with $S$ on every
stack outside $A$. Then for every stack $k \in A$ and every list $l$ over the alphabet of $k$,
the contents obtained from $S'$ by replacing stack $k$ with $l$ still agree with $S$ on every
stack outside $A$.

Formalized by `Cslib.Complexity.Path.Machine.Fr.upd`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#upd).

## The frame of a read

Let $d$ be a stack of the marking machine, $ps$ a list of pairs of a
stack and a symbol, $i$ a natural number, and $S$, $S'$ two contents of the stacks. Suppose every
stack $q$ other than the input $X$ and $d$ holds in $S'$ the list it holds in $S$ with $i$ further
copies of the symbol of the first entry for $q$ in $ps$ pushed on top (and unchanged if $ps$ has
no entry for $q$). Then $S'$ agrees with $S$ on every stack other than $X$, $d$ and the stacks
that have an entry in $ps$.

Formalized by `Cslib.Complexity.Path.Machine.fr_addU`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#fr-add-u).

## Reading a unary number

Let $d$ be a stack other than $X$, let $g$ encode bits as symbols
of $d$, and let $ps$ be a list of stack–symbol pairs whose stacks are distinct and differ from $X$
and $d$. Suppose the instruction of the marking machine at a label $\ell$ is the unary read off
$X$ onto $d$ through $g$ that pushes $ps$ for each true bit, repeats at $\ell$ and continues at
$\ell'$. If $X$ holds, as bit symbols, $k$ true bits, then a false bit, then a bit list $r$, then
in exactly $k + 1$ steps the machine goes from $\ell$, with any flag, to $\ell'$; afterwards $X$
holds $r$, $d$ has received $k$ copies of $g(\mathrm{true})$ and then $g(\mathrm{false})$ on top,
each stack $q$ with a pair $(q, a)$ in $ps$ has received $k$ copies of $a$ on top, and every
other stack is unchanged.

Formalized by `Cslib.Complexity.Path.Machine.readS_some`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#read-s-some).

## Reading a cut-off unary number

Let $d$ be a stack other than $X$ and $O$, let $g$ encode
bits as symbols of $d$, and let $ps$ be a list of stack–symbol pairs whose stacks are distinct and
differ from $X$ and $O$. Suppose the instruction of the marking machine at a label $\ell$ is the
unary read off $X$ onto $d$ through $g$ that pushes $ps$ for each true bit, repeats at $\ell$ and
continues at $\ell'$. If a bit list $l$ has no unary length prefix (every bit of $l$ is true) and
$X$ holds $l$ as bit symbols, then from $\ell$, with any flag, the machine reaches the label `bad`
within $|l| + 1$ steps, leaving the output stack $O$ unchanged.

Formalized by `Cslib.Complexity.Path.Machine.readS_none`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#read-s-none).

## Restoring the parked marks

Suppose the instruction of the marking machine at a label
$\ell$ moves the bits on top of $P$ onto $M$ one at a time, repeating at $\ell$ and continuing at
$\ell'$ once $P$ is empty or its top is not a bit. If $P$ holds the reverse of a bit list $p$ and
$M$ holds a bit list $q$, both as bit symbols, then in exactly $|p| + 1$ steps the machine goes
from $\ell$, with any flag, to $\ell'$, leaving $P$ empty, $M$ holding $p$ followed by $q$, and
every other stack unchanged.

Formalized by `Cslib.Complexity.Path.Machine.restore_run`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#restore-run).

## A walk step with an exhausted counter

Let $c$ be a stack, $\mathit{self}$ a label,
$\mathit{fin}$ a statement and $S$ stacks in which $c$ is empty. For every internal state $v$,
executing from $v$ and $S$ the walk step counted by $c$ that loops at $\mathit{self}$ and
finishes with $\mathit{fin}$ gives the same result as executing $\mathit{fin}$ from internal
state false and the same stacks $S$.

Formalized by `Cslib.Complexity.Path.Machine.stepAux_walkS_nil`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#step-aux-walk-s-nil).

## Walking along the marks of the PATH marking machine

Let $c$ be a stack other than the
marks stack $M$ and the parked stack $P$, let $u$ be a symbol of the alphabet of $c$, and let
$\ell$ be a label at which the program is the walk step counted by $c$ that returns to $\ell$
(with some final statement). Let $j$ be a natural number, $p$ and $q$ lists of bits, $v$ a
Boolean, and $S$ stack contents in which $c$ holds exactly $j$ copies of $u$, $M$ holds $q$ as
bit symbols, and $P$ holds the reverse of $p$ as bit symbols. Then there are a Boolean $v'$ and
stack contents $S'$ such that the machine goes in exactly $j$ steps from label $\ell$ with state
$v$ and stacks $S$ to label $\ell$ with state $v'$ and stacks $S'$, where $c$ is empty in $S'$,
$M$ holds $q$ with its first $j$ entries dropped, $P$ holds the reverse of the concatenation of
$p$ with the first $j$ entries of $q$, all as bit symbols, and $S'$ agrees with $S$ on every
stack other than $c$, $M$ and $P$.

Formalized by `Cslib.Complexity.Path.Machine.walk_run`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#walk-run).

## Effect of the mark-setting step

Let $\ell$ be a label, $v$ an internal state and $S$
stacks whose mark stack $M$ holds the bits of a list $l$ of booleans. Executing the mark-setting
step to $\ell$ from internal state $v$ and stacks $S$ ends at label $\ell$ with some internal
state and the stacks $S$ with $M$ replaced by the bits of $l$ with its first entry set to true
(the empty list stays empty); every other stack is unchanged.

Formalized by `Cslib.Complexity.Path.Machine.stepAux_setS`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#step-aux-set-s).

## Walking to a vertex and setting its mark

Let $c$ be a stack other than the mark stack $M$
and the parking stack $P$, and let $\mathit{self}$, $\mathit{back}$, $\mathit{next}$ be labels
such that the marking machine at $\mathit{self}$ is the walk step counted by $c$ that loops at
$\mathit{self}$ and finishes with the mark-setting step to $\mathit{back}$, and at
$\mathit{back}$ it moves the bit block of $P$ onto $M$, looping at $\mathit{back}$ and then
going to $\mathit{next}$. Let $S$ be stacks in which $c$ holds the counter value $j$ (for some
unit symbol), $M$ holds the bits of a list $m$ of booleans, and $P$ is empty. Then from label
$\mathit{self}$ with stacks $S$ and any internal state, the machine reaches label
$\mathit{next}$ in at most $2j + 2$ steps, with some internal state and stacks $S'$ such that
$c$ and $P$ are empty, $M$ holds the bits of $m$ with entry $j$ set to true (unchanged when
$j \ge |m|$), and $S'$ agrees with $S$ on every stack other than $c$, $M$ and $P$.

Formalized by `Cslib.Complexity.Path.Machine.setW_run`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#set-w-run).

## Reading the mark of a vertex

Let $u \in \mathbb{N}$ and let $m$ be a list of marks.
Start the marking machine at the label `go1`, with any flag, from stacks on which $U$ holds $u$
counter units, $M$ holds $m$ as bit symbols and $P$ is empty. Then within $2u + 2$ steps it
reaches `go2` if the mark of vertex $u$ in $m$ is set and `drV` otherwise (a vertex past the end
of $m$ counts as unmarked), with $U$ and $P$ empty, $M$ holding $m$ again, and every other
stack unchanged.

Formalized by `Cslib.Complexity.Path.Machine.readW_run`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#read-w-run).

## Validation phase of the PATH marking machine

Let $w$ be a list of bits, $v$ a Boolean
and $S$ stack contents whose input stack $X$ holds $w$ as bit symbols. Then there are a Boolean
$v'$ and stack contents $S'$ such that, in at most $2|w| + 1$ steps, the machine goes from the
validation label (at a pair) with state $v$ and stacks $S$ to state $v'$ and stacks $S'$ at the
label that walks to the source vertex if $w$ decodes as an edge list, and at the label that
answers false otherwise. The output stack $O$ of $S'$ equals that of $S$. Moreover, if $w$
decodes as an edge list, then $X$ is empty in $S'$, the edge stack $E$ of $S'$ is the reverse
of $w$ as bit symbols followed by the old contents of $E$, and $S'$ agrees with $S$ on every
stack other than $X$ and $E$.

Formalized by `Cslib.Complexity.Path.Machine.val_run`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#val-run).

## The edge loop of a pass

Let $n$ be a natural number, $es$ a list of arcs $(u, w)$ of
natural numbers and $m$ a list of $n$ Boolean marks. Encode an arc $(u, w)$ by $u$ ones, a zero,
$w$ ones and a zero, and $es$ by the concatenation of the codes of its arcs; let $\ell$ be the
length of this code. Suppose the marking machine is at the edge-loop label, in any internal state,
with stacks $S$ such that the input stack $X$ holds the code of $es$ and the mark stack $M$ holds
$m$ (vertex $0$ on top), as bit symbols, and the parked-mark stack $P$ and the arc counters $U$
and $V$ are empty. Then within $4\ell + 1$ steps it reaches the pass-loop label with stacks $S'$
in which $X$ is empty, the edge stack $E$ holds the code of $es$ in reverse order on top of its
contents in $S$, $M$ holds the marks that one pass of the marking algorithm with $n$ vertices over
$es$ (Mark Pass) produces from $m$, and $P$, $U$, $V$ are empty; every stack other than $X$, $E$,
$M$, $U$, $V$ and $P$ holds the same list in $S'$ as in $S$.

Formalized by `Cslib.Complexity.Path.Machine.edges_run`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#edges-run).

## The pass loop of the marking machine

Let $n, k \in \mathbb{N}$, let $es$ be a list of
pairs of natural numbers with edge bits $b$, and let $m$ be a list of $n$ marks. Start the marking
machine at the label `pass`, with any flag, from stacks on which $N$ holds $k$ counter units, $X$,
$P$, $U$ and $V$ are empty, $E$ holds the reverse of $b$ and $M$ holds $m$, both as bit symbols.
Then within $k(5|b| + 3) + 1$ steps the machine reaches the label `goT`, with $M$ holding
$p^k(m)$ as bit symbols, where $p$ is one marking pass over $es$ on $n$ vertices, with $P$ empty,
and with every stack other than $N$, $X$, $E$, $M$, $U$, $V$ and $P$ unchanged.

Formalized by `Cslib.Complexity.Path.Machine.passes_run`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#passes-run).

## Running time and output of the marking machine

For every bit string $x$, the marking
machine started at its start label, with any flag, with $x$ on the input stack $X$ as bit symbols
and every other stack empty, reaches the label `done` within $8(|x| + 1)^4$ steps, with the
output stack $O$ holding exactly one entry: the answer of the marking algorithm on $x$.

Formalized by `Cslib.Complexity.Path.Machine.run`, a theorem declared in [CSLibExt/Computability/Complexity/PathMachine.lean, line 559](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathMachine.lean#L559). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#run).

## The marking machine as a host component

The component machine whose stack indices,
stack alphabets, labels and program are those of the marking machine, with its eleven stacks
listed once each, in the order: input, output, edge bits, junk, the counters for the source, the
target and the number of vertices, the counters for the two ends of an arc, the marks and the
parked marks.

Formalized by `Cslib.Complexity.Path.pathComp`, an abbreviation declared in [CSLibExt/Computability/Complexity/PathInP.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathInP.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#path-comp).

## The marking algorithm is polynomial-time

The marking algorithm for PATH, as a function
from bit strings to booleans, is computable in polynomial time by a Turing machine with respect
to the canonical bitstring encodings of lists of booleans and of booleans.

Formalized by `Cslib.Complexity.Path.isPolyTime_pathCheck`, a theorem declared in [CSLibExt/Computability/Complexity/PathInP.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathInP.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#is-poly-time-path-check).

## PATH ∈ P

**PATH ∈ P** (Sipser, Theorem 7.14). The decision problem PATH belongs to the class P of
decision problems decidable in polynomial time. Here PATH accepts a bit string exactly when it
encodes natural numbers $s$, $t$, $n$ and a list $E$ of pairs of natural numbers such that
$s < n$, $t < n$ and $t$ is reachable from $s$ in zero or more steps along the arcs of $E$ below
$n$, the pairs $(u, v) \in E$ with $u < n$ and $v < n$.

Formalized by `Cslib.Complexity.Path.pathDec_mem_P`, a theorem declared in [CSLibExt/Computability/Complexity/PathInP.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PathInP.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html#path-dec-mem-p).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graph reachability](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/polynomial-time-problems/graph-reachability)
