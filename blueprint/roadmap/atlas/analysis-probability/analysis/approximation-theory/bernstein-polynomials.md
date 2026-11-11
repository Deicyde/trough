---
declaration: section
origin: cited
lean: bernstein.mean, bernstein.fourth_moment, bernstein.fourth_moment_le, bernsteinApproximation.tendsto_voronovskaya
statement: formalized
proof: formalized
---

# Bernstein polynomials

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/bernstein-polynomials/index.html).

## Bernstein

## First central moment of the Bernstein weights

For `n ≠ 0`,
`∑ k : Fin (n + 1), (x - k / n) * bernstein n k x = 0`: the binomial frequency `S / n` has
mean `x`.

Formalized by `bernstein.mean`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Bernstein/Voronovskaya.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/Bernstein/Voronovskaya.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/bernstein-polynomials/index.html#mean).

## Fourth central moment of the Bernstein weights

For `n ≠ 0`,
`∑ k : Fin (n + 1), (x - k / n) ^ 4 * bernstein n k x = x (1 - x) (1 + 3 (n - 2) x (1 - x)) / n³`,
i.e. `E[(S - n x) ^ 4] = n x (1 - x) (1 + 3 (n - 2) x (1 - x))` for `S ~ Bin(n, x)`.

Formalized by `bernstein.fourth_moment`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Bernstein/Voronovskaya.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/Bernstein/Voronovskaya.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/bernstein-polynomials/index.html#fourth-moment).

## Fourth central moment bound for Bernstein weights

The fourth central moment of the Bernstein weights is at most `1 / n ^ 2`, uniformly in
`x ∈ [0, 1]`.

Formalized by `bernstein.fourth_moment_le`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Bernstein/Voronovskaya.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/Bernstein/Voronovskaya.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/bernstein-polynomials/index.html#fourth-moment-le).

## Voronovskaya's theorem (1932)

For `f : ℝ → ℝ` of class `C²` and `x ∈ [0, 1]`, the
Bernstein approximations of `f` on `[0, 1]` satisfy
`n · (bernsteinApproximation n f x - f x) → x (1 - x) / 2 · f''(x)` as `n → ∞`.

## Sources

- Voronovskaya (1932); Lorentz, *Bernstein Polynomials* (1953), Chapter 1.

Formalized by `bernsteinApproximation.tendsto_voronovskaya`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Bernstein/Voronovskaya.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/Bernstein/Voronovskaya.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/bernstein-polynomials/index.html#tendsto-voronovskaya).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bernstein polynomials](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/bernstein-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/approximation-theory/bernstein-polynomials)
