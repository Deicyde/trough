---
declaration: theorem
origin: cited
lean: Combinatorics.Line.exists_mono_of_shelahBound_le, Combinatorics.Line.shelahBound_lt_ack, Combinatorics.Line.exists_mono_of_ack_le
statement: formalized
proof: formalized
---

# Shelah's bound for the Hales–Jewett numbers

> Proves the Hales–Jewett theorem with Shelah's primitive recursive bound. The proof is by induction on the alphabet; to add a letter it finds a subspace on which the coloring is insensitive to replacing the new letter by an old one, building each dimension of the subspace from a line given by the pigeonhole principle. This gives an explicit recursion shelahBound k r for the dimension, which is proved to be below the fifth level of the Ackermann function, so every r-coloring of the words of length n ≥ A(5, 2k + r) over k ≥ 1 letters has a monochromatic combinatorial line.

*Quoted from the card [LeanPool/projects/shelah-hales-jewett.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/shelah-hales-jewett.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Combinatorics.Line.exists_mono_of_shelahBound_le`](https://leanpool.github.io/lean-pool/LeanPool/ShelahHalesJewett/HalesJewett.html#Combinatorics.Line.exists_mono_of_shelahBound_le) (theorem; a main declaration), declared in [LeanPool/ShelahHalesJewett/HalesJewett.lean, line 190](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ShelahHalesJewett/HalesJewett.lean#L190): “Over a nonempty finite alphabet α, every coloring with κ colors of the words indexed by a finite type ι has a monochromatic combinatorial line when |ι| ≥ shelahBound |α| |κ|.” Its source, as the card gives it: “The Hales–Jewett theorem with Shelah's bound.”
- [`Combinatorics.Subspace.exists_insensitive`](https://leanpool.github.io/lean-pool/LeanPool/ShelahHalesJewett/HalesJewett.html#Combinatorics.Subspace.exists_insensitive) (theorem), declared in [LeanPool/ShelahHalesJewett/HalesJewett.lean, line 65](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ShelahHalesJewett/HalesJewett.lean#L65): “For letters a and b and a finite type η, in a cube of dimension insensitiveBound every coloring has an η-dimensional subspace on which replacing a by b in any coordinates does not change the color.” Its source, as the card gives it: “Shelah's insensitivity lemma.”
- [`Combinatorics.Line.shelahBound_lt_ack`](https://leanpool.github.io/lean-pool/LeanPool/ShelahHalesJewett/Ackermann.html#Combinatorics.Line.shelahBound_lt_ack) (theorem; a main declaration), declared in [LeanPool/ShelahHalesJewett/Ackermann.lean, line 88](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ShelahHalesJewett/Ackermann.lean#L88): “shelahBound k r < A(5, 2k + r), where A is the Ackermann function.”
- [`Combinatorics.Line.exists_mono_of_ack_le`](https://leanpool.github.io/lean-pool/LeanPool/ShelahHalesJewett/Ackermann.html#Combinatorics.Line.exists_mono_of_ack_le) (theorem; a main declaration), declared in [LeanPool/ShelahHalesJewett/Ackermann.lean, line 98](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ShelahHalesJewett/Ackermann.lean#L98): “Over a nonempty finite alphabet of k letters, every coloring with r colors of the words of length n ≥ A(5, 2k + r) has a monochromatic combinatorial line.”

## Project

- Authors: Gabriel Dahia.
- Source: *Primitive recursive bounds for van der Waerden numbers* by Saharon Shelah, [doi:10.1090/S0894-0347-1988-0929498-X](https://doi.org/10.1090/S0894-0347-1988-0929498-X), [https://github.com/gdahia/ShelahHalesJewett/tree/8a91fc0e8a9617f8ade16ccb3b56e543990c9f45](https://github.com/gdahia/ShelahHalesJewett/tree/8a91fc0e8a9617f8ade16ccb3b56e543990c9f45).
- Project repository: [gdahia/ShelahHalesJewett](https://github.com/gdahia/ShelahHalesJewett), at commit [8a91fc0e](https://github.com/gdahia/ShelahHalesJewett/tree/8a91fc0e8a9617f8ade16ccb3b56e543990c9f45).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05D10, 03D20.
- In Lean Pool: [LeanPool/ShelahHalesJewett](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ShelahHalesJewett), from the card [LeanPool/projects/shelah-hales-jewett.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/shelah-hales-jewett.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/shelah-hales-jewett.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/shelah-hales-jewett.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ShelahHalesJewett](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ShelahHalesJewett)
