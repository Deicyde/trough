---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.LotkaVolterra.firstIntegral, MathlibExt.Biology.Dynamics.LotkaVolterra.hasDerivAt_firstIntegral, MathlibExt.Biology.Dynamics.LotkaVolterra.firstIntegral_eq, MathlibExt.Biology.Dynamics.LotkaVolterra.firstIntegral_equilibrium_le
statement: formalized
proof: formalized
---

# Lotka–Volterra predator–prey model

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/lotka-volterra-predator-prey-model/index.html).

## First integral of the Lotka–Volterra system

The Lotka–Volterra first integral `V(x, y) = δ x - γ log x + β y - α log y` for the
system `x' = α x - β x y`, `y' = δ x y - γ y`. It is meaningful on the open positive quadrant
`x, y > 0`; elsewhere `Real.log` takes junk values (`log 0 = 0`, `log (-x) = log x`).

Formalized by `MathlibExt.Biology.Dynamics.LotkaVolterra.firstIntegral`, a definition declared in [MathlibExt/Biology/Dynamics/LotkaVolterra.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/LotkaVolterra.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/lotka-volterra-predator-prey-model/index.html#first-integral).

## Lotka–Volterra first integral

If `x' = α x - β x y` and `y' = δ x y - γ y` at time `t`
and `x t, y t > 0`, then `t ↦ V(x t, y t)` has derivative `0` at `t`.

Formalized by `MathlibExt.Biology.Dynamics.LotkaVolterra.hasDerivAt_firstIntegral`, a theorem declared in [MathlibExt/Biology/Dynamics/LotkaVolterra.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/LotkaVolterra.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/lotka-volterra-predator-prey-model/index.html#has-deriv-at-first-integral).

## Positive solutions lie on level curves

If `(x, y)` solves the Lotka–Volterra system
on `[0, ∞)` and both populations stay positive there, then `V(x t, y t) = V(x 0, y 0)` for
all `t ≥ 0`.

Formalized by `MathlibExt.Biology.Dynamics.LotkaVolterra.firstIntegral_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/LotkaVolterra.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/LotkaVolterra.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/lotka-volterra-predator-prey-model/index.html#first-integral-eq).

## The coexistence equilibrium minimizes the first integral

For positive parameters and
`x, y > 0`, `V(γ / δ, α / β) ≤ V(x, y)`.

Formalized by `MathlibExt.Biology.Dynamics.LotkaVolterra.firstIntegral_equilibrium_le`, a theorem declared in [MathlibExt/Biology/Dynamics/LotkaVolterra.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/LotkaVolterra.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/lotka-volterra-predator-prey-model/index.html#first-integral-equilibrium-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lotka–Volterra predator–prey model](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/lotka-volterra-predator-prey-model/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-dynamics/lotka-volterra-predator-prey-model)
