---
declaration: lemma
origin: cited
lean: SpherePacking.ModularForms.E₄_eq_thetaE4, SpherePacking.ModularForms.E₆_eq_thetaE6, Delta_eq_H₂_H₃_H₄
statement: formalized
proof: formalized
---

# lv1-lv2-identities

We have

$$
\begin{aligned}
E_4 &= \frac{1}{2}(H_{2}^{2} + H_{3}^{2} + H_{4}^{2}) = H_{2}^{2} + H_{2}H_{4} + H_{4}^{2}\qquad\text{(30)}\\
E_6 &= \frac{1}{2} (H_{2} + H_{3})(H_{3} + H_{4}) (H_{4} - H_{2}) = \frac{1}{2}(H_2 + 2H_4)(2H_2 + H_4)(H_4 - H_2)\qquad\text{(31)}\\
\Delta &= \frac{1}{256} (H_{2}H_{3}H_{4})^2.\qquad\text{(32)}\end{aligned}
$$

## Depends on

- [theta-transform-S-T](../part-02/lemma-theta-transform-s-t.md)
- [theta-modular](../part-02/lemma-theta-modular.md)
- [disc-cuspform](../part-02/lemma-disc-cuspform.md)

## Proof

We can prove these similarly as Lemma [jacobi-identity](../part-02/lemma-jacobi-identity.md). Right hand sides of (30), (31), and (32) are all modular forms of level $\Gamma_1$ and desired weights, where (32) is a cusp form since $H_2$ is. Now the identities follow from the dimension calculations $\dim M_4(\Gamma_1) = \dim M_6(\Gamma_1) = \dim S_{12}(\Gamma_1) = 1$ and comparing the first nonzero $q$-coefficients.

## Lean

Formalized as [`SpherePacking.ModularForms.E₄_eq_thetaE4`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.ModularForms.E₄_eq_thetaE4), [`SpherePacking.ModularForms.E₆_eq_thetaE6`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.ModularForms.E₆_eq_thetaE6), [`Delta_eq_H₂_H₃_H₄`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Delta_eq_H₂_H₃_H₄).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 496](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L496)
