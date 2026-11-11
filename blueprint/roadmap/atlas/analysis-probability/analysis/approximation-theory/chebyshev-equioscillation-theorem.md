---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Approximation.Equioscillation.Equioscillates, MathlibExt.Analysis.Approximation.Equioscillation.eq_of_equioscillates, MathlibExt.Analysis.Approximation.Equioscillation.not_lt_of_equioscillates, MathlibExt.Analysis.Approximation.Equioscillation.de_la_vallee_poussin
statement: formalized
proof: formalized
---

# Chebyshev equioscillation theorem

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/chebyshev-equioscillation-theorem/index.html).

## Equioscillation of a polynomial approximation

A polynomial `p` of degree at most `n` equioscillates against `f` on `[a, b]`
with amplitude `E` and sign `σ = ±1` at the `n + 2` points `x 0 < ⋯ < x (n+1)`,
if `f (x i) - p (x i) = σ * (-1) ^ i * E` for every `i ≤ n + 1`, and
`|f y - p.eval y| ≤ E` for every `y ∈ [a, b]`.

Formalized by `MathlibExt.Analysis.Approximation.Equioscillation.Equioscillates`, a definition declared in [MathlibExt/Analysis/Approximation/Equioscillation.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Approximation/Equioscillation.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/chebyshev-equioscillation-theorem/index.html#equioscillates).

## Uniqueness of the equioscillating best approximation

If `p` equioscillates against `f` on `[a, b]`, then `p` is the unique
polynomial of degree at most `n` whose uniform error on `[a, b]` is at most `E`.
In particular `p` is the unique best uniform approximation to `f` among
polynomials of degree at most `n`.

Formalized by `MathlibExt.Analysis.Approximation.Equioscillation.eq_of_equioscillates`, a theorem declared in [MathlibExt/Analysis/Approximation/Equioscillation.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Approximation/Equioscillation.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/chebyshev-equioscillation-theorem/index.html#eq-of-equioscillates).

## Chebyshev equioscillation theorem (sufficiency)

If `p` equioscillates against `f`, then no polynomial of degree at most `n`
has uniform error strictly less than `E` on `[a, b]`: `p` is a best uniform
approximation.

Formalized by `MathlibExt.Analysis.Approximation.Equioscillation.not_lt_of_equioscillates`, a theorem declared in [MathlibExt/Analysis/Approximation/Equioscillation.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Approximation/Equioscillation.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/chebyshev-equioscillation-theorem/index.html#not-lt-of-equioscillates).

## De la Vallée Poussin's theorem

If the error `f - p` of a polynomial
`p` of degree at most `n` alternates with a one-sided lower bound `η` at
`n + 2` strictly increasing points of `[a, b]`,
`η ≤ σ * (-1) ^ i * (f (x i) - p (x i))`, then every polynomial of degree at
most `n` has uniform error at least `η` on `[a, b]`.

Formalized by `MathlibExt.Analysis.Approximation.Equioscillation.de_la_vallee_poussin`, a theorem declared in [MathlibExt/Analysis/Approximation/Equioscillation.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Approximation/Equioscillation.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/chebyshev-equioscillation-theorem/index.html#de-la-vallee-poussin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chebyshev equioscillation theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/chebyshev-equioscillation-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/approximation-theory/chebyshev-equioscillation-theorem)
