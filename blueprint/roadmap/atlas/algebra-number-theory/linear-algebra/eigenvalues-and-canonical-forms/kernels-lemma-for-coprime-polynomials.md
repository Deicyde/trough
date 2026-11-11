---
declaration: section
origin: cited
lean: MathlibExt.LinearAlgebra.KernelsLemmaWanted.iSup_ker_aeval_eq_ker_aeval_prod_of_pairwise_isCoprime, MathlibExt.LinearAlgebra.KernelsLemmaWanted.supIndep_ker_aeval_of_pairwise_isCoprime, MathlibExt.LinearAlgebra.KernelsLemmaWanted.iSupIndep_ker_aeval_and_iSup_eq_of_pairwise_isCoprime, MathlibExt.LinearAlgebra.KernelsLemmaWanted.kernels_lemma_pairwise_isCoprime
statement: formalized
proof: formalized
---

# Kernels lemma for coprime polynomials

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/kernels-lemma-for-coprime-polynomials/index.html).

## Kernel of a product of pairwise coprime polynomials

Let $R$ be a commutative ring, $M$
an $R$-module, $f$ an $R$-linear endomorphism of $M$, and $(p_i)_{i \in \iota}$ a family of
polynomials in $R[X]$ that are pairwise coprime, meaning that for all $i \ne j$ there are
$a, b \in R[X]$ with $a p_i + b p_j = 1$. Then for every finite set $s \subseteq \iota$, the sum
of the submodules $\ker p_i(f)$ over $i \in s$ equals $\ker \bigl(\prod_{i \in s} p_i\bigr)(f)$.

Formalized by `MathlibExt.LinearAlgebra.KernelsLemmaWanted.iSup_ker_aeval_eq_ker_aeval_prod_of_pairwise_isCoprime`, a theorem declared in [MathlibExt/LinearAlgebra/KernelsLemma.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/KernelsLemma.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/kernels-lemma-for-coprime-polynomials/index.html#i-sup-ker-aeval-eq-ker-aeval-prod-of-pai).

## Kernels of pairwise coprime polynomials are independent over a finite set

Let $R$ be a
commutative ring, $M$ an $R$-module, $f$ an $R$-linear endomorphism of $M$, and
$(p_i)_{i \in \iota}$ a family of polynomials in $R[X]$ that are pairwise coprime, meaning that
for all $i \ne j$ there are $a, b \in R[X]$ with $a p_i + b p_j = 1$. Then for every finite set
$s \subseteq \iota$, every $i \in s$ and every $t \subseteq s$ with $i \notin t$, the submodule
$\ker p_i(f)$ meets the sum of the submodules $\ker p_j(f)$ over $j \in t$ only in $0$.

Formalized by `MathlibExt.LinearAlgebra.KernelsLemmaWanted.supIndep_ker_aeval_of_pairwise_isCoprime`, a theorem declared in [MathlibExt/LinearAlgebra/KernelsLemma.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/KernelsLemma.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/kernels-lemma-for-coprime-polynomials/index.html#sup-indep-ker-aeval-of-pairwise-is-copri).

## Independence and sum of kernels of pairwise coprime polynomials

Let $R$ be a commutative
ring, $M$ an $R$-module, $f$ an $R$-linear endomorphism of $M$, and $(p_i)_{i \in \iota}$ a
family of polynomials in $R[X]$, indexed by a finite type $\iota$, that are pairwise coprime,
meaning that for all $i \ne j$ there are $a, b \in R[X]$ with $a p_i + b p_j = 1$. Then the
submodules $\ker p_i(f)$ are independent (each meets the sum of the others only in $0$), and
their sum is $\ker \bigl(\prod_{i \in \iota} p_i\bigr)(f)$.

Formalized by `MathlibExt.LinearAlgebra.KernelsLemmaWanted.iSupIndep_ker_aeval_and_iSup_eq_of_pairwise_isCoprime`, a theorem declared in [MathlibExt/LinearAlgebra/KernelsLemma.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/KernelsLemma.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/kernels-lemma-for-coprime-polynomials/index.html#i-sup-indep-ker-aeval-and-i-sup-eq-of-pa).

## Kernels lemma

Let $R$ be a commutative ring, $M$ an $R$-module, $f$ an $R$-linear
endomorphism of $M$, and $(p_i)_{i \in \iota}$ a family of polynomials in $R[X]$, indexed by a
finite type $\iota$, that are pairwise coprime, meaning that for all $i \ne j$ there are
$a, b \in R[X]$ with $a p_i + b p_j = 1$. Then the submodules $\ker p_i(f)$ are independent
(each meets the sum of the others only in $0$), and their sum is
$\ker \bigl(\prod_{i \in \iota} p_i\bigr)(f)$.

The decomposition is internal to $\ker \bigl(\prod_{i \in \iota} p_i\bigr)(f)$; it need not span
all of $M$.

Proof: induction on the number of polynomials from the two-polynomial case, as in the cited French
Wikipedia article. For coprime $p$ and $q$ one has $\ker p(f) + \ker q(f) = \ker (pq)(f)$, which
gives the inductive step, and independence follows because $\ker p_i(f) \cap \ker q(f) = 0$ when
$q$ is the product of the other polynomials.

## Sources

- https://fr.wikipedia.org/wiki/Lemme_des_noyaux; S. Axler, Linear Algebra Done Right, 4th ed., Springer (2024), Section 8C.

Formalized by `MathlibExt.LinearAlgebra.KernelsLemmaWanted.kernels_lemma_pairwise_isCoprime`, a theorem declared in [MathlibExt/LinearAlgebra/KernelsLemma.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/KernelsLemma.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/kernels-lemma-for-coprime-polynomials/index.html#kernels-lemma-pairwise-is-coprime).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kernels lemma for coprime polynomials](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/kernels-lemma-for-coprime-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/kernels-lemma-for-coprime-polynomials)
