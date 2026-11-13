---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ODE.FiniteElement1D.width, MathlibExt.Analysis.ODE.FiniteElement1D.elementSlope, MathlibExt.Analysis.ODE.FiniteElement1D.ramp, MathlibExt.Analysis.ODE.FiniteElement1D.p1, MathlibExt.Analysis.ODE.FiniteElement1D.hat, MathlibExt.Analysis.ODE.FiniteElement1D.interp, MathlibExt.Analysis.ODE.FiniteElement1D.p1Map, MathlibExt.Analysis.ODE.FiniteElement1D.dirichletNodal
statement: formalized
proof: formalized
---

# Finite element method in one dimension

46 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html).

## Length of a mesh element

The length `hᵢ = xᵢ₊₁ - xᵢ` of the `i`-th element of the mesh.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.width`, a definition declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#width).

## Slope of a P1 function on a mesh element

The slope `(dᵢ₊₁ - dᵢ) / hᵢ` on the `i`-th element of the P1 function with
nodal values `d`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.elementSlope`, a definition declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#element-slope).

## Clamped ramp function of a mesh element

The clamped ramp of the `i`-th element: `0` left of `xᵢ`, `x - xᵢ` on
`[xᵢ, xᵢ₊₁]`, and `hᵢ` right of `xᵢ₊₁`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.ramp`, a definition declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#ramp).

## Continuous piecewise linear function with given nodal values

The continuous piecewise linear (P1) function with nodal values `d`:
`d₀ + ∑ᵢ slopeᵢ · rampᵢ(x)`. On `[0, 1]` it is linear on each element and
takes the value `dⱼ` at `xⱼ`; outside `[0, 1]` it is constant.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.p1`, a definition declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#p1).

## Hat function of a mesh node

The hat function `φⱼ` of node `j`: the P1 function equal to `1` at `xⱼ`
and `0` at every other node.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.hat`, a definition declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#hat).

## Nodal interpolant of a function

The nodal interpolant `I_h u`: the P1 function with nodal values
`u(xⱼ)`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.interp`, a definition declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#interp).

## Linear map from nodal values to P1 functions

`p1` as a linear map from nodal values to functions.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.p1Map`, a definition declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#p1-map).

## Nodal vectors with zero boundary values

Nodal vectors with zero boundary values `d₀ = dₙ = 0`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.dirichletNodal`, a definition declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#dirichlet-nodal).

## P1 finite element space with zero boundary values

The P1 finite element space `V_h` with zero boundary values: the image under
`p1Map` of the nodal vectors vanishing at both ends.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.p1Space`, a definition declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#p1-space).

## Energy form of the equation $-u'' = f$

The energy form `a(u, v) = ∫₀¹ u'(x) v'(x) dx` of `-u'' = f`. For a P1
function, `deriv` is junk at the mesh nodes, a null set.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.energy`, a definition declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#energy).

## Element vector of the stiffness assembly

The `i`-th element vector `eᵢ = δ_{i+1} - δᵢ` of the assembly.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.elementVector`, a definition declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#element-vector).

## Assembled stiffness matrix of the P1 method

The assembled stiffness matrix `K = ∑ᵢ (1 / hᵢ) eᵢ eᵢᵀ` on all nodes:
each element contributes `(1 / hᵢ) [[1, -1], [-1, 1]]` at nodes `i, i + 1`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.stiffness`, a definition declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#stiffness).

## Load vector of the P1 method

The load vector `Fⱼ = ∫₀¹ f φⱼ`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.load`, a definition declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#load).

## Classical solution of the Dirichlet problem $-u'' = f$

`u` is a classical solution of `-u'' = f` on `(0, 1)` with
`u(0) = u(1) = 0`. We ask `u` to be `C²` on all of `ℝ`, which is no loss for
the interval problem (a `C²` function on `[0, 1]` extends), and `f` to be continuous.
The equation is stated on the open interval, as in the Dirichlet problem: requiring it
at the endpoints without regularity of `f` would be a genuine strengthening. With `f`
continuous, endpoint equality follows by continuity (`eq_Icc`), and the integral proofs
use that derived version.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.IsClassicalSolution`, a structure declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#is-classical-solution).

## Classical solutions satisfy the equation on the closed interval

Endpoint equality, derived from the open-interval equation by continuity of
`-u''` and `f`: the two sides agree on `(0, 1)`, hence on its closure `[0, 1]`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.IsClassicalSolution.eq_Icc`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#eq-icc).

## Solution of the Galerkin system

The coefficient vector `c` solves the Galerkin system: zero boundary
values and `(K c)ⱼ = Fⱼ` at every interior node `j`. The Galerkin solution is
`u_h = p1 P c`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.IsGalerkinSolution`, a definition declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#is-galerkin-solution).

## Mesh elements have positive length

Every element has positive length.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.width_pos`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#width-pos).

## Element lengths are bounded by the mesh size

Every element length is at most the mesh size `h`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.width_le_mesh`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#width-le-mesh).

## P1 functions are linear on each element

On the `i`-th element, `p1 P d` is the linear function through
`(xᵢ, dᵢ)` with slope `slopeᵢ = elementSlope P d i`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.p1_eq_of_mem_Icc`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#p1-eq-of-mem-icc).

## P1 functions interpolate their nodal values

`p1 P d` interpolates the nodal values.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.p1_points`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#p1-points).

## Continuity of P1 functions

P1 functions are continuous.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.continuous_p1`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#continuous-p1).

## Derivative of a P1 function inside an element

Inside an element, `p1 P d` has derivative `slopeᵢ`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.hasDerivAt_p1`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#has-deriv-at-p1).

## Integral over the unit interval as a sum over elements

An integral over `[0, 1]` is the sum of the integrals over the elements.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.integral_eq_sum`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#integral-eq-sum).

## Energy pairing with a P1 function via nodal differences

The key identity of the 1D P1 method: for `w` continuous on each element,
differentiable inside it, and with integrable derivative there,
`a(w, p1 d) = ∑ᵢ slopeᵢ(d) (w(xᵢ₊₁) - w(xᵢ))`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.energy_p1`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#energy-p1).

## Characterization of membership in the P1 space

Membership in the P1 space: `v = p1 P d` for nodal values `d` with
`d₀ = dₙ = 0`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.mem_p1Space`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#mem-p1-space).

## Interior hat functions lie in the P1 space

The hat function of an interior node lies in the P1 space.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.hat_mem_p1Space`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#hat-mem-p1-space).

## Weak form of the classical solution for $C^1$ test functions

The weak form for `C¹` test functions vanishing at `0` and `1`:
`∫₀¹ u' v' = ∫₀¹ f v`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.energy_eq_integral_mul_of_contDiff`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#energy-eq-integral-mul-of-cont-diff).

## Weak form of the classical solution for P1 test functions

The weak form for P1 test functions: `∫₀¹ u' v_h' = ∫₀¹ f v_h`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.energy_eq_integral_mul_of_mem_p1Space`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#energy-eq-integral-mul-of-mem-p1-space).

## Energy form of two P1 functions

The energy form of two P1 functions:
`a(p1 c, p1 d) = ∑ᵢ (cᵢ₊₁ - cᵢ)(dᵢ₊₁ - dᵢ) / hᵢ`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.energy_p1_p1`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 525](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L525). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#energy-p1-p1).

## Quadratic form of the stiffness matrix

The quadratic form of the stiffness matrix:
`dᵀ K c = ∑ᵢ (cᵢ₊₁ - cᵢ)(dᵢ₊₁ - dᵢ) / hᵢ`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.dotProduct_stiffness_mulVec`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 543](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L543). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#dot-product-stiffness-mul-vec).

## Stiffness matrix is the Gram matrix of the hat functions

The stiffness matrix is the Gram matrix of the hat functions:
`a(φⱼ, φₖ) = Kⱼₖ`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.energy_hat_hat`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 571](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L571). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#energy-hat-hat).

## Off-diagonal stiffness entry of an element

The off-diagonal entry of an element: `K_{i, i+1} = -1 / hᵢ`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.stiffness_castSucc_succ`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#stiffness-cast-succ-succ).

## Diagonal stiffness entry at an interior node

The diagonal entry at an interior node `xⱼ` shared by consecutive
elements `i` and `j`: `K = 1 / hᵢ + 1 / hⱼ`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.stiffness_succ_succ`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 592](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L592). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#stiffness-succ-succ).

## Tridiagonality of the stiffness matrix

Entries between nodes two or more apart vanish (tridiagonality).

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.stiffness_eq_zero`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 608](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L608). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#stiffness-eq-zero).

## Nodal values of the exact solution solve the Galerkin system

The nodal values of the exact solution solve the Galerkin system.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.isGalerkinSolution_nodal`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 684](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L684). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#is-galerkin-solution-nodal).

## Uniqueness of the Galerkin solution

The Galerkin system has at most one solution (`K` is positive definite on
nodal vectors with zero boundary values).

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.isGalerkinSolution_unique`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#is-galerkin-solution-unique).

## In one dimension the Galerkin solution is the nodal interpolant

In one dimension the P1 Galerkin solution is the nodal interpolant of the
exact solution: `u_h = I_h u`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.p1_eq_interp_of_isGalerkinSolution`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 700](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L700). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#p1-eq-interp-of-is-galerkin-solution).

## Galerkin orthogonality

`a(u - u_h, v_h) = 0` for every `v_h ∈ V_h`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.galerkin_orthogonality`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 707](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L707). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#galerkin-orthogonality).

## Element-wise energy of a function minus a P1 function

Element-wise form of the energy of `u - p1 d` for a `C²` function `u`:
`a(u - p1 d, u - p1 d) = ∑ᵢ ∫_{xᵢ}^{xᵢ₊₁} (u' - slopeᵢ(d))²`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.energy_sub_p1_self`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 719](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L719). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#energy-sub-p1-self).

## Best approximation

**Best approximation** (Céa's lemma for the symmetric energy form, with
constant `1`): `‖u - u_h‖_a ≤ ‖u - v_h‖_a` for every `v_h ∈ V_h`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.energy_sub_galerkin_le`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 794](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L794). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#energy-sub-galerkin-le).

## Wirtinger's inequality on an interval

Wirtinger's inequality on `[a, b]`: a `C¹` function vanishing at `a` and
`b` satisfies `∫ₐᵇ g² ≤ ((b - a) / π)² ∫ₐᵇ (g')²`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.integral_sq_le_of_eq_zero`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 836](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L836). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#integral-sq-le-of-eq-zero).

## Element estimate for $C^2$ functions vanishing at both ends

The element estimate: a `C²` function vanishing at `a` and `b` satisfies
`∫ₐᵇ (g')² ≤ ((b - a) / π)² ∫ₐᵇ (g'')²`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.integral_deriv_sq_le_of_eq_zero`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 879](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L879). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#integral-deriv-sq-le-of-eq-zero).

## Interpolation estimate

`‖u - I_h u‖_a² ≤ (h / π)² ‖u''‖²_{L²(0,1)}`,
with `h` the mesh size.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.energy_sub_interp_le`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 930](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L930). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#energy-sub-interp-le).

## Energy error estimate

`‖u - u_h‖_a² ≤ (h / π)² ‖f‖²_{L²(0,1)}`, so the
energy error is `O(h)`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.energy_sub_galerkin_le_mesh`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 953](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L953). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#energy-sub-galerkin-le-mesh).

## Energy error estimate for the P1 Galerkin solution

The energy error estimate in norm form:
`‖u - u_h‖_a ≤ (h / π) ‖f‖_{L²(0,1)}`.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.sqrt_energy_sub_galerkin_le_mesh`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 962](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L962). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#sqrt-energy-sub-galerkin-le-mesh).

## `L²` error estimate

`‖u - u_h‖²_{L²(0,1)} ≤ (h / π)⁴ ‖f‖²_{L²(0,1)}`,
so the `L²` error is `O(h²)`. The proof uses nodal exactness and Wirtinger's
inequality on each element, not the Aubin–Nitsche duality argument.

Formalized by `MathlibExt.Analysis.ODE.FiniteElement1D.integral_sq_sub_galerkin_le_mesh`, a theorem declared in [MathlibExt/Analysis/ODE/FiniteElement1D.lean, line 977](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/FiniteElement1D.lean#L977). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html#integral-sq-sub-galerkin-le-mesh).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite element method in one dimension](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/numerical-analysis/finite-element-method-in-one-dimension)
