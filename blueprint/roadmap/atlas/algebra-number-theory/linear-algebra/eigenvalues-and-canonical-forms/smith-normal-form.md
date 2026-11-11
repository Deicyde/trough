---
declaration: section
origin: cited
lean: Submodule.exists_smith_normal_form_dvd_chain, MathlibExt.LinearAlgebra.SmithNormalFormWanted.smithNormalForm
statement: formalized
proof: formalized
---

# Smith normal form

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/smith-normal-form/index.html).

## Submodule

## Smith normal form with a divisibility chain

Let $R$ be a principal ideal domain, let $M$
be a finitely generated free $R$-module and let $N$ be a submodule of $M$. Then there are natural
numbers $n \le m$, a basis $e_0, \dots, e_{m-1}$ of $M$, a basis $f_0, \dots, f_{n-1}$ of $N$ and
nonzero elements $a_0, \dots, a_{n-1}$ of $R$ such that $f_i = a_i e_i$ in $M$ for every $i < n$
and $a_i \mid a_{i+1}$ whenever $i + 1 < n$.

Formalized by `Submodule.exists_smith_normal_form_dvd_chain`, a theorem declared in [MathlibExt/LinearAlgebra/SmithNormalForm.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/SmithNormalForm.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/smith-normal-form/index.html#exists-smith-normal-form-dvd-chain).

## Smith normal form

Let $R$ be a principal ideal domain, let $M$ be a finitely generated free
$R$-module and let $N$ be a submodule of $M$. Then there are natural numbers $n \le m$, a basis
$e_0, \dots, e_{m-1}$ of $M$, a basis $f_0, \dots, f_{n-1}$ of $N$ and nonzero elements
$a_0, \dots, a_{n-1}$ of $R$ such that $f_i = a_i e_i$ in $M$ for every $i < n$ and
$a_i \mid a_{i+1}$ whenever $i + 1 < n$.

## Sources

- H. J. S. Smith, Phil. Trans. R. Soc. Lond. 151 (1861), 293-326, DOI 10.1098/RSTL.1861.0016. It is `Submodule.exists_smith_normal_form_dvd_chain`, kept under the source's name.

Formalized by `MathlibExt.LinearAlgebra.SmithNormalFormWanted.smithNormalForm`, a theorem declared in [MathlibExt/LinearAlgebra/SmithNormalForm.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/SmithNormalForm.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/smith-normal-form/index.html#smith-normal-form).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Smith normal form](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/smith-normal-form/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/smith-normal-form)
