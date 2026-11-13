---
declaration: section
origin: cited
lean: SL2.HasEigenvalues, SL2.isConj_diag2_iff, SL2.normal_subgroup_contains_all_conj_to_diag, SL2.eigenvalues_implies_isConj_diag2, SL2.eigenvalues_implies_conj_to_diag, SL2.normal_contains_all_with_eigenvalues
statement: formalized
proof: formalized
---

# Conjugacy by eigenvalues in SL₂

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/conjugacy-by-eigenvalues-in-sl/index.html).

## Elements of $\mathrm{SL}_2(F)$ with eigenvalues $s$ and $s^{-1}$

Let $F$ be a field and
let $s \in F$. A matrix $M \in \mathrm{SL}_2(F)$ has eigenvalues $s$ and $s^{-1}$ if its
characteristic polynomial is $(X - s)(X - s^{-1})$.

Formalized by `SL2.HasEigenvalues`, a definition declared in [MathlibExt/GroupTheory/SL2EigenvalueConjugacy.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/SL2EigenvalueConjugacy.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/conjugacy-by-eigenvalues-in-sl/index.html#has-eigenvalues).

## Conjugacy to $\operatorname{diag}(s, s^{-1})$ in terms of a conjugator

Let $F$ be a field,
let $s \in F$ with $s \ne 0$, and let $M \in \mathrm{SL}_2(F)$. Then $M$ is conjugate in
$\mathrm{SL}_2(F)$ to the diagonal matrix $\operatorname{diag}(s, s^{-1})$ if and only if there is
$P \in \mathrm{SL}_2(F)$ such that the matrix $P M P^{-1}$ equals
$\operatorname{diag}(s, s^{-1})$.

Formalized by `SL2.isConj_diag2_iff`, a theorem declared in [MathlibExt/GroupTheory/SL2EigenvalueConjugacy.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/SL2EigenvalueConjugacy.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/conjugacy-by-eigenvalues-in-sl/index.html#is-conj-diag2-iff).

## Conjugates of $\operatorname{diag}(s, s^{-1})$ lie in the same normal subgroups of $\mathrm{SL}_2(F)$

**Conjugates of $\operatorname{diag}(s, s^{-1})$ lie in the same normal subgroups of
$\mathrm{SL}_2(F)$.** Let $F$ be a field, let $N$ be a normal subgroup of $\mathrm{SL}_2(F)$, and
let $s \in F$. Suppose $N$ contains a matrix $B$ for which some $P \in \mathrm{SL}_2(F)$ makes the
matrix $P B P^{-1}$ equal to the diagonal matrix $\operatorname{diag}(s, s^{-1})$. Then $N$
contains every $Q \in \mathrm{SL}_2(F)$ for which some $P \in \mathrm{SL}_2(F)$ makes $P Q P^{-1}$
equal to $\operatorname{diag}(s, s^{-1})$.

The two matrices are conjugate to each other, via the diagonal matrix, and a normal subgroup is
closed under conjugation.

Formalized by `SL2.normal_subgroup_contains_all_conj_to_diag`, a theorem declared in [MathlibExt/GroupTheory/SL2EigenvalueConjugacy.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/SL2EigenvalueConjugacy.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/conjugacy-by-eigenvalues-in-sl/index.html#normal-subgroup-contains-all-conj-to-dia).

## Distinct eigenvalues give conjugacy to $\operatorname{diag}(s, s^{-1})$ in $\mathrm{SL}_2(F)$

**Distinct eigenvalues give conjugacy to $\operatorname{diag}(s, s^{-1})$ in
$\mathrm{SL}_2(F)$.** Let $F$ be a field and let $s \in F$ with $s \ne s^{-1}$ and $s \ne 0$. If
$M \in \mathrm{SL}_2(F)$ has eigenvalues $s$ and $s^{-1}$, that is, characteristic polynomial
$(X - s)(X - s^{-1})$, then $M$ is conjugate in $\mathrm{SL}_2(F)$ to the diagonal matrix
$\operatorname{diag}(s, s^{-1})$.

The proof builds the conjugating matrix from eigenvectors for $s$ and $s^{-1}$: distinct
eigenvalues give linearly independent eigenvectors, so the matrix of eigenvectors has nonzero
determinant, and rescaling its first column makes the determinant $1$.

Formalized by `SL2.eigenvalues_implies_isConj_diag2`, a theorem declared in [MathlibExt/GroupTheory/SL2EigenvalueConjugacy.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/SL2EigenvalueConjugacy.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/conjugacy-by-eigenvalues-in-sl/index.html#eigenvalues-implies-is-conj-diag2).

## Diagonalizing elements of $\mathrm{SL}_2(F)$ with distinct eigenvalues

Let $F$ be a field,
let $s \in F$ with $s \ne s^{-1}$, and let $M \in \mathrm{SL}_2(F)$ have eigenvalues $s$ and
$s^{-1}$, that is, characteristic polynomial $(X - s)(X - s^{-1})$. Then there is
$P \in \mathrm{SL}_2(F)$ such that the matrix $P M P^{-1}$ equals the diagonal matrix
$\operatorname{diag}(s, s^{-1})$.

Formalized by `SL2.eigenvalues_implies_conj_to_diag`, a theorem declared in [MathlibExt/GroupTheory/SL2EigenvalueConjugacy.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/SL2EigenvalueConjugacy.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/conjugacy-by-eigenvalues-in-sl/index.html#eigenvalues-implies-conj-to-diag).

## Matrices with the same distinct eigenvalues lie in the same normal subgroups of $\mathrm{SL}_2(F)$

**Matrices with the same distinct eigenvalues lie in the same normal subgroups of
$\mathrm{SL}_2(F)$.** Let $F$ be a field, let $N$ be a normal subgroup of $\mathrm{SL}_2(F)$, and
let $s \in F$ with $s \ne s^{-1}$. If $N$ contains a matrix with eigenvalues $s$ and $s^{-1}$, then
$N$ contains every matrix in $\mathrm{SL}_2(F)$ with eigenvalues $s$ and $s^{-1}$.

Formalized by `SL2.normal_contains_all_with_eigenvalues`, a theorem declared in [MathlibExt/GroupTheory/SL2EigenvalueConjugacy.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/SL2EigenvalueConjugacy.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/conjugacy-by-eigenvalues-in-sl/index.html#normal-contains-all-with-eigenvalues).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conjugacy by eigenvalues in SL₂](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/conjugacy-by-eigenvalues-in-sl/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/linear-groups/conjugacy-by-eigenvalues-in-sl)
