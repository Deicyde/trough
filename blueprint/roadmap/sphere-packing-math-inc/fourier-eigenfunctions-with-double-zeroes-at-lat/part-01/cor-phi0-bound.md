---
declaration: corollary
origin: cited
lean: MagicFunction.PolyFourierCoeffBound.norm_φ₀_le
statement: formalized
proof: formalized
---

# phi0-bound

There exists a constant $C_0 > 0$ such that

$$
|\phi_0(z)| \le C_0 e^{-2 \pi \Im z}\qquad\text{(15)}
$$

for all $z$ with $\Im z > 1/2$.

## Depends on

- [ramanujan-formula](../../modular-forms/part-03/thm-ramanujan-formula.md)
- [mod-div-disc-bound](lemma-mod-div-disc-bound.md)
- [Ek-Fourier](../../modular-forms/part-01/lemma-ek-fourier.md)

## Proof

By Ramanujan's formula, $E_2 E_4 - E_6 = 3E_4' = 720 \sum_{n \ge 1} n \sigma_3(n) e^{2 \pi i n z}$ and

$$
(E_2(z) E_4(z) - E_6(z))^{2} = 720^{2} e^{4 \pi i z} + O(e^{5 \pi i z}).
$$

Then the result follows from Lemma [mod-div-disc-bound](lemma-mod-div-disc-bound.md) with $f(z) = (E_2 E_4 - E_6)^2$ and $n_0 = 4$.

## Lean

Formalized as [`MagicFunction.PolyFourierCoeffBound.norm_φ₀_le`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.PolyFourierCoeffBound.norm_φ₀_le).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/construct-a-b.tex, line 131](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L131)
