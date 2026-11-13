---
declaration: section
origin: cited
lean: MetaMathlibExt.primeIdealCubicSymbolFactorRaw, MetaMathlibExt.cubicResidueSymbolRaw, MetaMathlibExt.primeIdealCubicSymbol, MetaMathlibExt.IsCubicResidueDenominator, MetaMathlibExt.cubicResidueSymbol
statement: formalized
proof: formalized
---

# Cubic residue symbol

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/cubic-residue-symbol/index.html).

## Totalized prime-ideal cubic symbol

Let $K$ be a number field that is the third
cyclotomic extension of $\mathbb{Q}$, with ring of integers $\mathcal{O}_K$, let $\zeta \in K$ be
a primitive cube root of unity and let $\omega$ be $\zeta$ regarded as an element of
$\mathcal{O}_K$. For an ideal $P$ of $\mathcal{O}_K$ and $a \in \mathcal{O}_K$: if $P$ is a
nonzero prime ideal whose absolute norm $N(P)$ is coprime to $3$, the value is $0$ when
$a \in P$, and otherwise the unique $c \in \{1, \omega, \omega^2\}$ with
$c \equiv a^{(N(P) - 1)/3} \pmod{P}$; for every other ideal $P$ the value is $1$.

Formalized by `MetaMathlibExt.primeIdealCubicSymbolFactorRaw`, a definition declared in [MathlibExt/NumberTheory/Cyclotomic/CubicResidueSymbol.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Cyclotomic/CubicResidueSymbol.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/cubic-residue-symbol/index.html#prime-ideal-cubic-symbol-factor-raw).

## Totalized cubic residue symbol

Let $K$ be a number field that is the third cyclotomic
extension of $\mathbb{Q}$, with ring of integers $\mathcal{O}_K$, and let $\zeta \in K$ be a
primitive cube root of unity. For $a, n \in \mathcal{O}_K$, the value is $0$ if $n = 0$;
otherwise it is the product, over the prime ideals $P$ in the factorization of the principal
ideal $(n)$ counted with multiplicity, of the totalized prime-ideal cubic symbol of $a$ at $P$
(which is $1$ unless $P$ is a nonzero prime ideal whose absolute norm is coprime to $3$).

Formalized by `MetaMathlibExt.cubicResidueSymbolRaw`, a definition declared in [MathlibExt/NumberTheory/Cyclotomic/CubicResidueSymbol.lean, line 490](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Cyclotomic/CubicResidueSymbol.lean#L490). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/cubic-residue-symbol/index.html#cubic-residue-symbol-raw).

## Cubic residue symbol at a prime ideal

Let $K$ be a number field that is the third
cyclotomic extension of $\mathbb{Q}$, with ring of integers $\mathcal{O}_K$, let $\zeta \in K$ be
a primitive cube root of unity and let $\omega$ be $\zeta$ regarded as an element of
$\mathcal{O}_K$. For a nonzero prime ideal $P$ of $\mathcal{O}_K$ whose absolute norm $N(P)$ is
coprime to $3$ and for $a \in \mathcal{O}_K$, the cubic residue symbol $(a/P)_3$ is $0$ if
$a \in P$, and otherwise the unique $c \in \{1, \omega, \omega^2\}$ with
$c \equiv a^{(N(P) - 1)/3} \pmod{P}$.

Formalized by `MetaMathlibExt.primeIdealCubicSymbol`, a definition declared in [MathlibExt/NumberTheory/Cyclotomic/CubicResidueSymbol.lean, line 647](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Cyclotomic/CubicResidueSymbol.lean#L647). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/cubic-residue-symbol/index.html#prime-ideal-cubic-symbol).

## Cubic residue denominators

Let $K$ be a number field that is the third cyclotomic
extension of $\mathbb{Q}$, with ring of integers $\mathcal{O}_K$. An element $n \in \mathcal{O}_K$
is a cubic residue denominator when $n \neq 0$ and the absolute norm of the principal ideal
$(n)$ is coprime to $3$.

Formalized by `MetaMathlibExt.IsCubicResidueDenominator`, a definition declared in [MathlibExt/NumberTheory/Cyclotomic/CubicResidueSymbol.lean, line 659](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Cyclotomic/CubicResidueSymbol.lean#L659). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/cubic-residue-symbol/index.html#is-cubic-residue-denominator).

## Cubic residue symbol modulo an element

Let $K$ be a number field that is the third
cyclotomic extension of $\mathbb{Q}$, with ring of integers $\mathcal{O}_K$, let $\zeta \in K$ be
a primitive cube root of unity and let $\omega$ be $\zeta$ regarded as an element of
$\mathcal{O}_K$. For $a \in \mathcal{O}_K$ and a cubic residue denominator $n$ (that is,
$n \neq 0$ and the absolute norm of the principal ideal $(n)$ is coprime to $3$), the cubic
residue symbol $(a/n)_3$ is the product, over the prime ideals $P$ in the factorization of $(n)$
counted with multiplicity, of the value that is $0$ if $a \in P$ and otherwise the unique
$c \in \{1, \omega, \omega^2\}$ with $c \equiv a^{(N(P) - 1)/3} \pmod{P}$, where $N(P)$ is the
absolute norm of $P$. Each such $P$ is a nonzero prime ideal whose absolute norm is coprime
to $3$.

Formalized by `MetaMathlibExt.cubicResidueSymbol`, a definition declared in [MathlibExt/NumberTheory/Cyclotomic/CubicResidueSymbol.lean, line 664](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Cyclotomic/CubicResidueSymbol.lean#L664). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/cubic-residue-symbol/index.html#cubic-residue-symbol).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cubic residue symbol](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/cubic-residue-symbol/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/power-residues-reciprocity/cubic-residue-symbol)
