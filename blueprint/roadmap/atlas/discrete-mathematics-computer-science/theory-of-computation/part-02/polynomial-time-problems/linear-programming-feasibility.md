---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.LPInPWanted.decodeInt, MetaMathlibExt.Complexity.KeyTheorems.LPInPWanted.lpDec, MetaMathlibExt.Complexity.KeyTheorems.LPInPWanted.lp_in_p
statement: formalized
---

# Linear programming feasibility

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/linear-programming-feasibility/index.html).

## Signed integer from a magnitude–sign pair

The integer decoded from a pair $(k, s)$ of a
natural number $k$ and a boolean $s$ is $k$ if $s$ is true and $-k$ if $s$ is false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LPInPWanted.decodeInt`, a definition declared in [WantedExt/Complexity/KeyTheorems/LPInPWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LPInPWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/linear-programming-feasibility/index.html#decode-int).

## Rational linear-program feasibility

The decision problem of rational linear-program
feasibility accepts a bitstring $w$ exactly when $w$ decodes, under the canonical bitstring
encoding, to a pair $(A, b)$ of a list $A$ of $m$ rows, each a list of magnitude–sign pairs, and
a list $b$ of $m'$ magnitude–sign pairs, such that every row of $A$ has the length $n$ of the
first row ($n = 0$ when $m = 0$), $m' = m$, and some $x \in \mathbb{Q}^n$ satisfies
$\sum_{j\lt n} A_{rj} x_j \le b_r$ for every $r < m$. Here a magnitude–sign pair $(k, s)$ of a
natural number $k$ and a boolean $s$ stands for the integer $k$ if $s$ is true and $-k$ if $s$ is
false, $A_{rj}$ is the integer given by the $j$-th entry of the $r$-th row and $b_r$ is the
integer given by the $r$-th entry of $b$. Bitstrings that do not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LPInPWanted.lpDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/LPInPWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LPInPWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/linear-programming-feasibility/index.html#lp-dec).

## Linear programming is in P (Khachiyan)

The decision problem of rational linear-program
feasibility is in the complexity class P. This problem accepts exactly the bitstrings that decode,
under the canonical bitstring encoding, to a list $A$ of $m$ rows of integers, all of the same
length $n$, and a list $b$ of $m$ integers, for which some $x \in \mathbb{Q}^n$ satisfies
$\sum_{j\lt n} A_{rj} x_j \le b_r$ for every $r < m$, where $A_{rj}$ is the $j$-th entry of the
$r$-th row of $A$ and $b_r$ is the $r$-th entry of $b$. Each integer is given as a magnitude–sign
pair $(k, s)$ of a natural number $k$ and a boolean $s$, standing for $k$ if $s$ is true and $-k$
if $s$ is false.

## Sources

- L. G. Khachiyan, "A polynomial algorithm in linear programming", Soviet Mathematics Doklady 20 (1979), 191-194.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.LPInPWanted.lp_in_p` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/LPInPWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LPInPWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/linear-programming-feasibility/index.html#lp-in-p).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear programming feasibility](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/linear-programming-feasibility/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/polynomial-time-problems/linear-programming-feasibility)
