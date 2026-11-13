---
declaration: section
origin: cited
lean: Cslib.CookLevin.varsOf, Cslib.CookLevin.lookupVar, Cslib.CookLevin.checkClause, Cslib.CookLevin.checkCNF, Cslib.CookLevin.satVerifier, Cslib.CookLevin.lookupVar_time_le, Cslib.CookLevin.lookupVar_ret_map, Cslib.CookLevin.checkClause_ret
statement: formalized
proof: formalized
---

# Polynomial-time verifier for SAT

146 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/index.html).

## Occurrence list of a CNF formula

For a CNF formula $\varphi = (C_1, \dots, C_m)$, the
occurrence list of $\varphi$ is the list of the variable indices of its literals, in order: the
variables of the literals of $C_1$ in order, then those of $C_2$, and so on up to $C_m$.
Duplicates are kept, so a variable appears once for each literal in which it occurs.

Formalized by `Cslib.CookLevin.varsOf`, a definition declared in [CSLibExt/Computability/SatTimeM.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#vars-of).

## Witness lookup

Given a list $N = (n_1, \dots, n_k)$ of natural numbers, a list
$w = (b_1, \dots, b_m)$ of booleans and a natural number $x$, the lookup of $x$ in $N$ and $w$ is
the timed computation (a returned boolean together with a natural-number cost) that scans the
pairs $(n_1, b_1), (n_2, b_2), \dots$ in order, charging one tick for each pair it examines, and
returns $b_i$ for the first $i$ with $n_i = x$; if either list runs out first, it returns false at
no further cost.

It is used with $N$ the variables occurring in a formula and $w$ the witness values, so the first
occurrence of a variable wins.

Formalized by `Cslib.CookLevin.lookupVar`, a definition declared in [CSLibExt/Computability/SatTimeM.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#lookup-var).

## Clause check against a witness

Given a list $N$ of natural numbers, a list $w$ of
booleans and a CNF clause $C$, the check of $C$ against $N$ and $w$ is the timed computation (a
returned boolean together with a natural-number cost) that scans the literals $(x, b)$ of $C$ in
order: for each it charges one tick, then looks up $x$ in $N$ and $w$, paying the cost of the
lookup, and returns true if the value found equals the polarity $b$; otherwise it moves on to the
next literal. When the literals are exhausted it returns false at no further cost; in particular
the empty clause fails.

Formalized by `Cslib.CookLevin.checkClause`, a definition declared in [CSLibExt/Computability/SatTimeM.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#check-clause).

## Formula check against a witness

Given a list $N$ of natural numbers, a list $w$ of
booleans and a CNF formula $\varphi$, the check of $\varphi$ against $N$ and $w$ is the timed
computation that runs the clause check against $N$ and $w$ on the clauses of $\varphi$ in order,
adding up their costs, and returns false as soon as one of them returns false. If every clause
check returns true, in particular if $\varphi$ has no clauses, it returns true.

Formalized by `Cslib.CookLevin.checkCNF`, a definition declared in [CSLibExt/Computability/SatTimeM.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#check-cnf).

## The SAT verifier

The SAT verifier takes a pair $(x, w)$ of lists of Booleans, an input
$x$ and a witness $w$, and returns a Boolean together with a declared time cost. If the complete
CNF decoder fails on $x$, it returns false at cost $0$. If $x$ decodes to a CNF formula
$\varphi$, it returns the result and the cost of the CNF check of $\varphi$ against the witness
$w$ and the occurrence list of $\varphi$, so that $w$ is read as values for the variables of
$\varphi$ in order of occurrence.

Decoding the input is uncharged preprocessing: it adds nothing to the declared cost.

Formalized by `Cslib.CookLevin.satVerifier`, a definition declared in [CSLibExt/Computability/SatTimeM.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#sat-verifier).

## Cost bound for witness lookup

For every list $N$ of natural numbers, every list $w$ of
booleans and every natural number $x$, the cost of looking up $x$ in $N$ and $w$ is at most the
length of $N$.

Formalized by `Cslib.CookLevin.lookupVar_time_le`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#lookup-var-time-le).

## Lookup in the witness of an assignment

Let $v$ be a function from the natural numbers to
the booleans, $N = (n_1, \dots, n_k)$ a list of natural numbers and $x$ a natural number. Looking
up $x$ in $N$ and the list $(v(n_1), \dots, v(n_k))$ returns $v(x)$ if $x$ occurs in $N$, and false
otherwise.

Formalized by `Cslib.CookLevin.lookupVar_ret_map`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#lookup-var-ret-map).

## Correctness of the witness clause check

Let $N$ be a list of natural numbers, $w$ a list
of booleans and $C$ a CNF clause. The check of $C$ against $N$ and $w$ returns true if and only
if $C$ is satisfied by the assignment that sends each natural number $x$ to the value returned by
looking up $x$ in $N$ and $w$.

Formalized by `Cslib.CookLevin.checkClause_ret`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#check-clause-ret).

## Cost bound for the witness clause check

Let $N$ be a list of natural numbers, $w$ a list
of booleans and $C$ a CNF clause, viewed as a list of $\ell$ literals (repetitions counted). The
cost of checking $C$ against $N$ and $w$ is at most $\ell \cdot (|N| + 1)$, where $|N|$ is the
length of $N$.

Each literal examined costs one tick plus one lookup, and a lookup costs at most $|N|$.

Formalized by `Cslib.CookLevin.checkClause_time_le`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#check-clause-time-le).

## Correctness of the witness formula check

Let $N$ be a list of natural numbers, $w$ a list
of booleans and $\varphi$ a CNF formula. The check of $\varphi$ against $N$ and $w$ returns true if
and only if $\varphi$ is satisfied by the assignment that sends each natural number $x$ to the value
returned by looking up $x$ in $N$ and $w$.

Formalized by `Cslib.CookLevin.checkCNF_ret`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#check-cnf-ret).

## Cost bound for the witness formula check

Let $N$ be a list of natural numbers, $w$ a list
of booleans and $\varphi$ a CNF formula, and let $L$ be the sum of the lengths of the clauses of
$\varphi$ (its total number of literals). The cost of checking $\varphi$ against $N$ and $w$ is at
most $L \cdot (|N| + 1)$, where $|N|$ is the length of $N$.

Formalized by `Cslib.CookLevin.checkCNF_time_le`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#check-cnf-time-le).

## Length of the occurrence list

For every CNF formula $\varphi$, the length of the
occurrence list of $\varphi$ equals the total number of literals of $\varphi$, that is, the sum
over the clauses of $\varphi$ of their lengths.

Formalized by `Cslib.CookLevin.varsOf_length`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#vars-of-length).

## Variables of a formula occur in its occurrence list

Let $\varphi$ be a CNF formula, $C$ a
clause of $\varphi$ and $(x, b)$ a literal of $C$. Then $x$ belongs to the list of variables
occurring in $\varphi$.

Formalized by `Cslib.CookLevin.mem_varsOf`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#mem-vars-of).

## The literal count is at most the code length

For every CNF formula $\varphi$, the sum
over the clauses of $\varphi$ of their lengths (the total number of literals of $\varphi$) is at
most the length of the length-prefixed binary code of $\varphi$.

Each encoded clause contributes at least its literal count.

Formalized by `Cslib.CookLevin.sum_length_le_encodeCNF_length`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#sum-length-le-encode-cnf-length).

## The SAT verifier rejects undecodable inputs

For all lists of Booleans $x$ and $w$, if
the complete CNF decoder fails on $x$, then the SAT verifier on $(x, w)$ returns false at
declared time cost $0$.

Formalized by `Cslib.CookLevin.satVerifier_none`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#sat-verifier-none).

## The SAT verifier on a decodable input

For all lists of Booleans $x$ and $w$ and every
CNF formula $\varphi$, if the complete CNF decoder returns $\varphi$ on $x$, then the SAT verifier
on $(x, w)$ coincides with the CNF check of $\varphi$ against the witness $w$ and the occurrence
list of $\varphi$: both the returned Boolean and the declared time cost are the same.

Formalized by `Cslib.CookLevin.satVerifier_some`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#sat-verifier-some).

## Declared time bound of the SAT verifier

For all lists of Booleans $x$ (the input) and
$w$ (the witness), the declared time cost of the SAT verifier on $(x, w)$ is at most $N^2 + N$,
where $N = |x| + |w|$ is the sum of their lengths.

If $x$ decodes to a formula with $n$ literals, then $n \le N$ and the check costs at most
$n(n + 1) \le N(N + 1)$.

Formalized by `Cslib.CookLevin.satVerifier_time_le`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#sat-verifier-time-le).

## The SAT verifier has polynomial declared time

There is a polynomial $q$ with natural
number coefficients such that for all lists of Booleans $x$ (the input) and $w$ (the witness),
the declared time cost of the SAT verifier on $(x, w)$ is at most $q(|x| + |w|)$.

One can take $q = X^2 + X$. This bounds only the trusted cost annotation.

Formalized by `Cslib.CookLevin.satVerifier_verifierInDeclaredPolyTime`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#sat-verifier-verifier-in-declared-poly-t).

## The SAT verifier verifies SAT

The SAT verifier verifies the SAT decision problem with
witness bound the polynomial $X$: for every list $x$ of Booleans, $x$ encodes a satisfiable CNF
formula if and only if there is a list $w$ of Booleans, of length at most the length of $x$, such
that the SAT verifier on $(x, w)$ returns true.

The intended witness lists values for the variables occurring in the decoded formula, in order of
occurrence; its length is the literal count, which is at most the input length.

Formalized by `Cslib.CookLevin.satVerifier_verifies`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#sat-verifier-verifies).

## SAT is in NP if its verifier is polynomial-time

If the function sending a pair $(x, w)$
of lists of Booleans to the Boolean returned by the SAT verifier on $(x, w)$ is polynomial-time
computable, by a multi-stack Turing machine under the canonical bitstring encodings, then the
SAT decision problem belongs to NP.

This hypothesis must be proved separately: it does not follow from the polynomial bound on the
SAT verifier's declared time, which constrains only a trusted cost annotation and leaves the
decoding of the input uncharged.

Formalized by `Cslib.CookLevin.satDec_mem_NP_of_isPolyTime`, a theorem declared in [CSLibExt/Computability/SatTimeM.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/SatTimeM.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-01/index.html#sat-dec-mem-np-of-is-poly-time).

## Stack alphabet of the SAT verifier

The symbols of the token and table stacks are a name
bit $b$ for each boolean $b$, a polarity marker for each polarity $p$, a clause end marker, a
value marker for each boolean $b$, and a dead marker. Equality of symbols is decidable.

Formalized by `Cslib.Complexity.SatVerifier.Sym`, an inductive type declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#sym).

## Reading a symbol as a name bit

A symbol of the token and table stacks that is the name
bit $b$ reads as the bit $b$; every other symbol reads as no bit, and so ends a name block.

Formalized by `Cslib.Complexity.SatVerifier.Sym.bit?`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#bit).

## Tokens of a literal

For a literal $(n, p)$ with variable index $n$ and polarity $p$,
the token list is one bit symbol for each bit of the canonical binary representation of $n$
(least significant bit first, empty for $n = 0$), in order, followed by the polarity marker
symbol for $p$.

Formalized by `Cslib.Complexity.SatVerifier.litToks`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#lit-toks).

## Tokens of a clause

The tokens of a CNF clause are the tokens of its literals, in order,
followed by the clause-end symbol.

Formalized by `Cslib.Complexity.SatVerifier.clauseToks`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#clause-toks).

## Token sequence of a CNF formula

For a CNF formula $\varphi$ with clauses
$C_1, \dots, C_k$ (in order), the token sequence of $\varphi$ is the concatenation of the token
sequences of $C_1, \dots, C_k$. The token sequence of a clause is the concatenation of the token
sequences of its literals, in order, followed by a clause-end symbol; the token sequence of a
literal with variable index $n \in \mathbb{N}$ and polarity $p$ is the bits of the binary
encoding of $n$ (Mathlib's `encodeNat`), each as a name-bit symbol, followed by a polarity
marker for $p$.

The verifier's token stack holds this sequence in reverse order.

Formalized by `Cslib.Complexity.SatVerifier.toks`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#toks).

## Table entries

A table entry is a pair of a name, which is a list of bits, and an optional
bit, its value; the value is absent for occurrences past the end of the witness.

Formalized by `Cslib.Complexity.SatVerifier.Ent`, an abbreviation declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#ent).

## Closing marker of a table entry

The marker closing a table entry whose value is the
boolean $b$ is the value symbol for $b$; for an entry with no value it is the dead symbol.

Formalized by `Cslib.Complexity.SatVerifier.markOf`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#mark-of).

## Symbols of a table entry

The symbols of a table entry with name $q$ and value $v$ are the
bits of $q$ as name-bit symbols, in order, followed by one closing marker: the value marker of $b$
if $v$ is a bit $b$, and the dead marker if $v$ is absent.

Formalized by `Cslib.Complexity.SatVerifier.entToks`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#ent-toks).

## Table stack of an entry list

Write each table entry as one bit symbol per bit of its
name followed by its closing marker (the value symbol for its value, or the dead symbol if it
has no value), and concatenate these in the order of the list. The table stack is the reverse
of this sequence, with the head as the top of the stack, so the first entry lies at the bottom.

Formalized by `Cslib.Complexity.SatVerifier.tblStk`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#tbl-stk).

## Occurrence table of a list of variables

Given natural numbers $n_0, \dots, n_{k-1}$ and a
list $w$ of bits, the occurrence table is the list of $k$ table entries whose $i$-th entry has as
name the binary code of $n_i$ (Mathlib's encoding of natural numbers as bit lists) and as value
the bit $w_i$ if $i$ is less than the length of $w$, and no value otherwise.

Formalized by `Cslib.Complexity.SatVerifier.entsOf`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#ents-of).

## Occurrence table of a formula and a witness

Let $\varphi$ be a CNF formula, $w$ a list
of booleans, and $n_0, \dots, n_{k-1}$ the variable indices of the literals of $\varphi$ in
reading order, with repetitions. The occurrence table is the list of $k$ entries whose $i$-th
entry pairs the binary name of $n_i$ (its canonical binary representation, least significant
bit first, empty for $0$) with the value $w_i$ if $i$ is less than the length of $w$, and with
no value otherwise.

Formalized by `Cslib.Complexity.SatVerifier.ents`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#ents).

## Live value of a name in a table

Given a list of table entries, each pairing a name (a
bit string) with either a boolean value or no value, and a bit string $q$, the live value of
$q$ is the value of the first entry whose name is $q$ and which carries a value, or false if
there is no such entry.

Formalized by `Cslib.Complexity.SatVerifier.liveVal`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#live-val).

## Clause check against an occurrence table

For a CNF formula $\varphi$ and a list $es$ of
table entries, the clause check is true exactly when every clause of $\varphi$ contains a literal
$(x, p)$ whose live value equals its polarity $p$. Here the live value of $x$ is the value of the
first entry of $es$ that is named by the binary code of $x$ and has a value, and false if there
is no such entry.

Formalized by `Cslib.Complexity.SatVerifier.checkSpec`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#check-spec).

## Tokenizer of the SAT verifier

Given bit strings $x$ and $w$, the tokenizer rejects
(returns no result) if $x$ does not decode to a CNF formula. If $x$ decodes to a formula
$\varphi$, it returns the pair consisting of the token stack, the reverse of the tokens of
$\varphi$ in reading order, and the table stack of the occurrence table of $\varphi$ and $w$.

Formalized by `Cslib.Complexity.SatVerifier.tokenize`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#tokenize).

## The binary code of natural numbers is injective

For natural numbers $m$ and $n$, the
binary codes of $m$ and $n$ (Mathlib's encoding of natural numbers as bit lists) are equal if and
only if $m = n$.

Formalized by `Cslib.Complexity.SatVerifier.encodeNat_inj`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#encode-nat-inj).

## Canonical binary names

For every list $l$ of bits, encoding the natural number that $l$
decodes to (Mathlib's binary code of natural numbers, least significant bit first) gives back $l$
if and only if $l$ is empty or its last bit is true.

Formalized by `Cslib.Complexity.SatVerifier.encodeNat_decodeNat_eq_iff`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#encode-nat-decode-nat-eq-iff).

## Table lookup agrees with the verifier's variable lookup

Let $n = (n_0, \dots, n_{k-1})$
be a list of natural numbers, $w$ a list of booleans and $x$ a natural number. Write $[m]$ for
the binary name of a natural number $m$: its canonical binary representation, least significant
bit first, empty for $m = 0$. Form the table whose $i$-th entry, for $i < k$, pairs $[n_i]$
with $w_i$ if $i$ is less than the length of $w$, and with no value otherwise. Then the live
value of $[x]$ in this table (the value of the first entry named $[x]$ that carries a value, or
false if there is none) equals the return value of the verifier's lookup of $x$ in the lists
$n$ and $w$: the value $w_i$ for the first $i$ below both $k$ and the length of $w$ with
$n_i = x$, or false if there is none.

Formalized by `Cslib.Complexity.SatVerifier.liveVal_entsOf`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#live-val-ents-of).

## The clause check on the occurrence table is the formula check

For every CNF formula
$\varphi$ and every list $w$ of bits, the clause check of $\varphi$ against the occurrence table
of $\varphi$ and $w$ equals the value returned (ignoring the time count) by the formula check of
$\varphi$ against $w$ that uses the variable occurrences of $\varphi$, in order, as its variable
list.

Formalized by `Cslib.Complexity.SatVerifier.checkSpec_ents`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#check-spec-ents).

## The SAT verifier's answer through the occurrence table

For all lists $x$ and $w$ of bits,
the value returned by the SAT verifier on $(x, w)$, ignoring the time count, is false if the
complete length-prefixed CNF decoder fails on $x$, and is the clause check of $\varphi$ against
the occurrence table of $\varphi$ and $w$ if $x$ decodes to the CNF formula $\varphi$.

Formalized by `Cslib.Complexity.SatVerifier.satVerifier_ret_eq`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#sat-verifier-ret-eq).

## A clause has at most as many tokens as code bits

For every CNF clause $C$, the number
of tokens of $C$ is at most the length of the binary code of $C$.

Formalized by `Cslib.Complexity.SatVerifier.clauseToks_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-02/index.html#clause-toks-length-le).

## Token count is bounded by the encoding length

For every CNF formula $\varphi$, the
number of tokens of $\varphi$ is at most the length of the binary encoding of $\varphi$.

Formalized by `Cslib.Complexity.SatVerifier.toks_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierSpec.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierSpec.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#toks-length-le).

## Stacks of the clause check

The eight stacks of the clause-check machine: $T$ (tokens),
$B$ (table), $S$ (the lookup's stash), $A$ and $C$ (the lookup's scratch stacks), $V$ (looked-up
value), $P$ (polarity) and $F$ (clause flag).

Formalized by `Cslib.Complexity.SatVerifier.Check.K`, an inductive type declared in [CSLibExt/Computability/Complexity/SatCheck.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatCheck.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#k).

## Driver labels of the clause check

The seven labels of the clause-check driver: start
(begin the next clause), lits (read the next literal), ret (return from the lookup), drop
(discard a literal's name bits), endc (end of a clause), yes (accept) and no (reject).

Formalized by `Cslib.Complexity.SatVerifier.Check.DLab`, an inductive type declared in [CSLibExt/Computability/Complexity/SatCheck.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatCheck.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#dlab).

## Clause-check statements

For a label set $L$, the statements of a multi-stack Turing
machine with the eight driver stacks, each over the symbols of the token and table stacks, with
labels in $D \sqcup L$, where $D$ is the set of driver labels, and with a Boolean internal
state.

Formalized by `Cslib.Complexity.SatVerifier.Check.Stmt`, an abbreviation declared in [CSLibExt/Computability/Complexity/SatCheck.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatCheck.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#stmt).

## Configurations of the clause-check machine

For a type $LL$ of lookup labels, a
configuration of the multi-stack Turing machine of the clause check: a current label (absent once
the machine halts) that is either a driver label or a label in $LL$, a Boolean internal state,
and the contents of the eight stacks $T$, $B$, $S$, $A$, $C$, $V$, $P$, $F$ of the clause check,
each a list of symbols of the token and table stacks (name bits, literal and clause markers, and
table markers).

Formalized by `Cslib.Complexity.SatVerifier.Check.Cfg`, an abbreviation declared in [CSLibExt/Computability/Complexity/SatCheck.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatCheck.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#cfg).

## Calling the lookup

For the lookup's start label $l_0$ and a polarity $p$, the statement
that pops the top of the token stack $T$, pushes the bit $p$ onto the polarity stack $P$, and
then goes to label $l_0$.

Formalized by `Cslib.Complexity.SatVerifier.Check.callS`, a definition declared in [CSLibExt/Computability/Complexity/SatCheck.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatCheck.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#call-s).

## The clause-check driver

Given the lookup's start label $l_0$, the statement at each
driver label. At start: if the token stack $T$ is empty, go to yes; if its top is a clause
marker, pop it, push the bit false onto the flag stack $F$ and go to lits; otherwise go to no.
At lits: if the top of $T$ is a literal marker of polarity $p$, pop it, push the bit $p$ onto
the polarity stack $P$ and go to $l_0$; otherwise go to endc. At ret: if the top of the value
stack $V$ is the bit true exactly when the top of $P$ is the bit true, pop $F$ and push the bit
true onto it; in either case then pop $V$, pop $P$ and go to drop. At drop: if the top of $T$
is a bit, pop it and go to drop; otherwise go to lits. At endc: if the top of $F$ is the bit
true, pop it and go to start; otherwise go to no. At yes and at no: halt.

Formalized by `Cslib.Complexity.SatVerifier.Check.drv`, a definition declared in [CSLibExt/Computability/Complexity/SatCheck.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatCheck.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#drv).

## The clause-check driver with a lookup sub-program

Given a lookup sub-program $lk$ on a
label set $L$ and an entry label $l_0 \in L$, this is the program on the labels $D \sqcup L$, where
$D$ is the set of driver labels: at a driver label $d$ it runs the driver's statement for $d$
(the driver calls the lookup by jumping to $l_0$), and at a label $l \in L$ it runs $lk(l)$.

Formalized by `Cslib.Complexity.SatVerifier.Check.prog`, a definition declared in [CSLibExt/Computability/Complexity/SatCheck.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatCheck.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#prog).

## The lookup contract

A lookup sub-program $lk$ with start label $l_0$ meets the contract
with constants $a$ and $b$ when the following holds. For every name $q$ (a list of bits), every
table $es$, with table stack $B_{es}$, and every list of symbols $R$ whose first symbol, if any,
is not a bit, start the clause-check machine with lookup $lk$ at label $l_0$, with any internal
state and with stack contents that have the bits of $q$ in reverse order followed by $R$ on the
token stack $T$, $B_{es}$ on $B$, and $S$, $A$, $C$, $V$ empty. Then it reaches label ret in at
most $a \cdot |B_{es}| + b$ steps, with some internal state, with $V$ holding exactly the bit
that is the live value of $q$ in $es$, and with every other stack unchanged.

Formalized by `Cslib.Complexity.SatVerifier.Check.LookupSpec`, a definition declared in [CSLibExt/Computability/Complexity/SatCheck.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatCheck.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#lookup-spec).

## A literal's tokens on the token stack

For a literal $(n, p)$ with variable index $n$ and
polarity $p$, the list of symbols consisting of the literal marker of polarity $p$ followed by
the bits of the binary encoding of $n$ (least significant bit first, empty for $n = 0$) in
reverse order.

Formalized by `Cslib.Complexity.SatVerifier.Check.litRev`, a definition declared in [CSLibExt/Computability/Complexity/SatCheck.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatCheck.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#lit-rev).

## A clause's tokens on the token stack

For a clause with literals $l_1, \dots, l_k$, the
list of symbols consisting of the clause marker followed by the stack tokens of $l_k$, then of
$l_{k-1}$, down to $l_1$, where the stack tokens of a literal $(n, p)$ are the literal marker of
polarity $p$ followed by the bits of the binary encoding of $n$ (least significant bit first,
empty for $n = 0$) in reverse order.

Formalized by `Cslib.Complexity.SatVerifier.Check.clRev`, a definition declared in [CSLibExt/Computability/Complexity/SatCheck.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatCheck.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#cl-rev).

## Literal loop of the clause check

Suppose the lookup sub-program $lk$ with start label
$l_0$ meets the lookup contract with constants $a$ and $b$. Let $es$ be a table with table stack
$B_{es}$, let $R$ be a list of symbols that is empty or starts with a clause marker, and let $s$
be a bit. The stack tokens of a literal $(n, p)$ are the literal marker of polarity $p$
followed by the bits of the binary encoding of $n$ (least significant bit first, empty for
$n = 0$) in reverse order. Let $l_1, \dots, l_k$ be literals whose stack tokens have total
length $N$. Start the clause-check machine with lookup $lk$ at label lits, with any internal
state and with the stack tokens of $l_1$, then of $l_2$, up to $l_k$, followed by $R$ on the
token stack $T$, $B_{es}$ on $B$, the single bit $s$ on the flag stack $F$, and $S$, $A$, $C$,
$V$, $P$ empty. Then it reaches label endc in at most
$k \cdot (a \cdot |B_{es}| + b + 2) + N + 1$ steps, with some internal state, with $T$ holding
$R$, with $F$ holding the single bit that is true exactly when $s$ is true or some literal
$l_i = (n, p)$ has live value of the binary encoding of $n$ in $es$ equal to $p$, and with
every other stack unchanged.

Formalized by `Cslib.Complexity.SatVerifier.Check.lits_run`, a theorem declared in [CSLibExt/Computability/Complexity/SatCheck.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatCheck.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#lits-run).

## Clause loop of the clause check

Suppose the lookup sub-program $lk$ with start label
$l_0$ meets the lookup contract with constants $a$ and $b$. Let $es$ be a table with table stack
$B_{es}$, and let $\varphi$ be a CNF formula with clauses $D_1, \dots, D_m$. The stack tokens
of a clause are its clause marker followed by the stack tokens of its literals, last literal
first, where the stack tokens of a literal $(n, p)$ are the literal marker of polarity $p$
followed by the bits of the binary encoding of $n$ (least significant bit first, empty for
$n = 0$) in reverse order. Let $N$ be the total length of the stack tokens of
$D_1, \dots, D_m$. Start the clause-check machine with lookup $lk$ at label start, with any
internal state and with the stack tokens of $D_1$, then of $D_2$, up to $D_m$ on the token
stack $T$, $B_{es}$ on $B$, and $S$, $A$, $C$, $V$, $P$, $F$ empty. Then within
$N \cdot (a \cdot |B_{es}| + b + 5) + 1$ steps it reaches, with some internal state and some
stack contents, label yes if every clause $D_j$ has a literal $(n, p)$ such that the live value
of the binary encoding of $n$ in $es$ is $p$, and label no otherwise.

Formalized by `Cslib.Complexity.SatVerifier.Check.clauses_run`, a theorem declared in [CSLibExt/Computability/Complexity/SatCheck.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatCheck.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#clauses-run).

## The clause check

Suppose the lookup sub-program $lk$ with entry label $l_0$ satisfies
the lookup contract with constants $a, b \in \mathbb{N}$. Let $\varphi$ be a CNF formula, $es$ a
list of table entries, $t$ the token list of $\varphi$ and $m$ the length of the table stack of
$es$. Start the driver with lookup $lk$ at its start label, with any internal state, with $t$
reversed on the token stack, the table stack of $es$ on the table stack, and the other six stacks
empty. Then within at most $|t| \cdot (a m + b + 5) + 1$ steps it reaches the label yes, with
some internal state and some stack contents, if every clause of $\varphi$ has a literal whose
polarity equals the value of its variable, and it reaches the label no otherwise. Here the value
of a variable $n$ is the value of the first entry of $es$ that is named by the binary encoding of
$n$ and has a value, or false if there is no such entry.

Formalized by `Cslib.Complexity.SatVerifier.Check.run`, a theorem declared in [CSLibExt/Computability/Complexity/SatCheck.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatCheck.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#run).

## Stacks of the lookup machine

The lookup machine has six stacks: the query stack $T$, the
table stack $B$, the stash $S$, the two scratch stacks $A$ and $C$ used for comparisons, and the
value stack $V$.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.K`, an inductive type declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#k-2).

## Labels of the lookup machine

The lookup machine has the labels $\mathsf{init}$,
$\mathsf{scan}$, $\mathsf{cmp}(b)$ and $\mathsf{put}(b)$ for each bit $b$, $\mathsf{rstT}$,
$\mathsf{rstB}$, $\mathsf{mvN}$, $\mathsf{back}$, $\mathsf{mark}$ and $\mathsf{done}$. The labels
$\mathsf{cmp}(b)$ and $\mathsf{put}(b)$ serve a live table entry with value $b$.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#lab).

## Moving a symbol between stacks

For stacks $a$ and $b$, a symbol $x$ and a map $f$ from
symbols to labels, this machine instruction pops the top of $a$ (if any), pushes $x$ onto $b$ and
goes to the label $f(x)$.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.mvSym`, a definition declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#mv-sym).

## Moving a table marker between stacks

For stacks $a$ and $b$, a label $e$ and a map $f$
from symbols to labels, this machine instruction does the following: if the top of $a$ is a table
marker $y$ (that is, $\mathsf{dead}$ or $\mathsf{val}(c)$ for a bit $c$), it pops $y$ from $a$,
pushes it onto $b$ and goes to $f(y)$; if $a$ is empty or has another symbol on top, it goes to
$e$ and leaves the stacks unchanged.

The invariants of the lookup machine rule out another symbol on top of $a$.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.mvMark`, a definition declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#mv-mark).

## Next label of the lookup scan

The label at which the lookup scan continues after moving
a marker symbol $x$: the comparison label $\mathsf{cmp}(b)$ if $x$ is the value marker
$\mathsf{val}(b)$, and the name-moving label $\mathsf{mvN}$ for every other symbol.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.scanNext`, a definition declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#scan-next).

## The lookup program

The lookup machine works on the stacks $T$, $B$, $S$, $A$, $C$ and
$V$ and acts at each label as follows. At $\mathsf{init}$ it pushes the bit symbol of false onto
$V$ and goes to $\mathsf{scan}$. At $\mathsf{scan}$, if the top of $B$ is a table marker it moves
that marker onto $S$ and goes to $\mathsf{cmp}(b)$ if the marker is $\mathsf{val}(b)$ and to
$\mathsf{mvN}$ if it is $\mathsf{dead}$; if $B$ is empty or has another symbol on top it goes to
$\mathsf{back}$. At $\mathsf{cmp}(b)$ it compares the bit blocks on top of $T$ and $B$: while
both tops are equal bits it pops them, pushes that bit symbol onto $A$ and onto $C$ and stays at
$\mathsf{cmp}(b)$; when both blocks end together it goes to $\mathsf{put}(b)$, and on a mismatch
(different bits, or one block ending first) it goes to $\mathsf{rstT}$ without popping. At
$\mathsf{put}(b)$ it pops $V$, pushes the bit symbol of $b$ onto $V$ and goes to
$\mathsf{rstT}$. At $\mathsf{rstT}$, $\mathsf{rstB}$, $\mathsf{mvN}$ and $\mathsf{back}$ it moves
the bit block on top of $A$ onto $T$, of $C$ onto $B$, of $B$ onto $S$ and of $S$ onto $B$
respectively, staying at the label while the top is a bit and then going to $\mathsf{rstB}$,
$\mathsf{mvN}$, $\mathsf{scan}$ and $\mathsf{mark}$ respectively. At $\mathsf{mark}$, if the top
of $S$ is a table marker it moves that marker onto $B$ and goes to $\mathsf{back}$; if $S$ is
empty or has another symbol on top it goes to $\mathsf{done}$. At $\mathsf{done}$ it halts.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.prog`, a definition declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-03/index.html#prog-2).

## Start label of the lookup machine

The lookup program starts at its initialization label
$\mathsf{init}$.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.start`, a definition declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#start).

## Stack contents of the lookup machine

For lists of symbols $t$, $b$, $s$, $a$, $c$, $v$,
the assignment of contents to the six stacks of the lookup machine that gives $T$ the list $t$,
$B$ the list $b$, $S$ the list $s$, $A$ the list $a$, $C$ the list $c$ and $V$ the list $v$.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.stk`, a definition declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#stk).

## A name bit reads as itself

For every bit $b$, the name-bit symbol for $b$ reads as the
bit $b$.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.bit?_bit`, a theorem declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#bit-bit).

## Initialization step of the lookup machine

Let $t$ and $b$ be lists of symbols and $v$ a
bit. In exactly one step, the lookup program goes from the label $\mathsf{init}$ with internal bit
$v$, stack $T$ holding $t$, stack $B$ holding $b$ and the stacks $S$, $A$, $C$, $V$ empty, to the
label $\mathsf{scan}$ with internal bit $v$, the same contents of $T$, $B$, $S$, $A$ and $C$, and
stack $V$ holding the single symbol name bit false.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.init_run`, a theorem declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#init-run).

## Restoring and stashing after a comparison in the lookup machine

Let $q$, $n$, $c$ be
lists of bits such that $c$ is a prefix of both the reverse of $q$ and the reverse of $n$; let
$R$, $r$, $s$, $w$ be lists of symbols with $r$ empty or starting with a symbol other than a name
bit; and for a list of bits $x$ write $\bar x$ for the list of its bits as name bits. Suppose the
lookup program is at label $\mathsf{rstT}$, with any internal bit, and its stacks are: $T$ holds
the reverse of $\bar q$ with its first $|c|$ symbols removed, followed by $R$; $B$ holds the
reverse of $\bar n$ with its first $|c|$ symbols removed, followed by $r$; $S$ holds $s$; $A$ and
$C$ both hold the reverse of $\bar c$; and $V$ holds $w$. Then after exactly
$2(|c| + 1) + (|n| + 1)$ steps the program is at label $\mathsf{scan}$, with some internal bit,
where $T$ holds the reverse of $\bar q$ followed by $R$, $B$ holds $r$, $S$ holds $\bar n$
followed by $s$, $A$ and $C$ are empty, and $V$ holds $w$.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.tail_run`, a theorem declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#tail-run).

## Serving a live table entry

Write stack contents top first, and for a list of bits $u$ let
$\overrightarrow{u}$ be its bit symbols in order and $\overleftarrow{u}$ the same symbols in
reverse order. Let $q$ and $n$ be lists of bits, $b$ and $x$ bits, $s$ a list of symbols, and $R$,
$r$ lists of symbols each empty or topped by a symbol that is not a bit. From label
$\mathsf{cmp}(b)$ with any internal state, $\overleftarrow{q}R$ on $T$, $\overleftarrow{n}r$ on
$B$, $s$ on $S$, the stacks $A$ and $C$ empty and the bit symbol of $x$ alone on $V$, the lookup
program reaches, in at most $4|n| + 5$ steps, label $\mathsf{scan}$ with some internal state,
$\overleftarrow{q}R$ on $T$, $r$ on $B$, $\overrightarrow{n}s$ on $S$, the stacks $A$ and $C$
empty and on $V$ alone the bit symbol of $b$ if $n = q$ and of $x$ otherwise.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.cmp_run`, a theorem declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#cmp-run).

## One scan step of the lookup

Write stack contents top first; for a list of bits $u$ let
$\overleftarrow{u}$ be its bit symbols in reverse order; for a list $E$ of table entries let
$\tau(E)$ be the symbols of its entries in reading order (each entry's name bits, then its marker)
and $\mathrm{val}_E(q)$ the value of the first live entry of $E$ named $q$, or false if there is
none. Let $q$ be a list of bits, $e = (n, m)$ a table entry, $E$ a list of entries, $eE$ the list
$E$ with $e$ prepended, and $R$, $r$ lists of symbols each empty or topped by a symbol that is not
a bit. From label $\mathsf{scan}$ with any internal state, $\overleftarrow{q}R$ on $T$, the marker
of $e$ above $\overleftarrow{n}r$ on $B$, $\tau(E)$ on $S$, the stacks $A$ and $C$ empty and the
bit symbol of $\mathrm{val}_E(q)$ alone on $V$, the lookup program reaches, in at most
$4|n| + 6$ steps, label $\mathsf{scan}$ with some internal state, $\overleftarrow{q}R$ on $T$, $r$
on $B$, $\tau(eE)$ on $S$, the stacks $A$ and $C$ empty and the bit symbol of
$\mathrm{val}_{eE}(q)$ alone on $V$.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.entry_run`, a theorem declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#entry-run).

## The scan loop of the lookup machine

Let $q$ be a list of bits, let $R$ be a list of
symbols that is empty or starts with a symbol other than a name bit, and let $pre$ and $post$ be
lists of table entries; the live value of $q$ in an entry list is the value of its first entry
named $q$ that has a value, or false if there is none. Suppose the lookup program is at label
$\mathsf{scan}$, with any internal bit, and its stacks are: $T$ holds the bits of $q$ as name
bits, last bit on top, above $R$; $B$ holds the table stack of $pre$, of length $\ell$; $S$ holds
the symbols of the entries of $post$ in reading order, first entry on top; $A$ and $C$ are empty;
and $V$ holds the single name bit carrying the live value of $q$ in $post$. Then within
$6\ell + 1$ steps the program reaches label $\mathsf{back}$, with some internal bit, where $B$ is
empty, $S$ holds the symbols of the entries of $pre$ followed by $post$ in reading order, first
entry on top, $V$ holds the single name bit carrying the live value of $q$ in $pre$ followed by
$post$, and $T$, $A$ and $C$ are unchanged.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.scan_loop`, a theorem declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#scan-loop).

## The return loop of the lookup machine

Let $t$ and $w$ be lists of symbols, let $pre$ and
$post$ be lists of table entries, and let $m$ be the total number of symbols of the entries of
$post$. Suppose the lookup program is at label $\mathsf{back}$, with any internal bit, and its
stacks are: $T$ holds $t$; $B$ holds the table stack of $pre$; $S$ holds the symbols of the
entries of $post$ in reading order, first entry on top; $A$ and $C$ are empty; and $V$ holds $w$.
Then within $2m + 2$ steps the program reaches label $\mathsf{done}$, with some internal bit,
where $B$ holds the table stack of the entry list $pre$ followed by $post$, the stacks $S$, $A$
and $C$ are empty, and $T$ and $V$ still hold $t$ and $w$.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.back_loop`, a theorem declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#back-loop).

## Correctness of the SAT-verifier lookup machine

Let $q$ be a list of bits, $es$ a list of
table entries and $R$ a list of symbols that is empty or starts with a symbol other than a name
bit. Suppose the stacks of the lookup machine are as follows: $T$ holds the bits of $q$ as name
bits, last bit on top, above $R$; $B$ holds the table stack of $es$, of length $\ell$; and $S$,
$A$, $C$ and $V$ are empty. Then the lookup program, started at its start label with any
internal bit, reaches the label $\mathsf{done}$ within $8\ell + 4$ steps, with some internal bit;
there $V$ holds the single name bit carrying the live value of $q$ in $es$ (the value of the
first entry of $es$ named $q$ that has a value, or false if there is none), and every other
stack is as it started.

Formalized by `Cslib.Complexity.SatVerifier.Lookup.run`, a theorem declared in [CSLibExt/Computability/Complexity/SatLookup.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatLookup.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#run).

## Stacks of the SAT tokenizer

The SAT tokenizer has six stacks: $X$ for the formula bits,
$W$ for the witness bits, $T$ for the token output, $B$ for the table output, and the clause
counter $\mathsf{CC}$ and the literal counter $\mathsf{LC}$.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.K`, an inductive type declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#k).

## Labels of the SAT tokenizer

The labels of the SAT tokenizer are: $\mathsf{un}(c)$ for a
bit $c$, which reads a unary count onto the clause counter $\mathsf{CC}$ if $c$ is true and onto
the literal counter $\mathsf{LC}$ otherwise; $\mathsf{cls}$, which starts a clause;
$\mathsf{lits}$, which starts a literal; $\mathsf{nm}(\ell)$, where $\ell$ is a bit or none,
which reads the bit pairs of a name block, $\ell$ being the last name bit read (none before the
first one); $\mathsf{pol}$, which reads the polarity and the next witness bit; $\mathsf{fin}$,
which checks that the formula stack $X$ is used up; and the halting labels $\mathsf{acc}$ and
$\mathsf{rej}$.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#lab).

## Testing whether the top symbol is a given bit

For a bit $b$ and the result of peeking at
a stack (a symbol, or nothing when the stack is empty), this is true exactly when the peeked
symbol is the bit symbol carrying $b$; it is false for an empty stack and for every other
symbol.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.topIsBit`, a definition declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#top-is-bit).

## Instruction for reading a unary count

For a stack $k$ of the tokenizer and labels $s$ and
$t$, this is the tokenizer instruction that looks at the top of the formula stack $X$. If it is
the bit true, the instruction pops it, pushes the clause-end symbol $\mathsf{cl}$ onto $k$ and
goes to $s$; if it is the bit false, it pops it and goes to $t$; otherwise, when $X$ is empty or
its top is not a bit, it goes to $\mathsf{rej}$. The internal bit is set to true in the first two
cases and to false in the last.

When $k$ is not $X$ and the instruction is placed at label $s$, a run on a formula stack that
starts with $m$ bits true followed by a bit false pops these $m + 1$ bits, pushes $m$ copies
of $\mathsf{cl}$ onto $k$ and goes to $t$.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.unary`, a definition declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#unary).

## The tokenizer program

The tokenizer is a multi-stack machine with stacks $X$ (formula
bits), $W$ (witness bits), $T$ (tokens), $B$ (table) and the unary counters $CC$, $LC$ (over the
unit symbol $\mathsf{cl}$), and one bit of internal state. Its instruction at each label is:

- $\mathsf{un}(\mathrm{true})$, $\mathsf{un}(\mathrm{false})$: read a unary count from $X$ onto
  $CC$ and $LC$ respectively. If the top of $X$ is the bit true, pop it, push $\mathsf{cl}$ onto
  the counter and stay; if it is the bit false, pop it and go to $\mathsf{cls}$ (from
  $\mathsf{un}(\mathrm{true})$) or $\mathsf{lits}$ (from $\mathsf{un}(\mathrm{false})$); otherwise
  go to $\mathsf{rej}$.
- $\mathsf{cls}$: pop $CC$; if it was non-empty go to $\mathsf{un}(\mathrm{false})$, else go to
  $\mathsf{fin}$.
- $\mathsf{lits}$: pop $LC$; if it was non-empty go to $\mathsf{nm}(\mathrm{none})$, else push
  $\mathsf{cl}$ onto $T$ and go to $\mathsf{cls}$.
- $\mathsf{nm}(\ell)$, where $\ell$ is an optional bit: if the top of $X$ is the bit true, pop it;
  then if the top of $X$ is a bit $s$, pop it, push the name bit $s$ onto $T$ and onto $B$ and go to
  $\mathsf{nm}(s)$, and otherwise go to $\mathsf{rej}$. If instead the top of $X$ is the bit false,
  pop it and go to $\mathsf{rej}$ if $\ell$ is the bit false and to $\mathsf{pol}$ otherwise. In
  any other case go to $\mathsf{rej}$.
- $\mathsf{pol}$: if the top of $X$ is a bit $p$, pop it and push $\mathsf{lit}(p)$ onto $T$; then
  if $W$ is non-empty, pop its top symbol, read as a bit $s$ (false if it is not a bit), and push
  $\mathsf{val}(s)$ onto $B$, and otherwise push $\mathsf{dead}$ onto $B$; go to $\mathsf{lits}$.
  If the top of $X$ is not a bit, go to $\mathsf{rej}$.
- $\mathsf{fin}$: go to $\mathsf{rej}$ if $X$ is non-empty and to $\mathsf{acc}$ if it is empty.
- $\mathsf{acc}$, $\mathsf{rej}$: halt.

Each test stores its outcome in the internal bit: whether the top of $X$ or $W$ has the stated
form, or, for the pop of $CC$ or $LC$, whether that counter was non-empty. Popping a name bit $s$
in $\mathsf{nm}(\ell)$, the polarity $p$ in $\mathsf{pol}$ or a witness symbol in $\mathsf{pol}$
stores the bit read ($s$, $p$ or the witness bit $s$); the remaining pops and all pushes leave the
internal bit unchanged. So after popping a bit of a unary count, or the closing bit false of a name
block, the internal bit is true.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.prog`, a definition declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#prog).

## Start label of the SAT tokenizer

The tokenizer starts at the label $\mathrm{un}(1)$,
which reads a unary count from the input stack $X$ onto the clause counter $CC$.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.start`, a definition declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#start-2).

## Tokenizer stack contents

For symbol lists $x, w, t, b$ and natural numbers $c, \ell$, this
assigns to the tokenizer's stacks $X$, $W$, $T$, $B$ the lists $x$, $w$, $t$, $b$, and to the
counter stacks $CC$ and $LC$ the lists of $c$ and $\ell$ copies of the clause-end symbol
$\mathrm{cl}$ (the counters in unary).

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.st`, a definition declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#st).

## Rejection of the SAT tokenizer within a step bound

For a natural number $n$ and a
configuration $c$ of the tokenizer, the tokenizer rejects from $c$ within $n$ steps when there are
an internal bit $v$ and stacks $S$ such that it runs in at most $n$ steps from $c$ to the
configuration with label $\mathsf{rej}$, internal bit $v$ and stacks $S$.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.Rej`, a definition declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#rej).

## One step to rejection

Let $\ell$ be a label, $v$ a bit and $S$ an assignment of symbol
stacks to the tokenizer's stacks. If executing the tokenizer's instruction at $\ell$ from internal
bit $v$ and stacks $S$ yields a configuration with label $\mathsf{rej}$, then the tokenizer
reaches $\mathsf{rej}$ within one step from the configuration with label $\ell$, internal bit $v$
and stacks $S$.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.rej_one`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#rej-one).

## Reading a unary count

Let $c$ be a bit, $n$ a natural number, $r$ a bit string, $w, t, b$
symbol lists and $m, \ell$ counter values. Started at the label $\mathrm{un}(c)$ with any value
of its Boolean variable, with $X$ holding the bits of $1^n 0 r$, with $W$, $T$, $B$ holding $w$,
$t$, $b$, and with the counters $CC$ and $LC$ holding $m$ and $\ell$ in unary, the tokenizer
takes exactly $n + 1$ steps to reach the configuration whose label is $\mathrm{cls}$ if $c = 1$
and $\mathrm{lits}$ if $c = 0$, whose Boolean variable is $1$, whose stack $X$ holds the bits of
$r$, whose stacks $W$, $T$, $B$ still hold $w$, $t$, $b$, and whose counters hold $m + n$ and
$\ell$ if $c = 1$, and $m$ and $\ell + n$ if $c = 0$.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.un_run`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-04/index.html#un-run).

## An unterminated unary count is rejected

Let $r$ be a bit string on which reading a unary
length prefix fails. For every bit $c$, symbol lists $w, t, b$, counter values $m, \ell$ and
value of the Boolean variable, the tokenizer started at the label $\mathrm{un}(c)$ with $X$
holding the bits of $r$, with $W$, $T$, $B$ holding $w$, $t$, $b$, and with the counters $CC$
and $LC$ holding $m$ and $\ell$ in unary reaches the rejecting label within $|r| + 1$ steps.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.un_fail`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#un-fail).

## Name-loop outcome

For an optional bit $\ell$ and a bit string $u$, the name-loop outcome
is the tokenizer label defined by recursion on $u$: for empty $u$ it is $\mathsf{rej}$ if $\ell$ is
the bit false and $\mathsf{pol}$ otherwise, and for $u = c\,u'$ it is the outcome for the bit $c$
and the string $u'$. So it is $\mathsf{rej}$ exactly when the string formed by $\ell$ (if present)
followed by $u$ is non-empty and ends in false, and $\mathsf{pol}$ otherwise.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.nmEnd`, a definition declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#nm-end).

## Name-loop outcome from the start of a name

For every bit string $u$, the name-loop
outcome with no previous bit after $u$ is the label $\mathsf{pol}$ if $u$ is a canonical name,
that is, encoding the natural number that $u$ decodes to gives back $u$, and the label
$\mathsf{rej}$ otherwise.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.nmEnd_none`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#nm-end-none).

## Reading a name block

Let $u$ and $r$ be bit strings, $\ell$ an optional bit, $v$ a bit,
$w$, $t$, $b$ symbol stacks and $c$, $l$ natural numbers. Started at label $\mathsf{nm}(\ell)$ with
internal bit $v$, the bits of the self-delimiting block of $u$ followed by $r$ on the formula stack
$X$, $w$ on the witness stack $W$, $t$ on the token stack $T$, $b$ on the table stack $B$, clause
counter $c$ and literal counter $l$, the tokenizer runs in exactly $|u| + 1$ steps to the
configuration whose label is the name-loop outcome for $\ell$ and $u$, with internal bit true, the
bits of $r$ on $X$, $w$ on $W$, the bits of $u$ in reverse order (last bit on top) above $t$ on $T$
and above $b$ on $B$, and the same counters.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.nm_run`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#nm-run).

## Rejecting an unterminated name block

Let $r$ be a bit string from whose front no
self-delimiting block can be parsed. For every optional last bit $\ell$, internal bit $v$, symbol
stacks $w$, $t$, $b$ and natural numbers $c$, $l$, the tokenizer started at label
$\mathsf{nm}(\ell)$ with internal bit $v$, the bits of $r$ on the formula stack $X$, $w$ on the
witness stack $W$, $t$ on the token stack $T$, $b$ on the table stack $B$, clause counter $c$ and
literal counter $l$ reaches the label $\mathsf{rej}$ within $|r| + 1$ steps.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.nm_fail`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#nm-fail).

## Reading a polarity

Let $p$, $v$ be bits, $r$, $w$ bit strings, $t$, $b$ symbol stacks and
$c$, $l$ natural numbers. Started at label $\mathsf{pol}$ with internal bit $v$, the bit $p$
followed by the bits of $r$ on the formula stack $X$, the bits of $w$ on the witness stack $W$, $t$
on the token stack $T$, $b$ on the table stack $B$, clause counter $c$ and literal counter $l$, the
tokenizer moves in exactly one step to label $\mathsf{lits}$ with the bits of $r$ on $X$, the bits
of $w$ after its first on $W$, the polarity marker $\mathsf{lit}(p)$ pushed onto $t$, and the same
counters. If $w$ starts with the bit $w_1$, the internal bit becomes $w_1$ and the marker
$\mathsf{val}(w_1)$ is pushed onto $b$; if $w$ is empty, the internal bit becomes false and the
marker $\mathsf{dead}$ is pushed onto $b$.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.pol_run`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#pol-run).

## Tokenizer run on one literal

A configuration $\langle \ell, v \mid x, w, t, b, i, j\rangle$
of the SAT tokenizer has label $\ell$, internal bit $v$, stacks $X$, $W$, $T$, $B$ holding $x$,
$w$, $t$, $b$ (top first; a bit string stands for its list of bit symbols), and $i$ and $j$ marks
on the clause and literal counters; $\mathbin{+\!\!+}$ is concatenation. Let
$n, i, j \in \mathbb{N}$, let $p$ and $v$ be bits, $r$ and $w$ bit strings and $t$ and $b$ symbol
lists. Let $q$ be the binary code of $n$ (Mathlib's canonical bits of $n$, least significant first,
empty for $0$), $E$ the encoding of the literal $(n, p)$, $o$ the first bit of $w$ (none if $w$ is
empty), $o'$ that bit with default false, and $w'$ the string $w$ with its first bit, if any,
removed. Then the tokenizer goes in exactly $|q| + 2$ steps from
$\langle \mathsf{nm}(\mathrm{none}), v \mid E \mathbin{+\!\!+} r, w, t, b, i, j\rangle$ to
$\langle \mathsf{lits}, o' \mid r, w', \mathrm{rev}(\lambda) \mathbin{+\!\!+} t,
\mathrm{rev}(\eta) \mathbin{+\!\!+} b, i, j\rangle$, where $\lambda$ is the token list of the
literal $(n, p)$ (the bits of $q$, then the polarity marker of $p$) and $\eta$ is the symbol list
of the table entry $(q, o)$ (the bits of $q$, then the value marker of $o$, which is dead if $o$
is none).

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.lit_run`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#lit-run).

## Tokenizer rejects an undecodable literal

A configuration
$\langle \ell, v \mid x, w, t, b, i, j\rangle$ of the SAT tokenizer has label $\ell$, internal bit
$v$, stacks $X$, $W$, $T$, $B$ holding $x$, $w$, $t$, $b$ (top first; a bit string stands for its
list of bit symbols), and $i$ and $j$ marks on the clause and literal counters. Let $r$ be a bit
string from whose front no literal can be decoded (a literal being a self-delimited canonical
variable code followed by a polarity bit), let $w$, $t$, $b$ be symbol lists,
$i, j \in \mathbb{N}$ and $v$ a bit. Then from
$\langle \mathsf{nm}(\mathrm{none}), v \mid r, w, t, b, i, j\rangle$ the tokenizer reaches the
label $\mathsf{rej}$ within $|r| + 2$ steps.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.lit_fail`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#lit-fail).

## Occurrence table of a nonempty list

Let $n$ be a natural number, $L$ a list of natural
numbers and $w$ a list of bits. The occurrence table of the list $n$ followed by $L$, with $w$, is
the entry whose name is the binary code of $n$ and whose value is the first bit of $w$ (no value
if $w$ is empty), followed by the occurrence table of $L$ with $w$ minus its first bit (with the
empty list if $w$ is empty).

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.entsOf_cons`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#ents-of-cons).

## Reading the literals of a clause

Let $C$ be a clause with literals
$(n_1, p_1), \dots, (n_k, p_k)$, let $u$ be the concatenation of their literal codes, and let $r$,
$w$ be bit strings, $t$, $b$ stacks of symbols, $c$ a natural number and $v$ a bit. Started at
label $\mathsf{lits}$ with internal bit $v$, the bits of $u$ followed by $r$ on the formula stack
$X$, the bits of $w$ on the witness stack $W$, $t$ on the token stack $T$, $b$ on the table stack
$B$, clause counter $c$ and literal counter $k$, the tokenizer reaches within $2|u| + 1$ steps the
configuration with label $\mathsf{cls}$, internal bit false, the bits of $r$ on $X$, the bits of
$w$ with its first $k$ bits removed on $W$, the tokens of $C$ in reverse order (its final
$\mathsf{cl}$ on top) above $t$ on $T$, the table stack of the entries $e_1, \dots, e_k$ above $b$
on $B$, clause counter $c$ and literal counter $0$. Here $e_i$ pairs the binary name of $n_i$ with
the $i$-th bit of $w$, or with no value when $w$ has fewer than $i$ bits.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.lits_run`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#lits-run).

## Tokenizer rejects undecodable literals

A configuration
$\langle \ell, v \mid x, w, t, b, i, j\rangle$ of the SAT tokenizer has label $\ell$, internal bit
$v$, stacks $X$, $W$, $T$, $B$ holding $x$, $w$, $t$, $b$ (top first; a bit string stands for its
list of bit symbols), and $i$ and $j$ marks on the clause and literal counters. Let
$c, k \in \mathbb{N}$, let $r$ and $w$ be bit strings, $t$ and $b$ symbol lists and $v$ a bit, and
suppose that decoding $k$ literals from the front of $r$ fails. Then from
$\langle \mathsf{lits}, v \mid r, w, t, b, c, k\rangle$ the tokenizer reaches the label
$\mathsf{rej}$ within $2|r| + 3$ steps.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.lits_fail`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#lits-fail).

## Tokenizer run on one clause

A configuration $\langle \ell, v \mid x, w, t, b, i, j\rangle$
of the SAT tokenizer has label $\ell$, internal bit $v$, stacks $X$, $W$, $T$, $B$ holding $x$,
$w$, $t$, $b$ (top first; a bit string stands for its list of bit symbols), and $i$ and $j$ marks
on the clause and literal counters; $\mathbin{+\!\!+}$ is concatenation. Let $C$ be a clause,
$r$ and $w$ bit strings, $t$ and $b$ symbol lists, $c \in \mathbb{N}$ and $v$ a bit. Let $E$ be
the encoding of $C$, $N$ the list of variable indices of the literals of $C$ in order, and $w'$
the string $w$ with its first $|C|$ bits removed (all of them if $w$ is shorter). Then the
tokenizer goes in at most $2|E| + 1$ steps from
$\langle \mathsf{cls}, v \mid E \mathbin{+\!\!+} r, w, t, b, c + 1, 0\rangle$ to
$\langle \mathsf{cls}, \mathsf{false} \mid r, w', \mathrm{rev}(\tau) \mathbin{+\!\!+} t,
\beta \mathbin{+\!\!+} b, c, 0\rangle$, where $\tau$ is the token list of $C$ and $\beta$ is the
table stack of the occurrence table of $N$ against $w$.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.clause_run`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#clause-run).

## Tokenizer run on all clauses

A configuration $\langle \ell, v \mid x, w, t, b, i, j\rangle$
of the SAT tokenizer has label $\ell$, internal bit $v$, stacks $X$, $W$, $T$, $B$ holding $x$,
$w$, $t$, $b$ (top first; a bit string stands for its list of bit symbols), and $i$ and $j$ marks
on the clause and literal counters; $\mathbin{+\!\!+}$ is concatenation. Let $r$ and $w$ be bit
strings, $\varphi$ a CNF formula with $m$ clauses, $t$ and $b$ symbol lists and $v$ a bit. Let
$E$ be the concatenation of the encodings of the clauses of $\varphi$, $N$ the list of variable
indices of all literal occurrences of $\varphi$ in order, and $w'$ the string $w$ with its first
$|N|$ bits removed (all of them if $w$ is shorter). Then the tokenizer goes in at most
$2|E| + m + 1$ steps from $\langle \mathsf{cls}, v \mid E \mathbin{+\!\!+} r, w, t, b, m, 0\rangle$
to $\langle \mathsf{fin}, \mathsf{false} \mid r, w', \mathrm{rev}(\tau) \mathbin{+\!\!+} t,
\beta \mathbin{+\!\!+} b, 0, 0\rangle$, where $\tau$ is the token list of $\varphi$ and $\beta$ is
the table stack of the occurrence table of $N$ against $w$.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.clauses_run`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#clauses-run).

## Tokenizer rejects undecodable clauses

A configuration
$\langle \ell, v \mid x, w, t, b, i, j\rangle$ of the SAT tokenizer has label $\ell$, internal bit
$v$, stacks $X$, $W$, $T$, $B$ holding $x$, $w$, $t$, $b$ (top first; a bit string stands for its
list of bit symbols), and $i$ and $j$ marks on the clause and literal counters. Let
$n \in \mathbb{N}$, let $r$ and $w$ be bit strings, $t$ and $b$ symbol lists and $v$ a bit, and
suppose that decoding $n$ clauses (each a unary literal count followed by that many encoded
literals) from the front of $r$ fails. Then from
$\langle \mathsf{cls}, v \mid r, w, t, b, n, 0\rangle$ the tokenizer reaches the label
$\mathsf{rej}$ within $2|r| + n + 2$ steps.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.clauses_fail`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#clauses-fail).

## The tokenizer accepts when the formula stack is empty

Let $w$, $t$, $b$ be lists of
symbols, $i, j \in \mathbb{N}$ and $v$ a bit. In exactly one step, the SAT tokenizer goes from the
label $\mathsf{fin}$ with internal bit $v$, empty formula stack $X$, stacks $W$, $T$, $B$ holding
$w$, $t$, $b$, and $i$ and $j$ marks on the clause and literal counters, to the label
$\mathsf{acc}$ with internal bit false and all stacks unchanged.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.fin_acc`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#fin-acc).

## Accepting run of the SAT tokenizer

Let $x$ and $w$ be bit strings such that $x$ decodes
to the CNF formula $\varphi$, and let $S$ be contents of the tokenizer's stacks in which $X$
holds the bits of $x$, $W$ holds the bits of $w$, and the counters $CC$ and $LC$ are empty.
Started at the start label with stacks $S$ and any value of its Boolean variable, the tokenizer
reaches the accepting label within $2|x| + 2$ steps, with final stacks $S'$ such that $X$, $CC$
and $LC$ are empty, $W$ holds the bits of $w$ without their first $m$ entries, where $m$ is the
number of literal occurrences in $\varphi$, $T$ holds the reversed token list of $\varphi$ on top
of the original contents of $T$, and $B$ holds the table stack of the occurrence table of
$\varphi$ and $w$ on top of the original contents of $B$.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.run_some`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#run-some).

## Rejecting run

Let $x$ and $w$ be bit strings such that $x$ does not decode as a CNF
formula. For every bit $v$ and stacks $S$ with the bits of $x$ on the formula stack $X$, the bits
of $w$ on the witness stack $W$, and both counter stacks $CC$ and $LC$ empty, the tokenizer
started at its start label with internal bit $v$ and stacks $S$ reaches a configuration with label
$\mathsf{rej}$ within $2|x| + 2$ steps.

Formalized by `Cslib.Complexity.SatVerifier.Tokenizer.run_none`, a theorem declared in [CSLibExt/Computability/Complexity/SatTokenizer.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatTokenizer.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#run-none).

## Input alphabet of the SAT verifier host

The alphabet $G$ of the host's input stack is the
pair alphabet $\mathrm{Bool} \oplus \mathrm{Option}\ \mathrm{Bool}$ of the dense SAT verifier.

In the encoding of a pair $(x, w)$, a formula bit $b$ is $\mathrm{inl}\ b$, the separator $\#$ is
$\mathrm{inr}\ \mathrm{none}$ and a certificate bit $b$ is $\mathrm{inr}\ (\mathrm{some}\ b)$.

Formalized by `Cslib.Complexity.SatVerifier.Machine.G`, an abbreviation declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#g).

## Stacks of the SAT verifier host

The SAT verifier host has seventeen stacks: the input
stack, the output stack, and fifteen work stacks, namely two holding the formula bits and the
certificate bits, two scratch stacks used to move them in phase 0, the token and table stacks,
six further stacks of the clause-check driver, two further stacks of the tokenizer, and one
further stack of the 3-clause filter.

Formalized by `Cslib.Complexity.SatVerifier.Machine.HK`, an inductive type declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#hk).

## Stack alphabets of the SAT verifier host

Each stack of the SAT verifier host has an
alphabet: the input stack has the input alphabet $G$, the output stack has alphabet
$\mathrm{Bool}$, and every other stack has the token alphabet $\mathrm{Sym}$.

Formalized by `Cslib.Complexity.SatVerifier.Machine.HΓ`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-05/index.html#h).

## Phase-0 labels of the SAT verifier host

The five labels of phase 0 of the SAT verifier
host: $m_1$ and $m_2$ move the formula bits $x$ off the input (in two passes), $\mathsf{sep}$
drops the separator, and $m_3$ and $m_4$ move the witness bits $w$ (in two passes).

Formalized by `Cslib.Complexity.SatVerifier.Machine.P0`, an inductive type declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#p0).

## Labels of the SAT verifier host

A label of the SAT verifier host is one of the
following: a phase-0 label; a label of the tokenizer; a label of the 3-clause filter; a label of
the clause-check driver or of the lookup embedded in it; a cleanup label carrying an answer bit;
or an output label carrying an answer bit.

Formalized by `Cslib.Complexity.SatVerifier.Machine.HLab`, an inductive type declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#hlab).

## Host labels as a sum type

Write $P_0$ for the phase-0 labels, $\Lambda_T$ for the
tokenizer labels, $\Lambda_F$ for the labels of the clause-length filter, and $\Lambda_D$ and
$\Lambda_L$ for the labels of the clause-check driver and of the lookup. The host labels are in
bijection with $P_0 \sqcup \Lambda_T \sqcup \Lambda_F \sqcup (\Lambda_D \sqcup \Lambda_L) \sqcup
\mathrm{Bool} \sqcup \mathrm{Bool}$: a phase-0 label $p$, tokenizer label, filter label, or driver
or lookup label goes to itself in its summand, a cleanup label with answer $a$ goes to $a$ in the
first copy of $\mathrm{Bool}$, and a final label with answer $a$ goes to $a$ in the second copy.
The bijection gives the host labels their finiteness instance.

Formalized by `Cslib.Complexity.SatVerifier.Machine.HLab.equiv`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#equiv).

## Placement of the tokenizer's stacks in the host

The stacks of the tokenizer (the formula
bits $X$, the witness bits $W$, the token output $T$, the table output $B$, and the clause and
literal counters $CC$ and $LC$) are placed in the host machine by the map that sends each of them
to the host stack of the same name.

Formalized by `Cslib.Complexity.SatVerifier.Machine.eT`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#e-t).

## Stack embedding of the tokenizer into the host

Every stack of the tokenizer has alphabet
$\mathrm{Sym}$. The tokenizer is embedded in the host machine by sending each of its stacks $X$,
$W$, $T$, $B$, $CC$, $LC$ to the host stack of the same name (an injective map) and identifying
the alphabet of each with that of its image, which is again $\mathrm{Sym}$, by the identity.

Formalized by `Cslib.Complexity.SatVerifier.Machine.embT`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#emb-t).

## Placement of the lookup's stacks in the clause-check driver

The stacks of the lookup
(the query $T$, the table $B$, the stash $S$, the scratch stacks $A$ and $C$, and the value $V$)
are placed in the clause-check driver by the map that sends each of them to the driver stack of
the same name.

Formalized by `Cslib.Complexity.SatVerifier.Machine.eL`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#e-l).

## Stack embedding of the lookup into the clause-check driver

Every stack of the lookup and
of the clause-check driver has alphabet $\mathrm{Sym}$. The lookup is embedded in the driver by
sending each of its stacks $T$, $B$, $S$, $A$, $C$, $V$ to the driver stack of the same name (an
injective map) and identifying the alphabets by the identity of $\mathrm{Sym}$.

Formalized by `Cslib.Complexity.SatVerifier.Machine.embL`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#emb-l).

## Lookup labels in the clause-check driver

The relabelling that places the lookup's labels
among the driver's labels, whose label set consists of the driver's own labels together with the
lookup's labels: the lookup's final label $\mathsf{done}$ goes to the driver's return label
$\mathsf{ret}$, and every other lookup label $l$ goes to the copy of $l$ among the lookup's
labels.

Formalized by `Cslib.Complexity.SatVerifier.Machine.φL`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#l).

## The embedded lookup program

The lookup sub-program of the clause-check driver: at each
lookup label $l$, it is the lookup program's statement at $l$ with every stack operation moved to
the driver's stack of the same name (the lookup's stacks $T$, $B$, $S$, $A$, $C$, $V$) and every
jump target relabelled by the lookup-label map, which sends $\mathsf{done}$ to the driver's
return label $\mathsf{ret}$ and keeps every other label.

Formalized by `Cslib.Complexity.SatVerifier.Machine.lkH`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#lk-h).

## Driver stacks in the SAT host

The map from the stacks of the clause-check driver into
the host stacks sends each driver stack to the host stack of the same name.

Formalized by `Cslib.Complexity.SatVerifier.Machine.eC`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#e-c).

## Stack embedding of the clause-check driver into the host

Every stack of the clause-check
driver has alphabet $\mathrm{Sym}$. The driver is embedded in the host machine by sending each of
its stacks $T$, $B$, $S$, $A$, $C$, $V$, $P$, $F$ to the host stack of the same name (an injective
map) and identifying the alphabet of each with that of its image, which is again $\mathrm{Sym}$,
by the identity.

Formalized by `Cslib.Complexity.SatVerifier.Machine.embC`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#emb-c).

## Placement of the filter's stacks in the host

The two stacks of the clause-length filter,
the token stack $T$ and the side stack $U$, are placed in the host machine by the map that sends
$T$ to the host stack $T$ and $U$ to the host stack $U$.

Formalized by `Cslib.Complexity.SatVerifier.Machine.eF`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#e-f).

## Stack embedding of the clause-length filter into the host

Both stacks of the
clause-length filter have alphabet $\mathrm{Sym}$. The filter is embedded in the host machine by
sending its stacks $T$ and $U$ to the host stacks of the same names (an injective map) and
identifying the alphabet of each with that of its image, which is again $\mathrm{Sym}$, by the
identity.

Formalized by `Cslib.Complexity.SatVerifier.Machine.embF`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#emb-f).

## Filter exits in the SAT verifier host

The relabelling of the 3-clause filter's labels
into the labels of the SAT verifier host sends the filter's exit label *pass* to the start label
of the clause-check driver, its exit label *fail* to the cleanup label with answer false, and
every other filter label $l$ to the host's copy of $l$ among its filter labels.

Formalized by `Cslib.Complexity.SatVerifier.Machine.φF`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#f).

## Tokenizer labels in the host machine

The map from labels of the tokenizer to labels of
the host SAT verifier sends the tokenizer's accepting label to the start label of the embedded
clause-length filter, its rejecting label to the cleanup label with answer false, and every
other label $l$ to the host label that runs the tokenizer at $l$.

Formalized by `Cslib.Complexity.SatVerifier.Machine.φT`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#t).

## Driver labels in the SAT host

The map from the labels of the clause-check driver (its
own labels and those of the lookup embedded in it) to the host labels sends the driver's label
for the answer yes to the cleanup label with answer true, its label for the answer no to the
cleanup label with answer false, and every other label $l$ to the host label running the
driver at $l$.

Formalized by `Cslib.Complexity.SatVerifier.Machine.φC`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#c).

## Reading a formula bit in the SAT host

The input alphabet of the SAT host consists of
the formula bits, the separator and the witness bits. This partial map sends a formula bit $b$
to $b$ and is undefined on the separator and on witness bits.

Formalized by `Cslib.Complexity.SatVerifier.Machine.dX`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#d-x).

## Reading a witness bit in the SAT host

The input alphabet of the SAT host consists of
the formula bits, the separator and the witness bits. This partial map sends a witness bit $b$
to $b$ and is undefined on formula bits and on the separator.

Formalized by `Cslib.Complexity.SatVerifier.Machine.dW`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#d-w).

## Stacks emptied by the SAT verifier's cleanup

The cleanup loop of the host SAT verifier
empties the list of stacks made of the input stack followed by the work stacks $X$, $W$, $T$, $B$,
$S$, $A$, $C$, $V$, $P$, $F$, $CC$, $LC$, $X1$, $W1$, $U$, in that order: every host stack except
the output stack.

Formalized by `Cslib.Complexity.SatVerifier.Machine.workKs`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#work-ks).

## Program of the SAT verifier host

For a value $c$ of the 3SAT flag, the host program
acts at each host label as follows. Here moving a bit block from one stack to another means
repeatedly popping the top symbol of the first stack while it is a bit and pushing it, as a bit
token, onto the second, and continuing at the next label once the top is not a bit or the stack
is empty.

The phase-0 labels move the formula bits from the input stack onto a scratch stack, move them
from there onto the formula stack, pop one symbol (on a pair encoding, the separator) from the
input stack, move the certificate bits from the input stack onto a second scratch stack, and move
them from there onto the certificate stack before going to the start label of the tokenizer. At
a tokenizer label, a filter label or a driver label the host runs the program of the tokenizer,
of the 3-clause filter with flag $c$, or of the clause-check driver with its embedded lookup, on
that component's stacks embedded in the host, with the component's labels renamed to host
labels; the tokenizer's accept exit goes to the filter's start label, the filter's pass exit to
the driver's start label, the driver's yes exit to the cleanup label with answer true, and the
tokenizer's reject exit, the filter's fail exit and the driver's no exit to the cleanup label
with answer false. At the cleanup label with answer $b$ the host pops every stack other than the
output stack once, repeats this while anything was popped, and then goes to the output label
with answer $b$, where it pushes $b$ onto the output stack, sets its internal state to false and
halts.

Formalized by `Cslib.Complexity.SatVerifier.Machine.hprog`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-06/index.html#hprog).

## The SAT verifier machine

For a flag $\mathit{cap}$, the host machine is the finite
multi-stack Turing machine whose stacks are the host stacks, with the input stack as input (its
alphabet is that of the pair encoding: tagged formula bits, a separator and tagged witness
bits), the output stack (alphabet the booleans) as output, the host alphabets on all stacks, the
host labels as labels, the first phase-0 label as start label, a boolean internal state
initially false, and the host program with flag $\mathit{cap}$ as program.

Formalized by `Cslib.Complexity.SatVerifier.Machine.tm`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#tm).

## Phase 0 of the SAT verifier host

Let $c$ be a flag, $x$ and $w$ bit strings of lengths
$m$ and $n$, $v$ an internal state, and $S$ host stacks whose input stack holds the pair encoding
$x \# w$ and whose other stacks are all empty. Then there are an internal state $v'$ and host
stacks $S'$ such that the host program with flag $c$ runs in exactly $2m + 2n + 5$ steps from
the configuration at the phase-0 label $m_1$ with internal state $v$ and stacks $S$ to the
configuration at the start label of the tokenizer with internal state $v'$ and stacks $S'$, the
stack $X$ of $S'$ holds the bits of $x$ in order and the stack $W$ holds the bits of $w$ in
order, each as a name-bit symbol, and every other stack of $S'$ is empty.

Formalized by `Cslib.Complexity.SatVerifier.Machine.phase0_run`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#phase0-run).

## The tokenizer embeds in the SAT verifier host

For every flag $c$, the tokenizer program
embeds in the host program with flag $c$ along the stack embedding of the tokenizer into the host
and the map of tokenizer labels into host labels, which sends the tokenizer's accepting label to
the start label of the clause-length filter, its rejecting label to the cleanup label with answer
false, and every other label $\ell$ to the host label running the tokenizer at $\ell$. That is,
for every tokenizer label $\ell$, either the tokenizer's statement at $\ell$ is the halt
statement, or the host program's statement at the image of $\ell$ is the tokenizer's statement
at $\ell$ translated along this embedding and label map.

Formalized by `Cslib.Complexity.SatVerifier.Machine.embeds_tok`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#embeds-tok).

## The embedded lookup meets the lookup contract

The clause-check driver, with the embedded
lookup program as its lookup sub-program and the lookup's start label as the label it calls, meets
the driver's lookup contract with constants $a = 8$ and $b = 4$: from the lookup's start label,
with a reversed name block $q$ on the token stack $T$ above a rest that does not begin with a name
bit, the table stack of an entry list $es$ on $B$, and the stacks $S$, $A$, $C$, $V$ empty, it
reaches the driver's return label within $8m + 4$ steps, where $m$ is the length of the table
stack, with $V$ holding the single bit of the live value of $q$ in $es$ and every other stack
unchanged.

Formalized by `Cslib.Complexity.SatVerifier.Machine.lookupSpec`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#lookup-spec).

## The cleanup stacks are distinct

The list of stacks emptied by the cleanup of the SAT
verifier host has no repeated entries.

Formalized by `Cslib.Complexity.SatVerifier.Machine.workKs_nodup`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#work-ks-nodup).

## Cleanup of the SAT host

Let $m$ be a natural number and let $S$ assign contents to the
host stacks so that every stack has length at most $m$ and the output stack is empty. Then for
every flag $c$, answer bit $a$ and internal state $v$, the host program with flag $c$ goes in at
most $m + 1$ steps from the cleanup label with answer $a$, internal state $v$ and stacks $S$ to
the final label with answer $a$, internal state false and every stack empty.

Formalized by `Cslib.Complexity.SatVerifier.Machine.clean_host`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#clean-host).

## Name lengths in an occurrence table

For every list $n_0, \dots, n_{k-1}$ of natural
numbers and every list $w$ of bits, the names of the entries of the occurrence table of
$n_0, \dots, n_{k-1}$ and $w$, in order, have the lengths of the binary codes of
$n_0, \dots, n_{k-1}$ (Mathlib's encoding of natural numbers as bit lists).

Formalized by `Cslib.Complexity.SatVerifier.Machine.entsOf_map_length`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#ents-of-map-length).

## Initial stacks of the SAT verifier host

For a word $l$ over the input alphabet $G$, the
initial host stacks on $l$ hold $l$ on the input stack and leave every other stack empty.

Formalized by `Cslib.Complexity.SatVerifier.Machine.initS`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#init-s).

## Tokenizer stacks after phase 0

For bit lists $x$ and $w$, these tokenizer stack contents
put the bits of $x$ on the formula stack $X$ and the bits of $w$ on the witness stack $W$ (each
bit as a bit symbol), and leave every other tokenizer stack (token, table and the two counters)
empty.

Formalized by `Cslib.Complexity.SatVerifier.Machine.tokS`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#tok-s).

## Driver stacks after tokenization

For a CNF formula $\varphi$ and a witness $w$, these
are the contents of the clause-check driver's stacks once the tokenizer has accepted $\varphi$:
the token stack holds the token list of $\varphi$ reversed, the table stack holds the
table-stack encoding of the occurrence table of $\varphi$ and $w$, and every other stack is
empty.

Formalized by `Cslib.Complexity.SatVerifier.Machine.chkS`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#chk-s).

## Step budget before the cleanup

For an input length $N$, the number
$(2N + 5) + (2N + 2) + (2N + 2) + (N(8N + 9) + 1)$.

It budgets the host steps before the cleanup: its four summands budget phase 0, the tokenizer,
the clause-length filter and the clause-check driver.

Formalized by `Cslib.Complexity.SatVerifier.Machine.preSteps`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#pre-steps).

## Cleanup phase of the SAT verifier host

Fix either value of the 3SAT flag, an answer bit
$b$, a natural number $m$, an internal state $v$, and host stacks $S$ such that every stack of $S$
has length at most $m$ and the output stack of $S$ is empty. Then for some $n \le m + 2$, the host
program runs in exactly $n$ steps from the configuration at the cleanup label with answer $b$,
internal state $v$ and stacks $S$ to the halted configuration with internal state false, the
one-symbol word $b$ on the output stack and every other stack empty.

Formalized by `Cslib.Complexity.SatVerifier.Machine.finish`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#finish).

## Answer of the SAT host

For a flag $c$ and a pair $(x, w)$ of bit strings, the host's
answer is false if $x$ does not decode to a CNF formula. If $x$ decodes to a formula $\varphi$,
give each variable $n$ the value $w_i$ (counting from $0$), where $i$ is the first position of
$n$ in the list of variable occurrences of $\varphi$ read clause by clause, and the value false
if $i \ge |w|$. Then the answer is true exactly when both (a) $c$ is false or every clause of
$\varphi$ has at most three literals, and (b) every clause of $\varphi$ contains a literal
$(n, b)$ whose variable $n$ has value $b$.

Formalized by `Cslib.Complexity.SatVerifier.Machine.ans`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#ans).

## Explicit step bound of the SAT verifier machine

For a flag $\mathit{cap}$ and an input
length $N$, let $s(N) = (2N + 5) + (2N + 2) + (2N + 2) + (N(8N + 9) + 1)$ be the number of
steps allowed before the cleanup, and let $p$ be the per-step push budget of the host machine
with that flag. The total step bound is $s(N) + (N + p \cdot s(N)) + 2$.

When the cleanup starts, every stack has length at most $N + p \cdot s(N)$; the cleanup and the
output step then take at most that many steps plus $2$.

Formalized by `Cslib.Complexity.SatVerifier.Machine.totalSteps`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#total-steps).

## Initial configuration of the SAT verifier machine

For every flag $c$ and every word $l$
over the input alphabet $G$ of the host, the initial configuration of the SAT verifier machine
with flag $c$ on $l$ (its start label, its initial internal state, $l$ on the input stack and
every other stack empty) is the configuration at the phase-0 label $m_1$ with internal state
false and the initial host stacks on $l$.

Formalized by `Cslib.Complexity.SatVerifier.Machine.initList_tm`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 582](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L582). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#init-list-tm).

## Step bound of the SAT verifier machine

For a flag $\mathit{cap}$, let $p$ be the
per-step push budget of the host machine with that flag (the sum over its labels of the number
of push instructions in each label's statement). The step bound is the polynomial
$(p + 1)(8X^2 + 15X + 10) + X + 2$ with natural-number coefficients, in the input length $X$.

Formalized by `Cslib.Complexity.SatVerifier.Machine.time`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 596](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L596). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#time).

## The `TM2` SAT verifier

For a flag $\mathit{cap}$, the host machine with that flag computes
the host's answer in polynomial time. For every pair $(x, w)$ of bit lists, started on the input
$x \# w$ (the bits of $x$, a separator, then the bits of $w$), it halts with the single bit
$\mathrm{ans}_{\mathit{cap}}(x, w)$ on its output stack and every other stack empty within $T(n)$
steps, where $n$ is the length of $x \# w$ and $T$ is the host's polynomial step bound. Here
$\mathrm{ans}_{\mathit{cap}}(x, w)$ is false unless $x$ decodes to a CNF formula $\varphi$; in that
case it is true exactly when $\varphi$ passes the clause check against the table built from $w$
and, if $\mathit{cap}$ is true, every clause of $\varphi$ has at most three literals.

Formalized by `Cslib.Complexity.SatVerifier.Machine.verifier`, a definition declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 606](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L606). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#verifier).

## The SAT host's answer is polynomial-time

For each value of the flag $\mathit{cap}$
(with or without the three-literal clause filter), the host's answer, as a function from pairs
$(x, w)$ of bit strings to Booleans, is polynomial-time computable under the canonical bitstring
encodings.

Formalized by `Cslib.Complexity.SatVerifier.Machine.isPolyTime_ans`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 636](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L636). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#is-poly-time-ans).

## The SAT verifier is polynomial-time

The function that maps a pair $(x, w)$ of bit
strings to the Boolean answer of the SAT verifier on $(x, w)$ (its return value, ignoring its
declared time cost) is polynomial-time computable under the canonical bitstring encodings.

Formalized by `Cslib.Complexity.SatVerifier.Machine.isPolyTime_satVerifier`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#is-poly-time-sat-verifier).

## SAT is in NP

The decision problem SAT, which accepts exactly the bit strings that encode
a satisfiable CNF formula, belongs to the class NP.

Variable indices are binary-coded in the encoding of formulas.

Formalized by `Cslib.Complexity.SatVerifier.Machine.satDec_mem_NP`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-07/index.html#sat-dec-mem-np).

## Cook–Levin theorem

CNF satisfiability is NP-complete: the decision problem accepting
exactly the bit strings that encode a satisfiable CNF formula is in NP, and every decision
problem in NP has a polynomial-time many-one reduction to it.

Formalized by `Cslib.Complexity.SatVerifier.Machine.cook_levin_SAT_np_complete`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 654](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L654). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-08/index.html#cook-levin-sat-np-complete).

## Answer of the SAT host with the three-literal filter

For all bit strings $x$ and $w$,
the answer of the SAT host with flag true on $(x, w)$ is the conjunction of two bits. The first
is false if the complete length-prefixed CNF decoder fails on $x$; if $x$ decodes to a CNF
formula $\varphi$, it is true exactly when every clause of $\varphi$ has at most three literals.
The second is the return value of the SAT verifier on $(x, w)$.

Formalized by `Cslib.Complexity.SatVerifier.Machine.ans_true`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 663](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L663). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-08/index.html#ans-true).

## 3SAT is in NP

The decision problem 3SAT, which accepts exactly the bit strings that
encode a satisfiable CNF formula in which every clause has at most three literals, belongs to the
class NP.

The verifier is the SAT verifier host with the three-literal clause filter switched on, and
witnesses no longer than the input suffice.

Formalized by `Cslib.Complexity.SatVerifier.Machine.sat3Dec_mem_NP`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 669](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L669). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-08/index.html#sat3-dec-mem-np).

## Token length bound for the SAT verifier (moved alias)

Moved to `SatVerifier.toks_length_le` (`SatVerifierSpec`).

Formalized by `Cslib.Complexity.SatVerifier.Machine.toks_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 695](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L695). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-08/index.html#toks-length-le).

## Clause token length bound for the SAT verifier (moved alias)

Moved to `SatVerifier.clauseToks_length_le` (`SatVerifierSpec`).

Formalized by `Cslib.Complexity.SatVerifier.Machine.clauseToks_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 700](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L700). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-08/index.html#clause-toks-length-le).

## Finiteness of the SAT verifier alphabet (moved alias)

Moved to the instance `SatVerifier.Sym.instFintype` (`SatVerifierSpec`); kept as a
definition, not an instance, so instance search sees one `Fintype Sym`.

Formalized by `Cslib.Complexity.SatVerifier.Machine.Sym.instFintype`, an abbreviation declared in [CSLibExt/Computability/Complexity/SatVerifierTM.lean, line 707](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SatVerifierTM.lean#L707). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/part-08/index.html#inst-fintype).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polynomial-time verifier for SAT](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/polynomial-time-verifier-for-sat)
