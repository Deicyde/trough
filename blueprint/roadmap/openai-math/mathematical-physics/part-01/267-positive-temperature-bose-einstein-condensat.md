---
declaration: section
origin: cited
lean: OAI.HardSphere.condensation_with_mixed
statement: formalized
---

# 267. Positive-temperature Bose–Einstein condensation and exact quantum depletion

5 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Bose–Einstein condensation for the exact canonical Gibbs state of the three-dimensional hard-sphere gas: each fixed exclusion distance and sufficiently small fixed density admit a strictly positive temperature, independent of volume, with positive condensate fraction in the thermodynamic limit. At zero temperature, proves the Bogoliubov leading quantum-depletion law for hard spheres and fixed bounded nonnegative radial finite-range potentials of positive scattering length, taking the thermodynamic limit before the dilute limit.

## Bose–Einstein condensation at positive temperature in the dilute hard-sphere gas

We prove Bose–Einstein condensation at positive temperature in the three-dimensional dilute hard-sphere gas. For each fixed exclusion distance and every sufficiently small fixed density, there is a strictly positive temperature, independent of the volume, at which the exact canonical Gibbs state has a positive condensate fraction in the thermodynamic limit. The condensate occupies the constant orbital.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/positive-temperature-hard-spheres.pdf).

## Quantum Depletion and Momentum Distribution in the Dilute Hard-Sphere Bose Gas

We prove the full scaled Bogoliubov momentum distribution for the depleted particles in the three-dimensional hard-sphere Bose gas at zero temperature. The thermodynamic limit is taken at each fixed density before the dilute limit, uniformly over all pure and mixed ground states. All thermodynamic accumulation values have the same dilute asymptotic: the limiting nonzero-momentum occupation measure has total mass $8/(3\sqrt\pi)$, giving the depletion fraction $\frac{8}{3\sqrt\pi}\sqrt{\rho a^3}+o(\sqrt{\rho a^3})$ for density *ρ* and hard-sphere exclusion distance *a*.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026/Quantum-Depletion-in-the-Dilute-Hard-Sphere-Bose-Gas.pdf).

## Quantum Depletion for Fixed Bounded Repulsive Potentials

We prove the Bogoliubov quantum-depletion asymptotic for the ground state of a three-dimensional Bose gas with a fixed bounded, nonnegative, radial interaction of finite range and positive scattering length *a*. The thermodynamic limit is taken at each fixed density *ρ* before the dilute limit. Every thermodynamic accumulation value of the fraction outside the constant mode is $\frac{8}{3\sqrt\pi}\sqrt{\rho a^3}+o(\sqrt{\rho a^3})$ as $\rho\downarrow0$. The assertion is uniform over ground-state density matrices and does not require the occupation to have a unique thermodynamic limit.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Quantum-Depletion-for-Fixed-Bounded-Repulsive-Potentials-October-5-2026/fixed-repulsion-quantum-depletion.pdf).

## A density-uniform condensate bound for dilute Bose gases

For each fixed bounded measurable, nonnegative, radial interaction of finite range in three dimensions that is not zero almost everywhere, we prove a positive lower bound on the constant-orbital condensate fraction that is uniform over all sufficiently small densities and all temperatures between zero and the square of the density. The interaction and density remain fixed in the thermodynamic limit.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026/paper.pdf).

## Ground-state condensation in the dilute hard-sphere gas

We prove Bose–Einstein condensation in every ground state of a dilute three-dimensional hard-sphere Bose gas. At every sufficiently small fixed gas parameter, the constant orbital contains a positive fraction of the particles in the thermodynamic limit. The fraction can be chosen independently of the gas parameter, and the conclusion holds for arbitrary complex ground states.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves ground-state Bose–Einstein condensation in the dilute hard-sphere gas. There are absolute constants $\varepsilon_0,c_0>0$ such that, whenever the density $\rho$ and hard-sphere radius $a$ satisfy $\rho a^3<\varepsilon_0$, the condensate occupation fraction has limit inferior at least $c_0$ along every thermodynamic sequence with $N/L^3\to\rho$.

The bound covers every pure ground state, every mixed state supported on the ground space, and the normalized ground-space projection. It is uniform in the gas parameter within this range and concerns ground states, without a positive-temperature assertion.

## Lean: Uniform ground-state condensation in the dilute hard-sphere gas

```lean
theorem condensation_with_mixed :
    ∃ε₀ c₀ : ℝ,0<ε₀ ∧ 0<c₀ ∧
    ∀a ρ : ℝ,0<a → 0<ρ → ρ*a^3<ε₀ →
    ∀(N : ℕ→ℕ) (L : ℕ→Length) (hN : ∀k,0<N k),
      Tendsto N atTop atTop → Tendsto (fun k ↦ (L k).val) atTop atTop →
      Tendsto (fun k ↦ (N k:ℝ)/(L k).val^3) atTop (𝓝 ρ) →
      (∀Ψ : (k : ℕ)→Jet (N k) (L k),
        (∀k,IsGroundVector (N k) (L k) a (Ψ k)) →
        c₀≤liminf (fun k ↦ occupation (hN k) (Ψ k).1) atTop) ∧
      (∀T : (k : ℕ)→Density.Operator (ScalarL2 (N k) (L k)),
        (∀k,GroundSupported a (T k)) →
        c₀≤liminf (fun k ↦ mixedOccupation (hN k) (T k)) atTop)
```

Stated in [HardSphere.lean, line 372](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HardSphere.lean#L372). Its proof is in [lean/OAI/Analysis/HardSphere/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/HardSphere/Main.lean) or a file it imports further down, which this chapter does not read.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/267.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/267.md)
