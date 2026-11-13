---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.LacunaryAvoidingBoundedGapSumsetErdosProblem1112Wanted.HasLacunaryThreshold, MathlibExt.Combinatorics.LacunaryAvoidingBoundedGapSumsetErdosProblem1112Wanted.lacunaryThresholdGapsTwoThreeThreeFold, MathlibExt.Combinatorics.LacunaryAvoidingBoundedGapSumsetErdosProblem1112Wanted.lacunaryThresholdGapsTwoThreeThreeFold_refuted
statement: formalized
---

# Bounded-gap sumsets avoiding lacunary sequences

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/bounded-gap-sumsets-avoiding-lacunary-sequences/index.html).

## Lacunary threshold for bounded-gap sumsets

For natural numbers $d_1$, $d_2$ and $k$,
the threshold $r_k(d_1, d_2)$ of Erdős Problem 1112 exists when there is a natural number $r$
such that for every strictly increasing sequence $b_0 < b_1 < \cdots$ of positive integers with
$b_{i+1} \ge r b_i$ for all $i$, there is a sequence $a_0, a_1, \dots$ of positive integers with
$a_i + d_1 \le a_{i+1} \le a_i + d_2$ for all $i$ such that no $b_i$ lies in the $k$-fold sumset
of $A = \{a_0, a_1, \dots\}$, the set of all sums of $k$ elements of $A$ with repetition allowed
(for $k = 0$ this set is $\{0\}$).

Formalized by `MathlibExt.Combinatorics.LacunaryAvoidingBoundedGapSumsetErdosProblem1112Wanted.HasLacunaryThreshold`, a definition declared in [WantedExt/Combinatorics/LacunaryAvoidingBoundedGapSumsetErdosProblem1112Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LacunaryAvoidingBoundedGapSumsetErdosProblem1112Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/bounded-gap-sumsets-avoiding-lacunary-sequences/index.html#has-lacunary-threshold).

## Statement of Erdős Problem 1112 for gaps in $(2, 3)$ and triple sums

The threshold
$r_3(2, 3)$ exists: there is a natural number $r$ such that for every strictly increasing
sequence $b_0 < b_1 < \cdots$ of positive integers with $b_{i+1} \ge r b_i$ for all $i$, there is
a sequence $a_0, a_1, \dots$ of positive integers with $a_i + 2 \le a_{i+1} \le a_i + 3$ for all
$i$ such that no $b_i$ is a sum $x + y + z$ of three, not necessarily distinct, terms $x, y, z$
of the sequence $a$.

Formalized by `MathlibExt.Combinatorics.LacunaryAvoidingBoundedGapSumsetErdosProblem1112Wanted.lacunaryThresholdGapsTwoThreeThreeFold`, a definition declared in [WantedExt/Combinatorics/LacunaryAvoidingBoundedGapSumsetErdosProblem1112Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LacunaryAvoidingBoundedGapSumsetErdosProblem1112Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/bounded-gap-sumsets-avoiding-lacunary-sequences/index.html#lacunary-threshold-gaps-two-three-three).

## Bollobás–Hegyvári–Jin theorem on Erdős Problem 1112

There is no natural number $r$ such
that for every strictly increasing sequence $b_0 < b_1 < \cdots$ of positive integers with
$b_{i+1} \ge r b_i$ for all $i$, there is a sequence $a_0, a_1, \dots$ of positive integers with
$a_i + 2 \le a_{i+1} \le a_i + 3$ for all $i$ such that no $b_i$ is a sum of three, not
necessarily distinct, terms of the sequence $a$. In other words, the threshold $r_3(2, 3)$ of
Erdős Problem 1112 (gaps between $2$ and $3$, triple sums) does not exist.

## Sources

- T. F. Bloom, Erdős Problems, Problem #1112, https://www.erdosproblems.com/1112 (status OPEN (LEAN)); resolution: B. Bollobás, N. Hegyvári and G. Jin, On a problem of Erdős and Graham, Discrete Math. 175 (1997), 253-257, main result (Theorem 3 of the paper), as recorded on erdosproblems.com/1112: for any integers 1 ≤ r₁ < r₂ < ⋯ there is a B with b_{i+1} ≥ r_i b_i such that (A + A + A) ∩ B ≠ ∅ for every A with 2 ≤ a_{i+1} - a_i ≤ 3; erdosproblems.com/1112: 'It follows from the above results that r₂(2, 3) = 2 and that r₃(2, 3) does not exist', https://doi.org/10.1016/S0012-365X(96)00122-7.

Stated but not proved: `MathlibExt.Combinatorics.LacunaryAvoidingBoundedGapSumsetErdosProblem1112Wanted.lacunaryThresholdGapsTwoThreeThreeFold_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/LacunaryAvoidingBoundedGapSumsetErdosProblem1112Wanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LacunaryAvoidingBoundedGapSumsetErdosProblem1112Wanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/bounded-gap-sumsets-avoiding-lacunary-sequences/index.html#lacunary-threshold-gaps-two-three-three-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounded-gap sumsets avoiding lacunary sequences](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/bounded-gap-sumsets-avoiding-lacunary-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/additive-bases/bounded-gap-sumsets-avoiding-lacunary-sequences)
