---
declaration: definition
origin: cited
lean: MIPRE.povmDistance, MIPRE.IsPOVMClose
statement: formalized
---

# POVM distance

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] Let $\mu$ be a distribution on a finite set ${\mathcal{X}}$, and $\{M^x_a\}$, $\{N^x_a\}$ families of POVMs. We say $M$ and $N$ are *$\delta$-close*, written $M^x_a \approx_\delta N^x_a$, if $\mathop{\mathbb{E}}_{x \sim \mu} \sum_a \left\| {M^x_a - N^x_a} \right\|_{hs}^2 \leq \delta$. Since each difference $M^x_a - N^x_a$ is Hermitian, the summand equals $\tau((M^x_a - N^x_a)^2)$.

## Depends on

- [Normalized Hilbert–Schmidt norm](def-hs-norm.md)

## Lean

Formalized as [`MIPRE.povmDistance`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.povmDistance), [`MIPRE.IsPOVMClose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPOVMClose).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 493](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L493)
