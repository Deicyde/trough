---
declaration: section
origin: cited
lean: OAI.LaughlinGap.thm_main, OAI.Laughlin.mainTarget_proved, OAI.LaughlinFock.thm_fock, OAI.Laughlin.planar_gap
statement: formalized
proof: formalized
---

# 269. Uniform Laughlin gap and stability under bounded scalar disorder

2 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the fermionic Laughlin spectral-gap conjecture for the full $V_{1}$ interaction at filling 1/3 on the round sphere. The unique ground state remains uniformly gapped under sufficiently weak bounded real scalar one-body potentials projected to the lowest Landau level. Both the gap and disorder threshold are uniform over all sufficiently large particle numbers and all normalized potential profiles.

## Uniform Stability of the Spherical Laughlin Gap

We prove that the fermionic Laughlin $V_{1}$ Hamiltonian at filling 1/3 on expanding round spheres retains a unique ground state and a uniform spectral gap under sufficiently weak bounded real scalar one-body potentials projected to the lowest Landau level. With coefficient one for each pair projector and Laughlin flux $q=3(N-1)$, the gap and perturbation threshold are uniform for all sufficiently large particle numbers and all potential profiles of supremum norm at most one. The result uses the uniform unperturbed Fock-space gap and gives existential constants.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/uniform-stability-spherical-laughlin-gap.pdf); the Lean below formalizes results from it.

## A Fock-space inequality and the Laughlin spectral gap

We prove the spherical fermionic Laughlin spectral-gap conjecture for the full $V_{1}$ interaction. With coefficient one for each pair projector, the gap above the Laughlin state at filling 1/3 on the round sphere is at least 1/25 for all sufficiently large systems. More generally, $H_Q^2\ge\gamma H_Q$ for some fixed $\gamma\gt 1/25$ on the entire lowest-Landau-level Fock space for all sufficiently large flux *Q*, independently of particle number.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The linked formalization proves the uniform unperturbed gap estimate used in the paper's stability argument for the fermionic Laughlin state at filling $1/3$ on the sphere. At flux $q=3(N-1)$ and all sufficiently large particle numbers $N$, every antisymmetric state has $V_1$ energy at least $1/25$ times its squared distance from the Laughlin ground-state line.

This selected statement is the unperturbed Fock-space inequality. Stability under projected one-body potentials and uniqueness of the perturbed ground state are outside it.

The Laughlin spectral-gap problem asks for a positive gap that remains uniform as the system grows. The formalization includes the finite spherical $V_1$ bound of $1/100$ above the Laughlin state at flux $3(N-1)$ for all sufficiently large particle numbers $N$. It also proves the stronger Fock-space inequality $H_Q^2\ge\gamma H_Q$ for every fixed $0<\gamma<\gamma_*$ and all sufficiently large fluxes $Q$, independently of particle number, where $\gamma_*=4616733319001/10^{14}>1/25$.

For the untruncated planar model, the formalization proves the corresponding inequality at the endpoint $\gamma_*$ on every homogeneous particle sector. These statements use coefficient one for each pair projector.

## Lean: Uniform unperturbed spherical Laughlin gap inequality

Stated in [LaughlinGap.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LaughlinGap.lean).

```lean
theorem thm_main : MainTarget
```

Proved in [lean/OAI/Analysis/LaughlinGap/Main.lean, line 57](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/LaughlinGap/Main.lean#L57).

## Lean: Uniform Laughlin $V_1$ spectral gap

Stated in [Laughlin.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Laughlin.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem mainTarget_proved : MainTarget
```

Proved in [lean/OAI/Analysis/Laughlin/Main.lean, line 19](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Laughlin/Main.lean#L19).

## Lean: Uniform Fock-space spectral-gap inequality

Stated in [LaughlinFock.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LaughlinFock.lean).

```lean
theorem thm_fock (γ : ℝ) (hγ : 0 < γ) (hγStar : γ < gammaStar) :
    ∃ Qγ : ℤ, 1 ≤ Qγ ∧ ∀ Q : ℤ, Qγ ≤ Q → FockInequality Q.toNat γ
```

Proved in [lean/OAI/Analysis/LaughlinFock/Main.lean, line 69](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/LaughlinFock/Main.lean#L69).

## Lean: Planar spectral-gap inequality

Stated in [LaughlinPlanar.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LaughlinPlanar.lean).

```lean
theorem planar_gap {N : ℕ} (ψ : Planar.HomogeneousState N) :
    ENNReal.ofReal gammaStar * Planar.fullEnergy ψ ≤ Planar.fullSquareNorm ψ
```

Proved in [lean/OAI/Analysis/Laughlin/UniformGap.lean, line 29](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Laughlin/UniformGap.lean#L29).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/269.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/269.md)
