---
declaration: theorem
origin: cited
lean: BatchedFri.Spec.batchedFRI_soundness_affineSpace, BatchedFri.Spec.batchedFRI_soundness_powers, BatchedFri.Spec.batchedFRI_soundness_multilinear, BatchedFri.Spec.batchedFRI_soundness_multilinear_johnson
statement: formalized
---

# Batched FRI with concrete generators

Under the hypotheses of Theorem [Batched FRI soundness](thm-batched-fri-soundness.md) without the $\mathsf{caError}$ assumption, the soundness error is the FRI error plus the following batching error.

- Affine space $c\mapsto(1,c_1,\ldots,c_m)$, $c\in\mathbb{F}^m$, with $0\lt \delta<1-\sqrt\rho$: $\varepsilon_{\mathrm{BCIKS}}(\delta)$.

- Powers $c\mapsto(1,c,\ldots,c^m)$, $c\in\mathbb{F}$, with $0\lt \delta<1-\sqrt\rho$: $m\cdot\varepsilon_{\mathrm{BCIKS}}(\delta)$.

- Multilinear monomials in $t$ variables, so $m+1=2^t$, with $\delta>0$ at most the relative unique decoding radius of $C_0$: $t\cdot 2^n/|\mathbb{F}|$.

- The same multilinear generator, with $\delta_{\min}$ the relative minimum distance of $C_0$, $0\lt \eta\lt \delta_{\min}$ and $0\lt \delta\leq 1-(1-\delta_{\min}+\eta)^{1/3}$: $t$ times the affine-line MCA error

    $$
    \frac{1}{|\mathbb{F}|}\left(\frac{2^n+6}{\eta}
    +\frac{2}{\eta\bigl((1-\delta_{\min}+\eta)^{1/3}
    -(1-\delta_{\min}+\eta)^{1/2}\bigr)}\right),
    $$

    truncated below at $0$.

## Depends on

- [Batched FRI soundness](thm-batched-fri-soundness.md)

## Lean

Stated as [`BatchedFri.Spec.batchedFRI_soundness_affineSpace`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BatchedFri.Spec.batchedFRI_soundness_affineSpace), [`BatchedFri.Spec.batchedFRI_soundness_powers`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BatchedFri.Spec.batchedFRI_soundness_powers), [`BatchedFri.Spec.batchedFRI_soundness_multilinear`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BatchedFri.Spec.batchedFRI_soundness_multilinear), [`BatchedFri.Spec.batchedFRI_soundness_multilinear_johnson`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BatchedFri.Spec.batchedFRI_soundness_multilinear_johnson); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/fri.tex, line 339](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/fri.tex#L339)
