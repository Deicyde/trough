---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.ILPFixedDimInP.decodeIntILP, MetaMathlibExt.Complexity.KeyTheorems.ILPFixedDimInP.ilpFixedDec, MetaMathlibExt.Complexity.KeyTheorems.ILPFixedDimInP.ilp_fixed_dim_in_p
statement: formalized
---

# Integer programming in fixed dimension

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/integer-programming-in-fixed-dimension/index.html).

## Integer from magnitude and sign

A pair $(n, s)$ of a natural number $n$ and a Boolean
sign $s$ decodes to the integer $n$ if $s$ is true and to $-n$ if $s$ is false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ILPFixedDimInP.decodeIntILP`, a definition declared in [WantedExt/Complexity/KeyTheorems/ILPFixedDimInPWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ILPFixedDimInPWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/integer-programming-in-fixed-dimension/index.html#decode-int-ilp).

## Integer linear-programming feasibility in fixed dimension

For a natural number $d$, this
decision problem accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
decoding, to a pair $(A, b)$ such that $A$ is a list of rows, each a list of exactly $d$ integers,
$b$ is a list of integers with as many entries as $A$ has rows, and there is an integer vector
$y \in \mathbb{Z}^d$ with $\sum_{j < d} A_{rj} y_j \le b_r$ for every row index $r$. Each integer
entry is given as a pair $(n, s)$ of a natural number and a sign, standing for $n$ if $s$ is true
and $-n$ otherwise. Every other bitstring is rejected.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ILPFixedDimInP.ilpFixedDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/ILPFixedDimInPWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ILPFixedDimInPWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/integer-programming-in-fixed-dimension/index.html#ilp-fixed-dec).

## Integer linear programming in fixed dimension is in P (Lenstra)

For every natural number
$d$, integer linear-programming feasibility in dimension $d$ is in the complexity class P.

## Sources

- H. W. Lenstra Jr., "Integer programming with a fixed number of variables", Mathematics of Operations Research 8 (1983), 538-548.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.ILPFixedDimInP.ilp_fixed_dim_in_p` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/ILPFixedDimInPWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ILPFixedDimInPWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/integer-programming-in-fixed-dimension/index.html#ilp-fixed-dim-in-p).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integer programming in fixed dimension](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/integer-programming-in-fixed-dimension/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/polynomial-time-problems/integer-programming-in-fixed-dimension)
