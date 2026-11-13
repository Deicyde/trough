---
declaration: section
origin: cited
lean: Cslib.Complexity.Karp.is3, Cslib.Complexity.Karp.sat3Dec, Cslib.Complexity.Karp.ren, Cslib.Complexity.Karp.fresh, Cslib.Complexity.Karp.renLit, Cslib.Complexity.Karp.chainTail, Cslib.Complexity.Karp.chain, Cslib.Complexity.Karp.used
statement: formalized
proof: formalized
---

# 3-satisfiability

109 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html).

## Three-literal clause test

For a CNF formula $\varphi$, this Boolean test holds exactly
when every clause of $\varphi$ has at most three literals.

Formalized by `Cslib.Complexity.Karp.is3`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSat.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSat.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#is3).

## The 3SAT decision problem

3SAT accepts a bit string $x$ exactly when $x$ is the binary
code of a satisfiable CNF formula in which every clause has at most three literals.

Formalized by `Cslib.Complexity.Karp.sat3Dec`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSat.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSat.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#sat3-dec).

## Renaming of the original variables

Variable index $n$ is renamed to $2n$, so the
variables of the original formula get even indices.

Formalized by `Cslib.Complexity.Karp.ren`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSat.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSat.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#ren).

## Fresh variable indices

For $u \in \mathbb{N}$, the $u$-th fresh variable has index
$2^{u+1} + 1$, an odd number.

Formalized by `Cslib.Complexity.Karp.fresh`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSat.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSat.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#fresh).

## Renaming a literal

The literal with variable index $n$ and polarity $b$ is renamed to
the literal with variable index $2n$ and the same polarity $b$.

Formalized by `Cslib.Complexity.Karp.renLit`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSat.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSat.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#ren-lit).

## The tail of a clause chain

Write $y_v$ for the variable with index $2^{v+1} + 1$ (the
$v$-th fresh variable), $\ell'$ for a literal $\ell$ whose variable index $n$ is replaced by $2n$
with the same polarity, and $z \ominus j$ for $\max(z - j, 0)$. Given literals
$\ell_1, \dots, \ell_m$ and a natural number $z$, the result is the empty formula if $m = 0$, and
otherwise the $m$ clauses $(\neg y_{z \ominus (i - 1)} \lor \ell_i' \lor y_{z \ominus i})$ for
$i = 1, \dots, m - 1$, followed by $(\neg y_{z \ominus (m - 1)} \lor \ell_m')$.

Here $z$ is the fresh number of the variable asserted by the clause before the tail; fresh
numbers decrease along the chain.

Formalized by `Cslib.Complexity.Karp.chainTail`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSat.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSat.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#chain-tail).

## The chain of clauses replacing one clause

Write $y_v$ for the variable with index
$2^{v+1} + 1$ (the $v$-th fresh variable) and $\ell'$ for a literal $\ell$ whose variable index $n$
is replaced by $2n$, with the same polarity. Given a clause $C$ and a natural number $u$, the
empty clause is replaced by the empty clause alone, a one-literal clause $\ell_1$ by the clause
$\ell_1'$, and a clause $\ell_1 \lor \dots \lor \ell_k$ with $k \ge 2$ by the $k$ clauses
$(\ell_1' \lor y_{u+k-2})$, then $(\neg y_{u+k-i} \lor \ell_i' \lor y_{u+k-i-1})$ for
$i = 2, \dots, k - 1$, then $(\neg y_u \lor \ell_k')$. A clause of length $k \ge 2$ thus uses
the fresh numbers $u$ to $u + k - 2$.

Formalized by `Cslib.Complexity.Karp.chain`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSat.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSat.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#chain).

## Fresh variables reserved for a clause

The number of fresh variables reserved for a CNF
clause $C$ in the SAT-to-3SAT translation: $k - 1$ if $C$ has $k \ge 1$ literals, and $0$ if $C$
is empty.

Formalized by `Cslib.Complexity.Karp.used`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSat.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSat.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#used).

## Clause-by-clause translation with a fresh-number counter

For a CNF formula this returns a
pair $(N, \psi)$ of a natural number $N$ and a CNF formula $\psi$. The empty formula gives $N = 0$
and $\psi$ empty. A formula with first clause $C$ and remaining clauses $\varphi'$, whose pair is
$(N', \psi')$, gives $N = N' + \max(|C| - 1, 0)$ and, as $\psi$, the chain of clauses replacing
$C$ with fresh numbers from $N'$ on, followed by the clauses of $\psi'$.

Fresh numbers are thus handed out from the last clause backwards, and $N$ is the next free one.

Formalized by `Cslib.Complexity.Karp.to3Aux`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSat.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSat.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#to3-aux).

## The SAT-to-3SAT translation

For a CNF formula with clauses $C_1, \dots, C_m$, the
translation is the concatenation, in order, of the chains of clauses replacing $C_1, \dots, C_m$,
where the chain for $C_i$ uses fresh numbers from $u_i = \sum_{j > i} \max(|C_j| - 1, 0)$ on.

Formalized by `Cslib.Complexity.Karp.to3`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSat.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSat.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#to3).

## The SAT-to-3SAT reduction on bit strings

A bit string that decodes, with no bits left
over, to a CNF formula $\varphi$ is sent to the binary code of the SAT-to-3SAT translation of
$\varphi$; any other bit string is sent to the empty string.

Formalized by `Cslib.Complexity.Karp.reduce3`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSat.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSat.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#reduce3).

## Chain-tail clauses have at most three literals

For every clause $C$ and natural number
$z$, every clause of $\mathrm{chainTail}(C, z)$ has at most three literals.

Formalized by `Cslib.Complexity.Karp.length_le_three_of_mem_chainTail`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#length-le-three-of-mem-chain-tail).

## Chain clauses have at most three literals

For every clause $C$ and natural number $u$,
every clause of $\mathrm{chain}(C, u)$ has at most three literals.

Formalized by `Cslib.Complexity.Karp.length_le_three_of_mem_chain`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#length-le-three-of-mem-chain).

## Clauses of the auxiliary 3SAT translation have at most three literals

For every CNF
formula $\varphi$, every clause of the clause list produced by the auxiliary SAT-to-3SAT
translation of $\varphi$ (which replaces each clause by its chain of clauses with fresh
variables) has at most three literals.

Formalized by `Cslib.Complexity.Karp.length_le_three_of_mem_to3Aux`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#length-le-three-of-mem-to3-aux).

## The SAT-to-3SAT translation yields clauses of length at most three

For every CNF formula
$\varphi$, every clause of the translation $\mathrm{to3}(\varphi)$ has at most three literals.

Formalized by `Cslib.Complexity.Karp.is3_to3`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#is3-to3).

## Soundness of the tail of a chain

Let $C$ be a nonempty clause and $z$ a natural number. If
an assignment $v'$ satisfies every clause of $\mathrm{chainTail}(C, z)$ and gives the fresh
variable $\mathrm{fresh}(z)$ the value true, then the assignment $n \mapsto v'(2n)$ satisfies
$C$.

Formalized by `Cslib.Complexity.Karp.chainTail_sound`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#chain-tail-sound).

## Soundness of the chain of one clause

Let $C$ be a clause and $u$ a natural number. If an
assignment $v'$ satisfies every clause of $\mathrm{chain}(C, u)$, then the assignment
$n \mapsto v'(2n)$ satisfies $C$.

Formalized by `Cslib.Complexity.Karp.chain_sound`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#chain-sound).

## Soundness of the auxiliary 3SAT translation

For every assignment
$v' : \mathbb{N} \to \mathrm{Bool}$ and every CNF formula $\varphi$, if $v'$ satisfies the
clause list produced by the auxiliary SAT-to-3SAT translation of $\varphi$, then the assignment
$n \mapsto v'(2n)$ satisfies $\varphi$.

Formalized by `Cslib.Complexity.Karp.to3Aux_sound`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#to3-aux-sound).

## Completeness of the tail of a chain

Let $v$ and $v'$ be assignments with $v'(2n) = v(n)$
for every $n$, let $C$ be a nonempty clause with $m + 1$ literals and let $z$ be a natural
number. Suppose that for every $j \le m$, $v'$ gives the fresh variable $\mathrm{fresh}(z - j)$
the value true exactly when $v$ satisfies some literal of the clause obtained from $C$ by
dropping its first $j$ literals, where $z - j$ is truncated subtraction ($0$ when $j > z$). Then
$v'$ satisfies every clause of $\mathrm{chainTail}(C, z)$.

Formalized by `Cslib.Complexity.Karp.chainTail_complete`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#chain-tail-complete).

## Completeness of the chain of one clause

Let $v$ and $v'$ be assignments with
$v'(2n) = v(n)$ for every $n$, let $C$ be a clause and $u$ a natural number, and write
$k = \mathrm{used}(C)$. Suppose that $v$ satisfies $C$, and that for every $w$ with
$u \le w < u + k$, $v'$ gives the fresh variable $\mathrm{fresh}(w)$ the value true exactly when
$v$ satisfies some literal of the clause obtained from $C$ by dropping its first $u + k - w$
literals. Then $v'$ satisfies every clause of $\mathrm{chain}(C, u)$.

Formalized by `Cslib.Complexity.Karp.chain_complete`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#chain-complete).

## Values of the fresh variables in the 3SAT translation

For an assignment
$v : \mathbb{N} \to \mathrm{Bool}$, a CNF formula $\varphi$ and a natural number $w$, the value
$f_v(\varphi, w)$ is defined by recursion on $\varphi$. For the empty formula it is false. For a
formula with first clause $C$ and remaining clauses $\varphi'$, let $N'$ be the next free fresh
number of the clause-by-clause translation of $\varphi'$, and let $k = \max(|C| - 1, 0)$ be the
number of fresh variables reserved for $C$. If $w < N'$, then $f_v(\varphi, w)$ is
$f_v(\varphi', w)$; otherwise $f_v(\varphi, w)$ is true exactly when $v$ satisfies some literal
of the clause obtained from $C$ by dropping its first $N' + k - w$ literals, where the
subtraction is truncated at $0$.

The chain of clauses replacing $C$ uses the fresh numbers $N'$ to $N' + k - 1$, so for these $w$
the value records whether $v$ satisfies one of the last $w - N' + 1$ literals of $C$.

Formalized by `Cslib.Complexity.Karp.freshVal`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#fresh-val).

## Completeness of the auxiliary 3SAT translation

Let $v, v' : \mathbb{N} \to \mathrm{Bool}$
be assignments with $v'(2n) = v(n)$ for every $n$, let $\varphi$ be a CNF formula satisfied by
$v$, and let $N$ be the next free fresh number of the auxiliary SAT-to-3SAT translation of
$\varphi$. If for every $w < N$ the assignment $v'$ gives fresh variable number $w$, the variable
$2^{w+1} + 1$, the fresh-variable value of $w$ built from $v$ and $\varphi$, then $v'$ satisfies
the clause list produced by the auxiliary translation of $\varphi$.

Formalized by `Cslib.Complexity.Karp.to3Aux_complete`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#to3-aux-complete).

## Lifting an assignment to the 3SAT translation

Given an assignment
$v : \mathbb{N} \to \mathrm{Bool}$ and a CNF formula $\varphi$, the lifted assignment sends an
even variable $n$ to $v(n/2)$ and an odd variable $n$ to the fresh-variable value built from $v$
and $\varphi$ at the number $\lfloor \log_2 (n - 1) \rfloor - 1$, where $\lfloor \log_2 0 \rfloor$
is taken to be $0$ and subtraction is truncated at $0$.

Formalized by `Cslib.Complexity.Karp.lift`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#lift).

## The lifted assignment on renamed variables

For every assignment
$v : \mathbb{N} \to \mathrm{Bool}$, every CNF formula $\varphi$ and every $n \in \mathbb{N}$,
the assignment lifted from $v$ for the 3SAT translation of $\varphi$ gives the renamed variable
$2n$ the value $v(n)$.

Formalized by `Cslib.Complexity.Karp.lift_ren`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#lift-ren).

## The lifted assignment on fresh variables

For every assignment
$v : \mathbb{N} \to \mathrm{Bool}$, every CNF formula $\varphi$ and every $w \in \mathbb{N}$,
the assignment lifted from $v$ for the 3SAT translation of $\varphi$ gives fresh variable number
$w$, that is variable $2^{w+1} + 1$, the fresh-variable value of $w$ built from $v$ and
$\varphi$.

Formalized by `Cslib.Complexity.Karp.lift_fresh`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#lift-fresh).

## The SAT-to-3SAT translation preserves satisfiability

For every CNF formula $\varphi$, the
translation $\mathrm{to3}(\varphi)$ is satisfiable if and only if $\varphi$ is satisfiable.

Formalized by `Cslib.Complexity.Karp.cnfSat_to3_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#cnf-sat-to3-iff).

## CNF encodings are nonempty

For every CNF formula $\varphi$, the binary encoding of
$\varphi$ is not the empty bit string.

Formalized by `Cslib.Complexity.Karp.encodeCNF_ne_nil`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#encode-cnf-ne-nil).

## Correctness of the SAT-to-3SAT reduction on bit strings

For every bit string $x$, SAT
accepts $x$ (that is, $x$ encodes a satisfiable CNF formula) exactly when 3SAT accepts the image
of $x$ under the SAT-to-3SAT reduction (that is, the image encodes a satisfiable CNF formula in
which every clause has at most three literals).

Formalized by `Cslib.Complexity.Karp.satDec_eq_sat3Dec_reduce3`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatCorrect.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#sat-dec-eq-sat3-dec-reduce3).

## Binary representation of a fresh name

For every natural number $z$, the binary
representation (least significant bit first) of $\mathrm{fresh}(z) = 2^{z+1} + 1$ is
$\mathrm{true}$, then $z$ copies of $\mathrm{false}$, then $\mathrm{true}$.

Formalized by `Cslib.Complexity.Karp.Emit3.encodeNat_fresh`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#encode-nat-fresh).

## Code of a fresh literal

For every natural number $z$ and every polarity $b$, the binary
code of the literal $(\mathrm{fresh}(z), b)$, where $\mathrm{fresh}(z) = 2^{z+1} + 1$, is
$\mathrm{true}, \mathrm{true}$, then $z$ copies of the pair $\mathrm{true}, \mathrm{false}$, then
$\mathrm{true}, \mathrm{true}, \mathrm{false}, b$.

Formalized by `Cslib.Complexity.Karp.Emit3.encodeLit_fresh`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#encode-lit-fresh).

## Code of a renamed literal

For every literal $(n, p)$, the binary code of the renamed
literal $(2n, p)$ is: the pair $\mathrm{true}, \mathrm{false}$ if $n \neq 0$ and nothing if
$n = 0$, then the pair $\mathrm{true}, b$ for each bit $b$ of the binary representation of $n$
(least significant bit first, no bits for $n = 0$), then $\mathrm{false}, p$.

Formalized by `Cslib.Complexity.Karp.Emit3.encodeLit_renLit`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#encode-lit-ren-lit).

## Stacks of the 3SAT emitter

The 3SAT emitter machine has six stacks: the token stack
$T$, the output stack $O$, the fresh counter $U$, two scratch counters $Z$ and $W$, and the
output clause count $C$.

Formalized by `Cslib.Complexity.Karp.Emit3.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#k).

## Stack alphabets of the SAT-to-3SAT emitter

The output stack of the emitter machine holds
Booleans; each of its other stacks (the token stack, the fresh counter, the two scratch counters
and the output clause count) holds symbols of the SAT verifier's token alphabet.

The counters are unary: they hold only the clause token.

Formalized by `Cslib.Complexity.Karp.Emit3.Γ`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#untitled).

## Control labels of the SAT-to-3SAT emitter

The emitter machine has the labels
$\mathrm{start}$, $\mathrm{clause}$, $\mathrm{fin}$ and $\mathrm{done}$, and, for Booleans
$f, p, s, x, e$, the labels $\mathrm{lit}(f)$, $\mathrm{fa}(s, x)$, $\mathrm{fb}(s, x)$,
$\mathrm{fc}(s, x)$, $\mathrm{fd}(s, x)$, $\mathrm{fe}(s, x)$, $\mathrm{body}(f, p)$,
$\mathrm{cp}(f, e)$, $\mathrm{aft}(f)$ and $\mathrm{sfx}(f)$, all distinct; equality of labels is
decidable.

At $\mathrm{lit}(f)$ the machine pops a literal marker, $f$ telling whether it is the first
literal walked in its clause. The labels $\mathrm{fa}$ to $\mathrm{fe}$ prepend the fresh literal
$(2^{z+1} + 1, s)$ for the current counter $z$, where $x$ is the polarity of the pending literal
when $s$ is true and its first-literal flag when $s$ is false. The labels $\mathrm{body}$ and
$\mathrm{cp}$ prepend the renamed literal, and $\mathrm{aft}$ and $\mathrm{sfx}$ close the output
clause.

Formalized by `Cslib.Complexity.Karp.Emit3.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#lab).

## Literal-marker test of the 3SAT emitter

For an optional token $s$ (the top of a stack,
absent when the stack is empty), the test is true exactly when $s$ is present and is a literal
marker, of either polarity.

Formalized by `Cslib.Complexity.Karp.Emit3.isLit`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#is-lit).

## Entry label of a literal

For Booleans $f$ and $p$, the label where the emitter continues
after popping the marker of a literal of polarity $p$ is $\mathrm{body}(\text{true}, p)$, which
copies the name directly, if $f$ holds (the literal is the first walked in its clause), and
$\mathrm{fa}(\text{true}, p)$, which first prepends the fresh literal of the current counter
with polarity true, otherwise.

Formalized by `Cslib.Complexity.Karp.Emit3.pre`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#pre).

## Return label of the fresh-literal subroutine

For Booleans $s$ and $x$, the label where
the emitter continues after prepending the fresh literal of polarity $s$ is
$\mathrm{body}(\text{false}, x)$ if $s$ is true, which copies the name of the pending literal of
polarity $x$, and $\mathrm{sfx}(x)$ if $s$ is false, which closes the output clause, $x$ being
the first-literal flag.

Formalized by `Cslib.Complexity.Karp.Emit3.ret`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#ret).

## The SAT-to-3SAT emitter machine

The emitter is the multi-stack machine on the stacks
$T, O, U, Z, W, C$ of the emitter ($O$ holds bits, the others token symbols), with the labels of
the emitter and one internal Boolean variable. A unit is the clause symbol, and prepending bits
$b_1, \dots, b_k$ to $O$ pushes them so that $O$ reads $b_1, \dots, b_k$ from the top. The labels
act as follows.

* $\mathrm{start}$: if $T$ is empty, push $\text{false}$ on $O$ and go to $\mathrm{fin}$;
  otherwise pop $T$ and go to $\mathrm{clause}$.
* $\mathrm{clause}$: if the top of $T$ is a literal marker, go to $\mathrm{lit}(\text{true})$;
  otherwise push a unit on $C$, push $\text{false}$ on $O$ and go to $\mathrm{start}$.
* $\mathrm{lit}(f)$: pop $T$, set the variable $p$ to whether the popped symbol is the literal
  marker of polarity true, and go to $\mathrm{body}(\text{true}, p)$ if $f$ holds and to
  $\mathrm{fa}(\text{true}, p)$ otherwise.
* $\mathrm{fa}(s, x)$: prepend $\text{true}, \text{true}, \text{false}, s$ to $O$ and go to
  $\mathrm{fb}(s, x)$.
* $\mathrm{fb}(s, x)$: pop $U$ until it is empty, pushing a unit on $Z$ and on $W$ per popped
  symbol, then go to $\mathrm{fc}(s, x)$.
* $\mathrm{fc}(s, x)$: pop $W$ until it is empty, pushing a unit on $U$ per popped symbol, then
  go to $\mathrm{fd}(s, x)$.
* $\mathrm{fd}(s, x)$: pop $Z$ until it is empty, prepending $\text{true}, \text{false}$ to $O$
  per popped symbol, then go to $\mathrm{fe}(s, x)$.
* $\mathrm{fe}(\text{true}, p)$: push a unit on $U$, prepend $\text{true}, \text{true}$ to $O$
  and go to $\mathrm{body}(\text{false}, p)$. $\mathrm{fe}(\text{false}, f)$: prepend
  $\text{true}, \text{true}$ to $O$ and go to $\mathrm{sfx}(f)$.
* $\mathrm{body}(f, p)$: prepend $\text{false}, p$ to $O$ and go to $\mathrm{cp}(f, \text{false})$.
* $\mathrm{cp}(f, e)$: if the top of $T$ is a bit symbol $b$, pop it, prepend $\text{true}, b$ to
  $O$ and go to $\mathrm{cp}(f, \text{true})$; otherwise prepend $\text{true}, \text{false}$ to
  $O$ if $e$ holds, and go to $\mathrm{aft}(f)$.
* $\mathrm{aft}(f)$: if the top of $T$ is a literal marker, go to $\mathrm{fa}(\text{false}, f)$;
  otherwise push a unit on $C$, prepend $k$ copies of $\text{true}$ and then $\text{false}$ to
  $O$, where $k = 1$ if $f$ holds and $k = 2$ otherwise, and go to $\mathrm{start}$.
* $\mathrm{sfx}(f)$: push a unit on $C$, prepend $k$ copies of $\text{true}$ and then
  $\text{false}$ to $O$, where $k = 2$ if $f$ holds and $k = 3$ otherwise, and go to
  $\mathrm{lit}(\text{false})$.
* $\mathrm{fin}$: pop $C$ until it is empty, prepending $\text{true}$ to $O$ per popped symbol,
  then go to $\mathrm{done}$.
* $\mathrm{done}$: halt.

Each test of a stack top and each pop of a loop also stores its outcome in the internal
variable.

Formalized by `Cslib.Complexity.Karp.Emit3.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#prog).

## Start label of the SAT-to-3SAT emitter

The start label of the emitter machine is its label
$\mathrm{start}$, at which the machine begins each input clause or, once the token stack is
empty, moves on to its final phase, which writes the output clause count.

Formalized by `Cslib.Complexity.Karp.Emit3.start`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#start).

## Stack contents of the SAT-to-3SAT emitter

For a list $t$ of tokens, a list $o$ of bits
and $z, c \in \mathbb{N}$, $\mathrm{st}(t, o, z, c)$ is the stack contents of the emitter machine
in which the token stack holds $t$, the output stack holds $o$, the fresh counter holds exactly
$z$ copies of the clause token $\mathrm{cl}$, the output clause count holds exactly $c$ copies of
$\mathrm{cl}$, and the two scratch counters are empty.

Formalized by `Cslib.Complexity.Karp.Emit3.st`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#st).

## Fresh-literal subroutine of the 3SAT emitter

For all booleans $s$ and $x$, every token
list $t$, output bit list $o$, natural numbers $z$ and $c$, and flag $v$, there is a flag $v'$
such that the 3SAT emitter machine, started at the fresh-literal label for $(s, x)$ with flag
$v$, token stack $t$, output stack $o$, fresh counter $z$, clause count $c$ and empty scratch
counters, reaches in exactly $3z + 5$ steps the return label for $(s, x)$ with flag $v'$, token
stack $t$, output stack the code of the literal $(\mathrm{fresh}(z), s)$ followed by $o$, where
$\mathrm{fresh}(z) = 2^{z+1} + 1$, fresh counter $z + 1$ if $s$ is true and $z$ if $s$ is false,
clause count $c$ and empty scratch counters. The return label is the renamed-literal label for a
literal of polarity $x$ that is not the first walked in its clause if $s$ is true, and the
clause-closing label for first-flag $x$ if $s$ is false.

The subroutine prepends $\mathrm{true}, \mathrm{true}, \mathrm{false}, s$, copies the fresh
counter $U$ into the scratch counter $Z$ (restoring $U$ through the scratch counter $W$),
prepends $\mathrm{true}, \mathrm{false}$ per unit of $Z$, then prepends
$\mathrm{true}, \mathrm{true}$, and for $s$ true adds one to $U$.

Formalized by `Cslib.Complexity.Karp.Emit3.fresh_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#fresh-run).

## Name copy loop of the 3SAT emitter

Let $f$ and $e$ be booleans, $R$ a token list whose
first token, if there is one, is not a name bit, $z$ and $c$ natural numbers, $b_1, \dots, b_m$
bits, $v$ a flag and $o$ an output bit list. Then there is a flag $v'$ such that the 3SAT emitter
machine, started at the copy label for $(f, e)$ with flag $v$, token stack the name-bit tokens
$b_1, \dots, b_m$ followed by $R$, output stack $o$, fresh counter $z$, clause count $c$ and
empty scratch counters, reaches in exactly $m + 1$ steps the after-literal label for $f$ with
flag $v'$, token stack $R$, output stack
$P, \mathrm{true}, b_m, \mathrm{true}, b_{m-1}, \dots, \mathrm{true}, b_1$ followed by $o$, and
the same counters, where $P$ is the pair $\mathrm{true}, \mathrm{false}$ if $e$ is true or
$m > 0$, and is empty otherwise.

Each name bit $b$ read prepends $b$ and then $\mathrm{true}$; the leading pair
$\mathrm{true}, \mathrm{false}$ codes the low bit $0$ of a renamed name $2n$.

Formalized by `Cslib.Complexity.Karp.Emit3.cp_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#cp-run).

## Copying a renamed name

Write $\langle \ell, w, t, o, z, c\rangle$ for the configuration
of the emitter machine at label $\ell$ with internal variable $w$, token stack $t$, output stack
$o$, fresh counter $z$, output-clause count $c$ and empty scratch stacks. Let $l = (n, b)$ be a
literal, $f$ and $v$ Booleans, $R$ a token stack whose top, if any, is not a bit symbol, $o$ an
output stack and $z$, $c$ natural numbers. Let $B$ be the $k$ binary digits of $n$ as bit
symbols, most significant first ($k = 0$ for $n = 0$), and $e$ the encoding of the renamed
literal $(2n, b)$. Then for some $w'$ the machine goes in exactly $k + 2$ steps from
$\langle \mathrm{body}(f, b), v, B R, o, z, c\rangle$ to
$\langle \mathrm{aft}(f), w', R, e\,o, z, c\rangle$, where juxtaposition is concatenation of
stacks, top first.

Formalized by `Cslib.Complexity.Karp.Emit3.name_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#name-run).

## The 3SAT emitter reads a literal marker

For all booleans $f$ and $p$, every token list
$t$, output bit list $o$, natural numbers $z$ and $c$, and flag $v$, there is a flag $v'$ such
that the 3SAT emitter machine, started at the literal label for $f$ with flag $v$, token stack
the literal marker of polarity $p$ followed by $t$, output stack $o$, fresh counter $z$, clause
count $c$ and empty scratch counters, reaches the renamed-literal label for $(f, p)$ with flag
$v'$ and token stack $t$ as follows. If $f$ is true (the literal is the first walked in its
clause), this takes exactly $1$ step and leaves the output stack and the fresh counter unchanged.
If $f$ is false, it takes exactly $3z + 6$ steps, the output stack becomes the code of the
literal $(\mathrm{fresh}(z), \mathrm{true})$ followed by $o$, where
$\mathrm{fresh}(z) = 2^{z+1} + 1$, and the fresh counter becomes $z + 1$. In both cases the
clause count stays $c$ and the scratch counters stay empty.

Formalized by `Cslib.Complexity.Karp.Emit3.head_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#head-run).

## Closing an output clause in the SAT-to-3SAT emitter

Let $f$ be a Boolean, $R$ a list of
tokens, $o$ a list of bits and $z, c \in \mathbb{N}$, and let $m = 1$ if $f$ is true and $m = 2$
otherwise. Start the emitter machine at its clause-closing label $\mathrm{aft}(f)$, with any
internal state, with stack contents $\mathrm{st}(R, o, z, c)$: token stack $R$, output stack $o$,
fresh counter $z$, output clause count $c$ and empty scratch counters.

If the top of $R$ is a literal marker, then after exactly $3z + 7$ steps the machine is at the
label $\mathrm{lit}(\mathrm{false})$ with stack contents $\mathrm{st}(R, o', z, c + 1)$, where the
list $o'$ consists of $m + 1$ copies of true, then false, then the code of the literal
$(\mathrm{fresh}(z), \mathrm{false})$, then $o$. Otherwise (in particular when $R$ is empty),
after exactly one step the machine is at the label $\mathrm{start}$ with stack contents
$\mathrm{st}(R, o', z, c + 1)$, where $o'$ consists of $m$ copies of true, then false, then $o$.
In both cases the final internal state is unspecified.

Formalized by `Cslib.Complexity.Karp.Emit3.tail_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#tail-run).

## Output clause of one literal

For Booleans $f$ and $g$, a counter $z$ and a literal
$l = (n, b)$, let $z' = z$ if $f$ holds and $z' = z + 1$ otherwise. The output clause of $l$ is
the clause consisting of, in this order: the literal $(2^{z'+1} + 1, \text{false})$ unless $g$
holds, then the renamed literal $(2n, b)$, then the literal $(2^{z+1} + 1, \text{true})$ unless
$f$ holds. Here $f$ tells whether $l$ is the first literal walked in its clause, $g$ whether it
is the last one, and $z'$ is the counter after $l$.

Formalized by `Cslib.Complexity.Karp.Emit3.litCl`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#lit-cl).

## Fresh numbers used by a run of literals

For a list $L$ of literals and a Boolean $f$,
the number of fresh numbers used up by walking $L$ is $|L| - 1$ (truncated at $0$) if $f$ holds
and $|L|$ otherwise; $f$ tells whether the last literal of $L$ is the first literal walked in
its clause.

Formalized by `Cslib.Complexity.Karp.Emit3.nz`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#nz).

## Output clauses of a walked list of literals

For a list $L$ of literals of a clause,
Booleans $f$ and $g$, and $z \in \mathbb{N}$, $\mathrm{walkF}(L, f, g, z)$ is the list of output
clauses of the literals of $L$, in reading order, when $L$ is walked from its last literal with
counter $z$; $f$ tells whether the last literal of $L$ is the first walked in its clause, and $g$
whether the first literal of $L$ is the last walked. It is defined by recursion on $L$. The empty
list gives no clauses. If $L$ has first literal $l$ and remaining literals $L'$, the first clause
is the output clause of $l$ whose first-walked flag is true exactly when $f$ is true and $L'$ is
empty, whose last-walked flag is $g$, and whose counter is $z + n$, where $n$ is the number of
fresh numbers used up by walking $L'$ ($|L'| - 1$ if $f$ is true, with $0 - 1 = 0$, and $|L'|$
otherwise); it is followed by $\mathrm{walkF}(L', f, \mathrm{false}, z)$.

Formalized by `Cslib.Complexity.Karp.Emit3.walkF`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#walk-f).

## Walking a whole clause gives its chain

For every non-empty clause $C$ and every
$z \in \mathbb{N}$, the output clauses of the literals of $C$, walked from its last literal with
counter $z$, with both the first-walked flag and the last-walked flag true, that is,
$\mathrm{walkF}(C, \mathrm{true}, \mathrm{true}, z)$, are the chain of clauses replacing $C$ with
fresh numbers from $z$ on.

Formalized by `Cslib.Complexity.Karp.Emit3.walkF_chain`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#walk-f-chain).

## One literal of the emitter

Write $\langle \ell, w, t, o, z, c\rangle$ for the
configuration of the emitter machine at label $\ell$ with internal variable $w$, token stack $t$,
output stack $o$, fresh counter $z$, output-clause count $c$ and empty scratch stacks. Let
$l = (n, b)$ be a literal, $f$ and $v$ Booleans, $R$ a token stack whose top, if any, is not a
bit symbol, $o$ an output stack, and $z$, $c$, $Z_b$ natural numbers with $z + d \le Z_b$, where
$d = 0$ if $f$ holds and $d = 1$ otherwise. Let $T_l$ be the token block of $l$: the literal
marker of polarity $b$ above the binary digits of $n$, most significant first (no digits for
$n = 0$). Let $g$ be true exactly when the top of $R$ is not a literal marker (in particular
when $R$ is empty), let $\ell'$ be $\mathrm{start}$ if $g$ holds and $\mathrm{lit}(\text{false})$
otherwise, and let $e$ be the encoding of the output clause of $l$ with flags $f$, $g$ and
counter $z$. Then for some $w'$ the machine goes in at most $|T_l| + 6 Z_b + 14$ steps from
$\langle \mathrm{lit}(f), v, T_l R, o, z, c\rangle$ to
$\langle \ell', w', R, e\,o, z + d, c + 1\rangle$, where juxtaposition is concatenation of
stacks, top first.

Formalized by `Cslib.Complexity.Karp.Emit3.lit_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#lit-run).

## The literals of a clause in the emitter

Write $\langle \ell, w, t, o, z, c\rangle$ for
the configuration of the emitter machine at label $\ell$ with internal variable $w$, token stack
$t$, output stack $o$, fresh counter $z$, output-clause count $c$ and empty scratch stacks. Let
$Z_b$ be a natural number, $L = (l_1, \dots, l_k)$ a list of literals, $R$ a token stack whose
top is a literal marker, $f$ and $v$ Booleans, $o$ an output stack and $z$, $c$ natural numbers
with $z + m \le Z_b$, where $m$ is $k - 1$ (truncated at $0$) if $f$ holds and $k$ otherwise.
The token block of a literal $(n, b)$ is the literal marker of polarity $b$ above the binary
digits of $n$, most significant first (no digits for $n = 0$); let $T$ be the concatenation of
the token blocks of $l_k, \dots, l_1$, in this order. For $1 \le i \le k$ let $z_i = z + m_i$,
where $m_i$ is $k - i - 1$ (truncated at $0$) if $f$ holds and $k - i$ otherwise, let $f_i$ be
true exactly when $f$ holds and $i = k$, and let $e_i$ be the encoding of the output clause of
$l_i$ with flags $f_i$, false and counter $z_i$. Let $E = e_1 \cdots e_k$ (empty for $k = 0$),
and let $f'$ be true exactly when $f$ holds and $k = 0$. Then for some $w'$ the machine goes in
at most $|T| + k (6 Z_b + 14)$ steps from $\langle \mathrm{lit}(f), v, T R, o, z, c\rangle$ to
$\langle \mathrm{lit}(f'), w', R, E\,o, z + m, c + k\rangle$, where juxtaposition is
concatenation of stacks, top first.

Formalized by `Cslib.Complexity.Karp.Emit3.lits_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 521](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L521). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#lits-run).

## The 3SAT emitter processes one clause

Let $C$ be a clause, $Z_b$, $z$ and $c$ natural
numbers with $z + \mathrm{used}(C) \le Z_b$, where $\mathrm{used}(C) = \max(|C| - 1, 0)$, let $R$
be a token list that is empty or starts with a clause token, $o$ an output bit list and $v$ a
flag. Let $\mathrm{clRev}(C)$ be the tokens of $C$ as they lie on the token stack (a clause token,
then the tokens of its literals, last literal first), and let $D_1, \dots, D_k$ be the clauses of
$\mathrm{chain}(C, z)$. Then there is a flag $v'$ such that the 3SAT emitter machine, started at
its start label with flag $v$, token stack $\mathrm{clRev}(C)$ followed by $R$, output stack $o$,
fresh counter $z$, clause count $c$ and empty scratch counters, reaches in at most
$|\mathrm{clRev}(C)| \cdot (6 Z_b + 15)$ steps its start label with flag $v'$, token stack $R$,
output stack $\mathrm{enc}(D_1) \cdots \mathrm{enc}(D_k)$ followed by $o$, fresh counter
$z + \mathrm{used}(C)$, clause count $c + k$ and empty scratch counters, where $\mathrm{enc}$ is
the binary clause encoding.

Formalized by `Cslib.Complexity.Karp.Emit3.clause_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#clause-run).

## The 3SAT emitter processes a whole formula

Let $\varphi = C_1 \cdots C_m$ be a CNF
formula, $u = \sum_{i=1}^{m} \max(|C_i| - 1, 0)$ the number of fresh variables its 3SAT
translation uses, $Z_b \ge u$ a natural number, $R$ a token list that is empty or starts with a
clause token, $o$ an output bit list and $v$ a flag. Let $T$ be the token list
$\mathrm{clRev}(C_m) \cdots \mathrm{clRev}(C_1)$, where $\mathrm{clRev}(C)$ is the list of tokens
of $C$ as they lie on the token stack, and let $D_1, \dots, D_k$ be the clauses of the 3SAT
translation $\mathrm{to3}(\varphi)$. Then there is a flag $v'$ such that the 3SAT emitter machine,
started at its start label with flag $v$, token stack $T$ followed by $R$, output stack $o$,
fresh counter $0$, clause count $0$ and empty scratch counters, reaches in at most
$|T| \cdot (6 Z_b + 15)$ steps its start label with flag $v'$, token stack $R$, output stack
$\mathrm{enc}(D_1) \cdots \mathrm{enc}(D_k)$ followed by $o$, fresh counter $u$, clause count $k$
and empty scratch counters, where $\mathrm{enc}$ is the binary clause encoding.

Formalized by `Cslib.Complexity.Karp.Emit3.formula_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 594](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L594). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#formula-run).

## Repeating a single bit

For every bit $x$ and every $n \in \mathbb{N}$, the repeated block
$\mathrm{rep}([x], n)$ is the list consisting of $n$ copies of $x$.

Formalized by `Cslib.Complexity.Karp.Emit3.rep_single`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 628](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L628). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#rep-single).

## The SAT-to-3SAT emitter writes the encoded translation in quadratic time

Let $\varphi$ be
a CNF formula, $o$ a list of bits and $T$ the token sequence of $\varphi$. Start the emitter
machine at its start label, with any internal state, with the token stack holding $T$ reversed
(so that the first token of $T$ is at the bottom), the output stack holding $o$, and every other
stack empty. Then after at most $8(|T| + 1)^2$ steps the machine reaches its label
$\mathrm{done}$, with some internal state and stack contents in which the output stack, read from
the top, holds the binary code of the SAT-to-3SAT translation of $\varphi$ followed by $o$.

Formalized by `Cslib.Complexity.Karp.Emit3.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean, line 636](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatEmit.lean#L636). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#run).

## Stacks of the 3SAT clause-length filter

The filter has exactly two stacks: the token
stack $T$ and the side stack $U$.

Formalized by `Cslib.Complexity.Karp.Filter3.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#k-2).

## Labels of the 3SAT clause-length filter

The filter has exactly seven labels: the walking
labels $w_0, w_1, w_2, w_3$, at which it walks the token stack having seen that many literals of
the current clause ($w_3$: three or more); the return label $\mathsf{back}$, at which it moves
the tokens back; and the exits $\mathsf{pass}$ and $\mathsf{fail}$.

Formalized by `Cslib.Complexity.Karp.Filter3.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#lab-2).

## Statements of the filter

The statements of a multi-stack Turing machine (Mathlib's TM2
model) with the two stacks $T$ and $U$, each over the symbol alphabet of the SAT verifier, the
labels of the filter, and a Boolean internal state.

Formalized by `Cslib.Complexity.Karp.Filter3.Stmt`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#stmt).

## Walking label for a literal count

The walking label after $n$ literals of the current
clause: $w_0$, $w_1$, $w_2$ for $n = 0, 1, 2$, and $w_3$ for every $n \ge 3$.

Formalized by `Cslib.Complexity.Karp.Filter3.wl`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#wl).

## Next walking label

Write $w_i$ for the walking label after $i$ literals of the current
clause ($w_3$: three or more). For a Boolean $c$ (whether the filter is capped), the label after
one more literal sends $w_0$ to $w_1$, $w_1$ to $w_2$ and $w_2$ to $w_3$; it sends $w_3$ to the
failure label when $c$ is true and to $w_3$ when $c$ is false; every other label is unchanged.

Formalized by `Cslib.Complexity.Karp.Filter3.nxt`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#nxt).

## Conditional move between stacks

For stacks $a$ and $b$ of the filter, a symbol $s$, a
label $\ell$ and a statement $q$: the statement that tests whether the top of stack $a$ is $s$ and
sets the internal state to the outcome; if it is, it pops $a$, pushes $s$ onto $b$ and jumps to
$\ell$, and otherwise it runs $q$.

Formalized by `Cslib.Complexity.Karp.Filter3.mvIf`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#mv-if).

## One step of the clause-length walk

Write $w_0, w_1, w_2, w_3$ for the walking labels
after zero, one, two, and three or more literals of the current clause. For a Boolean cap flag
$\mathrm{cap}$ and a label $\ell$, the filter statement run at $\ell$: if the token stack is
empty, go to the label $\mathrm{back}$; if its top is the clause marker, move it onto the side
stack and go to $w_0$; if its top is a polarity marker, move it onto the side stack and go to
$w_1$, $w_2$, $w_3$ when $\ell$ is $w_0$, $w_1$, $w_2$ respectively, to $\mathrm{fail}$ when
$\ell = w_3$ and $\mathrm{cap}$ is true, and to $\ell$ otherwise; if its top is a name bit, move
it onto the side stack and stay at $\ell$; on any other symbol, go to $\mathrm{fail}$ without
moving it. Each test stores its outcome in the local variable.

Formalized by `Cslib.Complexity.Karp.Filter3.walk`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#walk).

## The clause-length filter program

For a Boolean $c$ (whether the filter is capped), the
program on the labels of the filter: at a walking label it runs one walking step with cap $c$; at
the label back it moves the top of the side stack $U$ onto the token stack $T$ and stays at back
when that top is a token (a clause marker, a literal marker or a name bit), goes to the label pass
when $U$ is empty, and goes to the label fail otherwise; at pass and at fail it halts. Each test
records its outcome in the internal state.

Formalized by `Cslib.Complexity.Karp.Filter3.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#prog-2).

## Start label of the filter

The filter starts at the walking label $w_0$, the label for
having seen no literal of the current clause.

Formalized by `Cslib.Complexity.Karp.Filter3.start`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#start-2).

## Token symbols of the 3SAT filter

A symbol of the SAT verifier's alphabet is a token
symbol when it is the clause marker, a literal marker of either polarity, or a name bit. The value
markers and the dead marker are not token symbols.

Formalized by `Cslib.Complexity.Karp.Filter3.IsTok`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#is-tok).

## Label after a token

Write $w_i$ for the walking label after $i$ literals of the current
clause ($w_3$: three or more). For a Boolean $c$ (whether the filter is capped) and a label
$\ell$, the label reached from $\ell$ on a symbol $s$ is: $w_0$ if $s$ is a clause marker; if $s$
is a literal marker, $w_1$, $w_2$ or $w_3$ when $\ell$ is $w_0$, $w_1$ or $w_2$ respectively, the
failure label when $\ell = w_3$ and $c$ is true, and $\ell$ itself otherwise; and $\ell$ itself
for every other symbol.

Formalized by `Cslib.Complexity.Karp.Filter3.tgt`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#tgt).

## Filter stacks from two lists

For lists of symbols $t$ and $u$, the stack contents that
put $t$ on the token stack $T$ and $u$ on the side stack $U$.

Formalized by `Cslib.Complexity.Karp.Filter3.st`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#st-2).

## One step of the clause-length walk on a token

Let $\mathrm{cap}$ be a Boolean,
$n \in \mathbb{N}$, $s$ a token (a name bit, a polarity marker or the clause marker), $R$ and $U$
lists of symbols and $v$ a Boolean; stacks are lists written top first, and $w_m$ is the walking
label after $m$ literals. Let $t$ be $w_0$ if $s$ is the clause marker, $w_n$ if $s$ is a name
bit, and, if $s$ is a polarity marker, $\mathrm{fail}$ when $\mathrm{cap}$ is true and $n \ge 3$
and $w_{n+1}$ otherwise. The clause-length filter with cap flag $\mathrm{cap}$ goes in exactly
one step from label $w_n$, local variable $v$, token stack $s$ on top of $R$ and side stack $U$
to label $t$, local variable true, token stack $R$ and side stack $s$ on top of $U$.

Formalized by `Cslib.Complexity.Karp.Filter3.walk_step`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#walk-step).

## Walking over name bits keeps the label

Let $\mathrm{cap}$ be a Boolean, $n \in \mathbb{N}$
and $R$ a list of symbols; stacks are lists written top first, $w_n$ is the walking label after
$n$ literals and $\mathrm{bit}(b)$ is the name-bit symbol carrying the Boolean $b$. For all
Booleans $b_1, \dots, b_k$, every list of symbols $U$ and every Boolean $v$ there is a Boolean
$v'$ such that the clause-length filter with cap flag $\mathrm{cap}$ goes in exactly $k$ steps
from label $w_n$, local variable $v$, token stack $\mathrm{bit}(b_1), \dots, \mathrm{bit}(b_k)$
on top of $R$ and side stack $U$ to label $w_n$, local variable $v'$, token stack $R$ and side
stack $\mathrm{bit}(b_k), \dots, \mathrm{bit}(b_1)$ on top of $U$.

Formalized by `Cslib.Complexity.Karp.Filter3.walk_bits`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#walk-bits).

## Walking over a literal advances the literal count

Let $\mathrm{cap}$ be a Boolean and
$n \in \mathbb{N}$ with $\mathrm{cap}$ false or $n < 3$; stacks are lists written top first,
$w_m$ is the walking label after $m$ literals, $\mathrm{bit}(b)$ is the name-bit symbol carrying
the Boolean $b$ and $\mathrm{lit}(p)$ is the polarity marker of polarity $p$. Let $l = (i, p)$ be
a literal with variable index $i \in \mathbb{N}$ and polarity $p$, let $e_1, \dots, e_k$ be the
binary encoding $\mathrm{encodeNat}(i)$ of $i$, let $R$ and $U$ be lists of symbols and $v$ a
Boolean. Then there is a Boolean $v'$ such that the clause-length filter with cap flag
$\mathrm{cap}$ goes in exactly $k + 1$ steps from label $w_n$, local variable $v$, token stack
$\mathrm{lit}(p), \mathrm{bit}(e_k), \dots, \mathrm{bit}(e_1)$ on top of $R$ and side stack $U$
to label $w_{n+1}$, local variable $v'$, token stack $R$ and side stack
$\mathrm{bit}(e_1), \dots, \mathrm{bit}(e_k), \mathrm{lit}(p)$ on top of $U$.

Formalized by `Cslib.Complexity.Karp.Filter3.walk_lit`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#walk-lit).

## A capped walk fails on a literal past the third

Let $n \in \mathbb{N}$ with $n \ge 3$
and let $w_n$ be the walking label after $n$ literals; stacks are lists written top first,
$\mathrm{bit}(b)$ is the name-bit symbol carrying the Boolean $b$ and $\mathrm{lit}(p)$ is the
polarity marker of polarity $p$. Let $l = (i, p)$ be a literal with variable index
$i \in \mathbb{N}$ and polarity $p$, let $e_1, \dots, e_m$ be the binary encoding
$\mathrm{encodeNat}(i)$ of $i$, let $R$ and $U$ be lists of symbols and $v$ a Boolean. Then
there are a Boolean $v'$ and stacks $S'$ such that the capped clause-length filter (cap flag
true) goes in exactly one step from label $w_n$, local variable $v$, token stack
$\mathrm{lit}(p), \mathrm{bit}(e_m), \dots, \mathrm{bit}(e_1)$ on top of $R$ and side stack $U$
to the label $\mathrm{fail}$ with local variable $v'$ and stacks $S'$.

Formalized by `Cslib.Complexity.Karp.Filter3.walk_lit_fail`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#walk-lit-fail).

## The filter walks a clause's literals within the cap

Let $c$ be a Boolean (whether the
filter is capped), let $\ell_1, \dots, \ell_k$ be literals (pairs of a variable index and a
polarity), let $n$ be a natural number with $c$ false or $n + k \le 3$, and let $w$ be the
concatenation of the stack tokens of $\ell_1, \dots, \ell_k$. For all lists of symbols $R$ and $U$
and every internal state $v$, the filter program with cap $c$, started at the walking label for $n$
literals with internal state $v$, token stack $wR$ (top first) and side stack $U$, reaches in
exactly $|w|$ steps the walking label for $n + k$ literals, with some internal state, token stack
$R$ and side stack $w^{\mathrm{rev}} U$, where $w^{\mathrm{rev}}$ is $w$ reversed.

Formalized by `Cslib.Complexity.Karp.Filter3.lits_ok`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#lits-ok).

## The capped filter fails on a clause with too many literals

Let $n \le 3$, let
$\ell_1, \dots, \ell_k$ be literals (pairs of a variable index and a polarity) with $3 < n + k$,
and let $w$ be the concatenation of the stack tokens of $\ell_1, \dots, \ell_k$. For all lists of
symbols $R$ and $U$ and every internal state $v$, the capped filter program, started at the
walking label for $n$ literals with internal state $v$, token stack $wR$ (top first) and side
stack $U$, reaches the failure label, with some internal state and some stacks, in at most $|w|$
steps.

Formalized by `Cslib.Complexity.Karp.Filter3.lits_fail`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#lits-fail).

## The 3SAT filter walks one clause within the cap

Let $C$ be a clause, and suppose the cap
flag is off or $C$ has at most three literals. Let $\overline{C}$ be the tokens of $C$ as they
lie on the token stack (the clause marker on top, then the literals' tokens, last literal first),
and let $w_n$ be the walking label after $n$ literals. For every $n$, all lists of symbols $R$
and $U$ and every value $v$ of the Boolean variable, there is a value $v'$ such that the 3SAT
clause-length filter takes exactly $|\overline{C}|$ steps from label $w_n$ with variable $v$,
token stack $\overline{C}$ on top of $R$ and side stack $U$ to label $w_{|C|}$ with variable
$v'$, token stack $R$, and side stack the reversal of $\overline{C}$ on top of $U$.

The clause marker resets the literal count, and each literal then advances it.

Formalized by `Cslib.Complexity.Karp.Filter3.clause_ok`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#clause-ok).

## A clause with more than three literals makes the capped 3SAT filter fail

Let $C$ be a
clause with more than three literals, let $\overline{C}$ be its tokens as they lie on the token
stack (the clause marker on top, then the literals' tokens, last literal first), and let $w_n$ be
the walking label after $n$ literals. For every $n$, all lists of symbols $R$ and $U$ and every
value $v$ of the Boolean variable, the 3SAT clause-length filter with the cap on reaches label
$\mathsf{fail}$, with some value of the variable and some stacks, in at most $|\overline{C}|$
steps from label $w_n$ with variable $v$, token stack $\overline{C}$ on top of $R$, and side
stack $U$.

Formalized by `Cslib.Complexity.Karp.Filter3.clause_fail`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#clause-fail).

## The 3SAT filter walks a list of clauses within the cap

For a clause $C$ let
$\overline{C}$ be its tokens as they lie on the token stack (the clause marker on top, then the
literals' tokens, last literal first). Let $C_1, \dots, C_k$ be clauses such that, for each $i$,
the cap flag is off or $C_i$ has at most three literals. Let $X$ be the concatenation
$\overline{C_1} \cdots \overline{C_k}$ with $\overline{C_1}$ on top, and let $w_n$ be the walking
label after $n$ literals. For every list of symbols $R$, every $n$, every list of symbols $U$ and
every value $v$ of the Boolean variable, there are $m$ and a value $v'$ such that the 3SAT
clause-length filter takes exactly $|X|$ steps from label $w_n$ with variable $v$, token stack
$X$ on top of $R$ and side stack $U$ to label $w_m$ with variable $v'$, token stack $R$, and side
stack the reversal of $X$ on top of $U$.

Formalized by `Cslib.Complexity.Karp.Filter3.cls_ok`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#cls-ok).

## A long clause makes the capped 3SAT filter fail on a list of clauses

For a clause $C$ let
$\overline{C}$ be its tokens as they lie on the token stack (the clause marker on top, then the
literals' tokens, last literal first). For a list of clauses $C_1, \dots, C_k$, let $X$ be the
concatenation $\overline{C_1} \cdots \overline{C_k}$ with $\overline{C_1}$ on top, and let $w_n$
be the walking label after $n$ literals. If some $C_i$ has more than three literals, then for
every list of symbols $R$, every $n$, every list of symbols $U$ and every value $v$ of the Boolean
variable, the 3SAT clause-length filter with the cap on reaches label $\mathsf{fail}$, with some
value of the variable and some stacks, in at most $|X|$ steps from label $w_n$ with variable $v$,
token stack $X$ on top of $R$, and side stack $U$.

Formalized by `Cslib.Complexity.Karp.Filter3.cls_fail`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#cls-fail).

## An empty token stack ends the walk

Let $\mathrm{cap}$ be a Boolean, $n \in \mathbb{N}$,
$U$ a list of symbols and $v$ a Boolean, and let $w_n$ be the walking label after $n$ literals.
The clause-length filter with cap flag $\mathrm{cap}$ goes in exactly one step from label $w_n$,
local variable $v$, empty token stack and side stack $U$ to the label $\mathrm{back}$, local
variable true, empty token stack and side stack $U$.

Formalized by `Cslib.Complexity.Karp.Filter3.walk_end`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#walk-end).

## One step of the 3SAT filter's return phase

For either value of the cap flag, every token
symbol $s$, all lists of symbols $R$ and $M$ and every value $v$ of the Boolean variable, the 3SAT
clause-length filter takes exactly one step from label $\mathsf{back}$ with variable $v$, token
stack $R$ and side stack $s$ on top of $M$ to label $\mathsf{back}$ with variable true, token
stack $s$ on top of $R$, and side stack $M$.

Formalized by `Cslib.Complexity.Karp.Filter3.back_step`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#back-step).

## The 3SAT filter's return phase moves the side stack back

For either value of the cap
flag, all lists of symbols $M$ and $R$ such that every symbol of $M$ is a token symbol, and every
value $v$ of the Boolean variable, there is a value $v'$ such that the 3SAT clause-length filter
takes exactly $|M|$ steps from label $\mathsf{back}$ with variable $v$, token stack $R$ and side
stack $M$ to label $\mathsf{back}$ with variable $v'$, token stack the reversal of $M$ on top of
$R$, and empty side stack.

Formalized by `Cslib.Complexity.Karp.Filter3.back_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#back-run).

## The return phase ends on an empty side stack

For either value of the cap flag, every
list of symbols $R$ and every value $v$ of the Boolean variable, the 3SAT clause-length filter
takes exactly one step from label $\mathsf{back}$ with variable $v$, token stack $R$ and empty
side stack to label $\mathsf{pass}$ with variable true, token stack $R$ and empty side stack.

Formalized by `Cslib.Complexity.Karp.Filter3.back_end`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#back-end).

## Correctness of the clause-length filter

Let $c$ be a Boolean (whether the filter is
capped), $\varphi$ a CNF formula and $v$ an internal state, and let $S$ be stacks holding the
reversed token list of $\varphi$ on the token stack $T$ and nothing on the side stack $U$. Let $b$
be the condition that $c$ is false or every clause of $\varphi$ has at most three literals, and
let $N$ be the number of tokens of $\varphi$. Then the filter program with cap $c$, started at its
start label with internal state $v$ and stacks $S$, reaches within $2N + 2$ steps the label pass
if $b$ holds and the label fail otherwise, with some internal state $v'$ and stacks $S'$; and if
$b$ holds, then $S' = S$.

Formalized by `Cslib.Complexity.Karp.Filter3.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatFilter.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#run-2).

## Emitter

An emitter is a multi-stack machine, given by a type of stacks and a type of
labels (both with decidable equality), an alphabet for each stack and a program with boolean
state, together with a start label and a different exit label at which the program halts, a
token stack and a different output stack, a bijection from the SAT token symbols to the token
stack's alphabet, a bijection from the output stack's alphabet to the booleans, an output map
$g$ from CNF formulas to bit strings, a bit string reserved as the output for undecodable inputs,
and a monotone step bound $B : \mathbb{N} \to \mathbb{N}$. It must satisfy: for every CNF formula
$\varphi$ whose token sequence has length $n$, every initial state, and all stack contents in
which the token stack holds the token sequence of $\varphi$ in reverse, each token translated by
the token bijection, and every other stack is empty, the program goes from the start label to
the exit label in at most $B(n)$ steps and ends with the output stack holding $g(\varphi)$, each
bit translated by the inverse of the output bijection.

Formalized by `Cslib.Complexity.Karp.Emitter`, a structure declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#emitter).

## Output of an emitter on a bit string

For an emitter $E$ with output map $g$ and a bit
string $x$: if the length-prefixed CNF decoder reads a CNF formula $\varphi$ from $x$ with no bits
left over, the output is $g(\varphi)$; otherwise it is the bit string that $E$ reserves as the
output for undecodable inputs.

Formalized by `Cslib.Complexity.Karp.TokThen.out`, a definition declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#out).

## Stacks of the tokenize-then-emit machine

The stacks of the tokenize-then-emit machine for
an emitter $E$ are the disjoint union of the SAT tokenizer's stacks and $E$'s stacks.

The copy of the tokenizer's own token stack $T$ stays unused: the tokenizer writes its tokens on
$E$'s token stack.

Formalized by `Cslib.Complexity.Karp.TokThen.K`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#k-3).

## Alphabets of the tokenize-then-emit machine

For an emitter $E$, every stack of the
combined machine that comes from the SAT tokenizer has the tokenizer's symbol alphabet, and every
stack $k$ that comes from $E$ has the alphabet of $k$ in $E$.

Formalized by `Cslib.Complexity.Karp.TokThen.Γ`, a definition declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#untitled-2).

## Labels of the tokenize-then-emit machine

For an emitter $E$, the labels of the combined
machine form the disjoint union of the SAT tokenizer's labels, the labels of $E$, and the two
booleans: false labels the step that writes the output $E$ fixes for undecodable input, and true
is the exit label.

Formalized by `Cslib.Complexity.Karp.TokThen.L`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#l).

## Exit label of the tokenize-then-emit machine

The labels of the tokenize-then-emit machine
for an emitter $E$ are the SAT tokenizer's labels, $E$'s labels and two extra labels indexed by
the booleans; the exit label is the extra label indexed by true.

Formalized by `Cslib.Complexity.Karp.TokThen.fin`, a definition declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#fin).

## Tokenizer stacks in the tokenize-then-emit machine

The map from the SAT tokenizer's
stacks to the stacks of the tokenize-then-emit machine for an emitter $E$ that sends the
tokenizer's token stack $T$ to $E$'s token stack, and each other tokenizer stack ($X$, $W$, $B$,
$CC$, $LC$) to its own copy among the tokenizer stacks of the combined machine.

Formalized by `Cslib.Complexity.Karp.TokThen.eT`, a definition declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#e-t).

## Embedding the tokenizer's stacks into tokenize-then-emit

The stack embedding of the SAT
tokenizer into the tokenize-then-emit machine for an emitter $E$: the tokenizer's token stack $T$
goes to $E$'s token stack, with token symbols translated by $E$'s bijection from token symbols to
that stack's alphabet, and each other tokenizer stack goes to its own copy among the tokenizer
stacks of the combined machine, with symbols left unchanged.

Formalized by `Cslib.Complexity.Karp.TokThen.embT`, a definition declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#emb-t).

## Embedding the emitter's stacks into tokenize-then-emit

The stack embedding of an emitter
$E$ into the tokenize-then-emit machine for $E$: each stack of $E$ goes to its own copy among the
emitter stacks of the combined machine, which carries the same alphabet, and symbols are left
unchanged.

Formalized by `Cslib.Complexity.Karp.TokThen.embE`, a definition declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#emb-e).

## Renaming the tokenizer's labels

For an emitter $E$, the tokenizer's accepting label goes
to the start label of $E$, its rejecting label goes to the label of the combined machine that
writes the output $E$ fixes for undecodable input, and every other tokenizer label goes to its own
copy among the combined machine's labels.

Formalized by `Cslib.Complexity.Karp.TokThen.φT`, a definition declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#t).

## Emitter labels in the tokenize-then-emit machine

The map from the labels of an emitter
$E$ to the labels of the tokenize-then-emit machine for $E$ that sends $E$'s exit label to the
machine's exit label, and every other label of $E$ to its own copy among the emitter labels.

Formalized by `Cslib.Complexity.Karp.TokThen.φE`, a definition declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#e).

## Program of the tokenize-then-emit machine

For an emitter $E$, the combined machine acts as
follows. At a label of the SAT tokenizer it runs the tokenizer's statement for that label, with the
tokenizer's token stack replaced by the token stack of $E$ (token symbols identified with those of
$E$), its other stacks kept as copies, and its labels renamed: acceptance goes to the start label
of $E$, rejection goes to the step that writes the undecodable-input output, and every other label
goes to its own copy. At a label of $E$ it runs the statement of $E$ on the stacks of $E$, with the
exit label of $E$ renamed to the exit label of the combined machine and every other label of $E$
kept. At the label for undecodable input it pushes, in one step, the fixed output that $E$ assigns
to undecodable input, as output symbols of $E$, onto the output stack of $E$ (so that the stack
then reads that output from the top) and goes to the exit label. At the exit label the machine
halts.

Formalized by `Cslib.Complexity.Karp.TokThen.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#prog-3).

## Start label of the tokenize-then-emit machine

For an emitter $E$, the combined machine
starts at the start label of the SAT tokenizer.

Formalized by `Cslib.Complexity.Karp.TokThen.start`, a definition declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#start-3).

## Initial stacks of the tokenize-then-emit machine

For a bit string $x$, the initial stack
contents of the tokenize-then-emit machine for an emitter $E$: the tokenizer's input stack $X$
holds the bits of $x$ in order, each written as a bit symbol, and every other stack is empty.

Formalized by `Cslib.Complexity.Karp.TokThen.init`, a definition declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#init).

## Initial stacks of the tokenizer

For a bit string $x$, the SAT tokenizer's initial stacks
hold $x$, as bit symbols, on the formula-bit stack $X$ and leave every other stack empty.

Formalized by `Cslib.Complexity.Karp.TokThen.tokS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#tok-s).

## Tokenize, then emit

Let $E$ be an emitter with step bound $B$, and let $x$ be a bit
string. The tokenize-then-emit machine for $E$, started at its start label with internal state
false, with $x$ as bit symbols on the tokenizer's input stack and every other stack empty,
reaches its exit label, with some internal state, in at most $2|x| + 3 + B(|x|)$ steps, and the
output stack of $E$ then holds the output on $x$, written in the output symbols of $E$.

Formalized by `Cslib.Complexity.Karp.TokThen.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#run-3).

## List of the tokenizer's stacks

The list of the SAT tokenizer's six stacks in the order:
the formula-bit stack $X$, the witness-bit stack $W$, the token stack $T$, the table stack $B$,
the clause counter $CC$ and the literal counter $LC$.

Formalized by `Cslib.Complexity.Karp.TokThen.tokKs`, a definition declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#tok-ks).

## The tokenize-then-emit machine as a host component

Given an emitter $E$ with finitely
many stacks, finite stack alphabets and finitely many labels, and a list of $E$'s stacks that
contains every stack exactly once, this is the reduction-host component whose stacks, alphabets,
labels and program are those of the tokenize-then-emit machine for $E$, with its stacks listed
as the SAT tokenizer's six stacks followed by the given list of $E$'s stacks.

Formalized by `Cslib.Complexity.Karp.TokThen.comp`, a definition declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#comp).

## Emitter reductions out of SAT are polynomial-time

Let $E$ be an emitter with finitely
many stacks, finite stack alphabets and finitely many labels, given together with a list of its
stacks that contains every stack exactly once. Write $B$ for the step bound of $E$, $g$ for its
output map and $o$ for its output on undecodable inputs, and let $p$ be a polynomial with
natural-number coefficients such that $2n + 3 + B(n) \le p(n)$ for every $n$. Then the map
sending a bit string $x$ to $g(\varphi)$ when $x$ is the binary code of a CNF formula $\varphi$
(its clause count in unary followed by the encoded clauses), and to $o$ otherwise, is
polynomial-time computable for the canonical bit-string encoding of lists of booleans.

Formalized by `Cslib.Complexity.Karp.TokThen.isPolyTime_out`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/TokThen.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/TokThen.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#is-poly-time-out).

## Transitivity of polynomial-time many-one reductions

For decision problems $L_1$, $L_2$
and $L_3$, if $L_1$ has a polynomial-time many-one reduction to $L_2$ and $L_2$ has one to $L_3$,
then $L_1$ has a polynomial-time many-one reduction to $L_3$.

Formalized by `Cslib.Complexity.Karp.polyManyOneRed_trans`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#poly-many-one-red-trans).

## NP-hardness transfers along reductions

Let $L$ and $L'$ be decision problems. If every
decision problem in NP has a polynomial-time many-one reduction to $L$, and $L$ has a
polynomial-time many-one reduction to $L'$, then every decision problem in NP has a
polynomial-time many-one reduction to $L'$.

Formalized by `Cslib.Complexity.Karp.npHard_of_polyManyOneRed`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#np-hard-of-poly-many-one-red).

## The SAT-to-3SAT emitter

The emitter whose stacks, stack alphabets, labels, program, start
label and exit label are those of the 3SAT emitter machine, with that machine's token stack as its
token stack and its bit-valued output stack as its output stack. Its output on a CNF formula
$\varphi$ is the binary encoding of the SAT-to-3SAT translation of $\varphi$, its output on a bit
string that encodes no CNF formula is the empty bit string, and its step bound is
$B(n) = 8(n+1)^2$: started at its start label with the reversed token sequence of $\varphi$ on the
token stack and every other stack empty, it reaches its exit label within $B(n)$ steps, where $n$
is the number of tokens of $\varphi$, with the output for $\varphi$ on the output stack.

Formalized by `Cslib.Complexity.Karp.emit3`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#emit3).

## The stacks of the 3SAT emitter

The list of all six stacks of the SAT-to-3SAT emitter
machine, each listed once, in the order: token stack, output stack, fresh-variable counter, two
scratch counters, output clause counter.

Formalized by `Cslib.Complexity.Karp.emit3Ks`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#emit3-ks).

## The SAT-to-3SAT reduction is polynomial-time

The map on bit strings that sends the
binary encoding of a CNF formula $\varphi$ to the binary encoding of the SAT-to-3SAT translation
of $\varphi$, and sends every bit string that encodes no CNF formula to the empty bit string, is
computable in polynomial time.

Formalized by `Cslib.Complexity.Karp.isPolyTime_reduce3`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#is-poly-time-reduce3).

## SAT reduces to 3SAT

The decision problem SAT, which accepts exactly the bit strings that
encode a satisfiable CNF formula, has a polynomial-time many-one reduction to the decision problem
3SAT, which accepts exactly the bit strings that encode a satisfiable CNF formula with at most
three literals per clause.

Formalized by `Cslib.Complexity.Karp.satDec_polyManyOneRed_sat3Dec`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#sat-dec-poly-many-one-red-sat3-dec).

## 3SAT is NP-hard

Every decision problem in NP has a polynomial-time many-one reduction to
the decision problem 3SAT, which accepts exactly the bit strings that encode a satisfiable CNF
formula with at most three literals per clause.

Formalized by `Cslib.Complexity.Karp.sat3Dec_npHard`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#sat3-dec-np-hard).

## 3SAT is NP-complete

The decision problem 3SAT, which accepts exactly the bit strings
that encode a satisfiable CNF formula with at most three literals per clause, is in NP, and every
decision problem in NP has a polynomial-time many-one reduction to 3SAT.

Formalized by `Cslib.Complexity.Karp.sat3Dec_npComplete`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ThreeSatComplete.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html#sat3-dec-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: 3-satisfiability](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-satisfiability)
