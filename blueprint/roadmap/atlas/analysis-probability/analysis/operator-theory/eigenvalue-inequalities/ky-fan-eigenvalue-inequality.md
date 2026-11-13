---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.KyFanWanted.eigPrefSum, MathlibExt.Analysis.InnerProductSpace.KyFanWanted.ky_fan_eigenvalue_sum_le
statement: formalized
proof: formalized
---

# Ky Fan eigenvalue inequality

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/ky-fan-eigenvalue-inequality/index.html).

## Prefix sum of a finite real sequence

For real numbers $\lambda_0, \dots, \lambda_{n-1}$
and a natural number $k \le n$, the prefix sum of length $k$ is $\sum_{i < k} \lambda_i$, the
sum of the first $k$ entries. Applied to the eigenvalues of a Hermitian matrix, listed in
decreasing order, it is the sum of the $k$ largest ones.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KyFanWanted.eigPrefSum`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/KyFan.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/KyFan.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/ky-fan-eigenvalue-inequality/index.html#eig-pref-sum).

## Ky Fan inequality for sums of largest eigenvalues

Let $A$ and $B$ be Hermitian $n \times n$
complex matrices and let $k \le n$. Then the sum of the $k$ largest eigenvalues of $A + B$ is at
most the sum of the $k$ largest eigenvalues of $A$ plus the sum of the $k$ largest eigenvalues
of $B$, where eigenvalues are counted with multiplicity.

## Sources

- Ky Fan, On a theorem of Weyl, PNAS 35 (1949), 652-655, DOI 10.1073/pnas.35.11.652.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KyFanWanted.ky_fan_eigenvalue_sum_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KyFan.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/KyFan.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/ky-fan-eigenvalue-inequality/index.html#ky-fan-eigenvalue-sum-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ky Fan eigenvalue inequality](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/ky-fan-eigenvalue-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/eigenvalue-inequalities/ky-fan-eigenvalue-inequality)
