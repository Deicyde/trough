---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.Hastad.hastadNondegenerate, MetaMathlibExt.Complexity.KeyTheorems.Hastad.hastadVal, MetaMathlibExt.Complexity.KeyTheorems.Hastad.hastadOpt, MetaMathlibExt.Complexity.KeyTheorems.Hastad.hastad_max3sat_inapproximability, MetaMathlibExt.Complexity.KeyTheorems.MaxThreeSATMAXSNPComplete.max3SATVal, MetaMathlibExt.Complexity.KeyTheorems.MaxThreeSATMAXSNPComplete.NPOProblem, MetaMathlibExt.Complexity.KeyTheorems.MaxThreeSATMAXSNPComplete.optVal, MetaMathlibExt.Complexity.KeyTheorems.MaxThreeSATMAXSNPComplete.APX
statement: formalized
---

# Approximability of MAX-3SAT

12 results, 10 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat/index.html).

## Nondegenerate 3-clauses

A clause, given as a list of literals $(v, s)$ with variable
index $v \in \mathbb{N}$ and polarity $s$, is nondegenerate if it has exactly three literals,
its variable indices are pairwise distinct, and it contains no complementary pair, that is, no
two literals $(v, s)$ and $(v, \lnot s)$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Hastad.hastadNondegenerate`, a definition declared in [WantedExt/Complexity/KeyTheorems/HastadWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/HastadWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat/index.html#hastad-nondegenerate).

## Value of a MAX-3SAT assignment

For bitstrings $x$ and $a$, read $a$ as the assignment
giving variable $v$ the value $a_v$ if $v < |a|$ and false otherwise. If $x$ decodes, under the
canonical bitstring decoding, to a pair $(u, \varphi)$ of a bitstring $u$ and a CNF formula
$\varphi$ in which every variable index is less than $|u|$ and every clause is nondegenerate,
then the MAX-3SAT value of $a$ on $x$ is the number of clauses of $\varphi$, counted with
multiplicity, that contain a literal $(v, s)$ whose variable gets the value $s$. Otherwise the
value is $0$.

The bitstring $u$ gives the number of variables in unary. Since degenerate and malformed
instances get value $0$, the $7/8$ random-assignment bound holds on every instance with nonzero
value.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Hastad.hastadVal`, a definition declared in [WantedExt/Complexity/KeyTheorems/HastadWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/HastadWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat/index.html#hastad-val).

## Optimum of a MAX-3SAT instance

The MAX-3SAT optimum of a bitstring $x$ is the maximum,
over all bitstrings $a$ of length $|x|$, of the MAX-3SAT value of $a$ on $x$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Hastad.hastadOpt`, a definition declared in [WantedExt/Complexity/KeyTheorems/HastadWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/HastadWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat/index.html#hastad-opt).

## Hastad: optimal inapproximability of MAX-3SAT

If $\mathsf{P} \ne \mathsf{NP}$, then for
every rational $\varepsilon > 0$ there is no polynomial-time function $A$ from bitstrings to
bitstrings such that, for every bitstring $x$, the bitstring $A(x)$ has the same length as $x$
and the MAX-3SAT value of the assignment $A(x)$ on $x$ is at least $(7/8 + \varepsilon)$ times
the MAX-3SAT optimum of $x$.

## Sources

- J. Håstad, "Some optimal inapproximability results", Journal of the ACM 48 (2001), 798-859 (STOC 1997).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.Hastad.hastad_max3sat_inapproximability` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/HastadWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/HastadWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat/index.html#hastad-max3sat-inapproximability).

## The MAX-3SAT objective

The value of MAX-3SAT on an instance $x$ under an assignment $a$,
both bitstrings, is defined as follows. Suppose $x$ decodes, under the canonical bitstring
encoding, to a pair $(u, \varphi)$ of a bitstring $u$ and a CNF formula $\varphi$, and suppose
moreover that $|a| \le |x|$, that every literal of $\varphi$ has variable index less than $|u|$
and that every clause of $\varphi$ has at most $3$ literals. Then the value is the number of
clauses of $\varphi$, counted with multiplicity, that contain a literal $(v, b)$ with $a_v = b$,
where $a_v$ is the bit of $a$ at position $v$ (counting from $0$), read as false when
$v \ge |a|$. In every other case the value is $0$.

The length of $u$ is the number of variables, so the value reads only $a_v$ for $v < |u|$:
padding an assignment with trailing false bits, or padding an assignment of length at least
$|u|$ with arbitrary trailing bits, does not change its value as long as its length stays at
most $|x|$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MaxThreeSATMAXSNPComplete.max3SATVal`, a definition declared in [WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat/index.html#max3-satval).

## NPO problems

An NPO (NP optimization) problem consists of a rational-valued value
function $v$, a Boolean feasibility predicate $F$ and an objective encoding $e$, each taking an
instance $x$ and a solution $s$ (both bitstrings), together with a polynomial $b$ with
natural-number coefficients, such that the following hold. $F$ and $e$ are polynomial-time
computable. For all $x$ and $s$, $e(x, s)$ is a triple $(\sigma, p, q)$ of a Boolean $\sigma$
and natural numbers $p$ and $q$ with $q \ne 0$; if $s$ is feasible for $x$ (that is,
$F(x, s)$ is true), then $v(x, s) = -p/q$ when $\sigma$ is true and $v(x, s) = p/q$ when
$\sigma$ is false, and otherwise $v(x, s) = 0$; and $v(x, s) \ge 0$. Every feasible solution
$s$ for $x$ has $|s| \le b(|x|)$, and every instance $x$ has a feasible solution.

Feasible solutions on every instance are needed for completeness: an L-reduction to a problem
with no feasible solutions on some instance would have to map a feasible target output back to
a feasible source solution that does not exist.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MaxThreeSATMAXSNPComplete.NPOProblem`, a structure declared in [WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat/index.html#npoproblem).

## Optimum of an NPO problem

The optimum of an NPO problem $M$, with value function $v$ and
solution length bound $b$, on an instance $x$ is the maximum of $v(x, s)$ over all bitstrings $s$
with $|s| \le b(|x|)$.

Since every feasible solution has length at most $b(|x|)$, every instance has a feasible
solution, and $v$ is nonnegative and equals $0$ on infeasible solutions, this is the maximum of
$v(x, s)$ over the feasible solutions $s$ for $x$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MaxThreeSATMAXSNPComplete.optVal`, a definition declared in [WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat/index.html#opt-val).

## Membership in APX

An NPO problem $M$ is in APX when there are a rational number
$\rho \ge 1$ and a polynomial-time computable map $A$ from bitstrings to bitstrings such that, for
every instance $x$, the solution $A(x)$ is feasible for $x$ in $M$ and its value is at least
$\mathrm{opt}_M(x) / \rho$, where $\mathrm{opt}_M(x)$ is the optimum of $M$ on $x$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MaxThreeSATMAXSNPComplete.APX`, a definition declared in [WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat/index.html#apx).

## L-reductions

Write $\mathrm{opt}_M(x)$ for the optimum of an NPO problem $M$ on an
instance $x$ and $v_M(x, s)$ for the value of a solution $s$ for $x$. An NPO problem $M_1$
L-reduces to an NPO problem $M_2$ when there are polynomial-time computable maps $f$, from
bitstrings to bitstrings, and $g$, from pairs of bitstrings to bitstrings, and rational numbers
$\alpha > 0$ and $\beta > 0$, such that for every instance $x$ the following hold. First,
$\mathrm{opt}_{M_2}(f(x)) \le \alpha \, \mathrm{opt}_{M_1}(x)$. Second, for every solution $s$
that is feasible for $f(x)$ in $M_2$, the solution $g(x, s)$ is feasible for $x$ in $M_1$ and
$\mathrm{opt}_{M_1}(x) - v_{M_1}(x, g(x, s)) \le
\beta \, (\mathrm{opt}_{M_2}(f(x)) - v_{M_2}(f(x), s))$.

This is the L-reduction of Papadimitriou and Yannakakis, with polynomial-time maps $f$ and $g$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MaxThreeSATMAXSNPComplete.LReduces`, a definition declared in [WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat/index.html#lreduces).

## MAXSNP problems

A MAXSNP problem, in the normal form of Papadimitriou and
Yannakakis, is an NPO problem $M$, with value function $v$ and solution length bound $b$,
together with natural numbers $k$ and $N$, a polynomial-time computable map $W$ sending each
instance $x$ to a list $W(x)$ of windows, each a pair $(w, j)$ of a list
$w = (w_1, \dots, w_m)$ of natural numbers (variable indices) and a natural number $j$ (a
pattern index), and a function $\mathrm{acc}$ assigning a truth value to each pair of a natural
number and a bitstring, such that the following hold. There is a polynomial $q$ with
natural-number coefficients such that $W(x)$ has at most $q(|x|)$ entries for every instance
$x$. Every window $(w, j)$ in $W(x)$ has $|w| \le k$ and $j < N$. A bitstring $s$ is a feasible
solution for $x$ exactly when $|s| \le b(|x|)$. For every feasible solution $s$ for $x$, the
value $v(x, s)$ is the number of entries $(w, j)$ of the list $W(x)$, counted with
multiplicity, for which $\mathrm{acc}(j, (s_{w_1}, \dots, s_{w_m}))$ is true, where $s_i$ is
the bit of $s$ at position $i$ (counting from $0$), read as false when $i \ge |s|$.

The windows depend only on the instance, never on the candidate solution: only the fixed
predicate $\mathrm{acc}$ inspects bits of the solution. The counting equation is required only
for feasible solutions, because padding a solution with false bits preserves the window count
while sufficiently long paddings are infeasible.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MaxThreeSATMAXSNPComplete.MAXSNPProblem`, a structure declared in [WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat/index.html#maxsnpproblem).

## MAXSNP-completeness

A MAXSNP problem $M$ is MAXSNP-complete when its underlying NPO
problem is in APX and, for every MAXSNP problem $M'$, the underlying NPO problem of $M'$
L-reduces to the underlying NPO problem of $M$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MaxThreeSATMAXSNPComplete.MAXSNPComplete`, a definition declared in [WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat/index.html#maxsnpcomplete).

## MAX-3SAT is MAXSNP-complete

There is a MAXSNP problem whose value function is the
MAX-3SAT value function and which is MAXSNP-complete: its underlying NPO problem is in APX, and
the underlying NPO problem of every MAXSNP problem L-reduces to it.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.MaxThreeSATMAXSNPComplete.max_three_sat_maxsnp_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MaxThreeSATMAXSNPCompleteWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat/index.html#max-three-sat-maxsnp-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Approximability of MAX-3SAT](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/pcp-and-inapproximability/approximability-of-max-3sat)
