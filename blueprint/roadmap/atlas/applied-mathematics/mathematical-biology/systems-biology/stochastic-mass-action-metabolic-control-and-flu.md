---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.SystemsBiology.propensity, MathlibExt.Biology.Dynamics.SystemsBiology.fire, MathlibExt.Biology.Dynamics.SystemsBiology.unfire, MathlibExt.Biology.Dynamics.SystemsBiology.poissonWeight, MathlibExt.Biology.Dynamics.SystemsBiology.classGenerator, MathlibExt.Biology.Dynamics.SystemsBiology.poissonWeight_mul_sum_propensity, MathlibExt.Biology.Dynamics.SystemsBiology.isRateMatrix_classGenerator, MathlibExt.Biology.Dynamics.SystemsBiology.poissonWeight_vecMul_classGenerator
statement: formalized
proof: formalized
---

# Stochastic mass action, metabolic control and flux balance

45 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html).

## Stochastic mass-action propensity

The stochastic mass-action propensity of reaction `r` in state `x` (molecule counts):
`k r * ∏_s x_s (x_s - 1) ⋯ (x_s - src_s + 1)`, the falling factorial
`Nat.descFactorial x_s src_s` (it vanishes when `x_s < src_s`). Anderson, Craciun & Kurtz
(2010), §2.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.propensity`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#propensity).

## State after one reaction firing

The state reached from `x` by one firing of reaction `r`, `x - src r + prod r`
(meaningful when `src r ≤ x`, the only case in which the propensity is nonzero).

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.fire`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#fire).

## State before one reaction firing

The state from which one firing of reaction `r` leads to `x`, `x - prod r + src r`
(meaningful when `prod r ≤ x`).

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.unfire`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#unfire).

## Product-form Poisson weight of a state

The product-form Poisson weight `∏_s c_s ^ x_s e^{-c_s} / Nat.factorial x_s` of a
state `x`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.poissonWeight`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#poisson-weight).

## Generator of the mass-action chain on a finite state class

The generator of the stochastic mass-action chain restricted to a finite set `Ω` of
states: `Q x y = ∑_r λ_r(x) ([fire r x = y] - [x = y])`. It is a rate matrix when `Ω` is
closed under firing (`isRateMatrix_classGenerator`).

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.classGenerator`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#class-generator).

## Global balance of the product-form Poisson weights

**Global balance of the product-form Poisson weights** (Anderson, Craciun & Kurtz 2010,
Thm 4.1): if `c` is complex balanced for the deterministic mass-action system with rate
constants `k`, then at every state `x` the total outflow `π(x) ∑_r λ_r(x)` equals the total
inflow `∑_{r : prod r ≤ x} π(x - prod r + src r) λ_r(x - prod r + src r)` for
`π = poissonWeight c`. This is an algebraic identity valid for all real `k` and `c`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.poissonWeight_mul_sum_propensity`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#poisson-weight-mul-sum-propensity).

## Restricted mass-action generator is a rate matrix

The restricted generator is a rate matrix when the rate constants are nonnegative and
`Ω` is closed under the reactions.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.isRateMatrix_classGenerator`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#is-rate-matrix-class-generator).

## Anderson–Craciun–Kurtz on a finite class

**Anderson–Craciun–Kurtz on a finite class** (Anderson, Craciun & Kurtz 2010,
Thm 4.1–4.2): if `c` is complex balanced and every state of `Ω` from which a reaction leads
into `Ω` lies in `Ω` (`hbwd`), the Poisson weights restricted to `Ω` are invariant for the
restricted generator: `π Q = 0`, for all real `k` and `c`. For a closed communicating class of
a weakly reversible network with positive rate constants `hbwd` holds (the reverse reaction
path leads back).

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.poissonWeight_vecMul_classGenerator`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#poisson-weight-vec-mul-class-generator).

## Normalized Poisson stationary law on a finite state class

The Poisson weights normalized on a finite set `Ω` of states.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.classStationaryLaw`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#class-stationary-law).

## Stationary law of the stochastic mass-action chain on a finite class

**Stationary law of the stochastic mass-action chain on a finite class** (Anderson,
Craciun & Kurtz 2010, Thm 4.1–4.2). Let the rate constants be nonnegative, `c > 0` complex
balanced, and `Ω` a nonempty finite set of states closed under the reactions in both
directions. Then the restricted generator is a rate matrix, and the normalized product-form
Poisson law `π(x) ∝ ∏_s c_s^{x_s} e^{-c_s} / Nat.factorial x_s` on `Ω` is a positive
probability vector invariant under the transition semigroup: `π P(t) = π` for every `t`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.classStationaryLaw_spec`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#class-stationary-law-spec).

## Reaction fluxes proportional to enzyme levels

Reaction rates `v_i(e, s) = e_i f_i(s)` proportional to enzyme levels `e`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.flux`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#flux).

## Steady-state fluxes along a steady-state map

The steady-state fluxes `J(e) = v(e, σ(e))` along a steady-state map `σ`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.steadyFlux`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#steady-flux).

## Flux control coefficient

The flux control coefficient `C^{J_j}_{e_i} = (e_i / J_j) ∂J_j/∂e_i`. It is meaningful
when `J_j ≠ 0` and the steady-state flux is differentiable at `e`; otherwise Lean's `x / 0 = 0`
and `fderiv` of a non-differentiable map, `0`, give junk values.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.fluxControl`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#flux-control).

## Concentration control coefficient

The concentration control coefficient `C^{s_m}_{e_i} = (e_i / s_m) ∂s_m/∂e_i`, meaningful
for a positive concentration `s_m` and a steady state differentiable at `e`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.concControl`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#conc-control).

## Elasticity of a reaction rate

The elasticity `ε^{v_i}_{s_m} = (s_m / v_i) ∂v_i/∂s_m`, meaningful for a nonzero rate
`v_i` and a rate law differentiable at `s`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.elasticity`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#elasticity).

## Regular steady state of a metabolic network

A regular steady state at enzyme levels `e₀`: `σ` is differentiable at `e₀`, the rate
laws are differentiable at `σ e₀`, `N v(e, σ e) = 0` for `e` near `e₀`, and the Jacobian
`δ ↦ N ∂_s v(e₀, σ e₀) δ` is injective (it is square, so this is its invertibility).

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.IsRegularSteadyState`, a structure declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#is-regular-steady-state).

## Regular steady states exist by the implicit function theorem

If `s₀` is a steady state
at enzyme levels `e₀`, the rate laws are continuously differentiable at `s₀`, and the Jacobian
`δ ↦ N (e₀ ⊙ f'(s₀) δ)` is injective, then the steady state continues to a map `σ` with
`σ e₀ = s₀` satisfying `IsRegularSteadyState`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.exists_isRegularSteadyState`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#exists-is-regular-steady-state).

## Concentration summation theorem

**Concentration summation theorem** (Heinrich & Rapoport 1974): for a positive
steady-state concentration `s_m`, `∑_i C^{s_m}_{e_i} = 0`. The positivity hypothesis is the
domain on which the scaled concentration control coefficients have their biological meaning.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.sum_concControl`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 576](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L576). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#sum-conc-control).

## Flux summation theorem

**Flux summation theorem** (Kacser & Burns 1973; Heinrich & Rapoport 1974): for a
nonzero steady-state flux `J_j`, `∑_i C^{J_j}_{e_i} = 1`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.sum_fluxControl`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 594](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L594). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#sum-flux-control).

## Flux connectivity theorem

**Flux connectivity theorem** (Kacser & Burns 1973): when all steady-state fluxes are
nonzero, `∑_i C^{J_j}_{e_i} ε^{v_i}_{s_m} = 0` for every flux `J_j` and metabolite `s_m`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.sum_fluxControl_mul_elasticity`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 613](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L613). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#sum-flux-control-mul-elasticity).

## Feasible fluxes of flux balance analysis

The feasible fluxes of flux balance analysis: `S v = b`, `l ≤ v ≤ u`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.fbaFeasible`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 667](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L667). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#fba-feasible).

## Optimal value of flux balance analysis

The optimal value `max {c ⬝ᵥ v | S v = b, l ≤ v ≤ u}` of flux balance analysis
(the supremum; it is `0` by convention when the problem is infeasible).

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.fbaValue`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 673](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L673). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#fba-value).

## Dual feasibility for flux balance analysis

Dual feasibility for flux balance analysis: `y` prices the metabolites, `α, β ≥ 0` the
upper and lower flux bounds, and `Sᵀ y + α - β = c`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.fbaDualFeasible`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 679](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#fba-dual-feasible).

## Dual objective of flux balance analysis

The dual objective `b ⬝ᵥ y + u ⬝ᵥ α - l ⬝ᵥ β`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.fbaDualValue`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 684](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L684). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#fba-dual-value).

## Feasible flux balance problem attains its optimum

A feasible flux balance problem attains its optimum.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.exists_fbaValue_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 710](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L710). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#exists-fba-value-eq).

## Weak duality for flux balance analysis

Weak duality for flux balance analysis.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.dotProduct_le_fbaDualValue`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 722](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L722). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#dot-product-le-fba-dual-value).

## Strong duality for flux balance analysis

Strong duality for flux balance analysis: a feasible problem has a dual feasible point
whose value is the optimal value.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.exists_fbaDualValue_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 791](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L791). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#exists-fba-dual-value-eq).

## Concavity of the flux balance optimum in the right-hand side

The optimal value is concave in the right-hand side `b` on the set of feasible `b`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.fbaValue_concave`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 860](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L860). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#fba-value-concave).

## Shadow prices

**Shadow prices** (Orth, Thiele & Palsson 2010): at a feasible `b`, the metabolite prices
`y` of the optimal dual solutions are exactly the supergradients of the optimal value:
`fbaValue b' ≤ fbaValue b + y ⬝ᵥ (b' - b)` for every feasible `b'`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.exists_optimal_dual_iff_supergradient`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 885](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L885). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#exists-optimal-dual-iff-supergradient).

## Uniqueness of Sinkhorn scaling

Two diagonal scalings of a positive matrix to doubly
stochastic form differ by a positive scalar.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.sinkhorn_scaling_unique`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 993](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L993). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#sinkhorn-scaling-unique).

## Symmetric matrix balancing

**Symmetric matrix balancing** (Sinkhorn 1964; the "equal visibility" normalization of
Imakaev et al. 2012): a symmetric matrix with positive entries has a unique positive vector
`d` with `diag(d) A diag(d)` doubly stochastic.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.existsUnique_symmetric_balancing`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 1029](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L1029). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#exists-unique-symmetric-balancing).

## Total support of a square matrix

A square matrix has **total support** if it is nonzero and every positive entry lies on a
positive diagonal: for `A i j > 0` there is a permutation `σ` with `σ i = j` and
`A k (σ k) > 0` for all `k` (Sinkhorn & Knopp 1967; Csima & Datta 1972).

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.HasTotalSupport`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 1078](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L1078). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#has-total-support).

## Necessity of total support

**Necessity of total support** (Sinkhorn & Knopp 1967; Csima & Datta 1972): if a positive
diagonal scaling `diag(d) A diag(d)` is doubly stochastic, then `A` has total support. The proof
uses Birkhoff's theorem. The converse for symmetric nonnegative `A` is
`exists_symmetric_balancing_of_hasTotalSupport`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.hasTotalSupport_of_balancing`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 1092](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L1092). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#has-total-support-of-balancing).

## Interaction graph of a Boolean network

In the interaction graph of `f : {0,1}ⁿ → {0,1}ⁿ` there is an edge `j → i` when the
`i`-th coordinate of `f` depends on the `j`-th variable.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.Influences`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 1138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L1138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#influences).

## Acyclic interaction graph

The interaction graph of `f` has no directed cycle (loops included).

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.IsAcyclic`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 1142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L1142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#is-acyclic).

## Robert's theorem

**Robert's theorem** (Robert 1980): if the interaction graph of `f : {0,1}ⁿ → {0,1}ⁿ`
is acyclic, `f` has a unique fixed point `p`, and every synchronous trajectory reaches it
within `n` steps.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.robert_fixed_point`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 1245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L1245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#robert-fixed-point).

## Spanning in-tree rooted at a state

`t : ι → ι` is a spanning in-tree rooted at `r` (each `i ≠ r` points to its parent
`t i`): `t r = r` and iterating `t` from any state reaches `r`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.IsInTree`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 1265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L1265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#is-in-tree).

## Total weight of spanning in-trees

The total weight `∑_t ∏_{i ≠ r} Q i (t i)` of the spanning in-trees rooted at `r`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.treeWeight`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 1269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L1269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#tree-weight).

## Irreducible rate matrix

A rate matrix is irreducible if every state reaches every other state through positive
jump rates.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.IsIrreducible`, a definition declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 1275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L1275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#is-irreducible).

## Markov chain tree theorem

**Markov chain tree theorem** (King & Altman 1956; Hill 1966): the in-tree weights are
invariant for every matrix with zero row sums, `w Q = 0`. The proof matches both sides with the
maps `g : ι → ι` whose functional graph has its cycle through `j` (Anantharam & Tsoucas 1989).

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.treeWeight_vecMul_eq_zero`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 1436](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L1436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#tree-weight-vec-mul-eq-zero).

## In-tree weights of an irreducible rate matrix are positive

For an irreducible rate matrix every in-tree weight is positive.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.treeWeight_pos`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 1507](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L1507). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#tree-weight-pos).

## Uniqueness in the Markov chain tree theorem

For an irreducible rate matrix every invariant vector is a multiple of the in-tree weights:
the stationary law is proportional, at each state, to the weight of the spanning in-trees
rooted there.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.eq_smul_treeWeight_of_vecMul_eq_zero`, a theorem declared in [MathlibExt/Biology/Dynamics/SystemsBiology.lean, line 1563](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/SystemsBiology.lean#L1563). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#eq-smul-tree-weight-of-vec-mul-eq-zero).

## Finitely many dual solutions suffice

There is a finite set `T` of pairs
`(y, u ⬝ᵥ α - l ⬝ᵥ β)` with `(y, α, β)` dual feasible, such that for every feasible `b` some
pair in `T` is optimal: `y ⬝ᵥ b + κ = fbaValue S l u c b`.

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.exists_finset_optimal_fbaDual`, a theorem declared in [MathlibExt/Biology/Dynamics/FluxBalanceValue.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/FluxBalanceValue.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#exists-finset-optimal-fba-dual).

## The FBA value is piecewise linear

There are finitely many affine functions
`b ↦ y ⬝ᵥ b + κ` whose minimum is the optimal value at every feasible right-hand side `b`.

## Sources

- Rockafellar (1970), Thm 19.3; Orth, Thiele & Palsson (2010).

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.exists_finset_isLeast_fbaValue`, a theorem declared in [MathlibExt/Biology/Dynamics/FluxBalanceValue.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/FluxBalanceValue.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#exists-finset-is-least-fba-value).

## Shadow prices are derivatives when unique

If `b` is an interior point of the set of
feasible right-hand sides and `y` is the only metabolite price vector of an optimal dual
solution, then the optimal value is differentiable at `b` with derivative `b' ↦ y ⬝ᵥ b'`.

## Sources

- Rockafellar (1970), Thm 25.1; Orth, Thiele & Palsson (2010).

Formalized by `MathlibExt.Biology.Dynamics.SystemsBiology.hasFDerivAt_fbaValue_of_unique`, a theorem declared in [MathlibExt/Biology/Dynamics/FluxBalanceValue.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/FluxBalanceValue.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html#has-fderiv-at-fba-value-of-unique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stochastic mass action, metabolic control and flux balance](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/systems-biology/stochastic-mass-action-metabolic-control-and-flu)
