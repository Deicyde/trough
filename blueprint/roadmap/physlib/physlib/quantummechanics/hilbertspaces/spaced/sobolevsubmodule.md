---
declaration: module
origin: cited
lean: QuantumMechanics.SpaceDHilbertSpace.SobolevSubmodule, QuantumMechanics.SpaceDHilbertSpace.mem_sobolevSubmodule_iff, QuantumMechanics.SpaceDHilbertSpace.SobolevSubmodule.schwartzIncl_mem, QuantumMechanics.SpaceDHilbertSpace.schwartzSubmodule_le_sobolevSubmodule, QuantumMechanics.SpaceDHilbertSpace.SobolevSubmodule.dense, QuantumMechanics.SpaceDHilbertSpace.SobolevSubmodule.antitone
statement: formalized
proof: formalized
---

# Sobolev submodules of `SpaceDHilbertSpace`

The module `Physlib.QuantumMechanics.HilbertSpaces.SpaceD.SobolevSubmodule`, [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SobolevSubmodule.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SobolevSubmodule.lean): 6 declarations, 6 with a docstring.

## i. Overview

> In this module we define the Sobolev submodules of `SpaceDHilbertSpace`.

## ii. Key results

> - `SobolevSubmodule d s` : the Sobolev space `H^s` as a submodule of `SpaceDHilbertSpace d`.
> - `SobolevSubmodule.schwartzIncl_mem` / `schwartzSubmodule_le_sobolevSubmodule` /
>     `SobolevSubmodule.dense` : Schwartz maps lie in every `H^s`, which is therefore dense.
> - `SobolevSubmodule.antitone` : `H^s ≤ H^s'` for `s' ≤ s`.

## iv. References

> * None.

## A. The Sobolev submodule `H^s`

**`QuantumMechanics.SpaceDHilbertSpace.SobolevSubmodule`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SobolevSubmodule.lean#L50).

> The Sobolev space `H^s` as a submodule of `SpaceDHilbertSpace d`: the L² classes whose
> associated tempered distribution satisfies `MemSobolev s 2`.

```lean
def SobolevSubmodule (d : ℕ) (s : ℝ) : Submodule ℂ (SpaceDHilbertSpace d)
```

**`QuantumMechanics.SpaceDHilbertSpace.mem_sobolevSubmodule_iff`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SobolevSubmodule.lean#L57).

> Membership in `H^s` is the Sobolev condition on the associated tempered distribution.

```lean
lemma mem_sobolevSubmodule_iff {s : ℝ} {ψ : SpaceDHilbertSpace d} :
    ψ ∈ SobolevSubmodule d s ↔ MemSobolev s 2 (toTemperedDistribution ψ)
```

**`QuantumMechanics.SpaceDHilbertSpace.SobolevSubmodule.schwartzIncl_mem`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SobolevSubmodule.lean#L61).

> Schwartz maps lie in every Sobolev space `H^s`.

```lean
lemma SobolevSubmodule.schwartzIncl_mem (s : ℝ) (g : 𝓢(Space d, ℂ)) :
    schwartzIncl volume g ∈ SobolevSubmodule d s
```

**`QuantumMechanics.SpaceDHilbertSpace.schwartzSubmodule_le_sobolevSubmodule`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SobolevSubmodule.lean#L67).

> The Schwartz submodule is contained in every Sobolev space `H^s`.

```lean
lemma schwartzSubmodule_le_sobolevSubmodule (s : ℝ) :
    SchwartzSubmodule d ≤ SobolevSubmodule d s
```

**`QuantumMechanics.SpaceDHilbertSpace.SobolevSubmodule.dense`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SobolevSubmodule.lean#L74).

> Every Sobolev space `H^s` is dense in `SpaceDHilbertSpace d`, containing the dense Schwartz
> submodule.

```lean
lemma SobolevSubmodule.dense (s : ℝ) :
    Dense (SobolevSubmodule d s : Set (SpaceDHilbertSpace d))
```

**`QuantumMechanics.SpaceDHilbertSpace.SobolevSubmodule.antitone`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SobolevSubmodule.lean#L79).

> The Sobolev spaces shrink as the regularity index grows: `H^s ≤ H^s'` for `s' ≤ s`.

```lean
lemma SobolevSubmodule.antitone (d : ℕ) : Antitone (SobolevSubmodule d)
```

## Depends on

- [Schwartz submodule](schwartzsubmodule.md)

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SobolevSubmodule.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SobolevSubmodule.lean)
