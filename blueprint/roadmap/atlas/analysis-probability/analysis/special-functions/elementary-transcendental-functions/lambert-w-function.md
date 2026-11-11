---
declaration: section
origin: cited
lean: MetaMathlibExt.lambertMap, MetaMathlibExt.existsUnique_lambertMap_preimage, MetaMathlibExt.existsUnique_lambertMap_lower_preimage
statement: formalized
proof: formalized
---

# Lambert W function

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/lambert-w-function/index.html).

## Lambert map

The Lambert map is the function $h(y) = y e^y$ of a real variable $y$.

The inverse of $h$ restricted to $y > -1$ is the principal real branch of the Lambert W function.

## Sources

- Ouellet JIS VOL20 `ou2.tex` lines 426-432.

Formalized by `MetaMathlibExt.lambertMap`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/LambertWFunction.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/LambertWFunction.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/lambert-w-function/index.html#lambert-map).

## Principal-branch preimages of the Lambert map

Let $h(y) = y e^y$ be the Lambert map on
the real numbers. Every real $x > -e^{-1}$ has exactly one preimage $y > -1$ under $h$, that is,
there is exactly one real number $y > -1$ with $y e^y = x$.

Formalized by `MetaMathlibExt.existsUnique_lambertMap_preimage`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/LambertWFunction.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/LambertWFunction.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/lambert-w-function/index.html#exists-unique-lambert-map-preimage).

## Lower-branch preimages of the Lambert map

Let $h(y) = y e^y$ be the Lambert map on the
real numbers. Every real $x$ with $-e^{-1} \le x < 0$ has exactly one preimage $y \le -1$ under
$h$, that is, there is exactly one real number $y \le -1$ with $y e^y = x$.

This preimage is the value at $x$ of the lower real branch $W_{-1}$ of the Lambert W function.
Existence uses $h(-1) = -e^{-1}$, $h(y) \to 0$ as $y \to -\infty$ and the intermediate value
theorem; uniqueness uses $h'(y) = e^y (1 + y) < 0$ for $y < -1$.

## Sources

- Petojević, Gorjanac Ranitović, Rastovac and Mandić, *The Golden Ratio, Factorials, and the Lambert W Function*, Journal of Integer Sequences 27 (2024), Article 24.5.7, Section 3.1 (the lower branch `W₋₁`).

Formalized by `MetaMathlibExt.existsUnique_lambertMap_lower_preimage`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/LambertWFunction.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/LambertWFunction.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/lambert-w-function/index.html#exists-unique-lambert-map-lower-preimage).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lambert W function](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/lambert-w-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/special-functions/elementary-transcendental-functions/lambert-w-function)
