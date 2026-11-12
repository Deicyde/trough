---
declaration: section
origin: cited
lean: OAI.AtomicTriangular.sharp_gaussian_minorants_atomic, OAI.AtomicTriangular.universal_energy_minimum, OAI.AtomicTriangular.sharp_gaussian_minorants_with_construction, OAI.sharp_fourier_certificate
statement: formalized
proof: formalized
---

# 090. Triangular-lattice optimality, long-range Riesz and Coulomb energies, and spherical logarithmic energy

4 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that the triangular lattice minimizes the lower limit of energy per particle for every nonnegative completely monotone potential of squared distance among locally finite planar configurations of centered-disk density one. It also minimizes unit-background renormalized Riesz energies for $0\lt s\lt 2$ and Coulomb energy, resolving Sandier–Serfaty and the two-dimensional Brauchart–Hardin–Saff conjecture on the linear term of optimal spherical logarithmic energy.

## An atomic certificate for triangular-lattice universal optimality

We prove that the density-one triangular lattice minimizes the lower energy per particle for every nonnegative completely monotone function of squared distance, among all locally finite planar configurations of centered disk density one. The comparison includes infinite energies. The proof constructs sharp Gaussian Fourier minorants using an atomic interpolation certificate.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/paper.pdf); the Lean below formalizes results from it.

## Universal optimality of the triangular lattice

We prove universal energy minimality for the triangular lattice in the plane. Among locally finite configurations of centered density one, it minimizes the lower limit of centered-ball energy averages for every nonnegative completely monotone function of squared distance, including when the energy is infinite. We also prove triangular minimality for planar logarithmic and Riesz renormalized energies, with $0\lt s\lt 2$ in the Riesz case, and the corresponding jellium minima. The proof uses sharp Gaussian Fourier bounds, positive mixtures, and heat-kernel comparison.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026/paper.pdf).

## A sharp Fourier certificate for planar circle packing

We resolve the planar Cohn–Elkies sharpness conjecture: the two-point Fourier bound attains the optimal circle-packing density $\pi/(2\sqrt3)$. We construct a radial Schwartz certificate and prove its global sign conditions using rigorous interval arithmetic and analytic estimates. The same certificate recovers the classical uniqueness of the triangular packing among periodic equality cases.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-sharp-Fourier-certificate-for-planar-circle-packing-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Triangular minimality for planar Coulomb renormalized energy

We prove the Sandier–Serfaty conjecture: the triangular lattice of covolume one minimizes planar Coulomb renormalized energy over all admissible curl-free fields with a unit uniform background. Combined with Bétermin and Sandier's asymptotic formula, this also proves the Brauchart–Hardin–Saff conjecture for the linear term of optimal ordered-pair logarithmic energy on the unit two-sphere. The proof uses a direct Voronoi-cell comparison with rigorous interval arithmetic.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/paper.pdf).

## The Lean formalization

The formalization proves that the density-one triangular lattice minimizes lower energy per particle among all locally finite planar configurations of centered-disk density one, for every nonnegative completely monotone function of squared distance. Infinite energies are allowed in the comparison.

It also constructs sharp radial Schwartz minorants for every Gaussian potential: each minorant lies below the Gaussian, has nonnegative real Fourier transform, agrees with the Gaussian at nonzero triangular-lattice points, and vanishes on nonzero dual-lattice points after Fourier transformation. For the stated parameter range, the formalization includes the explicit atomic interpolation construction.

The planar Cohn–Elkies sharpness conjecture asks whether the two-point Fourier method attains the optimal circle-packing density. The formalization constructs a radial Schwartz function $f$ on $\mathbb R^2$ with $\widehat f(0)=1$, $f(0)=2/\sqrt3$, $\widehat f$ real and nonnegative everywhere, and $f(x)\le0$ whenever $\|x\|\ge1$. These are the sharp Fourier certificate conditions yielding density $\pi/(2\sqrt3)$. The separate uniqueness statement for periodic equality cases is outside this selected theorem.

## Lean: Sharp Gaussian minorants from an atomic certificate

Stated in [AtomicGaussian.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/AtomicGaussian.lean).

```lean
theorem sharp_gaussian_minorants_atomic (α : ℝ) (hα : 0 < α) :
    ∃ f : SchwartzMap Plane ℝ,
      Radial f ∧ (∀ x, f x ≤ gaussian α x) ∧
      (∀ w, (realFourier f w).im = 0 ∧ 0 ≤ (realFourier f w).re) ∧
      (∀ a ∈ A, a ≠ 0 → f a = gaussian α a) ∧
      (∀ w ∈ dualA, w ≠ 0 → realFourier f w = 0) ∧
      (1 ≤ α → Construction.HasAtomicConstruction α f)
```

Proved in [lean/OAI/Analysis/Triangular/Main.lean, line 75](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Triangular/Main.lean#L75).

## Lean: Universal energy minimality of the triangular lattice

Stated in [TriangularEnergy.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TriangularEnergy.lean).

```lean
theorem universal_energy_minimum (g : ℝ → ℝ) (C : Set Plane)
    (hg : AdmissiblePotential g) (hC : LocallyFinite C) (hd : DensityOne C) :
    latticeEnergy g ≤ energy g C ∧ latticeEnergy g = energy g A
```

Proved in [lean/OAI/Analysis/Triangular/Energy/Universal.lean, line 9](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Triangular/Energy/Universal.lean#L9).

## Lean: Gaussian Fourier minorants with their construction

Stated in [TriangularGaussian.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TriangularGaussian.lean).

```lean
theorem sharp_gaussian_minorants_with_construction (α : ℝ) (hα : 0 < α) :
    ∃ f : SchwartzMap Plane ℝ,
      Radial f ∧ (∀ x, f x ≤ gaussian α x) ∧
      (∀ w, (realFourier f w).im = 0 ∧ 0 ≤ (realFourier f w).re) ∧
      (∀ a ∈ A, a ≠ 0 → f a = gaussian α a) ∧
      (∀ w ∈ dualA, w ≠ 0 → realFourier f w = 0) ∧
      (1 ≤ α → AtomicConstruction α f)
```

Proved in [lean/OAI/Analysis/Triangular/GaussianMinorants.lean, line 73](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Triangular/GaussianMinorants.lean#L73).

## Lean: Sharp Fourier certificate for planar circle packing

Stated in [PlanarPacking.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PlanarPacking.lean).

```lean
theorem sharp_fourier_certificate :
    ∃ f : SchwartzMap SharpPlanar.Plane ℝ, SharpPlanar.SharpCertificate f
```

Proved in [lean/OAI/Analysis/PlanarPacking/Main.lean, line 32](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/PlanarPacking/Main.lean#L32).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/090.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/090.md)
