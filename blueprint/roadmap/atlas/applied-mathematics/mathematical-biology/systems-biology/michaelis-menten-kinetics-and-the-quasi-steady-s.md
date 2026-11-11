---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.MichaelisMenten.michaelisConstant, MathlibExt.Biology.Dynamics.MichaelisMenten.substrateRate, MathlibExt.Biology.Dynamics.MichaelisMenten.complexRate, MathlibExt.Biology.Dynamics.MichaelisMenten.IsSolution, MathlibExt.Biology.Dynamics.MichaelisMenten.IsSolution.enzyme_conservation, MathlibExt.Biology.Dynamics.MichaelisMenten.IsSolution.substrate_conservation, MathlibExt.Biology.Dynamics.MichaelisMenten.qssComplex, MathlibExt.Biology.Dynamics.MichaelisMenten.mmRate
statement: formalized
---

# Michaelis–Menten kinetics and the quasi-steady state

19 results, 18 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html).

## Michaelis constant

The Michaelis constant `K_M = (kb + k₂)/k₁` (Briggs–Haldane). Meaningful for `k₁ > 0`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.michaelisConstant`, a definition declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#michaelis-constant).

## Mass-action rate of the substrate

The mass-action rate of the substrate, `s' = -k₁ e s + kb c`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.substrateRate`, a definition declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#substrate-rate).

## Mass-action rate of the enzyme–substrate complex

The mass-action rate of the complex, `c' = k₁ e s - (kb + k₂) c`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.complexRate`, a definition declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#complex-rate).

## Solution of the Michaelis–Menten mass-action system

A solution of the Michaelis–Menten mass-action system on `[0, ∞)`:
`s' = -k₁ e s + kb c`, `c' = k₁ e s - (kb + k₂) c`, `e' = -c'`, `p' = k₂ c`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.IsSolution`, a structure declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#is-solution).

## Enzyme conservation

`e(t) + c(t) = e(0) + c(0)`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.IsSolution.enzyme_conservation`, a theorem declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#enzyme-conservation).

## Mass conservation

`s(t) + c(t) + p(t) = s(0) + c(0) + p(0)`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.IsSolution.substrate_conservation`, a theorem declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#substrate-conservation).

## Quasi-steady-state value of the complex

The quasi-steady-state value of the complex, `c = e₀ s / (K_M + s)`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.qssComplex`, a definition declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#qss-complex).

## Michaelis–Menten rate law

The Michaelis–Menten rate law `v(s) = V_max s / (K_M + s)`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.mmRate`, a definition declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#mm-rate).

## Quasi-steady-state manifold

With total enzyme `e₀` (so `e = e₀ - c`), `k₁ > 0` and
`K_M + s ≠ 0`, the complex is stationary iff `c = e₀ s / (K_M + s)`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.complexRate_eq_zero_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#complex-rate-eq-zero-iff).

## Briggs–Haldane rate law

On the quasi-steady-state manifold the product forms at rate
`k₂ c = V_max s / (K_M + s)`, `V_max = k₂ e₀`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.productRate_qss`, a theorem declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#product-rate-qss).

## Substrate consumption at the Michaelis–Menten rate under QSSA

On the quasi-steady-state manifold the substrate is consumed at the Michaelis–Menten rate:
`s' = -V_max s / (K_M + s)`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.substrateRate_qss`, a theorem declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#substrate-rate-qss).

## Michaelis–Menten rate is strictly increasing

The rate law is strictly increasing on `s ≥ 0` for `V_max, K_M > 0`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.mmRate_strictMono`, a theorem declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#mm-rate-strict-mono).

## Michaelis constant is the half-saturation substrate level

The Michaelis constant is the half-saturation substrate level: `v(K_M) = V_max / 2`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.mmRate_michaelisConstant`, a theorem declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#mm-rate-michaelis-constant).

## Michaelis–Menten rate stays below its maximum

The rate law is below its maximum: `v(s) < V_max` for `s ≥ 0`, `V_max, K_M > 0`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.mmRate_lt`, a theorem declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#mm-rate-lt).

## Saturation of the Michaelis–Menten rate

Saturation: `v(s) → V_max` as `s → ∞`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.tendsto_mmRate`, a theorem declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#tendsto-mm-rate).

## Fast transient of the complex with frozen substrate

The fast transient of the complex with the substrate frozen at `s̄`:
`c(t) = c* + (c₀ - c*) e^{-k₁ (s̄ + K_M) t}`, where `c* = e₀ s̄ / (K_M + s̄)`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.fastTransient`, a definition declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#fast-transient).

## Fast transient solves the boundary-layer equation

The fast transient solves the boundary-layer equation `c' = k₁ (e₀ - c) s̄ - (kb + k₂) c`
for `k₁ > 0` and `K_M + s̄ ≠ 0`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.hasDerivAt_fastTransient`, a theorem declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#has-deriv-at-fast-transient).

## Fast transient converges to the quasi-steady state

The fast transient converges to the quasi-steady-state value for `k₁ > 0` and
`s̄ + K_M > 0`.

Formalized by `MathlibExt.Biology.Dynamics.MichaelisMenten.tendsto_fastTransient`, a theorem declared in [MathlibExt/Biology/Dynamics/MichaelisMenten.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MichaelisMenten.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#tendsto-fast-transient).

## Rigorous QSSA

**Rigorous QSSA** (Tikhonov 1952; Heineken–Tsuchiya–Aris 1967). On the slow time scale
`τ = e₀ t`, the substrate of the full Michaelis–Menten system with `s(0) = s₀`, `c(0) = 0`,
`e(0) = e₀` stays within `C e₀` of the solution `S̄` of the reduced equation
`dS̄/dτ = -k₂ S̄ / (K_M + S̄)`, `S̄(0) = s₀`, uniformly on `[0, T]`.

Stated but not proved: `MathlibExt.Biology.Dynamics.MichaelisMenten.abs_sub_reduced_le` is written with `theorem_wanted` in [WantedExt/Biology/Dynamics/MichaelisMentenQSSAWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Biology/Dynamics/MichaelisMentenQSSAWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html#abs-sub-reduced-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Michaelis–Menten kinetics and the quasi-steady state](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/systems-biology/michaelis-menten-kinetics-and-the-quasi-steady-s)
