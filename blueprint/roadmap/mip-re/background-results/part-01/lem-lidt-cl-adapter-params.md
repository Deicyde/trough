---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.clK, MIPRE.LIDT.deltaCL, MIPRE.LIDT.lidtError_le_deltaCL
statement: formalized
proof: formalized
---

# The parameter choice

Take $a=2\cdot10^{11}$, $b=1/40000$ and $k=400m^3d+400m$. Then for all $m,d\geq1$, all $q$ and all $\varepsilon\geq0$,

$$
100000\,k^2m^4\Bigl((3m\varepsilon)^{b}+(d/q)^{b}+e^{-k/(2560000m^2)}\Bigr)
\ \leq\ a(dm)^{a}\bigl(\varepsilon^{b}+q^{-b}+2^{-bmd}\bigr),
$$

the left side being the error of Theorem [Quantum soundness of the canonical-line low individual degree test](thm-lidt-soundness.md) at $k$ on failure $3m\varepsilon$ and the right side $\delta_{\mathrm{CL}}$ at $\mathrm{ldc}=1$. Moreover $k\geq400md$ and $k>0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Term by term. $(3m\varepsilon)^b=(3m)^b\varepsilon^b\leq 3m\,\varepsilon^b$ and $(d/q)^b=d^b q^{-b}\leq d\,q^{-b}$, since $x^b\leq x$ for $x\geq1$ and $b\leq1$. The exponential is where $k$ is chosen: $e^{-k/(2560000m^2)}\leq2^{-bmd}$ asks for $k\geq 2560000\,b\,m^3d\ln2=64(\ln2)m^3d$, about $44.4\,m^3d$, and $400m^3d$ clears it; the $400m$ summand is there only so that $k>0$ and $k\geq400md$ hold for every $m,d\geq1$. The prefactor is then $100000k^2m^4\cdot3md\leq1.92\cdot10^{11}(dm)^{11}\leq a(dm)^a$, using $k\leq800m^3d$.

$d\geq1$ is needed and is not cosmetic: at $d=0$ the right side is identically zero, so no positive error could be bounded by it.

## Lean

Formalized as [`MIPRE.LIDT.clK`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.clK), [`MIPRE.LIDT.deltaCL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.deltaCL), [`MIPRE.LIDT.lidtError_le_deltaCL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.lidtError_le_deltaCL).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 893](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L893)
