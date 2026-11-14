# FLRW

The folder [Physlib/Cosmology/FLRW/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW): 13 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *FLRW cosmology* ([Physlib/Cosmology/FLRW/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Geometry and the FLRW model
>
> The constant-time slices have one of three spatial geometries, spherical, flat or saddle, with metric profile giving the transverse radius k sin(r/k), r, or k sinh(r/k) in the three cases. [\[1\]](basic.md) The flat geometry is the large-radius limit of the curved ones: the profiles of the spherical and saddle geometries tend to the flat profile as the curvature radius tends to infinity. [\[2\]](basic.md)
>
> An FLRW model is a scale factor, positive and twice differentiable on an open interval of cosmic time \{1}, together with a spatial geometry. [\[3\]](basic.md) The spatial geometry supplies the curvature parameter of the Friedmann equations, positive for the spherical geometry, zero for the flat one and negative for the saddle one. [\[3\]](basic.md) (For the Robertson–Walker metric see Weinberg \{2} and Baumann \{3}.)
>
> ### The Friedmann equations
>
> The first-order Friedmann equation (∂ₜ a / a)² = (8πG/3) ρ − k c² / a² + Λ c² / 3 relates a scale factor and an energy density, with the curvature parameter explicit; the second-order Friedmann equation ∂ₜ ∂ₜ a / a = −(4πG/3) (ρ + 3 p / c²) + Λ c² / 3 involves a pressure as well and has no curvature term. The cosmological constant, Newton's constant and the speed of light appear explicitly in both; the speed of light is positive by construction, so no result needs a hypothesis on it. [\[8\]](basic.md)
>
> A cosmic fluid is an energy density and a pressure, each a function of cosmic time; the empty fluid has zero density and pressure. [\[4\]](basic.md) A model filled with a fluid solves the Friedmann equations when both hold on the interval of the model, the curvature parameter being read off the spatial geometry. [\[4\]](basic.md) Every such solution satisfies the continuity equation [\[5\]](mattercontent.md) and the closure relation of the density parameters. \[6\] The de Sitter model at all times, and the Milne model after its Big Bang, each filled with the empty fluid, solve the Friedmann equations. [\[17\]](desitter.md)[\[7\]](solutions.md) The flat power-law models, filled with their fluid, solve the Friedmann equations on t > 0 for the matching equation of state. [\[25\]](specificcases-powerlaw.md) The radiation-dominated and Einstein–de Sitter models are the cases n = 1/2 and n = 2/3, and after their Big Bang they too solve the Friedmann equations. [\[26\]](specificcases-radiationdominated.md)[\[27\]](specificcases-einsteindesitter.md)
>
> ### Hubble and deceleration parameters
>
> The Hubble parameter H = ∂ₜ a / a is a function of the scale factor and cosmic time, and is nonzero wherever the scale factor and its derivative both are. [\[9\]](basic.md) The deceleration parameter is q = −(∂ₜ ∂ₜ a) a / (∂ₜ a)². The derivative ∂ₜ H obeys the quotient-rule formula, q equals −(1 + (∂ₜ H) / H²) and ∂ₜ H equals −H² (1 + q), and ∂ₜ H < 0 holds exactly when q > −1, both pointwise and in existential form. [\[10\]](basic.md)
>
> ### Matter content
>
> The continuity equation ∂ₜ ρ + 3 H (ρ + P/c²) = 0 of the cosmic fluid holds at an instant whenever the first-order Friedmann equation holds throughout a neighbourhood of that instant together with the second-order equation; conversely, the second-order equation follows from the first-order equation and the continuity equation wherever the scale factor is changing. [\[11\]](mattercontent.md) (See Dodelson and Schmidt \{4} for the smooth, expanding universe.)
>
> Under the barotropic equation of state P = w ρ c², the continuity equation implies the density scaling law ρ t = ρ t₀ (a t / a t₀)^(−3(1+w)), and conversely; dust, radiation and vacuum energy are special cases. [\[12\]](mattercontent.md) The cosmological constant is itself a fluid, with density ρ\_Λ = Λ c² / (8πG) and pressure p\_Λ = −ρ\_Λ c², and folding it into the cosmic fluid gives the fluid with density ρ + ρ\_Λ and pressure p + p\_Λ. [\[18\]](basic.md) Each Friedmann equation with a cosmological constant is equivalent to the same equation without one for the combined fluid, and that pressure is the w = −1 barotropic pressure of that density. [\[13\]](mattercontent.md) Hence a solution of the Friedmann equations with Λ is a solution without Λ for the combined fluid. [\[19\]](friedmannsolution.md)
>
> ### Density parameters, the standard model and the age
>
> The critical density of an FLRW model is ρ\_cr = 3 H² / (8πG), and the density parameters are Ω = ρ / ρ\_cr for a cosmic fluid in the model, Ω\_K = −k c² / (H² a²), k being the curvature parameter of its spatial geometry, and Ω\_Λ = Λ c² / (3 H²), the density parameter of the cosmological constant as a fluid; folding the cosmological constant into the fluid adds Ω\_Λ to its density parameter. [\[14\]](densityparameters.md) For a solution of the Friedmann equations, the first-order equation is the closure relation Ω + Ω\_Λ + Ω\_K = 1 at the times of its interval at which H ≠ 0. \[6\]
>
> The standard cosmological model has reduced Hubble function E(x)² = Ω\_Λ + Ω\_m x⁻³ + Ω\_r x⁻⁴ + Ω\_K x⁻², with H = H₀ E(a / a₀) for a solution of the Friedmann equations whose cosmic fluid is made of matter and radiation obeying their scaling laws between two times of its interval, and with radiation–matter and matter–Λ equality scale factors. [\[15\]](reducedhubble.md) The age of the universe is t₀ = H₀⁻¹ ∫₀¹ dx / (x E(x)). [\[16\]](age.md)
>
> ### Energy conditions and acceleration
>
> The null, weak, strong and dominant energy conditions of the cosmic fluid are defined, with the implications between them: the dominant condition implies the weak one, and the weak and strong conditions each imply the null one. [\[20\]](energyconditions.md) On the interval of a solution of the Friedmann equations the universe accelerates, 0 < ∂ₜ ∂ₜ a, exactly when ρ + 3 p / c² < 0, without and with Λ; and the deceleration parameter is q = ½ Σ\_i Ω\_i (1 + 3 w\_i) in terms of the density parameters of barotropic components, with its ΛCDM special case. \[21\]
>
> ### Eternal expansion and the Big Bang
>
> An FLRW model that decelerates on its interval and is expanding at t₀ lies below its tangent line at t₀, so it cannot be defined earlier than t₀ − 1 / H(t₀) and its interval is bounded below. [\[22\]](basic.md) On the interval of a solution, for a spatial geometry of non-positive curvature, 0 ≤ Λ and positive density, the expansion never stops; with 0 ≤ ρ, 0 ≤ p and Λ = 0 the solution decelerates, so it has a Big Bang in the finite past. [\[23\]](friedmannsolution.md) The de Sitter model, by contrast, is defined at all times. [\[24\]](desitter.md)
>
> ### Distances, redshift and horizons
>
> The distances are defined for an FLRW model, at the times of its interval. The comoving distance of a source emitting at t and observed at t₀ is χ = c ∫ dτ / a from t to t₀, so that ∂ₜ χ = −c / a. The redshift is 1 + z = a(t₀) / a(t), with ∂ₜ z = −(1 + z) H, and ∂ₜ a = a H; combining the two, ∂ₜ χ = (c / (a(t₀) H)) ∂ₜ z, the change of variables dχ = c dz / H for a(t₀) = 1. The proper distance D = a χ obeys the Hubble–Lemaître law ∂ₜ D = H D, and the recession velocity ∂ₜ D equals c exactly at the Hubble radius R\_H = c / H. [\[28\]](distances.md) The transverse comoving distance r(χ) is the profile of the spatial geometry of the model. With K its curvature parameter and curvature radius 1 / √|K|, it is (1 / √K) sin(√K χ), χ or (1 / √(−K)) sinh(√(−K) χ) for positive, zero or negative K. The particle and event horizons at t integrate c / a over the times of the interval before and after t, and the particle horizon of the Einstein–de Sitter model is 3 c t₀^(2/3) t^(1/3). [\[29\]](distances.md)

Its references:

> - \{1\} Time API map — [Physlib/SpaceAndTime/Time/API-map.md](../../spaceandtime/time/README.md)
> - \{2\} S. Weinberg, *Cosmology*, Oxford University Press (2008), Chapter 1.
> - \{3\} D. Baumann, *Cosmology*, Cambridge University Press (2022), Chapter 2.
> - \{4\} S. Dodelson and F. Schmidt, *Modern Cosmology*, 2nd ed., Chapter 2.

- [The Friedmann-Lemaître-Robertson-Walker metric](basic.md)
- [The age of the universe](age.md)
- [Density parameters and the closure relation](densityparameters.md)
- [The de Sitter solution of the Friedmann equations](desitter.md)
- [Distances and redshift in FLRW cosmology](distances.md)
- [Energy conditions of the cosmic fluid](energyconditions.md)
- [Solutions of the Friedmann equations: dynamical criteria](friedmannsolution.md)
- [Matter content of FLRW cosmology](mattercontent.md)
- [The reduced Hubble function of the standard cosmological model](reducedhubble.md)
- [Exact solutions of the Friedmann equations](solutions.md)

Modules in [SpecificCases/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases):

- [The Einstein-de Sitter model](specificcases-einsteindesitter.md)
- [The flat power-law models](specificcases-powerlaw.md)
- [The radiation-dominated model](specificcases-radiationdominated.md)
