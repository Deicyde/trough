---
declaration: section
origin: cited
lean: OAI.EntropyPhotonNumber.entropy_photon_number_inequality
statement: formalized
proof: formalized
---

# 273. The entropy photon-number inequality

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the entropy photon-number inequality for beam-splitter mixing of two independent finite-energy bosonic inputs in any finite number of modes: the output's entropy photon number is at least the transmissivity-weighted average of the inputs'. Arbitrary entanglement within each input is allowed, and product thermal inputs attain equality even when their entropies differ.

## The entropy photon-number inequality

We prove the entropy photon-number inequality for two independent bosonic inputs with finite mean energy, for every finite number of modes. This resolves the entropy photon-number conjecture in this finite-energy setting while allowing arbitrary entanglement among the modes within either input. As a consequence, we determine the exact minimum output entropy at fixed input entropy for every finite tensor power of an identical thermal attenuator, over finite-energy inputs that may be entangled across modes. We also obtain the exact classical capacity region of the degraded two-receiver pure-loss bosonic broadcast channel under a mean photon constraint.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-entropy-photon-number-inequality-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves the entropy photon-number inequality for two independent bosonic inputs with finite mean energy and any finite positive number $n$ of modes. Write $N(\rho)=g^{-1}(S(\rho)/n)$, where $S$ is von Neumann entropy and $g(x)=(x+1)\log(x+1)-x\log x$ is the thermal entropy per mode. For a beam splitter of transmissivity $0\le\eta\le1$, its output satisfies $N(\rho_C)\ge\eta N(\rho_A)+(1-\eta)N(\rho_B)$.

Entanglement among modes within either input is allowed. The thermal-attenuator minimum-output-entropy and broadcast-capacity consequences in the paper are outside this selected inequality.

## Lean: Entropy photon-number inequality for finite-energy bosonic inputs

```lean
theorem entropy_photon_number_inequality
    (n : ℕ) (hn : 1 ≤ n) (ρA ρB ρC : State n)
    (hA : FiniteEnergy ρA) (hB : FiniteEnergy ρB)
    (η : ℝ) (hη : η ∈ Set.Icc 0 1)
    (hC : IsBeamSplitterOutput η ρA ρB ρC) :
    η * gInv (entropy ρA / n) + (1 - η) * gInv (entropy ρB / n) ≤
      gInv (entropy ρC / n)
```

Stated in [EntropyPhotonNumber.lean, line 99](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EntropyPhotonNumber.lean#L99). Proved in [lean/OAI/InformationTheory/PhotonNumber/Inequality.lean, line 689](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/InformationTheory/PhotonNumber/Inequality.lean#L689).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/273.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/273.md)
