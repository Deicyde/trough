---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ZeroSumFixedLengthTwoResiduesErdosProblem541Wanted.fixedZeroSumLengthTwoResidues, MathlibExt.Combinatorics.ZeroSumFixedLengthTwoResiduesErdosProblem541Wanted.fixedZeroSumLengthTwoResidues_holds
statement: formalized
---

# Graham's zero-sum conjecture

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/graham-s-zero-sum-conjecture/index.html).

## Graham's zero-sum statement (Erdős Problem 541)

This is the statement that for every
prime $p$ and every sequence $a_0, \dots, a_{p-1}$ of residues modulo $p$, not necessarily
distinct, if there is a natural number $r$ such that every nonempty set
$S \subseteq \{0, \dots, p-1\}$ with $\sum_{i \in S} a_i = 0$ in $\mathbb{Z}/p\mathbb{Z}$ has
exactly $r$ elements, then at most two distinct residues occur among $a_0, \dots, a_{p-1}$.

Formalized by `MathlibExt.Combinatorics.ZeroSumFixedLengthTwoResiduesErdosProblem541Wanted.fixedZeroSumLengthTwoResidues`, a definition declared in [WantedExt/Combinatorics/ZeroSumFixedLengthTwoResiduesErdosProblem541Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ZeroSumFixedLengthTwoResiduesErdosProblem541Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/graham-s-zero-sum-conjecture/index.html#fixed-zero-sum-length-two-residues).

## Zero sums of a single length use at most two residues (Erdős Problem 541)

For every prime
$p$ and every sequence $a_0, \dots, a_{p-1}$ of residues modulo $p$, not necessarily distinct, if
there is a natural number $r$ such that every nonempty set $S \subseteq \{0, \dots, p-1\}$ with
$\sum_{i \in S} a_i = 0$ in $\mathbb{Z}/p\mathbb{Z}$ has exactly $r$ elements, then at most two
distinct residues occur among $a_0, \dots, a_{p-1}$.

Resolved true: Erdős and Szemerédi proved it for all large primes $p$, and Gao, Hamidoune and Wang
for every modulus.

## Sources

- T. F. Bloom, Erdős Problems, Problem #541, https://www.erdosproblems.com/541 (status PROVED (LEAN)); resolution: W. Gao, Y. O. Hamidoune and G. Wang, Distinct length modular zero-sum subsequences: a proof of Graham's conjecture, J. Number Theory (2010), 1425-1431, erdosproblems.com/541: proved by Erdős and Szemerédi for large p and by Gao, Hamidoune and Wang for all moduli, https://www.erdosproblems.com/541.

Stated but not proved: `MathlibExt.Combinatorics.ZeroSumFixedLengthTwoResiduesErdosProblem541Wanted.fixedZeroSumLengthTwoResidues_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ZeroSumFixedLengthTwoResiduesErdosProblem541Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ZeroSumFixedLengthTwoResiduesErdosProblem541Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/graham-s-zero-sum-conjecture/index.html#fixed-zero-sum-length-two-residues-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graham's zero-sum conjecture](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/graham-s-zero-sum-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/graham-s-zero-sum-conjecture)
