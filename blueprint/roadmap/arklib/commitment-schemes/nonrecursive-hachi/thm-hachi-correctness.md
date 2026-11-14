---
declaration: theorem
origin: cited
lean: ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursive_perfectCorrectness, ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursiveConcrete_perfectCorrectness, ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursiveOpening_perfectCompleteness
statement: formalized
---

# Perfect correctness of nonrecursive Hachi

Assume

- $z_{\max}\leq(b-1-\lfloor b/2\rfloor)\sum_{e\lt \tau}b^{e}$, the positive capacity of $\tau$ balanced base-$b$ digits;
- $2^{r}\,\omega\,\lfloor b/2\rfloor\leq z_{\max}$ and $\tau>0$;
- $\delta_b>0$, $2^\alpha>0$ and $b_0>0$;
- $(\mu_0+n_0\lceil\log_{b_0}q\rceil)\cdot 2^{\alpha}\leq 2^{M+1}$;
- $b_0-1\leq\gamma$.

Then, for every lift commitment, every initial oracle state and every implementation of the uniform oracle, the scheme is perfectly correct. The same holds for the concrete instance. The opening reduction alone is perfectly complete under these assumptions together with $\kappa\geq 1$ and a bound $\beta^2\geq 2^m\delta_b\,2^\alpha\lfloor b/2\rfloor^2$ on its auxiliary parameters $\kappa$ and $\beta^2$.

## Depends on

- [Nonrecursive Hachi](def-hachi-nonrecursive.md)

## Lean

Stated as [`ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursive_perfectCorrectness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursive_perfectCorrectness), [`ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursiveConcrete_perfectCorrectness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursiveConcrete_perfectCorrectness), [`ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursiveOpening_perfectCompleteness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursiveOpening_perfectCompleteness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: commitments/hachi.tex, line 43](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/commitments/hachi.tex#L43)
