---
declaration: section
origin: cited
lean: OAI.CoulombAtom.generalized_ionization, OAI.NeutralAtom.generalized_outer_radii
statement: formalized
proof: formalized
---

# 263. The ionization and generalized ionization conjectures

3 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For the full nonrelativistic Coulomb model with two electron spin states, proves that a molecule with *M* fixed nuclei of charges at least one and total charge *Z* strictly binds at most $Z+CM$ electrons. Neutral-atom first ionization energies and radii containing all but an expected half-electron have universal positive upper and lower bounds. The energy cost of removing *m* electrons has Thomas–Fermi asymptotics as $m\to\infty$ and $Z/m\to\infty$; neutral-atom outer radii have the corresponding iterated-limit asymptotics, taking $Z\to\infty$ first.

## Uniform excess charge for Coulomb molecules and the outer radius of neutral atoms

We prove that a molecule with *M* fixed nuclei of real charges at least one and total nuclear charge *Z* strictly binds at most $Z+CM$ electrons, where *C* is universal. The result holds for the full nonrelativistic Coulomb Hamiltonian with two spin states and arbitrary distinct nuclear positions. For neutral atoms with integer nuclear charge *Z* ≥ 1, the first ionization energy and, for every ground state, the radius outside which one half of an electron remains are each bounded above and below by positive universal constants.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf).

## Generalized ionization energies for full Coulomb atoms

We prove the energy part of the generalized ionization conjecture for full nonrelativistic Coulomb atoms with two electron spin states. The energy needed to remove *m* electrons is asymptotic to $a_{\mathrm{TF}}m^{7/3}$ whenever $m\to\infty$ and $Z/m\to\infty$, with the Thomas–Fermi constant in atomic units. We also obtain both conjectured iterated limits.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## Generalized outer-electron radii of neutral Coulomb atoms

We prove the radius part of the generalized ionization conjecture for neutral nonrelativistic Coulomb atoms with two spin states. For every choice of ground states, the upper and lower large-nuclear-charge limits of the radius defined by an expected exterior electron mass *m* are both asymptotic to $(81\pi^2/2)^{1/3}m^{-1/3}$ as *m* tends to infinity.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Generalized-outer-electron-radii-of-neutral-Coulomb-atoms-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization gives the large-ionization asymptotics for the full nonrelativistic two-spin Coulomb atom. Let $I_m(Z)$ be the energy needed to remove $m$ electrons from a neutral atom of nuclear charge $Z$. There is a positive coefficient $a_{\mathrm{TF}}$ with the Thomas–Fermi variational characterization such that $I_m(Z)/m^{7/3}\to a_{\mathrm{TF}}$ whenever $m\to\infty$ and $Z/m\to\infty$, with integers $Z>m\ge1$. The corresponding iterated limsup and liminf limits hold with $Z\to\infty$ first. The energy uses the full antisymmetric Sobolev form domain; fixed-$m$ convergence and ground-state attainment are outside this statement.

For neutral Coulomb atoms with two electron spin states, the formalization proves the asymptotic law for generalized outer-electron radii defined by an expected exterior electron mass $m$. For every choice of normalized ground states, both the upper and lower large-nuclear-charge radius limits satisfy
$m^{1/3}R_m\longrightarrow (81\pi^2/2)^{1/3}$ as $m\to\infty$. The large-nuclear-charge limit is taken first. Ground states are inputs to the statement; their existence is not asserted separately.

## Lean: Generalized Coulomb ionization-energy asymptotics

Stated in [CoulombIonization.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CoulombIonization.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem generalized_ionization : MainStatement
```

Proved in [lean/OAI/Analysis/CoulombIonization/Main.lean, line 46](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/CoulombIonization/Main.lean#L46).

## Lean: Asymptotic outer-electron radii of neutral atoms

Stated in [CoulombRadii.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CoulombRadii.lean).

```lean
theorem generalized_outer_radii
    (Ψ : ∀ N : ℕ, Wavefunction (N + 1))
    (hΨ : ∀ N : ℕ, IsNormalizedGroundState (N + 1) (Ψ N)) :
    Tendsto (fun m : ℕ => (((m : ℝ) ^ (1 / 3 : ℝ) : ℝ) : EReal) * upperRadius Ψ m)
      atTop (𝓝 (bTF : EReal)) ∧
    Tendsto (fun m : ℕ => (((m : ℝ) ^ (1 / 3 : ℝ) : ℝ) : EReal) * lowerRadius Ψ m)
      atTop (𝓝 (bTF : EReal))
```

Proved in [lean/OAI/Analysis/CoulombRadii/Main.lean, line 15](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/CoulombRadii/Main.lean#L15).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/263.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/263.md)
