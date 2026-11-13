---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.TwoSATInP.twoSatDec, MetaMathlibExt.Complexity.KeyTheorems.TwoSATInP.two_sat_in_p
statement: formalized
---

# 2-satisfiability

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/2-satisfiability/index.html).

## 2-SAT as a decision problem

The 2-SAT decision problem accepts a bitstring $x$ exactly
when $x$ decodes, under the canonical bitstring encoding, to a pair $(n, \varphi)$ of a natural
number $n$ and a CNF formula $\varphi$ such that every clause of $\varphi$ has at most two
literals, every variable occurring in $\varphi$ is less than $n$, and there is a list
$(a_0, \dots, a_{n-1})$ of booleans such that $\varphi$ is satisfied by the assignment that
sends each variable $v < n$ to $a_v$ and every other variable to false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.TwoSATInP.twoSatDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/TwoSATInPWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/TwoSATInPWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/2-satisfiability/index.html#two-sat-dec).

## 2-SAT is in P

The 2-SAT decision problem lies in the complexity class P.

## Sources

- M. Davis, G. Logemann, and D. Loveland, "A machine program for theorem-proving", Communications of the ACM 5 (1962), 394-397; B. Aspvall, M. F. Plass, and R. E. Tarjan, "A linear-time algorithm for testing the truth of certain quantified Boolean formulas", Information Processing Letters 8 (1979), 121-123.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.TwoSATInP.two_sat_in_p` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/TwoSATInPWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/TwoSATInPWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/2-satisfiability/index.html#two-sat-in-p).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: 2-satisfiability](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/2-satisfiability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/polynomial-time-problems/2-satisfiability)
