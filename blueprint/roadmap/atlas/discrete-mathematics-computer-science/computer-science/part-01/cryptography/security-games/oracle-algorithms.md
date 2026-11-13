---
declaration: section
origin: cited
lean: Cslib.Crypto.Framework.OracleSig, Cslib.Crypto.Framework.OracleComp, Cslib.Crypto.Framework.OracleComp.done, Cslib.Crypto.Framework.OracleComp.query, Cslib.Crypto.Framework.OracleComp.run, Cslib.Crypto.Framework.OracleComp.queries, Cslib.Crypto.Framework.OracleComp.run_congr, Cslib.Crypto.Framework.OracleComp.run_bind
statement: formalized
proof: formalized
---

# Oracle algorithms

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/security-games/oracle-algorithms/index.html).

## Single-oracle computations

## The signature of one oracle

For types $X$ and $Y$, this is the polynomial functor whose
operations are the queries $x \in X$, each answered by an element of $Y$.

Formalized by `Cslib.Crypto.Framework.OracleSig`, an abbreviation declared in [CSLibExt/Crypto/Framework/Oracle.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Framework/Oracle.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/security-games/oracle-algorithms/index.html#oracle-sig).

## Adaptive oracle algorithms

For a type $X$ of queries, a type $Y$ of answers and a type
$\alpha$ of outputs, an adaptive deterministic oracle algorithm is an element of CSLib's free
monad over the polynomial functor of one oracle with queries $X$ and answers $Y$. It is built
inductively: it either stops with an output in $\alpha$, or asks a query $x \in X$ and continues
with an algorithm that depends on the answer $y \in Y$.

Formalized by `Cslib.Crypto.Framework.OracleComp`, an abbreviation declared in [CSLibExt/Crypto/Framework/Oracle.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Framework/Oracle.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/security-games/oracle-algorithms/index.html#oracle-comp).

## The oracle algorithm that stops at once

For an output $a \in \alpha$, this is the
adaptive oracle algorithm with queries in $X$ and answers in $Y$ that asks no query and stops
with output $a$.

Formalized by `Cslib.Crypto.Framework.OracleComp.done`, an abbreviation declared in [CSLibExt/Crypto/Framework/Oracle.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Framework/Oracle.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/security-games/oracle-algorithms/index.html#done).

## Query step

For a point $x \in X$ and a continuation $k$ assigning an oracle algorithm to
each answer $y \in Y$, the oracle algorithm that first queries $x$ and then continues with
$k(y)$, where $y$ is the answer.

Formalized by `Cslib.Crypto.Framework.OracleComp.query`, an abbreviation declared in [CSLibExt/Crypto/Framework/Oracle.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Framework/Oracle.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/security-games/oracle-algorithms/index.html#query).

## Running an oracle algorithm

Given a function $O : X \to Y$, the run of an oracle
algorithm with queries in $X$, answers in $Y$ and outputs in $\alpha$ is its output when every
query $x$ is answered by $O(x)$: an algorithm that stops with output $a$ runs to $a$, and one
that queries $x$ and continues with $k(y)$ on answer $y$ runs to the run of $k(O(x))$.

Formalized by `Cslib.Crypto.Framework.OracleComp.run`, a definition declared in [CSLibExt/Crypto/Framework/Oracle.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Framework/Oracle.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/security-games/oracle-algorithms/index.html#run).

## Queries of an oracle algorithm

For an oracle algorithm $c$ and a function
$O : X \to Y$, the queries of $c$ against $O$ are the list of the points of $X$ that $c$ asks,
in order, when every query $x$ is answered by $O(x)$: the empty list if $c$ stops, and otherwise
the first query $x$ followed by the queries of the continuation on the answer $O(x)$.

Formalized by `Cslib.Crypto.Framework.OracleComp.queries`, a definition declared in [CSLibExt/Crypto/Framework/Oracle.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Framework/Oracle.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/security-games/oracle-algorithms/index.html#queries).

## Locality of oracle runs

Let $c$ be an oracle algorithm and let $O, O' : X \to Y$ agree
at every query of $c$ against $O$. Then $c$ has the same output against $O$ as against $O'$, and
the same list of queries against $O$ as against $O'$.

Formalized by `Cslib.Crypto.Framework.OracleComp.run_congr`, a theorem declared in [CSLibExt/Crypto/Framework/Oracle.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Framework/Oracle.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/security-games/oracle-algorithms/index.html#run-congr).

## Running a sequential composition

Let $c$ be an oracle algorithm with outputs in $\alpha$,
let $g$ map each $a \in \alpha$ to an oracle algorithm with outputs in $\beta$, and let
$O : X \to Y$. Running against $O$ the composition that first runs $c$ and then continues with
$g$ applied to its output gives the output of $g(a)$ run against $O$, where $a$ is the output
of $c$ run against $O$.

Formalized by `Cslib.Crypto.Framework.OracleComp.run_bind`, a theorem declared in [CSLibExt/Crypto/Framework/Oracle.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Framework/Oracle.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/security-games/oracle-algorithms/index.html#run-bind).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Oracle algorithms](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/security-games/oracle-algorithms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/cryptography/security-games/oracle-algorithms)
