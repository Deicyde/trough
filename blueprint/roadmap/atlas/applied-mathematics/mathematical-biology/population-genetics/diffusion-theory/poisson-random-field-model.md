---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Diffusion.prfDensity, MathlibExt.Biology.PopulationGenetics.Diffusion.prfDensity_of_ne_zero, MathlibExt.Biology.PopulationGenetics.Diffusion.prfDensity_zero, MathlibExt.Biology.PopulationGenetics.Diffusion.prfDensity_zero_eq_neutralGreen, MathlibExt.Biology.PopulationGenetics.Diffusion.forward_prfDensity, MathlibExt.Biology.PopulationGenetics.Diffusion.current_prfDensity, MathlibExt.Biology.PopulationGenetics.Diffusion.tendsto_weighted_prfDensity_zero, MathlibExt.Biology.PopulationGenetics.Diffusion.tendsto_weighted_prfDensity_one
statement: formalized
proof: formalized
---

# Poisson random field model

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model/index.html).

## Sawyer–Hartl Poisson random field density

The Sawyer–Hartl (1992) Poisson-random-field density: the expected number of sites per unit
frequency at which the derived allele has frequency `x`, for scaled mutation rate `θ = 4Nu`
and scaled genic selection `σ = 2Ns`:
`θ · u_σ(1 - x) / (x (1 - x))` with `u_σ = kimuraFixation σ`, i.e.
`θ (1 - e^{-2σ(1 - x)}) / ((1 - e^{-2σ}) x (1 - x))`, and `θ / x` when `σ = 0`.
The model domain is `θ > 0` and `x ∈ (0, 1)`; at `x = 0, 1` Lean's `a / 0 = 0` gives the junk
value `0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.prfDensity`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model/index.html#prf-density).

## Closed form of the Poisson random field density with selection

The Poisson-random-field density with selection, explicitly:
`θ (1 - e^{-2σ(1 - x)}) / ((1 - e^{-2σ}) x (1 - x))` for `σ ≠ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.prfDensity_of_ne_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model/index.html#prf-density-of-ne-zero).

## Neutral Poisson random field density

The neutral Poisson-random-field density is `θ / x` (for `x ≠ 1`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.prfDensity_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model/index.html#prf-density-zero).

## The neutral density from the Green's function

A new neutral mutation enters at a
small frequency `p`; with mutations arriving at rate `θ / (2p)` per unit time (so that the
mutational input of frequency is `θ / 2`), the expected sojourn density at `x ≥ p` is
`θ / (2p) · G(p, x) = θ / x`, the neutral Poisson-random-field density.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.prfDensity_zero_eq_neutralGreen`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model/index.html#prf-density-zero-eq-neutral-green).

## Stationary forward equation (Sawyer–Hartl 1992)

On `(0, 1)` the weighted density
`F(x) = x (1 - x) φ(x)` of the Poisson-random-field density solves the stationary
Fokker–Planck equation `½ F'' - σ F' = 0` of the Wright–Fisher diffusion with genic selection
`σ` (the forward equation `½ (x (1 - x) φ)'' - (σ x (1 - x) φ)' = 0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.forward_prfDensity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model/index.html#forward-prf-density).

## Probability current

On `(0, 1)` the current `J = σ F - F' / 2` of the stationary
forward equation, for the weighted density `F(x) = x (1 - x) φ(x)`, is the constant
`θ · u_σ'(0) / 2` (`u_σ'(0) = kimuraSlope σ = 2σ / (1 - e^{-2σ})`, and `1` for `σ = 0`), so
`J = θ σ / (1 - e^{-2σ})`, and `J = θ / 2` in the neutral case: the mutational input of
frequency at `0`, carried through `(0, 1)` to fixation at `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.current_prfDensity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model/index.html#current-prf-density).

## Boundary normalization at `0`

As `x → 0⁺` the weighted density `x (1 - x) φ(x)` tends
to `θ`. (This is not the probability current, which is `current_prfDensity`.)

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.tendsto_weighted_prfDensity_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model/index.html#tendsto-weighted-prf-density-zero).

## Boundary normalization at `1`

As `x → 1⁻` the weighted density `x (1 - x) φ(x)` tends
to `0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.tendsto_weighted_prfDensity_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model/index.html#tendsto-weighted-prf-density-one).

## ODE characterization of the Poisson-random-field density

Let `θ ≠ 0` and let `φ` be
a density on `(0, 1)` whose weighted density `x (1 - x) φ(x)` extends to a function `F`
continuous on `[0, 1]`, twice differentiable on `(0, 1)`, solving the stationary forward
equation `½ F'' - σ F' = 0` there, with boundary normalizations `F(0) = θ` and `F(1) = 0`.
Then `φ` is the Sawyer–Hartl density on `(0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.eq_prfDensity_of_forward`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model/index.html#eq-prf-density-of-forward).

## Expected site frequency spectrum under the Poisson random field

The expected unfolded site-frequency spectrum of a sample of `n` gene copies under the
Poisson random field: the expected number of sites where exactly `i` of the `n` sampled copies
carry the derived allele, `E ξ_i = ∫ x in 0..1, C(n, i) x ^ i (1 - x) ^ (n - i) φ(x)`.
The site-frequency spectrum consists of the segregating classes `1 ≤ i < n`. The value at
`i = n` is the expected number of sites at which every sampled copy is derived (monomorphic in
the sample, `expectedSFS_neutral_self`); for `i = 0` the integrand is not integrable at `0` (the
expected number of ancestral-monomorphic sites is infinite) and Lean's integral returns its junk
value `0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.expectedSFS`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model/index.html#expected-sfs).

## Neutral site-frequency spectrum (Fu 1995)

With `σ = 0`, for the segregating classes
`1 ≤ i < n` the expected number of sites with `i` derived copies in a sample of `n` is
`θ / i`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.expectedSFS_neutral`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model/index.html#expected-sfs-neutral).

## Expected number of sites derived in the whole neutral sample

With `σ = 0` the expected number of sites at which all `n ≥ 1` sampled copies carry the
derived allele is `θ / n`. These sites are monomorphic in the sample, so this is not a class of
the site-frequency spectrum.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.expectedSFS_neutral_self`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/PoissonRandomField.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model/index.html#expected-sfs-neutral-self).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Poisson random field model](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-genetics/diffusion-theory/poisson-random-field-model)
