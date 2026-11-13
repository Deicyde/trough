---
declaration: section
origin: cited
lean: OAI.Heisenberg.spontaneous_magnetization
statement: formalized
proof: formalized
---

# 271. Bloch's law, its lattice correction, and the spherical magnetization law

4 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Bloch's $T^{3/2}$ law with its exact coefficient for three-dimensional quantum Heisenberg ferromagnets at every positive quantum spin, allowing nonnegative symmetric finite-range couplings whose support generates ℤ$^{3}$. The thermodynamic limit precedes the zero-field derivative and low-temperature limit. The family also proves spontaneous magnetization for nearest-neighbor models in every dimension *d* ≥ 3 and determines the first lattice correction for three-dimensional nearest-neighbor couplings.

## Bloch's Law for Finite-Range Heisenberg Ferromagnets in Three Dimensions

We prove Bloch's $T^{3/2}$ law for the spontaneous magnetization of three-dimensional quantum Heisenberg ferromagnets at every fixed positive quantum spin. The result holds for every nonnegative symmetric finite-range interaction whose support generates ℤ$^{3}$, including spatially anisotropic couplings. The leading magnetization deficit has the exact coefficient determined by the determinant of the quadratic one-magnon dispersion. The thermodynamic limit is taken before the right field derivative at zero, and the low-temperature limit is taken last.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/bloch-law-heisenberg.pdf).

## The first lattice correction to Bloch's law

We prove the first lattice correction to Bloch's law for the three-dimensional nearest-neighbor quantum Heisenberg ferromagnet at every fixed spin $S=\tfrac12,1,\tfrac32,\ldots$. The spontaneous-magnetization deficit agrees with the full ideal-magnon density up to $o(\beta^{-5/2})$. In addition to the leading Bloch term, this gives the correction $3\zeta(5/2)(\beta S)^{-5/2}/(128\pi^{3/2})$. The magnetization is the right derivative at zero field of the thermodynamic pressure; the volume limit precedes the field derivative, and the low-temperature limit is taken last.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/first-lattice-correction-bloch-law.pdf).

## The spherical magnetization law for the three-dimensional quantum Heisenberg ferromagnet

We prove the spherical magnetization law for the three-dimensional nearest-neighbor isotropic quantum Heisenberg ferromagnet at every fixed positive quantum spin and every sufficiently low fixed positive temperature. As the even periodic cubes grow, the symmetric zero-field magnetization converges in moments to a uniform direction with a deterministic positive magnitude. This magnitude equals the right derivative at zero field of the infinite-volume pressure. The law is expressed through self-adjoint linear combinations of the spin components and requires no joint measurement of noncommuting observables.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/spherical-magnetization.pdf).

## Spontaneous magnetization in the quantum Heisenberg ferromagnet

For every dimension *d* ≥ 3 and every spin $S\in\{\frac12,1,\frac32,\ldots\}$, we prove that the nearest-neighbor isotropic quantum Heisenberg ferromagnet has a translation-invariant, spontaneously magnetized equilibrium state at every sufficiently low positive temperature. The same state satisfies the KMS condition for the zero-field dynamics and has magnetization at least $S/4$. This resolves the low-temperature ordering problem in the spontaneous-magnetization formulation.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves spontaneous magnetization for the nearest-neighbor isotropic quantum Heisenberg ferromagnet on $\mathbb Z^d$ for every $d\ge3$ and every spin $S\in\{\tfrac12,1,\tfrac32,\ldots\}$. At every sufficiently low positive temperature, it constructs a translation-invariant equilibrium state satisfying the KMS condition for the zero-field dynamics and having magnetization at least $S/4$.

It also proves convergence of the finite-volume dynamics to the infinite-volume dynamics used in the KMS statement.

## Lean: Low-temperature spontaneous magnetization for every positive spin

```lean
theorem spontaneous_magnetization (d ℓ : ℕ) (hd : 3≤d) (hℓ : 1≤ℓ) :
    DynamicsConverges d ℓ ∧
      ∃ β₀ : ℝ,0<β₀ ∧ ∀ β : ℝ,β₀≤β →
        ∃ ω : State d ℓ,TranslationInvariant ω ∧ IsKMS β ω ∧
          (ω.functional (spinZ d ℓ 0)).im=0 ∧
          (ℓ:ℝ)/8≤(ω.functional (spinZ d ℓ 0)).re
```

Stated in [Heisenberg.lean, line 206](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Heisenberg.lean#L206). Proved in [lean/OAI/MathematicalPhysics/Heisenberg/Main.lean, line 60](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Heisenberg/Main.lean#L60).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/271.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/271.md)
