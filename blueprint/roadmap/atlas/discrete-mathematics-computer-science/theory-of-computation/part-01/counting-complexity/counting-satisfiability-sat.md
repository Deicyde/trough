---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.CountSATSharpPComplete.countSatFun, MetaMathlibExt.Complexity.KeyTheorems.CountSATSharpPComplete.count_sat_sharpP_complete
statement: formalized
---

# Counting satisfiability (#SAT)

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/counting-satisfiability-sat/index.html).

## Counting satisfying assignments of a CNF formula

The counting function $f$ from
bitstrings to natural numbers is defined as follows. If a bitstring $x$ decodes, under the
canonical bitstring encoding of pairs, to a pair $(s, \varphi)$ of a bitstring $s$ of length $n$
and a CNF formula $\varphi$ every literal of which has variable index less than $n$, then $f(x)$
is the number of assignments $a : \{0, \dots, n - 1\} \to \{\mathrm{true}, \mathrm{false}\}$
such that $\varphi$ is satisfied by the assignment sending each variable $v < n$ to $a(v)$ and
every other variable to false. Otherwise $f(x) = 0$.

The bitstring $s$ serves only to give the number of variables $n$ in unary.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.CountSATSharpPComplete.countSatFun`, a definition declared in [WantedExt/Complexity/KeyTheorems/CountSATSharpPCompleteWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/CountSATSharpPCompleteWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/counting-satisfiability-sat/index.html#count-sat-fun).

## Counting SAT is #P-complete

The function counting the satisfying assignments of a CNF
formula is $\#P$-complete: it lies in $\#P$, and every function in $\#P$ is computed from it by
a polynomial-time oracle machine.

## Sources

- L. G. Valiant, "The complexity of enumeration and reliability problems", SIAM Journal on Computing 8 (1979), 410-421.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.CountSATSharpPComplete.count_sat_sharpP_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/CountSATSharpPCompleteWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/CountSATSharpPCompleteWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/counting-satisfiability-sat/index.html#count-sat-sharp-p-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Counting satisfiability (#SAT)](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/counting-satisfiability-sat/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/counting-complexity/counting-satisfiability-sat)
